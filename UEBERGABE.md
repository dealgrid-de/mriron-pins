# Übergabe: Pinterest-Pins Mr. Iron (Stand 08.11.2026)

Profil: de.pinterest.com/MrIroneduki · Repo-Spiegel: github.com/dealgrid-de/mriron-pins (Bilder werden per raw.githubusercontent.com-URL in den CSVs referenziert)

## Woher die Bilder kommen
1. **Cover** (`generator/covers/<eduki-ID>.webp`): Die öffentlichen Cover-Bilder der eduki-Materialseiten wurden im eingeloggten Chrome per JavaScript geladen, als Base64 in eine JSON-Datei gepackt (`Downloads\mriron_covers.json`) und in die Arbeitsumgebung übertragen. Kein Zugriff auf Kaufdateien nötig.
2. **Metadaten** (Titel, Fach, Klasse, Kurzbeschreibung, Preis): von den eduki-Materialseiten bzw. der eigenen Materialliste (`generator/meta_part*.json`, `materials_raw.txt`).
3. **Pins** werden NICHT fotografiert oder generiert per Bild-KI, sondern als HTML gebaut (`pin.py`: Fredoka/Nunito, Fachfarben aus `data.py`, Logo aus `assets.py`) und mit Playwright/Chromium als 1000 × 1500 JPG gerendert (`render.py`).

## Varianten (Dateiname `NNN_<eduki-ID>_<V>.jpg`)
- **A** = Cover-Pin (Headline, Cover schräg, Haken, Fußleiste mit CTA)
- **B** = „Darum geht's“ (Nutzen-Headline, Kurzbeschreibung, Cover)
- **S** = Cyber-Sale-Pin (Sale 15.–17.11.2026, eigene Pinnwand, danach archivieren)
- „Kostenlos“-Badge automatisch bei Gratis-Materialien

## Neue Pins bauen
```
pip install playwright pillow && playwright install chromium
cd generator
# neues Cover als covers/<ID>.webp ablegen, Material in data.py/meta ergänzen
python3 plan.py   # baut Plan + Texte
python3 pin.py    # rendert Pins
```

## Hochladen
- `csv/` = Pinterest-Bulk-CSVs (Spalten: Title, Media URL, Pinterest board, Thumbnail, Description, Link, Publish date (UTC), Keywords)
- Pinterest erlaubt max. 100 geplante Pins und ca. 30 Tage Vorlauf → Warteschlange `csv/QUEUE_ab_2026-11-13.csv` (181 Pins bis 14.01.2027) in Portionen nachladen; Ablauf in `csv/NACHFUELLEN_PROMPT.txt`
- Media-URLs zeigen auf das GitHub-Repo → Bilder müssen dort im Branch `main` unter `pins/` liegen

## Inhalt
- `pins/` 294 fertige Pins · `plan.json` alle Pins mit Datum, Uhrzeit (Berlin), Pinnwand, Titel, Beschreibung, Link
- `PINTEREST_PLAN.md` Strategie (Varianten, Pinnwände, Saison)
- `generator/` kompletter Baukasten inkl. Cover, Schriften, Profilbild/Titelbild
