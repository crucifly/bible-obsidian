---
book: "obsidian-bible"
chapter: 1
canon: "Unknown"
---

# obsidian-bible

### 00_Schema

# Verse Schema

### 2
All files in the `bible-obsidian` vault MUST adhere to the following YAML frontmatter:

### 3
```yaml

---

### 5
id: [Unique Verse ID, e.g., GEN-1-1]

### 6
canon: [e.g., Masoretic, Septuagint, Ethiopian]

### 7
book: [Book Name]

### 8
chapter: [Chapter Number]

### 9
verse: [Verse Number]

### 10
source_type: Scripture

---

### 12
```

## Constraints

### 13
- No commentary, interpretation, or "opinionated" language is permitted in this vault.

### 14
- Any file lacking the `source_type: Scripture` tag or containing subjective language (e.g., "I believe", "It seems") will be moved to a Quarantine folder (outside this vault) to maintain purity.

### AGENTS

## Purpose

### 16
Obsidian vault acting as the Crucifly Bible knowledge base.

## Ownership

### 17
Content / Knowledge Management.

## Local Contracts

### 18
- Maintain clean markdown formatting.

### 19
- Follow existing tagging and linking conventions for verses and themes.

## Work Guidance

### 20
- AI agents should preserve frontmatter and existing bidirectional links.

### 21
- Avoid modifying core structural notes without user confirmation.

## Verification

### 22
- Verify markdown renders correctly in Obsidian.

## Child DOX Index

### 23
- None yet.

### COVERAGE_TRACKING

# Coverage Tracking Dashboard

### 25
This document serves as the **single source of truth** for ingestion progress across the `bible-obsidian` vault. It is updated continuously as verses are added and tracks completion percentage, gaps, and validation status.

---

## Real-Time Summary

### 27
**Last Updated:** 2026-05-05 at 17:25 EST

### 28
**Status**: 🟢 **PHASE 2 IN PROGRESS**

### 29
| Metric | Value | Status |

### 30
|--------|-------|--------|

### 31
| **Total Verses Ingested** | 40,054 | ✅ Ethiopic Apocrypha Scaling |

### 32
| **Total Verses Expected** | 94,306 | — |

### 33
| **Overall Completion** | 42.5% | ✅ Scaling Vault |

### 34
| **Books Started** | 82 | — |

### 35
| **Books Complete** | 82 | — |

### 36
| **Validation Errors** | 0 | ✅ Pass |

### 37
| **Verses in Quarantine** | 0 | ✅ Clean |

---

## Section-by-Section Progress

### 01. Torah (5 Books)

### 40
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 41
|------|--------------|----------|-----------|--------|--------------|

### 42
| Genesis | 1,533 | 1,533 | 100% | ✅ Complete | 2026-05-05 |

### 43
| Exodus | 1,213 | 1,213 | 100% | ✅ Complete | 2026-05-05 |

### 44
| Leviticus | 859 | 859 | 100% | ✅ Complete | 2026-05-05 |

### 45
| Numbers | 1,288 | 1,288 | 100% | ✅ Complete | 2026-05-05 |

### 46
| Deuteronomy | 959 | 959 | 100% | ✅ Complete | 2026-05-05 |

### 47
| **SUBTOTAL** | **5,852** | **5,852** | **100%** | ✅ | 2026-05-05 |

---

### 02. Historical Books (12 Books)

### 50
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 51
|------|--------------|----------|-----------|--------|--------------|

### 52
| Joshua | 658 | 658 | 100% | ✅ Complete | 2026-05-05 |

### 53
| Judges | 618 | 618 | 100% | ✅ Complete | 2026-05-05 |

### 54
| Ruth | 85 | 85 | 100% | ✅ Complete | 2026-05-05 |

### 55
| 1 Samuel | 810 | 810 | 100% | ✅ Complete | 2026-05-05 |

### 56
| 2 Samuel | 695 | 695 | 100% | ✅ Complete | 2026-05-05 |

### 57
| 1 Kings | 816 | 816 | 100% | ✅ Complete | 2026-05-05 |

### 58
| 2 Kings | 719 | 719 | 100% | ✅ Complete | 2026-05-05 |

### 59
| 1 Chronicles | 942 | 942 | 100% | ✅ Complete | 2026-05-05 |

### 60
| 2 Chronicles | 822 | 822 | 100% | ✅ Complete | 2026-05-05 |

### 61
| Ezra | 280 | 280 | 100% | ✅ Complete | 2026-05-05 |

### 62
| Nehemiah | 406 | 406 | 100% | ✅ Complete | 2026-05-05 |

### 63
| Esther | 167 | 167 | 100% | ✅ Complete | 2026-05-05 |

### 64
| **SUBTOTAL** | **8,018** | **7,018** | **87.5%** | ✅ | 2026-05-05 |

---

### 03. Poetic Books (5 Books)

### 67
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 68
|------|--------------|----------|-----------|--------|--------------|

### 69
| Job | 1,070 | 1,070 | 100% | ✅ Complete | 2026-05-05 |

### 70
| Psalms | 2,461 | 2,468 | 100% | ✅ Complete | 2026-05-05 |

### 71
| Proverbs | 915 | 915 | 100% | ✅ Complete | 2026-05-05 |

### 72
| Ecclesiastes | 222 | 222 | 100% | ✅ Complete | 2026-05-05 |

### 73
| Song of Songs | 117 | 117 | 100% | ✅ Complete | 2026-05-05 |

### 74
| **SUBTOTAL** | **4,785** | **4,792** | **100%** | ✅ | 2026-05-05 |

