#!/usr/bin/env python3
"""Baut Routinen/site/content.md nach der neuen Struktur (E-012).
Übernommene Abschnitte werden wortgleich aus den bisherigen Quelltexten ausgeschnitten."""
import re, sys
from pathlib import Path

ROUT = Path(sys.argv[1])          # Routinen/site/content.md (alt)
RA = Path(sys.argv[2])            # ReverseAging/content.md (Quellenarchiv)
OUT = Path(sys.argv[3])

rout = ROUT.read_text(encoding="utf-8").split("\n")
ra_text = RA.read_text(encoding="utf-8")
ra = ra_text.split("\n")

def section(lines, heading, include_heading=True):
    """Text ab der Überschrift bis zur nächsten Überschrift gleicher oder höherer Ebene."""
    idx = [i for i, l in enumerate(lines) if l.strip() == heading]
    assert len(idx) == 1, (heading, idx)
    start = idx[0]
    level = len(heading.split(" ")[0])
    end = len(lines)
    for j in range(start + 1, len(lines)):
        m = re.match(r"^(#{1,6})\s", lines[j])
        if m and len(m.group(1)) <= level:
            end = j; break
        if lines[j].startswith("[^"):
            end = j; break
    body = lines[start if include_heading else start + 1:end]
    while body and not body[-1].strip(): body.pop()
    return "\n".join(body)

def demote(text, by=1):
    return re.sub(r"^(#{2,5})(\s)", lambda m: "#" * (len(m.group(1)) + by) + m.group(2), text, flags=re.M)

def footnotes(lines):
    return [l for l in lines if l.startswith("[^")]

# ---------- übernommene Bausteine ----------
morning = section(rout, "## Morgenroutine", include_heading=False)
pdf_line = "**Zum Ausdrucken:** [Morgenroutine als einseitige A5-PDF](assets/morgenroutine-a5.pdf)"
assert pdf_line in morning
morning = morning.replace(pdf_line,
    "**Zum Ausdrucken:** Die einseitige A5-Fassung liegt im Projektordner Routinen (`outputs/morgenroutine-a5.pdf`).\n\n"
    "Anker 3 (Training) und Anker 4 (Protein) sind unten ausführlicher beschrieben: [Wöchentlich: Kraft](#wochentlich-kraft) und [Ernährung](#ernahrung).")

calis = section(rout, "### Häng dich rein: Calisthenics in drei Levels", include_heading=False)

training = section(ra, "## Trainingsvorschläge", include_heading=False)
training = training.replace("### Plan A: „Big 5“ im Fitnessstudio", "### Pfad A: „Big 5“ im Fitnessstudio")
training = training.replace("### Plan B: Heimvariante ohne Geräte", "### Pfad B: Heimvariante ohne Geräte")
assert "### Pfad A" in training and "### Pfad B" in training

protein_book = section(ra, "## Ernährung und Protein", include_heading=False)
protein_book_par = [l for l in protein_book.split("\n") if l.startswith("**[Buch – verifiziert]**")][0]
protein_limits = protein_book[protein_book.index("Wichtig sind die Grenzen:"):]

kreatin = section(ra, "## Kreatin", include_heading=False)
kreatin = kreatin.replace("### Buchaussage", "#### Was Gießing sagt").replace("### Was die Evidenz hergibt", "#### Was die Evidenz hergibt")

hit = section(ra, "## HIT-Trainingsprinzipien", include_heading=False)
evidence = section(ra, "## Wissenschaftliche Evidenz zu zentralen Aussagen")
meaning = section(ra, "## Was „Reverse Aging“ sinnvoll bedeuten kann – und was nicht")
kurzurteil = [l for l in ra if l.startswith("> **Kurzurteil:**")][0]

leseschluessel = section(ra, "## Quellenstatus und Leseschlüssel")
leseschluessel = leseschluessel.replace(
    "- **[Fachliteratur]**: unabhängige Leitlinie, systematische Übersichtsarbeit, Metaanalyse oder Positionspapier.",
    "- **[Fachliteratur]**: unabhängige Leitlinie, systematische Übersichtsarbeit, Metaanalyse oder Positionspapier.\n"
    "- **[Magazin]**: Trainingsplan aus einem Publikumsmagazin; Übungen und Dosierungen nach dem Artikel, Darstellung redaktionell.\n"
    "- **[Redaktioneller Vorschlag]**: praktische Übertragung dieser Seite; kein Inhalt der genannten Quellen.")
