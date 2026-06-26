# -*- coding: utf-8 -*-
"""
Generator für die Unterseiten des Muyres-Relaunch-Demonstrators.
Erzeugt alle Subpages mit gemeinsamem Chrome (Nav/Menü/Footer/Cookie/Demo identisch
zur Startseite) + SEO/GEO (Meta, OG, Twitter, JSON-LD) + robots.txt/sitemap.xml/llms.txt.
index.html wird NICHT angefasst (Handarbeit). UTF-8 ohne BOM.
"""
import os, io, json

PROJ = os.path.dirname(os.path.abspath(__file__))
ORIG = "https://www.steuerberatung-muyres.de"
PAGES = "https://suak0903.github.io/steuerberatung-muyres"
VER = "50"

NAV = [("kanzlei.html", "Kanzlei", "kanzlei"),
       ("fachgebiete.html", "Fachgebiete", "fachgebiete"),
       ("service.html", "Service", "service"),
       ("steuerberaterwechsel.html", "Steuerberaterwechsel", "steuerberaterwechsel"),
       ("karriere.html", "Karriere", "karriere")]

# ---------------- Structured Data (JSON-LD @graph) ----------------
# Lokales SEO + GEO fuer Steuerberater: vollstaendige NAP, Oeffnungszeiten, Leistungskatalog,
# Team, Mitgliedschaft, Social-Profile. KEINE Geo-Koordinaten (Google geocodiert selbst).
_KANZLEI_ID = ORIG + "/#kanzlei"
_TEAM_LD = [
    ("Peter Muyres", "Steuerberater"),
    ("Doris Franke", "Steuerfachangestellte"),
    ("Claudia Wassenberg", "Steuerfachangestellte"),
    ("Ingrid Wolff", "Steuerfachangestellte"),
    ("Ulrike Rautenberger", "Steuerfachwirtin, Bilanzbuchhalterin"),
]
_SVC_LD = [
    ("Steuerberatung für Unternehmen", "fachgebiete-unternehmen", "Jahresabschluss, Lohnbuchhaltung, betriebliche Steuererklärung und Unternehmensnachfolge."),
    ("Steuerberatung für Privatpersonen", "fachgebiete-privatpersonen", "Einkommensteuererklärung, Prüfung von Steuerbescheiden und Vermögensübertragung."),
    ("Beratung für Existenzgründer und Startups", "fachgebiete-existenzgruender", "Businessplan, Rechtsformwahl, Fördergelder und Liquiditätsplanung."),
    ("Steuerberatung für Freiberufler und Freelancer", "fachgebiete-freiberufler", "Gewinnermittlung, Finanzbuchführung und betriebliche Steuererklärung."),
    ("Steuerberatung für Immobilienbesitzer", "fachgebiete-immobilienbesitzer", "Grundsteuererklärung, Vermietung und Verpachtung, Bewertung und Vermögensübertragung."),
]
ORG = {
    "@type": ["AccountingService", "ProfessionalService", "LocalBusiness"],
    "@id": _KANZLEI_ID,
    "name": "Steuerberatung Muyres",
    "alternateName": "Michael Muyres Steuerberatung",
    "slogan": "Freundlich. Professionell. Nah.",
    "description": "Persönliche Steuerberatung in Mönchengladbach: Einkommensteuer, Jahresabschluss, Lohnbuchhaltung, Grundsteuer und Existenzgründung. Gegründet 2020, direkt am Bunten Garten an der Beethovenstraße.",
    "url": ORIG + "/",
    "image": PAGES + "/media/og-muyres.jpg",
    "logo": PAGES + "/media/logo.svg",
    "telephone": "+4921614950780",
    "faxNumber": "+4921614950789",
    "email": "info@steuerberatung-muyres.de",
    "priceRange": "$$",
    "currenciesAccepted": "EUR",
    "foundingDate": "2020",
    "address": {"@type": "PostalAddress", "streetAddress": "Beethovenstraße 55", "postalCode": "41061",
                "addressLocality": "Mönchengladbach", "addressRegion": "Nordrhein-Westfalen", "addressCountry": "DE"},
    "areaServed": [{"@type": "City", "name": n} for n in
                   ["Mönchengladbach", "Korschenbroich", "Viersen", "Willich", "Jüchen", "Neuss"]],
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "08:30", "closes": "12:30"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "13:30", "closes": "16:30"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "08:30", "closes": "13:00"},
    ],
    "knowsAbout": ["Einkommensteuererklärung", "Jahresabschluss", "Lohnbuchhaltung", "Finanzbuchführung",
                   "Grundsteuererklärung", "Unternehmensnachfolge", "Existenzgründung", "Rechtsformwahl",
                   "Vermögensübertragung", "Steuerberaterwechsel", "DATEV"],
    "knowsLanguage": "de",
    "memberOf": {"@type": "Organization", "name": "Steuerberaterkammer Düsseldorf"},
    "founder": {"@type": "Person", "@id": ORIG + "/#michael-muyres", "name": "Michael Muyres",
                "jobTitle": "Steuerberater B.A.", "worksFor": {"@id": _KANZLEI_ID}},
    "employee": [{"@type": "Person", "name": n, "jobTitle": r, "worksFor": {"@id": _KANZLEI_ID}} for n, r in _TEAM_LD],
    "sameAs": ["https://www.xing.com/pages/steuerberatung-muyres",
               "https://www.linkedin.com/company/steuerberatung-muyres/"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Leistungen der Steuerberatung Muyres",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n,
            "url": ORIG + "/" + s + "/", "description": d, "provider": {"@id": _KANZLEI_ID}}} for n, s, d in _SVC_LD]},
}
WEBSITE = {"@type": "WebSite", "@id": ORIG + "/#website", "url": ORIG + "/",
           "name": "Steuerberatung Muyres", "inLanguage": "de-DE", "publisher": {"@id": _KANZLEI_ID}}

# FAQ: eine Quelle fuer sichtbare Sektion (faq_section) UND FAQPage-Schema (wortgleich).
# Faktentreu aus den Seiteninhalten abgeleitet.
FAQ_DATA = [
    ("Was kostet ein Erstgespräch?",
     "Das Erstgespräch ist kostenfrei. Sie können es als Telefonberatung, als Onlinecoaching oder als persönlichen Termin vor Ort wahrnehmen."),
    ("Für wen ist die Steuerberatung Muyres da?",
     "Wir beraten Unternehmen, Privatpersonen, Existenzgründer und Startups, Freiberufler und Freelancer sowie Immobilienbesitzer."),
    ("Wie läuft ein Steuerberaterwechsel ab?",
     "Ein Wechsel zu uns ist unkompliziert. Sie kündigen Ihrem bisherigen Berater, wir übernehmen auf Wunsch die weitere Kommunikation und das Anfordern Ihrer Unterlagen."),
    ("Arbeiten Sie digital?",
     "Ja. Als DATEV Digitale Kanzlei bieten wir digitale Zusammenarbeit, Onlinecoaching und ortsunabhängige Beratung."),
    ("Wo finde ich die Kanzlei?",
     "Unsere Kanzlei liegt am Bunten Garten an der Beethovenstraße 55 in 41061 Mönchengladbach."),
    ("Welche Bürozeiten haben Sie?",
     "Montag bis Donnerstag von 8:30 bis 12:30 Uhr und von 13:30 bis 16:30 Uhr, freitags von 8:30 bis 13:00 Uhr."),
]
FAQ_BY_SLUG = {"kontakt": FAQ_DATA}


