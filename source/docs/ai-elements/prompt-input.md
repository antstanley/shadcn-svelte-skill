# Prompt Input

A message field with attachments and a send button.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
 import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
 import FileTextIcon from "@lucide/svelte/icons/file-text";
 import PlusIcon from "@lucide/svelte/icons/plus";
 import XIcon from "@lucide/svelte/icons/x";
 import * as Attachment from "$lib/components/ui/attachment/index.js";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
 type AttachmentFile = {
  id: string;
  name: string;
 };
 const providers = [
  {
   name: "OpenAI",
   models: [
    { id: "gpt-5", name: "GPT-5" },
    { id: "gpt-5-mini", name: "GPT-5 mini" },
  ],
  },
  {
   name: "Anthropic",
   models: [
    { id: "claude-sonnet-4-5", name: "Claude Sonnet 4.5" },
    { id: "claude-haiku-4-5", name: "Claude Haiku 4.5" },
  ],
  },
 ];
 const models = providers.flatMap((provider) => provider.models);
 const efforts = [
  { id: "low", name: "Low" },
  { id: "medium", name: "Medium" },
  { id: "high", name: "High" },
];
 let text = $state("");
 let files = $state<AttachmentFile[]>([]);
 let model = $state(models[0].id);
 let effort = $state(efforts[1].id);
 let form = $state<HTMLFormElement | null>(null);
 let input = $state<HTMLInputElement | null>(null);
 const currentModel = $derived(models.find((item) => item.id === model) ?? models[0]);
 const currentEffort = $derived(efforts.find((item) => item.id === effort) ?? efforts[1]);
 const canSend = $derived(text.trim().length > 0);
 function onSubmit(event: SubmitEvent) {
  event.preventDefault();
  if (!canSend) {
   return;
  }
  text = "";
  files = [];
 }
 function onAttach(event: Event & { currentTarget: HTMLInputElement }) {
  const selected = event.currentTarget.files;
  if (!selected) {
   return;
  }
  files = [
   ...files,
   ...Array.from(selected, (file) => ({
    id: crypto.randomUUID(),
    name: file.name,
   })),
 ];
  event.currentTarget.value = "";
 }
</script>
<div class="mx-auto w-full max-w-lg py-6">
 <form bind:this={form} onsubmit={onSubmit}>
  <input
   bind:this={input}
   type="file"
   multiple
   class="sr-only"
   tabindex={-1}
   onchange={onAttach}
  />
  <InputGroup.Root>
   {#if files.length > 0}
    <InputGroup.Addon align="block-start" class="flex-wrap">
     {#each files as file (file.id)}
      <Attachment.Root size="sm">
       <Attachment.Media>
        <FileTextIcon />
       </Attachment.Media>
       <Attachment.Content>
        <Attachment.Title>{file.name}</Attachment.Title>
       </Attachment.Content>
       <Attachment.Actions>
        <Attachment.Action
         aria-label={`Remove ${file.name}`}
         onclick={() => (files = files.filter((item) => item.id !== file.id))}
        >
         <XIcon />
        </Attachment.Action>
       </Attachment.Actions>
      </Attachment.Root>
     {/each}
    </InputGroup.Addon>
   {/if}
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
     size="icon-sm"
     variant="outline"
     class="rounded-full"
     aria-label="Attach files"
     onclick={() => input?.click()}
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
        aria-label={`Model: ${currentModel.name}`}
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
        aria-label={`Effort: ${currentEffort.name}`}
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

Prompt Input is the field the person types into to message the agent. It is an [Input Group](https://shadcn-svelte.com/docs/components/input-group) with a textarea, an attach button, the [Model Selector](https://shadcn-svelte.com/docs/ai-elements/model-selector) menus and a send button. Attached files show as [Attachment](https://shadcn-svelte.com/docs/components/attachment) chips above the text.

## [Installation](#installation)

Prompt Input is built with the [Input Group](https://shadcn-svelte.com/docs/components/input-group), [Attachment](https://shadcn-svelte.com/docs/components/attachment) and [Dropdown Menu](https://shadcn-svelte.com/docs/components/dropdown-menu) components.

```bash
pnpm dlx shadcn-svelte@latest add input-group attachment dropdown-menu
```

```bash
npx shadcn-svelte@latest add input-group attachment dropdown-menu
```

```bash
bun x shadcn-svelte@latest add input-group attachment dropdown-menu
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
```

```svelte
<form bind:this={form} onsubmit={onSubmit}>
  <InputGroup.Root>
    <InputGroup.Textarea
      bind:value={text}
      placeholder="Ask the agent to change your code..."
      class="p-3"
    />
    <InputGroup.Addon align="block-end">
      <InputGroup.Button
        size="icon-sm"
        variant="outline"
        class="rounded-full"
        aria-label="Attach files"
        onclick={() => input?.click()}
      >
        <PlusIcon />
      </InputGroup.Button>
      <InputGroup.Button
        type="submit"
        size="icon-sm"
        variant="default"
        class="ml-auto rounded-full"
        disabled={!canSend}
        aria-label="Send"
      >
        <ArrowUpIcon />
      </InputGroup.Button>
    </InputGroup.Addon>
  </InputGroup.Root>
</form>
```

## [Attachments](#attachments)

The attach button opens a hidden file input. Show each file as an [Attachment](https://shadcn-svelte.com/docs/components/attachment) in an addon with `align="block-start"`, with a button to remove it.

## [Model and Effort](#model-and-effort)

Put the two [Model Selector](https://shadcn-svelte.com/docs/ai-elements/model-selector) menus in the `block-end` addon, between the attach and send buttons. Move `ml-auto` from the send button to the first menu trigger, so both menus sit next to the send button.

## [Keyboard](#keyboard)

Enter sends the message. Shift+Enter adds a new line.

```svelte
onkeydown={(event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form?.requestSubmit();
  }
}}
```

## [AI SDK](#ai-sdk)

Send the text and the `FileList` from the file input.

```ts
chat.sendMessage({ text, files });
```

The route streams the reply with `result.toUIMessageStreamResponse()`.