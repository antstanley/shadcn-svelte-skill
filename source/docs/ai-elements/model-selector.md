# Model Selector

Two menus. One picks the model the agent runs, the other picks how hard it thinks.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import PlusIcon from "@lucide/svelte/icons/plus";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  const providers = [
    {
      name: "OpenAI",
      models: [
        { id: "gpt-5", name: "GPT-5" },
        { id: "gpt-5-mini", name: "GPT-5 mini" }
     ]
    },
    {
      name: "Anthropic",
      models: [
        { id: "claude-sonnet-4-5", name: "Claude Sonnet 4.5" },
        { id: "claude-haiku-4-5", name: "Claude Haiku 4.5" }
     ]
    }
  ];
  const models = providers.flatMap((provider) => provider.models);
  const efforts = [
    { id: "low", name: "Low" },
    { id: "medium", name: "Medium" },
    { id: "high", name: "High" }
 ];
  let text = $state("");
  let model = $state(models[0].id);
  let effort = $state(efforts[1].id);
  let form = $state<HTMLFormElement | null>(null);
  const currentModel = $derived(
    models.find((item) => item.id === model) ?? models[0]
  );
  const currentEffort = $derived(
    efforts.find((item) => item.id === effort) ?? efforts[1]
  );
  const canSend = $derived(text.trim().length > 0);
  function onsubmit(event: SubmitEvent) {
    event.preventDefault();
    if (!canSend) {
      return;
    }
    text = "";
  }
