# Card

Displays a card with header, content, and footer.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add card
```

```bash
npx shadcn-svelte@latest add card
```

```bash
bun x shadcn-svelte@latest add card
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
</script>
```

```svelte
<Card.Root>
  <Card.Header>
    <Card.Title>Card Title</Card.Title>
    <Card.Description>Card Description</Card.Description>
  </Card.Header>
  <Card.Content>
    <p>Card Content</p>
  </Card.Content>
  <Card.Footer>
    <p>Card Footer</p>
  </Card.Footer>
</Card.Root>
```

## [Examples](#examples)

View Code

### [Spacing](#spacing)

In addition to the `size` prop, you can use the `--card-spacing` CSS variable to control the spacing between sections and the inset of card parts.

View Code

Use negative margins with `-mx-(--card-spacing)` to make content go edge to edge while keeping it aligned with the card inset. When the edge-to-edge content sits above a footer, use `-mb-(--card-spacing)` on `CardContent` to remove the section gap.

View Code

### [Image](#image)

Add an image before the card header to create a card with an image.

View Code