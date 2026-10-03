"""Tests for minister name normalization."""

import pytest

from backend.minister_normalization import (
    apply_normalization_to_list,
    filter_to_immigration_parties,
    normalize_minister_name,
    get_canonical_ministers,
)


class TestNormalizeMinisterName:
    """Tests for normalize_minister_name function."""

    def test_exact_match(self):
        """Exact matches should return canonical form."""
        assert normalize_minister_name("Citizenship and Immigration Canada") == \
               "Citizenship and Immigration Canada"

    def test_typo_correction(self):
        """Common typos should be corrected."""
        assert normalize_minister_name("Citizenship & Immigration Canada") == \
               "Citizenship and Immigration Canada"
        assert normalize_minister_name("Immig. Refugees & Citizenship Canada") == \
               "Immigration, Refugees and Citizenship Canada"

    def test_case_insensitive(self):
        """Matching should be case-insensitive."""
        assert normalize_minister_name("citizenship and immigration canada") == \
               "Citizenship and Immigration Canada"
        assert normalize_minister_name("CITIZENSHIP AND IMMIGRATION CANADA") == \
               "Citizenship and Immigration Canada"

    def test_whitespace_trimmed(self):
        """Leading/trailing whitespace should be trimmed."""
        assert normalize_minister_name("  Citizenship and Immigration Canada  ") == \
               "Citizenship and Immigration Canada"

    def test_abbreviations(self):
        """Abbreviations should be expanded to canonical forms."""
        assert normalize_minister_name("IRCC") == \
               "Immigration, Refugees and Citizenship Canada"
        assert normalize_minister_name("CIC") == \
               "Citizenship and Immigration Canada"

    def test_unknown_value_returned_as_is(self):
        """Unknown values should be returned trimmed but unchanged."""
        assert normalize_minister_name("Some Unknown Party") == "Some Unknown Party"

    def test_none_input(self):
        """None input should return None."""
        assert normalize_minister_name(None) is None

    def test_empty_string(self):
        """Empty string should return None."""
        assert normalize_minister_name("") is None
        assert normalize_minister_name("   ") is None


class TestFilterToImmigrationParties:
    """Tests for filter_to_immigration_parties function."""

    def test_canonical_immigration_parties(self):
        """Known immigration parties should pass filter."""
        assert filter_to_immigration_parties("Citizenship and Immigration Canada")
        assert filter_to_immigration_parties("Immigration, Refugees and Citizenship Canada")
        assert filter_to_immigration_parties("Minister of Citizenship and Immigration")
        assert filter_to_immigration_parties("Canada")
        assert filter_to_immigration_parties("Canada Border Services Agency")

    def test_keywords_match(self):
        """Parties with immigration-related keywords should pass."""
        assert filter_to_immigration_parties("Minister of Immigration")
        assert filter_to_immigration_parties("Immigration Policy")
        assert filter_to_immigration_parties("Refugee Services")
        assert filter_to_immigration_parties("Citizenship Board")

    def test_non_immigration_filtered(self):
        """Non-immigration parties should be filtered out."""
        assert not filter_to_immigration_parties("Ministry of Health")
        assert not filter_to_immigration_parties("Department of Finance")
        assert not filter_to_immigration_parties("Ministry of Transportation")

    def test_none_and_empty(self):
        """None and empty values should return False."""
        assert not filter_to_immigration_parties(None)
        assert not filter_to_immigration_parties("")
        assert not filter_to_immigration_parties("   ")


