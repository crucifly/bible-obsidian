<div align="center">

# 🕊️ The Divine Vault ☦️

### A Verse-Level Canonical Dataset for the Expanded Biblical, Ethiopic, Gnostic & Pseudepigraphal Canon

**46,836 verses** · **2,002 chapter files** · **10 canonical sections** · **Zero interpretation**

Built by **Crucifly, LLC** for the JEXXXUS Theological & Gnostic Intelligence Engine

---

</div>

---

<div align="center">
  <img src=".github/social-preview.png" alt="The Divine Vault Social Preview" width="100%">
</div>

---

## 📖 Overview & Purpose

**The Divine Vault** is a machine-readable, verse-level decomposition of the complete **expanded biblical canon**, encompassing the Masoretic Text, the Septuagint Deuterocanon, the New Testament, the Ethiopian Orthodox Tewahedo broader canon, the Nag Hammadi Gnostic Library, the Classical Pseudepigrapha, and the Corpus Hermeticum.

Every verse exists as a `### N` header inside an individual Markdown chapter file with structured YAML frontmatter, designed to serve as the **Source of Truth** for training, fine-tuning, and RAG (Retrieval-Augmented Generation) across large language models.

This vault contains **zero commentary, zero interpretation, and zero subjective opinions**—only verbatim scripture and canonical metadata.

---

## 🛡️ The Iron Curtain Directive

A strict validation rule governs this vault: only files tagged `source_type: Scripture` (canonical texts) or `source_type: Gnostic-Codex` (Nag Hammadi codices) are permitted to enter fine-tuning pipelines. Any file containing subjective commentary, modern commentary, or web-navigation noise is quarantined and purged.

This architectural constraint—the **Iron Curtain**—ensures that AI models trained on this repository produce accurate, verbatim canonical output rather than hallucinated theology.

---

## 📂 Vault Structure

```text
bible-obsidian/
├── 00_META/                          # Governance, manifestos, & core contracts
├── 00_Schema.md                      # YAML frontmatter specification & schema
├── 01-Torah/                         # Genesis → Deuteronomy (5,148 verses)
│   ├── 01-Genesis/Chapter 01.md
│   ├── 01-Genesis/Chapter 02.md
│   └── ...
├── 02-Historical/                    # Joshua → Esther (6,306 verses)
│   └── ...
├── 03-Poetic/                        # Job → Song of Solomon (4,396 verses)
│   └── ...
├── 04-Prophets/                      # Isaiah → Malachi (5,017 verses)
│   └── ...
├── 05-Deuterocanonical/              # Tobit → 3 Maccabees (3,173 verses)
│   └── ...
├── 06-New Testament/                 # Matthew → Revelation (6,896 verses)
│   └── ...
├── 07-Ethiopic Apocrypha/            # Ethiopian Orthodox Broad Canon (4,367 verses)
│   ├── 1 Enoch/                      #   108 chapters
│   ├── Jubilees/                     #   50 chapters
│   ├── Kebra Nagast/                 #   117 chapters
│   ├── Psalms of Solomon/            #   18 psalms
│   ├── 2 Enoch/                      #   68 chapters
│   ├── Apostolic Constitutions/      #   Horner Statutes (969 verses)
│   │   └── Horner Statutes/Chapter 01.md
│   ├── Didascalia/                   #   Harden Didascalia (41 chapters)
│   └── ...
├── 08-Nag Hammadi/                   # Gnostic Library & Coptic Codices (4,485 notes)
│   ├── Apocryphon of John/
│   ├── Gospel of Thomas/
│   ├── Gospel of Philip/
│   ├── Gospel of Mary/               #  Berlin Codex 8502—ch. 4, 5, 8, 9
│   ├── Poimandres/                   #  Corpus Hermeticum—G.R.S. Mead trans.
│   └── ...
├── 09-Pseudepigrapha/                # Old Testament Pseudepigrapha (7,047 notes)
│   ├── Book of Jasher/               #   Chapters 01 → 91
│   ├── Testaments of the Twelve Patriarchs/
│   ├── Sibylline Oracles/
│   ├── Ascension of Isaiah/
│   ├── Odes of Solomon/
│   └── ...
├── 12-Hermetic/                      # Corpus Hermeticum (1 note)
│   └── Poimandres/Chapter 01.md       #  Thrice-Greatest Hermes vol. 2, Mead 1906
├── scripts/
│   └── extract_headings.cjs          #  Lifts ALL-CAPS section headings from verse text
├── CANON_INVENTORY.md                # Master 117-book tracking inventory
└── COVERAGE_TRACKING.md              # Ingestion progress metrics
```

---

## 📊 Canon Breakdown

| Section | Classification | Chapter Files | Notes | Primary Source |
| :--- | :--- | ---: | ---: | :--- |
| **01** | Torah | 187 | 5,148 | Masoretic / LXX |
| **02** | Historical | 249 | 6,306 | Masoretic / LXX |
| **03** | Poetic & Wisdom | 244 | 4,396 | Masoretic / LXX |
| **04** | Prophets | 250 | 5,017 | Masoretic / LXX |
| **05** | Deuterocanonical | 177 | 3,173 | Septuagint (LXX) |
| **06** | New Testament | 260 | 6,896 | WEB (Public Domain) |
| **07** | Ethiopic Apocrypha | 366 | 4,367 | Ge'ez Manuscripts (Budge / Horner) |
| **08** | Nag Hammadi & Gnostic Codices | 169 | 4,485 | Coptic Library (gnosis.org) |
| **09** | Pseudepigrapha & Lost Books | 99 | 7,047 | Wikisource / EarlyChristianWritings |
| **12** | Hermetica | 1 | 1 | G.R.S. Mead, gnosis.org |
| **TOTAL** | **The Divine Vault Ecosystem** | **2,002** | **46,836** | **Canonical & Extracanonical** |

---

## 🛠️ YAML Frontmatter Specification

Every chapter file starts with YAML frontmatter:

```yaml
---
book: "Genesis"
chapter: 1
canon: "Torah"
source_type: Scripture
id: GEN-01
---
```

Every verse is a `### N` header block:

```markdown
### 1
In the beginning God created the heavens and the earth.
```

---

## 🛠️ Technology Stack & Tools

- **Markup & Storage**: Obsidian Markdown (GFM) with YAML Frontmatter
- **Scripting**: Python 3.12, Node.js
- **Rendering**: Next.js SSG (`bible.jexxx.us`) driven by `public/data/books/*.json`
- **Git Integration**: Automated sync with `Crucifly/bible-obsidian`

---

## 🤝 Contribution & Governance

Maintained by **Crucifly, LLC** under the **JEXXXUS Ecosystem** DOX Framework contract.

- **Organization**: Crucifly, LLC
- **Repository**: [git@github.com:Crucifly/bible-obsidian.git](https://github.com/Crucifly/bible-obsidian)
- **DOX Contract**: see `AGENTS.md` in the parent `JEXXXUS` workspace

---

**Crucifly, LLC · Absolute Digital Sovereignty** ⚡
