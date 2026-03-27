---
name: Fantasy Worldbuilding Style Guide
type: guide
category: meta
summary: "Conventions and standards for the fantasy setting documentation."
---

# Fantasy Worldbuilding Style Guide

> Standards for consistent, maintainable worldbuilding entries.

---

## General Philosophy

This wiki is designed for **creative works** — novels, games, tabletop campaigns, and world bibles. Content should focus on:

- **Lore and narrative** — what the item/place/person *is* and *means*
- **Thematic depth** — why it matters to your story or world
- **Story hooks** — ideas for how to use it in narratives
- **Consistent tone** — atmospheric, evocative prose

**No game mechanics.** No damage dice, saving throws, rarity tiers, or weight values. Keep descriptions narrative so they adapt to any system or no system at all.

---

## File Naming

| Type | Convention | Example |
|------|------------|---------|
| Races | `lowercase.md` | `the-cleansed.md`, `orcs.md` |
| Characters | `name-lowercase-dashes.md` | `velan-kivar-zan-ehkovok.md` |
| Locations | `lowercase-dashes.md` | `torrs-gate.md`, `silver-woods.md` |
| Factions | `lowercase-dashes.md` | `silver-compact.md` |
| Lore | `lowercase-dashes.md` | `magic-systems.md` |
| Creatures | `lowercase-dashes.md` | `yazghur.md` |
| Items | `lowercase-dashes.md` | `soul-breaker.md`, `dreadwinter.md` |

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
| `index` | Directory landing pages and navigation hubs |
| `sapient-race` | Thinking races (humans, elves, etc.) |
| `creature` | Non-sapient monsters and beasts |
| `character` | Named individuals |
| `faction` | Organizations and groups |
| `location` | Places, regions, cities |
| `magic-system` | Rules of magic |
| `lore` | History, mythology, concepts |
| `item` | Objects, weapons, artifacts |
| `adventure` | Quests and campaigns |
| `guide` | Meta-documentation (this file) |

### Valid Categories

- `races`
- `creatures`
- `characters`
- `factions`
- `places`
- `lore`
- `items`
- `adventures`
- `meta`

---

## Index File Standards

Use `_index.md` as the landing page for each category directory.

### Required Frontmatter

```markdown
---
name: [Category Name] Index
type: index
category: [category]
summary: "[Short summary of what this directory contains.]"
---
```

### Index Conventions

- Keep the H1 short and match the category name.
- Add a one-line blockquote that sets the tone and scope.
- Link only to entries that currently exist in the repository.
- Prefer wiki links for internal references.
- Inside subdirectories, use links relative to that folder, for example:
  - `[[yazghur|Yazghur]]` for files in the same directory
  - `[[../lore/magic-system|Spirit Binding]]` for sibling directories
- Avoid placeholder sections for folders or documents that do not yet exist.

---

## Item Entry Structure

```markdown
# [Name] ([Polish Name])

> [One-line tagline or quote]

## Description

[Physical appearance, materials, sensory details — 2-3 paragraphs]

## Properties

### [Property Name] ([Passive/Active])
[Narrative description of what it does]

[Additional properties as needed]

## History

[Origin story, notable appearances, how it changed hands]

## Lore

[Background, mythology, cultural significance]

## For Writers / Game Designers

### Themes to Explore
- [Key themes or ideas the item represents]

### Story Hooks
- [Specific narrative hooks for writers/GMs]

### World-Building Notes
- [How the item fits into different campaign types or genres]
```

### Property Descriptions

Use clear labels for how abilities work:

- **Passive**: Always active, no action required
- **Active**: Requires deliberate use

Keep descriptions **narrative** — describe *what happens*, not *how it resolves mechanically*.

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

## For Writers / Game Designers

[Hooks, themes, notes for GMs]

## TODO

- [ ] Add tribal variations
- [ ] Add known orc characters
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
| [Name] | [Narrative description] |

## Behavior

- How it hunts
- How it reproduces
- Social structure (if any)

## Weaknesses

- Known vulnerabilities
- How to fight/defeat

## For Writers / Game Designers

[Encounter hooks, narrative uses]

## TODO

- [ ] Add encounter hooks
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

## For Writers / Game Designers

[Plot hooks, character arcs]

## TODO

- [ ] Develop backstory further
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
| Item names | Yes (Łamacz Dusz) | Yes (Soul Breaker) |
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
- [ ] No game mechanics (dice, saves, rarity tiers, weights, ranges)
- [ ] "For the GM" renamed to "For Writers / Game Designers"