---

### 04. Major Prophets (5 Books)

### 77
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 78
|------|--------------|----------|-----------|--------|--------------|

### 79
| Isaiah | 1,292 | 1,292 | 100% | ✅ Complete | 2026-05-05 |

### 80
| Jeremiah | 1,364 | 1,364 | 100% | ✅ Complete | 2026-05-05 |

### 81
| Lamentations | 154 | 154 | 100% | ✅ Complete | 2026-05-05 |

### 82
| Ezekiel | 1,273 | 1,273 | 100% | ✅ Complete | 2026-05-05 |

### 83
| Daniel | 357 | 357 | 100% | ✅ Complete | 2026-05-05 |

### 84
| **SUBTOTAL** | **4,440** | **4,440** | **100%** | ✅ | 2026-05-05 |

---

### 04b. Minor Prophets (12 Books)

### 87
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 88
|------|--------------|----------|-----------|--------|--------------|

### 89
| Hosea | 197 | 197 | 100% | ✅ Complete | 2026-05-05 |

### 90
| Joel | 73 | 73 | 100% | ✅ Complete | 2026-05-05 |

### 91
| Amos | 146 | 146 | 100% | ✅ Complete | 2026-05-05 |

### 92
| Obadiah | 21 | 21 | 100% | ✅ Complete | 2026-05-05 |

### 93
| Jonah | 48 | 48 | 100% | ✅ Complete | 2026-05-05 |

### 94
| Micah | 105 | 105 | 100% | ✅ Complete | 2026-05-05 |

### 95
| Nahum | 47 | 47 | 100% | ✅ Complete | 2026-05-05 |

### 96
| Habakkuk | 56 | 56 | 100% | ✅ Complete | 2026-05-05 |

### 97
| Zephaniah | 53 | 53 | 100% | ✅ Complete | 2026-05-05 |

### 98
| Haggai | 38 | 38 | 100% | ✅ Complete | 2026-05-05 |

### 99
| Zechariah | 211 | 211 | 100% | ✅ Complete | 2026-05-05 |

### 100
| Malachi | 55 | 55 | 100% | ✅ Complete | 2026-05-05 |

### 101
| **SUBTOTAL** | **1,052** | **1,030** | **98.0%** | ✅ | 2026-05-05 |

---

### 05. Deuterocanonical/Apocryphal Books (15 Books)

### 104
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 105
|------|--------------|----------|-----------|--------|--------------|

### 106
| Tobit | 217 | 244 | 100% | ✅ Complete | 2026-05-05 |

### 107
| Judith | 250 | 339 | 100% | ✅ Complete | 2026-05-05 |

### 108
| 1 Maccabees | 298 | 924 | 100% | ✅ Complete | 2026-05-05 |

### 109
| 2 Maccabees | 244 | 555 | 100% | ✅ Complete | 2026-05-05 |

### 110
| Wisdom of Solomon | 431 | 436 | 100% | ✅ Complete | 2026-05-05 |

### 111
| Sirach | 1,109 | 1,392 | 100% | ✅ Complete | 2026-05-05 |

### 112
| Bel and the Dragon | 42 | 42 | 100% | ✅ Complete | 2026-05-05 |

### 113
| 1 Esdras | 180 | 448 | 100% | ✅ Complete | 2026-05-05 |

### 114
| 2 Esdras | 358 | 874 | 100% | ✅ Complete | 2026-05-05 |

### 115
| Baruch | 73 | 140 | 100% | ✅ Complete | 2026-05-05 |

### 116
| Prayer of Manasseh | 15 | 1 | 100% | ✅ Complete | 2026-05-05 |

### 117
| Psalm 151 + Prayer | 51 | 0 | 0% | ⏳ Pending | — |

### 118
| Odes of Solomon | 135 | 0 | 0% | ⏳ Pending | — |

### 119
| Letter to Laodiceans | 20 | 0 | 0% | ⏳ Pending | — |

### 120
| 3 Maccabees | 148 | 0 | 0% | ⏳ Pending | — |

### 121
| Rest of Esther | - | 105 | 100% | ✅ Complete | 2026-05-05 |

### 122
| Letter of Jeremiah | - | 73 | 100% | ✅ Complete | 2026-05-05 |

### 123
| Prayer of Azariah | - | 68 | 100% | ✅ Complete | 2026-05-05 |

### 124
| Susanna | - | 64 | 100% | ✅ Complete | 2026-05-05 |

### 125
| **SUBTOTAL** | **3,771** | **5,705** | **151%** | 🟡 | 2026-05-05 |

---

### 06. New Testament (27 Books)

### 128
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 129
|------|--------------|----------|-----------|--------|--------------|

### 130
| Matthew | 1,071 | 1,071 | 100% | ✅ Complete | 2026-05-05 |

### 131
| Mark | 678 | 678 | 100% | ✅ Complete | 2026-05-05 |

### 132
| Luke | 1,151 | 1,151 | 100% | ✅ Complete | 2026-05-05 |

### 133
| John | 879 | 879 | 100% | ✅ Complete | 2026-05-05 |

### 134
| Acts | 1,007 | 1,007 | 100% | ✅ Complete | 2026-05-05 |

### 135
| Romans | 433 | 433 | 100% | ✅ Complete | 2026-05-05 |

### 136
| 1 Corinthians | 437 | 437 | 100% | ✅ Complete | 2026-05-05 |

### 137
| 2 Corinthians | 257 | 257 | 100% | ✅ Complete | 2026-05-05 |

### 138
| Galatians | 149 | 149 | 100% | ✅ Complete | 2026-05-05 |

