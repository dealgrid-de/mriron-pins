# -*- coding: utf-8 -*-
"""Pin-Texte (Titel ≤100, Beschreibung ≤500, Alt-Text ≤500), Pinnwand-Zuordnung, Keywords."""
import re

BOARDS = [
    ("Deutsch Klasse 5 und 6", "Arbeitsblätter und Lernjobs für Deutsch in Klasse 5 und 6: Rechtschreibung, Zeichensetzung, Grammatik, Satzglieder, Zeitformen und Stunden to go – differenziert in G, M und E, mit Lösungen. Für Realschule und Gemeinschaftsschule, Bildungsplan Baden-Württemberg."),
    ("Deutsch Klasse 7 und 8", "Deutschunterricht Klasse 7 und 8: Bericht, Beschreibung, Zusammenfassung, Stellungnahme, Brief, Balladen und Kurzgeschichten. Fertige Lernjobs und Arbeitsblätter mit Lösungen für Realschule und Gemeinschaftsschule in BW."),
    ("Abschlussprüfung Deutsch 2027", "Prüfungsvorbereitung Deutsch für Realschulabschluss und Hauptschulabschluss 2027 in Baden-Württemberg: Pflichtlektüren, Argumentieren, Sachtexte, Rechtschreibung und Probeklausuren – mit Lösungen und Klassenarbeiten."),
    ("Geschichte Unterricht Klasse 7–9", "Geschichtsunterricht Klasse 7 bis 9: Industrialisierung, Kaiserreich, Imperialismus, Erster Weltkrieg, Weimarer Republik und Nationalsozialismus. Lernjobs mit Quellen, Karikaturen und Lösungen, differenziert in G und M."),
    ("Gemeinschaftskunde Unterricht", "Gemeinschaftskunde und Politik für Klasse 7 bis 10: Grundrechte, Demokratie, Gemeinde, Gesetzgebung, EU, Kinderrechte, Migration, Familie und Frieden. Lernjobs mit Lösungen nach Bildungsplan BW."),
    ("WBS Unterricht – Wirtschaft und Beruf", "Wirtschaft / Berufs- und Studienorientierung (WBS) Klasse 7 bis 10: Geld, Konto, Kredite, Markt und Preis, Verbraucherrechte, Arbeitnehmer, Versicherungen, Praktikum und Bewerbung. Lernjobs mit Lösungen."),
    ("Erdkunde Unterricht Klasse 7–9", "Erdkunde und Geographie Klasse 7 bis 9: Klimawandel, Plattentektonik, Erdbeben und Vulkane, Megastädte, Globalisierung und globale Disparitäten. Fertige Lernjobs in zwei Niveaus mit Lösungen."),
    ("Mathe Klasse 5", "Mathe Klasse 5: große Zahlen, Rechnen, Größen, Geometrie, Flächeninhalt, Daten und Brüche. Lernjobs in drei Niveaus mit Lösungen und Stationenlernen."),
    ("Medienbildung und Informatik", "Medienbildung, Informatik und Medienkompetenz Klasse 5 bis 9: Fake News, KI und Chatbots, Gaming, Werbung und Datenschutz, Infos suchen und prüfen. Lernjobs mit Lösungen."),
    ("Cyber Sale – Angebote", "Aktuelle Angebote für Unterrichtsmaterial: Im eduki Cyber Sale vom 15. bis 17. November 2026 gibt es 20 % auf alle Materialien – Lernjobs, Pakete und Lektüre-Material für Klasse 5 bis 10."),
    ("Kostenlose Arbeitsblätter", "Kostenlose Arbeitsblätter und Gratis-Proben für Klasse 5 bis 10: Deutsch, Geschichte, Gemeinschaftskunde, WBS, Mathe und mehr – mit Lösungen, sofort einsetzbar."),
]
BOARD_OF_FACH = {"Geschichte": 3, "Gemeinschaftskunde": 4, "WBS": 5, "Erdkunde": 6, "Mathe": 7, "Medienbildung": 8}


def board_for(m, variant):
    if variant == "S":
        return BOARDS[9][0]
    if m["typ"] == "gratis" and variant == "B":
        return BOARDS[10][0]
    f = m["fach"]
    if f == "Deutsch":
        if m["typ"] in ("lektuere", "pruefung") or "2027" in m["title"] or m["id"] == "2346079":
            return BOARDS[2][0]
        k = m["klasse"]
        if k.startswith("5") or k.startswith("6"):
            return BOARDS[0][0]
        if k.startswith("9") or k.startswith("10"):
            return BOARDS[2][0]
        return BOARDS[1][0]
    if f == "Fächerübergreifend":
        return BOARDS[10][0] if m["typ"] == "gratis" else BOARDS[0][0]
    return BOARDS[BOARD_OF_FACH.get(f, 10)][0]


TYPWORT = {"lernjob": "Lernjob", "gratis": "Gratis-Probe", "paket": "Paket", "lektuere": "Lektüre-Material",
           "pruefung": "Prüfungstraining", "togo": "Stunde to go", "ka": "Klassenarbeit"}


def kl(m):
    return f"Klasse {m['klasse']}" if m["klasse"] else ""


def niv(m):
    nv = [p for p in re.split(r"[\s,/]+|und", m.get("niveaus") or "") if p in ("G", "M", "E")]
    if not nv: return ""
    return ("Niveau " + nv[0]) if len(nv) == 1 else ("Niveaus " + ", ".join(nv[:-1]) + " und " + nv[-1])


