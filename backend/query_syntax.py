"""
Pure query syntax parser for power-user search operators.

This module provides a bounded, SQL-injection-safe parser for legal research
queries. It supports Boolean operators (AND/OR/NOT), leading minus (NOT variant),
and field operators (court:, year:, judge:, cites:, outcome:) with graceful
degradation for unknown operators and malformed input.

The parser is pure: it performs no database access, network calls, or credential
access. It returns a structured AST and a plain-language echo of the parsed query.

Public API:
    parse_query(query_str: str) -> QueryResult

QueryResult structure:
    {
        "raw_query": str,
        "terms": [str, ...],                    # Plain text search terms
        "filters": {
            "court": [str, ...],                # Exact court values (case preserved)
            "year": [int | (int, int), ...],    # Year values or (min, max) ranges
            "judge": [str, ...],                # Judge names (case preserved)
            "cites": [str, ...],                # Citation values (case preserved)
            "outcome": [str, ...],              # Outcome values (validated against allowlist)
        },
        "boolean_ops": {
            "and_terms": [str, ...],            # Terms that must appear (explicit AND)
            "or_terms": [str, ...],             # Terms that should appear (explicit OR)
            "not_terms": [str, ...],            # Terms to exclude (NOT or leading minus)
        },
        "expression": <AST>,                    # Structured Boolean expression tree
        "echo": str,                            # Plain-language reconstruction
        "unknown_ops": [str, ...],              # Unknown operators found and treated as words
        "issues": [str, ...],                   # Warnings: unbalanced quotes, etc.
    }

Expression AST structure:
    - Atom: {"type": "atom", "kind": "term"|"field", "value": str, "field_name": str|None}
    - AND: {"type": "and", "operands": [expr, ...]}
    - OR: {"type": "or", "operands": [expr, ...]}
    - NOT: {"type": "not", "operand": expr}

Operator syntax:
    - Boolean operators: AND, OR, NOT (case-insensitive)
    - Leading minus: -term (equivalent to NOT term)
    - Field operators: court:value, year:value, year:min..max or year:min-max, judge:value,
                       cites:"quoted" or cites:unquoted, outcome:allowed-value
    - Quoted phrases: "phrase with spaces" (handles unbalanced quotes gracefully)
    - Unknown operators are preserved as plain text and noted in unknown_ops

Year validation:
    - Single year: year:2020 (stored as integer 2020)
    - Range: year:2020..2025 or year:2020-2025 (stored as tuple (2020, 2025))
    - Invalid years produce a readable issue and remain safely represented as data

Outcome allowlist:
    - allowed, dismissed, affirmed, reversed, settled, withdrawn

Injection safety:
    - Parser stores values as data, never constructs SQL or commands
    - Year validation prevents calendar overflow
    - All operator values are stored as data for downstream parameterized queries
"""

import re
from typing import Any, Dict, List, Optional, Tuple, Union


OUTCOME_ALLOWLIST = {"allowed", "dismissed", "affirmed", "reversed", "settled", "withdrawn"}


def parse_query(query_str: str) -> Dict[str, Any]:
    """
    Parse a query string with optional Boolean and field operators.
    
    Args:
        query_str: Raw user query string
        
    Returns:
        Dictionary with keys: raw_query, terms, filters, boolean_ops, expression,
        echo, unknown_ops, issues
    """
    if not isinstance(query_str, str):
        query_str = str(query_str)
    
    query_str = query_str.strip()
    
    result = {
        "raw_query": query_str,
        "terms": [],
        "filters": {
            "court": [],
            "year": [],
            "judge": [],
            "cites": [],
            "outcome": [],
        },
        "boolean_ops": {
            "and_terms": [],
            "or_terms": [],
            "not_terms": [],
        },
        "expression": None,
        "echo": "",
        "unknown_ops": [],
        "issues": [],
    }
    
    if not query_str:
        result["echo"] = "(empty query)"
        result["expression"] = None
        return result
    
    # Tokenize query preserving operator context
    tokens = _tokenize(query_str, result)
    
    # Process tokens into structured result
    _process_tokens(tokens, result)
    
    # Build Boolean expression AST
    result["expression"] = _build_expression_ast(tokens, result)
    
    # Build echo
    result["echo"] = _build_echo(result)
    
    return result


