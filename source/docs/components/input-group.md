# Input Group

Add addons, buttons, and helper content to inputs.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import SearchIcon from "@lucide/svelte/icons/search";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<InputGroup.Root class="max-w-xs">
 <InputGroup.Input placeholder="Search..." />
 <InputGroup.Addon>
  <SearchIcon />
 </InputGroup.Addon>
 <InputGroup.Addon align="inline-end">12 results</InputGroup.Addon>
</InputGroup.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add input-group
```

```bash
npx shadcn-svelte@latest add input-group
```

```bash
bun x shadcn-svelte@latest add input-group
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import SearchIcon from "@lucide/svelte/icons/search";
</script>
```

```svelte
<InputGroup.Root>
  <InputGroup.Input placeholder="Search..." />
  <InputGroup.Addon>
    <SearchIcon />
  </InputGroup.Addon>
  <InputGroup.Addon align="inline-end">
    <InputGroup.Button>Search</InputGroup.Button>
  </InputGroup.Addon>
</InputGroup.Root>
```

## [Align](#align)

Use the `align` prop on `InputGroup.Addon` to position the addon relative to the input.

For proper focus management, `InputGroup.Addon` should always be placed after `InputGroup.Input` or `InputGroup.Textarea` in the DOM. Use the `align` prop to visually position the addon.

### [inline-start](#inline-start)

Use `align="inline-start"` to position the addon at the start of the input. This is the default.

```svelte
<script lang="ts">
 import SearchIcon from "@lucide/svelte/icons/search";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<Field.Field class="max-w-sm">
 <Field.Label for="inline-start-input">Input</Field.Label>
 <InputGroup.Root>
  <InputGroup.Input id="inline-start-input" placeholder="Search..." />
  <InputGroup.Addon align="inline-start">
   <SearchIcon class="text-muted-foreground" />
  </InputGroup.Addon>
 </InputGroup.Root>
 <Field.Description>Icon positioned at the start.</Field.Description>
</Field.Field>
```

View Code

### [inline-end](#inline-end)

Use `align="inline-end"` to position the addon at the end of the input.

```svelte
<script lang="ts">
 import EyeOffIcon from "@lucide/svelte/icons/eye-off";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<Field.Field class="max-w-sm">
 <Field.Label for="inline-end-input">Input</Field.Label>
 <InputGroup.Root>
  <InputGroup.Input id="inline-end-input" type="password" placeholder="Enter password" />
  <InputGroup.Addon align="inline-end">
   <EyeOffIcon />
  </InputGroup.Addon>
 </InputGroup.Root>
 <Field.Description>Icon positioned at the end.</Field.Description>
</Field.Field>
```

View Code

### [block-start](#block-start)

Use `align="block-start"` to position the addon above the input.

```svelte
<script lang="ts">
 import CopyIcon from "@lucide/svelte/icons/copy";
 import FileCodeIcon from "@lucide/svelte/icons/file-code";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<Field.Group class="max-w-sm">
 <Field.Field>
  <Field.Label for="block-start-input">Input</Field.Label>
  <InputGroup.Root class="h-auto">
   <InputGroup.Input id="block-start-input" placeholder="Enter your name" />
   <InputGroup.Addon align="block-start">
    <InputGroup.Text>Full Name</InputGroup.Text>
   </InputGroup.Addon>
  </InputGroup.Root>
  <Field.Description>Header positioned above the input.</Field.Description>
 </Field.Field>
 <Field.Field>
  <Field.Label for="block-start-textarea">Textarea</Field.Label>
  <InputGroup.Root>
   <InputGroup.Textarea
    id="block-start-textarea"
    placeholder="console.log('Hello, world!');"
    class="font-mono text-sm"
   />
   <InputGroup.Addon align="block-start">
    <FileCodeIcon class="text-muted-foreground" />
    <InputGroup.Text class="font-mono">script.js</InputGroup.Text>
    <InputGroup.Button size="icon-xs" class="ml-auto">
     <CopyIcon />
     <span class="sr-only">Copy</span>
    </InputGroup.Button>
   </InputGroup.Addon>
  </InputGroup.Root>
  <Field.Description>Header positioned above the textarea.</Field.Description>
 </Field.Field>
</Field.Group>
```

View Code

### [block-end](#block-end)

Use `align="block-end"` to position the addon below the input.

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<Field.Group class="max-w-sm">
 <Field.Field>
  <Field.Label for="block-end-input">Input</Field.Label>
  <InputGroup.Root class="h-auto">
   <InputGroup.Input id="block-end-input" placeholder="Enter amount" />
   <InputGroup.Addon align="block-end">
    <InputGroup.Text>USD</InputGroup.Text>
   </InputGroup.Addon>
  </InputGroup.Root>
  <Field.Description>Footer positioned below the input.</Field.Description>
 </Field.Field>
 <Field.Field>
  <Field.Label for="block-end-textarea">Textarea</Field.Label>
  <InputGroup.Root>
   <InputGroup.Textarea id="block-end-textarea" placeholder="Write a comment..." />
   <InputGroup.Addon align="block-end">
    <InputGroup.Text>0/280</InputGroup.Text>
    <InputGroup.Button variant="default" size="sm" class="ml-auto">Post</InputGroup.Button>
   </InputGroup.Addon>
  </InputGroup.Root>
  <Field.Description>Footer positioned below the textarea.</Field.Description>
 </Field.Field>
</Field.Group>
```

