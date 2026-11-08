# -*- coding: utf-8 -*-
"""Eigene Grafiken (SVG) für den Lernjob 'Expedition Klima'. Alle Grafiken selbst erstellt."""
import math, json, csv, io, base64, os
import qrcode, qrcode.image.svg

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "#12324F"; NAVY2 = "#1E4A6E"; ICE = "#E6F4FA"; ICE2 = "#CDE8F3"; TEAL = "#1C9AAE"; TEALD = "#137485"
SUN = "#FFC23D"; HEAT = "#F0612E"; BERRY = "#B8336A"; GREEN = "#3E9A5A"; INK = "#1F2933"; MUTE = "#5B6B78"
FONT = "font-family:Nunito,sans-serif"; FH = "font-family:Fredoka,sans-serif"

def T(x, y, s, size=12, fill=INK, anchor="start", weight=600, fam=None, extra=""):
    fam = fam or FONT
    if 'paint-order="stroke"' in extra:
        # Halo ohne paint-order (wird nicht von allen PDF-Viewern unterstützt): weiße Kopie darunter, Text darüber
        halo = extra.replace('paint-order="stroke" ', '').replace('paint-order="stroke"', '')
        return (f'<text x="{x:.1f}" y="{y:.1f}" style="{fam};font-size:{size}px;font-weight:{weight}" fill="#fff" text-anchor="{anchor}" {halo}>{s}</text>'
                f'<text x="{x:.1f}" y="{y:.1f}" style="{fam};font-size:{size}px;font-weight:{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')
    return f'<text x="{x:.1f}" y="{y:.1f}" style="{fam};font-size:{size}px;font-weight:{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

def numdot(x, y, n, r=11, fill=NAVY, blank=False):
    if blank:
        return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{fill}" stroke-width="2.2"/>'
                + T(x, y + r * 0.42, n, r * 1.15, fill, "middle", 700, FH))
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#fff" stroke-width="2"/>'
            + T(x, y + r * 0.42, n, r * 1.15, "#fff", "middle", 700, FH))

def arrowhead(x, y, ang, size=9, fill="#000"):
    a1 = ang + math.radians(150); a2 = ang - math.radians(150)
    p = [(x, y), (x + size * math.cos(a1), y + size * math.sin(a1)), (x + size * math.cos(a2), y + size * math.sin(a2))]
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in p)}" fill="{fill}"/>'

def wave(x1, y1, x2, y2, amp=5, wl=18, color=SUN, width=3.2, head=True, dash=None):
    L = math.hypot(x2 - x1, y2 - y1); ang = math.atan2(y2 - y1, x2 - x1)
    n = max(int(L / 2), 2); pts = []
    for i in range(n + 1):
        t = i / n; d = t * (L - 8)
        off = amp * math.sin(2 * math.pi * d / wl) * min(1, d / 10, (L - 8 - d) / 10 + 0.0001)
        px = x1 + d * math.cos(ang) - off * math.sin(ang); py = y1 + d * math.sin(ang) + off * math.cos(ang)
        pts.append(f"{px:.1f},{py:.1f}")
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    s = f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{ds}/>'
    if head:
        s += arrowhead(x2, y2, ang, 4 + width * 2.4, color)
    return s

def line_arrow(x1, y1, x2, y2, color=NAVY, width=2, head=8):
    ang = math.atan2(y2 - y1, x2 - x1)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - math.cos(ang)*head*0.6:.1f}" y2="{y2 - math.sin(ang)*head*0.6:.1f}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>'
            + arrowhead(x2, y2, ang, head, color))

# ---------------------------------------------------------------- Icons
def icon(name, size=24, color=None):
    c = color or NAVY
    body = {
        "pflicht": f'<circle cx="12" cy="12" r="9" fill="{c}"/><path d="M7.5 12.3l3 3 6-6.6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
        "wahl": f'<rect x="5" y="5" width="14" height="14" rx="2" transform="rotate(45 12 12)" fill="#fff" stroke="{c}" stroke-width="2.2"/><circle cx="12" cy="12" r="2.4" fill="{c}"/>',
        "profi": f'<path d="M12 2.6l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z" fill="{SUN}" stroke="#B07A00" stroke-width="1.3" stroke-linejoin="round"/>',
        "video": f'<rect x="2.5" y="3.5" width="19" height="13.5" rx="1.6" fill="#fff" stroke="{c}" stroke-width="2"/><path d="M10 7.2l5 3.1-5 3.1z" fill="{HEAT}"/><path d="M8 21h8M12 17.4V21" stroke="{c}" stroke-width="2" stroke-linecap="round"/>',
        "recherche": f'<circle cx="10" cy="10" r="6" fill="#fff" stroke="{c}" stroke-width="2.4"/><path d="M14.6 14.6l5.4 5.4" stroke="{c}" stroke-width="3" stroke-linecap="round"/>',
        "partner": f'<circle cx="8.4" cy="8" r="3.2" fill="{c}"/><circle cx="15.8" cy="8.6" r="2.8" fill="{TEAL}"/><path d="M2.6 19.5c.4-4 2.6-6 5.8-6s5.4 2 5.8 6z" fill="{c}"/><path d="M12.8 19.5c.3-3.4 1.4-5.2 3.1-5.4 2.6-.2 4.7 1.6 5.3 5.4z" fill="{TEAL}"/>',
        "versuch": f'<path d="M9 3h6M10 3v6l-5.4 9.6A1.8 1.8 0 0 0 6.2 21h11.6a1.8 1.8 0 0 0 1.6-2.4L14 9V3" fill="#fff" stroke="{c}" stroke-width="2" stroke-linejoin="round"/><path d="M6.8 16h10.4l1.4 2.8a.8.8 0 0 1-.7 1.2H6.1a.8.8 0 0 1-.7-1.2z" fill="{TEAL}"/>',
        "kontrolle": f'<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z" fill="{GREEN}"/><path d="M8 12.2l2.8 2.8 5.2-5.6" fill="none" stroke="#fff" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/>',
        "zeit": f'<circle cx="12" cy="13" r="8" fill="#fff" stroke="{c}" stroke-width="2.2"/><path d="M12 8.6V13l3 2" stroke="{c}" stroke-width="2.2" stroke-linecap="round" fill="none"/><path d="M9.5 2.8h5" stroke="{c}" stroke-width="2.2" stroke-linecap="round"/>',
        "hilfe": f'<circle cx="12" cy="12" r="9.4" fill="{SUN}"/><path d="M9.3 9.4a2.8 2.8 0 1 1 3.8 2.6c-.8.4-1.1.9-1.1 1.8v.6" fill="none" stroke="{NAVY}" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="17.3" r="1.3" fill="{NAVY}"/>',
        "stift": f'<path d="M4 20l1.2-4.6L15.6 5a2 2 0 0 1 2.8 0l.6.6a2 2 0 0 1 0 2.8L8.6 18.8z" fill="#fff" stroke="{c}" stroke-width="2" stroke-linejoin="round"/><path d="M13.6 7l3.4 3.4" stroke="{c}" stroke-width="2"/>',
        "rechnen": f'<rect x="4.5" y="2.8" width="15" height="18.4" rx="2.4" fill="#fff" stroke="{c}" stroke-width="2"/><rect x="7" y="5.4" width="10" height="3.6" rx=".8" fill="{TEAL}"/><g fill="{c}"><circle cx="8.6" cy="12.6" r="1.1"/><circle cx="12" cy="12.6" r="1.1"/><circle cx="15.4" cy="12.6" r="1.1"/><circle cx="8.6" cy="16.6" r="1.1"/><circle cx="12" cy="16.6" r="1.1"/><circle cx="15.4" cy="16.6" r="1.1"/></g>',
    }[name]
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