def _tokenize(query_str: str, result: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Tokenize query string into structured tokens.
    
    Returns list of token dicts with keys: type, value, original
    Types: term, boolean, field, quoted, operator_word
    """
    tokens = []
    i = 0
    in_quote = False
    quote_char = None
    current_token = ""
    current_type = None
    quote_field_prefix = ""
    quote_start = i
    
    while i < len(query_str):
        char = query_str[i]
        
        # Handle quoted sections
        is_single_quote = (
            char == "'"
            and not (
                i > 0
                and i + 1 < len(query_str)
                and query_str[i - 1].isalnum()
                and query_str[i + 1].isalnum()
            )
        )
        if (char == '"' or is_single_quote) and (i == 0 or query_str[i-1] != "\\"):
            if not in_quote:
                # Start quote
                if re.fullmatch(r"(?:court|year|judge|cites|outcome):", current_token, re.IGNORECASE):
                    # A quote immediately following a recognized field name is
                    # part of that field value (for example cites:"2019 SCC 65").
                    quote_field_prefix = current_token
                    current_token = ""
                elif current_token.strip():
                    # Flush current token
                    tokens.append(_make_token(current_type, current_token))
                    current_token = ""
                    current_type = None
                in_quote = True
                quote_char = char
                quote_start = i
                current_token = ""
                i += 1
                continue
            elif char == quote_char:
                # End quote
                in_quote = False
                if quote_field_prefix:
                    tokens.append(_make_token(None, quote_field_prefix + current_token))
                    quote_field_prefix = ""
                else:
                    tokens.append({
                        "type": "quoted",
                        "value": current_token,
                        "original": query_str[quote_start:i+1],
                    })
                current_token = ""
                current_type = None
                quote_char = None
                i += 1
                continue
            else:
                current_token += char
                i += 1
                continue
        
        if in_quote:
            current_token += char
            i += 1
            continue
        
        # Outside quotes
        if char.isspace():
            if current_token.strip():
                tokens.append(_make_token(current_type, current_token))
                current_token = ""
                current_type = None
            i += 1
            continue
        
        current_token += char
        i += 1
    
    # Handle unbalanced quote
    if in_quote:
        result["issues"].append(f"Unbalanced quote starting at position {quote_start}")
        if current_token:
            if quote_field_prefix:
                tokens.append(_make_token(None, quote_field_prefix + current_token))
            else:
                tokens.append({
                    "type": "quoted",
                    "value": current_token,
                    "original": query_str[quote_start:],
                    "unbalanced": True,
                })
    elif current_token.strip():
        tokens.append(_make_token(current_type, current_token))
    
    return tokens


def _make_token(current_type: Optional[str], token_str: str) -> Dict[str, Any]:
    """Convert accumulated token string to structured token."""
    token_str = token_str.strip()
    if not token_str:
        return None
    
    # Check for field operator (word:value pattern)
    if ":" in token_str and not token_str.startswith("-"):
        parts = token_str.split(":", 1)
        field_name = parts[0].lower()
        field_value = parts[1] if len(parts) > 1 else ""
        
        if field_name in ("court", "year", "judge", "cites", "outcome"):
            return {
                "type": "field",
                "field": field_name,
                "value": field_value,
                "original": token_str,
            }
        else:
            # Unknown operator - treat as term but mark it
            return {
                "type": "operator_word",
                "value": token_str,
                "original": token_str,
            }
    
    # Check for leading minus (NOT variant)
    if token_str.startswith("-") and len(token_str) > 1:
        return {
            "type": "boolean",
            "op": "NOT",
            "value": token_str[1:],
            "original": token_str,
        }
    
    # Check for Boolean operators
    if token_str.upper() in ("AND", "OR", "NOT"):
        return {
            "type": "boolean",
            "op": token_str.upper(),
            "original": token_str,
        }
    
    # Plain term
    return {
        "type": "term",
        "value": token_str,
        "original": token_str,
    }


def _process_tokens(tokens: List[Dict[str, Any]], result: Dict[str, Any]) -> None:
    """Process tokens into filters, terms, and boolean operations."""
    tokens = [t for t in tokens if t is not None]
    
    i = 0
    pending_bool_op = None
    
    while i < len(tokens):
        token = tokens[i]
        
        if token["type"] == "field":
            _process_field(token, result)
        elif token["type"] == "boolean":
            if token["op"] == "NOT" and "value" in token:
                # Inline NOT -term
                result["boolean_ops"]["not_terms"].append(token["value"])
            else:
                # Boolean connector for next term
                pending_bool_op = token["op"]
        elif token["type"] == "term":
            value = token["value"]
            if pending_bool_op == "AND":
                result["boolean_ops"]["and_terms"].append(value)
            elif pending_bool_op == "OR":
                result["boolean_ops"]["or_terms"].append(value)
            elif pending_bool_op == "NOT":
                result["boolean_ops"]["not_terms"].append(value)
            else:
                result["terms"].append(value)
            pending_bool_op = None
        elif token["type"] == "quoted":
            value = token["value"]
            if pending_bool_op == "AND":
                result["boolean_ops"]["and_terms"].append(value)
            elif pending_bool_op == "OR":
                result["boolean_ops"]["or_terms"].append(value)
            elif pending_bool_op == "NOT":
                result["boolean_ops"]["not_terms"].append(value)
            else:
                result["terms"].append(value)
            pending_bool_op = None
        elif token["type"] == "operator_word":
            # Unknown operator - treat as term, note it
            if token["value"] not in result["unknown_ops"]:
                result["unknown_ops"].append(token["value"])
            # Also add to terms as complete token
            result["terms"].append(token["value"])
        
        i += 1


def _process_field(token: Dict[str, Any], result: Dict[str, Any]) -> None:
    """Process a field operator token."""
    field_name = token["field"]
    field_value = token["value"]
    
    if field_name == "court":
        if field_value:
            result["filters"]["court"].append(field_value)
    elif field_name == "judge":
        if field_value:
            result["filters"]["judge"].append(field_value)
    elif field_name == "cites":
        if field_value:
            result["filters"]["cites"].append(field_value)
    elif field_name == "outcome":
        if field_value and field_value.lower() in OUTCOME_ALLOWLIST:
            result["filters"]["outcome"].append(field_value.lower())
        elif field_value:
            result["issues"].append(
                f"Unknown outcome '{field_value}'; allowed: {', '.join(sorted(OUTCOME_ALLOWLIST))}"
            )
    elif field_name == "year":
        _process_year_field(field_value, result)


def _process_year_field(field_value: str, result: Dict[str, Any]) -> None:
    """Process year: field with validation."""
    if not field_value:
        return
    
    # Accept the explicit inclusive range syntax and retain legacy hyphen syntax.
    range_separator = ".." if ".." in field_value else "-" if "-" in field_value else None
    if range_separator:
        parts = field_value.split(range_separator)
        if len(parts) == 2:
            try:
                start_year = int(parts[0].strip())
                end_year = int(parts[1].strip())
                # Basic validation
                if 1000 <= start_year <= 9999 and 1000 <= end_year <= 9999:
                    if start_year <= end_year:
                        result["filters"]["year"].append((start_year, end_year))
                    else:
                        result["issues"].append(
                            f"Invalid year range: start {start_year} > end {end_year}"
                        )
                else:
                    result["issues"].append(
                        f"Year values out of valid range: {parts[0]}, {parts[1]}"
                    )
            except ValueError:
                result["issues"].append(
                    f"Invalid year range format: '{field_value}' (expected YYYY..YYYY or YYYY-YYYY)"
                )
        else:
            result["issues"].append(
                f"Invalid year range format: '{field_value}' (expected YYYY..YYYY, YYYY-YYYY, or single YYYY)"
            )
    else:
        # Single year
        try:
            year = int(field_value.strip())
            if 1000 <= year <= 9999:
                result["filters"]["year"].append(year)
            else:
                result["issues"].append(f"Year out of valid range: {year}")
        except ValueError:
            result["issues"].append(f"Invalid year format: '{field_value}' (expected integer)")


def _build_expression_ast(tokens: List[Dict[str, Any]], result: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Build a Boolean expression AST from tokens using conventional precedence:
    NOT > AND > OR. Adjacent atoms/terms are implicitly AND.
    
    Returns AST root node or None if no expression.
    """
    tokens = [t for t in tokens if t is not None]
    
    if not tokens:
        return None
    
    # Parse using recursive descent with precedence: OR < AND < NOT
    parser = _ExpressionParser(tokens, result)
    expr = parser.parse_or()
    
    return expr if expr else None


class _ExpressionParser:
    """Recursive descent parser for Boolean expressions."""
    
    def __init__(self, tokens: List[Dict[str, Any]], result: Dict[str, Any]):
        self.tokens = tokens
        self.result = result
        self.pos = 0
    
    def current(self) -> Optional[Dict[str, Any]]:
        """Get current token."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def peek_type(self) -> Optional[str]:
        """Get type of current token."""
        curr = self.current()
        return curr["type"] if curr else None
    
    def consume(self) -> Optional[Dict[str, Any]]:
        """Consume and return current token."""
        token = self.current()
        if token:
            self.pos += 1
        return token
    
    def parse_or(self) -> Optional[Dict[str, Any]]:
        """Parse OR expression (lowest precedence)."""
        left = self.parse_and()
        if not left:
            return None
        
        operands = [left]
        
        while self.current() and self.peek_type() == "boolean":
            curr = self.current()
            if curr.get("op") == "OR":
                self.consume()
                right = self.parse_and()
                if right:
                    operands.append(right)
        
        if len(operands) == 1:
            return operands[0]
        
        return {"type": "or", "operands": operands}
    
    def parse_and(self) -> Optional[Dict[str, Any]]:
        """Parse AND expression (middle precedence). Adjacent atoms are AND."""
        left = self.parse_not()
        if not left:
            return None
        
        operands = [left]
        
        while True:
            curr = self.current()
            if not curr:
                break
            
            # Explicit AND
            if curr.get("type") == "boolean" and curr.get("op") == "AND":
                self.consume()
                right = self.parse_not()
                if right:
                    operands.append(right)
            # Implicit AND: adjacent atoms/terms that aren't OR
            elif (curr.get("type") in ("term", "quoted", "field") or
                  (curr.get("type") == "boolean" and curr.get("op") == "NOT")):
                right = self.parse_not()
                if right:
                    operands.append(right)
            else:
                break
        
        if len(operands) == 1:
            return operands[0]
        
        return {"type": "and", "operands": operands}
    
    def parse_not(self) -> Optional[Dict[str, Any]]:
        """Parse NOT expression (highest precedence)."""
        curr = self.current()
        
        # Explicit NOT
        if curr and curr.get("type") == "boolean" and curr.get("op") == "NOT":
            if "value" in curr:
                # NOT token with inline value (-term)
                self.consume()
                operand = {"type": "atom", "kind": "term", "value": curr["value"], "field_name": None}
                return {"type": "not", "operand": operand}
            else:
                # Standalone NOT operator
                self.consume()
                operand = self.parse_not()
                if operand:
                    return {"type": "not", "operand": operand}
        
        # Parse atom
        return self.parse_atom()
    
    def parse_atom(self) -> Optional[Dict[str, Any]]:
        """Parse atom (term, quoted, or field)."""
        curr = self.current()
        
        if not curr:
            return None
        
        if curr["type"] == "term":
            self.consume()
            return {
                "type": "atom",
                "kind": "term",
                "value": curr["value"],
                "field_name": None,
            }
        elif curr["type"] == "quoted":
            self.consume()
            return {
                "type": "atom",
                "kind": "term",
                "value": curr["value"],
                "field_name": None,
            }
        elif curr["type"] == "field":
            self.consume()
            return {
                "type": "atom",
                "kind": "field",
                "value": curr["value"],
                "field_name": curr["field"],
            }
        elif curr["type"] == "operator_word":
            self.consume()
            return {
                "type": "atom",
                "kind": "term",
                "value": curr["value"],
                "field_name": None,
            }
        
        return None


def _build_echo(result: Dict[str, Any]) -> str:
    """Build plain-language echo of parsed query."""
    parts = []
    expression = result.get("expression")
    if expression and _has_boolean_node(expression):
        parts.append("meaning: " + _echo_expression(expression))
    
    # Plain terms
    if result["terms"]:
        parts.append("search: " + " ".join(result["terms"]))
    
    # Boolean operations
    if result["boolean_ops"]["and_terms"]:
        parts.append("AND: " + " ".join(result["boolean_ops"]["and_terms"]))
    if result["boolean_ops"]["or_terms"]:
        parts.append("OR: " + " ".join(result["boolean_ops"]["or_terms"]))
    if result["boolean_ops"]["not_terms"]:
        parts.append("NOT: " + " ".join(result["boolean_ops"]["not_terms"]))
    
    # Filters
    filters_parts = []
    if result["filters"]["court"]:
        filters_parts.append("court: " + ", ".join(result["filters"]["court"]))
    if result["filters"]["year"]:
        year_strs = []
        for y in result["filters"]["year"]:
            if isinstance(y, tuple):
                year_strs.append(f"{y[0]} through {y[1]} (inclusive)")
            else:
                year_strs.append(str(y))
        filters_parts.append("year: " + ", ".join(year_strs))
    if result["filters"]["judge"]:
        filters_parts.append("judge: " + ", ".join(result["filters"]["judge"]))
    if result["filters"]["cites"]:
        filters_parts.append("cites: " + ", ".join(result["filters"]["cites"]))
    if result["filters"]["outcome"]:
        filters_parts.append("outcome: " + ", ".join(result["filters"]["outcome"]))
    
    if filters_parts:
        parts.append("filters: " + "; ".join(filters_parts))
    
    # Unknown operators
    if result["unknown_ops"]:
        parts.append("⚠ unknown operators: " + ", ".join(result["unknown_ops"]))
    
    # Issues
    if result["issues"]:
        parts.append("⚠ issues: " + "; ".join(result["issues"]))
    
    if not parts:
        return "(no search criteria parsed)"
    
    return " | ".join(parts)


def _has_boolean_node(node: Dict[str, Any]) -> bool:
    if node.get("type") in {"and", "or", "not"}:
        return True
    return any(_has_boolean_node(child) for child in node.get("operands", [])) or (
        _has_boolean_node(node["operand"]) if isinstance(node.get("operand"), dict) else False
    )


def _echo_expression(node: Dict[str, Any]) -> str:
    """Render the parsed expression without losing Boolean relationships."""
    node_type = node.get("type")
    if node_type == "atom":
        value = str(node.get("value", "")).replace('"', '\\"')
        if node.get("kind") == "field":
            return f'{node.get("field_name")}: "{value}"'
        return f'"{value}"'
    if node_type == "not":
        return f"NOT ({_echo_expression(node['operand'])})"
    if node_type in {"and", "or"}:
        operator = " AND " if node_type == "and" else " OR "
        return "(" + operator.join(_echo_expression(child) for child in node["operands"]) + ")"
    return "(unrecognized query)"