assert "[Magazin]" in leseschluessel, "Leseschlüssel-Zeile nicht gefunden"
leseschluessel = leseschluessel.replace("Diese Seite trennt drei Ebenen:", "Diese Seite kennzeichnet die Herkunft jeder Aussage:")
biblio = section(ra, "## Bibliografische Angaben")
book_core = section(ra, "### Kernaussagen des Buchprojekts")
author = section(ra, "## Autor")
interviews = section(ra, "## Interviews, Podcasts und Rezensionen")
critique = section(ra, "## Kritische Gesamtbewertung")
sources = section(ra, "## Bibliografie und Quellen")

fn = footnotes(ra) + [l for l in footnotes(rout) if l.startswith("[^calisthenics]")]
fn += [
 "[^steadi-chair]: Centers for Disease Control and Prevention, STEADI, *Assessment: 30-Second Chair Stand*, 2017. Unterdurchschnittliche Werte nach Rikli & Jones 1999. Zugriff 03.11.2026.",
 "[^steadi-balance]: Centers for Disease Control and Prevention, STEADI, *Assessment: The 4-Stage Balance Test*, 2017. Zugriff 03.11.2026.",
 "[^ewgsop2]: Cruz-Jentoft, A. J. et al. (2019): *Sarcopenia: revised European consensus on definition and diagnosis* (EWGSOP2). *Age and Ageing*, 48(1), 16–31. Grenzwerte hier nach übereinstimmenden Übersichtstabellen wiedergegeben; der Originalartikel war bei dieser Recherche nicht direkt abrufbar.",
 "[^nsf]: Hirshkowitz, M. et al. (2015): *National Sleep Foundation's updated sleep duration recommendations: final report*. *Sleep Health*, 1(4), 233–243.",
]

