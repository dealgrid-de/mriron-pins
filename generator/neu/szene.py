# -*- coding: utf-8 -*-
"""Realistische Szenen: Mr.-Iron-Hefte perspektivisch auf echte Fotos (Unsplash-Lizenz) legen."""
import os, numpy as np, cv2
from PIL import Image, ImageFilter, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
FOTO = os.path.join(HERE, "fotos")


def load(p):
    return np.asarray(Image.open(p).convert("RGB")).astype(np.float32) / 255.0


def booklet(cover, sheets=3):
    """Cover mit Papierkante (gestapelte Blätter) als RGBA-Array."""
    c = load(cover)
    h, w = c.shape[:2]
    pad = sheets * 4 + 2
    out = np.zeros((h + pad, w + pad, 4), np.float32)
    for i in range(sheets, 0, -1):
        o = i * 4
        g = 0.93 - i * 0.025
        out[o:o + h, o:o + w, :3] = g
        out[o:o + h, o:o + w, 3] = 1
    out[0:h, 0:w, :3] = c
    out[0:h, 0:w, 3] = 1
    return out


def warp(src, quad, size):
    h, w = src.shape[:2]
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), np.float32(quad))
    return cv2.warpPerspective(src, M, size, flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))


def place(photo, cover, quad, shadow=(18, 26, 28, 0.55), sheets=3, light=0.35):
    """photo: float RGB; quad: 4 Eckpunkte (oben links, oben rechts, unten rechts, unten links)."""
    H, W = photo.shape[:2]
    b = booklet(cover, sheets)
    wv = warp(b, quad, (W, H))
    a = wv[..., 3:4]
    dx, dy, blur, op = shadow
    sh = np.roll(np.roll(a[..., 0], int(dy), 0), int(dx), 1)
    sh = cv2.GaussianBlur(sh, (0, 0), blur)[..., None] * op
    img = photo * (1 - sh)
    # Licht des Fotos übernehmen: weich gefilterte Helligkeit
    lum = cv2.GaussianBlur(photo.mean(2), (0, 0), 60)
    lum = lum / max(lum.mean(), 1e-3)
    lumf = (1 - light) + light * np.clip(lum, 0.6, 1.4)
    rgb = wv[..., :3] * lumf[..., None]
    # leichte Wärme/Farbstich des Fotos
    tint = photo.reshape(-1, 3).mean(0); tint = tint / tint.mean()
    rgb = rgb * (0.92 + 0.08 * tint)
    # Kante weichzeichnen (Antialias)
    a2 = cv2.GaussianBlur(a[..., 0], (0, 0), 0.7)[..., None]
    img = img * (1 - a2) + np.clip(rgb, 0, 1) * a2
    return img


def rect_quad(cx, cy, w, h, ang, persp=0.0):
    """gedrehtes Rechteck, optional leichte Perspektive (oben schmaler)."""
    pts = np.array([[-w / 2, -h / 2], [w / 2, -h / 2], [w / 2, h / 2], [-w / 2, h / 2]], np.float32)
    pts[0, 0] += w * persp; pts[1, 0] -= w * persp
    r = np.deg2rad(ang); R = np.array([[np.cos(r), -np.sin(r)], [np.sin(r), np.cos(r)]])
    return (pts @ R.T + [cx, cy]).tolist()


def grain(img, s=0.012):
    return np.clip(img + np.random.default_rng(1).normal(0, s, img.shape), 0, 1)


def save(img, path, q=92):
    Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)).save(path, quality=q)


def fit(photo_path, W, H, fx=0.5, fy=0.5):
    """Foto auf W x H zuschneiden (cover)."""
    im = Image.open(photo_path).convert("RGB")
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = int((im.width - W) * fx); y = int((im.height - H) * fy)
    return np.asarray(im.crop((x, y, x + W, y + H))).astype(np.float32) / 255.0
