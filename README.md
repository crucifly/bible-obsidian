<div align="center">

# 🕊️ The Divine Vault ☦️

### A Verse-Level Canonical Dataset for the Ethiopian 81-Book Bible

**41,148 verses** · **7 canonical sections** · **81 books** · **Zero interpretation**

Built by [BLXCKBOOK Labs](https://github.com/blackbooklabs) for the JEXXXUS Theological Intelligence Engine

---

![Status](https://img.shields.io/badge/verses-41%2C148-gold?style=for-the-badge)
![Canon](https://img.shields.io/badge/canon-Ethiopian--81-darkred?style=for-the-badge)
![Format](https://img.shields.io/badge/format-Obsidian%20%2B%20JSONL-7C3AED?style=for-the-badge)
![License](https://img.shields.io/badge/license-Public%20Domain%20(Scripture)-333?style=for-the-badge)

</div>

---

<div align="center">
  <img src=".github/social-preview.png" alt="The Divine Vault Social Preview" width="100%">
</div>

---

## What Is This?

The Divine Vault is a **machine-readable, verse-level decomposition** of the complete Ethiopian Orthodox Tewahedo 81-book biblical canon. Every verse exists as an individual Markdown file with structured YAML frontmatter, designed to serve as the **Source of Truth** for fine-tuning large language models on canonical scripture.

This is not a study Bible. There is no commentary, no interpretation, no opinion. Every file contains exactly one verse and its canonical metadata — nothing more.

### The Iron Curtain

A strict validation rule governs this vault: only files tagged with `source_type: Scripture` are permitted to enter the training pipeline. Any file containing subjective language, commentary, or interpretation is quarantined. This architectural constraint — the **Iron Curtain** — ensures that downstream models trained on this data produce verbatim canonical output rather than hallucinated theology.

---

## Vault Structure

```text
bible-obsidian/
├── 00_META/                        # Manifesto & governance
├── 00_Schema.md                    # YAML frontmatter specification
├── 01-Torah/                       # Genesis → Deuteronomy (5,852 verses)
│   ├── 01-Genesis/
│   │   ├── Chapter 1/
│   │   │   ├── 1-1.md             # Individual verse file
│   │   │   ├── 1-2.md
│   │   │   └── ...
│   │   └── ...
├── 02-Historical/                  # Joshua → Esther (7,018 verses)
├── 03-Poetic/                      # Job → Song of Solomon (4,792 verses)
├── 04-Prophets/                    # Isaiah → Malachi (5,470 verses)
├── 05-Deuterocanonical/            # Tobit → 3 Maccabees (5,970 verses)
├── 06-NewTestament/                # Matthew → Revelation (7,885 verses)
├── 07-EthiopicApocrypha/           # The broader Ethiopian canon (4,151+ verses)
│   ├── 67-1Enoch/                  #   1,029 verses (108 chapters)
│   ├── 68-Jubilees/                #   1,640 verses (50 chapters)
│   ├── 69-KebraNagast/             #   533 verses (117 chapters)
│   ├── 70-PsalmsOfSolomon/         #   321 verses (18 psalms)
│   ├── 71-2Enoch/                  #   372 verses (68 chapters)
│   ├── 72-ApostolicConstitutions/  #   Horner Statutes (70 Statutes)
│   └── 73-Didascalica/              #   Harden Didascalia (41 Chapters)
├── 08-NagHammadi/                  # Gnostic Codices & "Secret Sayings"
│   ├── GospelOfThomas/             #   114 Logia (Sayings)
│   ├── GospelOfTruth/              #   19 Thematic Sections
│   └── GospelOfPhilip/             #   68 Theological Aphorisms
├── scripts/                        # Ingestion parsers & JSONL forge
├── divine_training_set.jsonl       # Pre-built training corpus (41,148 rows)
├── CANON_INVENTORY.md              # Master tracking document
└── COVERAGE_TRACKING.md            # Ingestion progress metrics
```

---

## Verse File Format

Every verse file follows a strict schema. Example — `01-Torah/01-Genesis/Chapter 1/1-1.md`:

```yaml
---
id: GEN-1-1
canon: Masoretic
book: Genesis
chapter: 1
verse: 1
source_type: Scripture
---

In the beginning, God created the heavens and the earth.
```

For the Ethiopic Apocrypha, additional metadata flags are included:

```yaml
---
id: 1ENOCH-1-1
canon: Ethiopian-81
canon_tier: broader
book: 1 Enoch
chapter: 1
verse: 1
source_type: Scripture
---

The words of the blessing of Enoch, wherewith he blessed the elect and righteous, who will be living in the day of tribulation, when all the wicked and godless are to be removed.
```

The `canon_tier` field allows downstream models to distinguish between core canon (`Masoretic`, `Septuagint`) and the broader Ethiopian tradition, enabling nuanced theological reasoning without conflating sources.

---

## Training Data Format

The `divine_training_set.jsonl` file contains one JSON object per line, structured for instruction-tuned LLM fine-tuning:

```json
{
  "instruction": "Provide the text for Genesis 1:1 from the Masoretic canon.",
  "thinking": "This verse is identified as ID GEN-1-1 from the Masoretic canon. It is located in Genesis, Chapter 1, Verse 1. The response must be the verbatim text of the scripture to ensure zero interpretation.",
  "context": "Source: GEN-1-1 (Masoretic)",
  "response": "In the beginning, God created the heavens and the earth."
}
```

| Field | Purpose |
| :--- | :--- |
| `instruction` | The natural language query a user or agent would ask |
| `thinking` | Chain-of-thought reasoning block for the model's internal process |
| `context` | Canonical source identifier for grounding |
| `response` | Verbatim scripture — the only acceptable output |

> [!NOTE]
> The `thinking` field is specifically designed for models that support structured reasoning (Gemma 4, etc.), training the model to verify canonical source and location *before* producing output.

---

## Ingestion Coverage

| Section | Books | Verses | Status |
| :--- | :--- | :--- | :--- |
| Torah | 5 | 5,852 | ✅ Complete |
| Historical | 12 | 7,018 | ✅ Complete |
| Poetic | 5 | 4,792 | ✅ Complete |
| Prophets | 17 | 5,470 | ✅ Complete |
| Deuterocanonical | 15 | 5,970 | ✅ Complete |
| New Testament | 27 | 7,885 | ✅ Complete |
| Ethiopic Apocrypha | 8 | 7,397+ | ✅ Complete |
| Nag Hammadi | 3 | 201+ | ✅ Complete |
| **Total** | **84+** | **48,746+** | **100% of Target Canon** |

---

## Scripts

The `scripts/` directory contains the Node.js ingestion pipeline:

| Script | Purpose |
| :--- | :--- |
| `jsonl-forge-plain.js` | Walks the entire vault and generates `divine_training_set.jsonl` |
| `chunk_apostolic.js` | Parses the Apostolic Constitutions (Book → Chapter → Verse) |
| `chunk_didascalia.js` | Parses the Didascalia Apostolorum (Chapter → Verse) |

Additional parsers exist in the parent project directory for 1 Enoch, 2 Enoch, Jubilees, Kebra Nagast, Psalms of Solomon, and 4 Ezra.

### Regenerating the Training Set

```bash
node scripts/jsonl-forge-plain.js
```

This will crawl all `.md` files in the vault, validate the `source_type: Scripture` tag (Iron Curtain), and output a fresh `divine_training_set.jsonl`.

---

## Fine-Tuning Architecture

This dataset is designed for **QLoRA fine-tuning** on Gemma 4 using the following stack:

| Component | Choice | Rationale |
| :--- | :--- | :--- |
| Framework | Unsloth + Axolotl | Optimized for Gemma; 2-5x speedup |
| Method | QLoRA (4-bit) | Preserves base model reasoning |
| Rank | r=64 to r=128 | High capacity for dense theological text |
| Target Modules | All linear layers | Maximum absorption of canonical structure |
| Dataset | `divine_training_set.jsonl` | 41,148 instruction/response pairs |

> [!TIP]
> The QLoRA approach ensures that the base model's general intelligence remains intact while the adapter layers absorb the full weight of the 81-book canon. The model learns to *reason with* scripture rather than merely recite it.

---

## Theological Scope

This vault encompasses the complete **Ethiopian Orthodox Tewahedo** biblical canon — the largest canonical Bible in Christendom at 81 books. It includes texts not found in the Western Protestant (66), Catholic (73), or Eastern Orthodox (76) canons:

- **1 Enoch** — The Watchers, the Parables, the Astronomical Book, the Dream Visions, and the Epistle of Enoch
- **Jubilees** — The "Little Genesis"; detailed patriarchal chronology
- **Kebra Nagast** — The Glory of Kings; the Solomonic lineage of Ethiopia
- **2 Enoch** — The Slavonic Apocalypse; the secrets of the heavens
- **Psalms of Solomon** — Messianic psalms from the Second Temple period
- **Apostolic Constitutions** — Church law and liturgical order (Horner)
- **Didascalia** — Pastoral teachings and ecclesiastical governance (Harden)
- **Nag Hammadi Library** — Primary Gnostic codices including the Gospel of Thomas, Gospel of Truth, and Gospel of Philip

---

## Usage with Obsidian

This vault is fully compatible with [Obsidian](https://obsidian.md). Open the `bible-obsidian` directory as a vault to get:

- Full-text search across all 41,148 verses
- Graph view of canonical relationships
- Backlink navigation between cross-referenced passages
- Local-first, offline access to the complete Ethiopian canon

---

## Contributing

This is a **Source of Truth** repository. Contributions must adhere to the Iron Curtain:

1. Every verse file must include valid YAML frontmatter per `00_Schema.md`
2. The `source_type: Scripture` tag is mandatory
3. Zero commentary, interpretation, or subjective language
4. All text must come from authorized public domain translations

---

<div align="center">

*"The words of the blessing of Enoch, wherewith he blessed the elect and righteous."*<br>
— **1 Enoch 1:1**

**BLXCKBOOK Labs** · [github.com/blackbooklabs](https://github.com/blackbooklabs)

</div>
