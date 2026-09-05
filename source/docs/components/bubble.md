# Bubble

Displays conversational content in a message bubble. Supports variants, alignment, grouping, reactions, and collapsible content.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Bubble.Root align="end">
    <Bubble.Content>Hey there! what's up?</Bubble.Content>
  </Bubble.Root>
  <Bubble.Group>
    <Bubble.Root variant="muted">
      <Bubble.Content>Hey! Want to see chat bubbles?</Bubble.Content>
    </Bubble.Root>
    <Bubble.Root variant="muted">
      <Bubble.Content>
        I can group messages, switch sides, and keep the whole thread easy to
        scan.
      </Bubble.Content>
      <Bubble.Reactions role="img" aria-label="Reaction: thumbs up">
        <span></span>
      </Bubble.Reactions>
    </Bubble.Root>
  </Bubble.Group>
  <Bubble.Root align="end">
    <Bubble.Content>Sure. Hit me with your best demo.</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="muted">
    <Bubble.Content>
      Yes. You are reading a demo that is demoing itself. Very meta. Very
      on-brand.
    </Bubble.Content>
    <Bubble.Reactions
      role="img"
      aria-label="Reactions: thumbs up, fire, eyes, and 2 more"
    >
      <span></span>
      <span></span>
      <span></span>
      <span>+2</span>
    </Bubble.Reactions>
  </Bubble.Root>
</div>
```

View Code

The `Bubble` component displays framed conversational content. Use it for chat text, short structured output, quoted replies, suggestions, and reactions.

For full-featured chat interfaces, use the [`Message`](https://shadcn-svelte.com/docs/components/message) component. `Bubble` is intentionally scoped to the bubble surface. Place avatars, names, timestamps, metadata, and message-level actions in [`Message`](https://shadcn-svelte.com/docs/components/message).

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add bubble
```

```bash
npx shadcn-svelte@latest add bubble
```

```bash
bun x shadcn-svelte@latest add bubble
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
```

```svelte
<Bubble.Root>
  <Bubble.Content>
    I checked the registry output and removed the stale route.
  </Bubble.Content>
  <Bubble.Reactions>
    <span></span>
  </Bubble.Reactions>
</Bubble.Root>
```

## [Composition](#composition)

Use the following composition to build a bubble:

```text
Bubble.Root
 Bubble.Content
 Bubble.Reactions
```

Use `Bubble.Group` to group consecutive bubbles from the same sender:

```text
Bubble.Group
 Bubble.Root
    Bubble.Content
 Bubble.Root
     Bubble.Content
```

## [Features](#features)

- Seven visual variants, from a strong primary bubble to unframed ghost content  
- Start and end alignment for sender and receiver bubbles  
- Reactions that anchor to the bubble edge with configurable side and alignment  
- Bubbles size to their content, up to 80% of the container width  
- Polymorphic content via the `child` snippet for link and button bubbles
- Customizable styling through the `class` prop on every part

## [Variants](#variants)

Use `variant` to change the visual treatment of the bubble.

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-12 py-12">
  <Bubble.Root>
    <Bubble.Content>This is the default primary bubble.</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="secondary" align="end">
    <Bubble.Content>This is the secondary variant.</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="muted">
    <Bubble.Content>
      This one is muted. It uses a lower emphasis color for the chat bubble.
    </Bubble.Content>
    <Bubble.Reactions role="img" aria-label="Reaction: thumbs up">
      <span></span>
    </Bubble.Reactions>
  </Bubble.Root>
  <Bubble.Root variant="tinted" align="end">
    <Bubble.Content>
      This one is tinted. The tint is a softer color derived from the primary
      color.
    </Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="outline">
    <Bubble.Content>We can also use an outlined variant.</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="destructive" align="end">
    <Bubble.Content>Or a destructive variant with a reaction.</Bubble.Content>
    <Bubble.Reactions role="img" aria-label="Reaction: fire">
      <span></span>
    </Bubble.Reactions>
  </Bubble.Root>
  <Bubble.Root variant="ghost">
    <Bubble.Content>
      <p>
        Ghost bubbles work for assistant text, <strong>markdown</strong>, and
        other content that should not be framed.
      </p>
      <p class="mt-4">
        This is perfect for assistant messages that should not have a frame and
        can take the full width of the container. You can also render <code
          >code</code
        > in it.
      </p>
      <p class="mt-4">
        Ghost bubbles are full width and can take the full width of the
        container.
      </p>
    </Bubble.Content>
  </Bubble.Root>
