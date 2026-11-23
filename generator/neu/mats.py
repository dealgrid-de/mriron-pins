# -*- coding: utf-8 -*-
"""Material-Pins: Foto-Szenen, Stunde to go, Freebies."""
import os, sys, json, re, csv
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import creative as C, szene as S, build_neu as B
T = B.T
F = C.FARBE
L = {m["id"]: m for m in json.load(open(os.path.join(HERE, "alle_mat.json")))}
# vollständige eduki-Links aus der Warteschlange / alten Plänen
URL = {}
for r in csv.reader(open("/home/claude/mriron-pins/csv/QUEUE_GESAMT.csv", encoding="utf-8")):
    mm = re.search(r"/material/(\d+)/", r[5] if len(r) > 5 else "")
    if mm: URL[mm.group(1)] = r[5]
for r in json.load(open(os.path.join(HERE, "ueb", "MrIron_Pinterest", "plan.json"))):
    mm = re.search(r"/material/(\d+)/", r["Link"])
    if mm: URL.setdefault(mm.group(1), r["Link"])
for m in L.values():
    m["url"] = URL.get(m["id"], m["url"])
    m["fach"] = m["fach"] or "Fächerübergreifend"

PRESETS = {  # Foto, fx, Platzierung
    "flat_laptop": (0.5, dict(quad=S.rect_quad(470, 700, 460, 613, -7))),
    "flat_wood_laptop2": (0.6, dict(quad=S.rect_quad(620, 620, 460, 613, 7))),
    "flat_notebook": (0.5, dict(quad=S.rect_quad(495, 507, 556, 741, 0), shadow=(10, 14, 16, 0.5))),
    "apple_books": (0.1, dict(quad=[[610, 560], [880, 575], [870, 935], [600, 945]], shadow=(-14, 6, 18, 0.45), sheets=2)),
    "coffee_light": (0.5, dict(quad=S.rect_quad(700, 560, 450, 600, 18))),
    "rustic_laptop": (0.5, dict(quad=S.rect_quad(560, 690, 470, 627, -6))),
    "dark_paper": (0.5, dict(quad=S.rect_quad(620, 560, 420, 560, 3), shadow=(8, 12, 14, 0.6))),
    "rustic_glasses": (0.5, dict(quad=S.rect_quad(520, 760, 460, 613, -4))),
    "light_notebook": (0.5, dict(quad=S.rect_quad(400, 690, 430, 573, 0), shadow=(8, 12, 14, 0.6))),
    "wood_book": (0.5, dict(quad=S.rect_quad(607, 523, 400, 533, -36))),
    "orange_note": (0.5, dict(quad=S.rect_quad(370, 740, 460, 613, -6))),
}
ORDER = list(PRESETS)


def core(m):
    t = re.sub(r"^Kostenlos:\s*", "", m["title"])
    return t


def kl(m):
    k = (m.get("klasse") or "").strip()
    return f"Klasse {k}" if k else ""


def pill(m):
    return " · ".join(x for x in [m["fach"] if m["fach"] != "Fächerübergreifend" else "Klassenlehrerstunde", kl(m)] if x)


def head_sticker(m):
    t = core(m); typ = m["typ"]
    if typ == "paket":
        a, _, b = t.partition(":")
        b = b.strip()
        st = re.sub(r"^(Komplettpaket|Paket|Großpaket)\s*(mit)?\s*", "", b).strip() or "Komplettpaket"
        st = st[0].upper() + st[1:] if st else st
        st = st.replace("Heften", "Hefte")
        return f"{a.strip()}: das komplette Paket", st
    if typ == "pruefung":
        teil = t.split(":")[-1].strip()
        return f"Realschulabschluss 2027: {teil} trainieren", "im Prüfungsformat"
    if typ == "lektuere":
        a, _, b = t.partition(":")
        buch = a.split(" – ")[0].strip()
        return f"{buch}: Lektüre fertig vorbereitet", b.strip()
    if typ == "ka":
        thema = t.split(":")[0].strip()
        h = thema if thema.startswith("Klassenarbeit") else f"Klassenarbeit {thema}"
        return h, f"Klassenarbeit · {kl(m)}" if kl(m) else "Klassenarbeit"
    a = t.split(" – ")[0].strip()
    return a, ("Lernjob · G · M · E" if "E" in (m.get("niveaus") or "") else f"Lernjob · {kl(m)}")


