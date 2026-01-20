# Svelte 5

Migrating from Svelte 4 + Tailwind 3 to Svelte 5 with shadcn-svelte.

## Overview

With Svelte 5 comes significant changes to this project, along with the headless UI library Bits UI.

**Important:** Complete the Svelte 5 migration before upgrading to Tailwind v4.

## Steps

### 1. Update components.json

Add the registry URL and additional alias keys:

```json
{
  "$schema": "https://shadcn-svelte.com/schema.json",
  "style": "new-york",
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "src/app.css",
    "baseColor": "zinc"
  },
  "aliases": {
    "components": "$lib/components",
    "utils": "$lib/utils",
    "ui": "$lib/components/ui",
    "hooks": "$lib/hooks"
  },
  "typescript": true,
  "registry": "https://shadcn-svelte.com/registry"
}
```

### 2. Install tailwindcss-animate

```bash
pnpm i tailwindcss-animate
```

Add to your `tailwind.config.ts`:

```ts
import animate from "tailwindcss-animate";

export default {
  // ...
  plugins: [animate],
};
```

### 3. Simplify utils.ts

```ts
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export type WithoutChildren<T> = T extends { children?: any }
  ? Omit<T, "children">
  : T;

export type WithoutChildrenOrChild<T> = T extends { children?: any; child?: any }
  ? Omit<T, "children" | "child">
  : T;
```

### 4. Update Dependencies

Update to these minimum versions:

| Package | Version |
| --- | --- |
| bits-ui | ^1.0.0 |
| svelte-sonner | ^1.0.0 |
| @lucide/svelte | ^0.482.0 |
| paneforge | ^1.0.0-next.5 |
| vaul-svelte | ^1.0.0-next.7 |
| mode-watcher | ^1.0.0 |

### 5. Deprecated Libraries

Replace these libraries:

- **cmdk-sv** → Use Bits UI's Command component
- **svelte-headless-table** → Use `@tanstack/table-core`
- **svelte-radix** → Use `@lucide/svelte`
- **lucide-svelte** → Use `@lucide/svelte`

### 6. Migrate Components

Commit your changes, then use the CLI to update components:

```bash
pnpm dlx shadcn-svelte@latest add button --overwrite
pnpm dlx shadcn-svelte@latest add card --overwrite
# ... repeat for each component
```

Or update all at once:

```bash
pnpm dlx shadcn-svelte@latest add --all --overwrite
```