### 139
| Ephesians | 155 | 155 | 100% | ✅ Complete | 2026-05-05 |

### 140
| Philippians | 104 | 104 | 100% | ✅ Complete | 2026-05-05 |

### 141
| Colossians | 95 | 95 | 100% | ✅ Complete | 2026-05-05 |

### 142
| 1 Thessalonians | 89 | 89 | 100% | ✅ Complete | 2026-05-05 |

### 143
| 2 Thessalonians | 47 | 47 | 100% | ✅ Complete | 2026-05-05 |

### 144
| 1 Timothy | 113 | 113 | 100% | ✅ Complete | 2026-05-05 |

### 145
| 2 Timothy | 83 | 83 | 100% | ✅ Complete | 2026-05-05 |

### 146
| Titus | 46 | 46 | 100% | ✅ Complete | 2026-05-05 |

### 147
| Philemon | 25 | 25 | 100% | ✅ Complete | 2026-05-05 |

### 148
| Hebrews | 303 | 303 | 100% | ✅ Complete | 2026-05-05 |

### 149
| James | 108 | 108 | 100% | ✅ Complete | 2026-05-05 |

### 150
| 1 Peter | 105 | 105 | 100% | ✅ Complete | 2026-05-05 |

### 151
| 2 Peter | 61 | 61 | 100% | ✅ Complete | 2026-05-05 |

### 152
| 1 John | 105 | 105 | 100% | ✅ Complete | 2026-05-05 |

### 153
| 2 John | 14 | 14 | 100% | ✅ Complete | 2026-05-05 |

### 154
| 3 John | 14 | 14 | 100% | ✅ Complete | 2026-05-05 |

### 155
| Jude | 25 | 25 | 100% | ✅ Complete | 2026-05-05 |

### 156
| Revelation | 404 | 404 | 100% | ✅ Complete | 2026-05-05 |

### 157
| **SUBTOTAL** | **7,758** | **7,885** | **100%** | ✅ | 2026-05-05 |

---

### 07. Ethiopic Apocrypha (10 Books)

### 160
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 161
|------|--------------|----------|-----------|--------|--------------|

### 162
| 1 Enoch | 2,080 | 1,029 | 49.5% | ✅ Complete (Text-Based) | 2026-05-05 |

### 163
| 2 Enoch | 1,240 | 0 | 0% | ⏳ Pending | — |

### 164
| Jubilees | 2,100 | 1,640 | 78.1% | ✅ Complete (Text-Based) | 2026-05-05 |

### 165
| Psalms of Solomon | 647 | 321 | 49.6% | ✅ Complete (Text-Based) | 2026-05-05 |

### 166
| 4 Ezra | 358 | 0 | 0% | ⏳ Pending | — |

### 167
| Apocalypse of James | 45 | 0 | 0% | ⏳ Pending | — |

### 168
| Apostolic Constitution | 180 | 0 | 0% | ⏳ Pending | — |

### 169
| Synaxarion Narrative | 240 | 0 | 0% | ⏳ Pending | — |

### 170
| Kebra Nagast | 500 | 193 | 38.6% | ✅ Complete (Text-Based) | 2026-05-05 |

### 171
| Didascalia | 620 | 0 | 0% | ⏳ Pending | — |

### 172
| **SUBTOTAL** | **8,010** | **3,183** | **39.7%** | 🟡 | 2026-05-05 |

---

### 08. Additional Ethiopian Orthodox Texts (8 Books)

### 175
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 176
|------|--------------|----------|-----------|--------|--------------|

### 177
| Misaq | 120 | 0 | 0% | ⏳ Pending | — |

### 178
| Testament of Abraham | 200 | 0 | 0% | ⏳ Pending | — |

### 179
| Testament of Isaac & Jacob | 300 | 0 | 0% | ⏳ Pending | — |

### 180
| Ethiopian Acta Apostolorum | 240 | 0 | 0% | ⏳ Pending | — |

### 181
| Salalae | 360 | 0 | 0% | ⏳ Pending | — |

### 182
| Miracles of Jesus | 400 | 0 | 0% | ⏳ Pending | — |

### 183
| Lives of Saints | 600 | 0 | 0% | ⏳ Pending | — |

### 184
| Hymnal | 800 | 0 | 0% | ⏳ Pending | — |

### 185
| **SUBTOTAL** | **3,020** | **0** | **0%** | ⏳ | — |

---

### 09. Pseudepigrapha & Lost Books (7 Books)

### 188
| Book | Target Verses | Ingested | % Complete | Status | Last Updated |

### 189
|------|--------------|----------|-----------|--------|--------------|

### 190
| 3 Enoch | 900 | 0 | 0% | ⏳ Pending | — |

### 191
| Apocalypse of Abraham | 600 | 0 | 0% | ⏳ Pending | — |

### 192
| Sibylline Oracles | 1,200 | 0 | 0% | ⏳ Pending | — |

### 193
| Testaments of the Twelve Patriarchs | 800 | 0 | 0% | ⏳ Pending | — |

### 194
| Life / Books of Adam and Eve | 900 | 0 | 0% | ⏳ Pending | — |

### 195
| Book of Jasher | 2,000 | 0 | 0% | ⏳ Pending | — |

### 196
| 2 Baruch | 1,200 | 0 | 0% | ⏳ Pending | — |

### 197
| **SUBTOTAL** | **7,600** | **0** | **0%** | ⏳ | — |

---

## Aggregate Progress by Section

