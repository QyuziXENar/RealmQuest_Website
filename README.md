# RealmQuest: Beyond the Veil — Promotional Website

A responsive, single-page promotional website built from the supplied RealmQuest game project. It takes cues from the cinematic presentation and strong navigation of official game sites while keeping the content deliberately introductory.

## Run locally

Requires Python 3.8+ (no third-party packages required).

```bash
python app.py
```

Open **http://127.0.0.1:8000** in your browser. Press `Ctrl+C` to stop the server.

You can also open `index.html` directly, though using the local server is recommended.

## Website features

- Cinematic opening section using the game's Oakwood gate background.
- Three selectable hero profiles: Warrior, Mage, and Archer.
- Interactive class tabs, previous/next controls, and keyboard arrow navigation.
- World overview with a small selection of regions.
- Teaser cards for the three Veil Anchor guardians.
- Responsive mobile navigation and layouts.
- Dedicated, responsive credits and team roster section with all supplied departments and honorable mentions.
- Vanilla HTML, CSS, and JavaScript; no build step or package installation.

## Content notes

The copy is intentionally promotional and avoids reproducing the full campaign, quest text, class balance tables, dungeon progression, or hidden story details. Class roles and signature skills are based on the project's `README.md`, `src/ui/class_info.py`, `src/skills/classes.py`, and `src/skills/skills.py`. World and antagonist references are based on `CAMPAIGN_STORY.md`, `src/maps/story.py`, and the world-lore modules.

## Asset notes

The `static/img/` directory contains selected, copied art from the supplied archive:
- Oakwood gate background: `assets/ui/menu_bg.png`
- Warrior sprite: `assets/characters/knight_idle.png`
- Mage sprite: Kendi idle frame
- Archer sprite: Elf Archer idle frame
- Goblin King action sheet, Minotaur sprite, and first Lich King idle frame

The three class-select portrait files in the game archive are explicitly marked **PLACEHOLDER**, so the website uses the character sprites instead.

The original project identifies itself as an educational project and not intended for commercial use. Review the original repository's asset credits and project terms before public/commercial deployment. This website is an unofficial promotional front-end assembled from the supplied project files.