def jsonld(title, desc, canon, slug, og):
    page = {"@type": "WebPage", "@id": canon + "#webpage", "url": canon,
            "name": title + " | Steuerberatung Muyres", "description": desc,
            "isPartOf": {"@id": ORIG + "/#website"}, "about": {"@id": _KANZLEI_ID},
            "primaryImageOfPage": PAGES + "/media/og-" + og + ".jpg", "inLanguage": "de-DE"}
    graph = [ORG, WEBSITE, page]
    if slug:  # Breadcrumb auf allen Unterseiten (nicht Startseite)
        items = [{"@type": "ListItem", "position": 1, "name": "Start", "item": ORIG + "/"}]
        if slug.startswith("fachgebiete-"):
            items.append({"@type": "ListItem", "position": 2, "name": "Fachgebiete", "item": ORIG + "/fachgebiete/"})
            items.append({"@type": "ListItem", "position": 3, "name": title, "item": canon})
        else:
            items.append({"@type": "ListItem", "position": 2, "name": title, "item": canon})
        page["breadcrumb"] = {"@id": canon + "#breadcrumb"}
        graph.append({"@type": "BreadcrumbList", "@id": canon + "#breadcrumb", "itemListElement": items})
    if slug in FAQ_BY_SLUG:  # FAQPage wortgleich zur sichtbaren FAQ-Sektion
        graph.append({"@type": "FAQPage", "@id": canon + "#faq", "isPartOf": {"@id": canon + "#webpage"},
            "mainEntity": [{"@type": "Question", "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ_BY_SLUG[slug]]})
    data = {"@context": "https://schema.org", "@graph": graph}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + '</script>'


MSOCIAL = (
    '    <div class="nav__msocial">\n'
    '      <a href="weiter.html?ziel=https://www.xing.com/pages/steuerberatung-muyres" aria-label="Steuerberatung Muyres auf Xing"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.188 0c-.517 0-.741.325-.927.66 0 0-7.455 13.224-7.702 13.657.015.024 4.919 9.023 4.919 9.023.17.308.436.66.967.66h3.454c.211 0 .375-.078.463-.22.089-.151.089-.346-.009-.536l-4.879-8.916c-.004-.006-.004-.016 0-.022L22.139.756c.095-.191.097-.387.006-.535C22.056.078 21.894 0 21.686 0h-3.498zM3.648 4.74c-.211 0-.385.074-.473.216-.09.149-.078.339.02.531l2.34 4.05c.004.01.004.016 0 .021L1.86 16.051c-.099.188-.093.381 0 .529.085.142.239.234.45.234h3.461c.518 0 .766-.348.945-.667l3.734-6.609-2.378-4.155c-.172-.308-.434-.659-.962-.659H3.648v.016z"/></svg></a>\n'
    '      <a href="weiter.html?ziel=https://www.linkedin.com/company/steuerberatung-muyres/" aria-label="Steuerberatung Muyres auf LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/></svg></a>\n'
    '    </div>\n')


def head(title, desc, slug, og="muyres"):
    canon = ORIG + "/" + (slug + "/" if slug else "")
    ogimg = PAGES + "/media/og-" + og + ".jpg"
    return (
        '<!doctype html>\n<html lang="de" class="no-js">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<link rel="icon" href="favicon.ico" sizes="any">\n'
        '<link rel="icon" type="image/png" sizes="32x32" href="media/favicon-32.png">\n'
        '<link rel="apple-touch-icon" href="media/favicon-180.png">\n'
        '<title>' + title + ' | Steuerberatung Muyres</title>\n'
        '<meta name="description" content="' + desc + '">\n'
        '<meta name="robots" content="noindex, follow">\n'
        '<link rel="canonical" href="' + canon + '">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:locale" content="de_DE">\n'
        '<meta property="og:site_name" content="Steuerberatung Muyres">\n'
        '<meta property="og:title" content="' + title + ' | Steuerberatung Muyres">\n'
        '<meta property="og:description" content="' + desc + '">\n'
        '<meta property="og:url" content="' + canon + '">\n'
        '<meta property="og:image" content="' + ogimg + '">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="' + title + ' | Steuerberatung Muyres">\n'
        '<meta name="twitter:description" content="' + desc + '">\n'
        '<meta name="twitter:image" content="' + ogimg + '">\n'
        + jsonld(title, desc, canon, slug, og) + '\n'
        '<script>document.documentElement.className=document.documentElement.className.replace(\'no-js\',\'has-js\');</script>\n'
        '<link rel="preload" href="font/archivo-700.woff2" as="font" type="font/woff2" crossorigin>\n'
        '<link rel="preload" href="font/archivo-400.woff2" as="font" type="font/woff2" crossorigin>\n'
        '<link rel="stylesheet" href="css/site.css?v=' + VER + '">\n'
        '</head>\n<body>\n'
        '<a class="skip" href="#main">Zum Inhalt springen</a>\n')


def nav(active):
    links = ""
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active else ''
        links += '      <a href="' + href + '"' + cur + '>' + label + '</a>\n'
    mlinks = ""
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active else ''
        mlinks += '  <a href="' + href + '"' + cur + '>' + label + '</a>\n'
    return (
        '<header class="nav" id="nav">\n  <div class="nav__inner">\n'
        '    <a class="nav__logo" href="index.html" aria-label="Startseite Steuerberatung Muyres">\n'
        '      <img class="logo-light" src="media/logo-white.svg" alt="Michael Muyres Steuerberatung" width="200" height="50">\n'
        '      <img class="logo-dark" src="media/logo.svg" alt="Michael Muyres Steuerberatung" width="200" height="50">\n'
        '    </a>\n'
        '    <nav class="nav__links" aria-label="Hauptnavigation">\n' + links + '    </nav>\n'
        '    <a class="btn btn--outline nav__cta" href="kontakt.html">Erstgespräch</a>\n'
        + MSOCIAL +
        '    <a class="nav__mcontact" href="kontakt.html">Kontakt</a>\n'
        '    <button class="nav__burger" id="burger" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span><span></span></button>\n'
        '  </div>\n</header>\n\n'
        '<nav class="mmenu" id="mmenu" aria-label="Mobile Navigation" inert>\n' + mlinks + '</nav>\n'
        '<div class="mmenu-backdrop" id="mbackdrop" hidden></div>\n\n'
        '<main id="main">\n')


FOOTER = (
'<footer class="footer">\n  <div class="container">\n    <div class="footer__grid">\n'
'      <div class="footer__brandcol">\n'
'        <div class="footer__logo"><img src="media/logo-white.svg" alt="Steuerberatung Muyres" width="220" height="62"></div>\n'
'        <p class="footer__brand">Ihre Steuerberatung Muyres.</p>\n'
'        <p class="footer__claim">Freundlich. Professionell. Nah.</p>\n'
'        <div class="social">\n'
'          <a href="weiter.html?ziel=https://www.xing.com/pages/steuerberatung-muyres" aria-label="Steuerberatung Muyres auf Xing">\n'
'            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.188 0c-.517 0-.741.325-.927.66 0 0-7.455 13.224-7.702 13.657.015.024 4.919 9.023 4.919 9.023.17.308.436.66.967.66h3.454c.211 0 .375-.078.463-.22.089-.151.089-.346-.009-.536l-4.879-8.916c-.004-.006-.004-.016 0-.022L22.139.756c.095-.191.097-.387.006-.535C22.056.078 21.894 0 21.686 0h-3.498zM3.648 4.74c-.211 0-.385.074-.473.216-.09.149-.078.339.02.531l2.34 4.05c.004.01.004.016 0 .021L1.86 16.051c-.099.188-.093.381 0 .529.085.142.239.234.45.234h3.461c.518 0 .766-.348.945-.667l3.734-6.609-2.378-4.155c-.172-.308-.434-.659-.962-.659H3.648v.016z"/></svg>\n'
'          </a>\n'
'          <a href="weiter.html?ziel=https://www.linkedin.com/company/steuerberatung-muyres/" aria-label="Steuerberatung Muyres auf LinkedIn">\n'
'            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/></svg>\n'
'          </a>\n        </div>\n      </div>\n'
'      <div class="footer__divider" aria-hidden="true"></div>\n'
'      <div>\n        <h4>Anschrift</h4>\n        <div class="footer__row">\n'
'          <span>Beethovenstraße 55</span>\n          <span>41061 Mönchengladbach</span>\n        </div>\n      </div>\n'
'      <div>\n        <h4>Kontakt</h4>\n        <div class="footer__row">\n'
'          <a href="tel:+4921614950780">Telefon: 02161 / 49 50 78 - 0</a>\n'
'          <span>Telefax: 02161 / 49 50 78 - 9</span>\n'
'          <a href="mailto:info@steuerberatung-muyres.de">info@steuerberatung-muyres.de</a>\n        </div>\n      </div>\n    </div>\n'
'    <div class="footer__bottom">\n'
'      <span>Relaunch-Entwurf, erstellt von Dr.-Ing. Suat Akyol. Kein offizieller Auftritt der Kanzlei.</span>\n'
'      <span><a href="impressum.html">Impressum</a> &nbsp;|&nbsp; <a href="datenschutz.html">Datenschutz</a> &nbsp;|&nbsp; <a href="#" id="cookieReopen">Cookies</a> &nbsp;|&nbsp; <a href="hinweise.html">Über diesen Entwurf</a></span>\n    </div>\n  </div>\n</footer>\n')

TAIL = (
'<div class="cookie hidden" id="cookie" role="dialog" aria-label="Cookie-Hinweis" aria-modal="false">\n'
'  <p class="cookie__text"><strong>Wir verwenden Cookies.</strong> Wir nutzen Cookies, um Ihnen die bestmögliche Erfahrung auf unserer Website zu bieten. Mehr dazu in der <a href="datenschutz.html">Datenschutzerklärung</a>.</p>\n'
'  <div class="cookie__actions">\n'
'    <button class="btn btn--quiet btn--mini" id="cookieDecline">Nur notwendige</button>\n'
'    <button class="btn btn--primary btn--mini" id="cookieAccept">Alle akzeptieren</button>\n  </div>\n</div>\n\n'
'<div class="demobar hidden" id="demobar" role="note">\n'
'  <span><strong>Redesign-Entwurf.</strong> <span class="hide-sm">Kein offizieller Auftritt der Steuerberatung Muyres.</span></span>\n'
'  <a href="hinweise.html">Mehr dazu</a>\n'
'  <button class="demobar__close" id="democlose" aria-label="Hinweis schließen">&times;</button>\n</div>\n\n'
'<script src="js/site.js?v=' + VER + '"></script>\n</body>\n</html>\n')


def subhero(crumb, title, lead, bg=None, accent=''):
    bgdiv = ('  <div class="subhero__bg" id="subheroBg" style="background-image:url(media/header/' + bg + '.webp)"></div>\n') if bg else ''
    c = '<section class="subhero">\n' + bgdiv + '  <div class="container">\n'
    c += '    <p class="crumb"><a href="index.html">Start</a> &nbsp;/&nbsp; ' + crumb + '</p>\n'
    h = title.replace(accent, '<span class="accent">' + accent + '</span>', 1) if accent and accent in title else title
    c += '    <h1>' + h + '</h1>\n'
    c += '    <div class="subhero__rule"></div>\n'
    if lead:
        c += '    <p>' + lead + '</p>\n'
    c += '  </div>\n</section>\n'
    return c

FG_ORDER = [("unternehmen", "Unternehmen"), ("privatpersonen", "Privatpersonen"),
            ("existenzgruender", "Existenzgründer & Startups"), ("freiberufler", "Freiberufler & Freelancer"),
            ("immobilienbesitzer", "Immobilienbesitzer")]
# Fachgebiete als Fortsetzung der Breadcrumb-Zeile (Suat-Wunsch 23.06.)
FG_CRUMB = ' &nbsp;/&nbsp; '.join('<a href="fachgebiete-%s.html">%s</a>' % (k, l) for k, l in FG_ORDER)


def cta_band(light=True):
    sec = "section--mist" if light else "section--navy"
    sec2 = "btn--outline" if light else "btn--ghost"
    return (
'  <section class="section ' + sec + '">\n    <div class="container">\n      <div class="ctaband">\n'
'        <div class="reveal">\n          <p class="eyebrow">Kostenfreies Erstgespräch</p>\n'
'          <h2 class="h2">Wir freuen uns auf Sie.</h2>\n'
'          <p class="lead">Melden Sie sich gleich bei uns und vereinbaren Sie ein kostenfreies Erstgespräch als Telefonberatung, Onlinecoaching oder persönlichen Termin vor Ort.</p>\n        </div>\n'
'        <div class="ctaband__actions reveal">\n          <a class="btn btn--primary" href="tel:+4921614950780">02161 / 49 50 78 - 0</a>\n'
'          <a class="btn ' + sec2 + '" href="kontakt.html">Termin anfragen</a>\n        </div>\n      </div>\n    </div>\n  </section>\n')


def zitat(text):
    return ('  <section class="section">\n    <div class="container">\n      <figure class="zitat reveal">\n'
            '        <blockquote>' + text + '</blockquote>\n'
            '        <figcaption>Ludwig van Beethoven (1770 - 1827)</figcaption>\n      </figure>\n    </div>\n  </section>\n')


def leistungen(title, items):
    c = '  <section class="section">\n    <div class="container">\n      <div class="section-intro reveal">\n'
    c += '        <p class="eyebrow">Leistungsspektrum</p>\n        <h2 class="h2">' + title + '</h2>\n      </div>\n'
    c += '      <ul class="llist stagger reveal">\n'
    for it in items:
        c += '        <li>' + it + '</li>\n'
    c += '      </ul>\n    </div>\n  </section>\n'
    return c


def pledges_section():
    return (
'  <section class="section section--stone">\n    <div class="container">\n'
'      <div class="pledges stagger reveal">\n'
'        <div class="pledge"><h3>Kompetente Beratung auf Augenhöhe</h3></div>\n'
'        <div class="pledge"><h3>Volle Kostentransparenz</h3></div>\n'
'        <div class="pledge"><h3>Service über den Tellerrand hinaus</h3></div>\n      </div>\n    </div>\n  </section>\n')


def faq_section(items, eyebrow="Häufige Fragen", h2="Gut zu wissen."):
    c = '  <section class="section section--stone">\n    <div class="container">\n'
    c += '      <div class="section-intro reveal"><p class="eyebrow">' + eyebrow + '</p><h2 class="h2">' + h2 + '</h2></div>\n'
    c += '      <div class="faq reveal">\n'
    for q, a in items:
        c += '        <details class="faq__item"><summary>' + q + '</summary><div class="faq__a"><p>' + a + '</p></div></details>\n'
    c += '      </div>\n    </div>\n  </section>\n'
    return c


def write(slug, title, desc, active, body, og="muyres"):
    full = head(title, desc, slug if slug != "index" else "", og) + nav(active) + body + '\n</main>\n\n' + FOOTER + TAIL
    path = os.path.join(PROJ, slug + ".html")
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(full)
    return slug + ".html"


# ---------------- Fachgebiete ----------------
FG = {
 "unternehmen": ("Unternehmen", "Steuerberatung für Unternehmen in Mönchengladbach: Jahresabschluss, Lohnbuchhaltung, betriebliche Steuererklärung und laufende Beratung.",
   "Gerade als Unternehmen gibt es im Geschäftsalltag viele Steuerthemen zu beachten. Ob Steuerplanung, Rechnungswesen oder Unternehmensberatung: Wir stehen als Partner an Ihrer Seite und entwickeln gemeinsam eine maßgeschneiderte Lösung für Ihr Unternehmen.",
   ["Jahresabschluss", "Betriebliche Steuererklärung", "Begleitung von Unternehmenskäufen (Asset- oder Share Deal)", "Finanzbuchführung und Lohnbuchhaltung", "Unternehmensnachfolge"]),
 "privatpersonen": ("Privatpersonen", "Steuerberatung für Privatpersonen: Einkommensteuererklärung, Prüfung von Steuerbescheiden und Vermögensübertragung.",
   "Von der Steuererklärung über Werbungskosten bis zum Rechtsbehelfsverfahren: Im Steuerrecht wird man als Privatperson mit vielen Themen konfrontiert. Wir helfen Ihnen, den Überblick zu bewahren, und ermitteln gezielt Ihr persönliches Steuersparpotenzial.",
   ["Einkommensteuererklärung", "Besteuerung sonstiger Einkünfte, etwa Renten- und Pensionsbezüge", "Prüfung von Steuerbescheiden", "Vermögensübertragung (Erbschaftsteuer und Schenkungsteuer)"]),
 "existenzgruender": ("Existenzgründer & Startups", "Steuerberatung für Existenzgründer und Startups: Businessplan, Rechtsformwahl, Fördergelder und Liquiditätsplanung.",
   "Sie sind Jungunternehmer oder planen ein Startup und benötigen steuerliche Hilfe bei den ersten Schritten? Wir unterstützen Sie bei Finanzierungsanfragen und Bankgesprächen und entwickeln gemeinsam ein Businesskonzept sowie eine Rentabilitätsvorschau.",
   ["Businessplan", "Liquiditätsplanung", "Beantragung von Fördergeldern, etwa Gründungszuschuss", "Beratung zur Rechtsformwahl", "Jahresabschluss"]),
 "freiberufler": ("Freiberufler & Freelancer", "Steuerberatung für Freiberufler und Freelancer: Gewinnermittlung, Finanzbuchführung und betriebliche Steuererklärung.",
   "Sie arbeiten als Selbstständiger und benötigen Hilfe bei Ihren Steuerthemen? Wir analysieren Ihre Ist-Situation und stellen gemeinsam die richtigen Weichen für Ihre steuerliche Zukunft.",
   ["Betriebliche Steuererklärung", "Erstellung von Gewinnermittlungen", "Finanzbuchführung"]),
 "immobilienbesitzer": ("Immobilienbesitzer", "Steuerberatung für Immobilienbesitzer: Grundsteuererklärung, Vermietung und Verpachtung, Bewertung und Vermögensübertragung.",
   "Der Kauf einer Immobilie ist eine Investition in die Zukunft, bringt aber viele steuerliche Fragen mit sich. Wir beraten Sie umfassend zu allen steuerlichen Aspekten rund um Ihre Immobilie und helfen, Ihre Steuerlast nachhaltig zu senken.",
   ["Grundsteuererklärung", "Optionsbesteuerung für Umsatzsteuer", "Bewertung von Grundstücken", "Vermietung und Verpachtung", "Vermögensübertragung (Erbschaftsteuer und Schenkungsteuer)"]),
}
FG_ICON = {"unternehmen":"icon-unternehmen","privatpersonen":"icon-privatpersonen","existenzgruender":"icon-startups","freiberufler":"icon-freelancer","immobilienbesitzer":"icon-immobilienbesitzer"}

for key,(t,desc,lead,items) in FG.items():
    body = subhero('<a href="fachgebiete.html">Fachgebiete</a> &nbsp;/&nbsp; ' + t, "Steuerberater für " + t, lead, "fachgebiete-" + key, accent=t)
    body += leistungen("Beispiele aus unserem Leistungsspektrum.", items)
    body += pledges_section()
    body += cta_band()
    write("fachgebiete-" + key, "Steuerberater " + t, desc, "fachgebiete", body, "fachgebiete-" + key)

# Fachgebiete-Übersicht
ov = subhero("Fachgebiete &nbsp;/&nbsp; " + FG_CRUMB, "Wir verstehen uns als Partner an Ihrer Seite.",
   "Ob als Unternehmer, Immobilienbesitzer oder Privatperson: Bei einem unverbindlichen Erstgespräch lernen wir uns kennen und besprechen Ihre steuerlichen Ziele und Wünsche.", "fachgebiete-unternehmen", accent="an Ihrer Seite.")
ov += '  <section class="section">\n    <div class="container">\n      <div class="fields fields--5 stagger reveal">\n'
for key,label in FG_ORDER:
    ov += ('        <a class="field" href="fachgebiete-' + key + '.html">\n'
           '          <span class="field__ic"><img src="media/' + FG_ICON[key] + '.svg" alt=""></span>\n'
           '          <h3>' + label + '</h3>\n'
           '          <span class="field__more"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>\n        </a>\n')
ov += '      </div>\n    </div>\n  </section>\n'
ov += cta_band()
write("fachgebiete", "Fachgebiete", "Unsere Fachgebiete: Steuerberatung für Unternehmen, Privatpersonen, Existenzgründer, Freiberufler und Immobilienbesitzer in Mönchengladbach.", "fachgebiete", ov, "fachgebiete-unternehmen")

# ---------------- Kanzlei (mit Team) ----------------
TEAM = [
 ("michael-muyres-steuerberater-kanzlei-muyres", "Michael Muyres", "Steuerberater B.A."),
 ("steuerberatung-peter-muyres", "Peter Muyres", "Steuerberater"),
 ("2-muyres-steuerberatung-team-fr-franke", "Doris Franke", "Steuerfachangestellte"),
 ("3-muyres-steuerberatung-team-fr-wassenberg", "Claudia Wassenberg", "Steuerfachangestellte"),
 ("4-muyres-steuerberatung-team-fr-wolff", "Ingrid Wolff", "Steuerfachangestellte"),
 ("5-muyres-steuerberatung-team-fr-rautenberger", "Ulrike Rautenberger", "Steuerfachwirtin, Bilanzbuchhalterin"),
]
kb = subhero("Kanzlei", "Unser Steuerbüro.",
   "Gegründet 2020 von Michael Muyres, liegt unsere Steuerkanzlei heute direkt am Bunten Garten an der Beethovenstraße. Als moderne Kanzlei sind wir das Bindeglied zwischen klassischer Steuerberatung und aktuellen Steuerthemen.", "kanzlei", accent="Steuerbüro.")
# Werdegang (Foto + Text)
kb += ('  <section class="section section--stone">\n    <div class="container">\n      <div class="split">\n'
'        <div class="split__media reveal"><img src="media/team/muyres-steuerberatung-michael-muyres-randlos.webp" alt="Michael Muyres, Steuerberater"></div>\n'
'        <div class="prose reveal">\n          <p class="eyebrow">Michael Muyres</p>\n          <h2 class="h2">Mein Weg zur Steuerberatung.</h2>\n'
'          <p>Mein Weg zur Steuerberatung führte über Umwege: 2003 startete ich meine berufliche Laufbahn bei einer namhaften Krankenkasse in Düsseldorf, merkte jedoch früh, dass mich der Bereich der gesetzlichen Sozialversicherung nicht erfüllte.</p>\n'
'          <p>Das Steuerberater-Gen liegt mir im Blut. Geprägt von der Arbeit meines Vaters heuerte ich bei der Sozietät Keller & Muyres an. Ausbildung und berufsbegleitendes Studium verhalfen mir zu einer Anstellung in einer renommierten Wirtschaftsprüfungsgesellschaft aus dem Profisportbereich, in der ich 2019 zum Prokuristen bestellt wurde.</p>\n'
'          <p>Vor einigen Jahren habe ich den nächsten Schritt getan und mich mit meiner eigenen Steuerkanzlei in meiner Heimatstadt Mönchengladbach selbstständig gemacht. Durch meine über 15-jährige Erfahrung bieten mein Team und ich Ihnen heute professionelle Steuerberatung, so individuell wie Sie.</p>\n        </div>\n      </div>\n    </div>\n  </section>\n')
# Team-Grid
kb += '  <section class="section">\n    <div class="container">\n      <div class="section-intro reveal">\n        <p class="eyebrow">Unser Team</p>\n        <h2 class="h2">Menschen, die für Steuern brennen.</h2>\n      </div>\n      <div class="team stagger reveal">\n'
for img, name, role in TEAM:
    kb += ('        <figure class="tcard">\n          <div class="tcard__photo"><img src="media/team/' + img + '.webp" alt="' + name + '"></div>\n'
           '          <h3>' + name + '</h3>\n          <p>' + role + '</p>\n        </figure>\n')
kb += '      </div>\n    </div>\n  </section>\n'
# Kooperationspartner
kb += ('  <section class="section section--stone">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p class="eyebrow">Kooperationspartner</p>\n        <h2 class="h2">Beste Beratung Hand in Hand.</h2>\n'
'        <p>Gemeinsam mit unserem Kooperationspartner, dem <a href="weiter.html?ziel=https://www.steuerberatungneumann.de/">Steuerbüro Lars Neumann</a>, decken wir ein breites Fachspektrum ab und können auf Ihre Steuerfragen persönlich und individuell eingehen.</p>\n'
'        <p>Als Steuerberater lebt und arbeitet Lars Neumann in Düsseldorf. Seine berufliche Laufbahn startete er bei einer Big4-Gesellschaft aus dem Steuerbereich. Neben der Führung seiner Kanzlei ist er als Gesellschafter bei einer Wirtschaftsprüfungsgesellschaft tätig, die unter anderem im Bereich Eishockey, Handball und Fußball agiert. Auch privat stehen Lars Neumann und Michael Muyres regelmäßig in engem Kontakt. So erhalten Sie zu jeder Zeit beste Beratung Hand in Hand.</p>\n'
'        <p>Die Schwerpunkte unserer Zusammenarbeit sind unter anderem der <a href="fachgebiete-unternehmen.html">Jahresabschluss für Unternehmen</a>, die <a href="fachgebiete-immobilienbesitzer.html">Grundsteuererklärung für Immobilienbesitzer</a>, die <a href="fachgebiete-existenzgruender.html">Gründungsberatung für Existenzgründer und Startups</a> oder auch die professionelle Beratung zur <a href="fachgebiete-privatpersonen.html">Einkommensteuererklärung für Privatpersonen</a>.</p>\n      </div>\n    </div>\n  </section>\n')
kb += ('  <section class="section">\n    <div class="container">\n'
'      <div class="section-intro reveal"><p class="eyebrow">Mitgliedschaften und Partner</p><h2 class="h2">Geprüft und gut vernetzt.</h2></div>\n'
'      <div class="partners reveal">\n'
'        <figure><img src="media/partner/ihr-steuerberater.svg" alt="Ihr Steuerberater: unabhängig, zuverlässig, vorausschauend"></figure>\n'
'        <figure><img src="media/partner/stbk.webp" alt="Steuerberaterkammer Düsseldorf"></figure>\n'
'        <figure><img src="media/partner/datev.svg" alt="DATEV Digitale Kanzlei 2022"></figure>\n'
'        <figure><img src="media/partner/lars-neumann.webp" alt="Steuerbüro Lars Neumann"></figure>\n'
'      </div>\n    </div>\n  </section>\n')
kb += cta_band()
write("kanzlei", "Kanzlei", "Die Steuerkanzlei Muyres in Mönchengladbach: gegründet 2020 von Michael Muyres, am Bunten Garten. Lernen Sie unser Team kennen.", "kanzlei", kb, "kanzlei")

# ---------------- Service ----------------
DOWN = ["Checkliste Einkommensteuer", "Fragebogen Sofortmeldung", "Personalfragebogen Allgemein",
        "Personalfragebogen Auszubildende", "Personalfragebogen Minijob", "Vorlage zur Dokumentation der täglichen Arbeitszeit"]
sb = subhero("Service", "Unsere Services.", "Hier finden Sie nützliche Dokumente und Vorlagen rund um das Thema Steuern.", "service", accent="Services.")
sb += '  <section class="section">\n    <div class="container">\n      <div class="section-intro reveal">\n        <p class="eyebrow">Downloads</p>\n        <h2 class="h2">Dokumente und Vorlagen.</h2>\n        <p class="lead">Im Original stehen diese Vorlagen als Download bereit. In diesem Entwurf sind die Dateien nicht hinterlegt.</p>\n      </div>\n      <ul class="llist stagger reveal">\n'
for d in DOWN:
    sb += '        <li>' + d + '</li>\n'
sb += '      </ul>\n    </div>\n  </section>\n'
sb += cta_band()
write("service", "Service", "Nützliche Dokumente und Vorlagen der Steuerberatung Muyres: Checklisten, Personalfragebogen und mehr.", "service", sb, "service")

# ---------------- Kontakt ----------------
kc = subhero("Kontakt", "Kontakt.",
   "Ob als Privatperson, Unternehmer oder Selbstständiger: Bei uns erhalten Sie eine kompetente Beratung, bei der wir individuell auf Sie und Ihre Wünsche eingehen.", "kontakt")
kc += ('  <section class="section">\n    <div class="container">\n      <div class="split">\n'
'        <div class="prose reveal">\n          <p class="eyebrow">So erreichen Sie uns</p>\n          <h2 class="h2">Wir melden uns umgehend zurück.</h2>\n'
'          <div class="contactlist">\n'
'            <a href="tel:+4921614950780"><img class="ic" src="media/icon-phone-bx.svg" alt="">02161 / 49 50 78 - 0</a>\n'
'            <a href="mailto:info@steuerberatung-muyres.de"><img class="ic" src="media/icon-envelope-bx.svg" alt="">info@steuerberatung-muyres.de</a>\n'
'            <span><img class="ic" src="media/icon-calendar-bx.svg" alt="">Beethovenstraße 55, 41061 Mönchengladbach</span>\n          </div>\n'
'          <p class="hours">Montag bis Donnerstag: 8:30 - 12:30 und 13:30 - 16:30 Uhr<br>Freitag: 8:30 - 13:00 Uhr<br>Telefax: 02161 / 49 50 78 - 9</p>\n        </div>\n'
'        <form class="cform reveal" onsubmit="return false">\n'
'          <p class="cform__note">Demonstrator: Dieses Formular versendet keine Daten.</p>\n'
'          <label>Name<input type="text" name="name" autocomplete="name"></label>\n'
'          <label>E-Mail<input type="email" name="email" autocomplete="email"></label>\n'
'          <label>Nachricht<textarea name="nachricht" rows="4"></textarea></label>\n'
'          <button class="btn btn--primary" type="submit">Absenden</button>\n        </form>\n      </div>\n    </div>\n  </section>\n')
kc += faq_section(FAQ_DATA)
# Google-Maps consent-gated (TTDSG): iframe laedt erst nach Einwilligung (Klick oder Cookie "alle").
kc += ('  <section class="mapwrap" aria-label="Standort">\n'
'    <div class="mapconsent" id="mapConsent">\n'
'      <div class="mapconsent__box">\n'
'        <p class="mapconsent__t">Standort auf Google Maps</p>\n'
'        <p class="mapconsent__d">Beim Laden der Karte werden Daten an Google übertragen. Näheres in der <a href="datenschutz.html">Datenschutzerklärung</a>.</p>\n'
'        <button class="btn btn--primary" id="mapLoad" type="button">Karte laden</button>\n'
'        <label class="mapconsent__remember"><input type="checkbox" id="mapRemember"> Künftig automatisch laden</label>\n'
'      </div>\n    </div>\n'
'    <iframe id="mapFrame" title="Standort der Steuerberatung Muyres, Beethovenstraße 55, Mönchengladbach" loading="lazy" referrerpolicy="no-referrer-when-downgrade"\n'
'      data-src="https://maps.google.com/maps?q=Beethovenstra%C3%9Fe%2055%2C%2041061%20M%C3%B6nchengladbach&output=embed"></iframe>\n  </section>\n')
write("kontakt", "Kontakt", "Kontakt zur Steuerberatung Muyres in Mönchengladbach: Telefon, E-Mail, Anschrift und Bürozeiten.", "kontakt", kc, "kontakt")

# ---------------- Steuerberaterwechsel ----------------
wb = subhero("Steuerberaterwechsel", "Steuerberaterwechsel.",
   "Sie sind mit Ihrem Steuerberater unzufrieden, fühlen sich nicht gut beraten oder warten ewig auf Rückrufe? Die Gründe für einen Wechsel können vielfältig sein.", "steuerberaterwechsel")
wb += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p>Für uns sind eine ehrliche und transparente Beratung die wichtigste Basis für eine erfolgreiche Zusammenarbeit. Unser Anspruch ist es, Sie bei allen steuerlichen Anfragen jederzeit kompetent zu unterstützen, damit Sie Ihre Steuerangelegenheiten in guten Händen wissen.</p>\n'
'        <p>Nutzen Sie die Chance, uns bei einem unverbindlichen Erstgespräch kennenzulernen. Einen schnellen Überblick über die wichtigsten Punkte zum Wechsel finden Sie in unserer <a href="service.html">Checkliste Steuerberaterwechsel</a>.</p>\n      </div>\n    </div>\n  </section>\n')
wb += zitat("Ein gutes Wort findet gut statt.")
wb += cta_band()
write("steuerberaterwechsel", "Steuerberaterwechsel", "Steuerberater wechseln leicht gemacht: ehrliche, transparente Beratung bei der Steuerberatung Muyres in Mönchengladbach.", "steuerberaterwechsel", wb, "steuerberaterwechsel")

# ---------------- Karriere ----------------
BEN = ["Geregelte Arbeitszeit für eine ausgewogene Work-Life-Balance", "Ansprechende, leistungsgerechte Vergütung",
 "Förderung der individuellen, fachlichen Weiterbildung", "Abwechslungsreiche Tätigkeiten",
 "Wertschätzende, kollegiale Unternehmenskultur auf Augenhöhe", "Arbeitsplatz im Grünen direkt am Bunten Garten",
 "Kostenfreie Parkplätze unweit der Kanzlei", "Regelmäßige Teamevents wie Sommerfest und Grillabende",
 "Boni wie Einmalzahlungen, Tankgutscheine und Zuschüsse zur betrieblichen Altersvorsorge"]
ka = subhero("Karriere", "Wir suchen dich.",
   "Lust auf interessante Mandanten, abwechslungsreiche Arbeitsfelder und ein motiviertes Team? Dann komm zu uns.", "karriere", accent="dich.")
ka += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p>Wir sind eine moderne Steuerkanzlei mit Sitz in Mönchengladbach, direkt am historisch bedeutsamen Bunten Garten. Zwar sind wir nicht so musikalisch wie unser Leitbild Ludwig van Beethoven, aber wie er brennen wir für unseren Beruf und sind mit Herz dabei. Statt täglich dieselben Aufgaben abzuarbeiten, erhältst du ein intensives Onboarding und übernimmst Schritt für Schritt eigene Aufgabengebiete.</p>\n      </div>\n    </div>\n  </section>\n')
ka += '  <section class="section section--stone">\n    <div class="container">\n      <div class="section-intro reveal"><p class="eyebrow">Das erwartet dich</p><h2 class="h2">Gute Gründe für uns.</h2></div>\n      <ul class="llist stagger reveal">\n'
for b in BEN:
    ka += '        <li>' + b + '</li>\n'
ka += '      </ul>\n    </div>\n  </section>\n'
ka += ('  <section class="section section--navy">\n    <div class="container">\n      <div class="ctaband">\n'
'        <div class="reveal"><p class="eyebrow">Bewirb dich</p><h2 class="h2">Gehe mit uns den nächsten Schritt.</h2>\n'
'        <p class="lead">Ob gradlinige Laufbahn oder Quer- und Wiedereinsteiger: Sende deine Bewerbung mit Gehaltsvorstellung und frühestmöglichem Eintrittstermin direkt an Herrn Muyres.</p></div>\n'
'        <div class="ctaband__actions reveal"><a class="btn btn--primary" href="mailto:info@steuerberatung-muyres.de">Bewerbung senden</a></div>\n      </div>\n    </div>\n  </section>\n')
write("karriere", "Karriere", "Karriere bei der Steuerberatung Muyres in Mönchengladbach: motiviertes Team, moderne Kanzlei, attraktive Benefits. Auch für Quereinsteiger.", "karriere", ka, "karriere")

# ---------------- Coronasoforthilfe ----------------
cb = subhero("Coronasoforthilfe", "Coronasoforthilfe.",
   "Corona war und ist für uns alle eine Herausforderung. Damit Sie den Überblick behalten, beantworten wir Ihre Fragen rund um Kurzarbeit, Steuerstundung, Darlehensprogramme und weitere Themen.", "coronasoforthilfe")
cb += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p>Welche steuerliche Unterstützung der Staat Ihnen in der Coronazeit bietet und wie Sie diese geltend machen können, dazu beraten wir Sie gerne, als Telefonberatung, Onlinecoaching oder persönlichen Termin vor Ort.</p>\n      </div>\n    </div>\n  </section>\n')
cb += zitat("Der Mensch besitzt nichts Edleres und Kostbareres als die Zeit.")
cb += cta_band()
write("coronasoforthilfe", "Coronasoforthilfe", "Steuerliche Beratung rund um Corona: Kurzarbeit, Steuerstundung und Darlehensprogramme bei der Steuerberatung Muyres.", "coronasoforthilfe", cb, "coronasoforthilfe")

# ---------------- Impressum (Demonstrator) ----------------
im = subhero("Impressum", "Impressum.", "Angaben zu diesem Webseiten-Entwurf.")
im += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p><strong>Dieser Internetauftritt ist ein unverbindlicher Redesign-Entwurf</strong> und kein offizieller Auftritt der Steuerberatung Muyres. Die offizielle Website der Kanzlei finden Sie unter <a href="weiter.html?ziel=https://www.steuerberatung-muyres.de/">steuerberatung-muyres.de</a>.</p>\n'
'        <h2 class="h2">Verantwortlich für diesen Entwurf</h2>\n'
'        <p>Dr.-Ing. Suat Akyol<br>Interim Manager<br>E-Mail: contact@akyol.de</p>\n'
'        <p>Sämtliche Inhalte, Texte, Logos und Fotos stammen von der Steuerberatung Muyres und unterliegen deren Rechten. Sie werden hier ausschließlich zu Demonstrationszwecken verwendet. Bei Fragen oder auf Wunsch der Kanzlei wird dieser Entwurf umgehend entfernt.</p>\n      </div>\n    </div>\n  </section>\n')
write("impressum", "Impressum", "Impressum dieses Redesign-Entwurfs der Steuerberatung Muyres.", "", im)

# ---------------- Datenschutz (Demonstrator) ----------------
dz = subhero("Datenschutz", "Datenschutz.", "Hinweise zum Datenschutz dieses Entwurfs.")
dz += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p>Dieser Entwurf ist eine statische Demonstrationsseite, gehostet auf GitHub Pages. Es werden <strong>keine personenbezogenen Daten erhoben oder verarbeitet</strong>.</p>\n'
'        <h2 class="h2">Was lokal gespeichert wird</h2>\n'
'        <p>Lediglich Ihre Cookie-Auswahl und das Ausblenden des Entwurf-Hinweises werden technisch in Ihrem Browser (localStorage) gespeichert. Diese Angaben verlassen Ihr Gerät nicht.</p>\n'
'        <h2 class="h2">Externe Dienste</h2>\n'
'        <p>Es sind keine externen Dienste, Tracking-Tools oder Karten aktiv eingebunden. Das Kontaktformular versendet keine Daten. Externe Links werden über eine Zwischenseite geöffnet.</p>\n'
'        <h2 class="h2">Verantwortlich</h2>\n        <p>Dr.-Ing. Suat Akyol, contact@akyol.de</p>\n      </div>\n    </div>\n  </section>\n')
write("datenschutz", "Datenschutz", "Datenschutzhinweise dieses statischen Redesign-Entwurfs der Steuerberatung Muyres.", "", dz)

# ---------------- Hinweise (Über diesen Entwurf) ----------------
hw = subhero("Über diesen Entwurf", "Über diesen Entwurf.",
   "Was Sie hier sehen, wie es entstanden ist und was funktioniert.", accent="Entwurf.")
def statband(num, suf, eyebrow, h2, lead):
    s = '      <div class="statband reveal">\n        <div class="statband__num">' + num
    if suf:
        s += '<span>' + suf + '</span>'
    s += '</div>\n        <div class="statband__claim">\n          <p class="eyebrow">' + eyebrow + '</p>\n'
    s += '          <h2 class="h2">' + h2 + '</h2>\n          <p class="lead">' + lead + '</p>\n        </div>\n      </div>\n'
    return s

DONE = [
    "Vollständiges, individuelles Design, kein Baukasten-Template",
    "Alle Seiten: Start, Kanzlei, fünf Fachgebiete, Service, Kontakt, Karriere, Steuerberaterwechsel",
    "Optimiert für Smartphone, Tablet und Desktop",
    "Foto-Hero mit Animation und modernes Mobilmenü",
    "Vollständige Suchmaschinen-Daten (SEO) und KI-Suche (GEO)",
    "Häufige Fragen mit Rich-Results-Auszeichnung",
    "Rechtssichere Karten-Einbindung, lädt erst nach Zustimmung",
    "Social-Vorschaubilder, Favicon und schnelle Ladezeiten",
]
TODO = [
    "DATEV-News-Modul echt anbinden (aktuell Platzhalter)",
    "Kontaktformular an den Mailversand anbinden",
    "Seite live schalten und für Suchmaschinen freigeben",
    "Datenschutzerklärung rechtlich finalisieren",
    "Optional: Redaktionssystem zum Selbst-Pflegen",
]
COMP = [
    ("Korrektes Branchen-Schema (LocalBusiness)", 0, 1),
    ("Adresse und Öffnungszeiten strukturiert", 0, 1),
    ("Leistungen als auswertbare Daten", 0, 1),
    ("Team und Personen hinterlegt", 0, 1),
    ("Info-Datei für KI-Suche (llms.txt)", 0, 1),
    ("Frage-Antwort-Auszeichnung (FAQ)", 0, 1),
    ("Verknüpfung zu Social und Kammer", 0, 1),
    ("Klick-Pfad maschinenlesbar (Breadcrumb)", 0, 1),
]
REFS = [
    ("ref-akyol", "akyol.de", "Meine eigene Website: Interim Management und Blog.", "https://www.akyol.de"),
    ("ref-praesi", "KI: gestern, heute, morgen", "Interaktive Online-Keynote, die während des Vortrags live mitarbeitet.", "https://akyol.de/presentations/ki-gestern-heute-morgen/"),
    ("ref-coreform", "core form", "Pilates-Studio: Kursbuchung, Studios und Ausbildung, CI-konform.", "https://www.core-form.de"),
    ("ref-ddim", "DDIM-Relaunch", "Relaunch-Demonstrator für den Interim-Management-Verband DDIM.", "https://suak0903.github.io/ddim-relaunch-demonstrator/"),
    ("ref-cancontrols", "CanControls", "Bildverstehen und Sensorik, Aachen.", "https://suak0903.github.io/cancontrols/"),
    ("ref-seitec", "Seitec", "Energie- und Sicherheitstechnik aus einer Hand.", "https://suak0903.github.io/seitec/"),
]

# --- Disclaimer (ganz oben) ---
hw += ('  <section class="section section--tight">\n    <div class="container">\n'
'      <div class="disclaimer reveal">\n        <p class="disclaimer__t">Bitte beachten</p>\n'
'        <p>Diese Seite ist ein <strong>unverbindlicher Entwurf</strong> und <strong>nicht öffentlich auffindbar</strong> (für Suchmaschinen gesperrt). Sie wurde ausschließlich aus <strong>öffentlich verfügbaren Materialien</strong> des bestehenden Webauftritts zusammengestellt, steht in keiner Verbindung zum offiziellen Auftritt der Kanzlei und konkurriert nicht mit dem Original. Auf Wunsch wird sie <strong>jederzeit vollständig entfernt</strong>.</p>\n      </div>\n    </div>\n  </section>\n')

# --- Sektion 1: Status ---
hw += '  <section class="section">\n    <div class="container">\n'
hw += statband("85", "%", "Stand der Umsetzung", "Startklar, bis auf die letzte Meile.",
    "Design, Inhalte, Struktur und die komplette Suchmaschinen-Optimierung sind fertig. Was noch fehlt, sind technische Anbindungen für den Live-Betrieb.")
hw += '      <div class="twocol reveal">\n        <div class="panel"><h3>Fertig und funktionsfähig</h3>\n          <ul class="ck">\n'
for it in DONE:
    hw += '            <li>' + it + '</li>\n'
hw += '          </ul>\n        </div>\n        <div class="panel"><h3>Für den Live-Betrieb offen</h3>\n          <ul class="td">\n'
for it in TODO:
    hw += '            <li>' + it + '</li>\n'
hw += '          </ul>\n        </div>\n      </div>\n    </div>\n  </section>\n'

# --- Sektion 2: SEO / GEO ---
hw += '  <section class="section section--stone">\n    <div class="container">\n'
hw += statband("40", "+", "Auffindbarkeit: SEO und GEO", "Fakten, die Google und KI jetzt verstehen.",
    "Über 40 strukturierte Angaben (Adresse, Öffnungszeiten, Leistungen, Team, Themen) machen die Kanzlei für Suchmaschinen und KI-Assistenten auswertbar. Die bisherige Seite liefert davon keinen einzigen: ihr einziges Datenobjekt ist ein leeres „Article“.")
hw += '      <div class="comptable reveal">\n        <div class="comptable__head"><span>Signal für Suchmaschinen</span><span>Bisherige Seite</span><span>Dieser Entwurf</span></div>\n'
for label, a, b in COMP:
    def _cell(v):
        if v == 1: return '<span class="yes">Ja</span>'
        if v == 0: return '<span class="no">Nein</span>'
        return '<span class="txt">' + v + '</span>'
    hw += '        <div class="comptable__row"><span class="comptable__l">' + label + '</span>' + _cell(a) + _cell(b) + '</div>\n'
hw += '      </div>\n'
hw += ('      <div class="geobox reveal">\n        <p class="eyebrow">Warum GEO besonders zählt</p>\n'
'        <h3>Gefunden werden, wo künftig gesucht wird.</h3>\n'
'        <p>Immer mehr Menschen fragen ChatGPT, Perplexity oder die KI-Übersicht von Google: „Guter Steuerberater in Mönchengladbach?“ Diese Systeme empfehlen nur, was sie strukturiert verstehen. Dieser Entwurf gibt ihnen eine eigene Info-Datei, eine Frage-Antwort-Auszeichnung und klare Themen-Signale. Für die bisherige Seite sind diese Assistenten praktisch blind.</p>\n      </div>\n    </div>\n  </section>\n')

# --- Sektion 3: Referenzen ---
hw += '  <section class="section">\n    <div class="container">\n'
hw += statband("6", "", "Referenzen", "Kein Einzelfall: sechs Projekte aus meiner Hand.",
    "Von der eigenen Website über Kundenprojekte bis zu Relaunch-Demonstratoren, alle mit KI-Unterstützung gebaut.")
hw += '      <div class="reflist stagger reveal">\n'
for img, t, d, url in REFS:
    hw += ('        <a class="refcard" href="' + url + '" target="_blank" rel="noopener">\n'
           '          <span class="refcard__shot"><img src="media/' + img + '.jpg" alt="Startseite ' + t + '" loading="lazy" width="800" height="500"></span>\n'
           '          <span class="refcard__body"><span class="refcard__t">' + t + '</span><span class="refcard__d">' + d + '</span><span class="refcard__link">Live ansehen</span></span>\n        </a>\n')
hw += '      </div>\n    </div>\n  </section>\n'

# --- Abschluss: Demonstrator-Hinweis ---
hw += ('  <section class="section section--stone">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p class="eyebrow">Zum Hintergrund</p>\n        <h2 class="h2">Was ist das hier?</h2>\n'
'        <p>Ein unverbindlicher Redesign-Entwurf für die Steuerberatung Muyres, erstellt von Dr.-Ing. Suat Akyol. Inhalte und Bilder stammen aus dem bestehenden Auftritt; gezeigt wird, wie er in moderner, klarer und besser auffindbarer Form aussehen kann. Anmerkungen gerne an <a href="mailto:contact@akyol.de">contact@akyol.de</a>.</p>\n      </div>\n    </div>\n  </section>\n')
write("hinweise", "Über diesen Entwurf", "Status, SEO- und GEO-Analyse und Referenzen zum Redesign-Entwurf der Steuerberatung Muyres von Dr.-Ing. Suat Akyol.", "", hw)

# ---------------- weiter.html (Redirect-Platzhalter) ----------------
wt = subhero("Externer Link", "Sie verlassen den Entwurf.", "", accent="Entwurf.")
wt += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p>Dieser Link führt auf eine externe Seite, die nicht Teil dieses Entwurfs ist.</p>\n'
'        <p id="zielinfo"></p>\n        <p><a class="btn btn--primary" id="zielbtn" href="index.html">Weiter zur externen Seite</a> &nbsp; <a class="btn btn--ghost" href="index.html">Zurück</a></p>\n      </div>\n    </div>\n  </section>\n'
'  <script>(function(){var p=new URLSearchParams(location.search).get("ziel")||"";try{var u=new URL(p);var ok=/(steuerberatung-muyres\\.de|steuerberatungneumann\\.de|xing\\.com|linkedin\\.com)$/.test(u.hostname);if(ok){document.getElementById("zielbtn").href=u.href;document.getElementById("zielinfo").textContent=u.href;}else{document.getElementById("zielinfo").textContent="Unbekanntes Ziel.";}}catch(e){document.getElementById("zielinfo").textContent="Kein gültiges Ziel.";}})();</script>\n')
write("weiter", "Externer Link", "Zwischenseite für externe Links.", "", wt)

