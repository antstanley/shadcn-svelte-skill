# FAQ

Frequently asked questions about the registry.

## Complex Components

Registry items can include multiple file types:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry-item.json",
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A hello world block",
  "files": [
    {
      "path": "registry/hello-world/+page.svelte",
      "type": "registry:page",
      "target": "src/routes/hello-world/+page.svelte"
    },
    {
      "path": "registry/hello-world/hello-world.svelte",
      "type": "registry:component"
    },
    {
      "path": "registry/hello-world/use-hello.svelte.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/hello-world/utils.ts",
      "type": "registry:lib"
    }
  ]
}
```

## Adding Custom Tailwind Colors

Add custom colors to `cssVars` under `light` and `dark` keys:

```json
{
  "cssVars": {
    "light": {
      "brand": "oklch(0.5 0.2 240)"
    },
    "dark": {
      "brand": "oklch(0.7 0.2 240)"
    }
  }
}
```

Once added, the color becomes available as utility classes:

```html
<div class="bg-brand text-brand-foreground">...</div>
```

## Customizing Theme Variables

Add theme overrides using `cssVars.theme`:

```json
{
  "cssVars": {
    "theme": {
      "--text-base": "1rem",
      "--text-sm": "0.875rem",
      "--ease-in-out": "cubic-bezier(0.4, 0, 0.2, 1)",
      "--font-sans": "Inter, system-ui, sans-serif"
    }
  }
}
```
