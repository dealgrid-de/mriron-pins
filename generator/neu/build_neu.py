# -*- coding: utf-8 -*-
"""Neue Pins (ab Nr. 295) für die eduki-Materialien, die seit dem 29.10.2026 dazugekommen sind."""
import os, sys, json, re, csv, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "ueb", "MrIron_Pinterest", "generator")
sys.path.insert(0, GEN); sys.path.insert(0, HERE)
import pin as P, texts as T
from meta_neu import M

OUT = os.path.join(HERE, "out"); PINS = os.path.join(OUT, "pins"); os.makedirs(PINS, exist_ok=True)
os.makedirs(os.path.join(GEN, "html"), exist_ok=True)
REPO = "https://raw.githubusercontent.com/dealgrid-de/mriron-pins/main/pins/"

# Cover fehlt sauber (nur mit eduki-Wasserzeichen) oder eduki zeigt das falsche Cover
PENDING = {"2360804", "2360857", "2360873", "2360889", "2360904", "2360916", "2360933", "2377946",
           "2378126", "2381409", "2381560", "2393325", "2393480", "2394321", "2400480", "2411759", "2366382"}
RESERVE = {"2366307": "ab 15.10.2027 (9. November)"}
RESERVE_B = {"2372181": "ab 15.10.2027 (St. Martin)"}
FIX = {  # (A-Datum, A-Zeit, B-Datum, B-Zeit)
    "2372181": ("2026-11-10", "08:00", None, None),
    "2366342": ("2026-11-10", "12:30", "2026-11-21", "12:30"),
    "2366359": ("2026-11-20", "08:00", "2026-12-04", "08:00"),
    "2372169": ("2026-11-24", "08:00", "2026-12-14", "08:00"),
    "2347304": ("2027-01-08", "08:00", "2027-01-22", "08:00"),
}
PRIO = ["2378046", "2411880", "2411876", "2411867", "2380390", "2377937", "2358857", "2395385", "2377955",
        "2380377", "2395435", "2380403", "2411874", "2411856", "2411875", "2411863", "2410961", "2390695", "2395212"]
SLOTS = ["08:00", "12:30", "14:00", "21:30"]
START = dt.date(2026, 11, 10)

CLEAN = {
    "2390695": "Neuer Wehrdienst 2026: Pflicht, Freiheit, Gewissen",
    "2393325": "Jugendkriminalität: Jugendstrafrecht und Gericht",
    "2393480": "Kostenlos: Jugendkriminalität – Jugendstrafrecht",
    "2394321": "Kostenlos: Social-Media-Verbot für Kinder und Jugendliche",
    "2395212": "Antisemitismus erkennen: Gemeinschaftskunde 8–10",
    "2395325": "Kostenlos: Antisemitismus erkennen",
    "2390315": "Kostenlos: Extremismus erkennen – Demokratie schützen",
    "2400480": "Praktikumsbericht und Praktikumsmappe",
    "2378096": "Rico, Oskar und die Tieferschatten: Lektüre Klasse 5/6",
    "2383061": "Die Tribute von Panem: Lektüre Klasse 10",
    "2374198": "Elternsprechtag: Elterngespräch vorbereiten",
    "2372181": "Kostenlos: St. Martin – Teilen, mit Malvorlage und Laterne",
    "2372169": "Kostenlos: Weihnachtsfrieden 1914 – Stille Nacht an der Front",
    "2410319": "Harry Potter und der Stein der Weisen: Lektüre Klasse 5/6",
    "2402298": "Eine Weile bleibt die Zeit für uns stehen: Lektüre HSA 2028",
    "2402314": "Kostenlos: Eine Weile bleibt die Zeit stehen – Lektüre-Probe",
    "2366359": "Kostenlos: Tag der Menschenrechte – 30 Artikel",
}
BOARD_KL = "Klassenlehrerstunde Klasse 5–10"


def load():
    nw = {str(m["id"]): m for m in json.load(open(os.path.join(HERE, "neu.json")))}
    L = []
    for mid, (fach, kl, typ, niv, kurz, kw) in M.items():
        e = nw[mid]
        title = CLEAN.get(mid, e["t"]).replace("Bastelvolage", "Bastelvorlage")
        L.append(dict(id=mid, title=title, price=e["p"], pages=e["pg"], fach=fach, klasse=kl, typ=typ,
                      url=f"https://eduki.com/de/material/{mid}/{e['s']}", kurz=kurz, keywords=kw, niveaus=niv,
                      loesungen=True, lehrerheft=typ in ("lernjob", "lektuere", "paket", "ka"),
                      seiten=e["pg"], anzahl=e.get("n"), meta=True,
                      cover=os.path.join(HERE, "covers_neu", f"{mid}.jpg")))
    return L


# kleine Ergänzungen zum bestehenden Generator
_old_checks = P.checks_of
def checks_of(m):
    c = _old_checks(m)
    if m["typ"] == "ka":
        c[0] = "Klassenarbeit A/B mit Erwartungshorizont"
    if m["typ"] == "paket" and m.get("anzahl"):
        c[0] = f"{m['anzahl']} Materialien im Paket"
    if m["id"] == "2378046":
        c[0] = "42 Lernjobs + 6 Klassenarbeiten"
    return c
P.checks_of = checks_of

_old_board = T.board_for
def board_for(m, v):
    if m["typ"] == "gratis" and v == "B":
        return T.BOARDS[10][0]
    if m["fach"] == "Fächerübergreifend":
        return T.BOARDS[10][0] if m["typ"] == "gratis" else BOARD_KL
    if m["fach"] == "Deutsch" and m["klasse"].startswith("5"):
        return T.BOARDS[0][0]
    return _old_board(m, v)