# ---------------- 404 ----------------
nf = subhero("Seite nicht gefunden", "Seite nicht gefunden.", "Die aufgerufene Seite existiert nicht.", accent="nicht gefunden.")
nf += ('  <section class="section">\n    <div class="container">\n      <div class="prose narrow reveal">\n'
'        <p>Vielleicht hilft der Weg zurück zur <a href="index.html">Startseite</a> oder zu unseren <a href="fachgebiete.html">Fachgebieten</a>.</p>\n      </div>\n    </div>\n  </section>\n')
write("404", "Seite nicht gefunden", "Seite nicht gefunden.", "", nf)

# ---------------- robots.txt / sitemap.xml / llms.txt ----------------
SLUGS = ["", "kanzlei", "fachgebiete", "fachgebiete-unternehmen", "fachgebiete-privatpersonen",
 "fachgebiete-existenzgruender", "fachgebiete-freiberufler", "fachgebiete-immobilienbesitzer",
 "service", "kontakt", "steuerberaterwechsel", "karriere", "coronasoforthilfe", "hinweise"]
with io.open(os.path.join(PROJ, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: " + PAGES + "/sitemap.xml\n")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for s in SLUGS:
    sm += '  <url><loc>' + PAGES + "/" + (s + ".html" if s else "") + '</loc></url>\n'
sm += '</urlset>\n'
with io.open(os.path.join(PROJ, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write(sm)
llms = ("# Steuerberatung Muyres\n\n"
"> Persönliche Steuerberatung in Mönchengladbach. Gegründet 2020 von Michael Muyres, am Bunten Garten an der Beethovenstraße. Leitbild: Tradition trifft Moderne.\n\n"
"Hinweis: Diese Seite ist ein Redesign-Entwurf (Demonstrator) von Dr.-Ing. Suat Akyol, kein offizieller Auftritt der Kanzlei.\n\n"
"## Leistungen\n- Unternehmen: Jahresabschluss, Lohnbuchhaltung, betriebliche Steuererklärung, Unternehmensnachfolge\n"
"- Privatpersonen: Einkommensteuererklärung, Prüfung von Steuerbescheiden, Vermögensübertragung\n"
"- Existenzgründer und Startups: Businessplan, Rechtsformwahl, Fördergelder\n"
"- Freiberufler und Freelancer: Gewinnermittlung, Finanzbuchführung\n"
"- Immobilienbesitzer: Grundsteuererklärung, Vermietung und Verpachtung, Bewertung\n\n"
"## Team\n- Michael Muyres: Steuerberater B.A., Gründer\n- Peter Muyres: Steuerberater\n- Doris Franke, Claudia Wassenberg, Ingrid Wolff: Steuerfachangestellte\n- Ulrike Rautenberger: Steuerfachwirtin, Bilanzbuchhalterin\n\n"
"## Mitgliedschaften und Partner\n- Steuerberaterkammer Düsseldorf\n- DATEV Digitale Kanzlei 2022\n- Kooperationspartner: Steuerbüro Lars Neumann (Düsseldorf)\n\n"
"## Einzugsgebiet\nMönchengladbach und Umgebung (Korschenbroich, Viersen, Willich, Jüchen, Neuss).\n\n"
"## Steuerberaterwechsel\nEin Wechsel zu uns ist unkompliziert: Wir übernehmen die Kommunikation mit dem bisherigen Berater und das Anfordern der Unterlagen.\n\n"
"## Kontakt\n- Adresse: Beethovenstraße 55, 41061 Mönchengladbach\n- Telefon: 02161 / 49 50 78 - 0\n- Telefax: 02161 / 49 50 78 - 9\n- E-Mail: info@steuerberatung-muyres.de\n"
"- Bürozeiten: Mo-Do 8:30-12:30 und 13:30-16:30 Uhr, Fr 8:30-13:00 Uhr\n\n"
"## Erstgespräch\nKostenfreies Erstgespräch als Telefonberatung, Onlinecoaching oder Termin vor Ort.\n")
with io.open(os.path.join(PROJ, "llms.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write(llms)

print("Alle Seiten + robots/sitemap/llms geschrieben.")