# ---------- neue Texte ----------
doc = f"""---
title: "Reverse Aging – Routinen für ein starkes Älterwerden"
subtitle: "Was täglich, wöchentlich und vierteljährlich hilft – mit Herkunft und Evidenz"
language: de
status: "Zusammengeführte Routinenseite (E-012)"
stand: "2026-11-03"
---

# Reverse Aging – Routinen für ein starkes Älterwerden

> **Worum es geht:** Muskelkraft gehört zu den am besten beeinflussbaren Faktoren gesunden Älterwerdens. Diese Seite übersetzt das in Routinen: was täglich, wöchentlich und einmal pro Quartal zu tun ist – jeweils mit Herkunft und Evidenz. „Reverse Aging“ steht hier für beeinflussbare Altersfolgen wie Kraft, Funktion und Gleichgewicht, nicht für ein Versprechen der Verjüngung.

## Auf einen Blick

| Rhythmus | Routine | Umfang | Herkunft und Evidenz |
|---|---|---|---|
| täglich | Morgenroutine mit fünf Ankern | über den Vormittag verteilt | [Redaktioneller Vorschlag] |
| 2 × pro Woche | Krafttraining für den ganzen Körper: Pfad A im Studio oder Pfad B daheim | je etwa 30–45 Minuten | [Fachliteratur] gut belegt[^veryold][^who] |
| über die Woche | Ausdauer, moderat oder intensiv | 150–300 Minuten moderat oder 75–150 Minuten intensiv | [Fachliteratur] WHO-Empfehlung[^who] |
| an 3 Tagen pro Woche (ab 65) | Gleichgewicht und Kraft kombiniert | kurz, in Training oder Alltag eingebaut | [Fachliteratur] WHO-Empfehlung[^who] |
| jede Nacht | Schlaf | 7–9 Stunden (26–64 Jahre), 7–8 Stunden (ab 65) | [Fachliteratur][^nsf] |
| täglich | Protein auf die Mahlzeiten verteilt | 0,8 g/kg (19–64 Jahre), 1,0–1,2 g/kg (ab 65) pro Tag | [Fachliteratur][^dge][^protage] |
| optional | Kreatinmonohydrat zusätzlich zum Training | nach eigener Abwägung | [Fachliteratur] moderat belegt[^creatine-meta] |
| vierteljährlich | Selbsttests: Aufstehen, Gleichgewicht, Gehtempo | etwa 10 Minuten | [Fachliteratur][^steadi-chair][^ewgsop2] |
| als Kür | Pfad C: Calisthenics in drei Levels | wenn Pfad A oder B sicher sitzt | [Magazin][^calisthenics] |

> **Keine medizinische Beratung.** Bei Brustschmerz, ungeklärter Atemnot, Schwindel, Herz-Kreislauf-Erkrankung, frischer Operation oder ausgeprägter Gebrechlichkeit vor intensivem Training ärztlich oder physiotherapeutisch abklären. Details stehen bei den [Sicherheitsgrenzen](#praktische-sicherheitsgrenzen).

## Täglich: Morgenroutine

{morning}

## Wöchentlich: Kraft

**Kurzurteil:** Zwei Ganzkörpereinheiten pro Woche mit schrittweiser Steigerung sind die tragende Säule. Krafttraining steigert die Kraft auch im hohen Alter deutlich; welches Programm genau, ist zweitrangig, solange es regelmäßig und progressiv ist.[^veryold][^who]

| Pfad | Für wen | Ort | Herkunft |
|---|---|---|---|
| A · „Big 5“ an Geräten | Einstieg und dauerhafte Basis | Fitnessstudio | [Autor – Interview] |
| B · Heimvariante | ohne Studio oder als Wiedereinstieg | daheim | [Redaktioneller Vorschlag] |
| C · Calisthenics in drei Levels | wenn A oder B sicher sitzt | Klimmzugstange, Barren | [Magazin] |

{training}

## Kür: Calisthenics für Fortgeschrittene

**[Redaktioneller Vorschlag]** Pfad C ist eine Kür. Für die Ziele dieser Seite – Kraft und Alltagsfunktion – ist er nicht nötig; er bietet aber einen motivierenden Stufenplan für Oberkörper- und Rumpfkraft. Als Eingangsvoraussetzung gilt hier: Pfad A oder B läuft seit einigen Monaten regelmäßig und beschwerdefrei, und die drei Basisübungen gelingen technisch sauber.

{calis}

## Wöchentlich: Ausdauer, Gleichgewicht, Erholung

**Kurzurteil:** Kraft allein reicht nicht. Die WHO empfiehlt zusätzlich Ausdauer und ab 65 Jahren gezieltes Gleichgewichtstraining; ausreichend Schlaf und Ruhetage gehören dazu.[^who][^nsf]

### Ausdauer

**[Fachliteratur]** Die WHO empfiehlt Erwachsenen und Älteren pro Woche 150–300 Minuten moderate oder 75–150 Minuten intensive Ausdaueraktivität oder eine Kombination aus beidem. Dazu kommt Krafttraining für alle großen Muskelgruppen an mindestens zwei Tagen. Lange Sitzzeiten sollen begrenzt werden; jede Bewegung zählt.[^who]

**[Redaktioneller Vorschlag]** So lässt sich das im Alltag unterbringen:

| Variante | Beispiele | Woran man die Intensität erkennt | Beispielwoche |
|---|---|---|---|
| moderat | zügiges Gehen, Radfahren, Schwimmen | Sprechen geht, Singen nicht mehr | 5 × 30 Minuten |
| intensiv | Laufen, Bergauf-Radfahren, Rudern | nur noch kurze Sätze möglich | 3 × 25 Minuten |
| Alltag | Treppen, Wege zu Fuß, Gartenarbeit | – | zählt mit |

Wer Kraft und Ausdauer in derselben Einheit trainiert, macht die Kraftübungen zuerst.[^big5]

### Gleichgewicht

**[Fachliteratur]** Ab 65 Jahren empfiehlt die WHO an mindestens drei Tagen pro Woche vielseitige Aktivität, die funktionelles Gleichgewicht und Kraft verbindet, um die Leistungsfähigkeit zu erhalten und Stürzen vorzubeugen.[^who] Die CDC nennt Tai Chi als evidenzbasiertes Programm zur Sturzprävention.[^steadi-balance]

**[Redaktioneller Vorschlag]** Fünf Minuten genügen, etwa nach dem Krafttraining oder beim Zähneputzen – immer mit einem stabilen Halt in Reichweite:

1. Tandemstand (Ferse an Zehe), 3 × 30 Sekunden, Füße wechseln.
2. Einbeinstand, je Seite 3 × 20 Sekunden.
3. Auf einer Linie gehen, Ferse an Zehe, 2 × 10 Schritte.
4. Steigern: auf weicherem Untergrund stehen oder den Kopf dabei langsam drehen.

### Erholung und Schlaf

**[Fachliteratur]** Die US National Sleep Foundation empfiehlt Erwachsenen von 26 bis 64 Jahren 7–9 Stunden Schlaf, ab 65 Jahren 7–8 Stunden.[^nsf]

**[Redaktioneller Vorschlag]** Zwischen zwei intensiven Krafteinheiten liegt mindestens ein Ruhetag; Pfad A sieht ohnehin zwei nicht aufeinanderfolgende Trainingstage vor.[^big5] An Ruhetagen ist leichte Bewegung erwünscht. Anhaltende Schlafprobleme gehören ärztlich abgeklärt, nicht „wegtrainiert“.

## Ernährung

**Kurzurteil:** Protein ausreichend und über den Tag verteilt; mehr als ausreichend bringt bei gut Versorgten wenig Zusatznutzen. Kreatin ist eine Option zum Training, kein Muss.[^dge][^dge2026]

### Protein im Alltag

{protein_book_par}

| Gruppe | Orientierung pro Tag | Quelle |
|---|---|---|
| gesunde Erwachsene, 19–64 Jahre | 0,8 g pro kg Körpergewicht | DGE[^dge] |
| gesunde Erwachsene ab 65 | 1,0 g pro kg Körpergewicht | DGE[^dge] |
| gesunde Ältere | 1,0–1,2 g pro kg Körpergewicht | PROT-AGE[^protage] |
| Ältere mit akuter oder chronischer Erkrankung | häufig 1,2–1,5 g pro kg, individuell und unter Beachtung der Nierenfunktion | PROT-AGE[^protage] |

**[Redaktioneller Vorschlag]** Rechenbeispiel: 75 kg × 1,0 g = 75 g Protein pro Tag, verteilt auf zwei bis drei Mahlzeiten – so wie Anker 4 der Morgenroutine es vorsieht.

{protein_limits}

### Kreatin (optional)

{kreatin}

## Fortschritt messen

**Kurzurteil:** Einmal pro Quartal zeigen ein paar einfache Tests, ob die Routinen wirken. Es sind Screening-Werkzeuge aus der Altersmedizin, keine Diagnose; die Richtwerte gelten für Menschen ab 60. Für Jüngere zählt vor allem der eigene Verlauf.[^steadi-chair][^ewgsop2]

### Die Tests

| Test | So geht's | Richtwert | Quelle |
|---|---|---|---|
| 30-Sekunden-Aufstehtest | Stuhl ohne Armlehnen, Sitzhöhe etwa 43 cm, Arme vor der Brust gekreuzt. Zählen, wie oft man in 30 Sekunden ganz aufsteht; wer bei Zeitende mehr als halb oben ist, zählt mit. | siehe Tabelle unten | CDC STEADI[^steadi-chair] |
| Vier-Stufen-Gleichgewichtstest | Je 10 Sekunden: Füße nebeneinander, Halbtandem, Tandem (Ferse an Zehe), Einbeinstand – ohne die Füße zu bewegen, Halt in Reichweite. | Tandemstand unter 10 Sekunden: erhöhtes Sturzrisiko | CDC STEADI[^steadi-balance] |
| Fünfmal Aufstehen | Zeit für fünf vollständige Aufsteh-Wiederholungen ohne Armeinsatz. | über 15 Sekunden: Hinweis auf geringe Beinkraft | EWGSOP2[^ewgsop2] |
| Gehtempo (optional) | 4 Meter im normalen Tempo gehen, Zeit messen; Tempo = 4 ÷ Sekunden. | 0,8 m/s oder langsamer: Hinweis auf geringe körperliche Leistungsfähigkeit | EWGSOP2[^ewgsop2] |

**30-Sekunden-Aufstehtest: unterdurchschnittliche Werte nach CDC**[^steadi-chair]

| Alter | Männer | Frauen |
|---|---|---|
| 60–64 | unter 14 | unter 12 |
| 65–69 | unter 12 | unter 11 |
| 70–74 | unter 12 | unter 10 |
| 75–79 | unter 11 | unter 10 |
| 80–84 | unter 10 | unter 9 |
| 85–89 | unter 8 | unter 8 |
| 90–94 | unter 7 | unter 4 |

### So dokumentieren

**[Redaktioneller Vorschlag]** Pro Quartal eine Zeile: Datum, Testwerte, aktueller Trainingspfad, Körpergewicht, Beschwerden. Ziel ist der eigene Verlauf; die Richtwerte sind Untergrenzen für Ältere, kein Leistungsziel. Liegt ein Wert darunter oder verschlechtert er sich deutlich, ist das ein Anlass für ein ärztliches oder physiotherapeutisches Gespräch.

## Warum das wirkt

{kurzurteil}

{demote(hit)}

{demote(evidence)}

{demote(meaning)}

## Anhang: Zum Buch

Der Name dieser Seite geht auf Jürgen Gießings Ratgeber *Reverse Aging* zurück. Dieser Anhang fasst das Buch und seine Rezeption zusammen; Gießings Thesen sind oben als eine Quelle unter mehreren eingearbeitet. Die ausführliche Recherchefassung vom 12. Oktober 2026 bleibt im Quellenarchiv erhalten.

{demote(leseschluessel)}

{demote(biblio)}

{book_core}

{demote(author)}

{demote(interviews)}

{demote(critique)}

{sources}

### Ergänzende Quellen für Routinen

1. Centers for Disease Control and Prevention: [STEADI – 30-Second Chair Stand (PDF)](https://stacks.cdc.gov/view/cdc/157303/cdc_157303_DS1.pdf).
2. Centers for Disease Control and Prevention: [STEADI – The 4-Stage Balance Test (PDF)](https://www.cdc.gov/steadi/media/pdfs/STEADI-Assessment-4Stage-508.pdf).
3. Cruz-Jentoft, A. J. et al. (2019): [Sarcopenia: revised European consensus on definition and diagnosis](https://pubmed.ncbi.nlm.nih.gov/30312372/). *Age and Ageing*, 48(1), 16–31.
4. Hirshkowitz, M. et al. (2015): [National Sleep Foundation's updated sleep duration recommendations: final report](https://doi.org/10.1016/j.sleh.2015.10.004). *Sleep Health*, 1(4), 233–243.
5. Steinbach, Martina: „Häng dich rein!“, *Men's Health*, 14.10.2026, Heftseiten 56–63 (Druckausgabe).

---

*Stand: 3. November 2026. Zusammengeführt aus dem Routinen-Hub und dem quellenkritischen Reverse-Aging-Wiki (Recherchestand 12. Oktober 2026). Keine medizinische Diagnose oder individuelle Therapie- oder Trainingsanweisung.*

""" + "\n".join(fn) + "\n"

# nicht mehr referenzierte Fußnoten entfernen
body = doc.split("\n[^")[0]
used = set(re.findall(r"\[\^([^\]]+)\](?!:)", doc))
lines = []
for l in doc.split("\n"):
    m = re.match(r"^\[\^([^\]]+)\]:", l)
    if m and m.group(1) not in set(re.findall(r"\[\^([^\]]+)\](?!:)", "\n".join(x for x in doc.split("\n") if not x.startswith("[^")))):
        print("Fußnote entfernt (nicht referenziert):", m.group(1)); continue
    lines.append(l)
doc = "\n".join(lines)
defined = set(re.findall(r"^\[\^([^\]]+)\]:", doc, flags=re.M))
refd = set(re.findall(r"\[\^([^\]]+)\](?!:)", "\n".join(x for x in doc.split("\n") if not x.startswith("[^"))))
missing = refd - defined
assert not missing, f"undefinierte Fußnoten: {missing}"
OUT.write_text(doc, encoding="utf-8")
print("geschrieben:", OUT, len(doc), "Zeichen;", len(defined), "Fußnoten")
