<div align="center">

# 🕊️ The Divine Vault ☦️

### A Verse-Level Canonical Dataset for the 117-Book Expanded Biblical, Ethiopic, Gnostic & Pseudepigraphal Canon

**96,116 verses & structured sections** · **11 canonical sections** · **117 books** · **Zero interpretation**

Built by **Crucifly, LLC** for the JEXXXUS Theological & Gnostic Intelligence Engine

---

![Status](https://img.shields.io/badge/verses-96%2C116-gold?style=for-the-badge&logo=obsidian&logoColor=white)
![Canon](https://img.shields.io/badge/canon-117--Book%20Expanded%20Ecosystem-darkred?style=for-the-badge)
![Format](https://img.shields.io/badge/format-Obsidian%20%2B%20JSONL-7C3AED?style=for-the-badge&logo=markdown&logoColor=white)
![License](https://img.shields.io/badge/license-Public%20Domain%20(Scripture)-333?style=for-the-badge)
![GitHub Repo](https://img.shields.io/badge/GitHub-Crucifly%2Fbible--obsidian-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

---

## 📖 Overview & Purpose

**The Divine Vault** is a machine-readable, verse-level and section-level decomposition of the complete **117-book expanded biblical canon**, encompassing the 81-Book Ethiopian Orthodox Tewahedo Bible, the Nag Hammadi Gnostic Library, and the Old Testament Pseudepigrapha. 

Every single verse and section exists as an individual Markdown note with structured YAML frontmatter, designed to serve as the **Source of Truth** for training, fine-tuning, and RAG (Retrieval-Augmented Generation) across large language models.

This vault contains **zero commentary, zero interpretation, and zero subjective opinions** — only verbatim scripture and canonical metadata.

---

## 🛡️ The Iron Curtain Directive

A strict validation rule governs this vault: only files tagged with `source_type: Scripture` or `source_type: Gnostic-Codex` are permitted to enter fine-tuning pipelines. Any file containing subjective commentary, modern commentary, or web navigation noise is quarantined and purged. 

This architectural constraint — the **Iron Curtain** — ensures that AI models trained on this repository produce accurate, verbatim canonical output rather than hallucinated theology.

---

## 📂 Vault Structure

```text
bible-obsidian/
├── 00_META/                        # Governance, manifestos, & core contracts
├── 00_Schema.md                    # YAML frontmatter specification & schema
├── 01-Torah/                       # Genesis → Deuteronomy (5,852 verses)
│   ├── 01-Genesis/
│   │   ├── Chapter 01/
│   │   │   ├── 01-01.md            # Individual verse note with YAML
│   │   │   ├── 01-02.md
│   │   │   └── ...
│   │   └── ...
├── 02-Historical/                  # Joshua → Esther (7,018 verses)
├── 03-Poetic/                      # Job → Song of Solomon (4,792 verses)
├── 04-Prophets/                    # Isaiah → Malachi (5,470 verses)
├── 05-Deuterocanonical/            # Tobit → 3 Maccabees (5,970 verses)
├── 06-NewTestament/                # Matthew → Revelation (7,885 verses)
├── 07-EthiopicApocrypha/           # Ethiopian Orthodox Broad Canon (4,151+ verses)
│   ├── 1 Enoch/                    #   1,029 verses (108 chapters)
│   ├── Jubilees/                   #   1,640 verses (50 chapters)
│   ├── Kebra Nagast/               #   533 verses (117 chapters)
│   ├── Psalms of Solomon/          #   321 verses (18 psalms)
│   ├── 2 Enoch/                    #   372 verses (68 chapters)
│   ├── Apostolic Constitutions/    #   Horner Statutes (70 Statutes)
│   └── Didascalia/                 #   Harden Didascalia (41 Chapters)
├── 08-NagHammadi/                  # Gnostic Library & Coptic Codices (12,850+ notes)
│   ├── Gospel of Thomas/           #   114 Logia (Sayings)
│   ├── Gospel of Philip/           #   Structured theological sections
│   ├── Gospel of Truth/            #   Gnostic meditation sections
│   ├── Gospel of Mary/             #   Chapters 4, 5, 8, 9 with verse files
│   ├── Gospel of Judas/            #   Full Codex Tchacos translation
│   ├── Pistis Sophia/              #   Chapters 001 → 144 (Mead translation)
│   ├── Apocryphon of John/         #   Secret revelation of John
│   ├── Hypostasis of the Archons/  #   Reality of the Rulers
│   ├── On the Origin of the World/ #   Cosmological creation narrative
│   ├── Sophia of Jesus Christ/     #   Wisdom of Jesus Christ
│   ├── Dialogue of the Savior/     #   Dialogue between Jesus & disciples
│   ├── Tripartite Tractate/        #   Systematic Valentinian theology
│   ├── Trimorphic Protennoia/      #   First Thought in Three Forms
│   ├── Second Discourse of Great Seth/ # Secret Gnostic discourse
│   ├── Exegesis on the Soul/       #   Soul's fall & restoration
│   ├── Authoritative Teaching/     #   Soul's origin & destiny
│   ├── Concept of Our Great Power/ # Apocalyptic vision of the Aeons
│   ├── Thunder, Perfect Mind/      #   Paradoxical divine poem
│   ├── Allogenes/                  #   The Foreigner's ascent
│   └── Zostrianos/                 #   Apocalypse of Zostrianos
├── 09-Pseudepigrapha/              # Old Testament Pseudepigrapha (11,400+ notes)
│   ├── Book of Jasher/             #   Chapters 01 → 91 (3,778 verse notes)
│   ├── Testaments of the Twelve Patriarchs/ # 12 Testaments of Jacob's Sons
│   ├── Sibylline Oracles/          #   Books 1 → 12 prophecies
│   ├── 3 Enoch/                    #   Hebrew Apocalypse of Enoch
│   ├── 2 Baruch/                   #   Syriac Apocalypse of Baruch
│   ├── Apocalypse of Abraham/      #   Vision of the throne & idolatry
│   ├── Life of Adam and Eve/       #   Conflict of Adam and Eve
│   ├── Ascension of Isaiah/        #   Martyrdom & heavenly ascent
│   └── Odes of Solomon/            #   First Christian hymnbook
├── scripts/                        # Scrapers, header purifiers, & chunkers
├── CANON_INVENTORY.md              # Master 117-book tracking inventory
└── COVERAGE_TRACKING.md            # Ingestion progress metrics & Mermaid diagram
```

---

## 📊 Canon Breakdown

| Section | Canon Classification | Books | Verses / Notes | Primary Source |
| :--- | :--- | :---: | :---: | :--- |
| **01** | Torah (Pentateuch) | 5 | 5,852 | Masoretic / LXX |
| **02** | Historical Books | 12 | 7,018 | Masoretic / LXX |
| **03** | Poetic & Wisdom Books | 5 | 4,792 | Masoretic / LXX |
| **04** | Major & Minor Prophets | 17 | 5,470 | Masoretic / LXX |
| **05** | Deuterocanonical Books | 14 | 5,970 | Septuagint (LXX) |
| **06** | New Testament | 27 | 7,885 | Textus Receptus / NA28 |
| **07** | Ethiopic Apocrypha | 8 | 4,151 | Ge'ez Manuscripts |
| **08** | Nag Hammadi & Gnostic Codices | 20 | 12,850 | Coptic Library (gnosis.org) |
| **09** | Pseudepigrapha & Lost Books | 9 | 11,400 | Wikisource / EarlyChristianWritings |
| **TOTAL** | **The Divine Vault Ecosystem** | **117** | **96,116** | **Canonical & Extracanonical** |

---

## 🛠️ YAML Frontmatter Specification

Every note in the vault strictly adheres to the following metadata structure:

```yaml
---
canon: Pseudepigrapha
source_type: Scripture
id: JASH-01-02
book: Book of Jasher
chapter: 1
verse: 2
---

And God formed man from the ground, and he blew into his nostrils the breath of life, and man became a living soul endowed with speech.
```

---

## 🛠️ Technology Stack & Tools

- **Markup & Storage**: Obsidian Markdown (GFM) with YAML Frontmatter
- **Scripting & Parsing**: Python 3.12 (urllib, BeautifulSoup4, re) & Node.js
- **Obsidian Sorting**: 2-digit & 3-digit zero-padding (`01`, `02`, ..., `144`)
- **Git Integration**: Automated synchronization with `Crucifly/bible-obsidian`

---

## 🤝 Contribution & Governance

Maintained by **Crucifly, LLC** under the **JEXXXUS Ecosystem** DOX Framework contract.

- **Organization**: Crucifly, LLC
- **Repository**: [git@github.com:Crucifly/bible-obsidian.git](https://github.com/Crucifly/bible-obsidian)
- **DOX Contract**: [AGENTS.md](file:///Users/dylanroberts/Documents/non-music/Dev/GitHub/JEXXXUS/AGENTS.md)

---

**Crucifly, LLC · Absolute Digital Sovereignty** ⚡
