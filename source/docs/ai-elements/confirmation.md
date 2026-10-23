# Confirmation

Asks for approval before a tool runs.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import LoaderCircleIcon from "@lucide/svelte/icons/loader-circle";
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import { Chat } from "@ai-sdk/svelte";
 import {
  lastAssistantMessageIsCompleteWithApprovalResponses,
  type UIDataTypes,
  type UIMessage,
 } from "ai";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as Item from "$lib/components/ui/item/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 type ChatMessage = UIMessage<
  unknown,
  UIDataTypes,
  {
   runCommand: {
    input: { command: string };
    output: { stdout: string };
   };
  }
 >;
 const script = createChat<ChatMessage>()
  .user("Clean up the build folder.")
  .sleep(600)
  .assistant(({ writer }) => {
   writer.reasoning(
    "The build output lives in dist. Deleting it cannot be undone, so I should ask before I run the command."
   );
   writer.sleep(400);
   writer.tool("runCommand", {
    input: { command: "rm -rf dist" },
    needsApproval: true,
    output: { stdout: "" },
   });
  })
  .assistant(({ writer, toolCall }) => {
   writer.sleep(600);
   writer.text(
    toolCall?.approved ? "Removed the dist folder." : "Okay, I left the dist folder in place."
   );
  });
 const initialMessages = script.get(0);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat<ChatMessage>({
  messages: initialMessages,
  transport,
  sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithApprovalResponses,
 });
 const nextMessage = $derived(script.next(chat.messages));
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 // The reader's choice for each reasoning row. Until they click, it follows `running`.
 let reasoningOpen = $state<Record<string, boolean>>({});
</script>
{#snippet reasoningRow(id: string, text: string, running: boolean)}
 <Trace.Collapsible
  open={reasoningOpen[id] ?? running}
  onOpenChange={(open) => (reasoningOpen[id] = open)}
 >
  <Trace.CollapsibleTrigger>
   <Trace.Line status={running ? "running" : undefined}>
    <Trace.Icon>
     {#if running}
      <LoaderCircleIcon class="animate-spin" />
     {:else}
      <CircleCheckIcon />
     {/if}
    </Trace.Icon>
    <Trace.Title>{running ? "Thinking" : "Thought"}</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent class="whitespace-pre-wrap">{text}</Trace.CollapsibleContent>
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
   <Message.Root>
    <Message.Content class="gap-4">
     {#each message.parts as part, index (index)}
      {#if part.type === "text"}
       <p>{part.text}</p>
      {:else if part.type === "reasoning"}
       <Trace.Root>
        {@render reasoningRow( `${message.id}-${index}`,
         part.text,
         part.state === "streaming"
        )}
       </Trace.Root>
      {:else if part.type === "tool-runCommand"}
       {#if part.state === "approval-requested"}
        {@const approvalId = part.approval.id}
        <Item.Root variant="outline" size="sm">
         <Item.Media variant="icon">
          <TerminalIcon />
         </Item.Media>
         <Item.Content>
          <Item.Title>Run {part.input.command}?</Item.Title>
          <Item.Description>The command runs in this project.</Item.Description>
         </Item.Content>
         <Item.Actions>
          <Button
           size="sm"
           variant="outline"
           onclick={() =>
            chat.addToolApprovalResponse({ id: approvalId, approved: false })}
          >
           Deny
          </Button>
          <Button
           size="sm"
           onclick={() =>
            chat.addToolApprovalResponse({ id: approvalId, approved: true })}
          >
           Approve
          </Button>
         </Item.Actions>
        </Item.Root>
       {:else}
        {@const denied =
         part.state === "output-denied" ||
         (part.state === "approval-responded" && !part.approval.approved)}
        <Trace.Root>
         <Trace.Line
          status={!denied && part.state !== "output-available" ? "running" : undefined}
         >
          <Trace.Icon>
           <TerminalIcon />
          </Trace.Icon>
          <Trace.Title>
           {denied ? "Denied" : part.state === "output-available" ? "Ran" : "Running"}
           {part.input?.command}
          </Trace.Title>
         </Trace.Line>
        </Trace.Root>
       {/if}
      {/if}
     {/each}
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
    if (nextMessage) {
     void chat.sendMessage(nextMessage);
    } else {
     reasoningOpen = {};
     chat.messages = initialMessages;
    }
   }}
  >
   {nextMessage ? "Send message" : "Reset"}
  </Button>
 {/if}
</div>
```

View Code

Confirmation asks the person for a yes or no before a tool runs. The question is an [Item](https://shadcn-svelte.com/docs/components/item) with Deny and Approve buttons. Once the person answers, the call becomes a [Tool](https://shadcn-svelte.com/docs/ai-elements/tool) line.

## [Installation](#installation)

Confirmation is built with the [Item](https://shadcn-svelte.com/docs/components/item) and [Button](https://shadcn-svelte.com/docs/components/button) components.

```bash
pnpm dlx shadcn-svelte@latest add item button
```

```bash
npx shadcn-svelte@latest add item button
```

```bash
bun x shadcn-svelte@latest add item button
```

## [Usage](#usage)

```svelte
<Item.Root variant="outline" size="sm">
  <Item.Media variant="icon">
    <TerminalIcon />
  </Item.Media>
  <Item.Content>
    <Item.Title>Run {part.input.command}?</Item.Title>
    <Item.Description>The command runs in this project.</Item.Description>
  </Item.Content>
  <Item.Actions>
    <Button size="sm" variant="outline" onclick={deny}>Deny</Button>
    <Button size="sm" onclick={approve}>Approve</Button>
  </Item.Actions>
</Item.Root>
```

## [AI SDK](#ai-sdk)

While the part is `approval-requested`, answer with the approval id. Pass `sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithApprovalResponses` so the chat continues once every approval has an answer.

```ts
chat.addToolApprovalResponse({
  id: part.approval.id,
  approved: true,
});
```

```ts
const chat = new Chat({
  sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithApprovalResponses,
});
```

Approve streams the tool output. Deny streams `output-denied`. Either way, the part becomes a Tool line.

See [Tool](https://shadcn-svelte.com/docs/ai-elements/tool#approval).

## [AI SDK Helper](#ai-sdk-helper)

To script an approval with [`createChat`](https://ui.shadcn.com/docs/helpers/ai-sdk), set `needsApproval` on the tool. The `output` streams after approval, and the next agent turn reads `toolCall.approved`.

```ts
const chat = createChat()
  .user("Clean up the build folder.")
  .assistant(({ writer }) => {
    writer.tool("runCommand", {
      input: { command: "rm -rf dist" },
      needsApproval: true,
      output: { stdout: "" },
    });
  })
  .assistant(({ writer, toolCall }) => {
    writer.text(
      toolCall?.approved
        ? "Removed the dist folder."
        : "Okay, I left the dist folder in place."
    );
  });
```