def seo_title(m, kind):
    t = core(m); f = m["fach"]; k = kl(m)
    if "Klasse" in t: k = ""
    if kind == "foto":
        s = (f"{t} – {f} {k}".strip() if k else f"{t} – Unterrichtsmaterial {f}") if f != "Fächerübergreifend" else t
        if len(s) + 24 <= 100: s += " – fertig zum Ausdrucken"
    elif kind == "togo":
        thema = re.sub(r"\s*Klasse 5/6.*", "", t)
        s = f"Vertretungsstunde Deutsch Klasse 5/6: {thema} – fertige Stunde ohne Vorbereitung"
    else:
        s = f"Freebie: {t} – kostenloses Unterrichtsmaterial {f} {k}".replace("Fächerübergreifend ", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= 100 else T.cut(s, 99)


def desc(m, kind):
    base = T.description(m, "A")
    if kind == "togo":
        base = "Morgen Vertretung oder keine Zeit zum Vorbereiten? Diese Stunde to go ist fertig: Tafelbild, Arbeitsblätter und Lösungen – ausdrucken und loslegen. " + base
    if kind == "freebie":
        base = "Kostenlos zum Testen im Unterricht. " + base
    return base


# --- Auswahl ---
foto_ids = [m["id"] for m in L.values() if m["typ"] in ("paket", "pruefung", "ka")]
foto_ids += [m["id"] for m in L.values() if m["typ"] == "lektuere" and m["id"] != "2320047"]
lj = sorted([m for m in L.values() if m["typ"] == "lernjob" and m.get("meta")], key=lambda m: -float(m.get("price") or 0))
seen_f = {}
for m in lj:
    if seen_f.get(m["fach"], 0) < 3:
        foto_ids.append(m["id"]); seen_f[m["fach"]] = seen_f.get(m["fach"], 0) + 1
    if len(foto_ids) >= 66: break
togo_ids = [m["id"] for m in L.values() if m["typ"] == "togo"]
SKIP = ("Halloween", "Weihnacht", "9. November", "Black Friday", "Menschenrechte", "St. Martin", "Neues Jahr")
free_ids = [m["id"] for m in L.values() if m["typ"] == "gratis" and not any(s in m["title"] for s in SKIP)][:36]

KICK = ["Morgen Vertretung in Klasse 5?", "Keine Zeit zum Vorbereiten?", "Montag, 1. Stunde, Klasse 6?", "Spontan eine Stunde übernehmen?", "Grammatik ohne Vorbereitung?"]


def jobs():
    out = []
    for i, mid in enumerate(foto_ids):
        m = L[mid]; ph = ORDER[i % len(ORDER)]
        out.append(dict(kind="foto", m=m, photo=ph))
    for i, mid in enumerate(togo_ids):
        out.append(dict(kind="togo", m=L[mid], kick=KICK[i % len(KICK)]))
    for mid in free_ids:
        out.append(dict(kind="freebie", m=L[mid]))
    return out


def build(j, outdir):
    m = j["m"]; col = F.get(m["fach"], C.NAVY)
    if j["kind"] == "foto":
        fx, pl = PRESETS[j["photo"]]
        sp = os.path.join(outdir, f"sz_{m['id']}.jpg")
        img = S.fit(os.path.join(HERE, "fotos", j["photo"] + ".jpg"), 1000, 1050, fx=fx)
        img = S.place(img, m["cover"], pl["quad"], **{k: v for k, v in pl.items() if k != "quad"})
        S.save(S.grain(img), sp)
        h, st = head_sticker(m)
        return C.photo(pill(m), h, sp, col if m["fach"] != "Deutsch" or j["photo"] not in ("orange_note",) else C.NAVY, st)
    if j["kind"] == "togo":
        thema = re.sub(r"\s*Klasse 5/6.*", "", core(m))
        return C.togo(j["kick"], f"{thema} – die fertige Stunde", m["cover"], col, ["Tafelbild und Arbeitsblätter", "Mit Lösungen", "Ausdrucken und loslegen"], "Deutsch · Klasse 5/6")
    t = core(m)
    title = t
    anlass = "Kostenlos zum Testen im Unterricht"
    chk = [c for c in B.P.checks_of(m) if "Kostenlos" not in c][:3] or ["Fertig zum Ausdrucken"]
    return C.freebie(anlass, title, m["cover"], col, pill(m), chk)
