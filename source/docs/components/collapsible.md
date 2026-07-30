# Collapsible

An interactive component which expands/collapses a panel.

[Docs](https://bits-ui.com/docs/components/collapsible)

[API Reference](https://bits-ui.com/docs/components/collapsible#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add collapsible
```

```bash
npx shadcn-svelte@latest add collapsible
```

```bash
bun x shadcn-svelte@latest add collapsible
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible/index.js";
</script>
```

```svelte
<Collapsible.Root>
  <Collapsible.Trigger>Can I use this in my project?</Collapsible.Trigger>
  <Collapsible.Content>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </Collapsible.Content>
</Collapsible.Root>
```