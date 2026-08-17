#!/usr/bin/env python
"""Check if the routes.py updates were actually applied"""

with open('backend/routes.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for the key markers that should have been added
markers = {
    'debounced_function': 'function debouncedSuggestions(){',
    'search_input_listener': "addEventListener('input',debouncedSuggestions)",
    'prominent_panel_toggle': "document.getElementById('prominentPanel').hidden=active!=='prominent'",
    'prominent_load_call': "if(active==='prominent')loadProminent();",
}

print("Checking for applied updates in routes.py:")
print("-" * 50)

for name, marker in markers.items():
    if marker in content:
        print(f"✓ {name}: FOUND")
    else:
        print(f"✗ {name}: NOT FOUND")

# Show snippet around tab handler
print("\n" + "=" * 50)
print("Tab handler area (to inspect):")
print("=" * 50)

tab_handler_idx = content.find("document.querySelectorAll('.tab').forEach(tab=>tab.onclick=")
if tab_handler_idx > 0:
    snippet = content[tab_handler_idx:tab_handler_idx+400]
    print(snippet)
else:
    print("Tab handler not found!")