View Code

## [Icon](#icon)

```svelte
<script lang="ts">
 import CheckIcon from "@lucide/svelte/icons/check";
 import CreditCardIcon from "@lucide/svelte/icons/credit-card";
 import InfoIcon from "@lucide/svelte/icons/info";
 import MailIcon from "@lucide/svelte/icons/mail";
 import SearchIcon from "@lucide/svelte/icons/search";
 import StarIcon from "@lucide/svelte/icons/star";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<div class="grid w-full max-w-sm gap-6">
 <InputGroup.Root>
  <InputGroup.Input placeholder="Search..." />
  <InputGroup.Addon>
   <SearchIcon />
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input type="email" placeholder="Enter your email" />
  <InputGroup.Addon>
   <MailIcon />
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Card number" />
  <InputGroup.Addon>
   <CreditCardIcon />
  </InputGroup.Addon>
  <InputGroup.Addon align="inline-end">
   <CheckIcon />
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Card number" />
  <InputGroup.Addon align="inline-end">
   <StarIcon />
   <InfoIcon />
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code

## [Text](#text)

```svelte
<script lang="ts">
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<div class="grid w-full max-w-sm gap-6">
 <InputGroup.Root>
  <InputGroup.Addon>
   <InputGroup.Text>$</InputGroup.Text>
  </InputGroup.Addon>
  <InputGroup.Input placeholder="0.00" />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Text>USD</InputGroup.Text>
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Addon>
   <InputGroup.Text>https://</InputGroup.Text>
  </InputGroup.Addon>
  <InputGroup.Input placeholder="example.com" class="!ps-0.5" />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Text>.com</InputGroup.Text>
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Enter your username" />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Text>@company.com</InputGroup.Text>
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Textarea placeholder="Enter your message" />
  <InputGroup.Addon align="block-end">
   <InputGroup.Text class="text-xs text-muted-foreground">120 characters left</InputGroup.Text>
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code

## [Button](#button)

```svelte
<script lang="ts">
 import IconCheck from "@tabler/icons-svelte/icons/check";
 import IconCopy from "@tabler/icons-svelte/icons/copy";
 import IconInfoCircle from "@tabler/icons-svelte/icons/info-circle";
 import IconStar from "@tabler/icons-svelte/icons/star";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
 import * as Popover from "$lib/components/ui/popover/index.js";
 import { UseClipboard } from "$lib/hooks/use-clipboard.svelte.js";
 let isFavorite = $state(false);
 const clipboard = new UseClipboard();
</script>
<div class="grid w-full max-w-sm gap-6">
 <InputGroup.Root>
  <InputGroup.Input placeholder="https://x.com/shadcn" readonly />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Button
    aria-label="Copy"
    title="Copy"
    size="icon-xs"
    onclick={() => clipboard.copy("https://x.com/shadcn")}
   >
    {#if clipboard.copied}
     <IconCheck />
    {:else}
     <IconCopy />
    {/if}
   </InputGroup.Button>
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root class="[--radius:9999px]">
  <Popover.Root>
   <Popover.Trigger>
    {#snippet child({ props })}
     <InputGroup.Addon>
      <InputGroup.Button {...props} variant="secondary" size="icon-xs">
       <IconInfoCircle />
      </InputGroup.Button>
     </InputGroup.Addon>
    {/snippet}
   </Popover.Trigger>
   <Popover.Content align="start" class="flex flex-col gap-1 rounded-xl text-sm">
    <p class="font-medium">Your connection is not secure.</p>
    <p>You should not enter any sensitive information on this site.</p>
   </Popover.Content>
  </Popover.Root>
  <InputGroup.Addon class="ps-1.5 text-muted-foreground">https://</InputGroup.Addon>
  <InputGroup.Input id="input-secure-19" />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Button onclick={() => (isFavorite = !isFavorite)} size="icon-xs">
    <IconStar
     data-favorite={isFavorite}
     class="data-[favorite=true]:fill-blue-600 data-[favorite=true]:stroke-blue-600"
    />
   </InputGroup.Button>
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Type to search..." />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Button variant="secondary">Search</InputGroup.Button>
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code

## [Kbd](#kbd)

```svelte
<script lang="ts">
 import SearchIcon from "@lucide/svelte/icons/search";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
 import { Kbd } from "$lib/components/ui/kbd/index.js";
</script>
<InputGroup.Root class="max-w-sm">
 <InputGroup.Input placeholder="Search..." />
 <InputGroup.Addon>
  <SearchIcon class="text-muted-foreground" />
 </InputGroup.Addon>
 <InputGroup.Addon align="inline-end">
  <Kbd>K</Kbd>
 </InputGroup.Addon>
