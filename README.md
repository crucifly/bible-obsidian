
### 1
<div align="center">

# 🕊️ The Divine Vault ☦️

### A Verse-Level Canonical Dataset for the 117-Book Expanded Biblical, Ethiopic, Gnostic & Pseudepigraphal Canon

### 2
**96,116 verses & structured sections** · **11 canonical sections** · **117 books** · **Zero interpretation**

### 3
Built by **Crucifly, LLC** for the JEXXXUS Theological & Gnostic Intelligence Engine

---

### 4
</div>

---

### 5
<div align="center">

### 6
<img src=".github/social-preview.png" alt="The Divine Vault Social Preview" width="100%">

### 7
</div>

---

## 📖 Overview & Purpose

### 8
**The Divine Vault** is a machine-readable, verse-level and section-level decomposition of the complete **117-book expanded biblical canon**, encompassing the 81-Book Ethiopian Orthodox Tewahedo Bible, the Nag Hammadi Gnostic Library, and the Old Testament Pseudepigrapha.

### 9
Every single verse and section exists as an individual Markdown note with structured YAML frontmatter, designed to serve as the **Source of Truth** for training, fine-tuning, and RAG (Retrieval-Augmented Generation) across large language models.

### 10
This vault contains **zero commentary, zero interpretation, and zero subjective opinions**—only verbatim scripture and canonical metadata.

---

## 🛡️ The Iron Curtain Directive

### 11
A strict validation rule governs this vault: only files tagged with `source_type: Scripture` or `source_type: Gnostic-Codex` are permitted to enter fine-tuning pipelines. Any file containing subjective commentary, modern commentary, or web navigation noise is quarantined and purged.

### 12
This architectural constraint—the **Iron Curtain**—ensures that AI models trained on this repository produce accurate, verbatim canonical output rather than hallucinated theology.

---

## 📂 Vault Structure

### 13
```text

### 14
bible-obsidian/

### 15
├── 00_META/                        # Governance, manifestos, & core contracts

### 16
├── 00_Schema.md                    # YAML frontmatter specification & schema

### 17
├── 01-Torah/                       # Genesis → Deuteronomy (5,852 verses)

### 18
│   ├── 01-Genesis/

### 19
│   │   ├── Chapter 01/

### 20
│   │   │   ├── 01-01.md            # Individual verse note with YAML

### 21
│   │   │   ├── 01-02.md

### 22
│   │   │   └── ...

### 23
│   │   └── ...

### 24
├── 02-Historical/                  # Joshua → Esther (7,018 verses)

### 25
├── 03-Poetic/                      # Job → Song of Solomon (4,792 verses)

### 26
├── 04-Prophets/                    # Isaiah → Malachi (5,470 verses)

### 27
├── 05-Deuterocanonical/            # Tobit → 3 Maccabees (5,970 verses)

### 28
├── 06-NewTestament/                # Matthew → Revelation (7,885 verses)

### 29
├── 07-EthiopicApocrypha/           # Ethiopian Orthodox Broad Canon (4,151+ verses)

### 30
│   ├── 1 Enoch/                    #   1,029 verses (108 chapters)

### 31
│   ├── Jubilees/                   #   1,640 verses (50 chapters)

### 32
│   ├── Kebra Nagast/               #   533 verses (117 chapters)

### 33
│   ├── Psalms of Solomon/          #   321 verses (18 psalms)

### 34
│   ├── 2 Enoch/                    #   372 verses (68 chapters)

### 35
│   ├── Apostolic Constitutions/    #   Horner Statutes (70 Statutes)

### 36
│   └── Didascalia/                 #   Harden Didascalia (41 Chapters)

### 37
├── 08-NagHammadi/                  # Gnostic Library & Coptic Codices (12,850+ notes)

### 38
│   ├── Gospel of Thomas/           #   114 Logia (Sayings)

### 39
│   ├── Gospel of Philip/           #   Structured theological sections

### 40
│   ├── Gospel of Truth/            #   Gnostic meditation sections

### 41
│   ├── Gospel of Mary/             #   Chapters 4, 5, 8, 9 with verse files

### 42
│   ├── Gospel of Judas/            #   Full Codex Tchacos translation

### 43
│   ├── Pistis Sophia/              #   Chapters 001 → 144 (Mead translation)

### 44
│   ├── Apocryphon of John/         #   Secret revelation of John

### 45
│   ├── Hypostasis of the Archons/  #   Reality of the Rulers

### 46
│   ├── On the Origin of the World/ #   Cosmological creation narrative

### 47
│   ├── Sophia of Jesus Christ/     #   Wisdom of Jesus Christ

### 48
│   ├── Dialogue of the Savior/     #   Dialogue between Jesus & disciples

### 49
│   ├── Tripartite Tractate/        #   Systematic Valentinian theology

### 50
│   ├── Trimorphic Protennoia/      #   First Thought in Three Forms

### 51
│   ├── Second Discourse of Great Seth/ # Secret Gnostic discourse

### 52
│   ├── Exegesis on the Soul/       #   Soul's fall & restoration

### 53
│   ├── Authoritative Teaching/     #   Soul's origin & destiny

### 54
│   ├── Concept of Our Great Power/ # Apocalyptic vision of the Aeons

### 55
│   ├── Thunder, Perfect Mind/      #   Paradoxical divine poem

### 56
│   ├── Allogenes/                  #   The Foreigner's ascent

### 57
│   └── Zostrianos/                 #   Apocalypse of Zostrianos

### 58
├── 09-Pseudepigrapha/              # Old Testament Pseudepigrapha (11,400+ notes)

### 59
│   ├── Book of Jasher/             #   Chapters 01 → 91 (3,778 verse notes)

### 60
│   ├── Testaments of the Twelve Patriarchs/ # 12 Testaments of Jacob's Sons

### 61
│   ├── Sibylline Oracles/          #   Books 1 → 12 prophecies

### 62
│   ├── 3 Enoch/                    #   Hebrew Apocalypse of Enoch

### 63
│   ├── 2 Baruch/                   #   Syriac Apocalypse of Baruch

### 64
│   ├── Apocalypse of Abraham/      #   Vision of the throne & idolatry

### 65
│   ├── Life of Adam and Eve/       #   Conflict of Adam and Eve

### 66
│   ├── Ascension of Isaiah/        #   Martyrdom & heavenly ascent

### 67
│   └── Odes of Solomon/            #   First Christian hymnbook

### 68
├── scripts/                        # Scrapers, header purifiers, & chunkers

### 69
├── CANON_INVENTORY.md              # Master 117-book tracking inventory

### 70
└── COVERAGE_TRACKING.md            # Ingestion progress metrics & Mermaid diagram

### 71
```

