# -*- coding: utf-8 -*-
"""Pins im Instagram-Design von @mr.iron_lernjobs: Karopapier, Rand, Markerzeile, Klebezettel, Stempel."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import creative as C
esc = C.esc
IND, YEL, HL, ORA, PINK, RED = "#23265F", "#FFD23F", "#FFE27A", "#F07A1A", "#F9B8CF", "#D8473F"

CSS = """
.pg{position:absolute;inset:0;background-color:#F8F6EF;
 background-image:linear-gradient(#D6E2F0 1.5px,transparent 1.5px),linear-gradient(90deg,#D6E2F0 1.5px,transparent 1.5px);background-size:48px 48px;background-position:-2px -2px}
.mr{position:absolute;top:0;bottom:0;left:930px;width:3px;background:#E58C8C}
.lg{position:absolute;left:70px;top:64px;display:flex;align-items:center;gap:16px;font-family:Fredoka;font-weight:600;font-size:34px;color:#23265F}
.lg b{display:inline-flex;align-items:center;justify-content:center;width:62px;height:62px;border-radius:12px;background:#FFD23F;border:3px solid #23265F;font-family:Fredoka;font-weight:700;font-size:32px}
.nr{position:absolute;right:110px;top:76px;font-family:Fredoka;font-weight:600;font-size:30px;color:#23265F}
.kk{position:absolute;left:70px;top:178px;width:820px;font-family:Fredoka;font-weight:600;font-size:52px;color:#23265F;line-height:1.15}
.hl{position:absolute;left:70px;width:840px;font-family:Fredoka;font-weight:700;color:#23265F;line-height:1.18}
.hl span{background:linear-gradient(transparent 52%,#FFE27A 52%,#FFE27A 92%,transparent 92%);box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:0 6px}
.note{position:absolute;background:#FFD23F;box-shadow:0 18px 34px rgba(35,38,95,.22);padding:56px 58px;font-family:Fredoka;font-weight:700;color:#23265F;line-height:1.12}
.note .o{color:#F07A1A}
.note small{display:block;font-family:Nunito;font-weight:800;font-size:30px;line-height:1.3;margin-top:18px;color:#3A3A6A}
.tape{position:absolute;width:190px;height:52px;background:rgba(255,255,255,.62);box-shadow:0 2px 6px rgba(0,0,0,.08)}
.pink{position:absolute;background:#F9B8CF;box-shadow:0 14px 26px rgba(35,38,95,.2);padding:30px 36px;font-family:Fredoka;font-weight:600;font-size:36px;color:#23265F;line-height:1.2;text-align:center}
.stamp{position:absolute;border:7px solid #D8473F;color:#D8473F;font-family:Fredoka;font-weight:700;font-size:44px;letter-spacing:2px;padding:8px 26px;border-radius:14px;opacity:.88;box-shadow:inset 0 0 0 3px rgba(216,71,63,.35)}
.bt{position:absolute;left:70px;bottom:92px;width:560px;font-family:Fredoka;font-weight:600;font-size:36px;color:#23265F;line-height:1.2}
.wt{position:absolute;right:110px;bottom:84px;background:#FFD23F;border:4px solid #23265F;border-radius:99px;padding:12px 32px;font-family:Fredoka;font-weight:700;font-size:34px;color:#23265F}
.cv{position:absolute;box-shadow:0 22px 44px rgba(35,38,95,.3);border-radius:6px;background:#fff}
.li{font-family:Nunito;font-weight:800;font-size:34px;line-height:1.35;color:#23265F}
"""


def page(inner):
    return f'<!doctype html><html lang="de"><head><meta charset="utf-8"><style>{C.P.CSS}{CSS}</style></head><body><div class="p" style="background:#F8F6EF"><div class="pg"></div><div class="mr"></div>{inner}</div></body></html>'


def pin(kicker, head, note=None, note_sub=None, pink=None, stamp=None, bottom="", button="mehr dazu", cover=None, lines=None, nr=None, head_size=None, note_size=None):
    """note: HTML erlaubt (<span class=o> für orange). cover: Pfad zum Cover (wird angeklebt)."""
    hs = head_size or (96 if len(head) <= 18 else 84 if len(head) <= 26 else 72 if len(head) <= 36 else 62)
    o = '<div class="lg"><b>Fe</b>Mr. Iron</div>'
    if nr: o += f'<div class="nr">{esc(nr)}</div>'
    o += f'<div class="kk">{esc(kicker)}</div>'
    o += f'<div class="hl" style="top:258px;font-size:{hs}px"><span>{esc(head)}</span></div>'
    if cover:
        o += f'<img class="cv" src="file://{cover}" style="left:470px;top:560px;width:420px;height:560px;transform:rotate(4deg)">'
        o += '<div class="tape" style="left:600px;top:535px;transform:rotate(-6deg)"></div>'
        if note:
            ns = note_size or 58
            o += (f'<div class="note" style="left:60px;top:600px;width:470px;font-size:{ns}px;transform:rotate(-3deg);padding:44px 44px">{note}'
                  + (f'<small>{esc(note_sub)}</small>' if note_sub else "") + '</div>')
            o += '<div class="tape" style="left:190px;top:578px;transform:rotate(4deg)"></div>'
    elif note:
        ns = note_size or 78
        o += (f'<div class="note" style="left:110px;top:560px;width:760px;font-size:{ns}px;transform:rotate(-2deg)">{note}'
              + (f'<small>{esc(note_sub)}</small>' if note_sub else "") + '</div>')
        o += '<div class="tape" style="left:400px;top:535px;transform:rotate(-3deg)"></div>'
    if lines:
        o += '<div style="position:absolute;left:110px;top:560px;width:760px;display:flex;flex-direction:column;gap:26px">'
        for i, (a, b) in enumerate(lines):
            bg = [YEL, PINK, "#BFE3F2", "#CDEBC3", YEL, PINK][i % 6]
            o += (f'<div style="background:{bg};padding:22px 30px;box-shadow:0 10px 20px rgba(35,38,95,.15);transform:rotate({[-1.2,0.8,-0.6,1,-0.8,0.6][i % 6]}deg)">'
                  f'<div style="font-family:Fredoka;font-weight:700;font-size:50px;color:{IND}">{esc(a)}</div>'
                  + (f'<div class="li" style="font-size:33px;line-height:1.25">{esc(b)}</div>' if b else "") + '</div>')
        o += '</div>'
    if pink:
        o += f'<div class="pink" style="right:120px;bottom:250px;width:360px;transform:rotate(5deg)">{esc(pink)}</div>'
    if stamp:
        o += f'<div class="stamp" style="left:90px;bottom:250px;transform:rotate(-8deg)">{esc(stamp)}</div>'
    o += f'<div class="bt">{esc(bottom)}</div><div class="wt">{esc(button)} ▶</div>'
    return page(o)