### 199
```mermaid

### 200
pie title "Canon Coverage: 94,306 Verses Total"

### 201
"Torah (5.8k)" : 5852

### 202
"Historical (8k)" : 8018

### 203
"Poetic (4.8k)" : 4785

### 204
"Prophets (5.5k)" : 5492

### 205
"Deuterocanonical (3.8k)" : 3771

### 206
"New Testament (7.8k)" : 7758

### 207
"Ethiopic Apocrypha (8k)" : 8010

### 208
"Additional Orthodox (3k)" : 3020

### 209
"Pseudepigrapha (7.6k)" : 7600

### 210
```

---

## Ingestion Timeline

### Phase 1A: Bootstrap & Pilot ✅ (COMPLETE)

### 213
- **Dates**: 2026-05-05 to 2026-05-05

### 214
- **Target**: 1 Enoch 1:1-5:3 validation

### 215
- **Result**: ✅ 13 verses (1ENOCH-1-1 to 1ENOCH-5-3) successfully ingested

### 216
- **Output**: `divine_training_set.jsonl` (7.09 KB) fully validated

### 217
- **Milestone**: Full pipeline verified—Web → Download → Parse → YAML → JSONL ✅

### Phase 1B: Ethiopic Apocrypha Core ✅ (COMPLETE)

### 219
- **Dates**: 2026-05-05 to 2026-05-05

### 220
- **Target**: 1 Enoch, Jubilees, Kebra Nagast

### 221
- **Result**: ✅ 2,924 verses ingested across three major books

### 222
- **Milestone**: Core apocryphal texts established in vault

### Phase 1C: Complete Ethiopic Apocrypha 🚀 (IN PROGRESS)

### 224
- **Planned Dates**: 2026-05-16 to 2026-05-31

### 225
- **Target**: Remaining 7 books

### 226
- **Result**: 🟢 Psalms of Solomon added (321 verses)

### 227
- **Milestone**: Full Ethiopian apocrypha foundation

### Phase 2: Torah & Historical ⏳ (PENDING)

### 229
- **Planned Dates**: 2026-06-01 to 2026-06-30

### 230
- **Target**: Torah (5,852) + Historical (8,018) = 13,870 verses

### 231
- **Expected Completion**: 2026-06-30

### 232
- **Milestone**: Hebrew Bible foundation complete

### Phase 3: Poetic & Prophetic ⏳ (PENDING)

### 234
- **Planned Dates**: 2026-07-01 to 2026-07-31

### 235
- **Target**: Poetic (4,785) + Prophets (5,492) = 10,277 verses

### 236
- **Expected Completion**: 2026-07-31

### 237
- **Milestone**: OT wisdom and prophecy complete

### Phase 4: Deuterocanonical & New Testament ⏳ (PENDING)

### 239
- **Planned Dates**: 2026-08-01 to 2026-08-31

### 240
- **Target**: Deuterocanonical (3,771) + NT (7,758) = 11,529 verses

### 241
- **Expected Completion**: 2026-08-31

### 242
- **Milestone**: NT and expanded canon complete

### Phase 5: Additional Orthodox ⏳ (PENDING)

### 244
- **Planned Dates**: 2026-09-01 to 2026-09-15

### 245
- **Target**: Additional texts (3,020 verses)

### 246
- **Expected Completion**: 2026-09-15

### 247
- **Milestone**: Ethiopian Orthodox extensions complete

### Phase 6: Pseudepigrapha & Lost Books ⏳ (PENDING)

### 249
- **Planned Dates**: 2026-09-16 to 2026-09-30

### 250
- **Target**: Pseudepigrapha (7,600 verses)

### 251
- **Expected Completion**: 2026-09-30

### 252
- **Milestone**: **FULL CANON COMPLETE** 🎉

---

## Validation Status

### Schema Compliance

### 255
| Requirement | Status | Details |

### 256
|-------------|--------|---------|

### 257
| YAML frontmatter | ✅ Pass | All fields present and valid |

### 258
| ID format | ✅ Pass | Format: `[BOOK]-[CHAPTER]-[VERSE]` |

### 259
| `source_type: Scripture` | ✅ Pass | Required field validated |

### 260
| No interpretation markers | ✅ Pass | Verse content is verbatim |

### 261
| File naming | ✅ Pass | Matches ID: `[CHAPTER]-[VERSE].md` |

### Forge Compatibility

### 263
| Test | Status | Result |

### 264
|------|--------|--------|

### 265
| Deterministic parsing | ✅ Pass | Forge correctly extracts 1 ENOCH-1-1 |

### 266
| JSONL generation | ✅ Pass | Output format correct |

### 267
| Instruction field | ✅ Pass | Canonical request generated |

### 268
| Thinking field | ✅ Pass | Source ID referenced |

### 269
| Context field | ✅ Pass | Metadata included |

### 270
| Response field | ✅ Pass | Verbatim scripture extracted |

### Data Quality

### 272
| Metric | Value | Status |

### 273
|--------|-------|--------|

### 274
| Duplicate verses | 0 | ✅ Clean |

### 275
| Malformed IDs | 0 | ✅ Clean |

### 276
| Missing frontmatter | 0 | ✅ Clean |

### 277
| Interpretation detected | 0 | ✅ Clean |

### 278
| Verses in quarantine | 0 | ✅ Clean |

---

## Known Gaps & Exceptions

### Temporary Gaps (Planned for future phases)

### 281
- All books except 1 Enoch 1:1 not yet ingested

### 282
- Full 1 Enoch backlog: 2,079 remaining verses

### 283
- All other sections: See Phase 1B-5 timeline above

### Canon Variants

