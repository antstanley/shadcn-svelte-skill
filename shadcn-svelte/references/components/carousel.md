# Carousel

A carousel with motion and swipe built using Embla.

## About

The carousel component is built using [Embla Carousel](https://www.embla-carousel.com/get-started/svelte/).

## Installation

```bash
pnpm dlx shadcn-svelte@latest add carousel
```

```bash
npx shadcn-svelte@latest add carousel
```

```bash
bun x shadcn-svelte@latest add carousel
```

## Usage

```svelte
<script lang="ts">
  import * as Carousel from "$lib/components/ui/carousel/index.js";
</script>

<Carousel.Root>
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
  <Carousel.Previous />
  <Carousel.Next />
</Carousel.Root>
```

## Examples

### Sizes

Use the `basis` utility class on `<Carousel.Item />`:

```svelte
<Carousel.Root>
  <Carousel.Content>
    <Carousel.Item class="basis-1/3">...</Carousel.Item>
    <Carousel.Item class="basis-1/3">...</Carousel.Item>
    <Carousel.Item class="basis-1/3">...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

### Spacing

Use `ps-[VALUE]` on items and `-ms-[VALUE]` on content:

```svelte
<Carousel.Root>
  <Carousel.Content class="-ms-4">
    <Carousel.Item class="ps-4">...</Carousel.Item>
    <Carousel.Item class="ps-4">...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

### Orientation

```svelte
<Carousel.Root orientation="vertical">
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

## Options

Pass Embla options via the `opts` prop:

```svelte
<Carousel.Root
  opts={{
    align: "start",
    loop: true,
  }}
>
  <!-- content -->
</Carousel.Root>
```

## API

Use `setApi` to access the carousel API:

```svelte
<script lang="ts">
  import type { CarouselAPI } from "$lib/components/ui/carousel/context.js";

  let api = $state<CarouselAPI>();
  let current = $state(0);

  $effect(() => {
    if (api) {
      current = api.selectedScrollSnap() + 1;
      api.on("select", () => {
        current = api!.selectedScrollSnap() + 1;
      });
    }
  });
</script>

<Carousel.Root setApi={(emblaApi) => (api = emblaApi)}>
  <!-- content -->
</Carousel.Root>
```

## Plugins

Use Embla plugins via the `plugins` prop:

```svelte
<script lang="ts">
  import Autoplay from "embla-carousel-autoplay";
</script>

<Carousel.Root plugins={[Autoplay({ delay: 2000 })]}>
  <!-- content -->
</Carousel.Root>
```

See [Embla Carousel docs](https://www.embla-carousel.com/api/plugins/) for more plugins.
