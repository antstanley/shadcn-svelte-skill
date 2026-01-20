# shadcn-svelte Skill

A Claude Code skill for [shadcn-svelte](https://shadcn-svelte.com) - a Svelte 5 port of shadcn/ui with beautifully designed, accessible components.

## Installation

### From Release

1. Download the latest `shadcn-svelte.skill` file from the [Releases](../../releases) page
2. Install in Claude Code:
   ```
   /skill install path/to/shadcn-svelte.skill
   ```

### From Source

1. Clone this repository
2. Package the skill:
   ```bash
   python scripts/package_skill.py shadcn-svelte dist
   ```
3. Install the generated skill:
   ```
   /skill install dist/shadcn-svelte.skill
   ```

## Usage

Once installed, the skill activates when you ask Claude about:
- shadcn-svelte components
- Bits UI integration
- SvelteKit UI component setup
- Forms with Superforms/Formsnap
- Dark mode with mode-watcher
- Tailwind CSS v4 theming

### Example Prompts

```
"Add a dialog component to my SvelteKit app"
"How do I create a form with validation using shadcn-svelte?"
"Set up dark mode in my Svelte project"
"Create a data table with sorting and pagination"
```

## What's Included

- **Quick start guide** for installation and basic usage
- **54 component references** - Button, Dialog, Form, Data Table, and more
- **Installation guides** for SvelteKit, Astro, and Vite
- **Dark mode setup** with mode-watcher
- **Migration guides** for Svelte 5 and Tailwind v4
- **Registry documentation** for creating custom component registries

## Development

### Repository Structure

```
.
├── shadcn-svelte/           # The skill source
│   ├── SKILL.md             # Main instructions
│   └── references/          # Component & guide docs
├── source/                  # Downloaded upstream docs
│   ├── llms.txt             # Doc index with local paths
│   └── docs/                # Raw documentation
├── scripts/                 # Build & maintenance scripts
├── prompts/                 # LLM prompts for maintenance
└── .github/workflows/       # CI/CD automation
```

### Validate the Skill

```bash
python scripts/validate_skill.py shadcn-svelte
```

### Package the Skill

```bash
python scripts/package_skill.py shadcn-svelte dist
```

Creates `dist/shadcn-svelte.skill`.

### Release

Create a new GitHub release and the workflow will automatically package and attach the `.skill` file.

## Updating Documentation

The skill's documentation comes from [shadcn-svelte.com](https://shadcn-svelte.com). To update:

### 1. Download Latest Docs

```bash
python scripts/download_docs.py
```

This downloads:
- All `.md` files referenced in `llms.txt`
- Saves to `source/docs/`
- Updates `source/llms.txt` with local paths

### 2. Update the Skill

Use the provided prompt with Claude Code to update the skill:

```bash
cat prompts/UPDATE_SKILL.md
```

Or run Claude Code in this directory and ask:

```
Read prompts/UPDATE_SKILL.md and follow the instructions to update the skill
based on any changes in source/docs/
```

The prompt guides Claude to:
1. Compare source docs with current skill references
2. Update `shadcn-svelte/references/` with new content
3. Update `SKILL.md` if needed
4. Validate the updated skill

### 3. Validate and Package

```bash
python scripts/validate_skill.py shadcn-svelte
python scripts/package_skill.py shadcn-svelte dist
```

### Automated Updates

A GitHub workflow runs daily at 4am UTC to:
1. Download latest documentation
2. Create a Draft PR if changes are detected

Review and merge these PRs to keep the skill up to date.

## License

MIT