def cut(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= n: return s
    s = s[:n - 1]
    return s[:s.rfind(" ")].rstrip(",;:–-") + "…"


def clean_title(t):
    return re.sub(r"^Kostenlos:\s*", "", t)


def pin_title(m, v):
    t = clean_title(m["title"]); k = kl(m); fach = m["fach"] if m["fach"] != "Fächerübergreifend" else ""
    if v == "S":
        return cut(f"Cyber Sale 15.–17.11.: {t} 20 % günstiger", 100)
    if v == "A":
        if m["typ"] == "gratis":
            s = f"Kostenlos: {t}" + (f" – {fach} {k}" if k and "Klasse" not in t and "Kl." not in t else "") + " mit Lösungen"
        elif m["typ"] == "paket":
            s = f"{t} – Unterrichtsmaterial mit Lösungen"
        else:
            s = f"{t} – Arbeitsblätter mit Lösungen" + (f" {k}" if k and "Klasse" not in t and "Kl." not in t else "")
    else:
        hook = {"lernjob": "fertiger Lernjob zum Ausdrucken", "gratis": "gratis Arbeitsblatt zum Testen",
                "paket": "komplette Unterrichtsreihe", "lektuere": "Lektüre-Prüfungstraining",
                "pruefung": "Training für die Abschlussprüfung", "togo": "fertige Stunde ohne Vorbereitung",
                "ka": "Klassenarbeit mit Erwartungshorizont"}[m["typ"]]
        fk = " ".join(x for x in [fach if fach and fach not in t else "", k if "Klasse" not in t and "Kl." not in t else ""] if x)
        s = f"{t} – {fk}: {hook}" if fk else f"{t}: {hook}"
        if len(s) > 100: s = f"{t}: {hook}"
        if len(s) > 100: s = f"{t} – {fk}" if fk else t
    return cut(s, 100)


HASH = {"Deutsch": "#Deutschunterricht", "Geschichte": "#Geschichtsunterricht", "Gemeinschaftskunde": "#Gemeinschaftskunde",
        "WBS": "#WBS", "Erdkunde": "#Erdkunde", "Mathe": "#Matheunterricht", "Medienbildung": "#Medienbildung", "Fächerübergreifend": "#Grundschule"}


def tail(m):
    return f" eduki-ID {m['id']}. #Unterrichtsmaterial {HASH.get(m['fach'], '')} #Realschule".replace("  ", " ")


def description(m, v):
    k = kl(m); n = niv(m)
    kurz = (m.get("kurz") or "").rstrip(".") + "." if m.get("kurz") else ""
    facts = TYPWORT[m["typ"]] + (f" für {m['fach']}" if m["fach"] != "Fächerübergreifend" else " fächerübergreifend") + (f" {k}" if k else "")
    extra = [x for x in [n, (f"{m['seiten']} Seiten" if m.get("seiten") else ""),
                         ("mit Lösungen und Lehrerheft" if m.get("loesungen") and m.get("lehrerheft") else ("mit Lösungen" if m.get("loesungen") else ("mit Lehrerheft" if m.get("lehrerheft") else "")))] if x]
    if m["typ"] == "paket" and m.get("anzahl"): extra.insert(0, f"{m['anzahl']} Materialien")
    facts += (": " + ", ".join(extra) if extra else "") + "."
    sale = f"Cyber Sale auf eduki vom 15. bis 17. November 2026: 20 % auf alle Materialien, auch auf dieses."
    cta = ("Jetzt vormerken und im Sale zugreifen." if v == "S" else
           "Kostenlos auf eduki herunterladen." if m["typ"] == "gratis" else "Jetzt auf eduki ansehen und Vorschau öffnen.")
    bw = "Für Realschule, Gemeinschaftsschule und Werkrealschule, passend zum Bildungsplan Baden-Württemberg."
    selbst = "Ausdrucken, austeilen, loslegen – die Klasse arbeitet selbstständig."
    tl = tail(m)
    # (Text, Pflicht?) in Lesereihenfolge
    seq = ([(sale, True)] if v == "S" else []) + [(kurz, True)] + ([(selbst, False)] if v == "B" and m["typ"] != "gratis" else []) \
        + [(facts, True), (bw, False), (cta, True)]
    seq = [(s, req) for s, req in seq if s]
    budget = 500 - len(tl)
    def total(items): return len(" ".join(s for s, _ in items))
    items = list(seq)
    for drop in [s for s, req in reversed(seq) if not req]:
        if total(items) <= budget: break
        items = [(s, r) for s, r in items if s != drop]
    if total(items) > budget and kurz:
        over = total(items) - budget
        short = cut(kurz, max(60, len(kurz) - over - 2)).rstrip("…").rstrip(",;: ") + "."
        items = [(short if s == kurz else s, r) for s, r in items]
    return cut(" ".join(s for s, _ in items), budget) + tl


def alt_text(m, v):
    what = {"A": "Cover", "B": "Inhaltsbeschreibung und Cover", "S": "Cyber-Sale-Hinweis (20 %) und Cover"}[v]
    return cut(f"Pin mit {what} des Unterrichtsmaterials „{clean_title(m['title'])}“ für {m['fach']}" + (f", {kl(m)}" if m["klasse"] else "") + ", von Mr. Iron auf eduki.", 500)


def keywords(m):
    kw = list(m.get("keywords") or [])
    base = clean_title(m["title"]).split(":")[0].split(" – ")[0]
    for x in [base, f"{m['fach']} {kl(m)}".strip(), f"{m['fach']} Arbeitsblätter", "Unterrichtsmaterial", "Realschule BW"]:
        if x and x not in kw: kw.append(x)
    return [x for x in kw if "Ausländer" not in x][:10]
