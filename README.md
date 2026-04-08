# 🌍 Worldbuilding

Original campaign settings for tabletop RPGs — high fantasy and far-future sci-fi.

## Universes

### ⚔️ Fantasy

> *High fantasy world where ancient magic, political intrigue, and forgotten gods shape the fate of mortals. Heroes uncover secrets buried since the Sundering.*

**Setting**: Post-Sundering fantasy realm, 523 P.S.

**Core Conflict**: Political intrigue between noble houses, merchant guilds, and the Naterian Hegemony. Players navigate ancient magic, hidden conspiracies, and a cult seeking to use Blue Ore explosives.

**Key Hook**: Find the Black Stones of Ur before the cult, stop the Archmage's ascension to godhood.

| Category | Count | Examples |
|----------|-------|---------|
| Races | 7 | Naterians, Humans, Elves, Dwarves, Orcs, The Cleansed, Juuhroni |
| Characters | 20+ | Velan Kivar Zan-Ehkovok, Erin Telion, Damara Loehen, Archmage of Ur |
| Factions | 15+ | The Silver Compact, Naterian Hegemony, Noble Houses, Merchant Tides |
| Places | 15+ | Torr's Gate, The Silver Woods, Sky Torch, Great Bessam, Redwood |
| Lore | 13 | Spirit Binding, Mana, Aspects, Ancient Ones, The Abyss, Demons |
| Items | 3+ | Black Stones of Ur, Blue Ore, Soul Breaker |

📚 [Full Fantasy Index](fantasy/_index.md) · [Master Bible](fantasy/BIBLE.md)

### 🚀 Sci-Fi

> *Far future. Humanity scattered across the Veil Chain. AI awakens. The Void hungers. Corporate power collides with human freedom.*

**Setting**: 2147 P.S. — humanity among the stars, divided by corporate control.

**Core Conflict**: Exodus Corp's monopoly vs. independence. The Void's expansion vs. humanity's survival. AI personhood vs. property.

**Player Tone**: Mystery-driven, philosophical, cosmic horror adjacent.

| Category | Examples |
|----------|---------|
| Characters | Commander Chen, Unit-7, CEO Meridian, The Architect |
| Factions | Exodus Corp, The Collective, Free Traders |
| Places | Sol, Helios Station, The Frontier |

📚 [Full Sci-Fi Index](scifi/_index.md)

## Repository Structure

```
worldbuilding/
├── fantasy/
│   ├── BIBLE.md            # Master campaign reference
│   ├── STYLE.md            # Documentation conventions
│   ├── _index.md           # Navigation index
│   ├── adventures/         # Campaign plots and hooks
│   ├── characters/         # NPCs and protagonists
│   ├── creatures/          # Bestiary
│   ├── factions/           # Nations, houses, guilds
│   ├── items/              # Artifacts and materials
│   ├── lore/               # History, magic, cosmology
│   ├── places/             # Locations and maps
│   └── races/              # Peoples and cultures
└── scifi/
    ├── BIBLE.md            # Master setting reference
    ├── _index.md           # Navigation index
    ├── characters/         # Protagonists and antagonists
    ├── factions/           # Corporations and movements
    └── places/             # Systems and stations
```

## Conventions

- Files use **Markdown** with YAML frontmatter for metadata
- **Wiki-style links** between entries (e.g., `[[race-creation]]`)
- **Polish names** included alongside English for fantasy content
- **Style guide** maintained in [`fantasy/STYLE.md`](fantasy/STYLE.md)

## Used By

- [PicoClaw](https://github.com/goniszewski/picek_rpi) — AI agent workspace
- [Hermes](https://github.com/goniszewski/hermes_rat2) — AI agent (added as submodule)
