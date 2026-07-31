# Hover Card

For sighted users to preview content available behind a link.

[Docs](https://bits-ui.com/docs/components/link-preview)

[API Reference](https://bits-ui.com/docs/components/link-preview#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add hover-card
```

```bash
npx shadcn-svelte@latest add hover-card
```

```bash
bun x shadcn-svelte@latest add hover-card
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as HoverCard from "$lib/components/ui/hover-card/index.js";
</script>
```

```svelte
<HoverCard.Root>
  <HoverCard.Trigger>Hover</HoverCard.Trigger>
  <HoverCard.Content>
    SvelteKit - Web development, streamlined </HoverCard.Content>
</HoverCard.Root>
```