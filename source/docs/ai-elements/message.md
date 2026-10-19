# Message

One turn. The person's message, and the agent's reply with its actions.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

````svelte
<script lang="ts">
  import CheckIcon from "@lucide/svelte/icons/check";
  import CopyIcon from "@lucide/svelte/icons/copy";
  import PencilIcon from "@lucide/svelte/icons/pencil";
  import RefreshCcwIcon from "@lucide/svelte/icons/refresh-ccw";
  import ThumbsDownIcon from "@lucide/svelte/icons/thumbs-down";
  import ThumbsUpIcon from "@lucide/svelte/icons/thumbs-up";
  import { onDestroy, type Snippet } from "svelte";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import Markdown from "$lib/components/markdown/markdown.svelte";
  import { Button } from "$lib/components/ui/button/index.js";
  const reply = `Install Dialog, then open it from the gear button in `site-header.tsx`.
```bash
npx shadcn@latest add dialog
```
Wrap the button in a `DialogTrigger` and put the settings form in `DialogContent`. Focus moves into the dialog when it opens, and **Esc** closes it.`;
  let copied = $state(false);
  let feedback = $state<"like" | "dislike" | null>(null);
  let timeout: ReturnType<typeof setTimeout> | undefined;
  function copy() {
    void navigator.clipboard.writeText(reply);
    copied = true;
    clearTimeout(timeout);
    timeout = setTimeout(() => (copied = false), 2000);
  }
  onDestroy(() => clearTimeout(timeout));
</script>
{#snippet messageAction(
  label: string,
  icon: Snippet,
  onclick?: () => void,
  pressed?: boolean
)}
  <Tooltip.Root>
    <Tooltip.Trigger>
      {#snippet child({ props })}
        <Button
          {...props}
          variant="ghost"
          size="icon-sm"
          aria-label={label}
          aria-pressed={pressed}
          {onclick}
        >
          {@render icon()}
        </Button>
      {/snippet}
    </Tooltip.Trigger>
    <Tooltip.Content>
      <p>{label}</p>
    </Tooltip.Content>
  </Tooltip.Root>
{/snippet}
{#snippet copyIcon()}
  <CopyIcon />
{/snippet}
{#snippet copyStateIcon()}
  {#if copied}
    <CheckIcon />
  {:else}
    <CopyIcon />
  {/if}
{/snippet}
{#snippet editIcon()}
  <PencilIcon />
{/snippet}
{#snippet likeIcon()}
  <ThumbsUpIcon class={feedback === "like" ? "fill-current" : undefined} />
{/snippet}
{#snippet dislikeIcon()}
  <ThumbsDownIcon class={feedback === "dislike" ? "fill-current" : undefined} />
{/snippet}
{#snippet retryIcon()}
  <RefreshCcwIcon />
{/snippet}
<div class="mx-auto flex w-full max-w-md flex-col gap-8 py-6 text-sm">
  <Message.Root align="end">
    <Message.Content class="gap-2">
      <Bubble.Root align="end" variant="muted">
        <Bubble.Content>
          How do I add a settings dialog? It should open from the gear icon in
          the header.
        </Bubble.Content>
      </Bubble.Root>
      <Message.Footer>
        {@render messageAction("Copy", copyIcon)}
        {@render messageAction("Edit", editIcon)}
      </Message.Footer>
    </Message.Content>
  </Message.Root>
  <Message.Root>
    <Message.Content class="gap-2">
      <Markdown content={reply} />
      <Message.Footer class="px-0">
        {@render messageAction(copied ? "Copied" : "Copy", copyStateIcon, copy)}
        {@render messageAction(
          "Good response",
          likeIcon,
          () => (feedback = feedback === "like" ? null : "like"),
          feedback === "like"
        )}
        {@render messageAction(
          "Bad response",
          dislikeIcon,
          () => (feedback = feedback === "dislike" ? null : "dislike"),
          feedback === "dislike"
        )}
        {@render messageAction("Retry", retryIcon)}
      </Message.Footer>
    </Message.Content>
  </Message.Root>
</div>
````

View Code

Use Message for one turn in a thread. The person's text is a [Bubble](https://shadcn-svelte.com/docs/components/bubble) on a [Message](https://shadcn-svelte.com/docs/components/message) with `align="end"`. The agent's reply is markdown on a Message, with actions under it. A thread of these turns is [Chat](https://shadcn-svelte.com/docs/ai-elements/chat).

## [Installation](#installation)

Message is built with the [Message](https://shadcn-svelte.com/docs/components/message), [Bubble](https://shadcn-svelte.com/docs/components/bubble), and [Tooltip](https://shadcn-svelte.com/docs/components/tooltip) components.

```bash
pnpm dlx shadcn-svelte@latest add message bubble tooltip
```

```bash
npx shadcn-svelte@latest add message bubble tooltip
```

```bash
bun x shadcn-svelte@latest add message bubble tooltip
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import CopyIcon from "@lucide/svelte/icons/copy";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
```

```svelte
<Message.Root align="end">
  <Message.Content>
    <Bubble.Root align="end" variant="muted">
      <Bubble.Content>How do I add a settings dialog?</Bubble.Content>
    </Bubble.Root>
  </Message.Content>
</Message.Root>
<Message.Root>
  <Message.Content class="gap-2">
    <p>Install Dialog, then open it from the gear button.</p>
    <Message.Footer>
      <Button variant="ghost" size="icon-sm" aria-label="Copy">
        <CopyIcon />
      </Button>
    </Message.Footer>
  </Message.Content>
</Message.Root>
```

See [Message](https://shadcn-svelte.com/docs/components/message).

## [Actions](#actions)

Put actions in `Message.Footer`. It follows the message alignment, so on the person's turn the actions sit on the right. Use ghost icon buttons with a tooltip for each.

- **Copy** writes the reply to the clipboard and swaps to a check for two seconds.
- **Good response** and **Bad response**
  are toggles. Set `aria-pressed` so screen readers announce the state.
- **Retry** runs the turn again.
- **Edit** on the person's turn puts the text back in the field.

## [Markdown](#markdown)

The reply streams as markdown. Render it with [svelte-streamdown](https://github.com/beynar/svelte-streamdown) and route fenced code to a [Code Block](https://shadcn-svelte.com/docs/components/code-block#markdown), so code in the reply gets line numbers and a copy button.

## [AI SDK](#ai-sdk)

Branch on the message role. The person's turn is the bubble. The agent's turn is the reply, and `chat.regenerate` with the message id runs it again.

```svelte
<script lang="ts">
  import { Chat } from "@ai-sdk/svelte";
  const chat = new Chat({});
</script>
{#each chat.messages as message (message.id)}
  {#if message.role === "user"}
    <Message.Root align="end">
      <Message.Content>
        <Bubble.Root align="end" variant="muted">
          <Bubble.Content>{getMessageText(message)}</Bubble.Content>
        </Bubble.Root>
      </Message.Content>
    </Message.Root>
  {:else}
    <Message.Root>
      <Message.Content class="gap-2">
        <Streamdown content={getMessageText(message)} />
        <Message.Footer>
          <Button
            variant="ghost"
            size="icon-sm"
            aria-label="Retry"
            onclick={() => chat.regenerate({ messageId: message.id })}
          >
            <RefreshCcwIcon />
          </Button>
        </Message.Footer>
      </Message.Content>
    </Message.Root>
  {/if}
{/each}
```