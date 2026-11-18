# Projektstatus – reverse-aging

Alleinige aktuelle Statusquelle dieses registrierten Projekts. Historische Abnahmen und Übergaben sind Belege, keine konkurrierenden Statusquellen.

| Feld | Wert |
|---|---|
| Projekt | reverse-aging |
| Arbeitsstatus | aktiv; seit E-035 Vorprod (heger.earth/vorprod/reverse-aging/) und Prod (heger.earth/reverse-aging/), Fettstoffwechsel-Seite Fassung 1.0. |
| Letzte Statusaktualisierung | 2026-11-18T19:58:00+01:00 |
| Zuletzt erledigt | 18.11.2026: E-035 umgesetzt – Workflow main → Vorprod, prod → live, veroeffentlichen.sh mit --freigeben. E-036: Repo und Seite bleiben öffentlich. Danach Freigabeprüfung angepasst: Bei reinen Doku-/Statuscommits gilt der zuletzt ausgelieferte, inhaltlich gleiche Commit (fee705f), auf Vorprod und Prod veröffentlicht. |
| Nächster Schritt | Keiner beauftragt. Hermes-Pfad und GitHub Desktop sind mit E-035 geklärt (Git-Daten verlegt, GitHub Desktop am MacBook getrennt). |
| Offene Entscheidung | keine |
| Inhaltsstand | geprüft: Unterseite Fettstoffwechsel am 17.11.2026 von Ernesto als Fassung 1.0 freigegeben; die Dosierungen auf Pfad A bleiben ausdrücklich redaktionelle Vorschläge und sind in der Fußnote so gekennzeichnet. |
| Prüfstand | geprüft: Deployment-Tests (32/32) und Seitenbau in den Actions bestanden; Prod-Deploy 44303770351 am 18.11.2026 success, Live-Version fee705f bestätigt. |
| Site-Stand | veröffentlicht: http://heger.earth/reverse-aging/ aus Commit fee705f (Branch prod), Action 44303770351 erfolgreich am 18.11.2026; Vorprod http://heger.earth/vorprod/reverse-aging/. |
| Site-Projekt-ID | GitHub ernesto-earth/reverse-aging |
| Site-Version | fee705f / 2026-11-18T12:25:36.174Z |
| Site-URL | http://heger.earth/reverse-aging/ (Link auch als .webloc im Ordner) |
| Zuletzt aktualisiert durch | Claude im Auftrag Ernestos vom 2026-11-18; nur diese Statusquelle geändert, keine Veröffentlichung daraus abgeleitet. |

## Belege

### Offene Entscheidung geschlossen, 17.11.2026

Mit der Freigabe der Fettstoffwechsel-Seite als Fassung 1.0 ist keine fachliche
Entscheidung mehr offen. Die früheren Angaben bleiben als Beleg erhalten: Werte von
WHO und EWGSOP2 am 2026-11-03 von Ernesto akzeptiert, Hinweis dazu in der Fußnote;
die Dosierungen auf Pfad A bleiben redaktionelle Vorschläge.

### Freigabe der Fettstoffwechsel-Seite als Fassung 1.0, 17.11.2026

Ernesto hat die am 16.11.2026 veröffentlichte Unterseite durchgesehen und für eine
Fassung 1.0 freigegeben. Am Text, an den 27 Nachweisen und an den Herkunftskennzeichnungen
wurde dabei nichts geändert. Die Dosierungsangaben auf Pfad A bleiben redaktionelle
Vorschläge ohne eigenen Beleg; die entsprechende Kennzeichnung in der Fußnote bleibt
bestehen. Eine spätere Fassung kann sie durch belegte Werte ersetzen.

### Rückweg zum Cockpit, 17.11.2026

Die Kopfleiste trägt links ein Signalzeichen, das auf http://www.heger.earth/cos/#/uebersicht
führt. Geändert wurden `site/build.mjs` und `site/styles.css`; `site/content.md`, die
Nachweise und die Herkunftskennzeichnungen blieben unberührt. Die fachliche Durchsicht
der Unterseite Fettstoffwechsel durch Ernesto bleibt offen und hält den Inhaltsstand
weiterhin auf Achtung.