class TestApplyNormalizationToList:
    """Tests for apply_normalization_to_list function."""

    def test_empty_list(self):
        """Empty list should return empty list."""
        assert apply_normalization_to_list([]) == []

    def test_typos_corrected(self):
        """Typos should be corrected and deduplicated."""
        raw = [
            "Citizenship & Immigration Canada",
            "Citizenship and Immigration Canada",
            "CIC",
        ]
        result = apply_normalization_to_list(raw)
        assert len(result) == 1
        assert result[0] == "Citizenship and Immigration Canada"

    def test_non_immigration_filtered(self):
        """Non-immigration parties should be filtered out."""
        raw = [
            "Citizenship and Immigration Canada",
            "Ministry of Health",
            "Canada",
            "Department of Finance",
        ]
        result = apply_normalization_to_list(raw)
        assert "Ministry of Health" not in result
        assert "Department of Finance" not in result
        assert "Citizenship and Immigration Canada" in result
        assert "Canada" in result

    def test_sorted_output(self):
        """Output should be sorted."""
        raw = [
            "Minister of Immigration, Refugees and Citizenship",
            "Citizenship and Immigration Canada",
            "Canada",
        ]
        result = apply_normalization_to_list(raw)
        assert result == sorted(result)

    def test_duplicates_removed(self):
        """Duplicates should be removed."""
        raw = [
            "Citizenship and Immigration Canada",
            "Citizenship and Immigration Canada",
            "CIC",  # Normalizes to same as first
            "Citizenship and Immigration Canada",
        ]
        result = apply_normalization_to_list(raw)
        assert len(result) == 1

    def test_custom_normalize_function(self):
        """Custom normalization function should be respected."""
        def custom_normalize(name):
            return (name or "").upper() if name else None

        raw = ["test", "test2"]
        result = apply_normalization_to_list(
            raw,
            normalize_fn=custom_normalize,
            filter_fn=lambda x: True,  # Accept all for testing normalization
        )
        assert result == ["TEST", "TEST2"]

    def test_custom_filter_function(self):
        """Custom filter function should be respected."""
        def custom_filter(name):
            return bool(name and "TEST" in name.upper())

        raw = ["TEST value", "other value", "TEST another"]
        result = apply_normalization_to_list(
            raw,
            normalize_fn=lambda x: x,  # No normalization
            filter_fn=custom_filter,
        )
        assert len(result) == 2
        assert all("test" in r.lower() for r in result)


class TestGetCanonicalMinisters:
    """Tests for get_canonical_ministers function."""

    def test_returns_sorted_list(self):
        """Should return a sorted list of canonical forms."""
        canonical = get_canonical_ministers()
        assert isinstance(canonical, list)
        assert len(canonical) > 0
        assert canonical == sorted(canonical)

    def test_includes_major_departments(self):
        """Should include major immigration departments."""
        canonical = get_canonical_ministers()

        assert "Citizenship and Immigration Canada" in canonical
        assert "Immigration, Refugees and Citizenship Canada" in canonical
        assert "Canada" in canonical

    def test_caching(self):
        """Results should be cached."""
        result1 = get_canonical_ministers()
        result2 = get_canonical_ministers()
        assert result1 is result2  # Same object


class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_messy_input_produces_clean_output(self):
        """Real-world messy input should produce clean output."""
        raw_ministers = [
            "Citizenship & Immigration Canada",  # typo
            "Immigration, Refugees & Citizenship Canada",  # missing "and"
            "Citizenship and Immigration Canada",  # correct
            "CIC",  # abbreviation
            "IRCC",  # abbreviation
            "Ministry of Health",  # non-immigration (should be filtered)
            "Min. of Immigration",  # abbreviated title
            "Canada",  # government party
            "",  # empty
            None,  # None
            "some unknown party",  # unknown but might be immigration-related
        ]

        result = apply_normalization_to_list(raw_ministers)

        # Should have deduplicated CIC/IRCC variations
        cic_variants = [r for r in result if "Citizenship and Immigration" in r]
        assert len(cic_variants) == 1

        # Should have filtered out non-immigration
        assert not any("Health" in r for r in result)

        # Should include canonical forms
        assert "Canada" in result

    def test_normalization_preserves_information(self):
        """Normalization should preserve which department each case belongs to."""
        # All these refer to the same department (different names over time)
        variants = [
            "Citizenship and Immigration Canada",
            "Immigration, Refugees and Citizenship Canada",
            "IRCC",
            "CIC",
        ]

        normalized = [normalize_minister_name(v) for v in variants]

        # Should have exactly 2 canonical forms
        unique_normalized = set(normalized)
        assert len(unique_normalized) == 2
