"""Extended instrument registry for the law refinement layer.

It reads the pass-one ``LEGISLATION_REGISTRY`` (unchanged) and layers on
instruments that pass one does not know, plus French names and short forms.
When the layers are merged, these entries can move into
``backend.statutes.LEGISLATION_REGISTRY``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from ..statutes import LEGISLATION_REGISTRY

_JUSTICE = "https://laws-lois.justice.gc.ca/eng"


@dataclass(frozen=True)
class Instrument:
	key: str
	citation: str
	aliases: tuple[str, ...]
	french_aliases: tuple[str, ...] = ()
	url_template: str | None = None
	kind: str = "statute"  # "statute" or "instrument" (treaties)
	provision_label: str = "s."  # "s.", "r." (rules) or "art." (treaties)

	def url_for(self, section: str | None) -> str | None:
		if not section or not self.url_template:
			return None
		return self.url_template.format(section=section)


_EXTRA_INSTRUMENTS: dict[str, dict[str, object]] = {
	"canada.fc_cirp_rules": {
		"aliases": (
			"Federal Courts Citizenship, Immigration and Refugee Protection Rules",
			"Federal Courts Immigration and Refugee Protection Rules",
			"Federal Court Immigration and Refugee Protection Rules",
			"Federal Court Immigration Rules",
			"Federal Courts Immigration Rules",
		),
		"french_aliases": (
			"Règles des Cours fédérales en matière de citoyenneté, d'immigration et de protection des réfugiés",
		),
		"citation": "Federal Courts Citizenship, Immigration and Refugee Protection Rules, SOR/93-22",
		"url": f"{_JUSTICE}/regulations/SOR-93-22/section-{{section}}.html",
		"provision_label": "r.",
	},
	"canada.rpd_rules": {
		"aliases": ("Refugee Protection Division Rules", "RPD Rules"),
		"french_aliases": ("Règles de la Section de la protection des réfugiés",),
		"citation": "Refugee Protection Division Rules, SOR/2012-256",
		"url": f"{_JUSTICE}/regulations/SOR-2012-256/section-{{section}}.html",
		"provision_label": "r.",
	},
	"canada.rad_rules": {
		"aliases": ("Refugee Appeal Division Rules", "RAD Rules"),
		"french_aliases": ("Règles de la Section d'appel des réfugiés",),
		"citation": "Refugee Appeal Division Rules, SOR/2012-257",
		"url": f"{_JUSTICE}/regulations/SOR-2012-257/section-{{section}}.html",
		"provision_label": "r.",
	},
	"canada.id_rules": {
		"aliases": ("Immigration Division Rules", "ID Rules"),
		"french_aliases": ("Règles de la Section de l'immigration",),
		"citation": "Immigration Division Rules, SOR/2002-229",
		"url": f"{_JUSTICE}/regulations/SOR-2002-229/section-{{section}}.html",
		"provision_label": "r.",
	},
	"canada.iad_rules_2022": {
		"aliases": ("Immigration Appeal Division Rules, 2022",),
		"citation": "Immigration Appeal Division Rules, 2022, SOR/2022-277",
		"url": f"{_JUSTICE}/regulations/SOR-2022-277/section-{{section}}.html",
		"provision_label": "r.",
	},
	"canada.iad_rules": {
		"aliases": ("Immigration Appeal Division Rules", "IAD Rules"),
		"french_aliases": ("Règles de la Section d'appel de l'immigration",),
		"citation": "Immigration Appeal Division Rules, SOR/2002-230",
		"url": f"{_JUSTICE}/regulations/SOR-2002-230/section-{{section}}.html",
		"provision_label": "r.",
	},
	"canada.interpretation_act": {
		"aliases": ("Interpretation Act",),
		"french_aliases": ("Loi d'interprétation",),
		"citation": "Interpretation Act, R.S.C. 1985, c. I-21",
		"url": f"{_JUSTICE}/acts/I-21/section-{{section}}.html",
	},
	"canada.canada_evidence_act": {
		"aliases": ("Canada Evidence Act",),
		"french_aliases": ("Loi sur la preuve au Canada",),
		"citation": "Canada Evidence Act, R.S.C. 1985, c. C-5",
		"url": f"{_JUSTICE}/acts/C-5/section-{{section}}.html",
	},
	"canada.constitution_act_1982": {
		"aliases": ("Constitution Act, 1982",),
		"french_aliases": ("Loi constitutionnelle de 1982",),
		"citation": "Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c. 11",
	},
	"canada.constitution_act_1867": {
		"aliases": ("Constitution Act, 1867",),
		"french_aliases": ("Loi constitutionnelle de 1867",),
		"citation": "Constitution Act, 1867, 30 & 31 Vict., c. 3",
	},
	"international.refugee_protocol": {
		"aliases": ("Protocol relating to the Status of Refugees", "1967 Protocol"),
		"french_aliases": ("Protocole relatif au statut des réfugiés",),
		"citation": "Protocol relating to the Status of Refugees, 606 U.N.T.S. 267",
		"kind": "instrument",
		"provision_label": "art.",
	},
	"international.cat": {
		"aliases": (
			"Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment",
			"Convention Against Torture",
		),
		"french_aliases": (
			"Convention contre la torture et autres peines ou traitements cruels, inhumains ou dégradants",
		),
		"citation": "Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, Can. T.S. 1987 No. 36",
		"kind": "instrument",
		"provision_label": "art.",
	},
	"international.iccpr": {
		"aliases": ("International Covenant on Civil and Political Rights", "ICCPR"),
		"french_aliases": ("Pacte international relatif aux droits civils et politiques",),
		"citation": "International Covenant on Civil and Political Rights, 999 U.N.T.S. 171",
		"kind": "instrument",
		"provision_label": "art.",
	},
	"international.crc": {
		"aliases": ("Convention on the Rights of the Child",),
		"french_aliases": ("Convention relative aux droits de l'enfant",),
		"citation": "Convention on the Rights of the Child, Can. T.S. 1992 No. 3",
		"kind": "instrument",
		"provision_label": "art.",
	},
	"international.vienna_convention": {
		"aliases": ("Vienna Convention on the Law of Treaties", "Vienna Convention"),
		"citation": "Vienna Convention on the Law of Treaties, Can. T.S. 1980 No. 37",
		"kind": "instrument",
		"provision_label": "art.",
	},
	"international.un_charter": {
		"aliases": ("Charter of the United Nations", "United Nations Charter"),
		"citation": "Charter of the United Nations",
		"kind": "instrument",
		"provision_label": "art.",
	},
	"international.udhr": {
		"aliases": ("Universal Declaration of Human Rights",),
		"french_aliases": ("Déclaration universelle des droits de l'homme",),
		"citation": "Universal Declaration of Human Rights, GA Res 217A (III)",
		"kind": "instrument",
		"provision_label": "art.",
	},
}

# French names and short forms for instruments pass one already knows.
_EXTRA_ALIASES: dict[str, dict[str, tuple[str, ...]]] = {
	"canada.irpa": {
		"aliases": ("Immigration and Refugee Protection Act",),
		"french_aliases": ("Loi sur l'immigration et la protection des réfugiés", "LIPR"),
	},
	"canada.irpr": {
		"aliases": ("Immigration and Refugee Protection Regulations",),
		"french_aliases": ("Règlement sur l'immigration et la protection des réfugiés", "RIPR"),
	},
	"canada.charter": {
		"aliases": ("Canadian Charter",),
		"french_aliases": ("Charte canadienne des droits et libertés", "Charte"),
	},
	"canada.criminal_code": {"french_aliases": ("Code criminel",)},
	"canada.citizenship_act": {"french_aliases": ("Loi sur la citoyenneté",)},
	"canada.federal_courts_act": {"french_aliases": ("Loi sur les Cours fédérales",)},
	"canada.federal_courts_rules": {"french_aliases": ("Règles des Cours fédérales",)},
	"canada.immigration_act": {"aliases": ("Immigration Act, 1976",), "french_aliases": ("Loi sur l'immigration",)},
	"international.refugee_convention": {
		"aliases": ("Convention relating to the Status of Refugees", "1951 Convention", "Refugee Convention"),
		"french_aliases": ("Convention relative au statut des réfugiés",),
	},
}

# Treaties in pass one's registry are "instrument" rows, not statutes.
_TREATY_KEYS = {"international.refugee_convention"}


def _build_registry() -> dict[str, Instrument]:
	registry: dict[str, Instrument] = {}
	for key, definition in LEGISLATION_REGISTRY.items():
		extra = _EXTRA_ALIASES.get(key, {})
		aliases = tuple(dict.fromkeys((*definition["aliases"], *extra.get("aliases", ()))))  # type: ignore[misc]
		url = definition.get("url")
		is_treaty = key in _TREATY_KEYS
		registry[key] = Instrument(
			key=key,
			citation=str(definition.get("citation") or aliases[0]),
			aliases=aliases,
			french_aliases=tuple(extra.get("french_aliases", ())),
			url_template=url if isinstance(url, str) else None,
			kind="instrument" if is_treaty else "statute",
			provision_label="art." if is_treaty else "s.",
		)
	for key, definition in _EXTRA_INSTRUMENTS.items():
		registry[key] = Instrument(
			key=key,
			citation=str(definition["citation"]),
			aliases=tuple(definition["aliases"]),  # type: ignore[arg-type]
			french_aliases=tuple(definition.get("french_aliases", ())),  # type: ignore[arg-type]
			url_template=definition.get("url") if isinstance(definition.get("url"), str) else None,  # type: ignore[arg-type]
			kind=str(definition.get("kind", "statute")),
			provision_label=str(definition.get("provision_label", "s.")),
		)
	return registry


REGISTRY: dict[str, Instrument] = _build_registry()

# Short forms matched case-sensitively: acronyms, and "Charter" (not "charter flight").
_ACRONYMS = {
	"IRPA",
	"IRPR",
	"LIPR",
	"RIPR",
	"ICCPR",
	"RPD Rules",
	"RAD Rules",
	"ID Rules",
	"IAD Rules",
	"Charter",
	"Charte",
	"Canadian Charter",
}


def _alias_pairs() -> list[tuple[str, str, str]]:
	pairs: list[tuple[str, str, str]] = []
	for key, instrument in REGISTRY.items():
		for alias in instrument.aliases:
			pairs.append((alias, key, "en"))
		for alias in instrument.french_aliases:
			pairs.append((alias, key, "fr"))
	# Longest first so "Federal Courts Citizenship, ... Rules" beats "Federal Courts Rules"
	# and "Charter of the United Nations" beats "Charter".
	pairs.sort(key=lambda item: (-len(item[0]), item[0]))
	return pairs


ALIAS_PAIRS = _alias_pairs()
_ALIAS_LOOKUP = {alias.casefold().replace("’", "'"): (key, language) for alias, key, language in ALIAS_PAIRS}


def _alias_fragment(alias: str) -> str:
	escaped = re.escape(alias).replace("'", "['’]").replace(r"\ ", r"\s+")
	if alias in _ACRONYMS:
		return f"(?-i:{escaped})"
	return escaped


INSTRUMENT_ALIAS_PATTERN = "|".join(_alias_fragment(alias) for alias, _key, _lang in ALIAS_PAIRS)
INSTRUMENT_ALIAS_RE = re.compile(rf"(?<![\w'’])(?:{INSTRUMENT_ALIAS_PATTERN})(?![\w'’])", re.IGNORECASE)


def lookup_alias(name: str) -> tuple[str, str] | None:
	"""Return (instrument_key, language) for an exact alias, ignoring case and spacing."""
	key = " ".join(name.split()).casefold().replace("’", "'")
	return _ALIAS_LOOKUP.get(key)


def identify_instrument(text: str) -> tuple[Instrument, str, re.Match[str]] | None:
	"""Find the first (longest at that position) registered instrument named in ``text``."""
	match = INSTRUMENT_ALIAS_RE.search(text or "")
	if match is None:
		return None
	found = lookup_alias(match.group(0))
	if found is None:
		return None
	key, language = found
	return REGISTRY[key], language, match