</div>
```

View Code

| Variant                      | Description                                                      |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `default`     | A strong primary bubble, usually for the current user.           |
| `secondary`   | The standard neutral bubble for conversation content.            |
| `muted`       | A lower-emphasis bubble for quiet supporting content.            |
| `tinted`      | A subtle primary-tinted bubble.                                  |
| `outline`     | A bordered bubble for secondary or rich content.                 |
| `ghost`       | Unframed content for assistant text or rich content.             |
| `destructive` | A destructive bubble for error or failed actions. |

A bubble sizes to its content, up to 80% of the container width. The `ghost` variant removes the max-width so assistant text and rich content can span the full row.

## [Alignment](#alignment)

Use `align` on `Bubble.Root` to align the bubble to the start or end of the conversation.

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Bubble.Root variant="muted">
    <Bubble.Content>
      This bubble is aligned to the start. This is the default alignment.
    </Bubble.Content>
  </Bubble.Root>
  <Bubble.Root align="end">
    <Bubble.Content
      >This bubble is aligned to the end. Use this for user messages.</Bubble.Content
    >
  </Bubble.Root>
</div>
```

View Code

| align                  | Description                                                     |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `start` | Align the bubble to the start of the conversation.              |
| `end`   | Align the bubble to the end of the conversation. |

**Note:** When building chat interfaces, you probably want to use alignment on the `Message` component itself, not the `Bubble` component.

## [Bubble Group](#bubble-group)

Use `Bubble.Group` to group consecutive bubbles from the same sender. Note the `align` prop should be set on the `Bubble.Root` component itself, not the `Bubble.Group` component.

```text
Bubble.Group
 Bubble.Root
    Bubble.Content
 Bubble.Root
     Bubble.Content
```

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Bubble.Root variant="muted">
    <Bubble.Content>Can you tell me what's the issue?</Bubble.Content>
  </Bubble.Root>
  <Bubble.Group>
    <Bubble.Root align="end">
      <Bubble.Content>You tell me!</Bubble.Content>
    </Bubble.Root>
    <Bubble.Root align="end">
      <Bubble.Content>It worked yesterday. You broke it!</Bubble.Content>
    </Bubble.Root>
    <Bubble.Root align="end">
      <Bubble.Content>Find the bug and fix it.</Bubble.Content>
      <Bubble.Reactions aria-label="Reactions: eyes" align="start">
        <span></span>
      </Bubble.Reactions>
    </Bubble.Root>
  </Bubble.Group>
  <Bubble.Root variant="muted">
    <Bubble.Content>
      Want me to diff yesterday's you against today's you? It's a bit
      embarrassing.
    </Bubble.Content>
  </Bubble.Root>
</div>
```

View Code

## [Links and Buttons](#links-and-buttons)

You can turn a bubble into a link or button by using the `child` snippet on `Bubble.Content`.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Bubble.Root variant="muted">
    <Bubble.Content>How can I help you today?</Bubble.Content>
  </Bubble.Root>
  <Bubble.Group>
    <Bubble.Root variant="tinted" align="end">
      <Bubble.Content>
        {#snippet child({ props })}
          <button
            {...props}
            onclick={() => toast("You clicked forgot password")}
          >
            I forgot my password
          </button>
        {/snippet}
      </Bubble.Content>
    </Bubble.Root>
    <Bubble.Root variant="tinted" align="end">
      <Bubble.Content>
        {#snippet child({ props })}
          <button
            {...props}
            onclick={() => toast("You clicked help with subscription")}
          >
            I need help with my subscription
          </button>
        {/snippet}
      </Bubble.Content>
    </Bubble.Root>
    <Bubble.Root variant="tinted" align="end">
      <Bubble.Content>
        {#snippet child({ props })}
          <button
            {...props}
            onclick={() =>
              toast("You clicked something else. Talk to a human.")}
          >
            Something else. Talk to a human.
          </button>
        {/snippet}
      </Bubble.Content>
    </Bubble.Root>
  </Bubble.Group>
</div>
```

