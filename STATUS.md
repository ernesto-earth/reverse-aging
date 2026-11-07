# Projektstatus – Reverse Aging Routinen

Alleinige aktuelle Statusquelle dieses registrierten Projekts. Historische Abnahmen und Übergaben sind Belege, keine konkurrierenden Statusquellen.

| Feld | Wert |
|---|---|
| Projekt | Reverse Aging Routinen |
| Arbeitsstatus | aktiv; Website auf heger.earth/reverse-aging, Projektordner ist einzige Quelle (Grundsätze 2026-11-05); ein Projekt für Seite, Quelltext und Archiv (E-012/E-013) |
| Letzte Statusaktualisierung | 2026-11-06T11:54:47+01:00 |
| Zuletzt erledigt | 2026-11-06: E-024-Anleitungen und Veröffentlichungsskript lokal geprüft; Shell-Syntax gültig, Betriebsabnahme offen. Statusfelder innerhalb der Übertragungsgrenzen formuliert; vollständige Historie unter Lokale Belege erhalten. Kein Commit, Push oder Jobstart bei dieser Nachbesserung. |
| Nächster Schritt | Nach gesonderter Freigabe den E-024-Ende-zu-Ende-Test für dieses Projekt durchführen: Cockpit-Bestätigung, Hermes-Ausführung, exakter Commit, erfolgreicher Deploy und sichtbare Änderung getrennt belegen. Vorher nur prüfen, ob die vorbereitete Ausführung im Dienst geladen und der Zugang nutzbar ist; Einrichtung oder Neustart nicht pauschal wiederholen. Fachliche Durchsicht von Pfad A bleibt offen. Diese Statuspflege bleibt lokal, ohne Commit, Push oder Veröffentlichung durch Hermes. |
| Offene Entscheidung | Fachliche Durchsicht des neuen Pfads A (Dosierungen sind redaktionell) durch Ernesto offen. Werte von WHO und EWGSOP2 nach übereinstimmenden Übersichten von Ernesto am 2026-11-03 akzeptiert (Hinweis bleibt in der Fußnote). |
| Inhaltsstand | site/content.md ist der einzige Textquelltext: am 2026-11-06 lokal 58.002 Bytes und 37 Fußnotendefinitionen gezählt; site/hub.json enthält sieben Seiten mit Aufteilung und Kurzfassungen (Karten, Übungen, Tests). Inhalte bei dieser Statuspflege nicht verändert. A5-Bild, Sketchnote, 13 Workout-Grafiken, 9 Zeichnungen für Pfad A (pfad-a-*.png; Quellen in work/zeichnungen-pfad-a/, frühere Pfad-B-Zeichnungen archiviert in work/zeichnungen-pfad-b/) und Schrift Barlow Condensed (OFL) in site/assets; outputs/morgenroutine-a5.pdf; Designvorschlag in work/designvorschlag-2026-11-03/; Archiv der Recherchefassung in archiv/; Sicherungen in work/backup-2026-11-03-vor-zusammenfuehrung/ (u. a. *-vor-hub.*). |
| Prüfstand | 2026-11-06, lokale Statusprüfung: .hermes.md, README.md, das noch unversionierte veroeffentlichen.sh und vorhandene Git-Differenzen gelesen; bash -n für das Veröffentlichungsskript erfolgreich. Lokaler Git-HEAD a00392b; README/STATUS bereits vorher geändert. Neue Inhalts-/Build-/Browserprüfung und E-024-Betriebsabnahme nicht durchgeführt; Zugangsgeheimnisse nicht geprüft. Historischer Prüfstand vom 2026-11-03: Build ohne Fehler (7 Seiten, 37 Nachweise, jeder Abschnitt von content.md genau einer Seite zugeordnet, keine toten Sprungmarken, keine doppelten IDs); Build auf dem Mac aus dem Projektordner ergibt dieselbe Datei; alle Seiten im Browser geprüft (Desktop 1440 px und Handy 390 px, keine Skriptfehler); Gestaltung (Fassung 1793728542-dc03) von Ernesto am 2026-11-03 bestätigt. Fachliche Abnahme bleibt offen. |
| Site-Stand | Bisher dokumentierte Veröffentlichung unter http://heger.earth/reverse-aging/ (öffentliches Repo ernesto-earth/reverse-aging, GitHub Action); aktueller Live-Inhalt und exakter Deploy bei dieser lokalen Statuspflege nicht neu geprüft. E-024-Veröffentlichungsweg lokal vorbereitet, noch nicht Ende zu Ende abgenommen. Frühere Claude-Seite (claude.ai/artifact/S1pz7Q7c9yQRboJHKhRJic) und ChatGPT-Site werden nicht mehr gepflegt. |
| Site-Projekt-ID | GitHub ernesto-earth/reverse-aging |
| Site-Version | unbekannt (aktueller Live-Deploy nicht geprüft) |
| Site-URL | http://heger.earth/reverse-aging/ (Link auch als .webloc im Ordner) |
| Zuletzt aktualisiert durch | Hermes, im Auftrag Ernestos am 2026-11-06; lokale Nachbesserung der Statusfeldlängen, keine Veröffentlichung |

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
