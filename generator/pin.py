# -*- coding: utf-8 -*-
"""Pinterest-Pins (1000 x 1500) für Mr.-Iron-Materialien. Variante A (Cover) und B (Blick ins Heft)."""
import os, sys, re, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import assets as A
from data import FARBE

FONTS = "".join(
    f'@font-face{{font-family:"{f}";src:url("file://{HERE}/fonts/static/{f}-{w}.ttf");font-weight:{w}}}'
    for f, ws in (("Fredoka", (500, 600, 700)), ("Nunito", (600, 700, 800, 900))) for w in ws)

CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1000px;height:1500px;overflow:hidden}
.p{width:1000px;height:1500px;position:relative;overflow:hidden;font-family:Nunito;color:#1F2933;background:#E6F4FA}
.top{position:absolute;left:0;top:0;width:1000px;padding:58px 64px 0 64px;z-index:5}
.pill{display:inline-block;font-family:Fredoka;font-weight:600;font-size:34px;padding:8px 26px;border-radius:99px;color:#12324F;background:#FFC23D;letter-spacing:.3px}
.h{font-family:Fredoka;font-weight:700;color:#fff;line-height:1.04;letter-spacing:-.5px;margin-top:26px}
.sub{font-family:Nunito;font-weight:800;color:rgba(255,255,255,.93);font-size:40px;line-height:1.18;margin-top:16px}
.band{position:absolute;left:-60px;top:-60px;width:1120px;border-radius:0 0 90px 90px}
.cov{position:absolute;border-radius:10px;box-shadow:0 26px 60px rgba(15,42,68,.35);background:#fff}
.chk{position:absolute;left:64px;z-index:6;display:flex;flex-direction:column;gap:16px}
.chk div{display:inline-flex;align-items:center;gap:14px;background:#fff;border-radius:99px;padding:12px 26px 12px 14px;font-family:Fredoka;font-weight:600;font-size:31px;color:#12324F;box-shadow:0 8px 20px rgba(15,42,68,.14);width:max-content}
.chk i{width:42px;height:42px;border-radius:50%;background:#3E9A5A;color:#fff;font-style:normal;display:inline-flex;align-items:center;justify-content:center;font-size:26px}
.foot{position:absolute;left:0;bottom:0;width:1000px;height:150px;background:#12324F;display:flex;align-items:center;justify-content:space-between;padding:0 56px;z-index:7}
.foot .cta{font-family:Fredoka;font-weight:600;font-size:34px;color:#FFC23D;text-align:right;line-height:1.15}
.foot .cta small{display:block;font-family:Nunito;font-weight:800;font-size:24px;color:#C9D5DF;letter-spacing:1px}
.free{position:absolute;z-index:8;width:250px;height:250px;border-radius:50%;background:#FFC23D;color:#12324F;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Fredoka;font-weight:700;font-size:46px;line-height:1;transform:rotate(-12deg);box-shadow:0 14px 30px rgba(15,42,68,.3);border:8px solid #fff}
.free small{display:block;font-size:27px;font-weight:600;margin-top:6px}
"""


def esc(s):
    return H.escape(s, quote=False)


def logo_dark():
    return f'<div style="transform:scale(1.55);transform-origin:left center">{A.logo(16, dark=True)}</div>'


def split_title(t):
    t = re.sub(r"^Kostenlos:\s*", "", t)
    for sep in (": ", " – "):
        if sep in t:
            a, b = t.split(sep, 1); return a.strip(), b.strip()
    return t, ""


def hsize(s, maxw=872, base=96, lines=3):
    """grobe Schriftgröße, damit die Headline in <= lines Zeilen passt (Fredoka 700, ~0.55 em/Zeichen)."""
    n = len(s)
    for size in range(base, 50, -2):
        per = maxw / (size * 0.56)
        words = s.split(); ln = 1; cur = 0
        for w in words:
            L = len(w) + (1 if cur else 0)
            if cur + L > per:
                ln += 1; cur = len(w)
                if len(w) > per: ln += 9
            else:
                cur += L
        if ln <= lines:
            return size
    return 52


def nlines(s, size, maxw=872):
    per = maxw / (size * 0.56); ln = 1; cur = 0
    for w in s.split():
        L = len(w) + (1 if cur else 0)
        if cur + L > per: ln += 1; cur = len(w)
        else: cur += L
    return ln


NICE = {"WBS": "Wirtschaft und Beruf (WBS)"}


def label(m):
    k = f" · Klasse {m['klasse']}" if m["klasse"] else ""
    f = {"Fächerübergreifend": "Fächerübergreifend", "Medienbildung": "Medienbildung"}.get(m["fach"], m["fach"])
    return f + k


CHECKS = {
    "lernjob": ["Fertiger Lernjob", "Differenziert: G und M", "Mit Lösungen und Lehrerheft"],
    "gratis": ["Kostenlos zum Testen", "Sofort einsetzbar", "Mit Lösungen"],
    "paket": ["Alle Lernjobs im Paket", "Günstiger als einzeln", "Mit Lösungen und Lehrerheften"],
    "lektuere": ["Prüfungstraining zur Lektüre", "Klassenarbeit inklusive", "Mit Lösungen"],
    "pruefung": ["Abschlussprüfung 2027", "Aufgaben wie in der Prüfung", "Mit Lösungen"],
    "togo": ["Eine Stunde, fertig geplant", "Ausdrucken und loslegen", "Mit Lösungen"],
    "ka": ["Klassenarbeit mit Erwartungshorizont", "Differenziert", "Mit Lösungen"],
}

HOOK_B = {
    "lernjob": "Ausdrucken und loslegen:",
    "gratis": "Kostenlos testen:",
    "paket": "Komplettes Paket:",
    "lektuere": "Lektüre-Training:",
    "pruefung": "Prüfung 2027:",
    "togo": "Stunde to go:",
    "ka": "Klassenarbeit:",
}


def page(inner, bg="#E6F4FA"):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="p" style="background:{bg}">{inner}</div></body></html>'


def free_badge(x, y):
    return f'<div class="free" style="left:{x}px;top:{y}px"><div>GRATIS<small>zum Testen</small></div></div>'


def foot(m):
    cta = "Gratis auf eduki" if m["typ"] == "gratis" else "Jetzt auf eduki ansehen"
    return f'<div class="foot">{logo_dark()}<div class="cta">{cta}<small>REALSCHULE · BW</small></div></div>'


def checks_of(m):
    c = []
    if m["typ"] == "gratis": c.append("Kostenlos zum Testen")
    elif m["typ"] == "paket": c.append(f"{m.get('anzahl') or ''} Materialien im Paket".strip().replace("  ", " ") if m.get("anzahl") else "Komplettes Paket")
    elif m["typ"] == "togo": c.append("Eine Stunde, fertig geplant")
    elif m["typ"] == "lektuere": c.append("Lektüre-Prüfungstraining")
    elif m["typ"] == "pruefung": c.append("Training Abschlussprüfung")
    else: c.append("Fertiger Lernjob")
    nv = (m.get("niveaus") or "").replace(" ", "")
    if nv:
        parts = [p for p in re.split(r"[,/und]+", nv) if p in ("G", "M", "E")]
        if len(parts) >= 2: c.append("Differenziert: " + (", ".join(parts[:-1]) + " und " + parts[-1]))
        elif len(parts) == 1: c.append(f"Niveau {parts[0]}")
    if m.get("loesungen") and m.get("lehrerheft"): c.append("Mit Lösungen und Lehrerheft")
    elif m.get("loesungen"): c.append("Mit Lösungen")
    return c[:3]


def clean_head(a, m):
    if m["klasse"]:
        a = re.sub(r"\s*(Klasse|Kl\.)\s*[\d/–-]+\s*", " ", a).strip()
    return a


def var_a(m):
    """Cover-Pin: Farbband mit Fach/Klasse + Thema, darunter groß das eduki-Cover."""
    col = FARBE.get(m["fach"], "#12324F")
    a, b = split_title(m["title"]); a = clean_head(a, m); b = clean_head(b, m) if b else b
    a = NICE.get(a, a)
    hs = hsize(a, base=92, lines=2)
    two = hs < 80 or len(a) > 18
    bh = 300 + (hs * (2 if two else 1)) + (70 if b else 0)
    top = (f'<div class="band" style="height:{bh}px;background:{col}"></div>'
           f'<div class="top"><span class="pill">{esc(label(m))}</span>'
           f'<div class="h" style="font-size:{hs}px">{esc(a)}</div>'
           + (f'<div class="sub">{esc(b)}</div>' if b else "") + '</div>')
    ctop = bh - 120
    ch = 1500 - 150 - 40 - ctop; cw = int(ch * 3 / 4)
    if cw > 690: cw = 690; ch = int(cw * 4 / 3)
    left = 1000 - cw - 60
    cov = f'<img class="cov" src="file://{m["cover"]}" style="left:{left}px;top:{ctop}px;width:{cw}px;height:{ch}px;transform:rotate(2.5deg);z-index:4">'
    ck = checks_of(m)
    chk = f'<div class="chk" style="left:40px;top:{ctop + ch - 70 - 74*len(ck)}px">' + "".join(f'<div><i>✓</i>{esc(c)}</div>' for c in ck) + '</div>'
    fb = free_badge(36, ctop + 10) if m["typ"] == "gratis" else ""
    return page(top + cov + chk + fb + foot(m))


def var_b(m, prev_path=None):
    """Zweiter Pin: Nutzen-Headline, Inhaltssatz („Darum geht's“), Cover und Haken."""
    col = FARBE.get(m["fach"], "#12324F")
    a, b = split_title(m["title"]); a = clean_head(a, m); b = clean_head(b, m) if b else b
    head = HOOK_B[m["typ"]]
    topic = f"{a}: {b}" if b and len(a) + len(b) < 44 else a
    hs = hsize(topic, base=80, lines=3)
    top = (f'<div class="top" style="padding-top:60px"><span class="pill" style="background:{col};color:#fff">{esc(label(m))}</span>'
           f'<div style="font-family:Fredoka;font-weight:600;font-size:44px;color:{col};margin-top:28px">{esc(head)}</div>'
           f'<div class="h" style="color:#12324F;font-size:{hs}px;margin-top:6px">{esc(topic)}</div></div>')
    kurz = m.get("kurz") or ""
    card = ""
    y0 = 60 + 58 + 28 + 54 + 6 + int(nlines(topic, hs) * hs * 1.06) + 50
    if kurz:
        fs = 36 if len(kurz) < 150 else 32
        card = (f'<div style="position:absolute;left:56px;top:{y0}px;width:540px;background:#E6F4FA;border-radius:28px;padding:30px 34px;z-index:5;border-left:12px solid {col}">'
                f'<div style="font-family:Fredoka;font-weight:600;font-size:30px;color:{col};margin-bottom:10px">Darum geht’s</div>'
                f'<div style="font-family:Nunito;font-weight:700;font-size:{fs}px;line-height:1.3;color:#1F2933">{esc(kurz)}</div></div>')
    cov = f'<img class="cov" src="file://{m["cover"]}" style="left:600px;top:{y0 + 20}px;width:360px;height:480px;transform:rotate(5deg);z-index:4">'
    ck = checks_of(m)
    chk = f'<div class="chk" style="left:56px;top:{1350 - 30 - 74*len(ck)}px">' + "".join(f'<div><i>✓</i>{esc(c)}</div>' for c in ck) + '</div>'
    fb = free_badge(730, 1030) if m["typ"] == "gratis" else ""
    return page(top + card + cov + chk + fb + foot(m), bg="#FFFFFF")


def var_sale(m):
    """Cyber-Sale-Pin: Cover-Pin mit Sale-Band; eigene Pinnwand, nach dem Sale archivieren."""
    col = FARBE.get(m["fach"], "#12324F")
    a, b = split_title(m["title"]); a = clean_head(a, m); b = clean_head(b, m) if b else b
    a = NICE.get(a, a)
    hs = hsize(a, base=84, lines=2)
    top = ('<div class="band" style="height:420px;background:#12324F"></div>'
           '<div class="top" style="padding-top:62px"><div style="font-family:Fredoka;font-weight:700;font-size:96px;color:#FFC23D;line-height:1">Cyber Sale</div>'
           '<div style="font-family:Fredoka;font-weight:600;font-size:48px;color:#fff;margin-top:12px">−20 % auf alle Materialien</div>'
           '<div style="font-family:Nunito;font-weight:800;font-size:34px;color:#C9D5DF;margin-top:8px">15. bis 17. November auf eduki</div></div>')
    head = (f'<div style="position:absolute;left:64px;top:400px;width:872px;z-index:6"><span class="pill" style="background:{col};color:#fff">{esc(label(m))}</span>'
            f'<div class="h" style="color:#12324F;font-size:{hs}px;margin-top:18px">{esc(a)}</div>'
            + (f'<div class="sub" style="color:#5B6B78">{esc(b)}</div>' if b else '') + '</div>')
    ctop = 440 + 70 + int(nlines(a, hs) * hs * 1.06) + (70 if b else 0)
    ch = 1500 - 150 - 40 - ctop; cw = int(ch * 3 / 4)
    if cw > 640: cw = 640; ch = int(cw * 4 / 3)
    cov = f'<img class="cov" src="file://{m["cover"]}" style="left:{1000 - cw - 60}px;top:{ctop}px;width:{cw}px;height:{ch}px;transform:rotate(2.5deg);z-index:4">'
    badge = ('<div class="free" style="left:40px;top:' + str(ctop + 30) + 'px;background:#F0612E;color:#fff"><div>−20&nbsp;%<small>15.–17.11.</small></div></div>')
    ck = checks_of(m)
    chk = f'<div class="chk" style="left:40px;top:{ctop + ch - 70 - 74*len(ck)}px">' + "".join(f'<div><i>✓</i>{esc(c)}</div>' for c in ck) + '</div>'
    return page(top + head + cov + badge + chk + foot(m))
