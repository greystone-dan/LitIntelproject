#!/usr/bin/env python
import re

with open('backend/routes.py', 'r', encoding='utf-8') as f:
    content = f.read()

updates_made = []

# 1. Add debounced suggestions function BEFORE loadSuggestions
if 'function debouncedSuggestions()' not in content:
    # Find where loadSuggestions is and add debounce before it
    old_search = "let suggestionTimer=null;\n\tfunction renderSuggestions"
    new_search = "let suggestionTimer=null;\n\tfunction debouncedSuggestions(){clearTimeout(suggestionTimer);suggestionTimer=setTimeout(loadSuggestions, 200);}\n\tfunction renderSuggestions"
    if old_search in content:
        content = content.replace(old_search, new_search)
        updates_made.append("✓ Added debouncedSuggestions function")

# 2. Wire in search input listener AFTER setting onsubmit
if "addEventListener('input'" not in content or 'searchQuery' not in content.split("addEventListener('input'")[0]:
    old_search = "document.getElementById('caseSearch').onsubmit=loadSearch;"
    new_search = "document.getElementById('caseSearch').onsubmit=loadSearch;document.getElementById('searchQuery')?.addEventListener('input',debouncedSuggestions);"
    if old_search in content:
        content = content.replace(old_search, new_search)
        updates_made.append("✓ Added search input listener")

# 3. Wire in prominent panel visibility toggle
if "getElementById('prominentPanel').hidden" not in content:
    old_search = "document.getElementById('neighborhoodPanel').hidden=active!=='neighborhood';document.querySelectorAll('.tab').forEach(item=>item.classList.toggle('active',item===tab));"
    new_search = "document.getElementById('neighborhoodPanel').hidden=active!=='neighborhood';document.getElementById('prominentPanel').hidden=active!=='prominent';document.querySelectorAll('.tab').forEach(item=>item.classList.toggle('active',item===tab));"
    if old_search in content:
        content = content.replace(old_search, new_search)
        updates_made.append("✓ Added prominent panel toggle")

# 4. Wire in loadProminent() call
if "active==='prominent')loadProminent()" not in content:
    old_search = "if(active==='explorer')load();if(active==='neighborhood'"
    new_search = "if(active==='explorer')load();if(active==='prominent')loadProminent();if(active==='neighborhood'"
    if old_search in content:
        content = content.replace(old_search, new_search)
        updates_made.append("✓ Added prominent load call")

with open('backend/routes.py', 'w', encoding='utf-8') as f:
    f.write(content)

if updates_made:
    for msg in updates_made:
        print(msg)
    print("\n✓ Routes.py updated successfully")
else:
    print("✗ No updates were applied - pattern matching failed")
    print("This likely means the exact string patterns were not found in the minified code")
