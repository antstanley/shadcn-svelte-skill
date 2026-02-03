# Changelog

All notable changes to the shadcn-svelte skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2026-02-03

### Changed

- Updated all 78 reference docs to latest upstream shadcn-svelte documentation
- Component count increased from 54 to 59 (updated SKILL.md accordingly)
- Form component (`form.md`) is no longer marked as deprecated — deprecation notice removed upstream

### Added

- New component references: Button Group, Empty, Field, Input Group, Item, Kbd, Native Select, Spinner
- Expanded documentation across all existing components with additional examples, API references, and usage patterns

## [1.0.2] - 2025-01-20

### Changed

- Install script now installs to current project directory (`.claude/skills/`) instead of global home directory

## [1.0.1] - 2025-01-20

### Added

- Bash install script for one-liner curl-based installation
- Install script uploaded to GitHub releases alongside `.skill` file

### Changed

- Updated README with curl installation instructions
- Simplified "From Source" instructions to use manual extraction
- Removed references to `/skill install` command

## [1.0.0] - 2025-01-20

### Added

- Initial release of the shadcn-svelte Claude Code skill

#### Skill Contents
- **SKILL.md** - Quick start guide with installation, usage patterns, and reference navigation
- **54 component references** - Comprehensive documentation for all shadcn-svelte components:
  - Form & Input: Button, Checkbox, Combobox, Date Picker, Form, Input, Radio Group, Select, Slider, Switch, Textarea, and more
  - Layout & Navigation: Accordion, Breadcrumb, Navigation Menu, Resizable, Tabs, Sidebar
  - Overlays & Dialogs: Alert Dialog, Command, Context Menu, Dialog, Drawer, Dropdown Menu, Popover, Sheet, Tooltip
  - Feedback & Status: Alert, Badge, Progress, Skeleton, Sonner (toasts), Spinner
  - Display & Media: Avatar, Card, Carousel, Chart, Data Table, Table, Typography
- **Installation guides** - SvelteKit, Astro, Vite, and manual setup
- **Dark mode documentation** - mode-watcher integration for Svelte and Astro
- **Migration guides** - Svelte 5 and Tailwind v4 upgrade paths
- **Registry documentation** - Custom component registry creation

#### Tooling
- `download_docs.py` - Downloads latest documentation from shadcn-svelte.com
- `validate_skill.py` - Validates skill structure and YAML frontmatter
- `package_skill.py` - Packages skill into distributable `.skill` file

#### Automation
- **Release workflow** - Automatically packages and attaches `.skill` file on GitHub releases
- **Update workflow** - Daily check for documentation updates with Draft PR creation

#### Documentation
- `README.md` - Installation, usage, and maintenance instructions
- `prompts/UPDATE_SKILL.md` - LLM prompt for updating skill with latest docs

### Technical Details

- Built following [Anthropic skill-creator guidelines](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- Documentation sourced from [shadcn-svelte.com/llms.txt](https://www.shadcn-svelte.com/llms.txt)
- Supports Svelte 5, SvelteKit, Tailwind CSS v4, and Bits UI
