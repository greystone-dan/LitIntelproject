"""Small, explicit message catalog for the About-page French preview."""

import html
import re

MESSAGES = {
    "en": {
        "about.title": "iLit: where the project stands",
        "about.lede": (
            "iLit is a litigation intelligence tool for immigration law that I have been "
            "building independently. It reads every Federal Court immigration file and "
            "decision, connects them, and answers the questions a litigation analyst is "
            "asked every week, with the source behind every answer. This is where it is "
            "today, and where it could go next."
        ),
        "about.nav_today": "CanLII vs iLit",
        "about.nav_how": "How it works",
        "about.nav_files": "Tracking files",
        "about.review_notice": (
            "Machine-drafted French preview; review by a fluent French speaker is required. "
            "Legal terminology is not final."
        ),
        "about.language_label": "Language",
        "about.language_english": "English",
    },
    "fr": {
        "about.title": "iLit : où en est le projet",
        "about.lede": (
            "iLit est un outil d’intelligence contentieuse en droit de l’immigration que je "
            "développe de façon indépendante. Il lit les dossiers et décisions de la Cour "
            "fédérale en immigration, les relie et répond aux questions que les analystes "
            "en contentieux se posent chaque semaine, avec la source à l’appui de chaque "
            "réponse. Voici où en est le projet et où il pourrait aller."
        ),
        "about.nav_today": "CanLII et iLit",
        "about.nav_how": "Fonctionnement",
        "about.nav_files": "Suivi des dossiers",
        "about.review_notice": (
            "Aperçu français rédigé par machine : révision par une personne francophone "
            "requise. La terminologie juridique n’est pas définitive."
        ),
        "about.language_label": "Langue",
        "about.language_english": "English",
    },
}

MESSAGE_PLACEHOLDER = re.compile(r"\{\{\s*([a-z][a-z0-9_.-]*)\s*\}\}")


def message(key: str, lang: str = "en") -> str:
    """Return a localized message, falling back to English and then the key."""
    locale = MESSAGES.get(lang, {})
    return locale.get(key, MESSAGES["en"].get(key, key))


def render_about_fragment(fragment: str, lang: str = "en") -> str:
    """Resolve catalog placeholders without changing static English source text."""
    selected_language = "fr" if lang == "fr" else "en"
    rendered = MESSAGE_PLACEHOLDER.sub(
        lambda match: html.escape(message(match.group(1), selected_language)),
        fragment,
    )
    if selected_language == "fr":
        header = '<header class="top">'
        language_controls = (
            '<p class="small muted" lang="fr">'
            f'{html.escape(message("about.review_notice", "fr"))}</p>'
            f'<nav aria-label="{html.escape(message("about.language_label", "fr"))}">'
            f'<a href="/data-explorer?tab=about">{html.escape(message("about.language_english", "fr"))}</a></nav>'
        )
        rendered = rendered.replace(header, header + language_controls, 1)
    return rendered
