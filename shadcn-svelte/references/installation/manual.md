# Manual Installation for shadcn-svelte

This guide outlines the setup process for shadcn-svelte in your project.

## Core Setup Steps

The installation requires several foundational components:

1. **Tailwind CSS**: Add using the `sv` CLI with the command appropriate to your package manager (pnpm, npm, or bun)

2. **Dependencies**: Install utility libraries including tailwind-variants, clsx, tailwind-merge, and tw-animate-css

3. **Icon Library**: Add `@lucide/svelte` for icon support

## Configuration Requirements

**Path Aliases**: Users must configure aliases in their build setup. SvelteKit users modify `svelte.config.js`, while non-SvelteKit projects need updates to both `tsconfig.json` and `vite.config.ts`.

**Styling**: The guide recommends importing Tailwind and animation libraries, then establishing a comprehensive set of CSS custom properties using the oklch color format for both light and dark themes.

**Utilities**: Create a `cn` helper function that combines clsx and twMerge to streamline conditional class application.

```ts
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

## Layout Setup

Finally, establish a root layout component (`src/routes/+layout.svelte`) that imports your global styles, enabling the design system throughout your application.

Once complete, you're ready to add components to your project using the shadcn-svelte CLI.