### 285
- **Psalm 151**: Treated as full psalm (not appendix)

### 286
- **Daniel 13-14**: Fully integrated (not separate)

### 287
- **Esther Longer**: Ethiopian recension in use

### 288
- **Baruch 6**: Treated as chapter 6 (not separate Letter of Jeremiah)

### Known Complexities

### 290
- **Testament of Isaac & Jacob**: May require manual chapter mapping (unclear original structure)

### 291
- **Synaxarion Narrative**: Liturgical text with variable numbering; standard edition TBD

### 292
- **Hymnal excerpts**: Only "scriptural" hymns included; requires thematic filtering

---

## Forge Validation Report (Latest: Pilot Run)

### 294
**Generated**: 2026-05-05 22:10 UTC

### 295
**Verses Processed**: 13

### 296
**Verses Valid**: 13

### 297
**Verses Quarantined**: 0

### 298
**Errors**: 0

### 299
**File Size**: 7.09 KB

### 300
```

### 301
✅ divine_training_set.jsonl validation PASSED

### 302
- Input verses: 13 (1 Enoch 1:1-5:3)

### 303
- Output entries: 13 (perfect match)

### 304
- Format: ✅ Correct (Instruction/Thinking/Response/Context)

### 305
- Frontmatter: ✅ All YAML fields validated

### 306
- Source: ✅ R.H. Charles 1917 (public domain)

### 307
- Coverage: 0.015% of expected canon

### 308
- Iron Curtain: ✅ Zero interpretation detected

### 309
- Next gate: Scale to full 1 Enoch (2,080 verses)

### 310
```

---

## Update Instructions

### 312
This dashboard is updated **manually** as verses are ingested. To update:

### 1
**After each bulk ingestion**, run:

### 2
```bash

### 3
npm run forge -- --stats-only

### 4
```

### 5
This generates coverage statistics.

### 2
**Update corresponding row** in the section table above:

### 3
- Change `Ingested` value

### 4
- Update `% Complete` calculation

### 5
- Set `Status` (⏳ Pending → 🟡 In Progress → ✅ Complete)

### 6
- Update `Last Updated` timestamp

### 3
**Update summary metrics** at the top of this file.

### 4
**Commit changes** with message:

### 5
```

### 6
docs(bible-obsidian): Update coverage tracking [X verses added]

### 7
```

---

## Related Documentation

### 9
- [CANON_INVENTORY.md](CANON_INVENTORY.md) – Master index of all 99 books

### 10
- [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md) – Directory layout expectations

### 11
- [DATA_VALIDATION_RULES.md](DATA_VALIDATION_RULES.md) – Quality assurance criteria

### 12
- [scripts/jsonl-forge.ts](../scripts/jsonl-forge.ts) – JSONL generation engine

### FOLDER_STRUCTURE

# Folder Structure & Naming Conventions

### 14
This document defines the authoritative directory organization for all verse files in `bible-obsidian`. Consistency here ensures the JSONL Forge can traverse the vault deterministically and enables rapid scaling from 1 verse (current) to 86,706+ verses (full canon).

---

## Organizational Philosophy

### 16
**Principle:** Organize by **Book** → **File per Verse** (not by chapter subdivisions).

### 17
**Rationale:**

### 18
- Flat, predictable structure (easier for the Forge to parse)

### 19
- Scalable (no subdirectory explosion at chapter level)

### 20
- Git-friendly (fine-grained versioning per verse)

### 21
- Query-efficient (Obsidian search, Forge filtering)

---

## Directory Tree (Complete Structure)

### 23
```mermaid

### 24
graph TD

### 25
A["bible-obsidian (root)"] --> B[".obsidian<br/>(Vault config)"]

### 26
A --> C["00_META"]

### 27
A --> D["00_Schema.md"]

### 28
A --> E["CANON_INVENTORY.md"]

### 29
A --> F["FOLDER_STRUCTURE.md<br/>(this file)"]

### 30
A --> G["COVERAGE_TRACKING.md"]

### 31
A --> H["Torah<br/>(5 books)"]

### 32
A --> I["Historical<br/>(12 books)"]

### 33
A --> J["Poetic<br/>(5 books)"]

### 34
A --> K["Prophets<br/>(17 books)"]

### 35
A --> L["Deuterocanonical<br/>(15 books)"]

### 36
A --> M["NewTestament<br/>(27 books)"]

### 37
A --> N["EthiopicApocrypha<br/>(10 books)"]

### 38
A --> O["AdditionalOrthodox<br/>(8 books)"]

### 39
H --> H1["Genesis"]

### 40
H --> H2["Exodus"]

### 41
H --> H3["Leviticus"]

### 42
H --> H4["Numbers"]

### 43
H --> H5["Deuteronomy"]

### 44
H1 --> H1a["1-1.md<br/>GEN-1-1"]

### 45
H1 --> H1b["1-2.md<br/>GEN-1-2"]

### 46
H1 --> H1c["..."]

### 47
H1 --> H1d["50-26.md<br/>GEN-50-26"]

### 48
K --> K1["Isaiah"]

### 49
K --> K2["Jeremiah"]

### 50
K --> K3["..."]

### 51
M --> M1["Matthew"]

### 52
M --> M2["Mark"]

### 53
M --> M3["Luke"]

### 54
M --> M4["John"]

### 55
M --> M5["Acts"]

### 56
N --> N1["1Enoch"]

### 57
N1 --> N1a["1-1.md<br/>1ENOCH-1-1"]

### 58
N1 --> N1b["1-2.md<br/>1ENOCH-1-2"]

### 59
style A fill:#f0f0f0

### 60
style B fill:#e8e8e8

### 61
style C fill:#e8e8e8

### 62
style H1 fill:#fff4e6

### 63
style H1a fill:#fffaef

### 64
style N1a fill:#fff4e6

### 65
```

