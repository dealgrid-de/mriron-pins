# -*- coding: utf-8 -*-
"""Kreative Pin-Formate (1000 x 1500): Spickzettel, Regelkarte, Ideenliste, Zeitstrahl, Tipps, Countdown, Stunde to go, Freebie."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "ueb", "MrIron_Pinterest", "generator")
sys.path.insert(0, GEN)
import pin as P
from data import FARBE

NAVY, SUN, INK, SKY = "#12324F", "#FFC23D", "#1F2933", "#E6F4FA"
esc = P.esc

EXTRA = """
.card{background:#fff;border-radius:26px;box-shadow:0 10px 26px rgba(15,42,68,.12)}
.k{font-family:Fredoka;font-weight:700}
.n{font-family:Nunito}
.save{position:absolute;right:52px;top:52px;z-index:9;background:#fff;color:#12324F;font-family:Fredoka;font-weight:600;font-size:26px;padding:10px 22px;border-radius:99px;box-shadow:0 6px 16px rgba(15,42,68,.2)}
"""


def page(inner, bg=SKY):
    return P.page(f"<style>{EXTRA}</style>" + inner, bg=bg)


def foot_site(cta="Ganzer Artikel kostenlos", small="MRIRON.DE"):
    return f'<div class="foot">{P.logo_dark()}<div class="cta">{esc(cta)}<small>{esc(small)}</small></div></div>'


def foot_eduki(cta="Jetzt auf eduki ansehen"):
    return f'<div class="foot">{P.logo_dark()}<div class="cta">{esc(cta)}<small>REALSCHULE · BW</small></div></div>'


def save_tag(t="📌 Merken für später"):
    return f'<div class="save">{t}</div>'


# 1 Spickzettel (Artikel): Raster mit Begriff, Beispiel, Wirkung
def cheatsheet(pill, title, sub, items, col, more):
    top = (f'<div class="band" style="height:{420}px;background:{col}"></div>'
           f'<div class="top"><span class="pill">{esc(pill)}</span>'
           f'<div class="h" style="font-size:84px">{esc(title)}</div><div class="sub">{esc(sub)}</div></div>')
    cells = ""
    y = 400
    for i, (name, ex, eff) in enumerate(items):
        x = 40 if i % 2 == 0 else 510
        if i and i % 2 == 0: y += 222
        cells += (f'<div class="card" style="position:absolute;left:{x}px;top:{y}px;width:450px;height:204px;padding:22px 26px;border-top:10px solid {col}">'
                  f'<div class="k" style="font-size:36px;color:{col}">{esc(name)}</div>'
                  f'<div class="n" style="font-weight:800;font-size:25px;line-height:1.25;margin-top:8px;color:{INK}">„{esc(ex)}“</div>'
                  f'<div class="n" style="font-weight:700;font-size:22px;color:#5B6B78;margin-top:8px">→ {esc(eff)}</div></div>')
    m = f'<div class="k" style="position:absolute;left:0;width:1000px;top:{y + 226}px;text-align:center;font-size:34px;color:{NAVY}">{esc(more)}</div>'
    return page(top + cells + m + save_tag() + foot_site())


# 2 Regelkarte (Artikel): Frage, Probe, Beispiele richtig/falsch
def rulecard(pill, q, probe, rule_yes, rule_no, examples, col):
    top = (f'<div class="top" style="padding-top:70px"><span class="pill" style="background:{col};color:#fff">{esc(pill)}</span>'
           f'<div class="k" style="font-size:118px;color:{NAVY};line-height:1;margin-top:34px;white-space:nowrap">{q}</div>'
           f'<div class="k" style="font-size:44px;color:{col};margin-top:16px">{esc(probe)}</div></div>')
    box = (f'<div style="position:absolute;left:56px;top:420px;width:888px;display:flex;gap:24px">'
           f'<div class="card" style="flex:1;padding:28px;border-left:14px solid #3E9A5A"><div class="k" style="font-size:40px;color:#3E9A5A">{rule_yes[0]}</div><div class="n" style="font-weight:800;font-size:29px;margin-top:8px">{rule_yes[1]}</div></div>'
           f'<div class="card" style="flex:1;padding:28px;border-left:14px solid #F0612E"><div class="k" style="font-size:40px;color:#F0612E">{rule_no[0]}</div><div class="n" style="font-weight:800;font-size:29px;margin-top:8px">{rule_no[1]}</div></div></div>')
    ex = '<div style="position:absolute;left:56px;top:680px;width:888px;display:flex;flex-direction:column;gap:26px">'
    for s, why in examples:
        ex += (f'<div class="card" style="padding:30px 32px"><div class="n" style="font-weight:800;font-size:36px;color:{INK}">{s}</div>'
               f'<div class="n" style="font-weight:700;font-size:25px;color:#5B6B78;margin-top:6px">{esc(why)}</div></div>')
    ex += '</div>'
    return page(top + box + ex + save_tag() + foot_site("Regel + Übungen mit Lösungen"), bg="#FFF7E3")


# 3 Ideenliste (Artikel): Gruppen mit Ideen
def ideas(pill, title, sub, groups, col, cta):
    top = (f'<div class="band" style="height:430px;background:{col}"></div>'
           f'<div class="top"><span class="pill">{esc(pill)}</span>'
           f'<div class="h" style="font-size:78px">{esc(title)}</div><div class="sub">{esc(sub)}</div></div>')
    body = '<div style="position:absolute;left:46px;top:400px;width:908px;display:flex;flex-direction:column;gap:18px">'
    n = 1
    for g, its in groups:
        body += f'<div class="card" style="padding:22px 28px"><div class="k" style="font-size:30px;color:{col};margin-bottom:8px">{esc(g)}</div>'
        for name, d in its:
            body += (f'<div style="display:flex;gap:16px;align-items:flex-start;margin-top:10px"><div class="k" style="flex:0 0 46px;height:46px;border-radius:50%;background:{SUN};color:{NAVY};display:flex;align-items:center;justify-content:center;font-size:27px">{n}</div>'
                     f'<div class="n" style="font-size:28px;line-height:1.25;font-weight:700;color:{INK}"><b style="font-weight:900">{esc(name)}</b> – {esc(d)}</div></div>')
            n += 1
        body += '</div>'
    body += '</div>'
    return page(top + body + save_tag() + foot_site(cta))


# 4 Zeitstrahl (Artikel)
def timeline(pill, title, sub, events, col):
    top = (f'<div class="top" style="padding-top:64px"><span class="pill" style="background:{col};color:#fff">{esc(pill)}</span>'
           f'<div class="h" style="font-size:86px;color:{NAVY}">{esc(title)}</div><div class="sub" style="color:#5B6B78">{esc(sub)}</div></div>')
    y0, step = 450, 160
    line = f'<div style="position:absolute;left:250px;top:{y0}px;width:10px;height:{step*(len(events)-1)+40}px;background:{col};border-radius:5px"></div>'
    ev = ""
    for i, (yr, t, d) in enumerate(events):
        y = y0 + i * step
        ev += (f'<div class="k" style="position:absolute;left:30px;top:{y-12}px;width:190px;text-align:right;font-size:52px;color:{col}">{esc(yr)}</div>'
               f'<div style="position:absolute;left:236px;top:{y-4}px;width:38px;height:38px;border-radius:50%;background:#fff;border:9px solid {col}"></div>'
               f'<div class="card" style="position:absolute;left:300px;top:{y-22}px;width:650px;padding:16px 24px"><div class="k" style="font-size:33px;color:{NAVY}">{esc(t)}</div>'
               f'<div class="n" style="font-weight:700;font-size:24px;color:#5B6B78;margin-top:2px">{esc(d)}</div></div>')
    return page(top + line + ev + save_tag() + foot_site("Einfach erklärt + Selbsttest"), bg="#FFFFFF")


# 5 Tipps (Artikel): große Nummern
def tips(pill, kicker, title, items, col, cta):
    top = (f'<div class="band" style="height:470px;background:{NAVY}"></div>'
           f'<div class="top"><span class="pill">{esc(pill)}</span>'
           f'<div class="k" style="font-size:44px;color:{SUN};margin-top:26px">{esc(kicker)}</div>'
           f'<div class="h" style="font-size:80px;margin-top:6px">{esc(title)}</div></div>')
    body = '<div style="position:absolute;left:46px;top:450px;width:908px;display:flex;flex-direction:column;gap:20px">'
    for i, (t, d) in enumerate(items, 1):
        body += (f'<div class="card" style="display:flex;gap:26px;align-items:center;padding:34px 30px">'
                 f'<div class="k" style="font-size:92px;color:{col};line-height:1;width:70px;text-align:center">{i}</div>'
                 f'<div><div class="k" style="font-size:36px;color:{NAVY}">{esc(t)}</div><div class="n" style="font-weight:700;font-size:26px;line-height:1.25;color:#3D4B57;margin-top:4px">{esc(d)}</div></div></div>')
    body += '</div>'
    return page(top + body + save_tag() + foot_site(cta))


# 6 Countdown / Tool (Planer)
def countdown(pill, big, small, title, steps, col, cta, small_foot="MRIRON.DE · KOSTENLOS"):
    top = (f'<div class="band" style="height:760px;background:{NAVY}"></div>'
           f'<div class="top" style="text-align:center"><span class="pill">{esc(pill)}</span>'
           f'<div class="k" style="font-size:44px;color:#C9D5DF;margin-top:40px">{esc(small)}</div>'
           f'<div class="k" style="font-size:200px;color:{SUN};line-height:1;margin-top:6px">{esc(big)}</div>'
           f'<div class="h" style="font-size:68px;margin-top:30px">{esc(title)}</div></div>')
    body = '<div style="position:absolute;left:56px;top:800px;width:888px;display:flex;flex-direction:column;gap:18px">'
    for s in steps:
        body += f'<div class="card" style="display:flex;gap:18px;align-items:center;padding:20px 28px"><div style="flex:0 0 46px;height:46px;border-radius:50%;background:#3E9A5A;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px">✓</div><div class="n" style="font-weight:800;font-size:31px;color:{INK}">{esc(s)}</div></div>'
    body += '</div>'
    return page(top + body + foot_site(cta, small_foot))


# 7 Stunde to go (Material): Situation + Cover
def togo(kicker, title, cover, col, checks, label):
    top = (f'<div class="top" style="padding-top:64px"><div class="k" style="font-size:58px;color:#F0612E;line-height:1.1">{esc(kicker)}</div>'
           f'<div class="h" style="font-size:90px;color:{NAVY};margin-top:18px">{esc(title)}</div>'
           f'<span class="pill" style="background:{col};color:#fff;margin-top:24px">{esc(label)}</span></div>')
    clock = (f'<div style="position:absolute;left:60px;top:640px;width:300px;height:300px;border-radius:50%;background:{SUN};display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 14px 30px rgba(15,42,68,.25);border:10px solid #fff;z-index:6">'
             f'<div class="k" style="font-size:110px;color:{NAVY};line-height:.9">45</div><div class="k" style="font-size:36px;color:{NAVY}">Minuten</div><div class="n" style="font-weight:800;font-size:24px;color:{NAVY}">0 Vorbereitung</div></div>')
    cov = f'<img class="cov" src="file://{cover}" style="left:420px;top:560px;width:520px;height:693px;transform:rotate(3deg);z-index:4">'
    chk = '<div class="chk" style="left:40px;top:1000px">' + "".join(f'<div><i>✓</i>{esc(c)}</div>' for c in checks) + '</div>'
    return page(top + clock + cov + chk + foot_eduki(), bg="#FFF7E3")


# 8 Freebie (Material): Riesiges FREEBIE, Anlass, Cover
def freebie(anlass, title, cover, col, label, checks):
    top = (f'<div class="band" style="height:560px;background:{col}"></div>'
           f'<div class="top"><div class="k" style="font-size:170px;color:{SUN};line-height:.95;letter-spacing:2px">FREEBIE</div>'
           f'<div class="k" style="font-size:40px;color:#fff;margin-top:12px">{esc(anlass)}</div>'
           f'<div class="h" style="font-size:66px;margin-top:10px">{esc(title)}</div></div>')
    cov = f'<img class="cov" src="file://{cover}" style="left:440px;top:500px;width:500px;height:667px;transform:rotate(3deg);z-index:4">'
    pl = f'<span class="pill" style="position:absolute;left:56px;top:620px;background:#fff;color:{col};z-index:6">{esc(label)}</span>'
    chk = '<div class="chk" style="left:40px;top:740px">' + "".join(f'<div><i>✓</i>{esc(c)}</div>' for c in checks) + '</div>'
    return page(top + cov + pl + chk + foot_eduki("Kostenlos auf eduki"))


# 9 Foto-Szene (Material realistisch auf dem Tisch)
def photo(pill, head, foto, col, sticker=None, cta="Jetzt auf eduki ansehen"):
    hs = 54 if len(head) > 44 else (62 if len(head) > 36 else (70 if len(head) > 28 else 78))
    top = (f'<div style="position:absolute;left:0;top:0;width:1000px;height:300px;background:{col}"></div>'
           f'<div class="top" style="padding-top:44px"><span class="pill">{esc(pill)}</span>'
           f'<div class="h" style="font-size:{hs}px;margin-top:20px">{esc(head)}</div></div>')
    img = f'<img src="file://{foto}" style="position:absolute;left:0;top:300px;width:1000px;height:1050px;object-fit:cover">'
    st = ""
    if sticker:
        st = (f'<div style="position:absolute;right:46px;top:1180px;z-index:8;background:{SUN};color:{NAVY};font-family:Fredoka;font-weight:700;font-size:36px;'
              f'padding:16px 30px;border-radius:99px;box-shadow:0 10px 24px rgba(0,0,0,.35);transform:rotate(-4deg)">{esc(sticker)}</div>')
    return page(top + img + st + foot_eduki(cta))
