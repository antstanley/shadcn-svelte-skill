# Scroll Area

Augments native scroll functionality for custom, cross-browser styling.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add scroll-area
```

```bash
npx shadcn-svelte@latest add scroll-area
```

```bash
bun x shadcn-svelte@latest add scroll-area
```

## Usage

```svelte
<script lang="ts">
  import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";
</script>

<ScrollArea class="h-[200px] w-[350px] rounded-md border p-4">
  Jokester began sneaking into the castle in the middle of the night and
  leaving jokes all over the place: under the king's pillow, in his soup, even
  in the royal toilet. The king was furious, but he couldn't seem to stop
  Jokester.
</ScrollArea>
```

## Examples

### Vertical Scrolling

```svelte
<script lang="ts">
  import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";
  import { Separator } from "$lib/components/ui/separator/index.js";

  const tags = Array.from({ length: 50 }).map(
    (_, i, a) => `v1.2.0-beta.${a.length - i}`
  );
</script>

<ScrollArea class="h-72 w-48 rounded-md border">
  <div class="p-4">
    <h4 class="mb-4 text-sm leading-none font-medium">Tags</h4>
    {#each tags as tag (tag)}
      <div class="text-sm">{tag}</div>
      <Separator class="my-2" />
    {/each}
  </div>
</ScrollArea>
```

### Horizontal Scrolling

Set the `orientation` prop to `"horizontal"`:

```svelte
<script lang="ts">
  import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";

  const works = [
    { artist: "Ornella Binni", art: "https://images.unsplash.com/..." },
    { artist: "Tom Byrom", art: "https://images.unsplash.com/..." },
    // ...
  ];
</script>

<ScrollArea class="w-96 rounded-md border whitespace-nowrap" orientation="horizontal">
  <div class="flex w-max space-x-4 p-4">
    {#each works as artwork (artwork.artist)}
      <figure class="shrink-0">
        <div class="overflow-hidden rounded-md">
          <img
            src={artwork.art}
            alt="Photo by {artwork.artist}"
            class="aspect-[3/4] h-fit w-fit object-cover"
            width={300}
            height={400}
          />
        </div>
        <figcaption class="text-muted-foreground pt-2 text-xs">
          Photo by <span class="text-foreground font-semibold">{artwork.artist}</span>
        </figcaption>
      </figure>
    {/each}
  </div>
</ScrollArea>
```

## API

Built on [Bits UI Scroll Area](https://bits-ui.com/docs/components/scroll-area).

### Props

- `class` - Additional CSS classes
- `orientation` - "vertical" (default) or "horizontal"