# ---------------------------------------------------------------- QR
def qr_svg_datauri(url):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, border=2, box_size=10)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    rects = []
    for y, row in enumerate(m):
        x = 0
        while x < n:
            if row[x]:
                x0 = x
                while x < n and row[x]: x += 1
                rects.append(f'M{x0} {y}h{x - x0}v1h{-(x - x0)}z')
            else:
                x += 1
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n} {n}" shape-rendering="crispEdges"><rect width="{n}" height="{n}" fill="#fff"/><path d="{"".join(rects)}" fill="{NAVY}"/></svg>'
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()

# ---------------------------------------------------------------- Polar bear (stylised)
def bear(x, y, s=1.0, flip=False):
    tr = f'translate({x},{y}) scale({-s if flip else s},{s})'
    W = "#FBFDFE"; S = "#D6E6EE"; L = "#9FB8C5"
    return f'''<g transform="{tr}">
  <ellipse cx="0" cy="0" rx="46" ry="25" fill="{W}" stroke="{L}" stroke-width="1.4"/>
  <path d="M-40 6 q-4 18 2 30 h12 q2 -14 2 -20z" fill="{W}" stroke="{L}" stroke-width="1.4"/>
  <path d="M-18 14 q-2 14 2 22 h11 q1 -12 0 -22z" fill="{S}" stroke="{L}" stroke-width="1.2"/>
  <path d="M18 12 q-2 14 1 24 h12 q1 -14 -2 -24z" fill="{S}" stroke="{L}" stroke-width="1.2"/>
  <path d="M34 4 q2 18 6 32 h12 q-2 -18 -6 -32z" fill="{W}" stroke="{L}" stroke-width="1.4"/>
  <path d="M30 -16 q22 -14 38 -2 q8 6 10 12 q-2 6 -10 6 q-16 0 -30 8z" fill="{W}" stroke="{L}" stroke-width="1.4"/>
  <circle cx="44" cy="-19" r="5" fill="{W}" stroke="{L}" stroke-width="1.3"/>
  <circle cx="58" cy="-9" r="2.2" fill="{INK}"/>
  <ellipse cx="77.5" cy="0" rx="3.4" ry="2.6" fill="{INK}"/>
  <path d="M-46 -4 q-6 0 -8 4" stroke="{L}" stroke-width="1.4" fill="none"/>
  <path d="M-30 -14 q20 -8 50 -4" stroke="{S}" stroke-width="3" fill="none" stroke-linecap="round"/>
</g>'''

