# Umzug zu cyon – Stand 11. November 2026

Die Umstellung wird vor der noch ausstehenden Datenschutz-Auskunft von cyon vorbereitet. Eine ausschliessliche Bearbeitung in CH/EU ist nicht bestätigt.

- Gültiges Repository bleibt `bekuonen/meerwert-kuonen`.
- Neues Ziel: cyon-Hosting «meerwert», Webroot `public_html/meerwert.ch`.
- Site-Build mit Hugo 0.161.1 erfolgreich.
- Kontaktformular durch direkten E-Mail-Link ersetzt; keine Formspark-Aufrufe mehr.
- Datenschutzerklärung für cyon/Migadu aktualisiert und offene Standortfragen offengelegt.
- Sicherheitsheader in `static/.htaccess`; keine Verzeichnisauflistung, keine externen Skripte oder Form-Submits.
- Das mit Cloudflare/GitHub verbundene CMS unter `static/admin` bleibt als Quellcode erhalten, wird aber nicht auf cyon veröffentlicht. Inhalte vorerst im Repository pflegen und neu bauen.
- Website-Paket auf cyon hochgeladen und entpackt. Vorschau `vyyaxyllao.cyon.link` meldet noch «Domain nicht eingerichtet»; noch keine Live-Freigabe.
- Öffentliche Nameserver weiterhin Cloudflare (`amy.ns.cloudflare.com`, `amir.ns.cloudflare.com`). DNS noch nicht geändert. Die cyon-Zone enthält Standard-Mailwerte und darf nicht ungeprüft aktiviert werden! Vollständige bisherige Zone einschliesslich Migadu MX/SPF/DKIM/DMARC, Nextcloud und weiteren Subdomains vor einer Nameserver-Umstellung sichern und übernehmen.
- HTTPS auf cyon für meerwert.ch/www.meerwert.ch vor produktiver Umschaltung verifizieren. Keine Schutzmechanismen oder DNSSEC blind abschalten.
- Rückfall: unveränderte Cloudflare-Installation und bisherige DNS-Werte bis zur Abnahme erhalten.

## Paket erstellen

```sh
hugo --minify
python scripts/package_cyon.py /absoluter/pfad/meerwert-cyon.zip
```

Nur das generierte Paket entpacken; niemals das Quellrepository oder Zugangsdaten in den Webroot hochladen. Das Installationsarchiv anschliessend ausserhalb des Webroots aufbewahren.

## Bisherige Dokumentation (Cloudflare, vor Umzug)

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

## Technische Korrekturen – 12. November 2026

Vorbereitet und lokal gebaut; Veröffentlichung auf cyon noch ausstehend.

- Social-Vorschaubild 1200×630 aus der vorhandenen Wortmarke, Hintergrund in der bestehenden Website-Farbe.
- www wird dauerhaft auf die Hauptdomain weitergeleitet; alte Danke-Adresse auf Kontakt.
- Ungenutzte Taxonomien und Bestätigungsseite aus Build und Sitemap entfernt.
- Überschriftenhierarchie und Menü-Zuordnung korrigiert.
- Eingebettete Stilattribute in die CSS-Datei verschoben; CSS mit Inhalts-Hash gegen veraltete Browser-Caches.
- Aktueller Hauptzweig (ohne Monatsversprechen) mit der bereits ausgelieferten cyon-Migration zusammengeführt.

## Social-Vorschaubild

`static/img/og-image.jpg`, JPG 1200×630 px, aus der bestehenden SVG-Wortmarke.

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

Das Formular (`layouts/kontakt/list.html`) nutzt **Formspark**
(https://formspark.io, bewährter Stack). Die Formular-ID wird über den
Hugo-Parameter `formsparkId` in `hugo.toml` gesetzt. Solange sie leer ist, ist
der Absende-Button **deaktiviert** (kein versehentlicher Versand); die Seite
zeigt dann einen Hinweis mit der direkten E-Mail-Adresse.

## Fonts & Logo (seit 2026-07)

- **Fonts lokal** unter `static/fonts/` (woff2, latin), eingebunden via
  `@font-face` in `assets/css/main.css` — **kein Google-Fonts-Request** mehr
  (DSG/DSGVO). Quelle: fontsource-Pakete (Space Grotesk 300/400/500,
  Lora 400/500/400italic).
- **Logo:** `static/img/logo.svg` ist die Wortmarke in **Syne Bold als
  Pfade** (keine Font-Abhängigkeit, rendert überall identisch). Der Header
  bindet sie als `<img>` ein. Die übrigen Logo-Varianten (`logo-farbe.svg`,
  `logo-sw-*.svg`) sind noch textbasiert und nur für Print/intern gedacht.
- **Kleinschreibung** ist seit dem Konzept 2026-07 dem Logo vorbehalten;
  Headlines und UI-Elemente in normaler Schreibung.

## Rechtsseiten

`content/impressum.md` und `content/datenschutz.md` (Layout
`_default/single.html`, ohne CTA via `nocta: true`), verlinkt im Footer.
