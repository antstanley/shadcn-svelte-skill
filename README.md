# shadcn-svelte Skill

A Claude Code skill for [shadcn-svelte](https://shadcn-svelte.com) - a Svelte 5 port of shadcn/ui with beautifully designed, accessible components.

## Installation

Download the latest `.skill` file from the [Releases](../../releases) page and install it in Claude Code.

## What's Included

- **Quick start guide** for installation and basic usage
- **54 component references** - Button, Dialog, Form, Data Table, and more
- **Installation guides** for SvelteKit, Astro, and Vite
- **Dark mode setup** with mode-watcher
- **Migration guides** for Svelte 5 and Tailwind v4
- **Registry documentation** for creating custom component registries

## Development

### Validate the skill

```bash
python scripts/validate_skill.py shadcn-svelte
```

### Package the skill

```bash
python scripts/package_skill.py shadcn-svelte dist
```

This creates `dist/shadcn-svelte.skill`.

### Release

Create a new GitHub release and the workflow will automatically package and attach the `.skill` file.

## License

MIT