# ---------------------------------------------------------------- Cover
def cover_scene(w=800, h=660):
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">',
         '<defs>',
         f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F2A44"/><stop offset=".45" stop-color="#2C5C86"/><stop offset=".78" stop-color="#F49A6C"/><stop offset="1" stop-color="#FFD27A"/></linearGradient>',
         f'<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2D7F95"/><stop offset="1" stop-color="#0E3550"/></linearGradient>',
         '<radialGradient id="sunglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF1B8" stop-opacity=".95"/><stop offset=".55" stop-color="#FFC23D" stop-opacity=".55"/><stop offset="1" stop-color="#FFC23D" stop-opacity="0"/></radialGradient>',
         '<linearGradient id="ice" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#CFE8F2"/></linearGradient>',
         '<linearGradient id="iceside" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FD0E3"/><stop offset="1" stop-color="#2E8EA8"/></linearGradient>',
         '</defs>']
    hz = h * 0.60
    s.append(f'<rect width="{w}" height="{hz+2}" fill="url(#sky)"/>')
    # stars
    import random; rnd = random.Random(7)
    for _ in range(46):
        sx, sy = rnd.uniform(0, w), rnd.uniform(0, hz * 0.42)
        s.append(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{rnd.uniform(.6,1.8):.1f}" fill="#fff" opacity="{rnd.uniform(.35,.9):.2f}"/>')
    # sun
    s.append(f'<circle cx="{w*0.72}" cy="{hz-8}" r="170" fill="url(#sunglow)"/>')
    s.append(f'<circle cx="{w*0.72}" cy="{hz-8}" r="62" fill="#FFD966"/>')
    # sea
    s.append(f'<rect y="{hz}" width="{w}" height="{h-hz}" fill="url(#sea)"/>')
    s.append(f'<rect x="{w*0.72-70}" y="{hz}" width="140" height="{h-hz}" fill="#FFD27A" opacity=".18"/>')
    for i in range(12):
        yy = hz + 14 + i * 22; xx = (i * 97) % w
        s.append(f'<path d="M{xx} {yy} q18 -6 36 0 t36 0" stroke="#BFE6F0" stroke-width="2" fill="none" opacity="{0.5 - i*0.03:.2f}" stroke-linecap="round"/>')
        s.append(f'<path d="M{(xx+380)%w} {yy+9} q14 -5 28 0 t28 0" stroke="#BFE6F0" stroke-width="1.6" fill="none" opacity="{0.4 - i*0.025:.2f}" stroke-linecap="round"/>')
    # distant iceberg
    s.append(f'<path d="M60 {hz} l40 -52 l26 18 l30 -40 l44 74z" fill="#E9F6FB" opacity=".9"/><path d="M126 {hz-34} l30 -40 l44 74 h-40z" fill="#BFDDEA" opacity=".9"/>')
    # main floe
    fy = hz + 112
    s.append(f'<path d="M150 {fy} L210 {fy-36} L460 {fy-44} L560 {fy-20} L600 {fy+2} L540 {fy+30} L250 {fy+34} Z" fill="url(#ice)"/>')
    s.append(f'<path d="M150 {fy} L250 {fy+34} L540 {fy+30} L600 {fy+2} L600 {fy+20} L540 {fy+56} L250 {fy+58} L150 {fy+16} Z" fill="url(#iceside)"/>')
    s.append(f'<path d="M330 {fy-42} l14 22 l-10 16 l18 24 l-6 14" stroke="#8FBFD0" stroke-width="2.2" fill="none"/>')
    # small floes
    s.append(f'<path d="M620 {fy+30} l40 -12 l50 4 l14 16 l-60 10z" fill="#F4FBFE"/><path d="M620 {fy+30} l44 18 l60 -10 v8 l-60 12 l-44 -18z" fill="#6FB7CC"/>')
    s.append(f'<path d="M70 {fy+70} l30 -8 l36 6 l-12 12 l-44 2z" fill="#F4FBFE"/><path d="M70 {fy+70} l54 8 l12 -12 v6 l-12 12 l-54 -6z" fill="#6FB7CC"/>')
    s.append(f'<path d="M480 {fy+92} l22 -6 l26 4 l-8 8 l-32 2z" fill="#F4FBFE" opacity=".95"/>')
    # drips / meltwater
    for dx in (230, 300, 420, 505):
        s.append(f'<path d="M{dx} {fy+56} q-3 8 0 12 q3 -4 0 -12z" fill="#9AD5E6" opacity=".9"/>')
    s.append(bear(340, fy - 76, 1.3))
    s.append('</svg>')
    return "".join(s)

def thermo(h=220, level=0.78, w=46):
    # big decorative thermometer
    bulb = w * 0.62; tube_w = w * 0.42; top = 10; bot = h - bulb - 4
    fill_top = bot - (bot - top - 8) * level
    s = [f'<svg viewBox="0 0 {w+40} {h}" xmlns="http://www.w3.org/2000/svg">',
         f'<rect x="{(w-tube_w)/2}" y="{top}" width="{tube_w}" height="{bot-top+bulb*0.6}" rx="{tube_w/2}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>',
         f'<circle cx="{w/2}" cy="{h-bulb-2}" r="{bulb}" fill="{HEAT}" stroke="{NAVY}" stroke-width="3"/>',
         f'<rect x="{w/2-tube_w*0.22}" y="{fill_top}" width="{tube_w*0.44}" height="{h-bulb-fill_top}" rx="{tube_w*0.22}" fill="{HEAT}"/>']
    for i in range(7):
        yy = top + 14 + i * (bot - top - 20) / 6
        s.append(f'<line x1="{w/2+tube_w/2+3}" y1="{yy:.1f}" x2="{w/2+tube_w/2+ (12 if i%2==0 else 7)}" y2="{yy:.1f}" stroke="#fff" stroke-width="2.4"/>')
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- Greenhouse panels
def greenhouse(anthro=False, labels=True, blank=False, w=420, h=330):
    """M2: Natürlicher (anthro=False) bzw. verstärkter Treibhauseffekt."""
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">', '<defs>',
         '<linearGradient id="gsp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E2236"/><stop offset="1" stop-color="#26496B"/></linearGradient>',
         f'<linearGradient id="gat{int(anthro)}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{"#F6C9B4" if anthro else "#BFE3F1"}" stop-opacity=".95"/><stop offset="1" stop-color="{"#FBE3D6" if anthro else "#DFF2F9"}"/></linearGradient>',
         '<linearGradient id="gsk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EAF6FB"/><stop offset="1" stop-color="#F7FBFD"/></linearGradient>',
         '<linearGradient id="ggr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7DBB6E"/><stop offset="1" stop-color="#4E8D46"/></linearGradient>',
         '</defs>']
    space_h, atm_top, atm_bot, gy = 64, 64, 150, 268
    s.append(f'<rect width="{w}" height="{space_h}" fill="url(#gsp)" rx="0"/>')
    s.append(T(w - 10, 20, "Weltall", 11, "#CFE3EE", "end", 700))
    s.append(f'<rect y="{atm_top}" width="{w}" height="{atm_bot-atm_top}" fill="url(#gat{int(anthro)})"/>')
    s.append(f'<rect y="{atm_bot}" width="{w}" height="{gy-atm_bot}" fill="url(#gsk)"/>')
    s.append(T(w-10, atm_bot - 8, "Atmosphäre mit Treibhausgasen", 10.5, NAVY2, "end", 800, extra='paint-order="stroke" stroke="#fff" stroke-width="3.5"'))
    # molecules
    import random; rnd = random.Random(3 if anthro else 2)
    n = 70 if anthro else 26
    for _ in range(n):
        mx, my = rnd.uniform(8, w - 8), rnd.uniform(atm_top + 24, atm_bot - 6)
        col = "#5B6B78" if not anthro else rnd.choice(["#5B6B78", "#7A4A3A", "#5B6B78"])
        s.append(f'<g opacity=".75"><circle cx="{mx-3.4:.1f}" cy="{my:.1f}" r="2.3" fill="{col}"/><circle cx="{mx:.1f}" cy="{my:.1f}" r="2.9" fill="{NAVY2}"/><circle cx="{mx+3.4:.1f}" cy="{my:.1f}" r="2.3" fill="{col}"/></g>')
    # ground
    s.append(f'<path d="M0 {gy} Q{w*0.25} {gy-10} {w*0.5} {gy-2} T{w} {gy-4} V{h} H0z" fill="url(#ggr)"/>')
    s.append(f'<rect y="{h-26}" width="{w}" height="26" fill="#2F6F8A"/>')
    for i in range(6):
        s.append(f'<path d="M{20+i*70} {h-14} q10 -4 20 0 t20 0" stroke="#9FD3E2" stroke-width="1.6" fill="none"/>')
    s.append(T(w - 10, h - 6, "Erdoberfläche (Land und Meer)", 9.5, "#fff", "end", 700))
    # houses / trees
    def tree(x, y): return f'<rect x="{x-1.6}" y="{y-10}" width="3.2" height="10" fill="#6B4B2A"/><circle cx="{x}" cy="{y-16}" r="9" fill="#3E7D39"/>'
    def house(x, y): return f'<rect x="{x}" y="{y-16}" width="22" height="16" fill="#F3EDE3" stroke="#8A7A66" stroke-width="1"/><path d="M{x-3} {y-16} l14 -11 l14 11z" fill="#C2553A"/>'
    s.append(tree(26, gy - 2) + tree(48, gy - 4) + house(64, gy - 3) + tree(108, gy - 4))
    if anthro:
        # factory with smoke, car, cow
        fx = 300
        s.append(f'<rect x="{fx}" y="{gy-34}" width="54" height="30" fill="#8A97A3"/><rect x="{fx+38}" y="{gy-62}" width="10" height="30" fill="#6E7B87"/>'
                 f'<rect x="{fx+6}" y="{gy-24}" width="8" height="8" fill="#E9EEF2"/><rect x="{fx+20}" y="{gy-24}" width="8" height="8" fill="#E9EEF2"/>')
        for k, (cx, cy, r) in enumerate([(fx+43, gy-72, 8), (fx+50, gy-84, 11), (fx+60, gy-100, 14), (fx+74, gy-118, 16)]):
            s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#6E6E6E" opacity="{.55 - k*.08:.2f}"/>')
        cx0 = 240
        s.append(f'<rect x="{cx0}" y="{gy-15}" width="34" height="10" rx="3" fill="{HEAT}"/><path d="M{cx0+6} {gy-15} l5 -7 h14 l5 7z" fill="{HEAT}"/><circle cx="{cx0+8}" cy="{gy-4}" r="3.6" fill="{INK}"/><circle cx="{cx0+27}" cy="{gy-4}" r="3.6" fill="{INK}"/>'
                 f'<circle cx="{cx0-4}" cy="{gy-10}" r="3.5" fill="#888" opacity=".5"/><circle cx="{cx0-10}" cy="{gy-14}" r="4.5" fill="#888" opacity=".35"/>')
        # cow
        kx = 168
        s.append(f'<ellipse cx="{kx}" cy="{gy-14}" rx="16" ry="8" fill="#fff" stroke="{INK}" stroke-width="1"/><circle cx="{kx-5}" cy="{gy-16}" r="3.4" fill="{INK}"/><circle cx="{kx+6}" cy="{gy-12}" r="2.6" fill="{INK}"/>'
                 f'<rect x="{kx+12}" y="{gy-24}" width="10" height="9" rx="3" fill="#fff" stroke="{INK}" stroke-width="1"/><path d="M{kx-12} {gy-7} v8 M{kx-6} {gy-7} v8 M{kx+6} {gy-7} v8 M{kx+12} {gy-7} v8" stroke="{INK}" stroke-width="2"/>')
        # stumps (deforestation)
        s.append(f'<rect x="130" y="{gy-8}" width="7" height="6" fill="#6B4B2A"/><rect x="142" y="{gy-7}" width="7" height="5" fill="#6B4B2A"/>')
    else:
        s.append(tree(230, gy - 3) + tree(252, gy - 5) + tree(320, gy - 4) + house(340, gy - 4) + tree(380, gy - 3))
    # sun
    s.append(f'<circle cx="34" cy="30" r="22" fill="{SUN}"/><circle cx="34" cy="30" r="30" fill="{SUN}" opacity=".25"/>')
    # arrows
    s.append(wave(56, 44, 150, gy - 14, 5, 16, SUN, 3.4))                    # 1 Sonnenstrahlung
    s.append(wave(170, atm_bot + 6, 214, 10, 4, 16, "#E8B400", 2.2))         # 2 Reflexion
    s.append(f'<ellipse cx="160" cy="{gy-2}" rx="40" ry="8" fill="{HEAT}" opacity=".35"/>')
    s.append(wave(262, gy - 12, 286, atm_top + 34, 6, 22, HEAT, 3.6))       # 4 Wärmestrahlung
    s.append(wave(300, atm_top + 40, 318, 12, 6, 22, HEAT, 1.8 if anthro else 2.6, True, None))  # entweicht
    s.append(wave(352, atm_top + 40, 356, gy - 16, 6, 22, HEAT, 4.2 if anthro else 3.2))        # 6 Gegenstrahlung
    if anthro:
        s.append(wave(392, atm_top + 44, 400, gy - 16, 6, 22, HEAT, 4.2))
        s.append(wave(216, atm_top + 46, 208, gy - 22, 6, 22, HEAT, 3.6))
    # thermometer
    tx, ty = w - 28, atm_bot + 18
    lev = 0.86 if anthro else 0.55
    s.append(f'<rect x="{tx-5}" y="{ty}" width="10" height="66" rx="5" fill="#fff" stroke="{NAVY}" stroke-width="1.6"/><circle cx="{tx}" cy="{ty+72}" r="9" fill="{HEAT}" stroke="{NAVY}" stroke-width="1.6"/>'
             f'<rect x="{tx-2.4}" y="{ty+66-60*lev:.1f}" width="4.8" height="{60*lev+6:.1f}" fill="{HEAT}"/>')
    s.append(T(tx, ty - 6, "+15 °C" if not anthro else "wärmer!", 11, HEAT if anthro else NAVY, "middle", 800, FH, extra='paint-order="stroke" stroke="#fff" stroke-width="3"'))
    if labels:
        pos = [(92, 108), (198, 92), (160, gy - 2 + 0), (270, 186), (60, 128), (360, 202)]
        # adjust 5 label on molecules band
        pos[4] = (130, 108); pos[0] = (88, 152)
        for i, (x, y) in enumerate(pos, 1):
            s.append(numdot(x, y, str(i), 11, NAVY, blank))
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- Charts
def _axes(x0, y0, x1, y1, xt, yt, xlab, ylab, xfmt=str, yfmt=str, xmap=None, ymap=None, grid=True, size=10.5):
    s = []
    for v in yt:
        yy = ymap(v)
        if grid: s.append(f'<line x1="{x0}" y1="{yy:.1f}" x2="{x1}" y2="{yy:.1f}" stroke="#E1E8ED" stroke-width="1"/>')
        s.append(T(x0 - 6, yy + 3.6, yfmt(v), size, MUTE, "end", 700))
    for v in xt:
        xx = xmap(v)
        s.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{y0+4}" stroke="{MUTE}" stroke-width="1"/>')
        s.append(T(xx, y0 + 16, xfmt(v), size, MUTE, "middle", 700))
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{INK}" stroke-width="1.4"/>')
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{INK}" stroke-width="1.4"/>')
    if xlab: s.append(T((x0 + x1) / 2, y0 + 32, xlab, size, INK, "middle", 800))
    if ylab: s.append(T(x0 - 4, y1 - 10, ylab, size, INK, "start", 800))
    return "".join(s)

