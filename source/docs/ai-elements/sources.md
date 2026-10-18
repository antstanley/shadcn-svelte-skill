# Sources

Displays the links the agent used for a reply.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
  import GlobeIcon from "@lucide/svelte/icons/globe";
  import { Chat } from "@ai-sdk/svelte";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { UIMessage } from "ai";
  const script = createChat()
    .user("How do I start an Astro project with pnpm?")
    .assistant(({ writer }) => {
      writer.text(
        "Run pnpm create astro@latest and follow the prompts. It scaffolds the project and installs the dependencies."
      );
      writer.sourceUrl({
        url: "https://docs.astro.build/en/install-and-setup/",
        title: "Install Astro | docs.astro.build"
      });
      writer.sourceUrl({
        url: "https://www.npmjs.com/package/create-astro",
        title: "create-astro | npmjs.com"
      });
      writer.sourceUrl({
        url: "https://docs.astro.build/en/install-and-setup/",
        title: "Install Astro | docs.astro.build"
      });
      writer.sourceUrl({
        url: "https://pnpm.io/cli/create",
        title: "pnpm create | pnpm.io"
      });
    });
  const transcript = script.get();
  const [question] = script.get(1);
  const transport = script.transport({ delayMs: 20 });
  type SourcePart = Extract<UIMessage["parts"][number], { type: "source-url" }>;
  const chat = new Chat({ messages: transcript, transport });
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
</script>
{#snippet sourcesLine(sources: SourcePart[])}
  <Trace.Root>
    <Trace.Collapsible open>
      <Trace.CollapsibleTrigger>
        <Trace.Line>
          <Trace.Icon>
            <GlobeIcon />
          </Trace.Icon>
          <Trace.Title>Used {sources.length} sources</Trace.Title>
        </Trace.Line>
      </Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>
        <Trace.Root>
          {#each sources as source (source.sourceId)}
            <a href={source.url} target="_blank" rel="noreferrer">
              <Trace.Line>
                <Trace.Title>
                  {source.title ?? new URL(source.url).hostname}
                  <span class="sr-only"> (opens in a new tab)</span>
                </Trace.Title>
                <Trace.Icon>
                  <ArrowUpRightIcon />
                </Trace.Icon>
              </Trace.Line>
            </a>
          {/each}
        </Trace.Root>
      </Trace.CollapsibleContent>
    </Trace.Collapsible>
  </Trace.Root>
{/snippet}
<div class="flex min-h-72 w-full max-w-sm flex-col gap-4 py-6 text-sm">
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
      {@const sources = message.parts
        .filter((part) => part.type === "source-url")
        .filter(
          (part, index, all) =>
            all.findIndex((other) => other.url === part.url) === index
        )}
      {@const text = getMessageText(message)}
      <Message.Root>
        <Message.Content class="gap-4">
          {#if text}
            <p>{text}</p>
          {/if}
          {#if sources.length > 0}
            {@render sourcesLine(sources)}
          {/if}
        </Message.Content>
      </Message.Root>
    {/if}
  {/each}
  {#if !busy}
    <Button
      variant="outline"
      size="sm"
      class="mt-auto self-start"
      onclick={() => {
        chat.messages = [];
        void chat.sendMessage(question);
      }}
    >
      Replay
    </Button>
  {/if}
</div>
```

View Code

Sources is a line that lists the links the agent used for a reply. It says how many there are, like "Used 3 sources", and opens into a link for each one.

Sources is built with `Trace` with a `Trace.Collapsible` for the list.

## [Installation](#installation)

Sources is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) component.

```bash
pnpm dlx shadcn-svelte@latest add trace
```

```bash
npx shadcn-svelte@latest add trace
```

```bash
bun x shadcn-svelte@latest add trace
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Trace from "$lib/components/ui/trace/index.js";
</script>
```

```svelte
<Trace.Root>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <GlobeIcon />
        </Trace.Icon>
        <Trace.Title>Used {sources.length} sources</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        {#each sources as source (source.sourceId)}
          <a href={source.url} target="_blank" rel="noreferrer">
            <Trace.Line>
              <Trace.Icon>
                <GlobeIcon />
              </Trace.Icon>
              <Trace.Title>
                {source.title ?? new URL(source.url).hostname}
                <span class="sr-only"> (opens in a new tab)</span>
              </Trace.Title>
              <Trace.Icon>
                <ArrowUpRightIcon />
              </Trace.Icon>
            </Trace.Line>
          </a>
        {/each}
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [AI SDK](#ai-sdk)

Collect the `source-url` parts of a message and render them after the text. The agent can cite the same page more than once, so dedupe them by `url`.

```ts
const sources = $derived(
  message.parts
    .filter((part) => part.type === "source-url")
    .filter(
      (part, index, all) =>
        all.findIndex((other) => other.url === part.url) === index
    )
);
``` `title` is optional on a `source-url` part. Fall back to the hostname of the URL.

## [Accessibility](#accessibility)

Each source is a plain link inside the list.

- Links open in a new tab. Add `sr-only` text, like "(opens in a new tab)", so screen readers announce it.
- The arrow icon is decorative. The title is the name of the link.  
- The count in the trigger, like "Used 3 sources", tells the person what opens before they open it. ## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).