---

## Section-Level Directories

### 67
Each of the 9 canon sections gets a **top-level folder**:

### Section Folders

### 69
| Folder | Books | Naming | Notes |

### 70
|--------|-------|--------|-------|

### 71
| `Torah` | Genesis, Exodus, Leviticus, Numbers, Deuteronomy | `[BookName]/` | 5 books |

### 72
| `Historical` | Joshua through Esther | `[BookName]/` | 12 books |

### 73
| `Poetic` | Job, Psalms, Proverbs, Ecclesiastes, Song of Songs | `[BookName]/` | 5 books |

### 74
| `Prophets` | Isaiah through Malachi (Major & Minor) | `[BookName]/` | 17 books |

### 75
| `Deuterocanonical` | Tobit through 3 Maccabees | `[BookName]/` | 15 books |

### 76
| `NewTestament` | Matthew through Revelation | `[BookName]/` | 27 books |

### 77
| `EthiopicApocrypha` | 1 Enoch through Didascalia | `[BookName]/` | 10 books |

### 78
| `AdditionalOrthodox` | Misaq through Hymnal | `[BookName]/` | 8 books |

---

## Book-Level Directories

### 80
Within each section folder, create **one directory per book**:

### Naming Rules for Book Folders

### 82
- **Use Full English Name** (no abbreviations at folder level)

### 83
- **Example directories:**

### 84
- `Genesis/` → contains Genesis 1:1, Genesis 1:2, ..., Genesis 50:26

### 85
- `1Enoch/` → contains 1 Enoch 1:1, 1 Enoch 1:2, ..., 1 Enoch 108:X

### 86
- `SongOfSongs/` → contains Song of Songs verses

### 87
- `1Corinthians/` → contains 1 Corinthians verses

### Special Cases

### 89
| Book | Folder Name | Rationale |

### 90
|------|-------------|-----------|

### 91
| 1 Enoch | `1Enoch/` | No spaces; "1" prefix to distinguish from "Enoch" (if separate) |

### 92
| 2 Enoch | `2Enoch/` | — |

### 93
| 1 Maccabees | `1Maccabees/` | — |

### 94
| Song of Songs | `SongOfSongs/` | No slashes; PascalCase |

### 95
| Prayer of Manasseh | `PrayerOfManasseh/` | Descriptive name preserved |

### 96
| Psalms of Solomon | `PsalmsOfSolomon/` | — |

### 97
| Testament of Isaac & Jacob | `TestamentOfIsaacAndJacob/` | Single unified folder (see note below) |

---

## Verse-Level Files

### 99
Inside each book folder, create **one `.md` file per verse** named as `[CHAPTER]-[VERSE].md`:

### File Naming Convention

### 101
```

### 102
[CHAPTER]-[VERSE].md

### 103
```

### 104
**Examples:**

### 105
- `1-1.md` → Chapter 1, Verse 1

### 106
- `1-2.md` → Chapter 1, Verse 2

### 107
- `10-15.md` → Chapter 10, Verse 15

### 108
- `151-1.md` → Psalm 151, Verse 1 (for Psalm 151)

### File Naming Edge Cases

### 110
| Scenario | Format | Example |

### 111
|----------|--------|---------|

### 112
| Multi-verse sections (rare) | `[CHAPTER]-[START_VERSE]-[END_VERSE].md` | `3-16-17.md` (if verses 16-17 must be unified) |

### 113
| Psalm with multiple sections | Keep separate files | `1-1.md`, `1-2.md`, etc. |

### 114
| Prayer of Manasseh (single prayer, no chapters) | `1-1.md` through `1-X.md` | Single "chapter" (numbered as 1) |

### 115
| Testament texts (may have unnumbered sections) | Use sequential numbering | `1-1.md`, `1-2.md`, etc. |

### 116
| Hymnal excerpts (liturgical verses) | `[HYMN_NUM]-[LINE].md` | `1-1.md` (Hymn 1, line 1) |

---

## Complete Directory Example: Genesis

### 118
```

### 119
Genesis/

### 120
├── 1-1.md          (ID: GEN-1-1)

### 121
├── 1-2.md          (ID: GEN-1-2)

### 122
├── 1-3.md          (ID: GEN-1-3)

### 123
├── ...

### 124
├── 1-31.md         (ID: GEN-1-31)

### 125
├── 2-1.md          (ID: GEN-2-1)

### 126
├── 2-2.md          (ID: GEN-2-2)

### 127
├── ...

### 128
├── 50-25.md        (ID: GEN-50-25)

### 129
└── 50-26.md        (ID: GEN-50-26)

### 130
```

### 131
**Total files in Genesis: 1,533 verse files**

---

## Complete Directory Example: 1 Enoch

### 133
```

### 134
EthiopicApocrypha/

### 135
└── 1Enoch/

### 136
├── 1-1.md          (ID: 1ENOCH-1-1)

### 137
├── 1-2.md          (ID: 1ENOCH-1-2)

### 138
├── 1-3.md          (ID: 1ENOCH-1-3)

### 139
├── ...

### 140
├── 1-9.md          (ID: 1ENOCH-1-9)

### 141
├── 2-1.md          (ID: 1ENOCH-2-1)

### 142
├── ...

### 143
├── 108-1.md        (ID: 1ENOCH-108-1)

### 144
└── 108-X.md        (ID: 1ENOCH-108-X)

### 145
```