def chart_temp(w=520, h=250):
    rows = [(int(a), float(b)) for a, b in csv.reader(open(os.path.join(HERE, "data/temp_noaa.csv")))]
    base = sum(v for y, v in rows if 1850 <= y <= 1900) / 51
    rows = [(y, v - base) for y, v in rows]
    x0, x1, y0, y1 = 52, w - 14, h - 40, 26
    ymin, ymax = -0.4, 1.6
    xm = lambda yr: x0 + (yr - 1850) / (2026 - 1850) * (x1 - x0)
    ym = lambda v: y0 - (v - ymin) / (ymax - ymin) * (y0 - y1)
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    bw = (x1 - x0) / 176 * 0.86
    def col(v):
        stops = [(-0.4, (43, 108, 176)), (0.0, (180, 214, 232)), (0.35, (250, 232, 210)), (0.8, (244, 146, 96)), (1.4, (190, 30, 45))]
        for (a, ca), (b, cb) in zip(stops, stops[1:]):
            if v <= b:
                t = max(0, min(1, (v - a) / (b - a)))
                c = [int(ca[i] + (cb[i] - ca[i]) * t) for i in range(3)]; return f"rgb({c[0]},{c[1]},{c[2]})"
        return "rgb(170,20,35)"
    s.append(_axes(x0, y0, x1, y1, [1850, 1900, 1950, 2000, 2025], [-0.4, 0, 0.4, 0.8, 1.2, 1.6], "Jahr", "Abweichung in °C",
                   str, lambda v: (f"+{v:.1f}" if v > 0 else f"{v:.1f}").replace(".", ",").replace("-", "−"), xm, ym))
    for y, v in rows:
        top, bot = (ym(v), ym(0)) if v >= 0 else (ym(0), ym(v))
        s.append(f'<rect x="{xm(y)-bw/2:.2f}" y="{top:.1f}" width="{bw:.2f}" height="{max(bot-top,0.8):.1f}" fill="{col(v)}"/>')
    s.append(f'<line x1="{x0}" y1="{ym(0):.1f}" x2="{x1}" y2="{ym(0):.1f}" stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/>')
    s.append(f'<line x1="{x0}" y1="{ym(1.5):.1f}" x2="{x1}" y2="{ym(1.5):.1f}" stroke="{BERRY}" stroke-width="1.4" stroke-dasharray="6 4"/>')
    s.append(T(x0 + 6, ym(1.5) - 5, "1,5-Grad-Grenze (Pariser Abkommen)", 10, BERRY, "start", 800))
    s.append(T(x0 + 6, ym(0) - 5, "Durchschnitt 1850–1900 (vorindustriell)", 9.5, MUTE, "start", 700))
    s.append('</svg>')
    return "".join(s)

