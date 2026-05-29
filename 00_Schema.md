---
name: Bible Obsidian Schema
description: Mandatory YAML frontmatter for all scriptural verses to ensure "Iron Curtain" separation.
type: reference
---

# Verse Schema

All files in the `bible-obsidian` vault MUST adhere to the following YAML frontmatter:

```yaml
---
id: [Unique Verse ID, e.g., GEN-1-1]
canon: [e.g., Masoretic, Septuagint, Ethiopian]
book: [Book Name]
chapter: [Chapter Number]
verse: [Verse Number]
source_type: Scripture
---
```

## Constraints
- No commentary, interpretation, or "opinionated" language is permitted in this vault.
- Any file lacking the `source_type: Scripture` tag or containing subjective language (e.g., "I believe", "It seems") will be moved to a Quarantine folder (outside this vault) to maintain purity.
