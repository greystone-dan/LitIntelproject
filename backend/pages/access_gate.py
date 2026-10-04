"""Private-site login page builder."""

from .skip_link import with_skip_link


@with_skip_link
def access_login_page_html(error: str = "") -> str:
    message = f'<p class="error">{error}</p>' if error else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><title>Private site access</title>
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#f1efe8;color:#202522;font-family:system-ui,sans-serif}}main{{width:min(360px,calc(100% - 32px));padding:28px;background:#fffef9;border:1px solid #d8d5ca;border-radius:8px}}h1{{margin:0 0 8px;font-size:22px}}p{{color:#69726d;font-size:13px;line-height:1.5}}label{{display:block;margin:18px 0 6px;font-size:12px;font-weight:700}}input,button{{box-sizing:border-box;width:100%;height:42px;padding:0 12px;border:1px solid #d8d5ca;border-radius:5px;font:inherit}}button{{margin-top:12px;background:#202522;color:white;font-weight:700;cursor:pointer}}.error{{color:#a4412b}}</style></head>
<body><main><h1>Private research site</h1><p>Enter the access password to continue.</p>{message}<form method="post" action="/access/login"><label for="password">Access password</label><input id="password" name="password" type="password" autocomplete="current-password" required autofocus><button type="submit">Continue</button></form></main></body></html>"""