def chart_seaice(w=520, h=250, blankvals=False):
    rows = [(int(a), float(b)) for a, b in csv.reader(open(os.path.join(HERE, "data/seaice_sep.csv")))]
    x0, x1, y0, y1 = 48, w - 12, h - 40, 22
    ymax = 8
    xm = lambda yr: x0 + (yr - 1978.5) / (2025.5 - 1978.5) * (x1 - x0)
    ym = lambda v: y0 - v / ymax * (y0 - y1)
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    s.append(_axes(x0, y0, x1, y1, [1980, 1990, 2000, 2010, 2020], [0, 2, 4, 6, 8], "Jahr", "Fläche in Mio. km²", str, lambda v: str(v), xm, ym))
    bw = (x1 - x0) / 47 * 0.74
    for y, v in rows:
        hl = y in (1980, 2012, 2025)
        s.append(f'<rect x="{xm(y)-bw/2:.1f}" y="{ym(v):.1f}" width="{bw:.1f}" height="{y0-ym(v):.1f}" rx="1.2" fill="{TEALD if hl else "#7CC6D6"}"/>')
        if hl and not blankvals:
            s.append(T(xm(y), ym(v) - 5, f"{v:.2f}".replace(".", ","), 10, NAVY, "middle", 800))
    s.append('</svg>')
    return "".join(s)

def chart_co2_blank(version="G", w=540, h=300):
    """Leeres Gitter für Liniendiagramm CO2 (Aufgabe erstellen)."""
    x0, x1, y0, y1 = 58, w - 22, h - 44, 18
    nx, ny = 30, 16   # x: 1955..2030 (2,5 Jahre je Kästchen), y: 270..430 (10 ppm je Kästchen)
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    for i in range(nx + 1):
        xx = x0 + i * (x1 - x0) / nx
        s.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{y1}" stroke="#D6E6EE" stroke-width="{1.2 if i%2==0 else 0.6}"/>')
    for j in range(ny + 1):
        yy = y0 - j * (y0 - y1) / ny
        s.append(f'<line x1="{x0}" y1="{yy:.1f}" x2="{x1}" y2="{yy:.1f}" stroke="#D6E6EE" stroke-width="{1.2 if j%2==0 else 0.6}"/>')
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x1+8}" y2="{y0}" stroke="{INK}" stroke-width="1.6"/>' + arrowhead(x1 + 12, y0, 0, 8, INK))
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1-6}" stroke="{INK}" stroke-width="1.6"/>' + arrowhead(x0, y1 - 10, -math.pi / 2, 8, INK))
    if version == "G":
        for yr in (1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025):
            xx = x0 + (yr - 1955) / 75 * (x1 - x0)
            s.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{y0+4}" stroke="{INK}" stroke-width="1.2"/>')
            s.append(T(xx, y0 + 15, str(yr), 9.5, MUTE, "middle", 700))
        for j in range(0, ny + 1, 2):
            yy = y0 - j * (y0 - y1) / ny
            s.append(T(x0 - 6, yy + 3.5, str(270 + j * 10), 9.5, MUTE, "end", 700))
        s.append(T(x0 + 6, y1 + 2, "CO₂ in ppm", 10, INK, "start", 800, extra='paint-order="stroke" stroke="#fff" stroke-width="3"'))
        s.append(T(x1 + 12, y0 + 30, "Jahr", 10, INK, "end", 800))
    s.append('</svg>')
    return "".join(s)

def chart_emissions(w=520, h=230):
    tot = [("China", 12.3), ("USA", 4.9), ("Indien", 3.2), ("Russland", 1.8), ("Deutschland", 0.6)]
    pc = [("USA", 14.2), ("Russland", 12.3), ("China", 8.7), ("Deutschland", 6.8), ("Welt", 4.7), ("Indien", 2.2)]
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    def panel(ox, title, data, vmax, unit, color, fmt):
        out = [T(ox, 16, title, 12, NAVY, "start", 700, FH), T(ox, 31, unit, 9.5, MUTE, "start", 700)]
        bx = ox + 82; bwid = 150
        for i, (k, v) in enumerate(data):
            yy = 44 + i * 29
            hl = k == "Deutschland"
            out.append(T(bx - 6, yy + 13, k, 10.5, NAVY if hl else INK, "end", 800 if hl else 700))
            out.append(f'<rect x="{bx}" y="{yy}" width="{bwid*v/vmax:.1f}" height="18" rx="3" fill="{HEAT if hl else color}"/>')
            out.append(T(bx + bwid * v / vmax + 5, yy + 13.5, fmt(v), 10.5, INK, "start", 800))
        return "".join(out)
    s.append(panel(4, "A  CO₂-Ausstoß gesamt (2024)", tot, 12.3, "in Milliarden Tonnen", TEALD, lambda v: f"{v:.1f}".replace(".", ",")))
    s.append(panel(w / 2 + 6, "B  CO₂-Ausstoß pro Kopf (2024)", pc, 14.2, "in Tonnen pro Person", "#7CC6D6", lambda v: f"{v:.1f}".replace(".", ",")))
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- Maps (Natural Earth, public domain)
_geo = None
def _countries():
    global _geo
    if _geo is None:
        _geo = json.load(open(os.path.join(HERE, "data/countries.geojson")))
    return _geo["features"]

def _rings(geom):
    if geom["type"] == "Polygon": return [geom["coordinates"][0]]
    return [p[0] for p in geom["coordinates"]]