View Code

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
</script>
<Bubble.Root variant="muted">
  <Bubble.Content>
    {#snippet child({ props })}
      <button {...props}>Click here</button>
    {/snippet}
  </Bubble.Content>
</Bubble.Root>
```

## [Reactions](#reactions)

Use `Bubble.Reactions` for bubble reactions. You can use it to display reactions or quick action buttons. Use `side` and `align` to position the row. `side="top"` anchors it to the upper edge. Reactions overlap the bubble edge, so leave vertical space between rows. The examples below use a larger `gap` for this reason.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-12 py-12">
  <Bubble.Root variant="muted" align="end">
    <Bubble.Content>I don't need tests, I know my code works.</Bubble.Content>
    <Bubble.Reactions
      align="start"
      role="img"
      aria-label="Reactions: thumbs up, surprised"
    >
      <span></span>
      <span></span>
    </Bubble.Reactions>
  </Bubble.Root>
  <Bubble.Root variant="muted">
    <Bubble.Content>
      Bold. Fine I'll add some tests. I'll let you know when they're done.
    </Bubble.Content>
    <Bubble.Reactions
      role="img"
      aria-label="Reactions: eyes, rocket, and 2 more"
    >
      <span></span>
      <span></span>
      <span>+2</span>
    </Bubble.Reactions>
  </Bubble.Root>
  <Bubble.Root variant="default" align="end">
    <Bubble.Content
      >Tests passed on the first try. All 142 of them. Looking good!</Bubble.Content
    >
    <Bubble.Reactions
      side="top"
      align="start"
      role="img"
      aria-label="Reactions: party popper, clapping hands"
    >
      <span></span>
      <span></span>
    </Bubble.Reactions>
  </Bubble.Root>
  <Bubble.Root variant="destructive">
    <Bubble.Content>Are you sure I can run this command?</Bubble.Content>
    <Bubble.Reactions>
      <Button
        variant="ghost"
        size="xs"
        onclick={() => toast.success("You clicked yes, running command...")}
      >
        Yes, run it
      </Button>
    </Bubble.Reactions>
  </Bubble.Root>
</div>
```

View Code

## [Show More / Collapsible](#show-more--collapsible)

Long bubble content can be composed with [`Collapsible`](https://shadcn-svelte.com/docs/components/collapsible) to allow for a show more or show less interaction. Use the `Collapsible.Trigger` component to trigger the collapsible content.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Collapsible from "$lib/components/ui/collapsible/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const text = `The accessibility review found two focus states that were visually too subtle in dark mode.
I checked the dialog, menu, and drawer paths because each one renders focusable controls inside a layered surface.
The dialog and drawer are fine. The menu needs the hover and focus tokens split so keyboard focus stays visible when the pointer is not involved.
I also recommend keeping the change in the style file instead of the primitive so the other themes can choose their own focus treatment later.`;
  const previewLength = 180;
  const isLong = text.length > previewLength;
  const preview = `${text.slice(0, previewLength)}...`;
  let open = $state(false);
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Bubble.Root variant="muted">
    <Bubble.Content>How can I help you today?</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="muted" align="end">
    <Bubble.Content class="whitespace-pre-line">
      <Collapsible.Root bind:open>
        <div>{open || !isLong ? text : preview}</div>
        {#if isLong}
          <Collapsible.Trigger>
            {#snippet child({ props })}
              <Button
                variant="link"
                class="gap-1 p-0 text-muted-foreground"
                {...props}
              >
                {open ? "Show less" : "Show more"}
                <ChevronDownIcon
                  data-icon="inline-end"
                  class="group-data-open/button:rotate-180"
                />
              </Button>
            {/snippet}
          </Collapsible.Trigger>
        {/if}
      </Collapsible.Root>
    </Bubble.Content>
  </Bubble.Root>
</div>
```

View Code

## [Tooltip](#tooltip)

Wrap a bubble in a [`Tooltip`](https://shadcn-svelte.com/docs/components/tooltip) to reveal metadata on hover, such as when a message was read.

```svelte
<script lang="ts">
  import CheckIcon from "@lucide/svelte/icons/check";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-4 py-12">
  <Bubble.Root variant="secondary">
    <Bubble.Content>Did you remove the stale route?</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root align="end">
    <Bubble.Content>Yes, removed it from the registry.</Bubble.Content>
    <Bubble.Reactions class="p-0">
      <Tooltip.Root>
        <Tooltip.Trigger>
          {#snippet child({ props })}
            <Button variant="ghost" size="icon-xs" {...props}>
              <CheckIcon />
            </Button>
          {/snippet}
        </Tooltip.Trigger>
        <Tooltip.Content>Read on Jan 5, 2026 at 4:32 PM</Tooltip.Content>
      </Tooltip.Root>
    </Bubble.Reactions>
  </Bubble.Root>
</div>
```

View Code

## [Popover](#popover)

Pair a bubble with a [`Popover`](https://shadcn-svelte.com/docs/components/popover) to surface more information on demand, such as the full error message for a failed action.

```svelte
<script lang="ts">
  import InfoIcon from "@lucide/svelte/icons/info";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-4 py-12">
  <Bubble.Root align="end">
    <Bubble.Content>Run the build script.</Bubble.Content>
  </Bubble.Root>
  <Bubble.Root variant="destructive">
    <Bubble.Content>Failed to run the command.</Bubble.Content>
    <Bubble.Reactions>
      <Popover.Root>
        <Popover.Trigger>
          {#snippet child({ props })}
            <Button
              variant="ghost"
              size="icon-xs"
              aria-label="Show error details"
              class="aria-expanded:text-destructive"
              {...props}
            >
              <InfoIcon />
            </Button>
          {/snippet}
        </Popover.Trigger>
        <Popover.Content>
          <Popover.Header>
            <Popover.Title class="text-sm"
              >Command failed with exit code 1</Popover.Title
            >
            <Popover.Description class="text-sm">
              ENOENT: no such file or directory, open pnpm-lock.yaml
            </Popover.Description>
          </Popover.Header>
        </Popover.Content>
      </Popover.Root>
    </Bubble.Reactions>
  </Bubble.Root>
</div>
```

View Code

## [Accessibility](#accessibility) `Bubble` renders the presentational message surface. Keep conversation-level semantics on the surrounding container and follow the guidelines below.

### [Labeling Reactions](#labeling-reactions)

Reactions render as a row of emoji. A screen reader reads each glyph with no context, and counters like `+8` are announced as "plus eight". Group the row as a single image with a descriptive `aria-label` so it announces once. `role="img"` also hides the individual emoji from assistive tech, so no `aria-hidden` is needed.

```svelte
<Bubble.Reactions
  role="img"
  aria-label="Reactions: thumbs up, fire, and 8 more"
>
  <span></span>
  <span></span>
  <span>+8</span>
</Bubble.Reactions>
```

When reactions are interactive, render buttons instead and give icon-only buttons an `aria-label`.

```svelte
<Bubble.Reactions>
  <Button aria-label="Thumbs up" variant="secondary" size="icon-xs">
    <ThumbsUpIcon />
  </Button>
</Bubble.Reactions>
```

### [Interactive Bubbles](#interactive-bubbles)

When a bubble is clickable, render it as a real `<button>` or `<a>` with the `child` snippet so it is focusable and exposes the correct role. `Bubble.Content` ships a visible focus ring for interactive elements, and the accessible name comes from the bubble text. No extra label is needed.

```svelte
<Bubble.Root variant="muted" align="end">
  <Bubble.Content>
    {#snippet child({ props })}
      <button type="button" {...props} onclick={onReply}>
        I forgot my password
      </button>
    {/snippet}
  </Bubble.Content>
</Bubble.Root>
```

### [Meaning Beyond Color](#meaning-beyond-color)

Bubble variants signal role and tone with color. Pair them with text, alignment, or icons so meaning is not conveyed by color alone. For a `destructive` bubble, keep the error context in the message text rather than relying on the color treatment.

## [API Reference](#api-reference)

### [Bubble](#bubble)

The root bubble wrapper.

| Prop                     | Type                                                                                              | Default            | Description                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `variant` | `"default" \| "secondary" \| "muted" \| "tinted" \| "outline" \| "ghost" \| "destructive"` | `"default"` | The bubble visual treatment.                                    |
| `align`   | `"start" \| "end"`                                                                         | `"start"`   | The inline alignment of the bubble.                             |
| `class`   | `string`                                                                                   | -                  | Additional classes to apply to the root element. | ### [Bubble.Content](#bubblecontent)

The bubble content wrapper.

| Prop                   | Type             | Default | Description                                                        |
| ---------------------------------------------------- | ---------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `child` | `snippet` | -       | Render the content as the child element.                           |
| `class` | `string`  | -       | Additional classes to apply to the content element. | ### [Bubble.Reactions](#bubblereactions)

Displays overlapped reactions for a bubble.

| Prop                   | Type                       | Default           | Description                                                     |
| ---------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `side`  | `"top" \| "bottom"` | `"bottom"` | The side of the bubble to anchor the reactions.                 |
| `align` | `"start" \| "end"`  | `"end"`    | The inline alignment of the reactions.                          |
| `class` | `string`            | -                 | Additional classes to apply to the reaction row. | ### [Bubble.Group](#bubblegroup)

Groups consecutive bubbles from the same sender.

| Prop                   | Type            | Default | Description                                                   |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the group root. |