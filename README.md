
### 1
<div align="center">

# 🕊️ The Divine Vault ☦️

### 2
### A Verse-Level Canonical Dataset for the 117-Book Expanded Biblical, Ethiopic, Gnostic & Pseudepigraphal Canon

### 3
**96,116 verses & structured sections** · **11 canonical sections** · **117 books** · **Zero interpretation**

### 4
Built by **Crucifly, LLC** for the JEXXXUS Theological & Gnostic Intelligence Engine

### 5
---

### 6
![Status](https://img.shields.io/badge/verses-96%2C116-gold?style=for-the-badge&logo=obsidian&logoColor=white)

### 7
![Canon](https://img.shields.io/badge/canon-117--Book%20Expanded%20Ecosystem-darkred?style=for-the-badge)

### 8
![Format](https://img.shields.io/badge/format-Obsidian%20%2B%20JSONL-7C3AED?style=for-the-badge&logo=markdown&logoColor=white)

### 9
![License](https://img.shields.io/badge/license-Public%20Domain%20(Scripture)-333?style=for-the-badge)

### 10
![GitHub Repo](https://img.shields.io/badge/GitHub-Crucifly%2Fbible--obsidian-181717?style=for-the-badge&logo=github&logoColor=white)

### 11
</div>

### 12
---

### 13
<div align="center">

### 14
<img src=".github/social-preview.png" alt="The Divine Vault Social Preview" width="100%">

### 15
</div>

### 16
---

## 📖 Overview & Purpose

### 17
**The Divine Vault** is a machine-readable, verse-level and section-level decomposition of the complete **117-book expanded biblical canon**, encompassing the 81-Book Ethiopian Orthodox Tewahedo Bible, the Nag Hammadi Gnostic Library, and the Old Testament Pseudepigrapha.

### 18
Every single verse and section exists as an individual Markdown note with structured YAML frontmatter, designed to serve as the **Source of Truth** for training, fine-tuning, and RAG (Retrieval-Augmented Generation) across large language models.

### 19
This vault contains **zero commentary, zero interpretation, and zero subjective opinions**—only verbatim scripture and canonical metadata.

### 20
---

## 🛡️ The Iron Curtain Directive

### 21
A strict validation rule governs this vault: only files tagged with `source_type: Scripture` or `source_type: Gnostic-Codex` are permitted to enter fine-tuning pipelines. Any file containing subjective commentary, modern commentary, or web navigation noise is quarantined and purged.

### 22
This architectural constraint—the **Iron Curtain**—ensures that AI models trained on this repository produce accurate, verbatim canonical output rather than hallucinated theology.

### 23
---

## 📂 Vault Structure

### 24
```text

### 25
bible-obsidian/

### 26
├── 00_META/                        # Governance, manifestos, & core contracts

### 27
├── 00_Schema.md                    # YAML frontmatter specification & schema

### 28
├── 01-Torah/                       # Genesis → Deuteronomy (5,852 verses)

### 29
│   ├── 01-Genesis/

### 30
│   │   ├── Chapter 01/

### 31
│   │   │   ├── 01-01.md            # Individual verse note with YAML

### 32
│   │   │   ├── 01-02.md

### 33
│   │   │   └── ...

### 34
│   │   └── ...

### 35
├── 02-Historical/                  # Joshua → Esther (7,018 verses)

### 36
├── 03-Poetic/                      # Job → Song of Solomon (4,792 verses)

### 37
├── 04-Prophets/                    # Isaiah → Malachi (5,470 verses)

### 38
├── 05-Deuterocanonical/            # Tobit → 3 Maccabees (5,970 verses)

### 39
├── 06-NewTestament/                # Matthew → Revelation (7,885 verses)

### 40
├── 07-EthiopicApocrypha/           # Ethiopian Orthodox Broad Canon (4,151+ verses)

### 41
│   ├── 1 Enoch/                    #   1,029 verses (108 chapters)

### 42
│   ├── Jubilees/                   #   1,640 verses (50 chapters)

### 43
│   ├── Kebra Nagast/               #   533 verses (117 chapters)

### 44
│   ├── Psalms of Solomon/          #   321 verses (18 psalms)

### 45
│   ├── 2 Enoch/                    #   372 verses (68 chapters)

### 46
│   ├── Apostolic Constitutions/    #   Horner Statutes (70 Statutes)

### 47
│   └── Didascalia/                 #   Harden Didascalia (41 Chapters)

### 48
├── 08-NagHammadi/                  # Gnostic Library & Coptic Codices (12,850+ notes)

### 49
│   ├── Gospel of Thomas/           #   114 Logia (Sayings)

### 50
│   ├── Gospel of Philip/           #   Structured theological sections

### 51
│   ├── Gospel of Truth/            #   Gnostic meditation sections

### 52
│   ├── Gospel of Mary/             #   Chapters 4, 5, 8, 9 with verse files

### 53
│   ├── Gospel of Judas/            #   Full Codex Tchacos translation

### 54
│   ├── Pistis Sophia/              #   Chapters 001 → 144 (Mead translation)

### 55
│   ├── Apocryphon of John/         #   Secret revelation of John

### 56
│   ├── Hypostasis of the Archons/  #   Reality of the Rulers

### 57
│   ├── On the Origin of the World/ #   Cosmological creation narrative

### 58
│   ├── Sophia of Jesus Christ/     #   Wisdom of Jesus Christ

### 59
│   ├── Dialogue of the Savior/     #   Dialogue between Jesus & disciples

### 60
│   ├── Tripartite Tractate/        #   Systematic Valentinian theology

### 61
│   ├── Trimorphic Protennoia/      #   First Thought in Three Forms

### 62
│   ├── Second Discourse of Great Seth/ # Secret Gnostic discourse

### 63
│   ├── Exegesis on the Soul/       #   Soul's fall & restoration

### 64
│   ├── Authoritative Teaching/     #   Soul's origin & destiny

### 65
│   ├── Concept of Our Great Power/ # Apocalyptic vision of the Aeons

### 66
│   ├── Thunder, Perfect Mind/      #   Paradoxical divine poem

### 67
│   ├── Allogenes/                  #   The Foreigner's ascent

### 68
│   └── Zostrianos/                 #   Apocalypse of Zostrianos

### 69
├── 09-Pseudepigrapha/              # Old Testament Pseudepigrapha (11,400+ notes)

### 70
│   ├── Book of Jasher/             #   Chapters 01 → 91 (3,778 verse notes)

### 71
│   ├── Testaments of the Twelve Patriarchs/ # 12 Testaments of Jacob's Sons

### 72
│   ├── Sibylline Oracles/          #   Books 1 → 12 prophecies

### 73
│   ├── 3 Enoch/                    #   Hebrew Apocalypse of Enoch

### 74
│   ├── 2 Baruch/                   #   Syriac Apocalypse of Baruch

### 75
│   ├── Apocalypse of Abraham/      #   Vision of the throne & idolatry

### 76
│   ├── Life of Adam and Eve/       #   Conflict of Adam and Eve

### 77
│   ├── Ascension of Isaiah/        #   Martyrdom & heavenly ascent

### 78
│   └── Odes of Solomon/            #   First Christian hymnbook

### 79
├── scripts/                        # Scrapers, header purifiers, & chunkers

### 80
├── CANON_INVENTORY.md              # Master 117-book tracking inventory

### 81
└── COVERAGE_TRACKING.md            # Ingestion progress metrics & Mermaid diagram

### 82
```

### 83
---

## 📊 Canon Breakdown

### 84
| Section | Canon Classification | Books | Verses / Notes | Primary Source |

### 85
| :--- | :--- | :---: | :---: | :--- |

### 86
| **01** | Torah (Pentateuch) | 5 | 5,852 | Masoretic / LXX |

### 87
| **02** | Historical Books | 12 | 7,018 | Masoretic / LXX |

### 88
| **03** | Poetic & Wisdom Books | 5 | 4,792 | Masoretic / LXX |

### 89
| **04** | Major & Minor Prophets | 17 | 5,470 | Masoretic / LXX |

### 90
| **05** | Deuterocanonical Books | 14 | 5,970 | Septuagint (LXX) |

### 91
| **06** | New Testament | 27 | 7,885 | Textus Receptus / NA28 |

### 92
| **07** | Ethiopic Apocrypha | 8 | 4,151 | Ge'ez Manuscripts |

### 93
| **08** | Nag Hammadi & Gnostic Codices | 20 | 12,850 | Coptic Library (gnosis.org) |

### 94
| **09** | Pseudepigrapha & Lost Books | 9 | 11,400 | Wikisource / EarlyChristianWritings |

### 95
| **TOTAL** | **The Divine Vault Ecosystem** | **117** | **96,116** | **Canonical & Extracanonical** |

### 96
---

## 🛠️ YAML Frontmatter Specification

### 97
Every note in the vault strictly adheres to the following metadata structure:

### 98
```yaml

### 99
---

### 100
canon: Pseudepigrapha

### 101
source_type: Scripture

### 102
id: JASH-01-02

### 103
book: Book of Jasher

### 104
chapter: 1

### 105
verse: 2

### 106
---

### 107
And God formed man from the ground, and he blew into his nostrils the breath of life, and man became a living soul endowed with speech.

### 108
```

### 109
---

## 🛠️ Technology Stack & Tools

### 110
- **Markup & Storage**: Obsidian Markdown (GFM) with YAML Frontmatter

### 111
- **Scripting & Parsing**: Python 3.12 (urllib, BeautifulSoup4, re) & Node.js

### 112
- **Obsidian Sorting**: 2-digit & 3-digit zero-padding (`01`, `02`, ..., `144`)

### 113
- **Git Integration**: Automated synchronization with `Crucifly/bible-obsidian`

### 114
---

## 🤝 Contribution & Governance

### 115
Maintained by **Crucifly, LLC** under the **JEXXXUS Ecosystem** DOX Framework contract.

### 116
- **Organization**: Crucifly, LLC

### 117
- **Repository**: [git@github.com:Crucifly/bible-obsidian.git](https://github.com/Crucifly/bible-obsidian)

### 118
- **DOX Contract**: [AGENTS.md](file:///Users/dylanroberts/Documents/non-music/Dev/GitHub/JEXXXUS/AGENTS.md)

### 119
---

### 120
**Crucifly, LLC · Absolute Digital Sovereignty** ⚡
