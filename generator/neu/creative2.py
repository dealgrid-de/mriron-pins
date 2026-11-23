# -*- coding: utf-8 -*-
"""Flexible Artikel-/Wissens-Pins mit automatischer Schriftanpassung (1000 x 1500)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import creative as C
from playwright.sync_api import sync_playwright
from PIL import Image

P, esc = C.P, C.esc
NAVY, SUN, INK = C.NAVY, C.SUN, C.INK
GREEN, RED = "#3E9A5A", "#D9483B"

CSS2 = """
:root{--s:1;--t:1}
#hd{position:absolute;left:0;top:0;width:1000px;padding:56px 60px 0 60px;z-index:5;box-sizing:border-box;overflow:hidden}
#hd .tt{font-family:Fredoka;font-weight:700;line-height:1.04;letter-spacing:-.5px;margin-top:22px;font-size:calc(84px*var(--t))}
#hd .ss{font-family:Nunito;font-weight:800;font-size:calc(36px*var(--t));line-height:1.2;margin-top:14px}
#b{position:absolute;left:44px;width:912px;display:flex;flex-direction:column;gap:calc(18px*var(--s));overflow:hidden;box-sizing:border-box;padding:4px 4px 8px 4px}
.cd{background:#fff;border-radius:24px;box-shadow:0 8px 22px rgba(15,42,68,.12);padding:calc(20px*var(--s)) calc(26px*var(--s));display:flex;gap:calc(20px*var(--s));align-items:center}
.cd .bd{flex:0 0 auto;min-width:calc(64px*var(--s));height:calc(64px*var(--s));border-radius:18px;display:flex;align-items:center;justify-content:center;font-family:Fredoka;font-weight:700;font-size:calc(34px*var(--s));color:#fff;padding:0 calc(10px*var(--s))}
.cd .hh{font-family:Fredoka;font-weight:700;font-size:calc(34px*var(--s));color:#12324F;line-height:1.1}
.cd .tx{font-family:Nunito;font-weight:700;font-size:calc(27px*var(--s));color:#3D4B57;line-height:1.25;margin-top:calc(4px*var(--s))}
.gr{display:grid;grid-template-columns:1fr 1fr;gap:calc(16px*var(--s))}
.gr .cd{display:block;min-width:0;hyphens:auto;overflow-wrap:break-word;padding:calc(18px*var(--s)) calc(22px*var(--s))}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.col{background:#fff;border-radius:24px;box-shadow:0 8px 22px rgba(15,42,68,.12);padding:calc(22px*var(--s))}
.col .ch{font-family:Fredoka;font-weight:700;font-size:calc(40px*var(--s));margin-bottom:calc(10px*var(--s))}
.col .it{font-family:Nunito;font-weight:700;font-size:calc(26px*var(--s));line-height:1.25;color:#2B3742;margin-top:calc(14px*var(--s))}
.col .it b{font-family:Fredoka;font-weight:600;color:#12324F;display:block;font-size:calc(30px*var(--s))}
.chips{display:flex;flex-wrap:wrap;gap:calc(14px*var(--s))}
.chips span{background:#fff;border-radius:99px;padding:calc(14px*var(--s)) calc(26px*var(--s));font-family:Fredoka;font-weight:600;font-size:calc(34px*var(--s));color:#12324F;box-shadow:0 6px 16px rgba(15,42,68,.12)}
.big{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.big div{background:#fff;border-radius:26px;box-shadow:0 8px 22px rgba(15,42,68,.12);padding:calc(26px*var(--s));text-align:center}
.big b{display:block;font-family:Fredoka;font-weight:700;font-size:calc(110px*var(--s));line-height:1}
.big span{display:block;font-family:Nunito;font-weight:800;font-size:calc(28px*var(--s));color:#3D4B57;margin-top:8px;line-height:1.2}
.note{font-family:Nunito;font-weight:700;font-size:calc(22px*var(--s));color:#5B6B78;text-align:center}
.lab{font-family:Fredoka;font-weight:700;font-size:calc(32px*var(--s));color:#12324F;margin:calc(6px*var(--s)) 0 0 6px}
"""

FIT = """
(()=>{const r=document.documentElement;const b=document.getElementById('b');const h=document.getElementById('hd');
let t=1;while(h.scrollHeight>h.clientHeight+2&&t>0.55){t-=0.03;r.style.setProperty('--t',t);}
const ov=()=>b.scrollHeight>b.clientHeight+1||[...b.querySelectorAll('.cd,.col,.big div,.chips span')].some(e=>e.scrollWidth>e.clientWidth+1);let s=1.7;r.style.setProperty('--s',s);while(ov()&&s>0.5){s-=0.02;r.style.setProperty('--s',s);}
b.style.justifyContent='center';window.__fit={t:t,s:s,ok:!ov()&&h.scrollHeight<=h.clientHeight+2};})();
"""


def card(head, text="", badge=None, bcol=NAVY):
    if badge is None:
        tx = f'<div class="tx">{esc(text)}</div>' if text else ""
        return f'<div class="cd" style="border-left:12px solid {bcol}"><div><div class="hh" style="color:{bcol}">{esc(head)}</div>{tx}</div></div>'
    bd = f'<div class="bd" style="background:{bcol}">{esc(badge)}</div>' if badge is not None else ""
    tx = f'<div class="tx">{esc(text)}</div>' if text else ""
    return f'<div class="cd">{bd}<div><div class="hh">{esc(head)}</div>{tx}</div></div>'


def gcard(head, text, col):
    return f'<div class="cd" style="border-top:8px solid {col}"><div class="hh" style="color:{col}">{esc(head)}</div><div class="tx">{esc(text)}</div></div>'


def blk_cards(items, col, badges=None):
    out = ""
    for i, it in enumerate(items):
        h, t = (it if isinstance(it, (list, tuple)) else (it, ""))[:2]
        b = (badges[i] if badges else None)
        bc = col
        if b == "✓": bc = GREEN
        if b == "✗": bc = RED
        out += card(h, t, b, bc)
    return out


def blk_grid(items, col):
    return '<div class="gr">' + "".join(gcard(h, t, col) for h, t in items) + '</div>'


def blk_two(a, b):
    def col(title, c, its):
        return (f'<div class="col" style="border-top:10px solid {c}"><div class="ch" style="color:{c}">{esc(title)}</div>'
                + "".join(f'<div class="it"><b>{esc(h)}</b>{esc(t)}</div>' for h, t in its) + '</div>')
    return '<div class="two">' + col(*a) + col(*b) + '</div>'


def blk_chips(words, label=None):
    l = f'<div class="lab">{esc(label)}</div>' if label else ""
    return l + '<div class="chips">' + "".join(f'<span>{esc(w)}</span>' for w in words) + '</div>'


def blk_big(items, col):
    return '<div class="big">' + "".join(f'<div><b style="color:{col}">{esc(n)}</b><span>{esc(t)}</span></div>' for n, t in items) + '</div>'


def blk_note(t):
    return f'<div class="note">{esc(t)}</div>'


def pin(pill, title, sub, body, col, cta="Ganzer Artikel kostenlos", small="MRIRON.DE", head_h=400, light=False, save=False):
    """body: HTML-Blöcke; Kopf farbig (col) oder hell."""
    tc, sc, bg = ("#fff", "rgba(255,255,255,.93)", C.SKY)
    hb = col
    if light:
        tc, sc, hb, bg = (NAVY, "#5B6B78", "#FFF7E3", "#FFF7E3")
    pl = f'<span class="pill">{esc(pill)}</span>' if pill else ""
    ss = f'<div class="ss" style="color:{sc}">{esc(sub)}</div>' if sub else ""
    hd = (f'<div style="position:absolute;left:0;top:0;width:1000px;height:{head_h}px;background:{hb};border-radius:0 0 60px 60px"></div>'
          f'<div id="hd" lang="de" style="height:{head_h - 20}px">{pl}<div class="tt" style="color:{tc}">{esc(title)}</div>{ss}</div>')
    b = f'<div id="b" lang="de" style="top:{head_h + 24}px;height:{1350 - head_h - 24 - 22}px">{body}</div>'
    sv = C.save_tag() if save else ""
    foot = C.foot_site(cta, small) if small == "MRIRON.DE" else C.foot_eduki(cta)
    return C.page(f"<style>{CSS2}</style>" + hd + b + sv + foot, bg=bg)


def shoot(jobs, quality=90):
    """jobs: [(html, out)] → Liste der Fit-Infos; Seiten mit Überlauf melden."""
    res = []
    hdir = os.path.join(C.GEN, "html")
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1000, "height": 1500})
        for html, out in jobs:
            tmp = os.path.join(hdir, os.path.basename(out).replace(".jpg", ".html"))
            open(tmp, "w", encoding="utf-8").write(html)
            pg.goto("file://" + tmp); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(120)
            fit = None
            if "id=\"b\"" in html:
                pg.evaluate(FIT); pg.wait_for_timeout(60); fit = pg.evaluate("window.__fit")
            png = out.replace(".jpg", ".png"); pg.screenshot(path=png)
            Image.open(png).convert("RGB").save(out, "JPEG", quality=quality, optimize=True, progressive=True); os.remove(png)
            res.append((out, fit))
        br.close()
    return res
