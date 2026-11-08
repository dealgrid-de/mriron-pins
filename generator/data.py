# -*- coding: utf-8 -*-
"""Materialdaten (eduki, Stand 29.10.2026) + Ableitungen für Pins."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))

BUNDLES = {
    "2346079": ("Abschlussprüfung Deutsch 2027: Komplettpaket 6 in 1", "Deutsch", "10", "deutsch-abschlusspruefung-10-realschule-bw-2027-komplettpaket"),
    "2308713": ("Mathe Klasse 5: Paket mit 8 Lernjobs", "Mathe", "5", "mathe---klasse-5---paket-zahlen-rechnen-groessen-geometrie-brueche"),
    "2340111": ("WBS Klasse 7–9: Paket mit 10 Lernjobs", "WBS", "7–9", "wbs-klasse-7-9-bundle-9-lernjobs-geld-markt-arbeit-beruf"),
    "2295902": ("Medienbildung Klasse 5–9: Paket mit 4 Lernjobs", "Medienbildung", "5–9", "ium-kl-5-9-4-lernjobs-zu-medien-infos-ki-und-gaming-g-m-e"),
    "2338309": ("Aufsatz Klasse 7/8: Paket mit 5 Schreibformen", "Deutsch", "7/8", "aufsatz-bundle-bericht-zusammenfassung-brief-kommentar-7-8-deutsch-realschule"),
    "2331503": ("Rechtschreibung Klasse 5/6: Komplettpaket", "Deutsch", "5/6", "rechtschreibung-kl-5-6-komplettpaket-5-lernjobs-g-m-e-check"),
    "2256710": ("Erdkunde Klasse 7–9: Paket mit 5 Lernjobs", "Erdkunde", "7–9", "erdkunde-bundle-7-9-5-lernjobs-klima-erdbeben-migration"),
    "2353527": ("Industrialisierung: Paket mit 7 Lernjobs", "Geschichte", "8", "industrialisierung-paket-mit-7-lernjobs"),
    "2353677": ("Imperialismus und Erster Weltkrieg: Paket", "Geschichte", "8", "imperialismus-und-erster-weltkrieg-paket"),
}

ANZ = {"2346079": 6, "2308713": 8, "2340111": 10}

# Fach aus Titel-Stichwörtern (Fallback, wenn eduki-Metadaten fehlen)
FACH_RULES = [
    (r"Lektüre|Argumentier|Rechtschreib|Zeichensetzung|Nominalisierung|Satzglied|Zeitformen|Brief|Bericht|Stellungnahme|Zusammenfassung|Vorgangsbeschreibung|Dehnung|Schärfung|Ableiten|ss oder ß|Doppelkonsonant|Großschreibung|Kurzgeschicht|Ballade|Realschulabschluss Deutsch|Schreib|Formulierungshilf|Wörtliche Rede|Prädikat|Präteritum|Erebos|Weggesperrt|Tunnelbauer|Windstärke", "Deutsch"),
    (r"Erster Weltkrieg|Industrialisierung|Kaiserreich|Imperialismus|Weimarer|Nationalsozialismus|Zwischenkriegszeit", "Geschichte"),
    (r"Mathe|Multiplikation|Addition|Zahlen|Geometrie|Brüche|Flächeninhalt|Größen|Daten und Diagramme", "Mathe"),
    (r"Klimawandel|Globalisierung|Verstädterung|Plattentektonik|Disparitäten", "Erdkunde"),
    (r"Medienkompetenz|Mediennutzung|Gaming|Medienbildung|Künstliche Intelligenz", "Medienbildung"),
    (r"Verbraucher|Unternehmen|Schulden|Praktikum|Arbeitnehmer|Geldanlage|Bewerbung|Markt und Preis|Umgang mit Geld|Soziale Marktwirtschaft|Versicherungen|Sozialstaat|Weltwirtschaft", "WBS"),
    (r"Demokratie|Europäische Union|EU-|Rechte und Pflichten|Familie|Migration|Gesetzgebung|Kinderrechte|Gruppen|Gemeinde|Grundgesetz|Menschenrechte|Krieg und Frieden", "Gemeinschaftskunde"),
    (r"Halloween|Weihnachten", "Fächerübergreifend"),
]
FARBE = {"Deutsch": "#B8336A", "Geschichte": "#B5600F", "Gemeinschaftskunde": "#137485", "WBS": "#3E9A5A",
         "Erdkunde": "#1C9AAE", "Mathe": "#7A5BC7", "Medienbildung": "#1E4A6E", "Fächerübergreifend": "#F0612E"}


FACH_OVR = {"2255714": "Gemeinschaftskunde", "2341723": "Gemeinschaftskunde", "2341693": "Gemeinschaftskunde",
            "2341480": "WBS", "2341495": "WBS"}


def fach_of(title):
    for rx, f in FACH_RULES:
        if re.search(rx, title, re.I):
            return f
    return "Fächerübergreifend"


def typ_of(title, price, mid):
    if mid in BUNDLES: return "paket"
    if price == 0: return "gratis"
    if "Stunde to Go" in title: return "togo"
    if "Lektüre" in title or "Akte Anja" in title: return "lektuere"
    if title.startswith("Realschulabschluss"): return "pruefung"
    if title.startswith("Klassenarbeit"): return "ka"
    return "lernjob"


def klasse_from(s):
    m = re.search(r"(?:Klasse|Kl\.)\s*(\d+(?:\s*[/–-]\s*\d+)?)", s)
    return m.group(1).replace(" ", "").replace("-", "–") if m else ""


def norm_kl(k):
    k = (k or "").replace("Klasse", "").replace(".", "").replace(" ", "").replace("-", "–")
    m = re.findall(r"\d+", k)
    if not m: return ""
    if len(m) == 1: return m[0]
    if len(m) == 2 and int(m[1]) - int(m[0]) == 1: return f"{m[0]}/{m[1]}"
    return f"{m[0]}–{m[-1]}"


def load():
    meta = {}
    for part in ("meta_part1.json", "meta_part2.json"):
        p = os.path.join(HERE, "work", part)
        if os.path.exists(p):
            try: meta.update(json.load(open(p, encoding="utf-8")))
            except Exception as e: print("meta-Fehler", part, e)
    out = []
    for line in open(os.path.join(HERE, "work", "materials_raw.txt"), encoding="utf-8"):
        line = line.strip()
        if not line: continue
        mid, title, price, pages = (line.split("|") + [""])[:4]
        price = 0.0 if price == "0" else float(price.replace(",", "."))
        m = meta.get(mid, {})
        if mid in BUNDLES:
            title, fach, kl, slug = BUNDLES[mid]
            url = m.get("url") or f"https://eduki.com/de/material/{mid}/{slug}"
            if m.get("klasse"): kl = norm_kl(m["klasse"])
        else:
            fach = FACH_OVR.get(mid) or fach_of(title)
            kl = norm_kl(m.get("klasse")) or klasse_from(title)
            url = m.get("url") or f"https://eduki.com/de/material/{mid}"
        url = url.split("?")[0]
        out.append(dict(id=mid, title=title, price=price, pages=pages, fach=fach, klasse=kl,
                        typ=typ_of(title, price, mid), url=url, kurz=m.get("kurz", ""), keywords=m.get("keywords", []),
                        niveaus=m.get("niveaus", ""), loesungen=bool(m.get("loesungen")), lehrerheft=bool(m.get("lehrerheft")),
                        seiten=m.get("seiten") or pages, anzahl=m.get("anzahl") or ANZ.get(mid), meta=bool(m),
                        cover=os.path.join(HERE, "covers", f"{mid}.webp")))
    return out


if __name__ == "__main__":
    from collections import Counter
    L = load(); print(len(L)); print(Counter(x["fach"] for x in L)); print(Counter(x["typ"] for x in L))
    print("ohne Meta:", [x["id"] for x in L if not x["meta"]][:200])
    print("ohne Klasse:", [x["id"] for x in L if not x["klasse"]])
