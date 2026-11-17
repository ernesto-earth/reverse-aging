# CLAUDE.md – Hinweise für Claude Code

Projekt „Reverse Aging – Routinen für ein starkes Älterwerden“, veröffentlicht unter http://heger.earth/reverse-aging/.
Ausführliche Anleitung: `README.md`. Aktueller Stand: `STATUS.md`. Sprache im Projekt: Deutsch.

## Wichtig

- **Das Repo ist öffentlich.** Keine persönlichen Gesundheitsangaben, Namen, Zugangsdaten oder Tokens
  in Dateien, Commits oder Seitentext. `.gitignore` nicht aufweichen (u. a. `Fettstoffwechsel/`, `Chats/`, `archiv/`).
- Jeder Push auf `main`, der `site/**` berührt, veröffentlicht die Seite automatisch (`.github/workflows/deploy.yml`).
- Claude verwaltet Git selbst: Änderungen auf dem Arbeitszweig committen und pushen.
  **Auf `main` (= Deploy nach heger.earth) nur, wenn Ernesto es ausdrücklich sagt** („deploy“, „veröffentlichen“).
- `veroeffentlichen.sh` ist für den Mac (Hermes, E-024), nicht in Cloud-Sitzungen ausführen.

## Deploy in einer Cloud-Sitzung (nur auf Ansage)

1. `cd site && node build.mjs --assets` muss fehlerfrei sein; `STATUS.md` nachziehen und committen.
2. `git fetch origin main`, Arbeitszweig auf `origin/main` bringen (merge, kein Force-Push), dann `git push origin HEAD:main`.
3. Lauf des Workflows `deploy.yml` für genau diesen Commit beobachten (GitHub-MCP `actions_list`, bei Fehler `get_job_logs`).
   Der Workflow prüft selbst die Live-Seite (`deploy-pruefen.mjs`): grüner Lauf = online, Live-Commit stimmt.
   heger.earth ist aus der Cloud-Sitzung nicht direkt erreichbar (nur http, Netzwerkregel); das ist so gewollt.
4. Ernesto Commit, Action-Lauf und Ergebnis melden; Site-Felder in `STATUS.md` beim nächsten Commit nachtragen.
   Fehlgeschlagenen Lauf nicht blind neu starten, sondern Ursache melden.

## Seite bearbeiten

- Text: `site/content.md` (Markdown mit Fußnoten als Nachweise). Aufteilung, Kurzfassungen, Karten, Übungen, Tests: `site/hub.json`.
  Jeder `##`-Abschnitt in `content.md` muss in `hub.json` genau einer Seite zugeordnet sein.
- Bilder nach `site/assets/` bzw. `site/assets/workouts/`.
- Nach jeder Änderung `STATUS.md` nachziehen (Felder in der Tabelle oben, Zeitstempel mit Zeitzone).

## Prüfen

```bash
cd site && node build.mjs --assets
```

Erwartet: `Built dist/index.html (… Seiten, … Nachweise)`; jede Fehlermeldung nennt Abschnitt, Nachweis oder Sprungmarke.
`site/dist/` wird nicht eingecheckt. Test für das Deploy-Prüfskript: `node test-deploy-pruefen.mjs`.