</InputGroup.Root>
```

View Code

## [Dropdown](#dropdown)

```svelte
<script lang="ts">
 import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
 import MoreHorizontalIcon from "@lucide/svelte/icons/more-horizontal";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<div class="grid w-full max-w-sm gap-4">
 <InputGroup.Root>
  <InputGroup.Input placeholder="Enter file name" />
  <InputGroup.Addon align="inline-end">
   <DropdownMenu.Root>
    <DropdownMenu.Trigger>
     {#snippet child({ props })}
      <InputGroup.Button {...props} variant="ghost" aria-label="More" size="icon-xs">
       <MoreHorizontalIcon />
      </InputGroup.Button>
     {/snippet}
    </DropdownMenu.Trigger>
    <DropdownMenu.Content align="end" sideOffset={8} alignOffset={-4}>
     <DropdownMenu.Group>
      <DropdownMenu.Item>Settings</DropdownMenu.Item>
      <DropdownMenu.Item>Copy path</DropdownMenu.Item>
      <DropdownMenu.Item>Open location</DropdownMenu.Item>
     </DropdownMenu.Group>
    </DropdownMenu.Content>
   </DropdownMenu.Root>
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Enter search query" />
  <InputGroup.Addon align="inline-end">
   <DropdownMenu.Root>
    <DropdownMenu.Trigger>
     {#snippet child({ props })}
      <InputGroup.Button {...props} variant="ghost" class="!pe-1.5 text-xs">
       Search In... <ChevronDownIcon class="size-3" />
      </InputGroup.Button>
     {/snippet}
    </DropdownMenu.Trigger>
    <DropdownMenu.Content align="end" sideOffset={8} alignOffset={-4}>
     <DropdownMenu.Group>
      <DropdownMenu.Item>Documentation</DropdownMenu.Item>
      <DropdownMenu.Item>Blog Posts</DropdownMenu.Item>
      <DropdownMenu.Item>Changelog</DropdownMenu.Item>
     </DropdownMenu.Group>
    </DropdownMenu.Content>
   </DropdownMenu.Root>
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code

## [Spinner](#spinner)

```svelte
<script lang="ts">
 import LoaderIcon from "@lucide/svelte/icons/loader";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
 import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="grid w-full max-w-sm gap-4">
 <InputGroup.Root>
  <InputGroup.Input placeholder="Searching..." />
  <InputGroup.Addon align="inline-end">
   <Spinner />
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Processing..." />
  <InputGroup.Addon>
   <Spinner />
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Saving changes..." />
  <InputGroup.Addon align="inline-end">
   <InputGroup.Text>Saving...</InputGroup.Text>
   <Spinner />
  </InputGroup.Addon>
 </InputGroup.Root>
 <InputGroup.Root>
  <InputGroup.Input placeholder="Refreshing data..." />
  <InputGroup.Addon>
   <LoaderIcon class="animate-spin" />
  </InputGroup.Addon>
  <InputGroup.Addon align="inline-end">
   <InputGroup.Text class="text-muted-foreground">Please wait...</InputGroup.Text>
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code

## [Textarea](#textarea)

```svelte
<script lang="ts">
 import IconBrandJavascript from "@tabler/icons-svelte/icons/brand-javascript";
 import IconCopy from "@tabler/icons-svelte/icons/copy";
 import IconCornerDownLeft from "@tabler/icons-svelte/icons/corner-down-left";
 import IconRefresh from "@tabler/icons-svelte/icons/refresh";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<div class="grid w-full max-w-md gap-4">
 <InputGroup.Root>
  <InputGroup.Textarea
   id="textarea-code-32"
   placeholder="console.log('Hello, world!');"
   class="min-h-[200px]"
  />
  <InputGroup.Addon align="block-end" class="border-t">
   <InputGroup.Text>Line 1, Column 1</InputGroup.Text>
   <InputGroup.Button size="sm" class="ms-auto" variant="default">
    Run <IconCornerDownLeft />
   </InputGroup.Button>
  </InputGroup.Addon>
  <InputGroup.Addon align="block-start" class="border-b">
   <InputGroup.Text class="font-mono font-medium">
    <IconBrandJavascript />
    script.js
   </InputGroup.Text>
   <InputGroup.Button class="ms-auto" size="icon-xs">
    <IconRefresh />
   </InputGroup.Button>
   <InputGroup.Button variant="ghost" size="icon-xs">
    <IconCopy />
   </InputGroup.Button>
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code

## [Custom Input](#custom-input)

Add the `data-slot="input-group-control"` attribute to your custom input for automatic focus state handling.

Here's an example of a custom auto-resizing textarea.

```svelte
<script lang="ts">
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<div class="grid w-full max-w-sm gap-6">
 <InputGroup.Root>
  <textarea
   data-slot="input-group-control"
   class="flex field-sizing-content min-h-16 w-full resize-none rounded-md bg-transparent px-3 py-2.5 text-base transition-[color,box-shadow] outline-none md:text-sm"
   placeholder="Autoresize textarea..."></textarea>
  <InputGroup.Addon align="block-end">
   <InputGroup.Button class="ms-auto" size="sm" variant="default">Submit</InputGroup.Button>
  </InputGroup.Addon>
 </InputGroup.Root>
</div>
```

View Code