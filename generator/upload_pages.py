# -*- coding: utf-8 -*-
"""Upload-Seiten: je 30 Pins als eingebettete Bilder + Plan-Daten. Die Seite reicht die Bilder per postMessage
an ein Pinterest-Fenster weiter (window.opener bzw. das von ihr geöffnete Fenster). Funktioniert als lokale Datei."""
import os, sys, json, base64
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

TPL = """<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Mr. Iron · Pinterest-Upload {n}</title>
<style>body{{font-family:system-ui,sans-serif;margin:24px;background:#E6F4FA;color:#12324F}}h1{{margin:0 0 8px}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}}.c{{background:#fff;border-radius:8px;padding:6px;font-size:11px}}
.c img{{width:100%;border-radius:4px}}button{{font-size:18px;padding:10px 18px;border-radius:99px;border:0;background:#12324F;color:#fff;cursor:pointer}}</style></head>
<body><h1>Pinterest-Upload {n}</h1><p>Pins {a}–{b}. Diese Seite reicht die Bilder an Pinterest weiter.</p>
<button id="open">Pinterest öffnen</button> <span id="st"></span>
<div class="g" id="g"></div>
<script>
const PINS = {pins};
const g = document.getElementById('g');
for (const p of PINS) {{ const d = document.createElement('div'); d.className='c'; d.innerHTML = '<img src="data:image/jpeg;base64,'+p.b64+'"><b>'+p.nr+'</b> '+p.date+' '+p.time+'<br>'+p.title; g.appendChild(d); }}
function blobOf(p) {{ const bin = atob(p.b64); const u = new Uint8Array(bin.length); for (let i=0;i<bin.length;i++) u[i]=bin.charCodeAt(i); return new Blob([u], {{type:'image/jpeg'}}); }}
window.MRIRON = {{
  pins: PINS.map(p => Object.assign({{}}, p, {{b64: undefined}})),
  send(win, nrs) {{ const sel = PINS.filter(p => !nrs || nrs.includes(p.nr)); for (const p of sel) win.postMessage({{mriron: true, nr: p.nr, file: p.file, blob: blobOf(p), meta: Object.assign({{}}, p, {{b64: undefined}})}}, '*'); return sel.length; }}
}};
let W = null;
document.getElementById('open').onclick = () => {{ W = window.open('https://de.pinterest.com/pin-creation-tool/', 'mriron_pin'); window.MRIRON.win = W; document.getElementById('st').textContent = W ? 'Pinterest-Fenster offen' : 'Popup blockiert'; }};
window.addEventListener('message', e => {{ if (e.data && e.data.mriron_ready && e.source) {{ const n = window.MRIRON.send(e.source, e.data.nrs); document.getElementById('st').textContent = n + ' Bilder gesendet'; }} }});
</script></body></html>"""


def build(rows, pins_dir, size=30):
    os.makedirs(OUT, exist_ok=True)
    files = []
    for k in range(0, len(rows), size):
        chunk = rows[k:k + size]
        pins = []
        for r in chunk:
            b64 = base64.b64encode(open(os.path.join(pins_dir, r["Datei"]), "rb").read()).decode()
            pins.append({"nr": r["Nr"], "file": r["Datei"], "date": r["Datum"], "time": r["Uhrzeit"], "board": r["Pinnwand"],
                         "title": r["Titel"], "desc": r["Beschreibung"], "link": r["Link"], "alt": r["Alt-Text"], "b64": b64})
        n = k // size + 1
        fn = os.path.join(OUT, f"Upload_{n:02d}_Pins_{chunk[0]['Nr']:03d}-{chunk[-1]['Nr']:03d}.html")
        open(fn, "w", encoding="utf-8").write(TPL.format(n=n, a=chunk[0]["Nr"], b=chunk[-1]["Nr"], pins=json.dumps(pins, ensure_ascii=False)))
        files.append(fn)
    return files
