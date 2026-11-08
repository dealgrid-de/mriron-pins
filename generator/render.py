# -*- coding: utf-8 -*-
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from playwright.sync_api import sync_playwright
from PIL import Image


def shoot(jobs, quality=90):
    """jobs: [(html, out_jpg)]"""
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1000, "height": 1500})
        for html, out in jobs:
            tmp = os.path.join(HERE, "html", os.path.basename(out).replace(".jpg", ".html"))
            open(tmp, "w", encoding="utf-8").write(html)
            pg.goto("file://" + tmp); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(150)
            png = out.replace(".jpg", ".png"); pg.screenshot(path=png)
            Image.open(png).convert("RGB").save(out, "JPEG", quality=quality, optimize=True, progressive=True); os.remove(png)
        b.close()
