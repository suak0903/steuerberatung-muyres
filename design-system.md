# Design-System - Steuerberatung Muyres (Relaunch-Demonstrator)

Abgeleitet aus dem Bestand (`_source/`), modernisiert nach Suat-Stil (Web-Starter-Kit §4).
Redesign-Modus: **Preserve** - CI bleibt erkennbar, Optik wird geglättet.

## Farben (Palette nach Suat-Vorgabe, 23.06.)

| Token | Hex | Verwendung |
|---|---|---|
| `--navy` | `#0D1931` | Primärfarbe dunkel: Hero, Footer, dunkle Sektion, Headlines |
| `--navy-2` | `#152444` | Tiefe/Verlauf, Kontaktzeile |
| `--bordeaux` | `#7F2346` | Akzent (genau einer): Buttons, Linien, Eyebrows, Links |
| `--bordeaux-bright` | `#963A5B` | Hover auf Bordeaux |
| `--blue` | `#1D3A63` | harmonische Blauvariante (ersetzt Bestand-#001F60), sparsam |
| `--sky` | `#A9C7E8` | heller Blauton: Akzent-Text auf dunkel (statt Rosa) |
| `--ink` | `#1A2230` | Fließtext auf hell |
| `--muted` | `#5E6675` | Sekundärtext |
| `--paper` | `#FFFFFF` | heller Grund |
| `--stone` | `#F3F2EF` | warmer heller Wechselgrund (Haupt-Rhythmus, edel) |
| `--mist` | `#EDF1F6` | sehr dezenter Blau-Tint, sparsam |
| `--line` | `#E7E4DF` | warme Hairline |

**Akzent-Lock:** Bordeaux `#7F2346` ist der einzige Akzent. Auf dunklem Grund tritt
das helle `--sky` an die Stelle von Rosa. Keine weiteren Farben. (Bestand-#001F60 und
das kalte Off-White #EEF5FA wurden auf Suats Wunsch durch harmonischere Töne ersetzt.)

## Schriften (self-hosted, `font/`)

| Rolle | Familie | Schnitte | Datei |
|---|---|---|---|
| Alles (Display + Body) | **Archivo** | 300 / 400 / 500 / 600 / 700 | `archivo-{300..700}.woff2` |

Eine serifenlose Familie durchgängig (Suat-Wunsch: keine Serife). Archivo ist eine
seriöse Grotesk mit vollem Schnitt-Set, edel und gut lesbar. DATEV Compatil (Original)
wurde verworfen (wirkte serifig/altmodisch); liegt als Quelle in `_source/`.

## Form & Rhythmus (Suat-Invarianten)

- `border-radius: 0` global (Inputs max 2 px, dekorative Punkte ausgenommen).
- Hairlines (`--line`) statt Box-Shadows; Karten-Hover = Farbe/Border, kein Scale/translateY.
- Sektions-Rhythmus (nie zwei gleiche hintereinander, nie `<hr>`):
  `paper -> mist -> paper -> navy(dunkel) -> paper -> cloud ...`
- Sektions-Padding 96 px Desktop / 48 px Mobile; Container max 1200 px.
- Eyebrows uppercase, `letter-spacing`, Bordeaux. Headlines enden auf Punkt.
- Animation: `cubic-bezier(.22,1,.36,1)`, 250-450 ms, Stagger-Eingang Hero/Nav.
  `prefers-reduced-motion: reduce` schaltet ALLES ab.
- Nur Inline-SVG-Icons (die echten Fachgebiet-Icons aus `media/`). Keine Emojis,
  keine Ausrufezeichen, keine em-Dashes.

## Logo-Assets (`media/`)

- `logo.svg` - Hauptlogo farbig (Navy/Bordeaux), helle Flächen.
- `logo-white.svg` - invertiert für Navy-Flächen/Footer.
- `logo-signet.png` - Signet (393x364), dezentes Grafikelement.
- `icon-{unternehmen,privatpersonen,existenzgruender,freelancer,immobilienbesitzer}.svg` - Fachgebiete.
- `icon-{phone,envelope,calendar}.svg` - Kontakt.

## Stimme (Original übernommen, faktentreu)

Claim: „Freundlich. Professionell. Nah." · „So individuell wie Sie." ·
„Schnell. Einfach. Unkompliziert." · Beethoven-Leitbild (Tradition trifft Moderne) ·
15+ Jahre Erfahrung · kostenfreies Erstgespräch · Kooperationspartner Lars Neumann.
Außentexte durch `humanizer`, Testimonials wörtlich.
