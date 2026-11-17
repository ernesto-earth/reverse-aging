# CLAUDE.md – Hinweise für Claude Code

Projekt „Reverse Aging – Routinen für ein starkes Älterwerden“, veröffentlicht unter http://heger.earth/reverse-aging/.
Ausführliche Anleitung: `README.md`. Aktueller Stand: `STATUS.md`. Sprache im Projekt: Deutsch.

## Wichtig

- **Das Repo ist öffentlich.** Keine persönlichen Gesundheitsangaben, Namen, Zugangsdaten oder Tokens
  in Dateien, Commits oder Seitentext. `.gitignore` nicht aufweichen (u. a. `Fettstoffwechsel/`, `Chats/`, `archiv/`).
- Jeder Push auf `main`, der `site/**` berührt, veröffentlicht die Seite automatisch (`.github/workflows/deploy.yml`).
  In Cloud-Sitzungen deshalb nur auf dem zugewiesenen Arbeitszweig arbeiten; auf `main` kommt es erst nach Freigabe durch Ernesto.
- `veroeffentlichen.sh` ist für den Mac (Hermes, E-024) gedacht, pusht direkt auf `main` und nicht in Cloud-Sitzungen ausführen.

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
