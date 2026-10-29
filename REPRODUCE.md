# How this repository was made (Suriname)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| De Nationale Assemblee, Surinaamse wetten | <https://www.dna.sr/wetgeving/surinaamse-wetten/> | 2026-10-28 | Official legislative text; no licence stated |
| Surinaams Rechtsinformatiesysteem (sris.sr) | <https://sris.sr/> | 2026-10-28 | Official Staatsblad text; no licence stated |
| Government of Suriname (gov.sr) | <https://gov.sr/> | 2026-10-28 | Official text; no licence stated |
| Surinaams Rechtsinformatiesysteem (sris.sr) | <https://www.sris.sr/> | 2026-10-29 | Official Staatsblad text; no licence stated |
| Surinaams Rechtsinformatiesysteem (sris.sr) | <https://www.sris.sr/> | 2026-10-29 | Official Staatsblad text; no licence stated |
| Surinaams Rechtsinformatiesysteem (sris.sr) | <https://www.sris.sr/> | 2026-10-29 | Official Staatsblad text; no licence stated |
| Surinaams Rechtsinformatiesysteem (sris.sr) | <https://www.sris.sr/> | 2026-10-29 | Official Staatsblad text; no licence stated |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `grondwet` | Grondwet van de Republiek Suriname | 3 | 1992-04-08 to 2025-02-07 |
| `burgerlijk-wetboek` | Burgerlijk Wetboek (Boeken 1-8) | 1 | 2025-05-01 to 2025-05-01 |
| `rechtsvordering` | Wetboek van Burgerlijke Rechtsvordering | 1 | 2025-05-01 to 2025-05-01 |
| `kiesregeling` | Kiesregeling | 1 | 2025-02-07 to 2025-02-07 |
| `algemene-termijnenwet` | Algemene termijnenwet | 1 | 2025-05-01 to 2025-05-01 |
| `handelsregisterwet` | Handelsregisterwet | 1 | 2025-05-01 to 2025-05-01 |
| `kinderombudspersoon` | Wet Kinderombudspersoon | 1 | 2025-01-23 to 2025-01-23 |
| `spaar-en-stabilisatiefonds` | Wet Spaar- en Stabilisatie Fonds Suriname 2024 | 2 | 2025-01-01 to 2025-07-29 |

The build made 11 commits:

| Commits | Kind |
| ---: | --- |
| 8 | first version of an act |
| 2 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `toekomst`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 21 laws in the record.
- 19 tags.

## Dates

