# meerwert.ch — Website

Statische Website von **meerwert – kuonen** (biografische Beratung, Bernhard Kuonen).
Stack: **Hugo** + **Sveltia CMS** + **Cloudflare Pages**.

> **README gewählt (nicht separate Doku-Datei):** Es existierte noch keine
> Projektdoku. Die Repo-Autorität und Setup-Infos gehören an die Standardstelle,
> die Entwickler:innen und Tools zuerst öffnen — daher `README.md` im Repo-Root.

## ✅ Gültiges Arbeits-Repository

Dieses Repository ist die **einzige gültige Quelle** für meerwert.ch:

- **Lokaler Pfad:** `/Users/bernhard/Developer/meerwert-kuonen-site`
- **Git-Remote:** `git@github.com:bekuonen/meerwert-kuonen.git`
- **Domain:** https://meerwert.ch

### ⚠️ Nicht verwenden
Es existiert ein **zweites, veraltetes** Meerwert-Repo unter iCloud:

```
~/Library/Mobile Documents/com~apple~CloudDocs/01_Projekte/Kundenprojekte/Tschiffra/meerwert-ch
(Remote: github.com/bekuonen/meerwert-ch)
```

Dieses iCloud/Tschiffra-Repo **nicht** für Entwicklung oder Deployment nutzen —
nur das hier dokumentierte Repo (`meerwert-kuonen`) ist maßgeblich.

> Hinweis: An welches Repo Cloudflare Pages tatsächlich gebunden ist, muss im
> Cloudflare-Dashboard überprüft werden (Pages → Projekt → Settings → Builds &
> deployments → Git). Es muss auf `bekuonen/meerwert-kuonen` zeigen. Diese Datei
> dokumentiert nur die Soll-Vorgabe; an Cloudflare selbst wurde nichts geändert.

## Lokale Entwicklung

```bash
hugo server -D        # Dev-Server mit Drafts
hugo --minify         # Produktions-Build nach public/
```

## Build / Deployment (Cloudflare Pages)

| Einstellung | Wert |
|---|---|
| Build command | `hugo --minify` |
| Build output | `public` |
| Root directory | (leer) |
| `HUGO_VERSION` | `0.124.1` (im Dashboard gesetzt; siehe `cloudflare-build.toml`) |

`cloudflare-build.toml` dient nur als **Referenz/Doku** — die wirksame
Build-Konfiguration liegt im Cloudflare-Dashboard.

**Hugo-Versionshinweis:** Dashboard/Build ist auf **0.124.1** dokumentiert, die
lokale Entwicklung lief beim Audit mit **0.161.1 (extended)**. Bei einem Upgrade
beide Stände synchron halten und einen Build verifizieren. (Cloudflare wurde
nicht angefasst.)

## CMS

- Sveltia CMS unter `/admin/` (`static/admin/`), Login via GitHub.
- Eingebunden über eine **gepinnte Version**: `@sveltia/cms@0.165.0`
  (`static/admin/index.html`) — nicht mehr `@latest` (das zuvor genutzte
  *unscoped* `sveltia-cms@latest` lieferte 404).
- Backend-Repo in `static/admin/config.yml`: `bekuonen/meerwert-kuonen`.
- Auth-Worker: `https://cms-auth.bekuonen.workers.dev`.

## Offen: OG-Image

Die Open-Graph-/Social-Vorschau-Tags (`og:image`) verweisen auf
**`/img/og-image.jpg`** (absolut: `https://meerwert.ch/img/og-image.jpg`).
Dieses Bild **fehlt noch** und muss als Datei hinterlegt werden:

- Pfad: `static/img/og-image.jpg`
- Format: **JPG, 1200×630 px** (Open-Graph-Standard)

## Offen: Portrait (Über-mich)

Die Über-mich-Seite (`layouts/ueber-mich/list.html`) bindet ein Portrait ein,
sobald es vorhanden ist (`{{ if fileExists "static/img/portrait.jpg" }}`).

- Pfad: `static/img/portrait.jpg`
- Verwendung: Über-mich-Seite
- Status: **fehlt noch** — kein geeignetes Bild vorhanden, daher bewusst nicht
  umgesetzt. Sobald die Datei abgelegt ist, erscheint das Portrait automatisch.

Solange die Datei fehlt, zeigen Social-Vorschauen kein Bild (die Tags sind aber
bereits korrekt gesetzt). Es wurde bewusst **kein Platzhalterbild** generiert.

## Kontaktformular

Das Formular (`layouts/kontakt/list.html`) nutzt **Web3Forms**. Der Access Key
wird über den Hugo-Parameter `web3formsKey` in `hugo.toml` gesetzt. Solange er
leer ist, ist der Absende-Button **deaktiviert** (kein versehentlicher Versand).
Zum Aktivieren den Web3Forms-Key in `hugo.toml` → `[params]` → `web3formsKey`
eintragen.