def polar_map(north=True, size=300, labels=None, letters=None, ll_letters=None, ll_labels=None):
    R = size / 2 - 6; cx = cy = size / 2
    lat_edge = 52 if north else -55
    rho_edge = math.cos(math.radians(abs(lat_edge)))
    sc = R / rho_edge
    def proj(lon, lat):
        if north:
            lat = max(lat, 20); r = math.cos(math.radians(lat)) * sc
            a = math.radians(lon) - math.pi / 2
            return cx + r * math.cos(a), cy + r * math.sin(a)
        else:
            lat = min(lat, -20); r = math.cos(math.radians(-lat)) * sc
            a = -math.radians(lon) + math.pi / 2
            return cx + r * math.cos(a), cy - r * math.sin(a)
    cid = "pn" if north else "ps"
    s = [f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">',
         f'<defs><clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath></defs>',
         f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#9ED3E4"/>', f'<g clip-path="url(#{cid})">']
    for f in _countries():
        name = f["properties"].get("NAME", ""); g = f["geometry"]
        for ring in _rings(g):
            lats = [p[1] for p in ring]
            if north and max(lats) < 35: continue
            if (not north) and min(lats) > -40: continue
            pts = " ".join(f"{a:.1f},{b:.1f}" for a, b in (proj(lo, la) for lo, la in ring if abs(la) < 89.5))
            icy = name in ("Greenland", "Antarctica")
            fill = "#FFFFFF" if icy else "#E8DCC4"
            s.append(f'<polygon points="{pts}" fill="{fill}" stroke="{"#9FB8C5" if icy else "#B9A684"}" stroke-width=".7"/>')
    # polar circle
    pc_r = math.cos(math.radians(66.56)) * sc
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{pc_r:.1f}" fill="none" stroke="{NAVY2}" stroke-width="1.2" stroke-dasharray="5 4"/>')
    s.append('</g>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{NAVY}" stroke-width="2"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="3.4" fill="{BERRY}"/>')
    for (x, y, t, sz, col) in (labels or []):
        s.append(T(x, y, t, sz, col, "middle", 800, extra='paint-order="stroke" stroke="#fff" stroke-width="3"'))
    for (lo, la, t, sz, col) in (ll_labels or []):
        x, y = proj(lo, la)
        s.append(T(x, y, t, sz, col, "middle", 800, extra='paint-order="stroke" stroke="#fff" stroke-width="3"'))
    letters = list(letters or [])
    for (lo, la, t) in (ll_letters or []):
        x, y = proj(lo, la); letters.append((x, y, t))
    for (x, y, t) in letters:
        s.append(f'<rect x="{x-11}" y="{y-11}" width="22" height="22" rx="5" fill="{NAVY}" stroke="#fff" stroke-width="1.6"/>' + T(x, y + 5, t, 13, "#fff", "middle", 700, FH))
    s.append('</svg>')
    return "".join(s)

def world_map(w=760, h=380, markers=None):
    lat_top, lat_bot = 82, -58
    xm = lambda lo: (lo + 180) / 360 * w
    ym = lambda la: (lat_top - la) / (lat_top - lat_bot) * h
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">', f'<rect width="{w}" height="{h}" rx="8" fill="#BFE3F0"/>']
    for la in (-40, -20, 0, 20, 40, 60):
        s.append(f'<line x1="0" y1="{ym(la):.1f}" x2="{w}" y2="{ym(la):.1f}" stroke="#A8D4E6" stroke-width="{1.4 if la==0 else .8}"/>')
    for f in _countries():
        if f["properties"].get("NAME") == "Antarctica": continue
        for ring in _rings(f["geometry"]):
            # avoid dateline-wrapping artefacts
            lons = [p[0] for p in ring]
            if max(lons) - min(lons) > 300: continue
            pts = " ".join(f"{xm(lo):.1f},{ym(max(min(la,lat_top),lat_bot)):.1f}" for lo, la in ring)
            de = f["properties"].get("NAME") == "Germany"
            s.append(f'<polygon points="{pts}" fill="{"#F7C9B3" if de else "#F1E9D8"}" stroke="#BFAE8E" stroke-width=".6"/>')
    s.append(T(8, ym(0) - 4, "Äquator", 9, NAVY2, "start", 700))
    for (lo, la, lab) in (markers or []):
        x, y = xm(lo), ym(la)
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="18" fill="{HEAT}" opacity=".25"/><circle cx="{x:.1f}" cy="{y:.1f}" r="12.5" fill="{NAVY}" stroke="#fff" stroke-width="2"/>' + T(x, y + 5, lab, 14, "#fff", "middle", 700, FH))
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- Route map (Lernlandkarte)
def route_map(w=700, h=300):
    stops = [(70, 230, "Start", "Basislager", NAVY), (205, 160, "1", "Treibhaus Erde", HEAT), (345, 215, "2", "Polarstation", TEAL),
             (485, 140, "3", "Weltreise", GREEN), (600, 205, "4", "Zukunftslabor", "#7A5BC7"), (650, 70, "Ziel", "Gipfel", SUN)]
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">',
         f'<rect width="{w}" height="{h}" rx="14" fill="{ICE}"/>']
    # mountains backdrop
    s.append(f'<path d="M520 300 L640 50 L700 160 V300z" fill="#D2E7F0"/><path d="M610 108 L640 50 L668 106 L652 98 L640 112 L628 98z" fill="#fff"/>')
    s.append(f'<path d="M0 300 L120 190 L220 260 L330 180 L430 270 L520 220 L600 300z" fill="#DCEEF5"/>')
    d = "M" + " ".join(f"{x},{y}" for x, y, *_ in stops)
    pts = [(x, y) for x, y, *_ in stops]
    path = f"M{pts[0][0]},{pts[0][1]} " + " ".join(f"Q{(a[0]+b[0])/2},{min(a[1],b[1])-40} {b[0]},{b[1]}" for a, b in zip(pts, pts[1:]))
    s.append(f'<path d="{path}" fill="none" stroke="{NAVY2}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>')
    for (x, y, n, t, c) in stops:
        if n == "Ziel":
            s.append(f'<path d="M{x} {y+18} v-46" stroke="{NAVY}" stroke-width="3"/><path d="M{x} {y-28} l30 9 l-30 9z" fill="{HEAT}"/>')
            s.append(f'<circle cx="{x}" cy="{y+18}" r="20" fill="{SUN}" stroke="#fff" stroke-width="3"/>' + T(x, y + 23, "★", 16, NAVY, "middle", 700))
            s.append(T(x - 40, y + 56, "Gipfel: Abschluss", 12.5, NAVY, "middle", 700, FH))
            continue
        s.append(f'<circle cx="{x}" cy="{y}" r="24" fill="{c}" stroke="#fff" stroke-width="3.5"/>')
        s.append(T(x, y + (7 if len(n) == 1 else 5), n, 20 if len(n) == 1 else 12, "#fff", "middle", 700, FH))
        s.append(T(x, y + 44, t, 13, NAVY, "middle", 700, FH))
        s.append(f'<rect x="{x-8}" y="{y+52}" width="16" height="16" rx="3" fill="#fff" stroke="{NAVY}" stroke-width="1.6"/>')
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- Experiments
def exp_greenhouse(w=360, h=182):
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    s.append(f'<circle cx="180" cy="26" r="16" fill="{SUN}"/>' + T(204, 30, "Lampe oder Sonne", 11, MUTE, "start", 700))
    s.append(wave(166, 42, 96, 110, 3, 12, SUN, 2.2) + wave(194, 42, 262, 110, 3, 12, SUN, 2.2))
    s.append(f'<rect x="20" y="146" width="320" height="10" rx="3" fill="#C9B79C"/>')
    # thermometer A (open)
    def th(x):
        return f'<rect x="{x-4}" y="96" width="8" height="44" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="1.4"/><circle cx="{x}" cy="141" r="6" fill="{HEAT}" stroke="{NAVY}" stroke-width="1.4"/><rect x="{x-1.6}" y="114" width="3.2" height="24" fill="{HEAT}"/>'
    s.append(th(80) + T(80, 174, "A: offen", 11.5, NAVY, "middle", 800))
    s.append(f'<path d="M232 146 V96 Q232 76 252 76 H288 Q308 76 308 96 V146" fill="#DDF1F8" fill-opacity=".55" stroke="{TEALD}" stroke-width="2"/>' + th(270))
    s.append(T(270, 174, "B: unter einem Glas", 11.5, NAVY, "middle", 800))
    s.append('</svg>')
    return "".join(s)

def exp_ice(w=380, h=190):
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    def glass(x, title):
        return (f'<path d="M{x} 50 L{x+8} 160 H{x+112} L{x+120} 50" fill="none" stroke="{NAVY}" stroke-width="2.4"/>'
                f'<path d="M{x+4.6} 104 L{x+8} 160 H{x+112} L{x+115.4} 104z" fill="#9ED3E4" opacity=".85"/>'
                f'<line x1="{x-6}" y1="104" x2="{x+128}" y2="104" stroke="{BERRY}" stroke-width="1.6" stroke-dasharray="4 3"/>'
                + T(x + 60, 30, title, 12, NAVY, "middle", 700, FH))
    s.append(glass(16, "Glas A: „Meereis“"))
    s.append(f'<path d="M50 104 l12 -14 h26 l10 14 l-6 10 h-36z" fill="#fff" stroke="#8FBFD0" stroke-width="1.5"/>')
    s.append(glass(240, "Glas B: „Inlandeis“"))
    s.append(f'<path d="M262 104 L262 72 L320 72 L320 104" fill="#C9B79C" stroke="#8A7A66" stroke-width="1.4"/>')
    s.append(f'<path d="M268 72 l8 -16 h30 l8 16z" fill="#fff" stroke="#8FBFD0" stroke-width="1.5"/>')
    s.append(T(326, 66, "Stein", 10, MUTE, "start", 700))
    s.append(T(190, 182, "gestrichelte Linie = Wasserstand am Anfang markieren", 10.5, BERRY, "middle", 700))
    s.append('</svg>')
    return "".join(s)

