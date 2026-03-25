---
name: Fantasy Worldbuilding Style Guide
type: guide
category: meta
summary: "Conventions and standards for the fantasy setting documentation."
---

# Fantasy Worldbuilding Style Guide

> Standards for consistent, maintainable worldbuilding entries.

---

## File Naming

| Type | Convention | Example |
|------|------------|---------|
| Races | `lowercase.md` | `pierwsi.md`, `orkowie.md` |
| Characters | `name-lowercase-dashes.md` | `velan-kivar-zan-ehkovok.md` |
| Locations | `lowercase-dashes.md` | `torrs-gate.md`, `silver-woods.md` |
| Factions | `lowercase-dashes.md` | `silver-compact.md` |
| Lore | `lowercase-dashes.md` | `magic-systems.md` |
| Creatures | `lowercase-dashes.md` | `yazghur.md` |

**Rule:** Use English base names, lowercase, hyphens instead of spaces.

---

## Frontmatter Template

```markdown
---
name: [English Name]
type: [type]
category: [category]
tags: [relevant, tags]
related:
  - related-file
  - another-file
summary: "[Brief description in English, one sentence max.]"
---

# [English Name] ([Polish Name])

> [One-line tagline/quote in English]
```

### Valid Types

| Type | Use For |
|------|---------|
| `sapient-race` | Thinking races (humans, elves, etc.) |
| `creature` | Non-sapient monsters and beasts |
| `character` | Named individuals |
| `faction` | Organizations and groups |
| `location` | Places, regions, cities |
| `magic-system` | Rules of magic |
| `lore` | History, mythology, concepts |
| `adventure` | Quests and campaigns |
| `guide` | Meta-documentation (this file) |

### Valid Categories

- `races`
- `creatures`
- `characters`
- `factions`
- `places`
- `lore`
- `adventures`
- `meta`

---

## Race Entry Structure

```markdown
# [Name] ([Polish Name])

> Tagline.

## Overview

| Attribute | Value |
|-----------|-------|
| **Category** | Sapient Race |
| **Polish Name** | Polish |
| **Adult Age** | X |
| **Average Age** | X |
| **Oldest Recorded** | X |
| **Height** | ~X cm |
| **Type** | Humanoid/etc. |
| **Sentience** | Sapient/Non-sapient |

## Description

[2-4 paragraphs]

## Physical Traits

### Strengths
- Bullet points

### Weaknesses
- Bullet points

## Society & Culture

[Optional: Only if significant]

## Relations

| Race | Relationship |
|------|--------------|
| [[Race]] | Description |

## Known [Plural]

- List of famous individuals or subgroups

## Notes

[Any GM-relevant info or edge cases]
```

---

## Creature Entry Structure

```markdown
# [Name]

> Tagline.

## Overview

| Attribute | Value |
|-----------|-------|
| **Category** | Creature |
| **Classification** | [Taxonomic/typological] |
| **Danger Level** | [Low/Medium/High/Deadly] |
| **Typical Habitat** | [Where found] |
| **Average Size** | [Height/length] |
| **Sentience** | Non-sapient |

## Description

[Physical appearance, behavior, ecology]

## Abilities

| Ability | Effect |
|---------|--------|
| [Name] | [Description] |

## Behavior

- How it hunts
- How it reproduces
- Social structure (if any)

## Weaknesses

- Known vulnerabilities
- How to fight/defeat

## Yazghur as Example

See: [[yazghur|Yazghur (Beast)]]

## Notes

[GM info, encounter hooks, etc.]
```

---

## Character Entry Structure

```markdown
# [Full Name]

*[Role, Campaign/Series]*

## Basics

| Field | Value |
|-------|-------|
| Race | [[Race Name]] |
| Sex | Male/Female/Other |
| Age | X |

## Description

[Physical appearance, personality, backstory]

## Skills & Abilities

- **Combat**: [Details]
- **Magic**: [Details]
- **[Other]**: [Details]

## Equipment

- Item 1: Description
- Item 2: Description

## Relationships

- **[[Character]]**: [Relationship]
- **[[Character]]**: [Relationship]

## Notes

[GM info, plot hooks]
```

---

## Wiki-Style Links

Use double brackets for internal links:

```markdown
- [[Pierwsi (The First Ones)|Pierwsi]] — explicit text
- [[Pierwsi]] — implicit (uses file title)
- [[Torrs Gate (Brama Torra)|Torr's Gate]] — locations
```

---

## Polish Usage

| Element | Polish | English |
|---------|--------|---------|
| Race names | Yes (Orkowie) | Yes (Orcs) |
| Location names | Yes (Brama Torra) | Yes (Torr's Gate) |
| Character names | Use as-is | No translation |
| UI text | — | English |

**Rule:** Primary name in English, Polish in parentheses.

---

## Tables Over Lists

**Do:**
```markdown
| Name | Value |
|------|-------|
| Foo | Bar |
| Baz | Qux |
```

**Don't:**
- Long bullet lists where a table fits better
- Inconsistent column counts

---

## TODOs Placement

Consolidate all TODOs in one section at the end:

```markdown
## TODO

- [ ] Add tribal variations
- [ ] Add known orc characters
```

**Don't scatter [TODO] throughout the document.**

---

## Visual References

For races with visual references (like Orcs from Gothic):

```markdown
## Visual Reference

![Description](URL)

*Credit: [Source]*
```

---

## Related Files

| This File | Related |
|-----------|---------|
| `yazghur.md` | Races that hunt/fear Yazghur |
| `pierwsi.md` | Origin mythology |
| `BIBLE.md` | Master index |

---

## Checklist

Before publishing an entry:

- [ ] Frontmatter complete (name, type, category, tags, summary)
- [ ] Wiki-links formatted correctly
- [ ] Tables properly aligned
- [ ] TODOs consolidated at bottom
- [ ] Polish name in parentheses
- [ ] Consistent header hierarchy
- [ ] No broken links
