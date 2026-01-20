# Badge

Displays a badge or a component that looks like a badge.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add badge
```

```bash
npx shadcn-svelte@latest add badge
```

```bash
bun x shadcn-svelte@latest add badge
```

## Usage

```svelte
<script lang="ts">
  import { Badge } from "$lib/components/ui/badge/index.js";
</script>

<Badge variant="outline">Badge</Badge>
```

## Examples

### Variants

```svelte
<Badge>Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="destructive">Destructive</Badge>
<Badge variant="outline">Outline</Badge>
```

### With Icon

```svelte
<script lang="ts">
  import BadgeCheckIcon from "@lucide/svelte/icons/badge-check";
  import { Badge } from "$lib/components/ui/badge/index.js";
</script>

<Badge variant="secondary" class="bg-blue-500 text-white">
  <BadgeCheckIcon />
  Verified
</Badge>
```

### Pill/Counter

```svelte
<Badge class="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums">8</Badge>
<Badge class="h-5 min-w-5 rounded-full px-1 font-mono tabular-nums" variant="destructive">
  99
</Badge>
```

### As Link

Use the `badgeVariants` helper to create a link styled as a badge:

```svelte
<script lang="ts">
  import { badgeVariants } from "$lib/components/ui/badge/index.js";
</script>

<a href="/dashboard" class={badgeVariants({ variant: "outline" })}>Badge</a>
```

## Variants

- **default** - Primary badge styling
- **secondary** - Subdued badge styling
- **destructive** - Error/warning badge styling
- **outline** - Border-only badge styling
