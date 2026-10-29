# Plan

Displays the steps the agent plans to take, and how far it has got.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import CircleIcon from "@lucide/svelte/icons/circle";
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import CircleDotIcon from "@lucide/svelte/icons/circle-dot";
 import RouteIcon from "@lucide/svelte/icons/route";
 import { Chat } from "@ai-sdk/svelte";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import type { UIMessage } from "ai";
 type ChatMessage = UIMessage<
  unknown,
  {
   plan: {
    title: string;
    steps: { title: string; status: "done" | "running" | "pending" }[];
   };
  }
 >;
 type PlanPart = Extract<ChatMessage["parts"][number], { type: "data-plan" }>;
 const STEPS = [
  "Install @base-ui/react",
  "Replace the Radix imports",
  "Rename asChild to render",
  "Run the type checker",
];
 function planAt(current: number) {
  return {
   title: "Plan: migrate to Base UI",
   steps: STEPS.map((title, index) => ({
    title,
    status: index < current ? "done" : index === current ? "running" : "pending",
   })),
  } satisfies PlanPart["data"];
 }
 const script = createChat<ChatMessage>()
  .user("Migrate the dialog components to Base UI.")
  .assistant(({ writer }) => {
   STEPS.forEach((_, index) => {
    writer.data({ type: "data-plan", id: "plan", data: planAt(index) }).sleep(1200);
   });
   writer.data({ type: "data-plan", id: "plan", data: planAt(STEPS.length) });
   writer.text("Migrated Dialog and AlertDialog. The type checker passes.");
  });
 const transcript = script.get();
 const [question] = script.get(1);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat<ChatMessage>({ messages: transcript, transport });
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
</script>
{#snippet planRow(plan: PlanPart["data"], streaming: boolean)}
 {@const done = plan.steps.filter((step) => step.status === "done").length}
 {@const running = streaming && done < plan.steps.length}
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line status={running ? "running" : undefined}>
    <Trace.Icon>
     <RouteIcon />
    </Trace.Icon>
    <Trace.Title>{plan.title}</Trace.Title>
    <Trace.Description>
     {done} of {plan.steps.length} done
    </Trace.Description>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <Trace.Root>
    {#each plan.steps as step, index (index)}
     <Trace.Line
      status={step.status === "pending"
       ? "pending"
       : streaming && step.status === "running"
        ? "running"
        : undefined}
     >
      <Trace.Icon>
       {#if step.status === "done"}
        <CircleCheckIcon />
       {:else if step.status === "running"}
        <CircleDotIcon />
       {:else}
        <CircleIcon />
       {/if}
      </Trace.Icon>
      <Trace.Title>{step.title}</Trace.Title>
     </Trace.Line>
    {/each}
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
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
   {@const streaming = busy && message === chat.messages.at(-1)}
   {@const plan = message.parts.find((part) => part.type === "data-plan")}
   {@const text = getMessageText(message)}
   <Message.Root>
    <Message.Content class="gap-4">
     {#if plan}
      <Trace.Root>
       {@render planRow(plan.data, streaming)}
      </Trace.Root>
     {/if}
     {#if text}
      <p>{text}</p>
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

Plan is the list of steps the agent decides on before it starts, such as the steps of a migration. Each step is done, running or pending, and the title counts how many are done.

Plan is built with `Trace` with a `Trace.Collapsible` for the plan.

When the steps are not known up front, use [Task](https://shadcn-svelte.com/docs/ai-elements/task#task-or-plan) instead.

## [Installation](#installation)

Plan is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) component.

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
  <Trace.Collapsible open>
    <Trace.CollapsibleTrigger>
      <Trace.Line status="running">
        <Trace.Icon>
          <RouteIcon />
        </Trace.Icon>
        <Trace.Title>Plan: migrate to Base UI</Trace.Title>
        <Trace.Description>2 of 5 done</Trace.Description>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        <Trace.Line>
          <Trace.Icon>
            <CircleCheckIcon />
          </Trace.Icon>
          <Trace.Title>Replace the Radix imports</Trace.Title>
        </Trace.Line>
        <Trace.Line status="running">
          <Trace.Icon>
            <CircleDotIcon />
          </Trace.Icon>
          <Trace.Title>Rename asChild to render</Trace.Title>
        </Trace.Line>
        <Trace.Line status="pending">
          <Trace.Icon>
            <CircleIcon />
          </Trace.Icon>
          <Trace.Title>Run the type checker</Trace.Title>
        </Trace.Line>
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Details](#details)

Put a description above the steps, inside `Trace.CollapsibleContent`.

```svelte
<script lang="ts">
 import CircleIcon from "@lucide/svelte/icons/circle";
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import RouteIcon from "@lucide/svelte/icons/route";
 import * as Trace from "$lib/components/ui/trace/index.js";
 const steps = [
  "Add a dark variant to the theme tokens",
  "Read the theme from a cookie on the server",
  "Add a toggle to the settings page",
  "Check contrast on the charts",
];
</script>
<Trace.Root class="max-w-sm">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <RouteIcon />
    </Trace.Icon>
    <Trace.Title>Plan: add dark mode</Trace.Title>
    <Trace.Description>1 of {steps.length} done</Trace.Description>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent class="flex flex-col gap-3">
   <p>
    Store the theme in a cookie so the server renders the right one and the page does not flash
    on load.
   </p>
   <Trace.Root>
    {#each steps as step, index (index)}
     <Trace.Line status={index > 0 ? "pending" : undefined}>
      <Trace.Icon>
       {#if index === 0}
        <CircleCheckIcon />
       {:else}
        <CircleIcon />
       {/if}
      </Trace.Icon>
      <Trace.Title>{step}</Trace.Title>
     </Trace.Line>
    {/each}
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</Trace.Root>
```

View Code

## [AI SDK](#ai-sdk)

Stream the plan as a data part with a fixed `id`. The AI SDK replaces a data part with the same `id`, so it updates in place.

src/routes/api/chat/+server.ts

```ts
const stream = createUIMessageStream({
  execute: async ({ writer }) => {
    writer.write({ type: "data-plan", id: "plan", data: { title, steps } });
  },
});
```

```svelte
{@const plan = message.parts.find((part) => part.type === "data-plan")}
```

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).