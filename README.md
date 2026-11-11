# Umzug zu cyon – Stand 11. November 2026

Die Website wurde am 11. November 2026 um ca. 22:19 Uhr (Europe/Zurich) auf cyon umgestellt. Die Datenschutz-Auskunft von cyon steht weiterhin aus. Eine ausschliessliche Bearbeitung in CH/EU ist nicht bestätigt.

- Gültiges Repository bleibt `bekuonen/meerwert-kuonen`.
- Neues Ziel: cyon-Hosting «meerwert», Webroot `public_html/meerwert.ch`.
- Site-Build mit Hugo 0.161.1 erfolgreich.
- Kontaktformular durch direkten E-Mail-Link ersetzt; keine Formspark-Aufrufe mehr.
- Datenschutzerklärung für cyon/Migadu aktualisiert und offene Standortfragen offengelegt.
- Sicherheitsheader in `static/.htaccess`; keine Verzeichnisauflistung, keine externen Skripte oder Form-Submits.
- Das mit Cloudflare/GitHub verbundene CMS unter `static/admin` bleibt als Quellcode erhalten, wird aber nicht auf cyon veröffentlicht. Inhalte vorerst im Repository pflegen und neu bauen.
- Produktiv: cyon-Hosting «meerwert», Server s136.cyon.net, IPv4 149.126.4.145.
- DNS: `meerwert.ch A 149.126.4.145`; `www CNAME meerwert.ch`, beide «Nur DNS». Nameserver bleiben amy.ns.cloudflare.com / amir.ns.cloudflare.com. Cloudflare dient weiterhin als DNS-Anbieter und für bestehende andere Dienste; die Website läuft direkt auf cyon.
- Gültige kostenlose SSL-Zertifikate für meerwert.ch und www.meerwert.ch installiert; beide HTTPS-Adressen mit HTTP 200 und erfolgreicher Zertifikatsprüfung getestet. HTTP wird jeweils per 301 auf HTTPS umgeleitet.
- Migadu MX (10 aspmx1 / 20 aspmx2), SPF, drei DKIM-CNAMEs, DMARC und Verifizierungseintrag unverändert geprüft. Kein Mailversand/-empfang getestet.
- `cloud.meerwert.ch` bleibt CNAME auf `261109kcj7ar5rvqv3g.nextcloud.hosting.zone`; HTTPS leitet zur Nextcloud-Anmeldung weiter. MCP-/Vault-Einträge und übrige DNS-Einträge unverändert.
- Hauptseiten, CSS und Logo am Ziel geprüft; Kontakt mit mailto:hallo@meerwert.ch, keine Formspark-Aufrufe. /admin/ liefert 404.
- Installationsarchiv aus dem Webroot nach `/home/damyvore/sicherung/meerwert-cyon.zip` verschoben; öffentliche Archiv-URL liefert 404.
- Die Preview-Domain vyyaxyllao.cyon.link meldet weiterhin «Domain nicht eingerichtet», obwohl die Zuordnung in my.cyon korrekt angezeigt wird. Für den Betrieb nicht erforderlich; produktive Domains wurden direkt geprüft.
- Rückfall: bisherige Cloudflare-Pages-Installation bleibt erhalten. Vorherige Web-DNS-Werte: Hauptdomain und www jeweils CNAME auf meerwert-kuonen.pages.dev mit Proxy und TTL Auto. Für einen Rückfall beide Werte wiederherstellen.


## Überprüfung und DNS-Vorbereitung am 11. November 2026

**Website auf cyon produktiv; vollständige DNS-Delegation noch nicht erfolgt.**

- Die Änderung aus Commit 3c27c232 (Monatsversprechen entfernt) wurde auch in der veröffentlichten Perspektiven-HTML-Datei auf cyon nachgeführt und öffentlich sowie im Browser geprüft.
- Auf meerwert.ch und www.meerwert.ch: Start, Angebot, Über mich, Perspektiven samt Artikel, Kontakt, Impressum und Datenschutz über HTTPS jeweils HTTP 200 von 149.126.4.145. Kontakt enthält mailto und kein Formular; keine Formspark-Verweise, kein Monatsversprechen. Datenschutz nennt cyon/Migadu.
- Zertifikat für beide Webnamen gültig bis 9. Februar 2027; HTTP jeweils 301 auf HTTPS.
- Vollständiger Cloudflare-BIND-Export (15 Nutzdaten-Records) im Benutzerbrowser gesichert: `~/Library/Mobile Documents/com~apple~CloudDocs/00_Inbox/Chrome-Download/meerwert.ch.txt`. Ursprüngliche cyon-Zone zusätzlich als `cyon-zonedump-meerwert.ch-2026-11-11-223944.json` exportiert.
- Bereinigte Importdatei: `~/Downloads/meerwert-cyon-dns-2026-11-11.txt`. Alle 15 Nutzdaten-Records übernommen; cyon erzeugt zusätzlich SOA und zwei NS. cyon-Standard-MX/SPF/Mail-Autodiscovery nicht aktiviert. E-Mail-Routing auf **Extern** gestellt. Werte direkt auf ns1.cyon.ch und ns2.cyon.ch identisch geprüft.
- Registrar: NOVATREND, angemeldeter Zugang zur Domainverwaltung vorhanden. Registrar bestätigt: keine DS-Records, DNSSEC nicht aktiv; öffentliche Registry-Prüfung entspricht dem.
- Migadu MX/SPF/DKIM/DMARC erhalten, beide MX-Server liefern SMTP-Banner. Tatsächlicher Versand und Empfang wurden nicht getestet.
- Nextcloud unter cloud.meerwert.ch über gültiges HTTPS bis zur Loginseite mit HTTP 200 geprüft.
- **Blocker für Nameserverwechsel:** Der Nutzer hat ausdrücklich bestätigt, dass die MCP-Dienste unverändert bestehen bleiben müssen. mcp-neu verwendet einen Cloudflare-Tunnel; vault/vault-neu verwenden Cloudflare-MCP-Portale. Die bestehenden proxied CNAMEs allein liefern bei einem exklusiven Wechsel zu cyon nicht deren Proxy-Funktion. Cloudflare Partial Setup für externes autoritatives DNS setzt Business/Enterprise voraus (https://developers.cloudflare.com/dns/zone-setups/partial-setup/).
- Daher Nameserver beim Registrar **nicht geändert**: weiterhin amy.ns.cloudflare.com / amir.ns.cloudflare.com. Keine kostenpflichtige Tarifänderung und keine Änderung der MCP-Dienste vorgenommen. Die wichtigen Dienste bleiben auf ihrer bisherigen Konfiguration. Die bei cyon vorbereiteten MCP-CNAME-Werte sind eine Kopie der DNS-Daten, kein verifizierter Ersatz für Cloudflare Proxy/Tunnel.
- Cloudflare-Installation und Zone bleiben für Rückfall und MCP erhalten. Ein Abschluss der vollständigen DNS-Migration darf erst nach einer funktionierenden MCP-Lösung dokumentiert werden.

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
