# Marker

Displays an inline status, system note, bordered row, or labeled separator in a conversation.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import GitBranchIcon from "@lucide/svelte/icons/git-branch";
  import SearchIcon from "@lucide/svelte/icons/search";
  import * as Marker from "$lib/components/ui/marker/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Marker.Root>
    <Marker.Icon>
      <GitBranchIcon />
    </Marker.Icon>
    <Marker.Content>Switched to a new branch</Marker.Content>
  </Marker.Root>
  <Marker.Root role="status">
    <Marker.Icon>
      <Spinner />
    </Marker.Icon>
    <Marker.Content class="shimmer">Thinking...</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator">
    <Marker.Content>Conversation compacted</Marker.Content>
  </Marker.Root>
  <Marker.Root>
    <Marker.Icon>
      <SearchIcon />
    </Marker.Icon>
    <Marker.Content>Explored 4 files</Marker.Content>
  </Marker.Root>
</div>
```

View Code

The `Marker` component displays inline conversation markers such as status updates, system notes, bordered rows, and labeled separators. Compose it with [`Message`](https://shadcn-svelte.com/docs/components/message) in a conversation thread.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add marker
```

```bash
npx shadcn-svelte@latest add marker
```

```bash
bun x shadcn-svelte@latest add marker
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
```

```svelte
<Marker.Root>
  <Marker.Icon>
    <CheckIcon />
  </Marker.Icon>
  <Marker.Content>Explored 4 files</Marker.Content>
</Marker.Root>
```

## [Composition](#composition)

Use the following composition to build a marker:

```text
Marker.Root
 Marker.Icon
 Marker.Content
```

## [Features](#features)

