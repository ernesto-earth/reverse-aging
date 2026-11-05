# Routinen – „Reverse Aging – Routinen für ein starkes Älterwerden“

Website: **http://heger.earth/reverse-aging/**

Der Projektordner `a.5. Projekte/Routinen` ist die einzige Quelle. Das öffentliche GitHub-Repo
`ernesto-earth/reverse-aging` ist sein Spiegel (ohne die lokalen Teile, siehe unten) und veröffentlicht
die Seite automatisch. Keine Abhängigkeit zu Claude oder ChatGPT.

Hinweis: Der frühere Ordner `ReverseAging` wurde am 2026-11-03 hier hineingeführt (E-012/E-013).

## Inhalt

| Pfad | Zweck | im Repo |
|---|---|---|
| `site/content.md` | einziger Textquelltext der Seite (Markdown mit Fußnoten) | ja |
| `site/hub.json` | Aufteilung in sieben Unterseiten, Kurzfassungen, Karten, Übungen, Tests | ja |
| `site/build.mjs`, `styles.css`, `site.js` | Build mit Prüfungen, Aussehen, Seitenwechsel | ja |
| `site/assets/` | Bilder (Morgenroutine, Sketchnote, Workouts) und Schrift | ja |
| `work/` | Erstellungsskripte (A5-PDF, Zeichnungen), Designvorschlag | ja (ohne Bilder und Sicherungen) |
| `.github/workflows/deploy.yml` | baut und lädt bei jedem Push nach heger.earth/reverse-aging hoch | ja |
| `README.md`, `STATUS.md` | diese Anleitung, aktueller Stand | ja |
| `outputs/morgenroutine-a5.pdf` | A5-Morgenroutine zum Ausdrucken | nein (nur lokal) |
| `archiv/`, `Chats/`, `tmp/`, `work/backup-*` | Quellenarchiv, Chat-Kopien, Arbeits- und Sicherungsdateien | nein |

## Seite ändern

1. Texte in `site/content.md`, Kurzfassungen und Seitenaufteilung in `site/hub.json` bearbeiten.
   Jeder `##`-Abschnitt in `content.md` muss in `hub.json` genau einer Seite zugeordnet sein, sonst bricht der Build ab.
   Neue Bilder nach `site/assets/` bzw. `site/assets/workouts/`.
2. Optional lokal prüfen: im Ordner `site` `node build.mjs --assets`, dann `dist/index.html` öffnen.
3. `STATUS.md` aktualisieren.
4. **GitHub Desktop** (Repository „reverse-aging“): Beschreibung eintragen → **Commit to main** → **Push origin**.
5. Nach ca. 1 Minute online. Kontrolle auf github.com/ernesto-earth/reverse-aging unter **Actions**: grüner Haken = online.

## Neu aufsetzen

1. Repo anlegen bzw. klonen, Inhalt dieses Ordners hinein, pushen.
2. FTP-Benutzer im Domaintechnik Control Panel (Modul **FTP**); Startordner = Hauptverzeichnis, sonst Variable `FTP_WEBROOT` = `./`.
3. Secrets (Settings → Secrets and variables → Actions): `FTP_SERVER` (`host28.ssl-net.net`), `FTP_USERNAME`, `FTP_PASSWORD`.
4. Actions → Deploy → **Run workflow**.

## Fehlersuche

- **Build rot:** Die Meldung nennt den Abschnitt, Nachweis oder die Sprungmarke.
- **Upload rot:** Secrets prüfen. **Prüfschritt rot, Upload grün:** `FTP_WEBROOT` oder `.htaccess` prüfen.
- Am Server wird nie gelöscht. heger.earth hat derzeit kein gültiges SSL-Zertifikat, deshalb http.
