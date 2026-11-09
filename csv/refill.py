# -*- coding: utf-8 -*-
"""Nächste Portion aus csv/QUEUE_GESAMT.csv für den Pinterest-Bulk-Upload.
Aufruf: python3 refill.py <geplante Termine als UTC 'YYYY-MM-DDTHH:MM', kommagetrennt> [Anzahl geplant gesamt]
Schreibt csv/batch.json (JSON-String der CSV) und gibt eine Übersicht aus."""
import csv, json, sys, os, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__))
S = set(x.strip() for x in sys.argv[1].split(",") if x.strip())
n_sched = int(sys.argv[2]) if len(sys.argv) > 2 else len(S)
rows = list(csv.reader(open(os.path.join(HERE, "QUEUE_GESAMT.csv"), encoding="utf-8")))
h, rows = rows[0], rows[1:]
now = dt.datetime.utcnow()
soon = (now + dt.timedelta(minutes=90)).strftime("%Y-%m-%dT%H:%M")
lim = (now + dt.timedelta(days=28)).strftime("%Y-%m-%dT%H:%M")
past = now.strftime("%Y-%m-%dT%H:%M")
open_ = [r for r in rows if r[6][:16] not in S and r[6][:16] > soon]
missed = [r for r in rows if r[6][:16] not in S and r[6][:16] <= soon and r[6][:16] > (now - dt.timedelta(days=3)).strftime("%Y-%m-%dT%H:%M")]
free = max(0, 100 - n_sched - 3)  # 3 Plätze Puffer
batch = [r for r in open_ if r[6][:16] <= lim][:free]
import io
buf = io.StringIO(); csv.writer(buf).writerows([h] + batch)
json.dump(buf.getvalue(), open(os.path.join(HERE, "batch.json"), "w"))
print(json.dumps({"geplant": n_sched, "frei": free, "batch": len(batch), "von": batch[0][6] if batch else None,
                  "bis": batch[-1][6] if batch else None, "noch_offen": len(open_) - len(batch),
                  "verpasst_letzte_3_tage": len(missed), "letzter_termin": rows[-1][6], "bytes": len(buf.getvalue())}))