# ---------------------------------------------------------------- Feedback loop template (Wirkungsgefüge)
def loop_diagram(kind="albedo", filled=None, w=560, h=250, color=TEAL):
    """Kreislauf mit 4 Kästen. filled: list of 4 strings or None for blank boxes."""
    boxes = [(280, 30), (472, 125), (280, 220), (88, 125)]
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    for i in range(4):
        (ax, ay), (bx, by) = boxes[i], boxes[(i + 1) % 4]
        mx, my = (ax + bx) / 2, (ay + by) / 2
        # curved arrow from box i to i+1
        cx, cy = mx + (mx - 280) * 0.35, my + (my - 125) * 0.35
        sx, sy = ax + (bx - ax) * 0.30, ay + (by - ay) * 0.30
        ex, ey = ax + (bx - ax) * 0.72, ay + (by - ay) * 0.72
        ang = math.atan2(ey - cy, ex - cx)
        s.append(f'<path d="M{sx:.0f} {sy:.0f} Q{cx:.0f} {cy:.0f} {ex:.0f} {ey:.0f}" fill="none" stroke="{color}" stroke-width="3"/>' + arrowhead(ex, ey, ang, 11, color))
    for i, (x, y) in enumerate(boxes):
        s.append(f'<rect x="{x-80}" y="{y-25}" width="160" height="50" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="1.8"/>')
        if filled and filled[i]:
            lines = filled[i].split("|")
            for k, ln in enumerate(lines):
                s.append(T(x, y + 4 - (len(lines) - 1) * 7 + k * 14, ln, 11.5, NAVY, "middle", 800))
    s.append(f'<circle cx="280" cy="125" r="34" fill="{HEAT}" opacity=".14"/>' + T(280, 120, "Teufels-", 12, HEAT, "middle", 700, FH) + T(280, 135, "kreis", 12, HEAT, "middle", 700, FH))
    s.append('</svg>')
    return "".join(s)

def matrix2x2(w=500, h=330):
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    x0, y0, x1, y1 = 60, h - 40, w - 12, 14
    xm = (x0 + x1) / 2; ymid = (y0 + y1) / 2
    fills = ["#E2F2E6", "#FFF3D1", "#E6F4FA", "#FDE6DC"]
    s.append(f'<rect x="{x0}" y="{y1}" width="{xm-x0}" height="{ymid-y1}" fill="{fills[0]}"/>')
    s.append(f'<rect x="{xm}" y="{y1}" width="{x1-xm}" height="{ymid-y1}" fill="{fills[1]}"/>')
    s.append(f'<rect x="{x0}" y="{ymid}" width="{xm-x0}" height="{y0-ymid}" fill="{fills[2]}"/>')
    s.append(f'<rect x="{xm}" y="{ymid}" width="{x1-xm}" height="{y0-ymid}" fill="{fills[3]}"/>')
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="{INK}" stroke-width="1.6"/>' + arrowhead(x1, y0, 0, 9, INK))
    s.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{INK}" stroke-width="1.6"/>' + arrowhead(x0, y1, -math.pi / 2, 9, INK))
    s.append(T((x0 + x1) / 2, h - 12, "Aufwand für mich →  (leicht … schwer)", 12, INK, "middle", 800))
    s.append(f'<text transform="translate(22 {ymid}) rotate(-90)" style="{FONT};font-size:12px;font-weight:800" fill="{INK}" text-anchor="middle">Wirkung fürs Klima →  (klein … groß)</text>')
    s.append(T(x0 + 8, y1 + 18, "Sofort machen!", 12, GREEN, "start", 700, FH))
    s.append(T(x1 - 8, y1 + 18, "Lohnt sich – mit Planung", 12, "#B07A00", "end", 700, FH))
    s.append(T(x0 + 8, y0 - 10, "Kleiner Schritt", 12, TEALD, "start", 700, FH))
    s.append(T(x1 - 8, y0 - 10, "Eher nicht", 12, HEAT, "end", 700, FH))
    s.append('</svg>')
    return "".join(s)

def mini_globe(size=120):
    return (f'<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="54" fill="#2E8EA8"/>'
            f'<path d="M30 30 q14 -8 26 2 q6 10 -4 16 q-12 4 -10 16 q2 12 -10 14 q-10 -6 -12 -20 q-2 -18 10 -28z" fill="#7DBB6E"/>'
            f'<path d="M70 22 q16 2 22 14 q-6 8 -16 6 q-8 6 -4 16 q10 6 8 18 q-6 14 -18 18 q-6 -12 -2 -24 q-10 -10 -4 -24 q2 -18 14 -24z" fill="#7DBB6E"/>'
            f'<path d="M24 22 q36 -20 72 0" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".9"/>'
            f'<circle cx="60" cy="60" r="54" fill="none" stroke="#fff" stroke-width="3"/></svg>')

# ---------------------------------------------------------------- Branding "Mr. Iron"
def logo_tile(size=40, dark=False):
    """Element-Kachel Fe (Eisen, Ordnungszahl 26) – Bildmarke von Mr. Iron."""
    return (f'<svg viewBox="0 0 100 100" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">'
            '<defs><linearGradient id="fe" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5E7385"/><stop offset=".55" stop-color="#2F4152"/><stop offset="1" stop-color="#1B2733"/></linearGradient>'
            '<linearGradient id="fesh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
            '<rect x="3" y="3" width="94" height="94" rx="18" fill="url(#fe)"/>'
            '<path d="M21 3 H79 Q97 3 97 21 V40 Q60 30 3 46 V21 Q3 3 21 3z" fill="url(#fesh)"/>'
            '<rect x="3" y="3" width="94" height="94" rx="18" fill="none" stroke="#FFC23D" stroke-width="3.5"/>'
            '<text x="15" y="27" style="font-family:Fredoka,sans-serif;font-size:16px;font-weight:600" fill="#FFC23D">26</text>'
            '<text x="50" y="72" text-anchor="middle" style="font-family:Fredoka,sans-serif;font-size:46px;font-weight:700;letter-spacing:-1px" fill="#fff">Fe</text>'
            '<text x="50" y="88" text-anchor="middle" style="font-family:Nunito,sans-serif;font-size:10px;font-weight:800;letter-spacing:2px" fill="#C9D5DF">EISEN</text>'
            '</svg>')

def logo(height_mm=12, dark=False, tagline="Unterrichtsmaterial"):
    col = "#fff" if dark else "#12324F"
    sub = "rgba(255,255,255,.85)" if dark else "#5B6B78"
    return (f'<div style="display:inline-flex;align-items:center;gap:{height_mm*0.22:.1f}mm;height:{height_mm}mm">'
            f'<div style="width:{height_mm}mm;height:{height_mm}mm">{logo_tile(100)}</div>'
            f'<div style="line-height:1"><div style="font-family:Fredoka;font-weight:700;font-size:{height_mm*1.75:.1f}pt;color:{col};letter-spacing:.2px">Mr.&nbsp;Iron</div>'
            f'<div style="font-family:Nunito;font-weight:800;font-size:{height_mm*0.52:.1f}pt;letter-spacing:{height_mm*0.12:.1f}px;text-transform:uppercase;color:{sub};margin-top:{height_mm*0.06:.1f}mm">{tagline}</div></div></div>')