- Inline marker, bordered row, and labeled separator variants  
- Decorative icon slot that is hidden from assistive tech  
- Polymorphic root via the `child` snippet for link and button markers
- Pairs with the [`shimmer`](https://shadcn-svelte.com/docs/utils/shimmer)
  utility for streaming status text
- Customizable styling through the `class` prop on every part

## [Variants](#variants)

Use `variant` to switch between an inline marker, bordered row, and labeled separator.

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Marker.Root>
    <Marker.Content>A default marker for inline notes.</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator">
    <Marker.Content>A separator marker</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="border">
    <Marker.Content>A border marker for row boundaries.</Marker.Content>
  </Marker.Root>
</div>
```

View Code

| Variant                    | Description                                                      |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `default`   | An inline marker for status, notes, and actions.                 |
| `border`    | A default marker with a bottom border under the row.             |
| `separator` | A centered label with divider lines on each side. |

## [Status](#status)

Set `role="status"` and include a [`Spinner`](https://shadcn-svelte.com/docs/components/spinner) for streaming or in-progress markers so updates are announced.

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Marker.Root role="status">
    <Marker.Icon>
      <Spinner />
    </Marker.Icon>
    <Marker.Content>Compacting conversation</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator" role="status">
    <Marker.Icon>
      <Spinner />
    </Marker.Icon>
    <Marker.Content>Running tests</Marker.Content>
  </Marker.Root>
</div>
```

View Code

## [Shimmer](#shimmer)

Add the [`shimmer`](https://shadcn-svelte.com/docs/utils/shimmer) utility class to `Marker.Content` for an animated streaming-text effect. The utility ships with the `shadcn-svelte` package. See the shimmer docs for installation.

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Marker.Root role="status">
    <Marker.Content class="shimmer">Thinking...</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator" role="status">
    <Marker.Content class="shimmer">Reading 4 files</Marker.Content>
  </Marker.Root>
</div>
```

View Code

## [Separator](#separator)

Use the `separator` variant for labeled dividers, such as dates or section breaks, in a conversation.

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Marker.Root variant="separator">
    <Marker.Content>Today</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator">
    <Marker.Content>Worked for 42s</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator">
    <Marker.Content>Conversation compacted</Marker.Content>
  </Marker.Root>
</div>
```

View Code

## [Border](#border)

Use the `border` variant for status rows that should keep the default marker alignment while separating the next row.

```svelte
<script lang="ts">
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import GitBranchIcon from "@lucide/svelte/icons/git-branch";
  import SearchIcon from "@lucide/svelte/icons/search";
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-3 py-12">
  <Marker.Root variant="border">
    <Marker.Icon>
      <GitBranchIcon />
    </Marker.Icon>
    <Marker.Content>Switched to release-candidate</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="border">
    <Marker.Icon>
      <SearchIcon />
    </Marker.Icon>
    <Marker.Content>Reviewed 8 related files</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="border">
    <Marker.Icon>
      <FileTextIcon />
    </Marker.Icon>
    <Marker.Content>Opened implementation notes</Marker.Content>
  </Marker.Root>
</div>
```

View Code

## [With Icon](#with-icon)

Use `Marker.Icon` to render an icon alongside the content. Use `flex-col` to stack the icon above the content.

```svelte
<script lang="ts">
  import BookOpenCheckIcon from "@lucide/svelte/icons/book-open-check";
  import GitBranchIcon from "@lucide/svelte/icons/git-branch";
  import SearchIcon from "@lucide/svelte/icons/search";
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-12 py-12">
  <Marker.Root>
    <Marker.Icon>
      <GitBranchIcon />
    </Marker.Icon>
    <Marker.Content>Switched to a new branch</Marker.Content>
  </Marker.Root>
  <Marker.Root variant="separator">
    <Marker.Icon>
      <SearchIcon />
    </Marker.Icon>
    <Marker.Content>Explored 4 files</Marker.Content>
  </Marker.Root>
  <Marker.Root class="flex-col">
    <Marker.Icon>
      <BookOpenCheckIcon />
    </Marker.Icon>
    <Marker.Content>Syncing completed</Marker.Content>
  </Marker.Root>
</div>
```

View Code

## [Links and Buttons](#links-and-buttons)

Turn a marker into a link or button with the `child` snippet on `Marker.Root`.

```svelte
<script lang="ts">
  import GitBranchIcon from "@lucide/svelte/icons/git-branch";
  import RotateCcwIcon from "@lucide/svelte/icons/rotate-ccw";
  import { toast } from "svelte-sonner";
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Marker.Root>
    {#snippet child({ props })}
      <a href="#links-and-buttons" {...props}>
        <Marker.Icon>
          <GitBranchIcon />
        </Marker.Icon>
        <Marker.Content>View the pull request</Marker.Content>
      </a>
    {/snippet}
  </Marker.Root>
  <Marker.Root class="transition-colors hover:text-foreground">
    {#snippet child({ props })}
      <button
        {...props}
        type="button"
        onclick={() => toast("You clicked the revert button")}
      >
        <Marker.Icon>
          <RotateCcwIcon />
        </Marker.Icon>
        <Marker.Content>Revert this change</Marker.Content>
      </button>
    {/snippet}
  </Marker.Root>
</div>
```

View Code

```svelte
<script lang="ts">
  import * as Marker from "$lib/components/ui/marker/index.js";
</script>
<Marker.Root>
  {#snippet child({ props })}
    <a href="#/" {...props}>
      <Marker.Content>View the pull request</Marker.Content>
    </a>
  {/snippet}
</Marker.Root>
```

## [Accessibility](#accessibility) `Marker` is presentational by default. The correct semantics depend on how you use it, so choose the role based on intent rather than relying on a single default.

### [Status and Progress](#status-and-progress)

For streaming or progress markers such as "Thinking..." or a running tool, set `role="status"` so assistive tech announces the update as it appears. `Marker` forwards `role` to the underlying element.

```svelte
<Marker.Root role="status">
  <Marker.Icon>
    <Spinner />
  </Marker.Icon>
  <Marker.Content>Compacting conversation</Marker.Content>
</Marker.Root>
```

### [Labeled Separators](#labeled-separators)

A separator that carries text, such as a date or a section label, needs no role. The divider lines are decorative CSS pseudo-elements, and the text is announced as ordinary content.

```svelte
<Marker.Root variant="separator">
  <Marker.Content>Today</Marker.Content>
</Marker.Root>
```

**Note:** Do not add `role="separator"` to a labeled divider. A separator takes its accessible name from `aria-label`, not from its text, and its contents are treated as presentational, so the visible label would not be announced. Reserve `role="separator"` for a divider with no meaningful text.

### [Bordered Markers](#bordered-markers)

A bordered marker keeps the same semantics as the default marker. The bottom border is decorative, so choose `role="status"`, the `child` snippet, or no role based on the marker's purpose.

```svelte
<Marker.Root variant="border">
  <Marker.Icon>
    <FileTextIcon />
  </Marker.Icon>
  <Marker.Content>Opened implementation notes</Marker.Content>
</Marker.Root>
```

### [Decorative Icons](#decorative-icons) `Marker.Icon` is decorative and hidden from assistive tech with `aria-hidden`, so the adjacent `Marker.Content` carries the meaning. For an icon-only marker, provide an `aria-label` or visible text so it is not announced as empty.

```svelte
<Marker.Root aria-label="Synced">
  <Marker.Icon>
    <CheckIcon />
  </Marker.Icon>
</Marker.Root>
```

### [Interactive Markers](#interactive-markers)

When a marker links or triggers an action, render it as a real `<button>` or `<a>` with the `child` snippet so it is focusable and exposes the correct role. The accessible name comes from the marker text.

```svelte
<Marker.Root>
  {#snippet child({ props })}
    <a href="/files" {...props}>
      <Marker.Icon>
        <FileTextIcon />
      </Marker.Icon>
      <Marker.Content>Explored 4 files</Marker.Content>
    </a>
  {/snippet}
</Marker.Root>
```

## [API Reference](#api-reference)

### [Marker](#marker)

The root marker element. The file also exports `markerVariants` for composing the marker styles into custom components.

| Prop                     | Type                                          | Default            | Description                                                     |
| ------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `variant` | `"default" \| "border" \| "separator"` | `"default"` | The marker layout.                                              |
| `child`   | `snippet`                              | -                  | Render as the child element, such as a link.                    |
| `class`   | `string`                               | -                  | Additional classes to apply to the root element. | ### [Marker.Icon](#markericon)

A decorative icon slot. Hidden from assistive tech with `aria-hidden`.

| Prop                   | Type            | Default | Description                                                  |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the icon slot. | ### [Marker.Content](#markercontent)

The marker text content.

| Prop                   | Type            | Default | Description                                                     |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the content slot. |