---

## 📊 Canon Breakdown

### 72
| Section | Canon Classification | Books | Verses / Notes | Primary Source |

### 73
| :--- | :--- | :---: | :---: | :--- |

### 74
| **01** | Torah (Pentateuch) | 5 | 5,852 | Masoretic / LXX |

### 75
| **02** | Historical Books | 12 | 7,018 | Masoretic / LXX |

### 76
| **03** | Poetic & Wisdom Books | 5 | 4,792 | Masoretic / LXX |

### 77
| **04** | Major & Minor Prophets | 17 | 5,470 | Masoretic / LXX |

### 78
| **05** | Deuterocanonical Books | 14 | 5,970 | Septuagint (LXX) |

### 79
| **06** | New Testament | 27 | 7,885 | Textus Receptus / NA28 |

### 80
| **07** | Ethiopic Apocrypha | 8 | 4,151 | Ge'ez Manuscripts |

### 81
| **08** | Nag Hammadi & Gnostic Codices | 20 | 12,850 | Coptic Library (gnosis.org) |

### 82
| **09** | Pseudepigrapha & Lost Books | 9 | 11,400 | Wikisource / EarlyChristianWritings |

### 83
| **TOTAL** | **The Divine Vault Ecosystem** | **117** | **96,116** | **Canonical & Extracanonical** |

---

## 🛠️ YAML Frontmatter Specification

### 84
Every note in the vault strictly adheres to the following metadata structure:

### 85
```yaml

---

### 86
canon: Pseudepigrapha

### 87
source_type: Scripture

### 88
id: JASH-01-02

### 89
book: Book of Jasher

### 90
chapter: 1

### 91
verse: 2

---

### 92
And God formed man from the ground, and he blew into his nostrils the breath of life, and man became a living soul endowed with speech.

### 93
```

---

## 🛠️ Technology Stack & Tools

### 94
- **Markup & Storage**: Obsidian Markdown (GFM) with YAML Frontmatter

### 95
- **Scripting & Parsing**: Python 3.12 (urllib, BeautifulSoup4, re) & Node.js

### 96
- **Obsidian Sorting**: 2-digit & 3-digit zero-padding (`01`, `02`, ..., `144`)

### 97
- **Git Integration**: Automated synchronization with `Crucifly/bible-obsidian`

---

## 🤝 Contribution & Governance

### 98
Maintained by **Crucifly, LLC** under the **JEXXXUS Ecosystem** DOX Framework contract.

### 99
- **Organization**: Crucifly, LLC

### 100
- **DOX Contract**: [AGENTS.md](file:///Users/dylanroberts/Documents/non-music/Dev/GitHub/JEXXXUS/AGENTS.md)

---

### 101
**Crucifly, LLC · Absolute Digital Sovereignty** ⚡