### Übernommener Belegstand vor COS-018

Die folgenden Angaben sind unverändert übernommene Dokumentation, keine in COS-018 erneut ausgeführten Prüfungen.

- Bisheriger Arbeitsstatus: COS-014 abgeschlossen; Prüfkorrektur genau einmal veröffentlicht, Action erfolgreich und Live-Commit identisch.
- Bisherige letzte Statusaktualisierung: 2026-11-07T09:24:53+01:00.
- Bisheriges Feld „Zuletzt erledigt“: Prüfprinzip aus Rezepte b3467bd übernommen: gemeinsamer deploy-pruefen.mjs für Workflow und Veröffentlichungsskript; bestehende Weiterleitungen ohne Zugangsdaten, nur heger.earth/www.heger.earth und unveränderter Seitenpfad, strikter Live-version.json-Abgleich am geprüften Ziel. Genau ein neu freigegebener Lauf: Commit 77bec4ef16ace6eebfc0df34c1cba277f2c5a205, Action 42355308795 success, Live-Commit identisch. Keine Server-, URL-, Zertifikats-, Weiterleitungs- oder Inhaltsänderung.
- Bisheriges Feld „Inhaltsstand“: site/content.md ist der einzige Textquelltext: am 2026-11-06 lokal 58.002 Bytes und 37 Fußnotendefinitionen gezählt; site/hub.json enthält sieben Seiten mit Aufteilung und Kurzfassungen (Karten, Übungen, Tests). Inhalte bei dieser Statuspflege nicht verändert. A5-Bild, Sketchnote, 13 Workout-Grafiken, 9 Zeichnungen für Pfad A (pfad-a-*.png; Quellen in work/zeichnungen-pfad-a/, frühere Pfad-B-Zeichnungen archiviert in work/zeichnungen-pfad-b/) und Schrift Barlow Condensed (OFL) in site/assets; outputs/morgenroutine-a5.pdf; Designvorschlag in work/designvorschlag-2026-11-03/; Archiv der Recherchefassung in archiv/; Sicherungen in work/backup-2026-11-03-vor-zusammenfuehrung/ (u. a. *-vor-hub.*).
- Bisheriges Feld „Prüfstand“: 2026-11-07: 27 Offline-Tests bestanden; node --check, bash -n und Workflow-YAML-Prüfung erfolgreich. Build erfolgreich: 7 Seiten, 37 Nachweise (Build-Ausgabe: 187699 bytes). SHA-256-Vergleich bestätigt 31 unveränderte Quelldateien (Text, Hub, Styles, Seitenskript, Assets). GitHub-API bestätigt Action 42355308795 success für den vollen Commit, einschließlich Offline-Tests, Versionserzeugung, FTPS und Live-Prüfung. Skript bestätigt HTTP 200 nach einer bestehenden Weiterleitung und exakten Live-Commit; Live-HTML zusätzlich bytegleich mit lokalem Build (189416 Bytes).
- Bisheriges Feld „Site-Stand“: Erfolgreich veröffentlicht: Commit 77bec4ef16ace6eebfc0df34c1cba277f2c5a205, Action https://github.com/ernesto-earth/reverse-aging/actions/runs/42355308795 success. http://heger.earth/reverse-aging/ leitet unverändert nach https://www.heger.earth/reverse-aging/; version.json dort HTTP 200, Commit identisch und deployed_at 2026-11-07T08:24:00.046Z. Genau ein Lauf nach ergänzender Freigabe; abschließender Statusnachtrag nur lokal, kein weiterer Push.
- Bisherige Aktualisierung durch: Hermes, ausdrücklich bestätigter COS-Auftrag COS-014 am 2026-11-07.

### Lokale Belege

### Vollständige Erläuterungen zu den gekürzten Statusfeldern

Die Statusfelder wurden am 2026-11-06 für die bestehenden Übertragungsgrenzen gekürzt, ohne Code oder Abgleich auszuführen. Die bisherigen vollständigen Erläuterungen bleiben hier in derselben alleinigen Statusquelle erhalten. Der aktuelle Live-Deploy bleibt unbekannt; der lokale Git-Stand ist kein Veröffentlichungsnachweis.

