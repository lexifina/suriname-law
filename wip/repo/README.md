# Suriname: law history in git

The law of Suriname as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `sr/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `grondwet/` | Grondwet van de Republiek Suriname (1987) | 3 | From the 1992 consolidation (as amended by S.B. 1992 no. 38) to today's official text, S.B. 2025 no. 15 |

The three versions are:

1. **1992-04-08**: the Grondwet of 1987 (S.B. 1987 no. 116) as amended by the Wet van 8 april 1992 (S.B. 1992 no. 38), from the consolidation published by De Nationale Assemblée. This is the oldest text online, so it is committed by the publisher as "oldest version available".
2. **2023-10-27**: the Wet van 25 oktober 2023 (S.B. 2023 no. 157), which rewrote arts. 60, 61, 161 (a new lid 4) and 163 after the Constitutioneel Hof's ruling on the Kiesregeling (S.B. 2022 no. 85). Only those four articles change, credited to the act.
3. **2025-02-07**: the official consolidation placed in the Staatsblad by Resolutie of 6 February 2025 (S.B. 2025 no. 15). It says it holds the 1992 and 2023 amendments only, yet it also differs from the 1992 consolidation in 20 articles: modern spelling (produktie to productie, privé-leven to privéleven), punctuation, the numbering of art. 31 lid 4 to lid 3, dashes in art. 142, and the word "oorlog" missing from art. 56 lid 2. No law explains these, so they are one commit by the publisher, labelled "unexplained", and `REPRODUCE.md` lists each.

Chapter and section headings are in `grondwet/indeling.md`; the preamble is `grondwet/preambule.md`.

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
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`sb-2023-157@dna.invalid`), so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **Credits come only from the source.** A changed provision is credited to a law only when the official consolidation footnotes it with that law ("Gew. bij S.B. 2023 no. 157").
- **Unexplained changes** are committed by the publisher and labelled "unexplained": the 20 differences of S.B. 2025 no. 15 that no law explains.
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words changed.

## What it does not show

- **The Grondwet of 1987 as enacted, and the 1992 amendment as a change.** Neither S.B. 1987 no. 116 nor the Wet van 8 april 1992 (S.B. 1992 no. 38) is online in any official copy we found (dna.sr and its Internet Archive history, sris.sr, gov.sr, WIPO Lex). The 1992 consolidation's footnotes name the roughly 75 provisions that S.B. 1992 no. 38 changed, inserted or repealed, and the first commit's message lists them, but their 1987 wording is not available.
- **Footnotes and the memorie van toelichting** are not in the text; the footnotes are used only to credit laws.
- **The Wetboek van Strafrecht and the Burgerlijk Wetboek.** De Nationale Assemblée publishes consolidations to 2005 with per-article footnotes, but most later amending acts are scanned Staatsblad issues with no text layer. Their history cannot be rebuilt without OCR, which this record does not use for legal text.
- **Data protection.** No data protection law appears in De Nationale Assemblée's lists of Surinamese legislation (the nearest is the Wet Elektronisch Rechtsverkeer).
- **Court rulings.** The Constitutioneel Hof's ruling of 5 August 2022 (S.B. 2022 no. 85) struck arts. 9 and 24 of the Kiesregeling, not Grondwet text, so it is not a commit here; it is the reason given in S.B. 2023 no. 157.
- **Pending proposals.** Initiative proposals to amend the Grondwet that were before De Nationale Assemblée in 2025 are not law and are not shown.

## How it is built

`tools/fetch.py` downloads every source once through curl (one request per second per host, cached by the sha256 of the URL), `tools/parse.py` reads the official PDFs' own text layers with PyMuPDF and writes `corpus.json`, and the shared builder `tools/build.py` writes the history with `git fast-import`. The same corpus always gives the same hashes. `REPRODUCE.md` records every command, tool version, data hash and decision, and the result of a hash-for-hash rebuild.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; it viewed the page images of S.B. 2023 no. 157 to identify the act, its commencement clause, and to compare its wording with S.B. 2025 no. 15. See `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [De Nationale Assemblée, Surinaamse wetten](https://www.dna.sr/wetgeving/surinaamse-wetten/) | Official legislation | no; consolidations to 2005, then Staatsblad issues | yes, a footnote per article in the consolidations | no | Used: the 1992 Grondwet consolidation, S.B. 2023 no. 157 (scan). Lists "Geldende teksten t/m 2005", "Wetten na 2005", "Wijzigingen na 2005". No robots.txt |
| [Surinaams Rechtsinformatiesysteem](https://sris.sr/) | Official texts | no | yes, footnotes | no | Used: S.B. 2025 no. 15 (today's Grondwet) and the 1992 Grondwet with memorie van toelichting (cross-check) |
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
- Bronnen: De Nationale Assemblée (www.dna.sr) en het Surinaams Rechtsinformatiesysteem (sris.sr). Geen AI-model heeft wettekst geschreven.
