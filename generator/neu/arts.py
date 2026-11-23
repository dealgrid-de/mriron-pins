# -*- coding: utf-8 -*-
"""Artikel-Pins (Inhalte aus den Artikeln auf mriron.de, Stand 23.11.2026)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import creative2 as K

D, G, GK, W, FU, KL = "#B8336A", "#B5600F", "#137485", "#3E9A5A", "#F0612E", "#1C7A55"
U = "https://mriron.de/"
cards, grid, two, chips, big, note = K.blk_cards, K.blk_grid, K.blk_two, K.blk_chips, K.blk_big, K.blk_note
A = []


def add(slug, url, html, title, desc, kw):
    assert len(title) <= 100, title
    A.append(dict(slug=slug, url=U + url + "/", html=html, title=title, desc=desc, kw=kw))


# Inhaltsangabe
add("inhaltsangabe1", "inhaltsangabe-schreiben", K.pin("Deutsch · Klasse 7/8", "Inhaltsangabe schreiben", "In 3 Schritten – mit Basissatz-Formel", cards([
    ("Basissatz", "Textsorte, Titel, Autor, Jahr und Thema in einem Satz."),
    ("Hauptteil", "Die wichtigsten Handlungsschritte in richtiger Reihenfolge, mit Zusammenhängen."),
    ("Schluss (falls verlangt)", "Kurze Deutung oder Stellungnahme, klar vom Hauptteil getrennt.")], D, ["1", "2", "3"])
    + note("Formel: In der [Textsorte] „[Titel]“ von [Autor] ([Jahr]) geht es um [Thema]."), D),
    "Inhaltsangabe schreiben: Aufbau, Basissatz und Beispiel für Deutsch Klasse 7/8",
    "So gelingt die Inhaltsangabe in Klasse 7/8: Basissatz mit Formel, Hauptteil in der richtigen Reihenfolge, Schluss nur wenn verlangt. Im Artikel mit Beispiel und den wichtigsten Regeln. #Deutschunterricht #Inhaltsangabe #Realschule",
    "Inhaltsangabe schreiben, Inhaltsangabe Aufbau, Basissatz Inhaltsangabe, Inhaltsangabe Klasse 7, Inhaltsangabe Klasse 8, Deutsch Schreiben")
add("inhaltsangabe2", "inhaltsangabe-schreiben", K.pin("Deutsch · Klasse 7/8", "Inhaltsangabe: 5 Regeln", "Was rein darf – und was nicht", cards([
    ("Präsens", "Vorzeitiges steht im Perfekt."),
    ("Keine wörtliche Rede", "Stattdessen dass-Satz oder indirekte Rede mit Konjunktiv I."),
    ("Keine eigene Meinung", "Keine Spannung, keine Wertung – höchstens im Schluss, wenn verlangt."),
    ("Deutlich kürzer", "Gliedern, weglassen, bündeln, Oberbegriffe finden."),
    ("Basissatz nie weglassen", "Nicht mitten in der Handlung beginnen.")], D, ["✓", "✗", "✗", "✓", "✓"]), D, light=True),
    "Inhaltsangabe Regeln: Präsens, keine wörtliche Rede, keine Meinung – Spickzettel Klasse 7/8",
    "Die fünf wichtigsten Regeln für die Inhaltsangabe auf einen Blick: Präsens, indirekte Rede statt wörtlicher Rede, keine Wertung, kürzer als das Original und immer mit Basissatz. Zum Merken für Deutsch Klasse 7/8. #Inhaltsangabe #Deutschunterricht #Spickzettel",
    "Inhaltsangabe Regeln, Inhaltsangabe Zeitform, indirekte Rede Inhaltsangabe, Inhaltsangabe Fehler, Deutsch Klasse 7, Deutsch Spickzettel")

# Handyverbot
add("handy1", "handyverbot-schule-pro-contra", K.pin("Gemeinschaftskunde · Deutsch · Klasse 7/8", "Handyverbot an Schulen", "Pro und Contra auf einen Blick", two(
    ("Pro", K.GREEN, [("Konzentration", "Ohne Benachrichtigungen wird der Unterricht ruhiger."), ("Pausen", "Wieder mehr reden und bewegen."), ("Schutz", "Weniger heimliche Fotos und Cybermobbing auf dem Hof."), ("Gesundheit", "Weniger Bildschirmzeit.")]),
    ("Contra", K.RED, [("Medienkompetenz", "Umgang wird nicht gelernt, wenn das Handy weggesperrt ist."), ("Alltag", "Vertretungsplan, Bus, Eltern laufen übers Handy."), ("Verlagerung", "Cybermobbing passiert meist nach der Schule."), ("Kontrolle", "Einsammeln kostet Zeit, wirft Haftungsfragen auf.")])), GK),
    "Handyverbot an Schulen: Pro und Contra – Argumente für Stellungnahme und Debatte",
    "Handyverbot an Schulen – die wichtigsten Argumente dafür und dagegen: Konzentration, Pausen, Schutz und Gesundheit gegen Medienkompetenz, Alltag, Verlagerung und Kontrolle. Im Artikel: was in Baden-Württemberg gilt und eine Unterrichtsidee für Klasse 7/8. #Handyverbot #Unterrichtsideen #Debatte",
    "Handyverbot Schule Pro Contra, Handyverbot Argumente, Handyverbot Baden-Württemberg, Stellungnahme Handyverbot, Debatte Unterricht, Erörterung Handy")
add("handy2", "handyverbot-schule-pro-contra", K.pin("Baden-Württemberg · Stand 21.11.2026", "Handyverbot in BW: Was gilt?", "", cards([
    ("Heute", "Kein landesweites Verbot. Jede Schule regelt die Handynutzung in ihrer Schulordnung (§ 23 Abs. 2b SchG)."),
    ("Geplant", "Eckpunkte vom 19.08.2026: privates Handy ab 2027/28 ganztags verboten, mit Ausnahmen. Noch nicht beschlossen."),
    ("Im Unterricht", "Stellungnahme schreiben: These, Begründung, Beispiel – oder Schulkonferenz als Rollenspiel.")], GK, ["!", "?", "✓"]), GK, light=True),
    "Handyverbot Schule Baden-Württemberg: Was heute gilt und was geplant ist",
    "Gibt es ein Handyverbot an Schulen in Baden-Württemberg? Stand 21.11.2026: Jede Schule regelt es selbst in der Schulordnung, ein landesweites Verbot ab 2027/28 ist geplant, aber noch nicht beschlossen. Mit Quellen und Unterrichtsidee im Artikel. #Handyverbot #Schule #BadenWürttemberg",
    "Handyverbot Baden-Württemberg, Handyverbot Schule BW, Schulgesetz Handy, Handynutzung Schulordnung, Handyverbot 2027")

# EU
add("eu1", "europaeische-union-einfach-erklaert", K.pin("Gemeinschaftskunde · Klasse 9/10", "Die 5 Organe der EU", "einfach erklärt", cards([
    ("Europäisches Parlament", "Wirkt an Gesetzen und Haushalt mit, kontrolliert die Kommission."),
    ("Rat der EU", "Die Fachminister der Mitgliedstaaten wirken an Gesetzen mit."),
    ("Europäische Kommission", "Schlägt Gesetze vor, „Hüterin der Verträge“."),
    ("Europäischer Rat", "Staats- und Regierungschefs legen die großen Ziele fest."),
    ("Gerichtshof der EU", "Legt EU-Recht aus und entscheidet Streitfälle.")], GK, ["1", "2", "3", "4", "5"]), GK),
    "EU einfach erklärt: die 5 Organe der Europäischen Union – Gemeinschaftskunde Klasse 9/10",
    "Parlament, Rat der EU, Kommission, Europäischer Rat und Gerichtshof: die fünf Organe der EU mit ihren Aufgaben auf einen Blick. Im Artikel: wie ein EU-Gesetz entsteht, mit Zahlen und Bezug zum Bildungsplan BW. #Gemeinschaftskunde #EU #Unterricht",
    "EU Organe, EU einfach erklärt, Organe der Europäischen Union, EU Gemeinschaftskunde, Europäische Union Klasse 9, EU Arbeitsblatt")
add("eu2", "europaeische-union-einfach-erklaert", K.pin("Gemeinschaftskunde · Klasse 9/10", "So entsteht ein EU-Gesetz", "in 6 Schritten", cards([
    ("Vorschlag", "Die Kommission legt einen Vorschlag vor."), ("Parlament", "berät und legt seine Position fest."), ("Rat der EU", "legt seine Position fest."),
    ("Trilog", "Parlament, Rat und Kommission verhandeln einen gemeinsamen Text."), ("Zustimmung", "Parlament und Rat stimmen dem Kompromiss zu."),
    ("Amtsblatt", "Das Gesetz wird veröffentlicht und tritt in Kraft.")], GK, ["1", "2", "3", "4", "5", "6"]), GK, light=True),
    "Wie entsteht ein EU-Gesetz? Gesetzgebung der EU in 6 Schritten einfach erklärt",
    "Vom Vorschlag der Kommission über Parlament, Rat und Trilog bis zum Amtsblatt: das ordentliche Gesetzgebungsverfahren der EU in sechs Schritten. Für Gemeinschaftskunde Klasse 9/10. #EU #Gemeinschaftskunde #Politikunterricht",
    "EU Gesetzgebung, wie entsteht ein EU Gesetz, Trilog EU, ordentliches Gesetzgebungsverfahren, EU Klasse 10, Gemeinschaftskunde EU")
add("eu3", "europaeische-union-einfach-erklaert", K.pin("Stand November 2026", "EU in Zahlen", "Für den Einstieg in Klasse 9/10", big([
    ("27", "Mitgliedstaaten"), ("720", "Abgeordnete im EU-Parlament (Wahl 2024)"), ("21", "Länder mit dem Euro – seit 2026 auch Bulgarien"), ("2020", "Großbritannien tritt aus")], GK), GK),
    "EU in Zahlen: 27 Mitgliedstaaten, 720 Abgeordnete, 21 Euro-Länder – Einstieg Gemeinschaftskunde",
    "Die EU in vier Zahlen (Stand November 2026): 27 Mitgliedstaaten, 720 Abgeordnete im Europäischen Parlament, 21 Länder mit dem Euro und der Brexit 2020. Perfekter Einstieg für Gemeinschaftskunde Klasse 9/10. #EU #Gemeinschaftskunde #Unterrichtseinstieg",
    "EU Zahlen, EU Mitgliedstaaten 2026, Euro Länder, EU Parlament Abgeordnete, EU Unterricht Einstieg, Gemeinschaftskunde Klasse 9")

# Familienformen
add("familie1", "familienformen-einfach-erklaert", K.pin("Gemeinschaftskunde · Klasse 7–9", "Familienformen heute", "8 Lebensformen einfach erklärt", grid([
    ("Kernfamilie", "Verheiratete Eltern mit gemeinsamen Kindern."), ("Nichteheliche Lebensgemeinschaft", "Unverheiratetes Paar mit Kindern."),
    ("Alleinerziehende", "Ein Elternteil lebt mit den Kindern."), ("Patchworkfamilie", "Paar mit Kindern aus früheren Beziehungen."),
    ("Regenbogenfamilie", "Zwei Mütter oder zwei Väter mit Kindern."), ("Pflegefamilie", "Kinder bei Pflegeeltern, begleitet vom Jugendamt."),
    ("Adoptivfamilie", "Kind rechtlich als eigenes angenommen."), ("Mehrgenerationenfamilie", "Kinder, Eltern, Großeltern unter einem Dach.")], GK), GK),
    "Familienformen einfach erklärt: 8 Lebensformen für Gemeinschaftskunde Klasse 7–9",
    "Kernfamilie, Patchwork, Regenbogenfamilie, Alleinerziehende und mehr: acht Familienformen mit kurzer Erklärung. Im Artikel auch die Aufgaben der Familie und was der Staat für Familien tut. Für Gemeinschaftskunde Klasse 7–9. #Gemeinschaftskunde #Familie #Unterricht",
    "Familienformen, Familienformen Arbeitsblatt, Lebensformen Familie, Patchworkfamilie, Gemeinschaftskunde Klasse 7, Familie Unterricht")
add("familie2", "familienformen-einfach-erklaert", K.pin("Gemeinschaftskunde · Klasse 7–9", "Was der Staat für Familien tut", "", cards([
    ("Grundgesetz Art. 6", "Schutz der Familie"), ("Kindergeld", ""), ("Elterngeld", "bei Betreuung nach der Geburt"),
    ("Kinderzuschlag & Unterhaltsvorschuss", "für Familien mit wenig Geld bzw. Alleinerziehende"), ("Kita-Platz", "mit Rechtsanspruch"),
    ("Ganztag in der Grundschule", "mit Rechtsanspruch")], GK, ["§", "€", "€", "€", "✓", "✓"]), GK, light=True),
    "Familienpolitik einfach erklärt: Was der Staat für Familien tut – Gemeinschaftskunde",
    "Grundgesetz Artikel 6, Kindergeld, Elterngeld, Kinderzuschlag, Unterhaltsvorschuss und Rechtsanspruch auf Betreuung: So unterstützt der Staat Familien. Mit Familienformen und Aufgaben der Familie im Artikel. #Gemeinschaftskunde #Familienpolitik",
    "Familienpolitik, Staat Familie Unterstützung, Kindergeld Elterngeld Unterricht, Artikel 6 Grundgesetz, Gemeinschaftskunde Familie")

# HSA Deutsch 2027
add("hsa1", "hauptschulabschluss-deutsch-2027-vorbereitung", K.pin("Hauptschulabschluss Deutsch 2027 · BW", "Die 4 Prüfungsaufgaben", "180 Minuten · 80 Punkte · 27. April 2027", cards([
    ("Sachtext und Rechtschreibung", "Fragen vor dem Text lesen, jede Antwort mit Textbeleg absichern."),
    ("Stellungnahme (18 Punkte)", "Fester Aufbau – und an die Briefform denken."),
    ("Gedicht oder Prosatext", "Beides üben, Stilmittel immer mit Wirkung erklären."),
    ("Ganzschrift (Schreibaufgabe 8 Punkte)", "Wer ist die Figur, was weiß und fühlt sie an dieser Stelle?")], D, ["1", "2", "3", "4"]), D),
    "Hauptschulabschluss Deutsch 2027 BW: die 4 Prüfungsaufgaben und wie man sie trainiert",
    "HSA Deutsch 2027 in Baden-Württemberg: Prüfung am 27. April 2027, 180 Minuten, 80 Punkte. Die vier Aufgaben mit Trainingstipps – Sachtext und Rechtschreibung, Stellungnahme, Gedicht oder Prosa, Ganzschrift. #Hauptschulabschluss #Deutschunterricht #Prüfung2027",
    "Hauptschulabschluss Deutsch 2027, HSA Deutsch BW, Prüfungsvorbereitung Hauptschulabschluss, Deutsch Klasse 9 Prüfung, Hauptschulprüfung Deutsch")
add("hsa2", "hauptschulabschluss-deutsch-2027-vorbereitung", K.pin("HSA Deutsch 2027 · Baden-Württemberg", "Prüfungstermine 2027", "", big([
    ("27.4.", "Hauptprüfung, Dienstag, ab 9 Uhr"), ("3.6.", "Nachtermin, Donnerstag"), ("180", "Minuten"), ("80", "Punkte")], D)
    + note("Lektüren 2027: „Der Tunnelbauer“ (Maja Nielsen) oder „Über kurz oder lang“ (Marie-Aude Murail)"), D, light=True),
    "HSA Deutsch 2027 BW: Prüfungstermin 27. April, Nachtermin 3. Juni – alles auf einen Blick",
    "Hauptschulabschluss Deutsch 2027 Baden-Württemberg: Hauptprüfung am Dienstag, 27. April 2027 ab 9 Uhr, Nachtermin am 3. Juni 2027, 180 Minuten und 80 Punkte. Mit den Prüfungslektüren und Trainingstipps im Artikel. #Hauptschulabschluss #Prüfung2027",
    "Hauptschulabschluss 2027 Termin, HSA Deutsch Prüfungstermin, Prüfung 27. April 2027, Hauptschulabschluss BW 2027, Prüfungslektüre HSA 2027")

# Steckbrief
add("steckbrief1", "steckbrief-schreiben", K.pin("Deutsch · Klasse 5/6", "Steckbrief schreiben", "Aufbau und Regeln", cards([
    ("Überschrift", "Wer oder was wird vorgestellt?"), ("Bild", "Zeichnung oder Foto"), ("Merkmale", "In Stichpunkten: „Merkmal: Angabe“"), ("Besonderheit", "Was macht sie oder ihn einzigartig?")], D, ["1", "2", "3", "4"])
    + chips(["Nur Fakten", "Kurz und sachlich", "Keine ganzen Sätze nötig", "Buchfigur: Seite angeben"]), D),
    "Steckbrief schreiben: Aufbau, Vorlage und Regeln für Deutsch Klasse 5/6",
    "Steckbrief in Klasse 5/6: Überschrift, Bild, Merkmale in Stichpunkten und Besonderheit – nur Fakten, kurz und sachlich. Im Artikel mit Vorlage und Beispielen für Person, Tier und Buchfigur. #Steckbrief #Deutschunterricht #Klasse5",
    "Steckbrief schreiben, Steckbrief Vorlage, Steckbrief Klasse 5, Steckbrief Buchfigur, Steckbrief Tier, Deutsch Klasse 5")
add("steckbrief2", "steckbrief-schreiben", K.pin("Deutsch · Klasse 5/6 · Beispiel", "Steckbrief: Ella Brandt", "ausgedachte Person", cards([
    ("Alter", "elf Jahre"), ("Wohnort", "eine Kleinstadt am Neckar"), ("Aussehen", "lange rote Haare, Sommersprossen, meist eine grüne Jacke"),
    ("Familie", "Mutter, Vater, kleiner Bruder Ben"), ("Hobbys", "Fußball, Zeichnen, Comics lesen"), ("Besonderheit", "hat einen Hund namens Keks, der Fußbälle fängt")], D), D, light=True),
    "Steckbrief Beispiel Person für Klasse 5: so sieht ein guter Steckbrief aus",
    "Ein Steckbrief-Beispiel zum Zeigen in Klasse 5/6: Alter, Wohnort, Aussehen, Familie, Hobbys und Besonderheit in Stichpunkten. Im Artikel mit Vorlage und weiteren Beispielen für Tier und Buchfigur. #Steckbrief #Deutschunterricht",
    "Steckbrief Beispiel, Steckbrief Person, Steckbrief Muster, Steckbrief Klasse 5, Steckbrief Grundschule weiterführende Schule")

# Kurzgeschichte
add("kurzg1", "kurzgeschichte-merkmale-analyse", K.pin("Deutsch · Klasse 7–10", "Merkmale der Kurzgeschichte", "8 Merkmale auf einen Blick", grid([
    ("Unvermittelter Anfang", "Mitten im Geschehen, ohne Einleitung."), ("Offenes Ende", "Fragen bleiben offen."), ("Alltagssituation", "Gewöhnliche Menschen, alltägliche Momente."),
    ("Wendepunkt", "Ein Ereignis verändert alles."), ("Kurze erzählte Zeit", "Meist Minuten oder Stunden."), ("Wenige Figuren", "Meist zwei oder drei."),
    ("Alltagssprache", "Knappe Sätze, oft Dialoge."), ("Andeutungen", "Gesten sagen mehr als Worte.")], D), D),
    "Merkmale der Kurzgeschichte: 8 Merkmale mit Erklärung – Spickzettel Deutsch Klasse 7–10",
    "Unvermittelter Anfang, offenes Ende, Wendepunkt, Alltagssituation und mehr: die acht Merkmale der Kurzgeschichte auf einem Spickzettel. Im Artikel mit Analyse-Aufbau und Beispielgeschichte. #Kurzgeschichte #Deutschunterricht #Spickzettel",
    "Merkmale Kurzgeschichte, Kurzgeschichte Merkmale Klasse 8, Kurzgeschichte Analyse, Kurzgeschichte Deutsch, Spickzettel Deutsch")
add("kurzg2", "kurzgeschichte-merkmale-analyse", K.pin("Deutsch · Klasse 7–10", "Kurzgeschichte analysieren", "Aufbau in 5 Schritten", cards([
    ("Einleitung", "Titel, Autor, Textsorte, Jahr und Thema in einem Satz."), ("Inhalt", "Kurz, im Präsens, ohne wörtliche Rede."),
    ("Analyse", "Figuren, Aufbau, Erzählperspektive, Sprache – mit Textbelegen."), ("Deutung", "Was bedeuten Wendepunkt, Symbole und offenes Ende?"),
    ("Schluss", "Deutung zusammenfassen, eigene begründete Meinung.")], D, ["1", "2", "3", "4", "5"]), D, light=True),
    "Kurzgeschichte analysieren: Aufbau der Analyse in 5 Schritten für Klasse 7–10",
    "So schreiben Schülerinnen und Schüler eine Kurzgeschichten-Analyse: Einleitung, Inhalt, Analyse mit Textbelegen, Deutung und Schluss. Mit Merkmalen und Beispielgeschichte im Artikel. #Kurzgeschichte #Textanalyse #Deutschunterricht",
    "Kurzgeschichte analysieren, Kurzgeschichte Analyse Aufbau, Interpretation Kurzgeschichte, Textanalyse Klasse 9, Deutsch Prüfung Prosa")

# John Maynard
add("maynard1", "john-maynard-ballade", K.pin("Deutsch · Klasse 7/8", "John Maynard", "Fontanes Ballade in 5 Schritten", cards([
    ("Die Fahrt", "Die „Schwalbe“ fährt auf dem Eriesee von Detroit nach Buffalo."), ("Das Feuer", "Im Schiffsraum bricht Feuer aus, alle drängen zum Bug."),
    ("Am Steuer", "Maynard hält das Schiff im Qualm auf Kurs zum Ufer."), ("Die Rettung", "Das Schiff läuft auf den Strand – alle gerettet, nur Maynard stirbt."),
    ("Die Trauer", "Buffalo ehrt Maynard mit einer Grabinschrift.")], D, ["1", "2", "3", "4", "5"])
    + note("Theodor Fontane, 1886 · Vorbild: Brand der „Erie“ 1841"), D),
    "John Maynard von Fontane einfach erklärt: Inhalt der Ballade in 5 Schritten",
    "John Maynard (Theodor Fontane, 1886) einfach erklärt: Fahrt, Feuer, Steuermann, Rettung und Trauer in fünf Schritten. Im Artikel: Aufbau, Merkmale der Ballade und Deutung für Deutsch Klasse 7/8. #Ballade #JohnMaynard #Deutschunterricht",
    "John Maynard, John Maynard Inhalt, Ballade Fontane, Ballade Klasse 7, Balladen Unterricht, John Maynard Interpretation")
add("maynard2", "john-maynard-ballade", K.pin("Deutsch · Klasse 7/8", "Was macht eine Ballade aus?", "am Beispiel „John Maynard“", cards([
    ("Lyrik", "Strophen, Verse und Reime – überwiegend Paarreim."), ("Epik", "Eine Handlung wird erzählt: Fahrt, Feuer, Rettung, Begräbnis."),
    ("Dramatik", "Dialog zwischen Kapitän und Steuermann, Spannung bis zum Höhepunkt."), ("Countdown", "Die Zeit bis Buffalo wird immer knapper."),
    ("Rahmen", "Frage am Anfang, Grabinschrift am Schluss.")], D, ["L", "E", "D", "⏱", "▢"]), D, light=True),
    "Merkmale der Ballade einfach erklärt: Lyrik, Epik, Dramatik – am Beispiel John Maynard",
    "Eine Ballade verbindet Lyrik, Epik und Dramatik. Am Beispiel von Fontanes „John Maynard“ erklärt: Reime, Handlung, Dialog, Countdown und Rahmen. Für Deutsch Klasse 7/8. #Ballade #Deutschunterricht #Lyrik",
    "Merkmale Ballade, Ballade Lyrik Epik Dramatik, Ballade Klasse 7, Ballade erklären, John Maynard Merkmale")

# Nationalsozialismus
add("ns1", "nationalsozialismus-einfach-erklaert", K.pin("Geschichte · Klasse 9/10", "Nationalsozialismus", "in 8 Daten", cards([
    ("30. Januar 1933", "Hitler wird Reichskanzler."), ("23. März 1933", "Ermächtigungsgesetz"), ("September 1935", "Nürnberger Gesetze entrechten Jüdinnen und Juden."),
    ("9./10. November 1938", "Novemberpogrome: Synagogen brennen."), ("1. September 1939", "Überfall auf Polen – Zweiter Weltkrieg beginnt."),
    ("20. Januar 1942", "Wannseekonferenz organisiert den Völkermord."), ("20. Juli 1944", "Das Attentat auf Hitler scheitert."), ("8. Mai 1945", "Bedingungslose Kapitulation")], G), G),
    "Nationalsozialismus Zeitstrahl: 8 wichtige Daten 1933–1945 für Geschichte Klasse 9/10",
    "Machtübernahme, Ermächtigungsgesetz, Nürnberger Gesetze, Novemberpogrome, Kriegsbeginn, Wannseekonferenz, 20. Juli 1944 und Kriegsende: der Nationalsozialismus in acht Daten. Im Artikel mit Begriffen und Widerstand. #Geschichtsunterricht #Nationalsozialismus",
    "Nationalsozialismus Zeitstrahl, NS-Zeit einfach erklärt, Nationalsozialismus Klasse 9, Daten 1933 bis 1945, Geschichte Klasse 10")
add("ns2", "nationalsozialismus-einfach-erklaert", K.pin("Geschichte · Klasse 9/10", "NS-Zeit: Begriffe einfach erklärt", "", grid([
    ("Gleichschaltung", "Ausrichtung von Staat und Gesellschaft auf die NSDAP."), ("Ermächtigungsgesetz", "Regierung macht Gesetze ohne Reichstag (März 1933)."),
    ("Nürnberger Gesetze", "Rassistische Gesetze von 1935, nahmen Jüdinnen und Juden die Bürgerrechte."), ("Holocaust (Shoah)", "Mord an rund sechs Millionen europäischen Jüdinnen und Juden."),
    ("Volksgemeinschaft", "Nur „Zugehörige“ gelten als vollwertig."), ("Führerprinzip", "Alle Macht bei einer obersten Führungsperson.")], G), G, light=True),
    "NS-Zeit Begriffe einfach erklärt: Gleichschaltung, Ermächtigungsgesetz, Volksgemeinschaft",
    "Die wichtigsten Begriffe zum Nationalsozialismus kurz erklärt: Gleichschaltung, Ermächtigungsgesetz, Nürnberger Gesetze, Holocaust, Volksgemeinschaft und Führerprinzip. Für Geschichte Klasse 9/10. #Geschichtsunterricht #Nationalsozialismus",
    "Gleichschaltung einfach erklärt, Ermächtigungsgesetz, Volksgemeinschaft, NS Begriffe, Nationalsozialismus Glossar, Geschichte Klasse 9")
add("ns3", "nationalsozialismus-einfach-erklaert", K.pin("Geschichte · Klasse 9/10", "Widerstand gegen Hitler", "3 Beispiele für den Unterricht", cards([
    ("Georg Elser", "Bombenanschlag auf Hitler 1939 – als Einzeltäter."), ("Weiße Rose", "Sophie und Hans Scholl verteilten Flugblätter, 1943 hingerichtet."),
    ("Claus Schenk Graf von Stauffenberg", "Scheiterte mit dem Attentat am 20. Juli 1944.")], G, ["1939", "1943", "1944"]), G),
    "Widerstand im Nationalsozialismus: Georg Elser, Weiße Rose, Stauffenberg – Geschichte Klasse 9",
    "Drei Beispiele für Widerstand gegen den Nationalsozialismus: Georg Elser 1939, die Weiße Rose mit Sophie und Hans Scholl und das Attentat vom 20. Juli 1944. Im Artikel mit Zeitstrahl und Begriffen. #Geschichtsunterricht #Widerstand #WeißeRose",
    "Widerstand Nationalsozialismus, Weiße Rose Unterricht, Georg Elser, Stauffenberg 20. Juli, Widerstand Klasse 9")

# Erster Weltkrieg
add("wk1a", "erster-weltkrieg-einfach-erklaert", K.pin("Geschichte · Klasse 8/9", "Erster Weltkrieg", "Zeitstrahl 1914–1919", cards([
    ("28. Juni 1914", "Attentat von Sarajevo"), ("1.–4. August 1914", "Kriegserklärungen der Großmächte"), ("September 1914", "Marneschlacht, Beginn des Stellungskriegs"),
    ("1916", "Schlachten von Verdun und an der Somme"), ("April 1917", "Kriegseintritt der USA"), ("9. November 1918", "Ausrufung der Republik in Deutschland"),
    ("11. November 1918", "Waffenstillstand"), ("28. Juni 1919", "Versailler Vertrag")], G), G),
    "Erster Weltkrieg einfach erklärt: Zeitstrahl von Sarajevo 1914 bis Versailles 1919",
    "Der Erste Weltkrieg in acht Daten: Attentat von Sarajevo, Kriegserklärungen, Marneschlacht, Verdun, Kriegseintritt der USA, Republik, Waffenstillstand und Versailler Vertrag. Für Geschichte Klasse 8/9. #ErsterWeltkrieg #Geschichtsunterricht",
    "Erster Weltkrieg Zeitstrahl, Erster Weltkrieg einfach erklärt, Erster Weltkrieg Klasse 8, Versailler Vertrag, Geschichte Klasse 9")
add("wk1b", "erster-weltkrieg-einfach-erklaert", K.pin("Geschichte · Klasse 8/9", "Warum begann der Erste Weltkrieg?", "4 Ursachen", cards([
    ("Imperialismus", "Die Großmächte konkurrierten um Kolonien und Einfluss."), ("Bündnisse", "Europa war in zwei Lager geteilt."),
    ("Wettrüsten", "Besonders Deutschland und Großbritannien rüsteten ihre Flotten auf."), ("Nationalismus", "Viele hielten die eigene Nation für überlegen.")], G, ["I", "B", "W", "N"])
    + note("Auslöser: Attentat von Sarajevo, 28. Juni 1914"), G, light=True),
    "Ursachen des Ersten Weltkriegs: Imperialismus, Bündnisse, Wettrüsten, Nationalismus",
    "Vier Ursachen des Ersten Weltkriegs einfach erklärt: Imperialismus, Bündnisse, Wettrüsten und Nationalismus – Auslöser war das Attentat von Sarajevo. Mit Verlauf und Folgen im Artikel für Klasse 8/9. #ErsterWeltkrieg #Geschichtsunterricht",
    "Ursachen Erster Weltkrieg, Erster Weltkrieg Ursachen Klasse 8, Imperialismus Bündnisse, Attentat Sarajevo, Geschichte Arbeitsblatt")

# Industrialisierung
add("indu1", "industrialisierung-einfach-erklaert", K.pin("Geschichte · Klasse 8/9", "Industrialisierung", "Zeitstrahl in 6 Daten", cards([
    ("1769", "James Watt erhält das Patent für seine verbesserte Dampfmaschine."), ("1834", "Der Deutsche Zollverein schafft einen gemeinsamen Markt."),
    ("1835", "Erste deutsche Eisenbahn: Nürnberg – Fürth"), ("1839", "Preußen verbietet Fabrikarbeit für Kinder unter 9 Jahren."),
    ("1871", "Gründung des Deutschen Kaiserreichs"), ("1883–1889", "Bismarck führt die Sozialversicherungen ein.")], G), G),
    "Industrialisierung einfach erklärt: Zeitstrahl von der Dampfmaschine bis zur Sozialversicherung",
    "Die Industrialisierung in Deutschland in sechs Daten: Dampfmaschine, Zollverein, erste Eisenbahn, Verbot von Kinderarbeit, Reichsgründung und Sozialversicherungen. Für Geschichte Klasse 8/9. #Industrialisierung #Geschichtsunterricht",
    "Industrialisierung Zeitstrahl, Industrialisierung einfach erklärt, Industrialisierung Klasse 8, Dampfmaschine, soziale Frage, Geschichte Klasse 8")
add("indu2", "industrialisierung-einfach-erklaert", K.pin("Geschichte · Klasse 8/9", "Wer löste die soziale Frage?", "", cards([
    ("Arbeiter", "Gewerkschaften, Arbeitervereine, Parteien (Vorläufer der SPD)"), ("Kirchen", "Hilfsvereine, Kolpinghäuser, Hilfe für Kranke und Kinder"),
    ("Unternehmer", "Werkswohnungen, Schulen und Krankenkassen für die eigenen Arbeiter"), ("Staat", "Kinderarbeit eingeschränkt (1839), Sozialversicherungen (1883–1889)")], G, ["A", "K", "U", "S"])
    + note("Soziale Frage: Not der Arbeiterfamilien – lange Arbeitszeiten, niedrige Löhne, Kinderarbeit"), G, light=True),
    "Soziale Frage einfach erklärt: Lösungen von Arbeitern, Kirchen, Unternehmern und Staat",
    "Wer löste die soziale Frage der Industrialisierung? Arbeiter mit Gewerkschaften, Kirchen mit Hilfsvereinen, Unternehmer mit Werkswohnungen und der Staat mit Sozialversicherungen. Für Geschichte Klasse 8/9. #Industrialisierung #SozialeFrage",
    "soziale Frage, soziale Frage Lösungen, Industrialisierung soziale Frage, Bismarck Sozialversicherung, Geschichte Klasse 8 Arbeitsblatt")

# Wörtliche Rede
add("rede1", "woertliche-rede-zeichensetzung", K.pin("Deutsch · Klasse 4–6", "Wörtliche Rede richtig setzen", "3 Fälle + 1 Sonderfall", cards([
    ("Begleitsatz vorn", "Mia sagte: „Ich komme gleich.“"), ("Begleitsatz hinten", "„Ich komme gleich“, sagte Mia."),
    ("Begleitsatz in der Mitte", "„Ich komme gleich“, sagte Mia, „ich muss nur noch meine Jacke holen.“"), ("Frage oder Ausruf", "„Kommst du?“, fragte sie.")], D, ["1", "2", "3", "!"]), D),
    "Wörtliche Rede Zeichensetzung: Begleitsatz vorn, hinten und in der Mitte mit Beispielen",
    "Wörtliche Rede richtig setzen: Begleitsatz vorn mit Doppelpunkt, hinten mit Komma, in der Mitte zwischen zwei Kommas – und Frage- und Ausrufezeichen bleiben. Mit Beispielsätzen für Deutsch Klasse 4–6. #Zeichensetzung #Deutschunterricht",
    "wörtliche Rede, wörtliche Rede Zeichensetzung, Begleitsatz, wörtliche Rede Klasse 5, Anführungszeichen Regeln, Zeichensetzung Arbeitsblatt")
add("rede2", "woertliche-rede-zeichensetzung", K.pin("Deutsch · Klasse 4–6", "Komma oder Punkt?", "Die wörtliche Rede in 3 Regeln", cards([
    ("Vorn", "Nach dem Begleitsatz ein Doppelpunkt, die Rede beginnt groß."), ("Hinten", "Nach der Rede ein Komma, der Punkt der Rede entfällt, der Begleitsatz beginnt klein."),
    ("Mitte", "Begleitsatz zwischen zwei Kommas, der zweite Teil der Rede beginnt klein.")], D, [":", ",", ", ,"]), D, light=True),
    "Wörtliche Rede Regeln einfach erklärt: Doppelpunkt, Komma und Anführungszeichen",
    "Drei Regeln, die jede Klasse 5 kennen sollte: Begleitsatz vorn mit Doppelpunkt, hinten mit Komma ohne Punkt, in der Mitte zwischen zwei Kommas. Mit Beispielen und Übungen im Artikel. #Zeichensetzung #Rechtschreibung",
    "wörtliche Rede Regeln, Zeichensetzung wörtliche Rede, Begleitsatz Komma, Deutsch Klasse 5 Zeichensetzung, wörtliche Rede Übungen")

# Großschreibung
add("gross1", "grossschreibung-nominalisierung", K.pin("Deutsch · Klasse 5–7", "Nominalisierung erkennen", "5 Signalwörter", cards([
    ("Artikel", "das Laufen, ein Lachen"), ("Versteckter Artikel", "beim, zum, im, vom – zum Lachen, im Dunkeln"),
    ("Mengenwort", "etwas Gutes, nichts Neues, viel, wenig, alles"), ("Possessivpronomen", "dein Singen, sein Zögern"), ("Adjektiv davor", "lautes Lachen, schnelles Laufen")], D, ["1", "2", "3", "4", "5"]), D),
    "Nominalisierung Signalwörter: Großschreibung einfach erklärt mit Beispielen Klasse 5–7",
    "Wann schreibt man Verben und Adjektive groß? Fünf Signalwörter für die Nominalisierung: Artikel, versteckter Artikel, Mengenwörter, Possessivpronomen und Adjektive. Mit Fallen und Übungen im Artikel. #Rechtschreibung #Großschreibung",
    "Nominalisierung, Signalwörter Großschreibung, Großschreibung Verben, Nominalisierung Klasse 6, Rechtschreibung Arbeitsblatt, Großschreibung Regeln")
add("gross2", "grossschreibung-nominalisierung", K.pin("Deutsch · Klasse 5–7", "Groß oder klein?", "4 typische Fallen", cards([
    ("am besten, am schnellsten", "Steigerung mit „am“: klein. Wer läuft am schnellsten?"), ("Tageszeiten", "heute Abend groß – aber abends, montags klein"),
    ("Höflichkeitsform", "Sie, Ihnen, Ihr in der Anrede immer groß"), ("Satzanfang", "immer groß")], D, ["!", "!", "!", "!"]), D, light=True),
    "Groß oder klein? 4 Fallen bei der Großschreibung – am besten, heute Abend, Sie",
    "Die vier häufigsten Fallen bei der Groß- und Kleinschreibung: am besten, Tageszeiten, Höflichkeitsform und Satzanfang. Mit Signalwörtern und Übungen im Artikel für Klasse 5–7. #Rechtschreibung #Deutschunterricht",
    "Groß- und Kleinschreibung, am besten klein, heute Abend groß, Höflichkeitsform Sie, Rechtschreibung Fehler, Deutsch Klasse 6")

# s, ss, ß
add("sss1", "s-ss-oder-scharfes-s", K.pin("Deutsch · Klasse 5–7", "s, ss oder ß?", "3 Regeln", cards([
    ("ss", "nach einem kurzen Vokal: Fluss, Kuss"), ("ß", "nach langem Vokal oder ei, au, äu, eu – scharfer s-Laut: Fuß, Straße"), ("s", "weicher, summender s-Laut: Hose, Rasen")], D, ["ss", "ß", "s"]), D),
    "s, ss oder ß? Die 3 Regeln mit Beispielen – Rechtschreibung Klasse 5–7",
    "ss nach kurzem Vokal, ß nach langem Vokal oder Doppellaut, s beim weichen Laut: die drei Regeln mit Beispielen. Im Artikel mit Verlängerungs-Trick und Übungen. #Rechtschreibung #Deutschunterricht",
    "s ss ß Regeln, ss oder ß, scharfes s Regel, Rechtschreibung Klasse 5, s-Laute Arbeitsblatt, Deutsch Rechtschreibung")
add("sss2", "s-ss-oder-scharfes-s", K.pin("Deutsch · Klasse 5–7", "Der Verlängerungs-Trick", "Am Wortende klingt jedes s gleich", cards([
    ("Gras → Gräser", "weiches s → s"), ("Fuß → Füße", "scharfes s nach langem Vokal → ß"), ("Fluss → Flüsse", "kurzer Vokal → ss"), ("Haus → Häuser", "weiches s → s"), ("groß → größer", "scharfes s → ß")], D), D, light=True),
    "s, ss oder ß am Wortende? Der Verlängerungs-Trick mit Beispielen",
    "Am Wortende klingt jedes s gleich scharf – deshalb verlängern: Gras – Gräser, Fuß – Füße, Fluss – Flüsse. Der Trick mit Beispielen für Deutsch Klasse 5–7. #Rechtschreibung #Deutschunterricht",
    "Verlängerungsprobe, s ss ß Trick, Wörter verlängern, Rechtschreibstrategie, Rechtschreibung Klasse 5")

# Vorgangsbeschreibung
add("vorgang1", "vorgangsbeschreibung-schreiben", K.pin("Deutsch · Klasse 5–8", "Vorgangsbeschreibung", "Aufbau in 4 Teilen", cards([
    ("Überschrift", "Was wird beschrieben? z. B. „So topfst du eine Zimmerpflanze um“"), ("Einleitung", "Ziel, Dauer, Schwierigkeit und alles, was man braucht."),
    ("Hauptteil", "Arbeitsschritte in richtiger Reihenfolge, ein Schritt pro Satz."), ("Schluss", "Ergebnis, Tipp oder Hinweis auf Fehlerquellen.")], D, ["1", "2", "3", "4"])
    + chips(["Präsens", "sachlich", "Fachwörter", "eine Form durchhalten"]), D),
    "Vorgangsbeschreibung schreiben: Aufbau, Regeln und Beispiel für Deutsch Klasse 5–8",
    "Vorgangsbeschreibung in vier Teilen: Überschrift, Einleitung mit Material, Hauptteil Schritt für Schritt und Schluss. Im Präsens, sachlich und genau. Mit Beispiel im Artikel. #Vorgangsbeschreibung #Deutschunterricht",
    "Vorgangsbeschreibung, Vorgangsbeschreibung Aufbau, Vorgangsbeschreibung Klasse 6, Vorgangsbeschreibung Beispiel, Beschreiben Deutsch")
add("vorgang2", "vorgangsbeschreibung-schreiben", K.pin("Deutsch · Klasse 5–8", "Reihenfolgewörter", "für jede Vorgangsbeschreibung", chips(["zuerst", "zunächst", "danach", "anschließend", "sobald", "währenddessen", "nun", "zum Schluss"])
    + cards([("Präsens", ""), ("Sachlich und genau", "mit Fachwörtern"), ("Eine Form wählen", "man-Form, Passiv oder Aufforderung – und dabei bleiben")], D, ["✓", "✓", "✓"]), D, light=True),
    "Reihenfolgewörter für die Vorgangsbeschreibung: zuerst, danach, anschließend, zum Schluss",
    "Acht Reihenfolgewörter für die Vorgangsbeschreibung und drei Regeln: Präsens, sachlich bleiben und eine Form durchhalten. Zum Aufhängen im Klassenzimmer, Deutsch Klasse 5–8. #Vorgangsbeschreibung #Deutschunterricht",
    "Reihenfolgewörter, Vorgangsbeschreibung Wörter, Satzanfänge Vorgangsbeschreibung, Deutsch Klasse 5, Schreiben Klasse 6")

# Formeller Brief
add("brief1", "formellen-brief-schreiben", K.pin("Deutsch · Klasse 7–10", "Formeller Brief", "Aufbau in 8 Teilen", cards([
    ("Absender", "oben links"), ("Empfänger", "Name oder Firma und Adresse"), ("Ort und Datum", "rechtsbündig"), ("Betreff", "kurz, ohne Punkt"),
    ("Anrede", "Sehr geehrte Frau …,"), ("Brieftext", "Anlass, Anliegen, Bitte"), ("Grußformel", "Mit freundlichen Grüßen – ohne Komma"), ("Unterschrift", "handschriftlich")], D,
    ["1", "2", "3", "4", "5", "6", "7", "8"]), D),
    "Formellen Brief schreiben: Aufbau in 8 Teilen mit Anrede und Grußformel – Klasse 7–10",
    "Absender, Empfänger, Ort und Datum, Betreff, Anrede, Brieftext, Grußformel und Unterschrift: der formelle Brief Schritt für Schritt. Im Artikel mit Beispiel und Tipps für die E-Mail. #FormellerBrief #Deutschunterricht",
    "formeller Brief, formeller Brief Aufbau, Brief schreiben Klasse 8, Geschäftsbrief Schule, Anrede Grußformel, Bewerbung Deutsch")
add("brief2", "formellen-brief-schreiben", K.pin("Deutsch · Klasse 7–10", "6 Fehler im formellen Brief", "und in der E-Mail", cards([
    ("„Hallo“ oder „Hey“ als Anrede", ""), ("Komma nach der Grußformel", ""), ("Nach der Anrede groß weiterschreiben", "Richtig: klein weiter."),
    ("„du“ und „Sie“ mischen", ""), ("Leerer Betreff", "Besser: „Anfrage Praktikum Klasse 9“"), ("Anliegen kommt zu spät", "")], D, ["✗"] * 6), D, light=True),
    "Formeller Brief und E-Mail: 6 typische Fehler, die Schüler machen",
    "Hallo als Anrede, Komma nach dem Gruß, groß weiterschreiben, du und Sie mischen, leerer Betreff: sechs typische Fehler im formellen Brief und in der E-Mail – mit Regeln im Artikel. Für Klasse 7–10. #FormellerBrief #Bewerbung",
    "formeller Brief Fehler, E-Mail schreiben Schule, Anrede Komma, E-Mail an Lehrer, Bewerbung Praktikum E-Mail, Deutsch Klasse 9")

# Bericht
add("bericht1", "bericht-schreiben", K.pin("Deutsch · Klasse 6–8", "Bericht schreiben", "Die 7 W-Fragen", chips(["Was ist passiert?", "Wer war beteiligt?", "Wann?", "Wo?", "Wie lief es ab?", "Warum?", "Welche Folgen?"])
    + cards([("Einleitung", "Die wichtigsten W-Fragen auf einen Blick"), ("Hauptteil", "Ablauf in zeitlicher Reihenfolge"), ("Schluss", "Folgen, Ergebnis oder Ausblick")], D, ["1", "2", "3"]), D),
    "Bericht schreiben: W-Fragen und Aufbau einfach erklärt für Deutsch Klasse 6–8",
    "Was, wer, wann, wo, wie, warum, welche Folgen: die sieben W-Fragen für den Bericht und der Aufbau mit Einleitung, Hauptteil und Schluss. Im Artikel mit Beispiel. #Bericht #Deutschunterricht",
    "Bericht schreiben, W-Fragen Bericht, Bericht Aufbau, Bericht Klasse 7, Unfallbericht Schule, Zeitungsbericht")
add("bericht2", "bericht-schreiben", K.pin("Deutsch · Klasse 6–8", "Bericht: 5 Regeln", "", cards([
    ("Präteritum", "Vorzeitiges im Plusquamperfekt"), ("Sachlich", "Keine Gefühle, Übertreibungen oder Wertungen"), ("Indirekte Rede", "Keine wörtliche Rede"),
    ("Nur Fakten", "Keine Gerüchte"), ("Zeitungsbericht", "Schlagzeile, Vorspann, dritte Person")], D, ["✓", "✓", "✓", "✓", "+"]), D, light=True),
    "Bericht schreiben Regeln: Zeitform Präteritum, sachlich, keine wörtliche Rede",
    "Fünf Regeln für den Bericht: Präteritum, sachliche Sprache, indirekte Rede, nur gesicherte Fakten – und beim Zeitungsbericht Schlagzeile und Vorspann. Für Deutsch Klasse 6–8. #Bericht #Deutschunterricht",
    "Bericht Zeitform, Bericht Regeln, Bericht Präteritum, Bericht schreiben Klasse 6, Deutsch Spickzettel")

# Zusammenfassung
add("zusamm1", "zusammenfassung-schreiben", K.pin("Deutsch · Klasse 7–10", "Die KURZ-Methode", "Zusammenfassung in 4 Schritten", cards([
    ("Kern finden", "Text zweimal lesen, Thema in einem Satz."), ("Unwichtiges streichen", "Nur Schlüsselwörter markieren."),
    ("Reihenfolge ordnen", "Randnotizen je Abschnitt, logisch ordnen."), ("Zusammen schreiben", "Im Präsens, in eigenen Worten, mit Verbindungswörtern.")], D, ["K", "U", "R", "Z"]), D),
    "Zusammenfassung schreiben mit der KURZ-Methode: in 4 Schritten zum Sachtext – Klasse 7–10",
    "K wie Kern finden, U wie Unwichtiges streichen, R wie Reihenfolge ordnen, Z wie zusammen schreiben: die KURZ-Methode für die Zusammenfassung von Sachtexten. Mit Einleitungssatz und Beispiel im Artikel. #Zusammenfassung #Deutschunterricht",
    "Zusammenfassung schreiben, Sachtext zusammenfassen, Zusammenfassung Klasse 8, Einleitungssatz, Textzusammenfassung Methode, Deutsch Prüfung")
add("zusamm2", "zusammenfassung-schreiben", K.pin("Deutsch · Klasse 7–10", "Zusammenfassung: 6 Regeln", "", cards([
    ("Präsens", "auch wenn das Original in der Vergangenheit steht"), ("Eigene Worte", "statt Abschreiben"), ("Nur das Wichtigste", "in logischer Reihenfolge"),
    ("Sachlich", "ohne eigene Meinung"), ("Indirekte Rede", "keine wörtlichen Zitate"), ("Etwa ein Drittel", "der Länge des Originals")], D, ["✓"] * 6), D, light=True),
    "Zusammenfassung Regeln: Präsens, eigene Worte, ein Drittel der Länge – Spickzettel",
    "Sechs Regeln für eine gute Zusammenfassung: Präsens, eigene Worte, nur das Wichtigste, sachlich, indirekte Rede und etwa ein Drittel der Originallänge. Für Deutsch Klasse 7–10. #Zusammenfassung #Spickzettel",
    "Zusammenfassung Regeln, Zusammenfassung Zeitform, Zusammenfassung Länge, Sachtext Deutsch, Deutsch Klasse 9")

# Charakterisierung
add("charakt1", "charakterisierung-schreiben", K.pin("Deutsch · Klasse 7–10", "Charakterisierung", "8 Formulierungen, die immer passen", chips([
    "… wirkt …", "Auffällig ist, dass …", "Das wird deutlich, als …", "Daran erkennt man, dass …", "Das lässt darauf schließen, dass …", "Im Verlauf verändert sich …", "Ich finde …, weil …"])
    + note("Dreischritt: Eigenschaft nennen – belegen – erklären"), D),
    "Charakterisierung schreiben: Formulierungen und Satzanfänge für Deutsch Klasse 7–10",
    "Satzanfänge für die Charakterisierung: wirkt, auffällig ist, das wird deutlich, daran erkennt man, das lässt darauf schließen. Mit Dreischritt, Aufbau und Beispiel im Artikel. #Charakterisierung #Deutschunterricht",
    "Charakterisierung Formulierungen, Charakterisierung Satzanfänge, Charakterisierung schreiben, Figurencharakterisierung, Deutsch Klasse 8")
add("charakt2", "charakterisierung-schreiben", K.pin("Deutsch · Klasse 7–10", "Was gehört in eine Charakterisierung?", "7 Bereiche", grid([
    ("Äußeres", "Alter, Aussehen, Kleidung"), ("Lebensumstände", "Familie, Wohnort, Schule, Beruf"), ("Verhalten", "Handlungen, Reaktionen"), ("Gefühle & Gedanken", "Sorgen, Ängste, Wünsche"),
    ("Sprache", "Art des Sprechens"), ("Beziehungen", "zu anderen Figuren"), ("Entwicklung", "Veränderung im Verlauf"), ("Belege", "mit Zeilen- oder Kapitelangabe")], D), D, light=True),
    "Charakterisierung Aufbau: 7 Bereiche, die Schüler untersuchen sollten",
    "Äußeres, Lebensumstände, Verhalten, Gefühle, Sprache, Beziehungen und Entwicklung: sieben Bereiche für eine vollständige Charakterisierung – immer mit Textbeleg. Für Deutsch Klasse 7–10. #Charakterisierung #Lektüre",
    "Charakterisierung Aufbau, Charakterisierung Bereiche, Figur charakterisieren, Lektüre Figur, Deutsch Klasse 9")

# Tagebucheintrag
add("tagebuch1", "tagebucheintrag-schreiben", K.pin("Deutsch · Klasse 5–10", "Tagebucheintrag zur Lektüre", "Checkliste", cards([
    ("Datum und Ich-Form?", ""), ("Ereignis knapp, Gefühle ausführlich?", "Faustregel: ⅓ Ereignis, ⅔ Gefühle"), ("Zeitformen richtig?", "Rückblick Präteritum/Perfekt, Gefühle Präsens"),
    ("Weiß die Figur das schon?", ""), ("Klingt es nach der Figur?", ""), ("Gibt es einen Ausblick?", "")], D, ["✓"] * 6) + note("Richtwert Prüfung: 200–300 Wörter"), D),
    "Tagebucheintrag schreiben: Checkliste für die Lektüre und die Abschlussprüfung",
    "Sechs Fragen zum Abhaken: Datum und Ich-Form, ein Drittel Ereignis und zwei Drittel Gefühle, richtige Zeitformen, Wissen der Figur, passende Sprache und Ausblick. Mit Beispiel im Artikel. #Tagebucheintrag #Lektüre #Prüfung",
    "Tagebucheintrag schreiben, Tagebucheintrag Lektüre, Tagebucheintrag Checkliste, produktive Schreibaufgabe, Abschlussprüfung Deutsch")
add("tagebuch2", "tagebucheintrag-schreiben", K.pin("Deutsch · Klasse 5–10", "Tagebucheintrag: Aufbau", "in 4 Teilen", cards([
    ("Einstieg", "Datum, Anrede, Grund zum Schreiben"), ("Was passiert ist", "knapp, aus Sicht der Figur – nicht nacherzählen"), ("Gefühle und Gedanken", "der Kern des Eintrags"), ("Ausblick", "Pläne, Hoffnungen oder Ängste")], D, ["1", "2", "3", "4"]), D, light=True),
    "Tagebucheintrag Aufbau: Einstieg, Ereignis, Gefühle, Ausblick – Deutsch Klasse 5–10",
    "So ist ein Tagebucheintrag aufgebaut: Einstieg mit Datum, kurzer Blick aufs Ereignis, ausführlich Gefühle und Gedanken, dann ein Ausblick. Mit Checkliste und Fehlern im Artikel. #Tagebucheintrag #Deutschunterricht",
    "Tagebucheintrag Aufbau, Tagebucheintrag Beispiel, Tagebucheintrag Klasse 6, Tagebuch schreiben Schule, kreatives Schreiben")

# Innerer Monolog
add("monolog1", "innerer-monolog-schreiben", K.pin("Deutsch · Klasse 7–10", "Innerer Monolog oder Tagebuch?", "Die Unterschiede", two(
    ("Innerer Monolog", D, [("Zeitpunkt", "mitten in der Situation"), ("Zeitform", "Präsens"), ("Form", "keine Anrede, kein Datum"), ("Sprache", "sprunghaft, Fragen, Abbrüche")]),
    ("Tagebucheintrag", "#12324F", [("Zeitpunkt", "danach, mit Abstand"), ("Zeitform", "meist Präteritum oder Perfekt"), ("Form", "mit Anrede und Datum"), ("Sprache", "geordneter, wertender")])), D),
    "Innerer Monolog oder Tagebucheintrag? Die Unterschiede auf einen Blick",
    "Innerer Monolog und Tagebucheintrag im Vergleich: Zeitpunkt, Zeitform, Form und Sprache. Perfekt zur Vorbereitung auf die produktive Schreibaufgabe zur Lektüre, Klasse 7–10. #InnererMonolog #Lektüre #Prüfung",
    "innerer Monolog, innerer Monolog Merkmale, innerer Monolog Tagebuch Unterschied, produktive Schreibaufgabe, Deutsch Klasse 9")
add("monolog2", "innerer-monolog-schreiben", K.pin("Deutsch · Klasse 7–10", "Inneren Monolog schreiben", "in 5 Schritten", cards([
    ("Moment festlegen", "Welche Stelle in der Geschichte?"), ("Wissen prüfen", "Was weiß die Figur hier – und was nicht?"), ("Drei Gefühle sammeln", "auch widersprüchliche"),
    ("Gedankenlauf planen", "Auslöser, Erinnerungen, Grübeleien, Entschluss"), ("Schreiben und prüfen", "Präsens, Ich-Form, passt es zum Buch?")], D, ["1", "2", "3", "4", "5"]), D, light=True),
    "Inneren Monolog schreiben in 5 Schritten – mit Merkmalen für Klasse 7–10",
    "Moment festlegen, Wissen der Figur prüfen, Gefühle sammeln, Gedankenlauf planen und schreiben: der innere Monolog in fünf Schritten. Im Artikel mit Merkmalen und Beispiel. #InnererMonolog #Deutschunterricht",
    "inneren Monolog schreiben, innerer Monolog Aufbau, innerer Monolog Beispiel, Lektüre Schreibaufgabe, Deutsch Klasse 8")

# Klassenlehrerstunde
add("klst1", "klassenlehrerstunde-ideen", K.pin("Klassenlehrerstunde · Klasse 5–10", "Ideen fürs ganze Schuljahr", "", cards([
    ("Schuljahresbeginn", "Steckbrief-Bingo, Klassenregeln, Brief an sich selbst"), ("Herbst", "Klassenrat einführen, Elternsprechtag vorbereiten"),
    ("Winter", "Neue Ziele mit SMART-Regel, Halbjahres-Check"), ("Frühling", "Lernen lernen, Klassenchat-Regeln, Konflikte lösen"), ("Sommer", "Briefe öffnen, Komplimente-Dusche")], KL, ["🍂", "🍁", "❄", "🌱", "☀"]), KL),
    "Klassenlehrerstunde Ideen für das ganze Schuljahr – Klasse 5 bis 10",
    "Was mache ich in der Klassenlehrerstunde? Ideen für jede Jahreszeit: Steckbrief-Bingo, Klassenrat, SMART-Ziele, Halbjahres-Check, Klassenchat-Regeln und Komplimente-Dusche. Für Klasse 5–10. #Klassenlehrer #Unterrichtsideen",
    "Klassenlehrerstunde Ideen, Klassenlehrerstunde Klasse 5, Klassenrat, Klassenlehrer Material, Klassengemeinschaft stärken, Unterrichtsideen")
add("klst2", "klassenlehrerstunde-ideen", K.pin("Klassenlehrerstunde · ohne Vorbereitung", "Spontan Vertretung?", "3 Ideen, die immer gehen", cards([
    ("Steckbrief-Bingo", "Alle suchen Mitschüler, auf die eine Aussage passt."), ("Komplimente-Dusche", "Alle schreiben etwas Positives über jemanden auf."), ("Ziele-Vertrag", "Jede und jeder setzt sich ein Ziel bis zu den nächsten Ferien.")], KL, ["1", "2", "3"]), KL, light=True),
    "Vertretungsstunde ohne Vorbereitung: 3 Ideen für die Klassenlehrerstunde",
    "Spontan eine Vertretungsstunde? Drei Ideen ohne Vorbereitung: Steckbrief-Bingo, Komplimente-Dusche und Ziele-Vertrag. Mehr Ideen fürs ganze Schuljahr im Artikel. #Vertretungsstunde #Klassenlehrer",
    "Vertretungsstunde Ideen, Vertretungsstunde ohne Vorbereitung, Klassenlehrerstunde spontan, Komplimente-Dusche, Unterrichtsideen")

# Stellungnahme
add("stell1", "stellungnahme-schreiben-hauptschulabschluss", K.pin("Hauptschulabschluss Deutsch · Klasse 9", "Stellungnahme schreiben", "Aufbau · 18 von 80 Punkten", cards([
    ("Einleitung", "Anlass und Meinung in 2–4 Sätzen"), ("Hauptteil", "2–3 Argumente mit Begründung und Beispiel, das stärkste zuletzt"),
    ("Gegenargument", "nennen und entkräften"), ("Schluss", "Meinung bekräftigen, Vorschlag oder Bitte")], D, ["1", "2", "3", "4"]) + note("Briefform: Betreff, Anrede, Grußformel, Name"), D),
    "Stellungnahme schreiben Hauptschulabschluss: Aufbau und Briefform – 18 Punkte sichern",
    "Die Stellungnahme im Hauptschulabschluss Deutsch bringt 18 von 80 Punkten. So ist sie aufgebaut: Einleitung, Argumente, Gegenargument und Schluss – in Briefform. Mit Satzbausteinen im Artikel. #Hauptschulabschluss #Stellungnahme",
    "Stellungnahme schreiben, Stellungnahme Hauptschulabschluss, Stellungnahme Aufbau, Stellungnahme Klasse 9, Briefform Deutsch")
add("stell2", "stellungnahme-schreiben-hauptschulabschluss", K.pin("Stellungnahme · Satzbausteine", "So klingt eine gute Stellungnahme", "", chips([
    "Ich bin der Meinung, dass …", "Zuerst einmal …", "Außerdem …", "…, denn …", "…, weil …", "Zum Beispiel …", "Natürlich stimmt es, dass …", "Ich bitte Sie daher …"]), D, light=True),
    "Satzbausteine für die Stellungnahme: Meinung, Argumente, Gegenargument und Schluss",
    "Satzbausteine für die Stellungnahme zum Ausdrucken: Meinung sagen, Argumente ordnen, begründen, Beispiele geben, Gegenargument entkräften und Schluss. Für den Hauptschulabschluss und Klasse 7–9. #Stellungnahme #Deutschunterricht",
    "Satzbausteine Stellungnahme, Formulierungen Argumentation, Stellungnahme Formulierungen, Argumentieren Klasse 8, Hauptschulabschluss Deutsch")

# Prüfungslektüren
add("lekt27", "pruefungslektueren-bw-2027-2028", K.pin("Abschlussprüfung Deutsch BW", "Prüfungslektüren 2027", "Prüfung am 27. April 2027", cards([
    ("Weggesperrt", "Grit Poppe"), ("Windstärke 17", "Caroline Wahl")], D, ["RSA", "RSA"]) + cards([("Der Tunnelbauer", "Maja Nielsen"), ("Über kurz oder lang", "Marie-Aude Murail")], "#12324F", ["HSA", "HSA"]), D),
    "Prüfungslektüren BW 2027: alle Lektüren für Realschulabschluss und Hauptschulabschluss",
    "Pflichtlektüren für die Abschlussprüfung Deutsch 2027 in Baden-Württemberg: RSA „Weggesperrt“ und „Windstärke 17“, HSA „Der Tunnelbauer“ und „Über kurz oder lang“. Prüfung am 27. April 2027. #Prüfungslektüre #Abschlussprüfung",
    "Prüfungslektüre 2027 BW, Pflichtlektüre Realschulabschluss 2027, Pflichtlektüre Hauptschulabschluss 2027, Weggesperrt, Windstärke 17, Der Tunnelbauer")
add("lekt28", "pruefungslektueren-bw-2027-2028", K.pin("Abschlussprüfung Deutsch BW", "Prüfungslektüren 2028", "Prüfung am 3. Mai 2028", cards([
    ("Paradise Garden", "Elena Fischer"), ("Das Feuer vergessen wir nicht", "Sarah Jäger")], D, ["RSA", "RSA"]) + cards([("Schallplattensommer", "Alina Bronsky"), ("Eine Weile bleibt die Zeit für uns stehen", "Jacqueline Woodson")], "#12324F", ["HSA", "HSA"]), D, light=True),
    "Prüfungslektüren BW 2028: Paradise Garden, Schallplattensommer und mehr – RSA und HSA",
    "Die neuen Pflichtlektüren für 2028 in Baden-Württemberg: RSA „Paradise Garden“ und „Das Feuer vergessen wir nicht“, HSA „Schallplattensommer“ und „Eine Weile bleibt die Zeit für uns stehen“. Prüfung am 3. Mai 2028. #Prüfungslektüre #Deutschunterricht",
    "Prüfungslektüre 2028 BW, Pflichtlektüre 2028, Paradise Garden Unterricht, Schallplattensommer Unterricht, Realschulabschluss 2028")


def lek(slug, url, prue, titel, autor, ort, figuren, themen, title, desc, kw, light=False):
    add(slug, url, K.pin(prue, titel, autor, cards([("Schauplatz", ort)] + figuren, D, ["⌂"] + ["•"] * len(figuren)) + K.blk_chips(themen, "Themen"), D, light=light), title, desc, kw)


lek("windst", "windstaerke-17-unterrichtsmaterial-rsa-2027", "Realschulabschluss 2027 · BW", "Windstärke 17", "Caroline Wahl", "vor allem die Insel Rügen",
    [("Ida", "21, Ich-Erzählerin, flieht nach dem Tod der Mutter ans Meer"), ("Knut und Marianne", "Wirt der Kneipe „Robbe“ und seine Frau, die Ida aufnimmt"), ("Leif", "junger Mann, der Ida nicht loslässt")],
    ["Trauer und Schuld", "Sucht in der Familie", "Wahrheit und Lüge", "Ersatzfamilie", "Meer, Sturm, Regen"],
    "Windstärke 17 im Unterricht: Figuren, Themen und Prüfung RSA 2027 BW",
    "„Windstärke 17“ von Caroline Wahl – Prüfungslektüre Realschulabschluss 2027 in Baden-Württemberg: Schauplatz Rügen, Ida, Knut, Marianne und Leif, Themen wie Trauer, Sucht und Ersatzfamilie. Mit Prüfungsinfos im Artikel. #Windstärke17 #Prüfungslektüre",
    "Windstärke 17 Unterricht, Windstärke 17 Figuren, Windstärke 17 Themen, Caroline Wahl, Prüfungslektüre 2027, Realschulabschluss Deutsch")
lek("weggesp", "weggesperrt-unterrichtsmaterial-rsa-2027", "Realschulabschluss 2027 · BW", "Weggesperrt", "Grit Poppe", "DDR, Herbst 1988 bis 1989",
    [("Anja", "14, gerät ohne eigenes Vergehen ins System"), ("Anjas Mutter", "protestiert und stellt einen Ausreiseantrag"), ("Frau Falkner", "Lehrerin, die Anja leise warnt")],
    ["Macht und Ohnmacht", "Jugendwerkhof", "Widerstand und Anpassung", "Panther, Maske, Strom", "Torgau 1964–1989"],
    "Weggesperrt im Unterricht: Figuren, Themen und Prüfung RSA 2027 BW",
    "„Weggesperrt“ von Grit Poppe – Prüfungslektüre Realschulabschluss 2027 in Baden-Württemberg: DDR 1988/89, Anja und der Jugendwerkhof, Themen Macht, Widerstand und Anpassung. Mit Prüfungsinfos im Artikel. #Weggesperrt #Prüfungslektüre",
    "Weggesperrt Unterricht, Weggesperrt Grit Poppe, Weggesperrt Figuren, Jugendwerkhof Torgau, Prüfungslektüre 2027, Realschulabschluss Deutsch", light=True)
lek("tunnel", "der-tunnelbauer-unterrichtsmaterial-hsa-2027", "Hauptschulabschluss 2027 · BW", "Der Tunnelbauer", "Maja Nielsen", "Berlin, ab 1961",
    [("Achim Neumann", "junger Ost-Berliner, flieht in den Westen"), ("Chris", "bleibt im Osten"), ("Die Tunnelgruppe", "gräbt im Westen einen Fluchttunnel")],
    ["Mauerbau und Teilung", "Mut und Angst", "Vertrauen und Verrat", "Freundschaft und Liebe", "Roman und Wirklichkeit"],
    "Der Tunnelbauer im Unterricht: Figuren, Themen und Prüfung HSA 2027 BW",
    "„Der Tunnelbauer“ von Maja Nielsen – Prüfungslektüre Hauptschulabschluss 2027 in Baden-Württemberg: Berlin nach dem Mauerbau, Achim, Chris und die Tunnelgruppe, Themen Mut, Vertrauen und Verrat. #DerTunnelbauer #Prüfungslektüre",
    "Der Tunnelbauer Unterricht, Der Tunnelbauer Maja Nielsen, Tunnelbauer Figuren, Mauerbau Lektüre, Prüfungslektüre HSA 2027, Hauptschulabschluss Deutsch")
lek("kurzlang", "ueber-kurz-oder-lang-unterrichtsmaterial-hsa-2027", "Hauptschulabschluss 2027 · BW", "Über kurz oder lang", "Marie-Aude Murail", "Frankreich, ein Friseursalon",
    [("Louis", "macht ein Praktikum im Salon und blüht auf"), ("Madame Marielou", "Salonchefin mit schwerer Vergangenheit"), ("Louis' Vater", "wünscht sich einen anderen Beruf")],
    ["Berufsorientierung", "Rollenbilder", "Vater und Sohn", "Gewalt in Beziehungen", "Würde und Mut"],
    "Über kurz oder lang im Unterricht: Figuren, Themen und Prüfung HSA 2027 BW",
    "„Über kurz oder lang“ von Marie-Aude Murail – Prüfungslektüre Hauptschulabschluss 2027 in Baden-Württemberg: Louis im Friseursalon, Berufsorientierung, Rollenbilder und Vater-Sohn-Konflikt. #ÜberKurzOderLang #Prüfungslektüre",
    "Über kurz oder lang Unterricht, Marie-Aude Murail, Über kurz oder lang Figuren, Prüfungslektüre HSA 2027, Hauptschulabschluss Deutsch", light=True)
lek("paradise", "paradise-garden-unterrichtsmaterial-rsa-2028", "Realschulabschluss 2028 · BW", "Paradise Garden", "Elena Fischer", "ein gelbes Hochhaus am Stadtrand, 17. Stock",
    [("Billie", "Ich-Erzählerin, will Schriftstellerin werden, sucht ihren Vater"), ("Billies Mutter", "alleinerziehend, arbeitet in zwei Jobs"), ("Luna und Ahmed", "Nachbarn, die Billie Halt geben")],
    ["Trauer und Verlust", "Armut und Fantasie", "Familie und Herkunft", "Nachbarschaft"],
    "Paradise Garden im Unterricht: Figuren, Themen und Prüfung RSA 2028 BW",
    "„Paradise Garden“ von Elena Fischer – neue Prüfungslektüre Realschulabschluss 2028 in Baden-Württemberg: Billie, ihre Mutter und das Hochhaus, Themen Trauer, Armut und Herkunft. Prüfung am 3. Mai 2028. #ParadiseGarden #Prüfungslektüre",
    "Paradise Garden Unterricht, Paradise Garden Elena Fischer, Paradise Garden Figuren, Prüfungslektüre 2028, Realschulabschluss 2028")
lek("feuer", "das-feuer-vergessen-wir-nicht-unterrichtsmaterial-rsa-2028", "Realschulabschluss 2028 · BW", "Das Feuer vergessen wir nicht", "Sarah Jäger", "ein Pflegeheim und Aris Mehrfamilienhaus",
    [("Ari", "17, liest alten Menschen im Pflegeheim vor"), ("Flint", "lernt Ari im Pflegeheim kennen, wirkt einsam")],
    ["Zukunft", "Alter und Pflege", "Streik 1888", "Erste Liebe", "Familie"],
    "Das Feuer vergessen wir nicht im Unterricht: Figuren, Themen, Prüfung RSA 2028 BW",
    "„Das Feuer vergessen wir nicht“ von Sarah Jäger – neue Prüfungslektüre Realschulabschluss 2028 in Baden-Württemberg: Ari und Flint im Pflegeheim, der Streik der Streichholzarbeiterinnen 1888, Zukunft und erste Liebe. #Prüfungslektüre #Deutschunterricht",
    "Das Feuer vergessen wir nicht Unterricht, Sarah Jäger, Prüfungslektüre 2028, Realschulabschluss 2028 Lektüre", light=True)
lek("schallpl", "schallplattensommer-unterrichtsmaterial-hsa-2028", "Hauptschulabschluss 2028 · BW", "Schallplattensommer", "Alina Bronsky", "ein kleines Dorf mit Feriengästen",
    [("Maserati", "17, misstrauisch, voller Geheimnisse"), ("Oma", "versorgt die Feriengäste mit Limonade"), ("Caspar und Theo", "Brüder aus der reichen Familie")],
    ["Geheimnisse", "Familie und Herkunft", "Young Carers", "Dorfleben", "Schallplatte, See, Boot"],
    "Schallplattensommer im Unterricht: Figuren, Themen und Prüfung HSA 2028 BW",
    "„Schallplattensommer“ von Alina Bronsky – neue Prüfungslektüre Hauptschulabschluss 2028 in Baden-Württemberg: Maserati, Oma, Caspar und Theo, Themen Geheimnisse, Herkunft und Verantwortung. Prüfung am 3. Mai 2028. #Schallplattensommer #Prüfungslektüre",
    "Schallplattensommer Unterricht, Alina Bronsky, Schallplattensommer Figuren, Prüfungslektüre HSA 2028, Hauptschulabschluss 2028")
lek("weile", "eine-weile-bleibt-die-zeit-fuer-uns-stehen-unterrichtsmaterial-hsa-2028", "Hauptschulabschluss 2028 · BW", "Eine Weile bleibt die Zeit für uns stehen", "Jacqueline Woodson", "New York, Manhattan und Brooklyn",
    [("Ellie", "Schülerin aus Manhattan, erzählt in der Ich-Form"), ("Jeremiah", "Schüler aus Brooklyn, Ellies große Liebe")],
    ["Erste Liebe", "Vorurteile und Rassismus", "Familie", "Verlust und Trauer"],
    "Eine Weile bleibt die Zeit für uns stehen: Figuren, Themen und Prüfung HSA 2028 BW",
    "„Eine Weile bleibt die Zeit für uns stehen“ von Jacqueline Woodson – neue Prüfungslektüre Hauptschulabschluss 2028 in Baden-Württemberg: Ellie und Jeremiah in New York, erste Liebe, Vorurteile und Verlust. #Prüfungslektüre #Deutschunterricht",
    "Eine Weile bleibt die Zeit für uns stehen Unterricht, Jacqueline Woodson, Prüfungslektüre HSA 2028, Hauptschulabschluss 2028 Lektüre", light=True)

# Extremismus
add("extrem1", "extremismus-im-unterricht-klasse-9-10", K.pin("Gemeinschaftskunde · Klasse 9/10", "Extremismus im Klassenzimmer", "4 Situationen – so reagierst du", cards([
    ("„Das wird man ja wohl noch sagen dürfen!“", "Die Aussage benennen, nicht die Person. Nachfragen, Grenze klar machen."),
    ("„Sie sind doch auch nicht neutral!“", "Neutral heißt fair darstellen – nicht neutral bei Angriffen auf die Menschenwürde."),
    ("Symbole oder Zahlencodes", "Sachlich dokumentieren, Schulleitung informieren, Gespräch unter vier Augen."),
    ("Propagandavideo im Klassenchat", "Nicht weiterleiten, Schulleitung informieren, bei Straftaten Polizei.")], GK, ["1", "2", "3", "4"]), GK),
    "Extremismus im Unterricht: 4 schwierige Situationen und wie Lehrkräfte reagieren",
    "Was tun, wenn im Unterricht „Das wird man ja wohl noch sagen dürfen“ fällt, Symbole auftauchen oder ein Propagandavideo im Klassenchat kreist? Vier Situationen mit Handlungsempfehlung – mehr und Anlaufstellen in BW im Artikel. #Demokratiebildung #Gemeinschaftskunde",
    "Extremismus Schule, Extremismus Unterricht, Rechtsextremismus Schule Lehrer, Demokratiebildung, Gemeinschaftskunde Klasse 10, Prävention Extremismus")
add("extrem2", "extremismus-im-unterricht-klasse-9-10", K.pin("Baden-Württemberg · für Lehrkräfte", "Hilfe bei Extremismus an der Schule", "Anlaufstellen", cards([
    ("Demokratiezentrum Baden-Württemberg", "Workshops, Fortbildungen, Vermittlung"), ("Mobile Beratung gegen Rechtsextremismus", "bei konkreten Vorfällen"),
    ("FEX – Fachstelle Extremismusdistanzierung", "für Jugendliche, die abgleiten"), ("PREvent!on", "religiös begründeter Extremismus"),
    ("Vor Ort", "Beratungslehrkraft, Schulsozialarbeit, Schulpsychologie – bei Gefahr die Polizei")], GK, ["→"] * 5), GK, light=True),
    "Extremismus an der Schule: Anlaufstellen und Hilfe für Lehrkräfte in Baden-Württemberg",
    "Wer hilft Lehrkräften bei extremistischen Vorfällen? Demokratiezentrum BW, Mobile Beratung, FEX, PREvent!on und Ansprechpartner an der eigenen Schule. Mit acht Situationen und einer Unterrichtsreihe im Artikel. #Demokratiebildung #Schule",
    "Extremismus Beratung Schule, Demokratiezentrum Baden-Württemberg, Mobile Beratung Rechtsextremismus, Extremismusprävention Schule, Lehrkräfte Hilfe")

# Französische Revolution
add("fr1", "franzoesische-revolution-unterricht-klasse-8", K.pin("Geschichte · Klasse 8", "Revolutionszeitalter", "Zeitstrahl 1776–1871", cards([
    ("1776", "Unabhängigkeitserklärung der USA"), ("1789", "Sturm auf die Bastille, Menschen- und Bürgerrechte"), ("1791", "Olympe de Gouges: Rechte der Frau und Bürgerin"),
    ("1804", "Code civil"), ("1832", "Hambacher Fest"), ("1848/49", "Paulskirche, Grundrechte, Scheitern"), ("1871", "Reichsgründung durch Bismarck")], G), G),
    "Französische Revolution bis Reichsgründung: Zeitstrahl 1776–1871 für Geschichte Klasse 8",
    "Vom Unabhängigkeitskrieg der USA über die Französische Revolution, Napoleon, Hambacher Fest und Paulskirche bis zur Reichsgründung 1871: der rote Faden für Geschichte Klasse 8. #FranzösischeRevolution #Geschichtsunterricht",
    "Französische Revolution Zeitstrahl, Revolutionszeitalter, Französische Revolution Klasse 8, Paulskirche 1848, Reichsgründung 1871, Geschichte Klasse 8")
add("fr2", "franzoesische-revolution-unterricht-klasse-8", K.pin("Geschichte · Klasse 8 · Einstiege", "Französische Revolution: 3 Einstiege", "die hängen bleiben", cards([
    ("Ständepyramide mit Gummibärchen", "Die ungleich verteilte Steuerlast zum Anfassen."), ("Brotpreis", "Wie viel Taschengeld bräuchte man für Brot?"),
    ("Mannheimer Forderungen 1848", "Revolution vor der eigenen Haustür.")], G, ["1", "2", "3"]), G, light=True),
    "Französische Revolution Einstieg: 3 Ideen für die erste Stunde in Klasse 8",
    "Gummibärchen-Ständepyramide, Brotpreis-Rechnung und die Mannheimer Forderungen: drei Einstiege in die Französische Revolution, die hängen bleiben. Mit rotem Faden und Klassenarbeit im Artikel. #FranzösischeRevolution #Unterrichtseinstieg",
    "Französische Revolution Einstieg, Ständepyramide, Unterrichtseinstieg Geschichte, Französische Revolution Klasse 8, Geschichte Ideen")

# Produktive Schreibaufgabe
add("prod1", "produktive-schreibaufgabe-lektuere-pruefung", K.pin("Abschlussprüfung Deutsch · Lektüre", "Produktive Schreibaufgabe", "4 Textsorten auf einen Blick", grid([
    ("Tagebucheintrag", "Ort, Datum, Ich-Form; Erlebtes im Präteritum, Gefühle im Präsens."), ("Innerer Monolog", "Ich-Form, Präsens, kurze Sätze, keine Anrede, kein Datum."),
    ("Brief", "Ort, Datum, Anrede, Gruß, Unterschrift; Ton passt zum Empfänger."), ("Dialog", "Sprechernamen mit Doppelpunkt, Regieanweisungen in Klammern.")], D)
    + note("RSA: rund 250 Wörter · HSA: rund 150 Wörter"), D),
    "Produktive Schreibaufgabe zur Lektüre: Tagebuch, Brief, Monolog, Dialog – Prüfung Deutsch",
    "Tagebucheintrag, innerer Monolog, Brief oder Dialog: die vier Textsorten der produktiven Schreibaufgabe zur Prüfungslektüre mit ihren Merkmalen. Für Realschulabschluss und Hauptschulabschluss in BW. #Abschlussprüfung #Lektüre",
    "produktive Schreibaufgabe, Schreibaufgabe Lektüre, Abschlussprüfung Deutsch Lektüre, Tagebucheintrag innerer Monolog Brief, Prüfung Deutsch Klasse 10")
add("prod2", "produktive-schreibaufgabe-lektuere-pruefung", K.pin("Abschlussprüfung Deutsch · Lektüre", "Bevor du schreibst:", "6 Schritte zur Schreibaufgabe", cards([
    ("Situation genau lesen", "besonders den Zeitpunkt"), ("Wissen der Figur prüfen", "Was weiß sie schon – was nicht?"), ("Textsorte wählen", "die mit den meisten Ideen"),
    ("In der Stimme der Figur", "nicht in deiner eigenen"), ("Gedanken statt Handlung", ""), ("Mit dem Roman abgleichen", "Namen, Orte, Reihenfolge")], D, ["1", "2", "3", "4", "5", "6"]), D, light=True),
    "Produktive Schreibaufgabe: 6 Schritte, mit denen die Lektüre-Aufgabe gelingt",
    "Situation lesen, Wissen der Figur prüfen, Textsorte wählen, in der Stimme der Figur schreiben, Gedanken statt Handlung und mit dem Roman abgleichen: sechs Schritte für die Prüfung. #Prüfungsvorbereitung #Lektüre",
    "Schreibaufgabe Lektüre Tipps, produktive Schreibaufgabe Schritte, Prüfungsvorbereitung Deutsch, Lektüre Prüfung Realschule")

# Materialgestütztes Argumentieren
add("mga1", "materialgestuetztes-argumentieren-klasse-10", K.pin("Realschulabschluss Deutsch · Klasse 10", "Materialgestütztes Argumentieren", "So werden die 40 Punkte vergeben", big([
    ("16", "Hauptteil: Argumente belegt, erklärt, gewichtet"), ("10", "Sprache"), ("4 + 4", "Einleitung und Schluss"), ("4 + 2", "Rechtschreibung und Form")], D), D),
    "Materialgestütztes Argumentieren Klasse 10: so werden die 40 Punkte verteilt",
    "40 Punkte im materialgestützten Argumentieren: 16 für den Hauptteil, 10 für die Sprache, je 4 für Einleitung, Schluss und Rechtschreibung, 2 für die Form. Mit Aufbau und Satzbausteinen im Artikel. #Realschulabschluss #Argumentieren",
    "materialgestütztes Argumentieren, materialgestütztes Schreiben Klasse 10, Argumentieren Bewertung, Realschulabschluss Deutsch, Aufgabe 2 Deutsch")
add("mga2", "materialgestuetztes-argumentieren-klasse-10", K.pin("Materialgestütztes Argumentieren", "Satzbausteine für Klasse 10", "", chips([
    "Immer wieder wird darüber diskutiert, ob …", "Ein wichtiges Argument für … ist, dass …", "Das zeigt auch Material 2 … (vgl. M2)", "Zwar …, allerdings …",
    "Kritiker wenden ein, dass …", "Nach Abwägung der Argumente …", "Deshalb schlage ich vor, …"]), D, light=True),
    "Satzbausteine materialgestütztes Argumentieren: Formulierungen für Einleitung, Belege, Fazit",
    "Formulierungen für das materialgestützte Argumentieren in Klasse 10: Einleitung, Argument mit Materialbeleg, Gegenargument und Fazit. Zum Ausdrucken und Aufhängen. #Argumentieren #Realschulabschluss",
    "Satzbausteine Argumentieren, Formulierungen Erörterung, materialgestütztes Argumentieren Formulierungen, Deutsch Klasse 10")
add("mga3", "materialgestuetztes-argumentieren-klasse-10", K.pin("Realschulabschluss Deutsch · Klasse 10", "Materialgestützt argumentieren", "in 6 Schritten", cards([
    ("Aufgabe zerlegen", "Operator, Adressat, Textsorte"), ("Materialien sichten", "Art und Kernaussage"), ("Argumente herausarbeiten", "Pro und Kontra mit Materialnummer"),
    ("Auswählen und ordnen", "2–3 starke pro Seite, das wichtigste zuletzt"), ("Schreiben", "Argument, Erklärung, Beleg, Beispiel"), ("Überarbeiten", "Belege, Verknüpfungen, Rechtschreibung")], D, ["1", "2", "3", "4", "5", "6"]), D),
    "Materialgestütztes Argumentieren in 6 Schritten – Anleitung für Klasse 10",
    "Aufgabe zerlegen, Materialien sichten, Argumente herausarbeiten, ordnen, schreiben und überarbeiten: das materialgestützte Argumentieren in sechs Schritten für den Realschulabschluss. #Realschulabschluss #Deutschunterricht",
    "materialgestütztes Argumentieren Schritte, Argumentation schreiben, Realschulabschluss Aufgabe 2, Deutsch Klasse 10 Prüfung")

# Stoffverteilungsplan
add("svp", "stoffverteilungsplan-deutsch-klasse-10-pruefung-2027", K.pin("Deutsch · Klasse 10 · RSA 2027", "In 21 Schulwochen zur Prüfung", "Stoffverteilungsplan bis zum 27. April", cards([
    ("bis Ende Januar", "Lektüre: Leseabschnitte, Nachbereitung, Klassenarbeit"), ("Februar", "Materialgestütztes Argumentieren"), ("Anfang März", "Sachtexte, Rechtschreibung im Prüfungsformat"),
    ("Mitte–Ende März", "Gedicht und Prosatext"), ("5.–16. April", "Probeklausur (240 Minuten)"), ("19.–23. April", "Wiederholung, Operatoren, Selbstcheck"), ("27. April", "Deutschprüfung, 9 Uhr")], D), D),
    "Stoffverteilungsplan Deutsch Klasse 10: in 21 Schulwochen zur Prüfung 2027 BW",
    "Der Fahrplan für Deutsch Klasse 10 bis zum Realschulabschluss am 27. April 2027: Lektüre bis Ende Januar, Argumentieren im Februar, Sachtexte und Lyrik im März, Probeklausur im April. #Stoffverteilungsplan #Realschulabschluss",
    "Stoffverteilungsplan Deutsch Klasse 10, Jahresplanung Deutsch Klasse 10, Prüfungsvorbereitung Fahrplan, Realschulabschluss 2027, Deutsch Klasse 10 Planung")

# Inflation 1923
add("infl", "inflation-1923-einfach-erklaert", K.pin("Geschichte · Weimarer Republik", "Inflation 1923", "einfach erklärt", cards([
    ("Kriegskredite", "Der Erste Weltkrieg wurde vor allem mit Krediten finanziert."), ("Reparationen", "Zahlungen an die Siegermächte"),
    ("Ruhrbesetzung, Januar 1923", "Die Regierung bezahlte Streikende mit neu gedrucktem Geld."), ("November 1923", "Die Rentenmark stabilisiert die Währung.")], G, ["1", "2", "3", "✓"])
    + big([("1 : 1 Billion", "1 Rentenmark = 1 Billion Papiermark")], G), G),
    "Inflation 1923 einfach erklärt: Ursachen, Ruhrbesetzung und Rentenmark – Geschichte",
    "Warum kam es 1923 zur Hyperinflation? Kriegskredite, Reparationen und die Ruhrbesetzung – bis die Rentenmark im November 1923 die Währung stabilisierte. Im Artikel mit einer Unterrichtsidee zum Staunen. #Inflation1923 #WeimarerRepublik",
    "Inflation 1923, Hyperinflation einfach erklärt, Inflation 1923 Ursachen, Rentenmark, Weimarer Republik Krisenjahr, Geschichte Klasse 9")

# Antisemitismus
add("antisem1", "antisemitismus-erkennen-unterricht", K.pin("Gemeinschaftskunde · Geschichte · Klasse 8–10", "Antisemitismus erkennen", "5 Formen", cards([
    ("Religiöser Antijudaismus", "uralte, christlich geprägte Vorwürfe"), ("Rassistischer Antisemitismus", "Abwertung als angebliche „Rasse“"), ("Verschwörungsmythen", "„die Juden“ lenkten heimlich Banken oder Medien"),
    ("Sekundärer Antisemitismus", "Abwehr der Erinnerung an den Holocaust"), ("Israelbezogener Antisemitismus", "Hass auf Juden über den Staat Israel")], GK, ["1", "2", "3", "4", "5"]), GK),
    "Antisemitismus erkennen: 5 Formen einfach erklärt für den Unterricht Klasse 8–10",
    "Religiöser Antijudaismus, rassistischer Antisemitismus, Verschwörungsmythen, sekundärer und israelbezogener Antisemitismus: fünf Formen erkennen. Im Artikel mit aktuellen Zahlen und was Schule tun kann. #Antisemitismus #Demokratiebildung",
    "Antisemitismus erkennen, Formen Antisemitismus, Antisemitismus Unterricht, Antisemitismus Schule, Demokratiebildung Klasse 9")
add("antisem2", "antisemitismus-erkennen-unterricht", K.pin("Für Lehrkräfte", "Antisemitismus an der Schule: Was tun?", "", cards([
    ("Sofort eingreifen", "die Aussage klar benennen"), ("Betroffene schützen", "später in Ruhe mit der Klasse aufarbeiten"), ("Dokumentieren und melden", "Schulleitung, bei Straftaten Polizei"),
    ("Gesprächsregeln festlegen", "vor dem Einstieg"), ("Jüdisches Leben heute zeigen", "nicht nur als Opfergeschichte")], GK, ["✓"] * 5), GK, light=True),
    "Antisemitismus an der Schule: 5 Schritte, was Lehrkräfte tun können",
    "Eingreifen, Betroffene schützen, dokumentieren und melden, Gesprächsregeln setzen und jüdisches Leben als Gegenwart zeigen: was Lehrkräfte bei Antisemitismus tun können. Mit Formen und Zahlen im Artikel. #Antisemitismus #Schule",
    "Antisemitismus Schule Lehrer, Antisemitismus was tun, Prävention Antisemitismus, Demokratiebildung Schule")

# Zweitmotive bereits vorhandener Artikel
add("weimar2", "weimarer-republik-einfach-erklaert", K.pin("Geschichte · Klasse 8/9", "Weimarer Republik", "Krisenjahre – Goldene Zwanziger – Untergang", cards([
    ("1918/19", "Revolution, Republik, Verfassung"), ("1923", "Krisenjahr: Hyperinflation, Hitlerputsch"), ("1924–1929", "Goldene Zwanziger"),
    ("1929", "Weltwirtschaftskrise"), ("30. Januar 1933", "Hitler wird Reichskanzler – Ende der Republik")], G), G, light=True),
    "Weimarer Republik in 5 Phasen: von der Revolution 1918 bis 1933 – Spickzettel Geschichte",
    "Die Weimarer Republik in fünf Phasen: Revolution und Verfassung, Krisenjahr 1923, Goldene Zwanziger, Weltwirtschaftskrise und das Ende 1933. Einfach erklärt mit Selbsttest im Artikel. #WeimarerRepublik #Geschichtsunterricht",
    "Weimarer Republik Phasen, Weimarer Republik Spickzettel, Weimarer Republik Klasse 9, Goldene Zwanziger, Geschichte Klasse 8")
add("planer2", "pruefungsplaner-deutsch-2027", K.pin("Kostenloses Tool · Deutsch BW", "Wann muss die Lektüre fertig sein?", "Der Prüfungsplaner rechnet es dir aus", cards([
    ("Abschluss wählen", "RSA oder HSA"), ("Stunden und Lektürestand eingeben", ""), ("Wochenplan bekommen", "mit allen BW-Ferien bis zum 27. April 2027")], D, ["1", "2", "3"]), D, cta="Prüfungsplaner öffnen"),
    "Prüfungsplaner Deutsch 2027: kostenlos ausrechnen, wann die Lektüre fertig sein muss",
    "Wie viele Wochen bleiben bis zur Deutschprüfung am 27. April 2027? Der kostenlose Prüfungsplaner für RSA und HSA in Baden-Württemberg erstellt deinen Wochenplan mit allen Ferien. #Prüfungsplaner #Abschlussprüfung",
    "Prüfungsplaner Deutsch 2027, Wochenplan Prüfung, Deutschprüfung BW 2027, Prüfungsvorbereitung Planung, Realschulabschluss Planer")
add("klapp2", "differenzieren-klappklasse-g-m", K.pin("Klappklasse · Realschule BW", "G und M in einem Raum?", "So bleibt es fair für alle", cards([
    ("Ein Thema, drei Fassungen", "G, M und E arbeiten am gleichen Inhalt."), ("Gleicher Look", "Niemand fühlt sich abgestempelt."), ("Selbstkontrolle", "Lösungen schaffen dir Zeit für einzelne Schüler.")], W, ["G", "M", "E"]), W, light=True),
    "Klappklasse G und M: so differenzierst du fair – Tipps für Realschule BW",
    "Zwei Niveaus in einem Raum: ein Thema in drei Fassungen, gleicher Look und Selbstkontrolle mit Lösungen. Praxistipps für die Klappklasse an Realschule und Gemeinschaftsschule. #Differenzierung #Realschule",
    "Klappklasse Tipps, Differenzierung G M E, Binnendifferenzierung Realschule, Klappklasse BW, Unterrichtstipps")
