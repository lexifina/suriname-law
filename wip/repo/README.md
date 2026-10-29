# Suriname: law history in git

The law of Suriname as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `sr/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `grondwet/` | Grondwet van de Republiek Suriname (1987) | 3 | From the 1992 consolidation (as amended by S.B. 1992 no. 38) to today's official text, S.B. 2025 no. 15 |
| `burgerlijk-wetboek/` | Burgerlijk Wetboek, Boeken 1-8 (S.B. 2024 no. 164) | 1 | The new Civil Code as enacted, in force 1 May 2025; not amended since |
| `rechtsvordering/` | Wetboek van Burgerlijke Rechtsvordering (S.B. 2024 no. 170) | 1 | The new Code of Civil Procedure as enacted, in force 1 May 2025; not amended since |
| `kiesregeling/` | Kiesregeling (S.B. 1987 no. 62) | 1 | Today's official text, S.B. 2025 no. 16 (as amended up to S.B. 2025 no. 8) |

The three versions are:

1. **1992-04-08**: the Grondwet of 1987 (S.B. 1987 no. 116) as amended by the Wet van 8 april 1992 (S.B. 1992 no. 38), from the consolidation published by De Nationale Assemblée. This is the oldest text online, so it is committed by the publisher as "oldest version available".
2. **2023-10-27**: the Wet van 25 oktober 2023 (S.B. 2023 no. 157), which rewrote arts. 60, 61, 161 (a new lid 4) and 163 after the Constitutioneel Hof's ruling on the Kiesregeling (S.B. 2022 no. 85). Only those four articles change, credited to the act.
3. **2025-02-07**: the official consolidation placed in the Staatsblad by Resolutie of 6 February 2025 (S.B. 2025 no. 15). It says it holds the 1992 and 2023 amendments only, yet it also differs from the 1992 consolidation in 20 articles: modern spelling (produktie to productie, privé-leven to privéleven), punctuation, the numbering of art. 31 lid 4 to lid 3, dashes in art. 142, and the word "oorlog" missing from art. 56 lid 2. No law explains these, so they are one commit by the publisher, labelled "unexplained", and `REPRODUCE.md` lists each.

Chapter and section headings are in `grondwet/indeling.md`; the preamble is `grondwet/preambule.md`.

**The 2024 codes.** Suriname replaced its Civil Code of 1860 and its Code of Civil Procedure with new codes, both Wetten van 5 december 2024 (S.B. 2024 no. 164 and no. 170, uitgegeven 15 and 13 January 2025). Resolutie S.B. 2025 no. 14 put both into force on **1 May 2025**. Each is one commit, the code as enacted, credited to its act. No amending act of either code was found up to October 2026 (only a bill to amend the Rechtsvordering, August 2026), so that text is today's text.

- `burgerlijk-wetboek/`: Boeken 1 to 8. Each Book numbers its own articles, so files are `boek-<n>-art-<number>.md` (`boek-6-art-0162.md` is art. 6:162, the tort article); each Book's titles and sections are in `boek-<n>-indeling.md`. Boek 7A, the remains of the old code's Derde Boek kept by the Aanpassingswet (S.B. 2024 no. 168), is not included: that act gives only its changes, and the old text they apply to is not online in usable form (see below).
- `rechtsvordering/`: numbered straight through its four Books (Artikel A and B, then 1 to 1079, with unused numbers skipped); headings in `indeling.md`.

**The Kiesregeling** (electoral law) is one version: the official current text that Resolutie S.B. 2025 no. 16 placed in the Staatsblad on 7 February 2025, as amended by ten acts from 1987 to S.B. 2025 no. 8 (in force 21 January 2025). It is dated 7 February 2025, the day of that publication, and committed by the publisher as the oldest version available. Earlier versions are not built: the 2019 and 2023 amending acts are scans, and the 2024 and 2025 acts give only their changes.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 61 of the Grondwet say on 1 January 2020? | `python tools/geldend_op.py 2020-01-01 grondwet 61` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" main -- grondwet/art-061.md):grondwet/art-061.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" main -- grondwet/art-061.md; git show "$($r):grondwet/art-061.md"` |
| Which law wrote each paragraph of art. 163? | `git blame grondwet/art-163.md` |
| Every change to art. 61, word by word | `git log -p --word-diff grondwet/art-061.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/sb-2023-157` (tags `law/<key>` mark each law's commit) |
| The whole Grondwet on a date | `python tools/geldend_op.py 2024-01-01 grondwet` |
| Art. 6:162 BW (onrechtmatige daad) today | `python tools/geldend_op.py 2026-01-01 burgerlijk-wetboek boek-6-art-0162` |
| A dated version | `git show grondwet/2023-10-27` (tags `<act>/<in-force day>`) |
| Laws passed but not yet in force | `git log main..toekomst` (the branch exists only when there are any; none now) |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Paramaribo, on the day the change took effect**. Enactment and publication dates are trailers (`Enacted:`, `Published:`), and the in-force day is in `In-force:`, which the tools read.
- **Default rule.** Grondwet art. 80 lid 1: approved and ratified bills "verkrijgen kracht van wet na afkondiging"; art. 118 leaves the manner and moment of binding force to the law, and the Wet Algemene Bepalingen (G.B. 1868 no. 14) art. 1 says no regulation binds before its afkondiging. So a law binds from its afkondiging in the Staatsblad unless its own slotbepaling sets another day; most say "de dag volgende op die van haar afkondiging".
- **S.B. 2023 no. 157** was uitgegeven on 26 October 2023 and by its art. II lid 2 took effect the day after, **27 October 2023**.
- **The 1992 version** is dated 8 April 1992, the date of the amending Wet. Its Staatsblad issue and commencement clause are not online, so the real in-force day may be a few days later.
- **The 2025 version** is dated 7 February 2025, the day S.B. 2025 no. 15 was uitgegeven. It is a republication, not a law, so this is when its text appeared, not when any change took legal effect.
- The Grondwet itself took effect on 30 October 1987 (art. 186 lid 3); that original text is not in this record (see below).
- `--before="YYYY-MM-DD"` alone uses your clock's time of day. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- **Against the official text.** Today's text is S.B. 2025 no. 15 as parsed from its own PDF text layer. Parsing was checked word by word against that PDF: every body word is in the provisions, in order, apart from headings (in `indeling.md`) and words joined across a line-end hyphen.
- **The 1992 text** was read from the dna.sr consolidation and compared with two other copies: the gov.sr copy (which drops "oorlog" in art. 56 lid 2 and prints "Rege-ring" in art. 148) and the sris.sr edition with the memorie van toelichting (which agrees with dna.sr on art. 56).
- **The 2023 change** is the S.B. 2025 no. 15 wording of the four articles that S.B. 2025 no. 15 footnotes "Gew. bij S.B. 2023 no. 157". The act itself is a scanned PDF with no text layer; its page images were compared by eye with that wording. They agree, except that the act has a comma in art. 161 lid 4 ("per ressort, en de methode") that S.B. 2025 no. 15 does not. That comma is not in this record: adding it would mean transcribing a scan.
- **The 2024 codes and the Kiesregeling** were read from the Staatsblad PDFs on sris.sr, which have a born-digital text layer. `tools/verify_codes.py` reads the same pages again with a different extractor (PyMuPDF's word list) and checks that every word is in the provisions in the same order, apart from headings, title pages, signatures and the footnotes of S.B. 2025 no. 16; it also checks that no heading was swallowed by the article before it.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`sb-2023-157@dna.invalid`), so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **Credits come only from the source.** A changed provision is credited to a law only when the official consolidation footnotes it with that law ("Gew. bij S.B. 2023 no. 157").
- **Unexplained changes** are committed by the publisher and labelled "unexplained": the 20 differences of S.B. 2025 no. 15 that no law explains.
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words changed.

## What it does not show

- **The Grondwet of 1987 as enacted, and the 1992 amendment as a change.** Neither S.B. 1987 no. 116 nor the Wet van 8 april 1992 (S.B. 1992 no. 38) is online in any official copy we found (dna.sr and its Internet Archive history, sris.sr, gov.sr, WIPO Lex). The 1992 consolidation's footnotes name the roughly 75 provisions that S.B. 1992 no. 38 changed, inserted or repealed, and the first commit's message lists them, but their 1987 wording is not available.
- **Footnotes and the memorie van toelichting** are not in the text; the footnotes are used only to credit laws.
- **The Wetboek van Strafrecht, and the old Burgerlijk Wetboek and Rechtsvordering before 2025.** De Nationale Assemblée publishes consolidations to 2005 with per-article footnotes, but no official consolidation after that, and most later amending acts are scanned Staatsblad issues. The Wetboek van Strafrecht was re-enacted in full by the Wet van 30 maart 2015 (S.B. 2015 no. 44, with a text layer), but the amendments since then cannot be applied from official text: S.B. 2014 no. 118, S.B. 2023 no. 133 and S.B. 2023 no. 135 are scans (the last two with only the scanner's OCR layer), S.B. 2020 no. 42 carries only an uncorrected OCR layer ("Straftecht"), and S.B. 2017 no. 85 is not in the lists. This record uses no OCR, so the Penal Code is not included rather than shown out of date. For the old Burgerlijk Wetboek (G.B. 1860 no. 4), the amendments of 2016 and S.B. 2022 no. 34 are scans, so its history up to its replacement on 1 May 2025 is not built either.
- **Data protection.** Suriname has no data protection law in force; sris.sr holds only a bill, the Ontwerpwet Bescherming Privacy en Persoonsgegevens (2020).
- **Court rulings.** The Constitutioneel Hof's ruling of 5 August 2022 (S.B. 2022 no. 85) struck arts. 9 and 24 of the Kiesregeling, not Grondwet text, so it is not a commit here; it is the reason given in S.B. 2023 no. 157.
- **Pending proposals.** Initiative proposals to amend the Grondwet that were before De Nationale Assemblée in 2025 are not law and are not shown.

## How it is built

`tools/fetch.py` downloads every source once through curl (one request per second per host, cached by the sha256 of the URL), `tools/parse.py` reads the official PDFs' own text layers with PyMuPDF and writes `corpus.json` (the Grondwet), `tools/parse_codes.py` does the same for the 2024 codes and the Kiesregeling (the `corpus.d/` parts), and the shared builder `tools/build.py` writes the history with `git fast-import`. The same corpus always gives the same hashes. `REPRODUCE.md` records every command, tool version, data hash and decision, and the result of a hash-for-hash rebuild.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; it viewed the page images of S.B. 2023 no. 157 to identify the act, its commencement clause, and to compare its wording with S.B. 2025 no. 15. See `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [De Nationale Assemblée, Surinaamse wetten](https://www.dna.sr/wetgeving/surinaamse-wetten/) | Official legislation | no; consolidations to 2005, then Staatsblad issues | yes, a footnote per article in the consolidations | no | Used: the 1992 Grondwet consolidation, S.B. 2023 no. 157 (scan). Lists "Geldende teksten t/m 2005", "Wetten na 2005", "Wijzigingen na 2005". No robots.txt |
| [Surinaams Rechtsinformatiesysteem](https://sris.sr/) | Official texts | no | yes, footnotes | yes: WordPress media listing (`/wp-json/wp/v2/media`, 1,757 files) | Used: S.B. 2025 no. 15 (today's Grondwet), the 1992 Grondwet with memorie van toelichting (cross-check), S.B. 2024 nos. 164 and 170 (the 2024 codes), S.B. 2025 no. 14 (their commencement), S.B. 2025 no. 16 (today's Kiesregeling) |
| [Government of Suriname](https://gov.sr/) | Official copy | no | yes, footnotes | no | A 2011 copy of the 1992 consolidation, used only as a cross-check |
| [WIPO Lex](https://www.wipo.int/wipolex/en/legislation/details/8816) | Collection | no | n/a | no | Dutch and English PDFs of the 1992 consolidation only; not used |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of the Republic of Suriname, published in the Staatsblad van de Republiek Suriname and read from De Nationale Assemblée (www.dna.sr) and the Surinaams Rechtsinformatiesysteem (sris.sr). Neither publishes a licence, so their copyright status is not confirmed here; they are reproduced with that attribution. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## In het Nederlands

De geschiedenis van het Surinaamse recht in git: één bestand per bepaling en één commit per wet, gedateerd op de dag van inwerkingtreding en op naam van de wet die de wijziging aanbracht (`git blame` noemt de wet achter elke alinea). Het bevat de Grondwet van de Republiek Suriname vanaf de geconsolideerde tekst van 1992 (na de wijziging bij S.B. 1992 no. 38), de wijziging van de artikelen 60, 61, 161 en 163 bij S.B. 2023 no. 157 (in werking 27 oktober 2023), en de thans geldende tekst van S.B. 2025 no. 15.

- Geldende tekst op een datum: `python tools/geldend_op.py 2020-01-01 grondwet 61`
- Data: de dag van inwerkingtreding. Hoofdregel: een wet verkrijgt kracht van wet na afkondiging (Grondwet art. 80 lid 1), tenzij de wet zelf een andere dag bepaalt.
- Toerekening: een wijziging wordt alleen aan een wet toegeschreven als een voetnoot in de officiële tekst die wet noemt ("Gew. bij S.B. 2023 no. 157"). Verschillen die geen wet verklaart (spelling, interpunctie, nummering en het ontbrekende woord "oorlog" in art. 56 lid 2 van S.B. 2025 no. 15) staan in één aparte commit als "unexplained".
- De oorspronkelijke tekst van 1987 en de wijzigingswet van 1992 zijn niet online te vinden en ontbreken daarom.
- Verder: het nieuwe Burgerlijk Wetboek (Boeken 1 t/m 8, S.B. 2024 no. 164) en het nieuwe Wetboek van Burgerlijke Rechtsvordering (S.B. 2024 no. 170), beide zoals vastgesteld en in werking sinds 1 mei 2025 (S.B. 2025 no. 14), en de thans geldende tekst van de Kiesregeling (S.B. 2025 no. 16). Boek 7A, het Wetboek van Strafrecht en de oude wetboeken vóór 2025 ontbreken: de latere wijzigingswetten zijn alleen als scan beschikbaar en er wordt geen OCR gebruikt.
- Bronnen: De Nationale Assemblée (www.dna.sr) en het Surinaams Rechtsinformatiesysteem (sris.sr). Geen AI-model heeft wettekst geschreven.