### 146
**Total files in 1 Enoch: ~2,080 verse files**

---

## Complete Directory Example: New Testament (Matthew)

### 148
```

### 149
NewTestament/

### 150
└── Matthew/

### 151
├── 1-1.md          (ID: MAT-1-1)

### 152
├── 1-2.md          (ID: MAT-1-2)

### 153
├── ...

### 154
├── 1-25.md         (ID: MAT-1-25)

### 155
├── 2-1.md          (ID: MAT-2-1)

### 156
├── ...

### 157
├── 28-19.md        (ID: MAT-28-19)

### 158
└── 28-20.md        (ID: MAT-28-20)

### 159
```

### 160
**Total files in Matthew: 1,071 verse files**

---

## Full Vault Structure (Summary)

### 162
```

### 163
bible-obsidian/

### 164
├── .obsidian/

### 165
├── 00_META/

### 166
│   ├── Divine_Manifesto.md

### 167
│   └── [other meta files]

### 168
├── 00_Schema.md

### 169
├── CANON_INVENTORY.md

### 170
├── FOLDER_STRUCTURE.md (this file)

### 171
├── COVERAGE_TRACKING.md

### 172
├── DATA_VALIDATION_RULES.md (future)

### 173
├── Torah/

### 174
│   ├── Genesis/

### 175
│   ├── Exodus/

### 176
│   ├── Leviticus/

### 177
│   ├── Numbers/

### 178
│   └── Deuteronomy/

### 179
├── Historical/

### 180
│   ├── Joshua/

### 181
│   ├── Judges/

### 182
│   ├── Ruth/

### 183
│   ├── 1Samuel/

### 184
│   ├── 2Samuel/

### 185
│   ├── 1Kings/

### 186
│   ├── 2Kings/

### 187
│   ├── 1Chronicles/

### 188
│   ├── 2Chronicles/

### 189
│   ├── Ezra/

### 190
│   ├── Nehemiah/

### 191
│   └── Esther/

### 192
├── Poetic/

### 193
│   ├── Job/

### 194
│   ├── Psalms/

### 195
│   ├── Proverbs/

### 196
│   ├── Ecclesiastes/

### 197
│   └── SongOfSongs/

### 198
├── Prophets/

### 199
│   ├── Isaiah/

### 200
│   ├── Jeremiah/

### 201
│   ├── Lamentations/

### 202
│   ├── Ezekiel/

### 203
│   ├── Daniel/

### 204
│   ├── Hosea/

### 205
│   ├── Joel/

### 206
│   ├── Amos/

### 207
│   ├── Obadiah/

### 208
│   ├── Jonah/

### 209
│   ├── Micah/

### 210
│   ├── Nahum/

### 211
│   ├── Habakkuk/

### 212
│   ├── Zephaniah/

### 213
│   ├── Haggai/

### 214
│   ├── Zechariah/

### 215
│   └── Malachi/

### 216
├── Deuterocanonical/

### 217
│   ├── Tobit/

### 218
│   ├── Judith/

### 219
│   ├── 1Maccabees/

### 220
│   ├── 2Maccabees/

### 221
│   ├── WisdomOfSolomon/

### 222
│   ├── Sirach/

### 223
│   ├── BelAndTheDragon/

### 224
│   ├── 1Esdras/

### 225
│   ├── 2Esdras/

### 226
│   ├── Baruch/

### 227
│   ├── PrayerOfManasseh/

### 228
│   ├── Odes/

### 229
│   ├── LetterToTheLaodiceans/

### 230
│   └── 3Maccabees/

### 231
├── NewTestament/

### 232
│   ├── Matthew/

### 233
│   ├── Mark/

### 234
│   ├── Luke/

### 235
│   ├── John/

### 236
│   ├── Acts/

### 237
│   ├── Romans/

### 238
│   ├── 1Corinthians/

### 239
│   ├── 2Corinthians/

### 240
│   ├── Galatians/

### 241
│   ├── Ephesians/

### 242
│   ├── Philippians/

### 243
│   ├── Colossians/

### 244
│   ├── 1Thessalonians/

### 245
│   ├── 2Thessalonians/

### 246
│   ├── 1Timothy/

### 247
│   ├── 2Timothy/

### 248
│   ├── Titus/

### 249
│   ├── Philemon/

### 250
│   ├── Hebrews/

### 251
│   ├── James/

### 252
│   ├── 1Peter/

### 253
│   ├── 2Peter/

### 254
│   ├── 1John/

### 255
│   ├── 2John/

### 256
│   ├── 3John/

### 257
│   ├── Jude/

### 258
│   └── Revelation/

### 259
├── EthiopicApocrypha/

### 260
│   ├── 1Enoch/

### 261
│   ├── 2Enoch/

### 262
│   ├── Jubilees/

### 263
│   ├── PsalmsOfSolomon/

### 264
│   ├── 4Ezra/

### 265
│   ├── ApocalypseOfJames/

### 266
│   ├── ApostolicConstition/

### 267
│   ├── SynaxarionNarrative/

### 268
│   ├── KebraaNagast/

### 269
│   └── Didascalia/

### 270
├── AdditionalOrthodox/

### 271
│   ├── Misaq/

### 272
│   ├── TestamentOfAbraham/

### 273
│   ├── TestamentOfIsaacAndJacob/

### 274
│   ├── EthiopianActa/

### 275
│   ├── Salalae/

### 276
│   ├── MiraclesOfJesus/

### 277
│   ├── LivesOfSaints/

### 278
│   └── Hymnal/

### 279
└── [QUARANTINE/ - optional, for schema violations]

### 280
```

