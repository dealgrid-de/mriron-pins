# -*- coding: utf-8 -*-
"""Restliche 34 Pins (Nr. 475–508) für die 17 Materialien mit nachgebauten Covern."""
import os, sys, json, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_neu as B
P, T = B.P, B.T
REST = sorted(B.PENDING)
SLOTS = ["10:15", "19:45"]
START = dt.date(2026, 11, 22)
FIX = {"2366382": (dt.date(2026, 12, 15), dt.date(2026, 12, 29))}  # Neues Jahr
ORDER = ["2377946", "2393325", "2381409", "2400480", "2394321", "2411759", "2360804", "2393480", "2381560", "2360857", "2378126",
         "2360873", "2360889", "2360904", "2360916", "2360933"]


def plan():
    L = {m["id"]: m for m in B.load()}
    taken = {}
    pins = []
    def put(m, v, d, t):
        taken[(d, t)] = 1; pins.append(dict(m=m, v=v, board=T.board_for(m, v), date=d, time=t))
    for mid, (a, b) in FIX.items():
        put(L[mid], "A", a, SLOTS[0]); put(L[mid], "B", b, SLOTS[0])
    A = list(ORDER); Bq = []; aday = {}
    day = START
    while A or Bq:
        for s in SLOTS:
            if (day, s) in taken: continue
            ready = [x for x in Bq if (day - aday[x]).days >= 21]
            if ready and (s == SLOTS[1] or not A):
                mid = ready[0]; Bq.remove(mid); put(L[mid], "B", day, s)
            elif A:
                mid = A.pop(0); aday[mid] = day; Bq.append(mid); put(L[mid], "A", day, s)
        day += dt.timedelta(days=1)
    pins.sort(key=lambda p: (p["date"], p["time"]))
    seen = set(r["Titel"] for r in json.load(open(os.path.join(HERE, "ueb", "MrIron_Pinterest", "plan.json"), encoding="utf-8")))
    seen |= set(r["Titel"] for r in json.load(open(os.path.join(HERE, "out", "plan_neu.json"), encoding="utf-8")))
    for i, p in enumerate(pins, 475):
        m, v = p["m"], p["v"]
        p.update(nr=i, file=f"{i:03d}_{m['id']}_{v}.jpg", title=T.pin_title(m, v), desc=T.description(m, v), alt=T.alt_text(m, v), kw=T.keywords(m), link=m["url"])
        t = p["title"]; k = 2
        while p["title"] in seen:
            p["title"] = T.cut(t, 92) + f" ({'Vorschau' if k == 2 else k})"; k += 1
        seen.add(p["title"])
    return pins


if __name__ == "__main__":
    pins = plan()
    print(len(pins), pins[0]["date"], pins[-1]["date"])
    if "--render" in sys.argv:
        from render import shoot
        shoot([((P.var_a(p["m"]) if p["v"] == "A" else P.var_b(p["m"])), os.path.join(B.PINS, p["file"])) for p in pins])
    rows = [{"Nr": p["nr"], "Datum": p["date"].isoformat(), "Uhrzeit": p["time"], "Datei": p["file"], "Variante": {"A": "Cover", "B": "Darum geht's"}[p["v"]],
             "Pinnwand": p["board"], "Titel": p["title"], "Beschreibung": p["desc"], "Link": p["link"], "Alt-Text": p["alt"], "Keywords": ", ".join(p["kw"]),
             "Material": p["m"]["title"], "Fach": p["m"]["fach"], "Klasse": p["m"]["klasse"], "Status": "geplant"} for p in pins]
    json.dump(rows, open(os.path.join(B.OUT, "plan_rest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in rows[:4]: print(r["Nr"], r["Datum"], r["Uhrzeit"], r["Titel"], "|", r["Pinnwand"])
