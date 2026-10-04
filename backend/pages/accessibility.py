from functools import wraps
import re


_SKIP_LINK_STYLE = """
.a11y-visually-hidden{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
 :root{--a11y-focus:#102038}
:focus-visible{outline:3px solid var(--a11y-focus);outline-offset:2px}
.skip-link{position:absolute;left:-10000px;top:0;z-index:99999;padding:10px 14px;background:#102038;color:#fff;border:2px solid #fff;border-radius:4px}
.skip-link:focus{left:1rem;top:1rem}
@media(prefers-reduced-motion:reduce){html:focus-within{scroll-behavior:auto!important}*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}
"""
_TABLE_ACCESSIBILITY_SCRIPT = """
<script data-accessibility-table-labels>
(()=>{const labelTable=table=>{if(!table.caption){const context=table.closest('section')||table.parentElement,heading=context?.querySelector('h2,h3,h4'),headers=[...table.querySelectorAll('thead th')].map(cell=>cell.textContent.trim()).filter(Boolean),caption=document.createElement('caption');caption.className='a11y-visually-hidden';caption.textContent=(heading?.textContent||headers.join(', ')||'Data table').trim();table.prepend(caption)}table.querySelectorAll('thead th:not([scope])').forEach(cell=>cell.scope='col');table.querySelectorAll('tbody th:not([scope])').forEach(cell=>cell.scope='row')};document.querySelectorAll('table').forEach(labelTable);new MutationObserver(records=>records.forEach(record=>record.addedNodes.forEach(node=>{if(node.nodeType!==1)return;if(node.matches('table'))labelTable(node);node.querySelectorAll('table').forEach(labelTable)}))).observe(document.body,{childList:true,subtree:true})})();
</script>
"""
_MAIN_ROOT_CLASSES = {"container", "shell", "wrap"}


def _main_target(html: str) -> tuple[str, str]:
    main = re.search(r"<main\b[^>]*>", html, re.IGNORECASE)
    if main:
        opening = main.group()
        target = re.search(r"\bid=(['\"])(.*?)\1", opening, re.IGNORECASE)
        if target:
            return html, target.group(2)
        return (
            html[: main.start()] + opening[:-1] + ' id="main-content">' + html[main.end() :],
            "main-content",
        )

    for match in re.finditer(r"<div\b[^>]*>", html, re.IGNORECASE):
        opening = match.group()
        classes = re.search(r"\bclass=(?:\\)?(['\"])(.*?)\1", opening, re.IGNORECASE)
        if not classes:
            continue
        class_names = classes.group(2).replace("\\", "").replace('"', "").replace("'", "").split()
        if not _MAIN_ROOT_CLASSES.intersection(class_names):
            continue
        target = re.search(r"\bid=(['\"])(.*?)\1", opening, re.IGNORECASE)
        target_id = target.group(2) if target else "main-content"
        if not target:
            opening = opening[:-1] + f' id="{target_id}" role="main">'
            html = html[: match.start()] + opening + html[match.end() :]
        return html, target_id

    raise ValueError("Page builder HTML has no main landmark or recognized content root")


def _add_live_region_roles(html: str) -> str:
    def add_attributes(match):
        tag, attributes = match.groups()
        classes = re.search(r"\bclass=(['\"])(.*?)\1", attributes, re.IGNORECASE)
        element_id = re.search(r"\bid=(['\"])(.*?)\1", attributes, re.IGNORECASE)
        class_names = set(classes.group(2).split()) if classes else set()
        id_name = element_id.group(2).lower() if element_id else ""
        if "error" in class_names or id_name.endswith("error"):
            role, live = "alert", "assertive"
        elif (
            class_names.intersection({"status", "search-status", "search-meta", "fcx-status"})
            or id_name.endswith(("status", "meta"))
        ):
            role, live = "status", "polite"
        else:
            return match.group()
        if not re.search(r"\brole=", attributes, re.IGNORECASE):
            attributes += f' role="{role}"'
        if not re.search(r"\baria-live=", attributes, re.IGNORECASE):
            attributes += f' aria-live="{live}"'
        return f"<{tag}{attributes}>"

    return re.sub(r"<(div|span|p)\b([^>]*)>", add_attributes, html, flags=re.IGNORECASE)


def _describe_upload_errors(html: str) -> str:
    if not re.search(r"\bid=['\"]error['\"]", html, re.IGNORECASE):
        return html

    def add_description(match):
        opening = match.group()
        if re.search(r"\baria-describedby=", opening, re.IGNORECASE):
            return opening
        return opening[:-1] + ' aria-describedby="error">'

    return re.sub(
        r"<input\b(?=[^>]*\bid=['\"]file['\"])[^>]*>",
        add_description,
        html,
        count=1,
        flags=re.IGNORECASE,
    )


def accessible_page(builder):
    @wraps(builder)
    def wrapped(*args, **kwargs):
        html = builder(*args, **kwargs)
        if not isinstance(html, str):
            return html
        html = _add_live_region_roles(html)
        html = _describe_upload_errors(html)
        html, target_id = _main_target(html)
        if 'class="skip-link"' not in html:
            html = re.sub(
                r"(<body\b[^>]*>)",
                rf'\1<a class="skip-link" href="#{target_id}">Skip to main content</a>',
                html,
                count=1,
                flags=re.IGNORECASE,
            )
        if "</head>" in html and ".skip-link:focus" not in html:
            html = html.replace("</head>", f"<style>{_SKIP_LINK_STYLE}</style></head>", 1)
        if "</body>" in html and "data-accessibility-table-labels" not in html:
            html = html.replace("</body>", f"{_TABLE_ACCESSIBILITY_SCRIPT}</body>", 1)
        return html

    return wrapped