</script>
<div class="mx-auto w-full max-w-lg py-6">
  <form bind:this={form} {onsubmit}>
    <InputGroup.Root>
      <InputGroup.Textarea
        bind:value={text}
        placeholder="Ask the agent to change your code..."
        onkeydown={(event) => {
          if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            form?.requestSubmit();
          }
        }}
        class="p-3"
      />
      <InputGroup.Addon align="block-end">
        <InputGroup.Button
          type="submit"
          size="icon-sm"
          variant="outline"
          class="rounded-full"
          disabled={canSend}
          aria-label="Attach"
        >
          <PlusIcon />
        </InputGroup.Button>
        <DropdownMenu.Root>
          <DropdownMenu.Trigger>
            {#snippet child({ props })}
              <InputGroup.Button
                {...props}
                size="sm"
                variant="outline"
                aria-label="Model: {currentModel.name}"
                class="ml-auto"
              >
                {currentModel.name}
                <ChevronDownIcon />
              </InputGroup.Button>
            {/snippet}
          </DropdownMenu.Trigger>
          <DropdownMenu.Content align="start" class="w-48">
            <DropdownMenu.RadioGroup bind:value={model}>
              {#each providers as provider, index (provider.name)}
                {#if index > 0}
                  <DropdownMenu.Separator />
                {/if}
                <DropdownMenu.Group>
                  <DropdownMenu.Label>{provider.name}</DropdownMenu.Label>
                  {#each provider.models as item (item.id)}
                    <DropdownMenu.RadioItem value={item.id} closeOnSelect>
                      {item.name}
                    </DropdownMenu.RadioItem>
                  {/each}
                </DropdownMenu.Group>
              {/each}
            </DropdownMenu.RadioGroup>
          </DropdownMenu.Content>
        </DropdownMenu.Root>
        <DropdownMenu.Root>
          <DropdownMenu.Trigger>
            {#snippet child({ props })}
              <InputGroup.Button
                {...props}
                size="sm"
                variant="outline"
                aria-label="Effort: {currentEffort.name}"
              >
                <span class="text-muted-foreground">Effort</span>
                {currentEffort.name}
                <ChevronDownIcon />
              </InputGroup.Button>
            {/snippet}
          </DropdownMenu.Trigger>
          <DropdownMenu.Content align="start" class="w-36">
            <DropdownMenu.Group>
              <DropdownMenu.Label>Effort</DropdownMenu.Label>
              <DropdownMenu.RadioGroup bind:value={effort}>
                {#each efforts as item (item.id)}
                  <DropdownMenu.RadioItem value={item.id} closeOnSelect>
                    {item.name}
                  </DropdownMenu.RadioItem>
                {/each}
              </DropdownMenu.RadioGroup>
            </DropdownMenu.Group>
          </DropdownMenu.Content>
        </DropdownMenu.Root>
        <InputGroup.Button
          type="submit"
          size="icon-sm"
          variant="default"
          class="rounded-full"
          disabled={!canSend}
          aria-label="Send"
        >
          <ArrowUpIcon />
        </InputGroup.Button>
      </InputGroup.Addon>
    </InputGroup.Root>
  </form>
</div>
```

View Code

## [Installation](#installation)

Model Selector is built with the [Dropdown Menu](https://shadcn-svelte.com/docs/components/dropdown-menu) and [Input Group](https://shadcn-svelte.com/docs/components/input-group) components.

```bash
pnpm dlx shadcn-svelte@latest add dropdown-menu input-group
```

```bash
npx shadcn-svelte@latest add dropdown-menu input-group
```

```bash
bun x shadcn-svelte@latest add dropdown-menu input-group
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
```

```svelte
<InputGroup.Root>
  <InputGroup.Textarea placeholder="Ask the agent to change your code..." />
  <InputGroup.Addon align="block-end">
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        {#snippet child({ props })}
          <InputGroup.Button {...props} size="sm">
            GPT-5
            <ChevronDownIcon />
          </InputGroup.Button>
        {/snippet}
      </DropdownMenu.Trigger>
      <DropdownMenu.Content align="start">
        <DropdownMenu.RadioGroup bind:value={model}>
          <DropdownMenu.Group>
            <DropdownMenu.Label>OpenAI</DropdownMenu.Label>
            <DropdownMenu.RadioItem value="gpt-5" closeOnSelect>
              GPT-5
            </DropdownMenu.RadioItem>
            <DropdownMenu.RadioItem value="gpt-5-mini" closeOnSelect>
              GPT-5 mini
            </DropdownMenu.RadioItem>
          </DropdownMenu.Group>
        </DropdownMenu.RadioGroup>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        {#snippet child({ props })}
          <InputGroup.Button {...props} size="sm">
            Medium
            <ChevronDownIcon />
          </InputGroup.Button>
        {/snippet}
      </DropdownMenu.Trigger>
      <DropdownMenu.Content align="start">
        <DropdownMenu.RadioGroup bind:value={effort}>
          <DropdownMenu.RadioItem value="low" closeOnSelect>
            Low
          </DropdownMenu.RadioItem>
          <DropdownMenu.RadioItem value="medium" closeOnSelect>
            Medium
          </DropdownMenu.RadioItem>
          <DropdownMenu.RadioItem value="high" closeOnSelect>
            High
          </DropdownMenu.RadioItem>
        </DropdownMenu.RadioGroup>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
    <InputGroup.Button type="submit" variant="default" class="ml-auto">
      <ArrowUpIcon />
    </InputGroup.Button>
  </InputGroup.Addon>
</InputGroup.Root>
```

## [AI SDK](#ai-sdk)

Send the model and the effort with the message. Map them to a model and provider options in the route.

```ts
chat.sendMessage({ text }, { body: { model, effort } });
```

src/routes/api/chat/+server.ts

```ts
import { anthropic } from "@ai-sdk/anthropic";
import { openai } from "@ai-sdk/openai";
import { convertToModelMessages, streamText, type UIMessage } from "ai";
import type { RequestHandler } from "./$types";
const models = {
  "gpt-5": openai("gpt-5"),
  "gpt-5-mini": openai("gpt-5-mini"),
  "claude-sonnet-4-5": anthropic("claude-sonnet-4-5"),
  "claude-haiku-4-5": anthropic("claude-haiku-4-5"),
};
export const POST: RequestHandler = async ({ request }) => {
  const { messages, model, effort } = (await request.json()) as {
    messages: UIMessage[];
    model: keyof typeof models;
    effort: "low" | "medium" | "high";
  };
  const result = streamText({
    model: models[model] ?? models["gpt-5"],
    messages: await convertToModelMessages(messages),
    providerOptions: {
      openai: { reasoningEffort: effort },
      anthropic: { effort },
    },
  });
  return result.toUIMessageStreamResponse();
};
```

Each provider reads its own key in `providerOptions` and ignores the rest.