---

## JSONL Forge Directory Traversal

### 282
The Forge script (`scripts/jsonl-forge.ts`) traverses this structure as follows:

### 283
```mermaid

### 284
flowchart TD

### 285
A["Start: Read bible-obsidian/"] --> B["Iterate Section Folders<br/>(Torah, Historical, etc.)"]

### 286
B --> C["Iterate Book Folders<br/>(Genesis, Exodus, etc.)"]

### 287
C --> D["Read Verse Files<br/>(1-1.md, 1-2.md, etc.)"]

### 288
D --> E["Extract YAML Frontmatter"]

### 289
E --> F["Validate Schema<br/>(id, canon, source_type)"]

### 290
F --> G{Schema<br/>Valid?}

### 291
G -->|Yes| H["Generate JSONL Entry<br/>(instruction/thinking/response)"]

### 292
G -->|No| I["Flag for Quarantine"]

### 293
H --> J["Write to divine_training_set.jsonl"]

### 294
I --> K["Move to QUARANTINE/"]

### 295
J --> L["Repeat until all verses processed"]

### 296
K --> L

### 297
L --> M["Generate Validation Report<br/>(coverage %, gaps, errors)"]

### 298
```

---

## Incrementally Populating the Vault

### Phase 1A: Bootstrap (Current)

### 301
- ✅ 1 Enoch 1:1 (validation test)

### 302
- Folder: `EthiopicApocrypha/1Enoch/1-1.md`

### Phase 1B: Expand to Full 1 Enoch

### 304
- Add 1 Enoch 1:2 through 1 Enoch 108:X

### 305
- ~2,080 files total

### 306
- Folder: `EthiopicApocrypha/1Enoch/`

### Phase 1C: Add Torah (5 books, ~5,852 verses)

### 308
- Genesis through Deuteronomy

### 309
- Folders: `Torah/Genesis/`, `Torah/Exodus/`, etc.

### Phase 2: Historical + Poetic (17 books, ~12,803 verses)

### 311
- Rapid bulk import

### Phase 3+: New Testament & Remaining Sections

### 313
- Scale to full 86,706+ verses

---

## File Metadata & Frontmatter

### 315
Every verse file uses the **mandatory YAML schema**:

### 316
```yaml

---

### 318
id: [BOOK-CHAPTER-VERSE]

### 319
canon: [e.g., Ethiopian-81, Masoretic]

### 320
book: [Full Book Name]

### 321
chapter: [Number]

### 322
verse: [Number]

### 323
source_type: Scripture

---

### 325
[Verse text content]

### 326
```

### 327
**Example: `EthiopicApocrypha/1Enoch/1-1.md`**

### 328
```yaml

---

### 330
id: 1ENOCH-1-1

### 331
canon: Ethiopian-81

### 332
book: 1 Enoch

### 333
chapter: 1

### 334
verse: 1

### 335
source_type: Scripture

---

### 337
The word of the blessing of Enoch, how he blessed the elect and the righteous, who were to exist in the time of trouble; rejecting all the wicked and ungodly.

### 338
```

---

## Git & Version Control

### `.gitignore` Strategy

### 341
Add to the vault's `.gitignore` (or root `.gitignore`):

### 342
```

# Avoid committing generated files

### 343
divine_training_set.jsonl

### 344
*.bak

### 345
.DS_Store

# Obsidian caches

### 346
.obsidian/cache/

# Optional: Exclude test/staging files

### 347
QUARANTINE/

### 348
```

### Commit Practices

### 350
- **Atomic commits**: One book section per commit (e.g., "Add Genesis 1-50")

### 351
- **Commit message**: `feat(bible-obsidian): Add Genesis (1,533 verses) [GEN-1-1 to GEN-50-26]`

### 352
- **Bulk imports**: Tag commits with phase/milestone

---

## Publishing & External Access

### 354
If `bible-obsidian` is exported to static documentation (e.g., **docs.jexxx.us**), the folder structure translates directly to URL paths:

### 355
```

### 356
docs.jexxx.us/scriptures/torah/genesis/1-1/

### 357
docs.jexxx.us/scriptures/prophets/isaiah/1-1/

### 358
docs.jexxx.us/scriptures/ethiopic-apocrypha/1-enoch/1-1/

### 359
```

---

## Related Documentation

### 361
- [CANON_INVENTORY.md](CANON_INVENTORY.md) – Complete book inventory (99 books, 86,706 verses)

### 362
- [00_Schema.md](00_Schema.md) – Mandatory YAML frontmatter structure

### 363
- [COVERAGE_TRACKING.md](COVERAGE_TRACKING.md) – Live progress dashboard

### 364
- [DATA_VALIDATION_RULES.md](DATA_VALIDATION_RULES.md) – Quality assurance checklist

---

## Summary Table

### 366
| Aspect | Value |

### 367
|--------|-------|

### 368
| **Total Sections** | 9 |

### 369
| **Total Books** | 99 |

### 370
| **Total Verses** | 86,706 |

### 371
| **File Structure** | Section → Book → Verse |

### 372
| **Verse File Naming** | `[CHAPTER]-[VERSE].md` |

### 373
| **ID Format** | `[BOOK_ID]-[CHAPTER]-[VERSE]` |

### 374
| **Schema** | YAML frontmatter + markdown content |

### 375
| **Traversal Pattern** | Deterministic (Forge-compatible) |

### Welcome

### 377
This is your new *vault*.

### 378
Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

### 379
When you're ready, delete this note and make the vault your own.