- Bisheriges Feld „Zuletzt erledigt“: 2026-11-06: Projekt auf Hermes umgestellt (E-024): `veroeffentlichen.sh` (Build, Commit, Push, Action- und Seitenprüfung), `.hermes.md` mit Arbeitsablauf, README angepasst; Build lokal geprüft. Noch nicht über Hermes veröffentlicht. Davor 2026-11-05: Projektordner als einzige Quelle eingerichtet: README.md, .gitignore; Repo ernesto-earth/reverse-aging spiegelt den Ordner, Action baut aus site/ (node build.mjs --assets) und lädt nach heger.earth/reverse-aging; alter Git-Ordner der ChatGPT-Site aus site/ nach archiv/ verschoben. Davor 2026-11-03: Kraftplan umgebaut (E-015): Studioplan „Big 5“ und Heimvariante gestrichen; neuer Pfad A daheim mit Langhantel, Kurzhanteln, Klimmzugstange und Theraband an der Türschnalle in zwei Einheiten (9 Übungen, je eine Zeichnung); Calisthenics ist Pfad B; Big-5-Interview als Quelle unter Hintergrund. Zuvor: Pfad B (Heimvariante) wie Pfad C mit Bildkarten: fünf schlichte Strichzeichnungen (Start- und Endposition), Quellen in work/zeichnungen-pfad-b/. Zuvor: Routinen-Hub an den Designvorschlag angeglichen (Überblick am Handy mit Umschalter Heute/Woche/Quartal; Kraft mit Pfad-Reitern im Kopf, Steigerung und Seitenleiste nebeneinander; alle Details je Seite in einem aufklappbaren Block). Zuvor: Seite als Routinen-Hub mit sieben kurzen Unterseiten neu gebaut und veröffentlicht (E-014): Überblick, Morgen, Kraft, Bewegung, Ernährung, Tests, Hintergrund; Kopfleiste statt großem Titelbereich, Details aufklappbar, Quellen je Seite; Calisthenics-Stufen mit 13 Grafiken wiederhergestellt (waren bei der Zusammenführung verloren gegangen). Davor am selben Tag: Routinen und ReverseAging zusammengeführt (E-012/E-013).
- Bisheriges Feld „Site-Projekt-ID“: GitHub ernesto-earth/reverse-aging (früher Claude-Seite ca9209c0-c32c-443a-8845-5890a6693cd1, davor ChatGPT appgprj_6acc96d902008191acb23f0aa14bc8b8)
- Bisheriges Feld „Site-Version“: unbekannt (aktueller Live-Commit/Deploy nicht neu verifiziert); lokaler Git-HEAD a00392b ist kein Live-Nachweis. E-024-Anleitungen und Veröffentlichungsskript liegen teilweise nur lokal vor.

### Weitere lokale Belege

- Statusprüfung 2026-11-06: Die seit dem früheren Statuszeitpunkt neueren Dateien `.hermes.md`, `README.md` und `veroeffentlichen.sh` wurden vollständig gelesen. README ergänzt den Hermes-Veröffentlichungsweg; das Skript sieht Vorspulen, Build, `git add -A`, Commit, Push, Action-Abfrage und HTTP-Prüfung vor. `bash -n` erfolgreich; das Skript wurde nicht ausgeführt. Sein Ergebnistext allein ersetzt keinen erfolgreichen Deploy- und Inhaltsnachweis. Desktop-Modell gemäß E-026 vorerst extern, Cockpit-Ausführung weiterhin lokal; der Modellwechsel ist keine hier vorgenommene Änderung. Frühere Arbeits- und Abnahmeangaben oben bleiben historische Belege.
- `.hermes.md`, `veroeffentlichen.sh`
- `README.md`
- `.github/workflows/deploy.yml`
- `outputs/morgenroutine-a5.pdf`
- `work/pdfs/build_morgenroutine_a5.py`
- `site/content.md`
- `site/hub.json`
- `work/designvorschlag-2026-11-03/`
