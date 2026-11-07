# Projektstatus – Reverse Aging Routinen

Alleinige aktuelle Statusquelle dieses registrierten Projekts. Historische Abnahmen und Übergaben sind Belege, keine konkurrierenden Statusquellen.

| Feld | Wert |
|---|---|
| Projekt | Reverse Aging Routinen |
| Arbeitsstatus | COS-014: ausdrücklich freigegebene Weiterleitungsprüfung implementiert und lokal geprüft; genau ein neu freigegebener Veröffentlichungslauf steht aus. |
| Letzte Statusaktualisierung | 2026-11-07T09:23:20+01:00 |
| Zuletzt erledigt | Prüfprinzip aus Rezepte b3467bd übernommen: deploy-pruefen.mjs löst bestehende Weiterleitungen ohne Zugangsdaten auf, erlaubt nur heger.earth/www.heger.earth und den unveränderten Seitenpfad; version.json wird direkt am geprüften Ziel strikt mit dem erwarteten Commit abgeglichen. Workflow und Veröffentlichungsskript verwenden denselben Prüfer. Keine Server-, URL-, Zertifikats-, Weiterleitungs- oder Inhaltsänderung. |
| Nächster Schritt | Genau einmal mit ./veroeffentlichen.sh veröffentlichen; Action-Ergebnis und Live-Commit belegen. Fachliche Durchsicht von Pfad A bleibt unabhängig offen. |
| Offene Entscheidung | Fachliche Durchsicht des neuen Pfads A (Dosierungen sind redaktionell) durch Ernesto offen. Werte von WHO und EWGSOP2 nach übereinstimmenden Übersichten von Ernesto am 2026-11-03 akzeptiert (Hinweis bleibt in der Fußnote). |
| Inhaltsstand | site/content.md ist der einzige Textquelltext: am 2026-11-06 lokal 58.002 Bytes und 37 Fußnotendefinitionen gezählt; site/hub.json enthält sieben Seiten mit Aufteilung und Kurzfassungen (Karten, Übungen, Tests). Inhalte bei dieser Statuspflege nicht verändert. A5-Bild, Sketchnote, 13 Workout-Grafiken, 9 Zeichnungen für Pfad A (pfad-a-*.png; Quellen in work/zeichnungen-pfad-a/, frühere Pfad-B-Zeichnungen archiviert in work/zeichnungen-pfad-b/) und Schrift Barlow Condensed (OFL) in site/assets; outputs/morgenroutine-a5.pdf; Designvorschlag in work/designvorschlag-2026-11-03/; Archiv der Recherchefassung in archiv/; Sicherungen in work/backup-2026-11-03-vor-zusammenfuehrung/ (u. a. *-vor-hub.*). |
| Prüfstand | 2026-11-07: 27 Offline-Tests des gemeinsamen Deployment-Prüfers bestanden; node --check, bash -n und Workflow-YAML-Prüfung erfolgreich. Build: 187699 Bytes, 7 Seiten, 37 Nachweise. SHA-256-Vergleich bestätigt 31 unveränderte Quelldateien (Text, Hub, Styles, Seitenskript, Assets). Neuer Prüfer bestätigt bisherigen Live-Commit a0db75cf0ce89c1b975b21f4b85a6916e769f61c und ISO-Zeit nach genau einer bestehenden Weiterleitung zu https://www.heger.earth/reverse-aging/. Neuer Deploy noch ausstehend. |
| Site-Stand | Commit a0db75cf0ce89c1b975b21f4b85a6916e769f61c ist nach FTPS live nachweisbar; keine erfolgreiche Veröffentlichung bestätigt: Action 42353986101 beim Erreichbarkeitstest fehlgeschlagen. HTTP liefert 301 nach HTTPS/www, dort Version und HTML mit HTTP 200 erreichbar. Kein zweiter Veröffentlichungsversuch. Abschließender Statusnachtrag nur lokal. |
| Site-Projekt-ID | GitHub ernesto-earth/reverse-aging |
| Site-Version | a0db75c · 2026-11-07T08:05:46.488Z (version.json live geprüft; Action fehlgeschlagen) |
| Site-URL | http://heger.earth/reverse-aging/ (Link auch als .webloc im Ordner) |
| Zuletzt aktualisiert durch | Hermes, ausdrücklich bestätigter COS-Auftrag COS-014 am 2026-11-07 |

## Lokale Belege

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
