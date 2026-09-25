# shimmer

Utilities for adding a shimmer effect to text elements.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<p class="shimmer text-sm text-muted-foreground">Generating response&hellip;</p>
```

View Code

## [Installation](#installation)

If your project was set up with `npx shadcn-svelte@latest init`, you already have `shimmer`. It ships with the `shadcn-svelte` package, which the CLI imports in your global CSS file.

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

| Class                                       | Styles                                                                                                             |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shimmer`                     | `background-clip: text;` `animation: tw-shimmer var(--shimmer-duration, 2s) linear infinite;` |
| `shimmer-once`                | `animation-iteration-count: 1;`                                                                             |
| `shimmer-reverse`             | `animation-direction: reverse;`                                                                             |
| `shimmer-none`                | `--shimmer-image: none;` `--shimmer-text-fill: currentColor;`                                 |
| `shimmer-color-<color>`       | `--shimmer-color: <color>;`                                                                                 |
| `shimmer-color-[<value>]`     | `--shimmer-color: <value>;`                                                                                 |
| `shimmer-color-<color>/<pct>` | `--shimmer-color: color-mix(in oklch, <color> <pct>, transparent);`                                         |
| `shimmer-duration-<number>`   | `--shimmer-duration: calc(<number> * 1ms);`                                                                 |
| `shimmer-spread-<number>`     | `--shimmer-spread: calc(var(--spacing) * <number>);`                                                        |
| `shimmer-spread-[<value>]`    | `--shimmer-spread: <value>;`                                                                                |
| `shimmer-angle-<number>`      | `--shimmer-angle: calc(<number> * 1deg);`                                                     |

Add `shimmer` to a text element.

```svelte
<p class="shimmer text-muted-foreground">Generating response&hellip;</p>
```

The shimmer is built on `currentColor`, so it adapts to the element:

- The highlight is derived from the text color, with no configuration needed.  
- It works on any color, from `text-muted-foreground` to brand colors.
- In dark mode, the highlight automatically brightens to stay visible. The effect is pure CSS. The text is painted with `background-clip: text`, and the highlight sweeps across it in a seamless loop.

## [With Marker](#with-marker)

