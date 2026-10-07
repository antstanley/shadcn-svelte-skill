# scroll-fade

Utilities for adding a fade effect to the edges of a scroll container.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  const items = Array.from({ length: 12 }, (_, index) => index + 1);
</script>
<div class="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border">
  <div class="no-scrollbar h-72 scroll-fade overflow-y-auto">
    <div class="flex flex-col gap-1.5 p-1.5">
      {#each items as item (item)}
        <div class="rounded-lg bg-muted px-3 py-2.5 text-sm">
          Item {item}
        </div>
      {/each}
    </div>
  </div>
</div>
```

View Code

## [Installation](#installation)

If your project was set up with `npx shadcn-svelte@latest init`, you already have `scroll-fade`. It ships with the `shadcn-svelte` package, which the CLI imports in your global CSS file.

Otherwise, install the `shadcn-svelte` package:

```bash
npm install shadcn-svelte
```

Then import the shared utilities in your global CSS file:

```css
@import "tailwindcss";
@import "shadcn-svelte/tailwind.css";
```

## [Usage](#usage)

| Class                                           | Styles                                                                                                                            |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scroll-fade`                     | `mask-image: var(--scroll-fade-mask, var(--scroll-fade-block));` `animation-timeline: scroll(self y);`       |
| `scroll-fade-y`                   | `mask-image: var(--scroll-fade-mask, var(--scroll-fade-block));` `animation-timeline: scroll(self y);`       |
| `scroll-fade-x`                   | `mask-image: var(--scroll-fade-mask, var(--scroll-fade-inline));` `animation-timeline: scroll(self inline);` |
| `scroll-fade-t`                   | Fade mask on the top edge. `animation-timeline: scroll(self y);`                                                    |
| `scroll-fade-b`                   | Fade mask on the bottom edge. `animation-timeline: scroll(self y);`                                                 |
| `scroll-fade-l`                   | Fade mask on the left edge. `animation-timeline: scroll(self x);`                                                   |
| `scroll-fade-r`                   | Fade mask on the right edge. `animation-timeline: scroll(self x);`                                                  |
| `scroll-fade-s`                   | Fade mask on the start edge, mirrors in RTL. `animation-timeline: scroll(self inline);`                             |
| `scroll-fade-e`                   | Fade mask on the end edge, mirrors in RTL. `animation-timeline: scroll(self inline);`                               |
| `scroll-fade-<number>`            | `--scroll-fade-size: calc(var(--spacing) * <number>);`                                                                     |
| `scroll-fade-[<value>]`           | `--scroll-fade-size: <value>;`                                                                                             |
| `scroll-fade-{t,b,s,e}-<number>`  | `--scroll-fade-{t,b,s,e}-size: calc(var(--spacing) * <number>);`                                                           |
| `scroll-fade-{t,b,s,e}-[<value>]` | `--scroll-fade-{t,b,s,e}-size: <value>;`                                                                                   |
| `scroll-fade-none`                | `--scroll-fade-mask: none;`                                                                                  |

Add `scroll-fade` or `scroll-fade-y` to the scroll container, i.e. the element that has `overflow-y-auto`.

```svelte
<div class="scroll-fade overflow-y-auto"></div>
```

The fade is scroll-aware and tracks the scroll position:

- At rest, the top edge is crisp and the bottom edge fades to hint at more content.  
- As you scroll, a fade appears at the top and both edges stay faded mid-scroll.  
- At the end, the bottom edge sharpens to show you have reached the last item. The fade is applied with `mask-image`, so it dissolves the content itself rather than overlaying a color. The mask uses a linear fade from transparent to black, so it adapts to any background without configuration. If your scroll area sits inside a card, put the background and border on a wrapper and `scroll-fade` on the inner scroller, so the fade dissolves the content and not the card.

The [`ScrollArea`](https://shadcn-svelte.com/docs/components/scroll-area) component can use `scroll-fade` on its scrollable viewport.

## [No Overflow, No Fade](#no-overflow-no-fade)

If the content does not overflow, no fade is shown. You can apply `scroll-fade` to any list without checking whether it scrolls.

```svelte
<script lang="ts">
  const items = Array.from({ length: 3 }, (_, index) => index + 1);
</script>
<div class="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border">
  <div class="no-scrollbar scroll-fade overflow-y-auto">
    <div class="flex flex-col gap-1.5 p-1.5">
      {#each items as item (item)}
        <div class="rounded-lg bg-muted px-3 py-2.5 text-sm">
          Item {item}
        </div>
      {/each}
    </div>
  </div>
</div>
```

View Code

## [Horizontal Scrolling](#horizontal-scrolling)

Use `scroll-fade-x` on containers that scroll horizontally, i.e. the element that has `overflow-x-auto`.

```svelte
<script lang="ts">
  const tags = [
    "Design",
    "Engineering",
    "Marketing",
    "Product",
    "Research",
    "Sales",
    "Support",
    "Operations",
    "Finance",
    "Legal",
    "People",
    "Security"
 ];
</script>
<div class="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border">
  <div class="no-scrollbar scroll-fade-x overflow-x-auto">
    <div class="flex w-max gap-1.5 p-1.5">
      {#each tags as tag (tag)}
        <div class="shrink-0 rounded-lg bg-muted px-3 py-2.5 text-sm">
          {tag}
        </div>
      {/each}
    </div>
  </div>
</div>
```

View Code

```svelte
<div class="flex scroll-fade-x overflow-x-auto"></div>
```

The horizontal fade is direction-aware. In RTL layouts, the crisp edge and the fade follow the reading direction with no extra classes needed. `scroll-fade-<number>` and `scroll-fade-none` work the same for both axes.

## [Edge Fades](#edge-fades)

Use edge utilities when only one edge should track the scroll position.

```svelte
<script lang="ts">
  const items = [
    "Inbox triage",
    "Design review",
    "API contract",
    "QA pass",
    "Launch notes",
    "Metrics follow-up"
 ];
  const tags = [
    "Design",
    "Engineering",
    "Marketing",
    "Product",
    "Research",
    "Sales",
    "Support",
    "Operations"
 ];
</script>
{#snippet edgeItems()}
  <div class="flex flex-col gap-1.5 p-1.5">
    {#each items as item (item)}
      <div class="rounded-lg bg-muted px-3 py-2.5 text-sm">
        {item}
      </div>
    {/each}
  </div>
{/snippet}
{#snippet edgeTags()}
  <div class="flex w-max gap-1.5 p-1.5">
    {#each tags as tag (tag)}
      <div class="shrink-0 rounded-lg bg-muted px-3 py-2.5 text-sm">
        {tag}
      </div>
    {/each}
  </div>
{/snippet}
<div class="mx-auto flex max-w-xs min-w-0 flex-col gap-6">
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar h-36 scroll-fade-t overflow-y-auto">
        {@render edgeItems()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade-t
    </p>
  </div>
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar h-36 scroll-fade-b overflow-y-auto">
        {@render edgeItems()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade-b
    </p>
  </div>
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar scroll-fade-s overflow-x-auto">
        {@render edgeTags()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade-s
    </p>
  </div>
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar scroll-fade-e overflow-x-auto">
        {@render edgeTags()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade-e
    </p>
  </div>
</div>
```

View Code

```svelte
<div class="scroll-fade-b overflow-y-auto"></div>
```

The edge utilities are scroll-aware. Start edges fade in after you scroll away from the start, and end edges fade out when you reach the end. Use `scroll-fade-t`, `scroll-fade-b`, `scroll-fade-l`, and `scroll-fade-r` for physical edges. Use `scroll-fade-s` and `scroll-fade-e` for logical inline edges that mirror in RTL.

## [Fade Size](#fade-size)

The fade depth defaults to `12%` of the container, capped at `40px` so tall scrollers stay subtle. Use `scroll-fade-<number>` to set a fixed size on the spacing scale instead, the same way `scroll-mt-<number>` works.

```svelte
<script lang="ts">
  const items = Array.from({ length: 8 }, (_, index) => index + 1);
</script>
{#snippet sizeItems()}
  <div class="flex flex-col gap-1.5 p-1.5">
    {#each items as item (item)}
      <div class="rounded-lg bg-muted px-3 py-2.5 text-sm">
        Item {item}
      </div>
    {/each}
  </div>
{/snippet}
<div class="mx-auto flex w-full max-w-xs flex-col gap-6">
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar h-48 scroll-fade overflow-y-auto scroll-fade-4">
        {@render sizeItems()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade-4
    </p>
  </div>
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar h-48 scroll-fade overflow-y-auto scroll-fade-24">
        {@render sizeItems()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade-24
    </p>
  </div>
</div>
```

View Code

```svelte
<div class="scroll-fade overflow-y-auto scroll-fade-24"></div>
```

For one-off values, use an arbitrary length or percentage:

```svelte
<div class="scroll-fade overflow-y-auto scroll-fade-[15%]"></div>
```

To fade opposite edges by different amounts, use the per-edge modifiers `scroll-fade-t-<number>`, `scroll-fade-b-<number>`, `scroll-fade-s-<number>`, and `scroll-fade-e-<number>`. They override `scroll-fade-<number>` on the edge they target and accept arbitrary values too.

```svelte
<div class="scroll-fade overflow-y-auto scroll-fade-b-8 scroll-fade-t-2">
</div>
```

Use the logical `s`/`e` modifiers for horizontal scrollers so the sizes mirror in RTL.

The fade eases in and out over a fixed scroll distance rather than appearing instantly. That distance is the `--scroll-fade-reveal` variable, `96px` by default and independent of the fade depth. Lower it for a snappier reveal or raise it for a more gradual one:

```svelte
<div class="scroll-fade overflow-y-auto [--scroll-fade-reveal:64px]">
</div>
```

## [Disabling the Fade](#disabling-the-fade)

Use `scroll-fade-none` to remove the fade. It works in any class order, so the typical use is responsive or stateful:

```svelte
<div class="scroll-fade overflow-y-auto md:scroll-fade-none">
</div>
```

```svelte
<script lang="ts">
  const items = Array.from({ length: 8 }, (_, index) => index + 1);
</script>
{#snippet noneItems()}
  <div class="flex flex-col gap-1.5 p-1.5">
    {#each items as item (item)}
      <div class="rounded-lg bg-muted px-3 py-2.5 text-sm">
        Item {item}
      </div>
    {/each}
  </div>
{/snippet}
<div class="mx-auto flex max-w-xs min-w-0 flex-col gap-6">
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div class="no-scrollbar h-48 scroll-fade overflow-y-auto">
        {@render noneItems()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade
    </p>
  </div>
  <div class="flex flex-col gap-3">
    <div class="overflow-hidden rounded-2xl border">
      <div
        class="no-scrollbar h-48 scroll-fade overflow-y-auto scroll-fade-none"
      >
        {@render noneItems()}
      </div>
    </div>
    <p class="text-center font-mono text-xs text-muted-foreground">
      scroll-fade scroll-fade-none
    </p>
  </div>
</div>
```

View Code

## [Fallback](#fallback)

The scroll-aware behavior is implemented with [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations), with no JavaScript and no scroll listeners. In browsers that do not support scroll-driven animations, `scroll-fade` falls back to a static fade on both edges, and edge utilities fall back to a static fade on the selected edge.

Since the mask is applied to the scroll container itself, a visible scrollbar fades with the content at the edges. Pair `scroll-fade` with `no-scrollbar`, which ships in the same package, if you want to hide the scrollbar entirely.

## [RTL](#rtl) `scroll-fade-x` follows the reading direction. At rest, the start edge is crisp and the end edge fades. In RTL layouts that means a crisp right edge and a fade on the left, mirrored from LTR.

```svelte
<script lang="ts">
  const tags = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
 ];
</script>
<div
  class="mx-auto w-full max-w-xs overflow-hidden rounded-2xl border"
  dir="rtl"
>
  <div class="no-scrollbar scroll-fade-x overflow-x-auto">
    <div class="flex w-max gap-1.5 p-1.5">
      {#each tags as tag (tag)}
        <div class="shrink-0 rounded-lg bg-muted px-3 py-2.5 text-sm">
          {tag}
        </div>
      {/each}
    </div>
  </div>
</div>
```

View Code