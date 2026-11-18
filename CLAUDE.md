# reverse-aging – Hinweise für Claude Code

Seite „Reverse Aging – Routinen“ aus `site/`. Antworten und Commits auf Deutsch. Einstieg: `README.md`, Stand: `STATUS.md`.
Vorprod: http://heger.earth/vorprod/reverse-aging/ · Prod: http://heger.earth/reverse-aging/. Prüfen: `cd site && node build.mjs --assets`.

**Öffentlich, ohne Passwort – endgültig (E-036, Ernesto 2026-11-18):** Das Repo `ernesto-earth/reverse-aging` bleibt
public, die Seite (Prod und Vorprod) ist ohne Passwort lesbar. Nicht auf privat stellen, keinen Passwortschutz und keine
solche Rückfrage vorschlagen. Deshalb nur Veröffentlichbares ins Repo; nie einchecken: `Fettstoffwechsel/` (persönliche
Gesundheitsrecherche), PDFs aus Zeitschriften, `Chats/`, `archiv/` – siehe `.gitignore`.

## Git, Vorprod und Prod (E-035, gilt für Claude und Hermes gleich)

Beschluss: `ENTSCHEIDUNGEN.md` im Repo `ernesto-earth/chief-of-staff`, E-035.

- **Einzige Quelle ist dieses Repo.** Was nicht gepusht ist, zählt nicht – auch keine iCloud-Stände.
- **Nur zwei Branches:** `main` (Arbeitsstand, deployt nach `heger.earth/vorprod/<seite>/`) und `prod` (live,
  deployt auf die heutige Adresse). **Keine eigenen Branches** – auch nicht für Claude, auch nicht in
  Cloud-Sitzungen. Kein Force-Push, kein Umschreiben der Historie.
- **Arbeitsablauf:** vor Beginn Arbeitskopie sauber, dann `git pull --rebase`; kleine, fertige Commits mit
  bestandenem Build/Test; sofort auf `main` pushen. Push abgelehnt → `git pull --rebase`, Prüfung wiederholen,
  erneut pushen. Konflikt → abbrechen, nichts erzwingen, Ernesto melden. Nichts Unkommittiertes zurücklassen.
- **Freigabe nach Prod nur auf ausdrückliche Anweisung von Ernesto** (bzw. im freigegebenen Hermes-Auftrag):
  genau den auf Vorprod geprüften Commit vorspulen – `./veroeffentlichen.sh --freigeben <commit>` oder
  `git push origin <commit>:prod`. `prod` nie direkt bearbeiten; Fehler auf `main` korrigieren und neu freigeben.
- Am Mac Studio teilen sich Claude und Hermes die Arbeitskopie in `a.5. Projekte/`: nicht arbeiten, solange ein
  Hermes-Lauf das Projekt beansprucht. Vom MacBook aus wird in `a.5. Projekte/` nichts geschrieben.
- Technisch abgesichert: `.claude/hooks/git-branch-guard.py` (Hook in `.claude/settings.json`) blockiert in jeder
  Claude-Code-Sitzung neue Branches, Push auf andere Branches als main/prod, Force-Push und das Löschen von main/prod.
- Nie Zugangsdaten, Tokens oder Laufzeitdatenbanken ins Repo.
