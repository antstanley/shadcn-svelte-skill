# Accordion

A vertically stacked set of interactive headings that each reveal a section of content.

[Docs](https://bits-ui.com/docs/components/accordion)

[API Reference](https://bits-ui.com/docs/components/accordion#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add accordion
```

```bash
npx shadcn-svelte@latest add accordion
```

```bash
bun x shadcn-svelte@latest add accordion
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Accordion from "$lib/components/ui/accordion/index.js";
</script>
```

```svelte
<Accordion.Root type="single">
  <Accordion.Item value="item-1">
    <Accordion.Trigger>Is it accessible?</Accordion.Trigger>
    <Accordion.Content>
      Yes. It adheres to the WAI-ARIA design pattern.
    </Accordion.Content>
  </Accordion.Item>
</Accordion.Root>
```