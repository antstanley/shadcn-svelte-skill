# registry-item.json

Schema reference for individual registry items.

## Overview

The `registry-item.json` schema defines individual registry items for packaging and distributing components.

## Core Properties

### $schema

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry-item.json"
}
```

### name

Unique identifier for the item:

```json
{
  "name": "my-component"
}
```

### title

Human-readable label:

```json
{
  "title": "My Component"
}
```

### description

Detailed information about the item:

```json
{
  "description": "A reusable component for displaying user profiles"
}
```

### type

Determines how items are processed:

- `registry:block` - Complex components with multiple files
- `registry:component` - Simple, single-purpose components
- `registry:lib` - Utilities and library code
- `registry:hook` - Svelte hooks
- `registry:ui` - UI primitives and foundations
- `registry:page` - Routes and page components
- `registry:file` - Miscellaneous files
- `registry:style` - Style configurations
- `registry:theme` - Theme definitions

## Dependencies

### dependencies

NPM packages required by the item:

```json
{
  "dependencies": ["clsx", "tailwind-merge"]
}
```

### registryDependencies

Other registry items required:

```json
{
  "registryDependencies": [
    "button",
    "input",
    "https://other-registry.com/r/custom.json",
    "local:my-component",
    "./stepper.json"
  ]
}
```

Supports:
- shadcn-svelte registry names
- Full URLs to external registries
- Local aliases prefixed with `local:`
- Relative file paths

## Files

### files

Array of files included in the item:

```json
{
  "files": [
    {
      "path": "registry/my-component/my-component.svelte",
      "type": "registry:component"
    },
    {
      "path": "registry/my-component/+page.svelte",
      "type": "registry:page",
      "target": "src/routes/my-component/+page.svelte"
    }
  ]
}
```

- `path` - Location in the registry
- `type` - File classification
- `target` - Destination (required for pages and files). Use `~` for project root.

## Styling

### cssVars

Define CSS variables by theme:

```json
{
  "cssVars": {
    "theme": {
      "--animate-duration": "0.3s"
    },
    "light": {
      "primary": "oklch(0.5 0.2 240)"
    },
    "dark": {
      "primary": "oklch(0.7 0.2 240)"
    }
  }
}
```

### css

Add CSS rules to the project:

```json
{
  "css": [
    "@layer base { body { @apply antialiased; } }",
    "@layer components { .card { @apply rounded-lg border; } }",
    "@keyframes fade { from { opacity: 0; } to { opacity: 1; } }"
  ]
}
```

## Metadata

### author

Item creator information:

```json
{
  "author": "huntabyte"
}
```

### docs

Installation instructions:

```json
{
  "docs": "Run `pnpm add my-package` before using this component."
}
```

### categories

Organizational tags:

```json
{
  "categories": ["forms", "inputs"]
}
```

### meta

Custom key-value pairs:

```json
{
  "meta": {
    "version": "2.0.0",
    "featured": true
  }
}
```