The shimmer composes with any component that renders text. A common pattern is a [Marker](https://shadcn-svelte.com/docs/components/marker) showing a live status while the assistant is working:

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-4">
  <Marker.Root role="status">
    <Marker.Icon>
      <Spinner />
    </Marker.Icon>
    <Marker.Content class="shimmer">Thinking...</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator" role="status">
    <Marker.Content class="shimmer">Reading 4 files</Marker.Content>
  </Marker.Root>
</div>
```

View Code

```svelte
<Marker.Root role="status">
  <Marker.Icon>
    <Spinner />
  </Marker.Icon>
  <Marker.Content class="shimmer">Thinking&hellip;</Marker.Content>
</Marker.Root>
```

## [Color](#color)

Use `shimmer-color-<color>` to set the highlight color explicitly. It accepts theme colors with an optional opacity modifier, or any arbitrary color value.

```svelte
<div class="flex flex-col items-center gap-2 text-sm text-muted-foreground">
  <p class="shimmer shimmer-color-blue-500/60">Generating response&hellip;</p>
  <p class="shimmer shimmer-color-[#378ADD]">Generating response&hellip;</p>
</div>
```

View Code

```svelte
<p class="shimmer shimmer-color-blue-500/60">Generating response&hellip;</p>
<p class="shimmer shimmer-color-[#378ADD]">Generating response&hellip;</p>
```

## [Duration](#duration)

Use `shimmer-duration-<number>` to set the duration of one sweep in milliseconds. The default is `2000`, i.e. `2s`.

```svelte
<div
  class="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2"
>
  <div class="flex flex-col gap-3">
    <p class="shimmer">Generating response&hellip;</p>
    <p class="font-mono text-xs">shimmer</p>
  </div>
  <div class="flex flex-col gap-3">
    <p class="shimmer shimmer-duration-1000">Generating response&hellip;</p>
    <p class="font-mono text-xs">shimmer-duration-1000</p>
  </div>
</div>
```

View Code

```svelte
<p class="shimmer shimmer-duration-1000">Generating response&hellip;</p>
```

## [Spread](#spread)

Use `shimmer-spread-<number>` to set the width of the highlight band using the spacing scale. The default is `calc(3ch + 40px)`: a fixed base plus a `3ch` term that scales with the font size.

```svelte
<div
  class="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2"
>
  <div class="flex flex-col gap-3">
    <p class="shimmer shimmer-spread-4">Generating response&hellip;</p>
    <p class="font-mono text-xs">shimmer-spread-4</p>
  </div>
  <div class="flex flex-col gap-3">
    <p class="shimmer shimmer-spread-24">Generating response&hellip;</p>
    <p class="font-mono text-xs">shimmer-spread-24</p>
  </div>
</div>
```

View Code

```svelte
<p class="shimmer shimmer-spread-24">Generating response&hellip;</p>
```

For one-off values, use an arbitrary length or percentage:

```svelte
<p class="shimmer shimmer-spread-[5rem]">Generating response&hellip;</p>
```

## [Angle](#angle)

Use `shimmer-angle-<number>` to set the tilt of the highlight band in degrees. The default is `20`.

```svelte
<div
  class="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2"
>
  <div class="flex flex-col gap-3">
    <p class="shimmer">Generating response&hellip;</p>
    <p class="font-mono text-xs">shimmer</p>
  </div>
  <div class="flex flex-col gap-3">
    <p class="shimmer shimmer-angle-45">Generating response&hellip;</p>
    <p class="font-mono text-xs">shimmer-angle-45</p>
  </div>
</div>
```

View Code

```svelte
<p class="shimmer shimmer-angle-45">Generating response&hellip;</p>
```

## [Reverse](#reverse)

Use `shimmer-reverse` to sweep the highlight in the opposite direction. In RTL layouts the sweep already follows the reading direction. See [RTL](#rtl).

```svelte
<p class="shimmer shimmer-reverse">Generating response&hellip;</p>
```

## [Play Once](#play-once)

Use `shimmer-once` to play a single sweep instead of looping, useful as a reveal when streaming completes. Pair it with `shimmer-duration-<number>` to control how long the sweep takes.

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  let replay = $state(0);
</script>
<div class="flex flex-col items-center gap-4">
  {#key replay}
    <p
      class="shimmer text-sm text-muted-foreground shimmer-duration-1100 shimmer-once"
    >
      Generating response&hellip;
    </p>
  {/key}
  <Button variant="outline" size="sm" onclick={() => (replay += 1)}
    >Replay</Button
  >
</div>
```

View Code

```svelte
<p class="shimmer shimmer-duration-1100 shimmer-once">Response generated.</p>
```

## [Disabling the Shimmer](#disabling-the-shimmer)

Use `shimmer-none` to turn the effect off and render the text normally. It works in any class order, so the typical use is responsive or stateful:

```svelte
<div class="flex flex-col items-center gap-3 text-sm text-muted-foreground">
  <p class="shimmer md:shimmer-none">Generating response&hellip;</p>
  <p class="font-mono text-xs">shimmer md:shimmer-none</p>
</div>
```

View Code

```svelte
<p class="shimmer md:shimmer-none">Generating response&hellip;</p>
```

## [Fallback](#fallback)

The shimmer is built on modern color features, [relative color syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_colors/Relative_colors) and `color-mix()`, which are available in all current browsers. In older browsers without support, the highlight gradient is dropped and the text can render transparent. If you target older browsers, apply `shimmer` conditionally with a `supports-*` variant:

```svelte
<p class="supports-[color:oklch(from_white_l_c_h)]:shimmer">
  Generating response&hellip;
</p>
```

## [Reduced Motion](#reduced-motion)

When the user prefers reduced motion, the animation is disabled automatically and the text renders normally. There is nothing to configure.

## [RTL](#rtl)

The sweep follows the reading direction, left to right in LTR and right to left in RTL, with no extra classes. Use `shimmer-reverse` to flip the direction manually.

```svelte
<div
  class="mx-auto grid w-full max-w-lg gap-6 text-center text-sm text-muted-foreground sm:grid-cols-2"
>
  <div class="flex flex-col gap-3">
    <p dir="ltr" class="shimmer">Generating response&hellip;</p>
    <p class="font-mono text-xs">dir="ltr"</p>
  </div>
  <div class="flex flex-col gap-3">
    <p dir="rtl" class="shimmer">  &hellip;</p>
    <p class="font-mono text-xs">dir="rtl"</p>
  </div>
</div>
```

View Code