def teacher_char(bg=True):
    """Mr. Iron als Figur (eigene Illustration): dunkle Locken, kein Bart, keine Brille, schwarzes Shirt."""
    SK = "#F2C4A0"; SKD = "#E0A982"; HAIR = "#2B1E17"; HAIR2 = "#3D2A20"; NV = "#12324F"; TEE = "#1E1F24"
    s = ['<svg viewBox="0 0 200 200" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">']
    if bg:
        s.append('<circle cx="100" cy="100" r="96" fill="#E6F4FA"/><circle cx="100" cy="100" r="96" fill="none" stroke="#FFC23D" stroke-width="5"/>')
    s.append('<defs><clipPath id="tcc"><circle cx="100" cy="100" r="93.5"/></clipPath></defs><g clip-path="url(#tcc)">')
    # schwarzes T-Shirt mit Fe-Kachel
    s.append(f'<path d="M28 210 Q30 152 100 144 Q170 152 172 210z" fill="{TEE}"/>')
    s.append(f'<path d="M86 145 Q100 156 114 145" fill="none" stroke="#3A3C44" stroke-width="3"/>')
    s.append('<rect x="126" y="166" width="18" height="18" rx="4" fill="#2F4152" stroke="#FFC23D" stroke-width="1.8"/><text x="135" y="179.5" text-anchor="middle" style="font-family:Fredoka;font-size:10px;font-weight:700" fill="#fff">Fe</text>')
    # Hals, Ohren, Kopf
    s.append(f'<path d="M88 128 h24 v18 q-12 7 -24 0z" fill="{SKD}"/>')
    s.append(f'<ellipse cx="61" cy="98" rx="9" ry="12" fill="{SK}"/><ellipse cx="139" cy="98" rx="9" ry="12" fill="{SK}"/>')
    s.append(f'<ellipse cx="100" cy="94" rx="39" ry="45" fill="{SK}"/>')
    # dunkle Locken: kurz an den Seiten, lockig oben
    s.append(f'<path d="M60 92 Q56 58 80 48 Q100 40 122 48 Q144 58 140 92 Q136 74 126 68 Q100 62 74 68 Q64 74 60 92z" fill="{HAIR}"/>')
    for x, y, r in [(70, 60, 9), (80, 50, 10), (93, 45, 10), (106, 44, 10), (119, 48, 10), (130, 57, 9), (75, 68, 7), (87, 60, 8), (100, 56, 8), (113, 58, 8), (125, 66, 7), (66, 74, 6), (135, 74, 6)]:
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{HAIR}"/>')
    for x, y in [(84, 52), (98, 48), (112, 50), (124, 56), (93, 60), (108, 60)]:
        s.append(f'<path d="M{x - 4} {y + 2} q4 -6 8 0" stroke="{HAIR2}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    # Augen (fröhlich, leicht zusammengekniffen) + Brauen
    s.append(f'<ellipse cx="82" cy="94" rx="4.2" ry="4.6" fill="{NV}"/><ellipse cx="118" cy="94" rx="4.2" ry="4.6" fill="{NV}"/><circle cx="83.5" cy="92.5" r="1.3" fill="#fff"/><circle cx="119.5" cy="92.5" r="1.3" fill="#fff"/>'
             f'<path d="M75 99 q7 4 14 0" stroke="{SKD}" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M111 99 q7 4 14 0" stroke="{SKD}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    s.append(f'<path d="M73 84 q9 -6 18 -2" stroke="{HAIR}" stroke-width="3.6" fill="none" stroke-linecap="round"/><path d="M109 82 q9 -4 18 2" stroke="{HAIR}" stroke-width="3.6" fill="none" stroke-linecap="round"/>')
    # Nase, breites Lachen mit Zähnen, Wangen
    s.append(f'<path d="M100 100 q-4 9 2 11" stroke="{SKD}" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    s.append('<path d="M80 116 Q100 140 120 116 Z" fill="#7A2E22"/><path d="M82 117 Q100 124 118 117 L117 121 Q100 127 83 121z" fill="#fff"/>')
    s.append('<path d="M80 116 Q100 140 120 116" fill="none" stroke="#8A3B2A" stroke-width="2.4" stroke-linecap="round"/>')
    s.append('<circle cx="72" cy="110" r="6.5" fill="#F0612E" opacity=".2"/><circle cx="128" cy="110" r="6.5" fill="#F0612E" opacity=".2"/>')
    s.append('</g></svg>')
    return "".join(s)

def logo_char(height_mm=12, dark=False, tagline="Unterrichtsmaterial"):
    col = "#fff" if dark else "#12324F"; sub = "rgba(255,255,255,.85)" if dark else "#5B6B78"
    return (f'<div style="display:inline-flex;align-items:center;gap:{height_mm*0.22:.1f}mm;height:{height_mm}mm">'
            f'<div style="width:{height_mm*1.1}mm;height:{height_mm*1.1}mm">{teacher_char()}</div>'
            f'<div style="line-height:1"><div style="font-family:Fredoka;font-weight:700;font-size:{height_mm*1.75:.1f}pt;color:{col}">Mr.&nbsp;Iron</div>'
            f'<div style="font-family:Nunito;font-weight:800;font-size:{height_mm*0.52:.1f}pt;letter-spacing:{height_mm*0.12:.1f}px;text-transform:uppercase;color:{sub};margin-top:{height_mm*0.06:.1f}mm">{tagline}</div></div></div>')

def chalk_badge():
    """Design C: Tafel-Badge mit Kreideschrift."""
    return ('<svg viewBox="0 0 260 150" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">'
            '<rect x="4" y="4" width="252" height="142" rx="18" fill="#8A5A34"/>'
            '<rect x="14" y="14" width="232" height="112" rx="10" fill="#1F4D45"/>'
            '<path d="M24 30 q60 -8 120 2" stroke="#fff" stroke-opacity=".06" stroke-width="16" fill="none"/>'
            '<text x="130" y="76" text-anchor="middle" style="font-family:Caveat;font-size:58px;font-weight:700" fill="#F7F3E8">Mr. Iron</text>'
            '<path d="M60 90 Q130 100 204 86" stroke="#FFC23D" stroke-width="4" fill="none" stroke-linecap="round"/>'
            '<text x="130" y="114" text-anchor="middle" style="font-family:Nunito;font-size:12px;font-weight:800;letter-spacing:3px" fill="#CFE3DA">UNTERRICHTSMATERIAL</text>'
            '<rect x="186" y="128" width="34" height="9" rx="3" fill="#F7F3E8"/><rect x="160" y="129" width="20" height="8" rx="3" fill="#FFC23D"/>'
            '<g transform="translate(24 122)"><rect width="22" height="22" rx="5" fill="#2F4152" stroke="#FFC23D" stroke-width="1.6"/><text x="11" y="16" text-anchor="middle" style="font-family:Fredoka;font-size:12px;font-weight:700" fill="#fff">Fe</text></g>'
            '</svg>')
