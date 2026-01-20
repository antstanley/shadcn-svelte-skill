# Tailwind v4

Upgrading to Tailwind v4 with shadcn-svelte.

## Overview

The CLI now supports Tailwind v4 and Svelte 5 for initialization. Key changes:

- All components include `data-slot` attributes for enhanced styling
- Default border color changed to `currentcolor` in Tailwind v4
- HSL colors converted to OKLCH (non-breaking for v3 projects)
- The `default` style is deprecated; new projects use `new-york`
- Buttons default to standard cursor styling

## Prerequisites

Read the [Tailwind v4 Compatibility Docs](https://tailwindcss.com/docs/v4-beta#compatibility) and ensure your project is ready. Tailwind v4 targets modern browsers with cutting-edge features.

## Upgrade Steps

### 1. Run Tailwind Upgrade

Follow the [official Tailwind v4 upgrade guide](https://tailwindcss.com/docs/upgrade-guide) and run the codemod:

```bash
npx @tailwindcss/upgrade@next
```

### 2. Switch to Vite Plugin

Remove PostCSS configuration and switch to the Vite plugin:

```bash
# Remove postcss.config.js
rm postcss.config.js

# Uninstall PostCSS plugin
pnpm remove @tailwindcss/postcss

# Install Vite plugin
pnpm i @tailwindcss/vite
```

Update `vite.config.ts`:

```ts
import { sveltekit } from "@sveltejs/kit/vite";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [tailwindcss(), sveltekit()],
});
```

### 3. Update app.css

```css
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  /* Your theme variables */
}
```

### 4. Replace tailwindcss-animate

```bash
pnpm remove tailwindcss-animate
pnpm i tw-animate-css
```

### 5. Update Dependencies

Update all shadcn-svelte dependencies to latest versions.

### 6. Update Components

Use the CLI to refresh component colors:

```bash
pnpm dlx shadcn-svelte@latest add button --overwrite
```

## Resources

- Demo: https://v4.shadcn-svelte.com
- Issues: https://github.com/huntabyte/shadcn-svelte/issues
