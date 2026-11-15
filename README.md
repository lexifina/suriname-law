# Suriname: law history in git

The law of Suriname as a git history: one file per article, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Suriname's national law, which global-law reads at `suriname/national/acts/`.

**What is in it now:** 8 acts with 11 versions: the Grondwet (the Constitution) in 3 versions, from the 1992 consolidation to today's official text (S.B. 2025 no. 15); the new Burgerlijk Wetboek (Civil Code, Books 1 to 8) and Wetboek van Burgerlijke Rechtsvordering (Code of Civil Procedure) of 2024, in force since 1 May 2025; today's official text of the Kiesregeling (electoral law); and four acts of 2024-2025 as enacted: the Algemene termijnenwet, the Handelsregisterwet, the Wet Kinderombudspersoon and the Wet Spaar- en Stabilisatie Fonds Suriname 2024 (2 versions, the second its correction by S.B. 2025 no. 103). [`REPRODUCE.md`](REPRODUCE.md) lists every act with its versions.

Each act is a folder, one file per article: `grondwet/art-061.md` is Article 61 of the Grondwet (the National Assembly and how it is elected); the Burgerlijk Wetboek numbers each Book's articles on its own (`burgerlijk-wetboek/boek-6-art-0162.md` is art. 6:162, the tort article). Headings are kept apart, in the `indeling.md` files, and each folder's `README.md` lists every article.

The text is in Dutch, the official language of Suriname, as the Staatsblad prints it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 61 of the Grondwet | `git log -p --word-diff -- grondwet/art-061.md` |
| Which law wrote each line of Article 61? | `git blame grondwet/art-061.md` |
| Every version of Article 61, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- grondwet/art-061.md` |
| Article 61 as in force on 1 January 2020 | `python tools/geldend_op.py 2020-01-01 grondwet 61` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Surinamese law](https://global-law.lexifina.com/v1/try_claude?country=suriname)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=suriname)**: the same question in ChatGPT.
- **[Search Surinamese law on our site](https://lexifina.com/law?country=suriname&q=onrechtmatige+daad)**: a search for "onrechtmatige daad" (tort), with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=onrechtmatige+daad&jurisdiction=suriname)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Dutch or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add suriname/national/acts
python3 tools/law.py show 2026-01-01 suriname/national/acts/grondwet/art-061.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Paramaribo, on the day the version took effect, and carries it in its `In-force:` trailer (the enactment and Staatsblad days are in `Enacted:` and `Published:`):

- a law binds from its afkondiging in the Staatsblad unless it sets another day (Grondwet art. 80 lid 1; Wet Algemene Bepalingen art. 1); most take effect the day after, as S.B. 2023 no. 157 did on 27 October 2023;
- the 2024 codes, the Algemene termijnenwet and the Handelsregisterwet took effect on 1 May 2025, the day Resolutie S.B. 2025 no. 14 set;
- the first Grondwet version is dated 8 April 1992, the date of the amending Wet, whose Staatsblad issue is not online, so the real day may be a few days later; the official texts of the Grondwet and the Kiesregeling republished on 7 February 2025 (S.B. 2025 nos. 15 and 16) are dated that day, when their text appeared.

A change is credited to a law only when the official consolidation's footnote names it ("Gew. bij S.B. 2023 no. 157"), and an act as enacted to the act itself. The oldest text available of the Grondwet and the Kiesregeling, and the 20 differences in S.B. 2025 no. 15 that no law explains (labelled "unexplained"), are credited to the Staatsblad. The committer is always Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before; both must match the corpus the history was built from. It also checks that every commit's trailers parse, that there are no merge commits and that nothing is dated in the future. Results are in [`REPRODUCE.md`](REPRODUCE.md): 11 versions of 8 acts, 0 mismatches.
- A second build from the same corpus gave identical commit hashes.
- Every text comes from a PDF's own text layer, never OCR, and every word of law in each PDF was checked to be in the files in order, apart from headings and words joined across a line-end hyphen (for the 2024 codes and the later acts, with a second, independent extractor).
- The 1992 Grondwet was compared with two other copies (gov.sr and the sris.sr edition with the memorie van toelichting), and the 2023 wording with the page images of S.B. 2023 no. 157, a scan; the one difference, a comma in art. 161 lid 4, is recorded in `REPRODUCE.md`, not applied.

## What it does not show

- **The Grondwet of 1987 as enacted, and the 1992 amendment as a change.** Neither S.B. 1987 no. 116 nor S.B. 1992 no. 38 is online in any official copy found, so the history starts with the 1992 consolidation.
- **The Wetboek van Strafrecht, and the old Civil Code and Code of Civil Procedure before 2025.** Their later amending acts are not all online with a text layer (most are scans), and this record uses no OCR; Boek 7A of the new Civil Code, which would have to be rebuilt on the old code, is left out too.
- **Earlier versions of the Kiesregeling.** The 2019 and 2023 amending acts are scans, and the 2024 and 2025 ones give only their changes.
- **Other acts.** Acts on sris.sr whose PDFs carry only a scanner's text layer (such as the Comptabiliteitswet 2024) are not built; court rulings and bills are not here.
- **Footnotes and the memorie van toelichting** are not in the text; the footnotes are used only to credit laws.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [De Nationale Assemblée, Surinaamse wetten](https://www.dna.sr/wetgeving/surinaamse-wetten/) | Official legislation | consolidations to 2005, then Staatsblad issues | The 1992 Grondwet consolidation and S.B. 2023 no. 157 |
| [Surinaams Rechtsinformatiesysteem](https://www.sris.sr/) | Official Staatsblad texts | as published | Today's Grondwet and Kiesregeling, the 2024 codes and the four acts of 2024-2025 |
| [Government of Suriname](https://gov.sr/) | Official copy | no | A copy of the 1992 consolidation, used only as a cross-check |

## Licence

See [`LICENSE`](LICENSE). The texts are official texts of the Republic of Suriname, published in the Staatsblad and read from De Nationale Assemblée and sris.sr; neither publishes a licence, their copyright status is not confirmed, and they are reproduced with that attribution. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model, which also viewed the page images of S.B. 2023 no. 157 to compare its wording (see [`REPRODUCE.md`](REPRODUCE.md)).

## In het Nederlands

De geschiedenis van het Surinaamse recht in git: één bestand per artikel, één commit per versie op de dag van inwerkingtreding, en als auteur van elke commit de wet die de wijziging aanbracht. Het bevat 8 wetten met 11 versies: de Grondwet vanaf de geconsolideerde tekst van 1992 tot de thans geldende tekst (S.B. 2025 no. 15), het nieuwe Burgerlijk Wetboek en Wetboek van Burgerlijke Rechtsvordering (in werking sinds 1 mei 2025), de thans geldende tekst van de Kiesregeling, en de Algemene termijnenwet, de Handelsregisterwet, de Wet Kinderombudspersoon en de Wet Spaar- en Stabilisatie Fonds Suriname 2024, zoals vastgesteld. Het Wetboek van Strafrecht en de oude wetboeken vóór 2025 ontbreken: de latere wijzigingswetten zijn alleen als scan beschikbaar en er wordt geen OCR gebruikt. Geldende tekst op een datum: `python tools/geldend_op.py 2020-01-01 grondwet 61`; `git blame grondwet/art-061.md` noemt de wet achter elke alinea.

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
