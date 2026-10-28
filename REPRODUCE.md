# How this repository was made (Suriname)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| De Nationale Assemblee, Surinaamse wetten | <https://www.dna.sr/wetgeving/surinaamse-wetten/> | 2026-10-28 | 37 | Official legislative text; no licence stated; robots.txt absent (404) |
| Surinaams Rechtsinformatiesysteem (sris.sr) | <https://sris.sr/> | 2026-10-28 | 2 | Official Staatsblad text; no licence stated |
| Government of Suriname (gov.sr) | <https://gov.sr/> | 2026-10-28 | 1 | Official text; no licence stated |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `grondwet` | Grondwet van de Republiek Suriname | 3 | 1992-04-08 to 2025-02-07 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 1 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `toekomst`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/Paramaribo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Grondwet art. 80 lid 1: laws "verkrijgen kracht van wet na afkondiging"; art. 118 leaves the manner and moment to the law; Wet Algemene Bepalingen (G.B. 1868 no. 14) art. 1: no regulation binds before its afkondiging. So a law binds from its afkondiging in the Staatsblad, unless its own slotbepaling sets another day (most say "de dag volgende op die van haar afkondiging"). https://sris.sr/wp-content/uploads/2025/04/ (S.B. 2025 no. 15, arts. 80 and 118); https://www.dna.sr/media/frtc5hy3/wet_algemene_bepalingen.pdf

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/suriname-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `1c80bad1727f28e1dac139455ba928179484fdef89d22725b411a2a17542bdfc` (311901 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `393620efbfbe0a04540926b2d8f0a75ed749d600` |
| check.py | `741bd38ee6a4a25cfcecc28ccb2b93ce4e8b3fb2` |
| on.py | `668b24bbcd37efdfa1b60429c0d2b2c940ca9fff` |
| fetch.py | `f5d99753b3bf1b7d34420121415f1de9953ea8fb` |
| parse.py | `4a49b212e62bb3944e01898d814e0e92e67c4b8f` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

2 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Grondwet: the original 1987 text (S.B. 1987 no. 116) and the 1992 amending act (S.B. 1992 no. 38) are not online in any official copy we found (dna.sr, its Wayback history, sris.sr, gov.sr, WIPO Lex), so the history starts with the 1992 consolidation, committed by the publisher as the oldest version available.
- Grondwet: the first version is dated 1992-04-08, the date of the Wet van 8 april 1992; its Staatsblad issue date and commencement clause could not be read online, so the real in-force day may be a few days later.
- Grondwet: S.B. 2023 no. 157 took effect the day after its afkondiging (art. II lid 2); it was uitgegeven on 26 October 2023, so the in-force day is 2023-10-27.
- Grondwet: three versions. 1992-04-08 is the dna.sr 1992 consolidation. 2023-10-27 is that text with arts. 60, 61, 161 and 163, the articles S.B. 2025 no. 15 footnotes "Gew. bij S.B. 2023 no. 157", replaced by their S.B. 2025 no. 15 wording and credited to S.B. 2023 no. 157 (whose own PDF is a scan with no text layer). 2025-02-07, the day S.B. 2025 no. 15 was uitgegeven, is S.B. 2025 no. 15 in full; every other difference from 1992 has no amending law and is committed uncredited by the publisher.
- Grondwet: the wording S.B. 2025 no. 15 gives arts. 60, 61, 161 and 163 was compared by eye with the page images of S.B. 2023 no. 157. It agrees, except that the act reads "per ressort, en de methode" in art. 161 lid 4 where S.B. 2025 no. 15 has no comma. The 2023-10-27 version uses the S.B. 2025 no. 15 wording, so that comma is not in this history; adding it would mean transcribing a scan.
- Grondwet: S.B. 2025 no. 15 is a republication by Resolutie (no. 14.227/24), not an amending law, so its changes against the 1992 consolidation are not credited to any law; each is listed below.
- Grondwet: art. 56 lid 2 "in geval van oorlog of andere buitengewone omstandigheden" is read as in the dna.sr 1992 consolidation; the sris.sr 1992 edition with memorie van toelichting agrees, while the gov.sr copy and S.B. 2025 no. 15 omit "oorlog". The omission appears in the 2025-02-07 commit, uncredited.
- Grondwet: the two publishers break some paragraphs differently (the preamble clauses, the oaths in arts. 93 and 114, art. 66, the list in art. 142 lid 1). Where the words agree, the 1992 version takes the line breaks of S.B. 2025 no. 15, so layout does not show up as change.
- Grondwet: parse completeness was checked word by word against each PDF text layer: every body word of S.B. 2025 no. 15 is in the units in order, apart from headings (kept in grondwet/indeling.md) and words joined across a line-end hyphen.
- Chapter and section headings are kept in one unit, grondwet/indeling.md, so article files hold only article text.
- Quotes and dashes are normalised to straight quotes and "-"; words the typesetter broke at a line end are joined.
- Grondwet art-056: the gov.sr copy of the 1992 consolidation differs from the dna.sr copy used here (drops "oorlog").
- Grondwet art-148: the gov.sr copy of the 1992 consolidation differs from the dna.sr copy used here ("Regering" -> "Rege-ring").
- Grondwet art-005: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "produktie" -> "productie". Left uncredited (publisher).
- Grondwet art-016: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: adds "het". Left uncredited (publisher).
- Grondwet art-017: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "privé-leven," -> "privéleven,". Left uncredited (publisher).
- Grondwet art-026: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "produktie." -> "productie.". Left uncredited (publisher).
- Grondwet art-027: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "produktie." -> "productie.". Left uncredited (publisher).
- Grondwet art-031: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "4." -> "3.". Left uncredited (publisher).
- Grondwet art-038: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "sociaal-rechtvaardige" -> "sociaalrechtvaardige". Left uncredited (publisher).
- Grondwet art-039: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "produktieve" -> "productieve". Left uncredited (publisher).
- Grondwet art-048: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "produkten" -> "producten". Left uncredited (publisher).
- Grondwet art-056: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: drops "oorlog". Left uncredited (publisher).
- Grondwet art-078: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "ontworpen" -> "ontwerpen". Left uncredited (publisher).
- Grondwet art-084: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "de" -> "De". Left uncredited (publisher).
- Grondwet art-115: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "vastgesteld;" -> "vastgesteld.". Left uncredited (publisher).
- Grondwet art-133: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "ledenplaatsvervangers" -> "leden-plaatsvervangers"; "ledenplaatsvervangers" -> "leden-plaatsvervangers". Left uncredited (publisher).
- Grondwet art-142: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: adds "-"; adds "-". Left uncredited (publisher).
- Grondwet art-150: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "onder-voorzitter," -> "ondervoorzitter,". Left uncredited (publisher).
- Grondwet art-154: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "produktieve" -> "productieve". Left uncredited (publisher).
- Grondwet art-160: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "no.24)" -> "no.24).". Left uncredited (publisher).
- Grondwet art-169: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "bevoegheid" -> "bevoegdheid". Left uncredited (publisher).
- Grondwet art-170: S.B. 2025 no. 15 differs from the 1992 consolidation with no amending law: "Disticts-commissariaat" -> "Districtscommissariaat". Left uncredited (publisher).

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Opus 5.5 (claude-opus-5-5, Claude Code) researched the sources and wrote fetch.py and parse.py. It viewed the 6 page images of S.B. 2023 no. 157 to identify the amending act and its commencement clause and to compare its wording of arts. 60, 61, 161 and 163 with S.B. 2025 no. 15 (one difference found and recorded in decisions, not applied); no legal text in this corpus was written, transcribed or OCRed by a model: all text comes from PDF text layers via PyMuPDF.
