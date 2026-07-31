# Badge

Displays a badge or a component that looks like a badge.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add badge
```

```bash
npx shadcn-svelte@latest add badge
```

```bash
bun x shadcn-svelte@latest add badge
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Badge } from "$lib/components/ui/badge/index.js";
</script>
```

```svelte
<Badge variant="outline">Badge</Badge>
```

### [Link](#link)

You can use the `badgeVariants` helper to create a link that looks like a badge.

```svelte
<script lang="ts">
  import { badgeVariants } from "$lib/components/ui/badge/index.js";
</script>
<a href="/dashboard" class={badgeVariants({ variant: "outline" })}>Badge</a>
```