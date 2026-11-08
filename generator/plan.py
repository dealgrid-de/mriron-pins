# -*- coding: utf-8 -*-
"""Veröffentlichungsplan: Reihenfolge, Datum/Uhrzeit, Dateinamen, Pinnwand, Texte. Export als JSON/XLSX/CSV."""
import os, sys, json, csv, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import data, texts

START = dt.date(2026, 10, 30)
SLOTS3 = ["15:30", "19:00", "20:30"]
SLOTS5 = ["06:30", "15:30", "17:30", "19:00", "20:30"]
RESERVE = {"2295876"}   # Halloween: erst ab September 2027 pinnen
NOTPUBLIC = {"2347278", "2347620", "2347694", "2347709"}  # auf eduki noch nicht öffentlich
PRIO = ["2346079", "2340111", "2256710", "2331503", "2338309", "2308713", "2295902", "2353527", "2353677",  # Pakete
        "2319055",                                     # Weihnachten (saisonal)
        "2305102", "2309448", "2329903", "2328670", "2320047", "2307434"]  # Prüfung 2027 / Lektüren
PRIO_B = ["2338192", "2338127", "2338170", "2338318", "2338320", "2338321", "2346079", "2305102"]  # Januar: Prüfung


def interleave(items):
    """Rundlauf über Pinnwände, damit nicht 5 Pins derselben Pinnwand hintereinander kommen."""
    from collections import OrderedDict, deque
    groups = OrderedDict()
    for it in items:
        groups.setdefault(it["board"], deque()).append(it)
    out = []
    while any(groups.values()):
        for q in groups.values():
            if q: out.append(q.popleft())
    return out


def build():
    L = data.load()
    pins = []
    for m in L:
        for v in ("A", "B"):
            pins.append(dict(m=m, v=v, board=texts.board_for(m, v)))
    res = [p for p in pins if p["m"]["id"] in RESERVE | NOTPUBLIC]
    pins = [p for p in pins if p["m"]["id"] not in RESERVE | NOTPUBLIC]
    A = [p for p in pins if p["v"] == "A"]; B = [p for p in pins if p["v"] == "B"]
    pr = {mid: i for i, mid in enumerate(PRIO)}
    A_first = sorted([p for p in A if p["m"]["id"] in pr], key=lambda p: pr[p["m"]["id"]])
    A_rest = interleave([p for p in A if p["m"]["id"] not in pr])
    A_q = A_first + A_rest
    # B: Gratis und Lernjobs gemischt; Prüfungs-B-Pins für Januar zurückhalten
    pb = set(PRIO_B)
    B_jan = [p for p in B if p["m"]["id"] in pb]
    B_q = interleave([p for p in B if p["m"]["id"] not in pb])
    sched = []; day = START; a_seen = {}
    jan = dt.date(2027, 1, 7)
    while A_q or B_q or B_jan:
        n = 3 if (day - START).days < 14 else 5
        slots = SLOTS3 if n == 3 else SLOTS5
        todays = []
        for s in slots:
            src = None
            if day >= jan and B_jan and len([t for t in todays if t["m"]["id"] in pb]) < 1:
                src = B_jan
            elif (day - START).days >= 14 and B_q and (len(todays) % 2 == 1 or not A_q):
                # B frühestens 21 Tage nach dem A-Pin desselben Materials
                for i, p in enumerate(B_q):
                    d0 = a_seen.get(p["m"]["id"])
                    if d0 and (day - d0).days >= 21:
                        src = B_q; idx = i; break
                if src is None and not A_q:
                    for i, p in enumerate(B_q):
                        d0 = a_seen.get(p["m"]["id"])
                        if d0 and (day - d0).days >= 7:
                            src = B_q; idx = i; break
            if src is B_q:
                p = B_q.pop(idx)
            elif src is B_jan:
                p = B_jan.pop(0)
            elif A_q:
                p = A_q.pop(0)
            else:
                continue
            p = dict(p, date=day, time=s); todays.append(p)
            if p["v"] == "A": a_seen[p["m"]["id"]] = day
        sched += todays
        day += dt.timedelta(days=1)
        if day > dt.date(2027, 4, 30): break
    # Cyber Sale 15.–17.11.2026: eigene Pins auf eigener Pinnwand (danach Pinnwand archivieren)
    byid = {m["id"]: m for m in L}
    sale_ids = ["2346079", "2340111", "2331503", "2338309", "2353527", "2256710", "2305102", "2309448", "2329903", "2328670",
                "2308713", "2295902", "2353677", "2307434"]
    slots = [(dt.date(2026, 11, d), "18:00") for d in range(8, 15)] + [(dt.date(2026, 11, 15), t) for t in ("07:00", "12:00", "18:00")] \
        + [(dt.date(2026, 11, 16), t) for t in ("07:00", "18:00")] + [(dt.date(2026, 11, 17), t) for t in ("07:00", "16:00")]
    for mid, (d, t) in zip(sale_ids, slots):
        sched.append(dict(m=byid[mid], v="S", board=texts.board_for(byid[mid], "S"), date=d, time=t))
    sched.sort(key=lambda p: (p["date"], p["time"]))
    for r in res:
        sched.append(dict(r, date=None, time=None))
    for i, p in enumerate(sched, 1):
        m = p["m"]; v = p["v"]
        p["nr"] = i
        p["file"] = f"{i:03d}_{m['id']}_{v}.jpg"
        p["title"] = texts.pin_title(m, v)
        p["desc"] = texts.description(m, v)
        p["alt"] = texts.alt_text(m, v)
        p["kw"] = texts.keywords(m)
        p["link"] = m["url"]
    # Titel eindeutig machen
    seen = set()
    for p in sched:
        t = p["title"]; k = 2
        while p["title"] in seen:
            p["title"] = texts.cut(t, 92) + f" ({'Vorschau' if k == 2 else k})"; k += 1
        seen.add(p["title"])
    return sched


def export(sched, outdir):
    os.makedirs(outdir, exist_ok=True)
    rows = []
    for p in sched:
        m = p["m"]
        rows.append({"Nr": p["nr"], "Datum": p["date"].isoformat() if p["date"] else ("Reserve: sobald auf eduki öffentlich" if m["id"] in NOTPUBLIC else "Reserve: ab 1.9.2027 (Halloween)"),
                     "Uhrzeit": p["time"] or "", "Datei": p["file"], "Variante": {"A": "Cover", "B": "Darum geht's", "S": "Cyber Sale"}[p["v"]],
                     "Pinnwand": p["board"], "Titel": p["title"], "Beschreibung": p["desc"], "Link": p["link"],
                     "Alt-Text": p["alt"], "Keywords": ", ".join(p["kw"]), "Material": m["title"], "Fach": m["fach"],
                     "Klasse": m["klasse"], "Status": "geplant"})
    json.dump(rows, open(os.path.join(outdir, "plan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return rows


if __name__ == "__main__":
    s = build()
    rows = export(s, os.path.join(HERE, "out"))
    print(len(rows), "Pins;", rows[0]["Datum"], "bis", [r["Datum"] for r in rows if r["Uhrzeit"]][-1])
    from collections import Counter
    print(Counter(r["Pinnwand"] for r in rows))
    for r in rows[:12]: print(r["Nr"], r["Datum"], r["Uhrzeit"], r["Variante"], r["Titel"])
