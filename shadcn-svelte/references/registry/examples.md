# Examples

Example registry items for different use cases.

## registry:style

Create custom styling systems:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry-item.json",
  "name": "my-style",
  "type": "registry:style",
  "dependencies": ["clsx", "tailwind-merge"],
  "registryDependencies": ["button", "input"],
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.2 0 0)"
    },
    "dark": {
      "background": "oklch(0.15 0 0)",
      "foreground": "oklch(0.95 0 0)"
    }
  }
}
```

Use `"extends": "none"` for standalone styles without shadcn-svelte defaults.

## registry:theme

Define color schemes:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry-item.json",
  "name": "ocean-theme",
  "type": "registry:theme",
  "cssVars": {
    "light": {
      "primary": "oklch(0.5 0.15 220)",
      "primary-foreground": "oklch(1 0 0)"
    },
    "dark": {
      "primary": "oklch(0.7 0.15 220)",
      "primary-foreground": "oklch(0.1 0 0)"
    }
  }
}
```

## registry:block

Reusable component compositions:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry-item.json",
  "name": "login-form",
  "type": "registry:block",
  "title": "Login Form",
  "description": "A login form with email and password",
  "registryDependencies": ["button", "input", "label", "card"],
  "files": [
    {
      "path": "registry/login-form/login-form.svelte",
      "type": "registry:component"
    }
  ]
}
```

## registry:component

Individual UI elements:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry-item.json",
  "name": "fancy-button",
  "type": "registry:component",
  "registryDependencies": ["button"],
  "files": [
    {
      "path": "registry/fancy-button/fancy-button.svelte",
      "type": "registry:component"
    }
  ],
  "css": ["@layer components { .fancy-button { @apply transition-transform hover:scale-105; } }"]
}
```

## Animations

Define keyframes with theme variables:

```json
{
  "cssVars": {
    "theme": {
      "--animate-fade-in": "fade-in 0.3s ease-out"
    }
  },
  "css": [
    "@keyframes fade-in { from { opacity: 0; } to { opacity: 1; } }"
  ]
}
```

## Override Primitives

Reference remote registries:

```json
{
  "registryDependencies": [
    "https://other-registry.com/r/custom-button.json"
  ]
}
```