Each commit is dated at noon (America/Paramaribo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Grondwet art. 80 lid 1: laws "verkrijgen kracht van wet na afkondiging"; art. 118 leaves the manner and moment to the law; Wet Algemene Bepalingen (G.B. 1868 no. 14) art. 1: no regulation binds before its afkondiging. So a law binds from its afkondiging in the Staatsblad, unless its own slotbepaling sets another day (most say "de dag volgende op die van haar afkondiging"). https://sris.sr/wp-content/uploads/2025/04/ (S.B. 2025 no. 15, arts. 80 and 118); https://www.dna.sr/media/frtc5hy3/wet_algemene_bepalingen.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `321d05bbb988c202e8fbb76ae08588ccd5f46f41fb0d43453fababc74267153b` (3134528 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

11 versions of 8 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 11 history commits and 19 tags (history tip `1b104808dbe16d49378f98a325f78dc645acc18e`).

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
- Wetboek van Strafrecht and the old Burgerlijk Wetboek (G.B. 1860 no. 4) not included: no official consolidation after 2005, and later amending acts (WvSr: S.B. 2023 no. 133 and S.B. 2023 no. 135 scans with OCR layers, S.B. 2020 no. 42 uncorrected OCR layer, S.B. 2014 no. 118 scan, S.B. 2017 no. 85 not listed; old BW: 2016 and S.B. 2022 no. 34 scans) cannot be applied from official text, so no text in force today could be built and checked. The new Burgerlijk Wetboek of 2024 is built (corpus.d part 20-burgerlijk-wetboek). No data protection law is in force: sris.sr holds only a bill, the Ontwerpwet Bescherming Privacy en Persoonsgegevens (2020).
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
- Burgerlijk Wetboek: the act is the new code of 2024, Boeken 1 to 8 (S.B. 2024 no. 164), from the day it took effect, 2025-05-01. It replaced the code of 1860 (G.B. 1860 no. 4), whose last official consolidation (dna.sr) runs only to 2005 and whose later amending acts (2016, S.B. 2022 no. 34) are scans without a text layer, so the old code's history is not built.
- Burgerlijk Wetboek: Boek 7A is left out. It is what remains of the old code's Derde Boek (hire-purchase, loans and other contracts), renumbered and amended by the Aanpassingswet nieuw Burgerlijk Wetboek (S.B. 2024 no. 168, art. I), which gives only the changes; its full text would have to be replayed onto the 2005 consolidation of the old code across the 2016 and 2022 scans.
- Burgerlijk Wetboek: each Book numbers its own articles, so unit keys are boek-<n>-art-<number>, zero-padded to four digits (boek-1-art-0025a). The closing provision of Boek 8, printed under the heading "ALGEMENE SLOTBEPALING" without an article number, is the unit boek-8-algemene-slotbepaling.
- Burgerlijk Wetboek: the enacting wet's own articles 1 and 2 (adoption of the Books, citation title, commencement by presidential decree) are not part of the code text and are left out.
- Both 2024 codes took effect on 2025-05-01: Resolutie of 6 February 2025 no. 2909/25 (S.B. 2025 no. 14), besluit I, fixes that day for S.B. 2024 nos. 164 to 170 (art. 2 lid 3 of the BW wet and art. 1079 lid 3 of the Rv let the President set it).
- No amending act of either code was found in the sris.sr media listing (every Staatsblad PDF the site holds, to October 2026) or in the DNA lists "Wetten na 2005" and "Wijzigingen na 2005" (read 2026-10-28): each code has one version, its text as enacted, in force since 2025-05-01. Only bills (ontwerpwetten) are pending, such as the Ontwerpwet houdende wijziging van het Wetboek van Burgerlijke Rechtsvordering (sris.sr, August 2026).
- Paragraphs: the PDFs set every article in lines of about 100 characters. A line starts a new paragraph when it begins with a list marker ("1.", "a.", "2°") or when its first word would have fitted on the line before; otherwise lines are joined. A paragraph that ends exactly at the right margin and is followed by an unnumbered paragraph is therefore joined to it; the words are unaffected.
- Line-end hyphens: a word broken at a line end is joined without the hyphen unless the hyphenated form occurs more often inside lines of the same code than the closed form (kept: "proces-verbaal", "mede-erfgenaam", "netto-opbrengst", "averij-grosse", "niet-bevrijdende", "aandeelhouder-bestuurde", "rechter-commissaris", "niet-ontvankelijkheid", "Procureur-generaal").
- Headings (Boek, Titel, Afdeling, paragraaf) are kept in indeling units, so article files hold only article text. The memories van toelichting printed after each Book are not law text and are left out.
- Completeness: the law-text pages are read again with PyMuPDF's word extractor and aligns the words with the units. Every word is in the units in order; the only differences are headings, each Book's title page, the enacting formula and signatures, a line-end join next to a heading, the full stop of the heading "Artikel 518b." (Boek 8) and the capitalisation of the heading "ALGEMENE SLOTBEPALING" in its unit's title.
- Wetboek van Burgerlijke Rechtsvordering: the act is the new code of 2024 (S.B. 2024 no. 170) from the day it took effect, 2025-05-01. The code it replaced (G.B. 1935, consolidated by dna.sr to 2005, amended by S.B. 2008 no. 19 and others) is not built: its amending acts after 2005 were not all found with a text layer.
- Wetboek van Burgerlijke Rechtsvordering: the code numbers its articles straight through its four Books (Artikel A and B, then 1 to 1079, with gaps where numbers are unused), so unit keys are art-<number> zero-padded to four digits, and art-a and art-b. Book, title and section headings are in rechtsvordering/indeling.md.
- Both 2024 codes took effect on 2025-05-01: Resolutie of 6 February 2025 no. 2909/25 (S.B. 2025 no. 14), besluit I, fixes that day for S.B. 2024 nos. 164 to 170 (art. 2 lid 3 of the BW wet and art. 1079 lid 3 of the Rv let the President set it).
- No amending act of either code was found in the sris.sr media listing (every Staatsblad PDF the site holds, to October 2026) or in the DNA lists "Wetten na 2005" and "Wijzigingen na 2005" (read 2026-10-28): each code has one version, its text as enacted, in force since 2025-05-01. Only bills (ontwerpwetten) are pending, such as the Ontwerpwet houdende wijziging van het Wetboek van Burgerlijke Rechtsvordering (sris.sr, August 2026).
- Paragraphs: the PDFs set every article in lines of about 100 characters. A line starts a new paragraph when it begins with a list marker ("1.", "a.", "2°") or when its first word would have fitted on the line before; otherwise lines are joined. A paragraph that ends exactly at the right margin and is followed by an unnumbered paragraph is therefore joined to it; the words are unaffected.
- Line-end hyphens: a word broken at a line end is joined without the hyphen unless the hyphenated form occurs more often inside lines of the same code than the closed form (kept: "proces-verbaal", "mede-erfgenaam", "netto-opbrengst", "averij-grosse", "niet-bevrijdende", "aandeelhouder-bestuurde", "rechter-commissaris", "niet-ontvankelijkheid", "Procureur-generaal").
- Headings (Boek, Titel, Afdeling, paragraaf) are kept in indeling units, so article files hold only article text. The memories van toelichting printed after each Book are not law text and are left out.
- Completeness: the law-text pages are read again with PyMuPDF's word extractor and aligns the words with the units. Every word is in the units in order; the only differences are headings, each Book's title page, the enacting formula and signatures, a line-end join next to a heading, the full stop of the heading "Artikel 518b." (Boek 8) and the capitalisation of the heading "ALGEMENE SLOTBEPALING" in its unit's title.
- Kiesregeling: one version, the official current text S.B. 2025 no. 16, dated 2025-02-07, the day it was uitgegeven, and committed by the publisher as the oldest version available. The last amendment it contains, S.B. 2025 no. 8 (uitgegeven 20 January 2025, in force the next day by its art. II lid 2), took effect on 2025-01-21; the version is dated from its own source, the republication, rather than from that day.
- Kiesregeling: earlier versions are not built. The amending acts S.B. 2019 no. 55 and S.B. 2023 no. 158 and the 2005 consolidation exist online only as scans (the sris.sr copies carry an OCR layer made by the publisher's scanner software), and no OCR is used for this record; S.B. 2024 no. 59 and S.B. 2025 no. 8 have a born-digital text layer, but they give only the changed provisions, not the text before them.
- Kiesregeling: no amending act after S.B. 2025 no. 8 was found: the DNA list "Wijzigingen na 2005" ends with it (read 2026-10-29) and the sris.sr listing holds only later Kiesbesluit decrees (S.B. 2025 nos. 25, 26, 38, 39), which are not part of the Kiesregeling.
- Kiesregeling: S.B. 2025 no. 16 footnotes each article with the act that inserted or changed it ("Gew. bij S.B. 2023 no. 158"). The footnotes and their reference numbers are left out of the text (they are publisher notes, not law), and the opening paragraph that names the act and its amendments is the act's title, not a provision.
- Kiesregeling: chapter and paragraph headings are in kiesregeling/indeling.md. Its paragraphs and line-end hyphens are handled as for the 2024 codes, and every 12-point word of the text is found in the units, in order, apart from headings and the opening paragraph.
- Algemene termijnenwet (S.B. 2024 no. 167): one version as enacted, in force on 1 May 2025, the day the new Burgerlijk Wetboek took effect (art. 6 lid 3; Resolutie S.B. 2025 no. 14), but only for terms set in or under the Burgerlijk Wetboek, the Wetboek van Burgerlijke Rechtsvordering, the Wetboek van Koophandel and the Faillissementswet; for other terms commencement is left to a later act (art. 6 lid 4), and none was found.
- Handelsregisterwet (S.B. 2024 no. 169): one version as enacted, in force on 1 May 2025, the day the new Burgerlijk Wetboek took effect (its own closing article, lid 3; Resolutie S.B. 2025 no. 14).
- Wet Kinderombudspersoon (S.B. 2025 no. 1): one version as enacted, in force on 23 January 2025, the day after its afkondiging (uitgegeven 22 January 2025; its closing article, lid 3).
- Wet Spaar- en Stabilisatie Fonds Suriname 2024 (S.B. 2024 no. 179): as enacted, then corrected, in force on 1 January 2025, the day after its afkondiging (uitgegeven 31 December 2024; its closing article, lid 3).
- Wet Spaar- en Stabilisatie Fonds Suriname 2024: the verbeterblad S.B. 2025 no. 103 (uitgegeven 29 July 2025) is applied as a second version on that day, credited to it, instruction by instruction: art. 2 lid 4 "staatsinvesteringsfondsen" becomes "staatsbeleggingsfondsen"; the points under art. 9 lid 3 sub d, art. 11 lid 2 sub g and art. 13 lid 4 sub e are numbered 1, 2, 3 ... in place of their bullets (written "1.", "2.", ..., as the verbeterblad gives the numbers but not their printed form); in art. 13 lid 17 "behersovereenkomsten" and "rgeling" become "beheersovereenkomsten" and "regeling"; and art. 23 lid 1 gets "2024" after "Suriname" (the sentence already ends with a full stop). A verbeterblad corrects the printed text rather than changing the law, so the earlier version shows the text as first printed.
- Wet Spaar- en Stabilisatie Fonds Suriname 2024: S.B. 2024 no. 179 sets its bullets a few points below the top of each point's first line, so the line reader put each bullet on the point's second line; Lexifina's code moves it back in front of the point.
- Sources and amendments: each act was found in the sris.sr WordPress media listing (1,762 files, read 2026-10-29), which lists no amending act for any of them up to October 2026; the Aanpassingswet nieuw Burgerlijk Wetboek (S.B. 2024 no. 168) names the Algemene termijnenwet only to exclude terms from it, without amending it. Implementing decrees (for example the Handelsregisterbesluit, S.B. 2025 no. 46) are not part of these acts.
- Acts on sris.sr whose PDFs carry only a scanner's text layer (Comptabiliteitswet 2024, S.B. 2024 no. 178; Wet Toezicht Bank- en Kredietwezen 2023, S.B. 2024 no. 4; Wet Herstel en Afwikkeling Kredietinstellingen, S.B. 2024 no. 5) are not built: that text layer is OCR, not the publisher's own text.
- Reading: the same reader as the 2024 codes: headings go to the act's indeling unit, paragraphs are rebuilt from line widths, and line-end hyphens are resolved from the act's own vocabulary. The enacting formula, signatures and the Memorie van Toelichting are left out.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Opus 5.5 (claude-opus-5-5, Claude Code) researched the sources and wrote Lexifina's code. It viewed the 6 page images of S.B. 2023 no. 157 to identify the amending act and its commencement clause and to compare its wording of arts. 60, 61, 161 and 163 with S.B. 2025 no. 15 (one difference found and recorded in decisions, not applied); no legal text in this corpus was written, transcribed or OCRed by a model: all text comes from PDF text layers via PyMuPDF.
- Claude Opus 5.5 (claude-opus-5-5, Claude Code) found the sources and wrote Lexifina's code. No legal text in these parts was written, transcribed or OCRed by a model: all text comes from the PDF text layers via PyMuPDF.
- Claude Opus 5.5 (claude-opus-5-5, Claude Code) found the sources and wrote Lexifina's code. No legal text in these parts was written, transcribed or OCRed by a model: all text comes from the PDF text layers via PyMuPDF.
- Claude Opus 5.5 (claude-opus-5-5, Claude Code) found the sources and wrote Lexifina's code. No legal text in these parts was written, transcribed or OCRed by a model: all text comes from the PDF text layers via PyMuPDF.
- Claude Opus 5.5 (claude-opus-5-5, Claude Code) chose these acts and wrote Lexifina's code, including the replay of the verbeterblad S.B. 2025 no. 103 from its printed instructions. No legal text was written, transcribed or OCRed by a model: all text comes from the PDF text layers via PyMuPDF.
