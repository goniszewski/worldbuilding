---
name: Contributing Guide
type: guide
category: meta
summary: "Technical reference for adding new content to the fantasy wiki."
---

# Contributing Guide

> Quick-reference documentation for adding story-first entries to the fantasy worldbuilding project.

This folder is for **worldbuilding and narrative reference**, not tabletop rulebooks. Entries should support fiction, setting design, and adaptable game usage without introducing concrete mechanics such as damage, durations, skill points, rarity ladders, or balance values.

---

## Quick Start

1. **Pick the right location**: See [File Locations](#file-locations)
2. **Use the correct template**: See [Templates](#templates)
3. **Fill in frontmatter**: See [Frontmatter Reference](#frontmatter-reference)
4. **Follow section structure**: See [Section Templates](#section-templates)
5. **Review against checklist**: See [Quality Checklist](#quality-checklist)

---

## File Locations

```
worldbuilding/fantasy/
├── races/           # Sapient races (humans, elves, dwarves, etc.)
├── creatures/       # Non-sapient monsters and beasts
├── characters/      # Named individuals (NPCs, protagonists)
├── factions/        # Organizations, guilds, governments
├── places/          # Locations (cities, regions, landmarks)
├── items/           # Equipment, artifacts, weapons, tools
├── lore/            # History, mythology, magic systems, concepts
├── adventures/      # Quests, campaigns, storylines
└── _index.md        # Category indexes (auto-generated navigation)
```

**Rules:**
- One file per entry
- File name = slug version of English name (lowercase, hyphens)
- No special characters, no spaces, no Polish characters

---

## Frontmatter Reference

### Required Fields

| Field | Description | Required For |
|-------|-------------|--------------|
| `name` | English display name | All entries |
| `type` | Content type identifier | All entries |
| `category` | Wiki category (usually matches folder) | All entries |
| `summary` | One-sentence description | All entries |

### Optional Fields

| Field | Description | Common For |
|-------|-------------|------------|
| `tags` | Searchable keywords (array) | All entries |
| `related` | Related file paths (array) | All entries |
| `summary` | Already listed above | — |

### Frontmatter Examples

**Minimal (simple entry):**
```yaml
---
name: The Mourning Wars
type: lore
category: lore
summary: "A century-long conflict that reshaped the known world."
---
```

**Full (complex entry):**
```yaml
---
name: Velan Kivar Zan Ehkovok
type: character
category: characters
tags: [warrior, orc, mercenary, iron-fist]
related:
  - gwenn-lysel-the-warden
  - silver-compact
  - angmar-ironfist-warband
summary: "A battle-scarred orc warrior leading the Iron Fist warband."
---
```

---

## Type Specifications

### `sapient-race`

**Category:** `races`

**Frontmatter:**
```yaml
name: [English name]
type: sapient-race
category: races
tags: [race, humanoid, tag2, tag3]
related:
  - other-race-file
  - relevant-lore-file
summary: "[One sentence, present tense, no period at end]"
```

**Required Sections:**
1. Overview table (narrative descriptors)
2. Description (2-4 paragraphs)
3. Physical Traits (strengths/weaknesses)
4. Society & Culture (if significant)
5. Relations (table of race relationships)
6. Known Members (optional)
7. Story Use (optional adaptation notes)

**Wiki-links from this type:**
- Other races: `[[race-file|Display Name]]`
- Lore references: `[[lore-file|Lore Topic]]`
- Characters: `[[character-file|Character Name]]`

---

### `creature`

**Category:** `creatures`

**Frontmatter:**
```yaml
name: [Creature name]
type: creature
category: creatures
tags: [creature, beast, monster, tag2]
related:
  - creature-that-hunts-it
  - habitat-location
summary: "[One sentence describing what it is]"
```

**Required Sections:**
1. Overview table (perceived threat, habitat, size)
2. Description (appearance, behavior, ecology)
3. Notable Traits (table with name/effect columns)
4. Behavior (hunting, reproduction, social)
5. Weaknesses
6. Story Use (narrative hooks, adaptation notes)

**Overview Table Fields:**
| Field | Value |
|-------|-------|
| **Category** | Creature |
| **Classification** | Taxonomic or typological group |
| **Perceived Threat** | Minor / Serious / Fearsome / Catastrophic |
| **Typical Habitat** | Where found |
| **Typical Size** | Small / man-sized / huge / colossal |
| **Sentience** | Non-sapient |

---

### `character`

**Category:** `characters`

**Frontmatter:**
```yaml
name: [Full Name]
type: character
category: characters
tags: [role, race, faction, notable-trait]
related:
  - faction-file
  - location-file
  - other-character
summary: "[One sentence describing role/significance]"
```

**Required Sections:**
1. Basics table (race, sex, life stage, role)
2. Description (appearance, personality, backstory)
3. Notable Traits (if notable)
4. Equipment (if notable)
5. Relationships (linked to other characters)
6. Story Use (plot hooks, arc notes)

**Naming Convention:**
- Use full given name + surname
- Compound names with hyphens: `Velan-Kivar-Zan-Ehkovok`
- For foreigners: original name + common translation

---

### `faction`

**Category:** `factions`

**Frontmatter:**
```yaml
name: [Faction name]
type: faction
category: factions
tags: [type, alignment, size, tag3]
related:
  - leader-character
  - location-file
  - rival-faction
summary: "[One sentence describing purpose/scope]"
```

**Required Sections:**
1. Overview table (founded, scope, HQ, current standing)
2. Description (history, purpose, structure)
3. Structure (ranks, divisions, hierarchy)
4. Resources (if significant)
5. Relations (table with other factions)
6. Story Use (hooks, adaptation notes)

**Overview Table Fields:**
| Field | Value |
|-------|-------|
| **Category** | Faction |
| **Founded** | Year or era |
| **Headquarters** | Location |
| **Character** | How the faction is perceived |
| **Scale** | Local / regional / continental |
| **Status** | Active / Dissolved / Unknown |

---

### `location`

**Category:** `places`

**Frontmatter:**
```yaml
name: [Location name]
type: location
category: places
tags: [type, region, terrain, tag4]
related:
  - nearby-location
  - faction-that-controls
  - lore-file
summary: "[One sentence describing significance]"
```

**Required Sections:**
1. Overview table (type, region, atmosphere, controlling power)
2. Description (appearance, history, atmosphere)
3. Notable Features (key locations within)
4. Inhabitants (factions, races present)
5. Story Use (hooks, adaptation notes)

**Naming Convention:**
- Use English common name
- Include original name if significant: `Torr's Gate (Brama Torra)`

---

### `lore`

**Category:** `lore`

**Frontmatter:**
```yaml
name: [Topic name]
type: lore
category: lore
tags: [topic, era, relevance, tag3]
related:
  - related-lore
  - affected-faction
  - historical-event
summary: "[One sentence overview]"
```

**Required Sections:**
1. Overview (what this lore covers)
2. History (chronological or thematic)
3. Key Concepts (table or paragraphs)
4. Related Entries (see also)
5. Notes

**Use Cases:**
- Historical events
- Magic systems
- Mythology and religion
- Cultural concepts
- World rules

---

### `item`

**Category:** `items`

**Subcategories:** `weapons`, `armor`, `artifacts`, `consumables`, `tools`

**Frontmatter:**
```yaml
name: [Item name]
type: item
category: items
tags: [type, material, cultural-significance, tag4]
related:
  - creator-character
  - owner-character
  - related-item
summary: "[One sentence describing what it is]"
```

**Required Sections:**
1. Overview table (type, origin, significance, current status)
2. Description (appearance, history, significance)
3. Properties (narrative traits, abilities, effects)
4. Lore (background, related stories)
5. Story Use (adaptation notes, acquisition ideas, weaknesses)

**Overview Table Fields:**
| Field | Value |
|-------|-------|
| **Category** | Item |
| **Type** | Weapon / Armor / Artifact / Consumable / Tool |
| **Significance** | Common / uncommon / rare / legendary within the setting |
| **Origin** | Created by / Found in / Era |
| **Current Status** | Lost / guarded / widespread / forbidden |

**Item Subtype Tags:**
| Subtype | Examples |
|---------|----------|
| `weapons` | Sword, Bow, Dagger, Polearm |
| `armor` | Chain, Plate, Shield, Helmet |
| `artifacts` | Relics, Sentient items, Ancient objects |
| `consumables` | Potions, Scrolls, Reagents, Food |
| `tools` | Instruments, Containers, Keys, Maps |

---

## Section Templates

### Overview Table (All Types)

```markdown
## Overview

| Attribute | Value |
|-----------|-------|
| **Category** | [Type from valid types] |
| **Field 1** | Value |
| **Field 2** | Value |
| **Field 3** | Value |
```

**Always include Category and Type-specific fields. Prefer descriptive, in-world labels over system statistics.**

### Description (All Types)

```markdown
## Description

[Paragraph 1: Introduction - what is it?]

[Paragraph 2: History or significance - why does it matter?]

[Paragraph 3: Notable characteristics - what makes it unique?]
```

**Rule:** 2-4 paragraphs. More detail goes in specialized sections.

### Relations / Relationships Table

```markdown
## Relations

| Name | Type | Relationship |
|------|------|--------------|
| [[file|Display]] | Race/Faction | Description |
| [[file|Display]] | Character | Description |
```

### TODO Section (All Types)

```markdown
## TODO

- [ ] Task one
- [ ] Task two
- [ ] Add more details about [topic]
```

**Rule:** Keep TODOs at the bottom. Don't scatter [TODO] throughout.

---

## Wiki-Link Format

| Purpose | Syntax | Example |
|---------|--------|---------|
| Explicit text | `[Display](file\.md)` | `[Pierwsi](pierwsi\.md)` |
| Implicit text | `[[file]]` | `[[pierwsi]]` |
| Within sentences | `[Display](file\.md)` | "The [Pierwsi](pierwsi\.md) believe..." |

**Folder prefixes for disambiguation:**
```markdown
- [[races/pierwsi|Pierwsi]]
- [[creatures/yazghur|Yazghur]]
- [[characters/velan-kivar|Velan Kivar]]
```

---

## Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Race | English name | `pierwsi.md` |
| Creature | Common name | `yazghur.md` |
| Character | Full name, hyphens | `velan-kivar-zan-ehkovok.md` |
| Faction | Short name | `silver-compact.md` |
| Location | Common name | `torrs-gate.md` |
| Item | Item name, hyphens | `spirit-blade.md` |
| Lore | Topic name | `magic-systems.md` |

**No:**
- Spaces: `torr's gate.md` → `torrs-gate.md`
- Polish characters: `brama-torra.md` → `torrs-gate.md`
- Acronyms: `tfg.md` → `thornwood-forest-guard.md`
- Redundancy: `orc-race.md` → `orcs.md`

---

## Quality Checklist

Before committing:

- [ ] **Frontmatter complete**
  - [ ] `name:` filled (English)
  - [ ] `type:` matches file location
  - [ ] `category:` matches file location
  - [ ] `summary:` is one sentence, no trailing period
  - [ ] `tags:` array is populated (even if just type)
  - [ ] `related:` links to 1+ other entries

- [ ] **Content complete**
  - [ ] Overview table has all required fields
  - [ ] Description has 2+ paragraphs
  - [ ] Traits and relations use clear narrative structure
  - [ ] TODO section at bottom (if incomplete)

- [ ] **Links valid**
  - [ ] Wiki-links use `[[file|display]]` format
  - [ ] No broken links to non-existent files
  - [ ] Related files added to both entries

- [ ] **Style consistent**
  - [ ] Polish name in parentheses after English
  - [ ] Header hierarchy: `#` for title, `##` for sections
  - [ ] No bullet lists where tables fit better
  - [ ] English text (comments can be Polish)
  - [ ] No concrete mechanics (damage, durations, skill points, rarity ladders, prices, balance notes)

---

## Common Mistakes

### ❌ Wrong
```markdown
name: Orkowie
type: Race
summary: "The orcs are green and mean."
tags: orcs, green, mean
```

### ✅ Correct
```yaml
---
name: Orcs
type: sapient-race
category: races
tags: [orc, humanoid, green]
related:
  - silver-compact
summary: "A warrior culture of the Silver Woods, bound by the Compact"
---
```

### ❌ Wiki-Link Mistakes
```markdown
<!-- Wrong: implicit text -->
See the [[pierwsi]] for details.

<!-- Wrong: broken path -->
See [[races/pierwsi]] for details.

<!-- Wrong: period outside link -->
The [[pierwsi]] are ancient.
```

```markdown
<!-- Correct: explicit text -->
See [[pierwsi|the Pierwsi]] for details.

<!-- Correct: file name only -->
See [[pierwsi]] for details.

<!-- Correct: period before or integrated -->
The [[pierwsi|Pierwsi]] are ancient.
```

---

## Polish Usage Guidelines

| Element | Language | Example |
|---------|----------|---------|
| Race names (entry title) | Polish in parens | `# Orcs (Orkowie)` |
| Location names (entry title) | Polish in parens | `# Torr's Gate (Brama Torra)` |
| Body text | English | "The orcs speak Common." |
| In-universe names | As-is | "Zan Ehkovok" |
| UI/technical text | English | frontmatter, wiki-link |

---

## Related Documentation

| File | Purpose |
|------|---------|
| `STYLE.md` | Design philosophy, visual standards |
| `CONTRIBUTING.md` | This file - technical reference |
| `races/_index.md` | Race category index |
| `creatures/_index.md` | Creature category index |
| `items/_index.md` | Item category index |
| `_index.md` | Master wiki index |