T.board_for = board_for

# B-Pin: Teilthema nicht weglassen, sonst sehen alle Teile einer Reihe gleich aus
import inspect, textwrap
_src = inspect.getsource(P.var_b).replace(
    'topic = f"{a}: {b}" if b and len(a) + len(b) < 44 else a',
    'topic = (f"{a}: {b}" if len(a) + len(b) < 58 else b) if b else a')
exec(compile(_src, "var_b", "exec"), P.__dict__)


def interleave(items):
    from collections import OrderedDict, deque
    g = OrderedDict()
    for it in items: g.setdefault(it["board"], deque()).append(it)
    out = []
    while any(g.values()):
        for q in g.values():
            if q: out.append(q.popleft())
    return out


def plan(L):
    byid = {m["id"]: m for m in L}
    act = [m for m in L if m["id"] not in PENDING]
    taken = {}  # (date,time) -> pin
    pins = []
    def put(m, v, d, t, board=None):
        p = dict(m=m, v=v, board=board or T.board_for(m, v), date=d, time=t); taken[(d, t)] = p; pins.append(p); return p
    a_day = {}
    for mid, (ad, at, bd, bt) in FIX.items():
        if mid in PENDING: continue
        put(byid[mid], "A", dt.date.fromisoformat(ad), at); a_day[mid] = dt.date.fromisoformat(ad)
        if bd: put(byid[mid], "B", dt.date.fromisoformat(bd), bt)
    res = []
    for m in act:
        if m["id"] in RESERVE:
            res += [dict(m=m, v=v, board=T.board_for(m, v), date=None, time=None, note=RESERVE[m["id"]]) for v in ("A", "B")]
        if m["id"] in RESERVE_B:
            res.append(dict(m=m, v="B", board=T.board_for(m, "B"), date=None, time=None, note=RESERVE_B[m["id"]]))
    skip = set(FIX) | set(RESERVE)
    A = [dict(m=m, v="A", board=T.board_for(m, "A")) for m in act if m["id"] not in skip]
    pr = {k: i for i, k in enumerate(PRIO)}
    A_q = sorted([p for p in A if p["m"]["id"] in pr], key=lambda p: pr[p["m"]["id"]]) + interleave([p for p in A if p["m"]["id"] not in pr])
    B_q = interleave([dict(m=m, v="B", board=T.board_for(m, "B")) for m in act if m["id"] not in skip])
    day = START
    while A_q or B_q:
        for i, s in enumerate(SLOTS):
            if (day, s) in taken: continue
            src = None
            if B_q and (i % 2 == 1 or not A_q):
                for j, p in enumerate(B_q):
                    d0 = a_day.get(p["m"]["id"])
                    if d0 and (day - d0).days >= 21: src = j; break
            if src is not None:
                p = B_q.pop(src)
            elif A_q:
                p = A_q.pop(0); a_day[p["m"]["id"]] = day
            else:
                continue
            put(p["m"], p["v"], day, s, p["board"])
        day += dt.timedelta(days=1)
        if day > dt.date(2027, 6, 30): break
    pins.sort(key=lambda p: (p["date"], p["time"]))
    pins += res
    for i, p in enumerate(pins, 295):
        m, v = p["m"], p["v"]
        p.update(nr=i, file=f"{i:03d}_{m['id']}_{v}.jpg", title=T.pin_title(m, v), desc=T.description(m, v),
                 alt=T.alt_text(m, v), kw=T.keywords(m), link=m["url"])
    seen = set(r["Titel"] for r in json.load(open(os.path.join(HERE, "ueb", "MrIron_Pinterest", "plan.json"), encoding="utf-8")))
    for p in pins:
        t = p["title"]; k = 2
        while p["title"] in seen:
            p["title"] = T.cut(t, 92) + f" ({'Vorschau' if k == 2 else k})"; k += 1
        seen.add(p["title"])
    return pins, [byid[i] for i in M if i in PENDING]


if __name__ == "__main__":
    L = load(); pins, pend = plan(L)
    print(len(pins), "Pins;", pins[0]["date"], "bis", max(p["date"] for p in pins if p["date"]), "; offen:", len(pend))
    if "--render" in sys.argv:
        from render import shoot
        jobs = []
        for p in pins:
            html = P.var_a(p["m"]) if p["v"] == "A" else P.var_b(p["m"])
            jobs.append((html, os.path.join(PINS, p["file"])))
        only = [a for a in sys.argv if a.startswith("--only=")]
        if only:
            n = int(only[0].split("=")[1]); jobs = jobs[:n]
        shoot(jobs)
    rows = []
    for p in pins:
        m = p["m"]
        rows.append({"Nr": p["nr"], "Datum": p["date"].isoformat() if p["date"] else "Reserve: " + p["note"],
                     "Uhrzeit": p["time"] or "", "Datei": p["file"], "Variante": {"A": "Cover", "B": "Darum geht's"}[p["v"]],
                     "Pinnwand": p["board"], "Titel": p["title"], "Beschreibung": p["desc"], "Link": p["link"],
                     "Alt-Text": p["alt"], "Keywords": ", ".join(p["kw"]), "Material": m["title"], "Fach": m["fach"],
                     "Klasse": m["klasse"], "Status": "geplant"})
    json.dump(rows, open(os.path.join(OUT, "plan_neu.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump([{"id": m["id"], "title": m["title"], "url": m["url"]} for m in pend], open(os.path.join(OUT, "offen.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(r["Pinnwand"] for r in rows))
    for r in rows[:6] + rows[-4:]: print(r["Nr"], r["Datum"], r["Uhrzeit"], r["Variante"], r["Titel"], "|", r["Pinnwand"])
