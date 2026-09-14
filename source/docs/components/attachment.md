# Attachment

Displays a file or image attachment with media, metadata, upload state, and actions.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import FileCodeIcon from "@lucide/svelte/icons/file-code";
  import XIcon from "@lucide/svelte/icons/x";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
  const images = [
    {
      name: "workspace.png",
      meta: "PNG  820 KB",
      src: "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80",
      alt: "Workspace"
    },
    {
      name: "desk-reference.jpg",
      meta: "JPG  1.1 MB",
      src: "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=900&auto=format&fit=crop&q=80",
      alt: "Desk"
    },
    {
      name: "office-reference.jpg",
      meta: "JPG  940 KB",
      src: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=900&auto=format&fit=crop&q=80",
      alt: "Office"
    }
 ];
</script>
<div class="mx-auto flex w-full max-w-sm flex-col gap-3 py-12">
  <Attachment.Group>
    {#each images as image (image.name)}
      <Attachment.Root orientation="vertical">
        <Attachment.Media variant="image">
          <img src={image.src} alt={image.alt} />
        </Attachment.Media>
        <Attachment.Content>
          <Attachment.Title>{image.name}</Attachment.Title>
          <Attachment.Description>{image.meta}</Attachment.Description>
        </Attachment.Content>
      </Attachment.Root>
    {/each}
  </Attachment.Group>
  <Attachment.Root state="uploading" class="w-full">
    <Attachment.Media>
      <Spinner />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>sales-dashboard.pdf</Attachment.Title>
      <Attachment.Description>Uploading  64%</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Cancel upload">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
  <Attachment.Root class="w-full">
    <Attachment.Media>
      <FileCodeIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>message-renderer.tsx</Attachment.Title>
      <Attachment.Description>TypeScript  12 KB</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Remove message-renderer.tsx">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
</div>
```

View Code

The `Attachment` component displays a file or image attachment, its media, name, and metadata, with optional actions and upload state. Use it for files and images in chat composers, message threads, and upload lists.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add attachment
```

```bash
npx shadcn-svelte@latest add attachment
```

```bash
bun x shadcn-svelte@latest add attachment
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Attachment from "$lib/components/ui/attachment/index.js";
</script>
```

```svelte
<Attachment.Root>
  <Attachment.Media>
    <FileTextIcon />
  </Attachment.Media>
  <Attachment.Content>
    <Attachment.Title>sales-dashboard.pdf</Attachment.Title>
    <Attachment.Description>PDF  2.4 MB</Attachment.Description>
  </Attachment.Content>
  <Attachment.Actions>
    <Attachment.Action aria-label="Remove sales-dashboard.pdf">
      <XIcon />
    </Attachment.Action>
  </Attachment.Actions>
</Attachment.Root>
```

## [Composition](#composition)

Use the following composition to build an attachment:

```text
Attachment.Root
 Attachment.Media
 Attachment.Content
    Attachment.Title
    Attachment.Description
 Attachment.Actions
    Attachment.Action
 Attachment.Trigger
```

Use `Attachment.Group` to lay out multiple attachments in a scrollable row:

```text
Attachment.Group
 Attachment.Root
 Attachment.Root
```

## [Features](#features)

- Icon and image media through `Attachment.Media` - Upload states: `idle` , `uploading` , `processing` , `error` , and `done` with built-in styling and a shimmer while in progress
- Three sizes and horizontal or vertical orientation  
- A full-card `Attachment.Trigger` that opens a link or dialog while the actions stay independently clickable
- Scrollable, snapping `Attachment.Group` with an edge fade
- Customizable styling through the `class` prop on every part

## [Image](#image)

Set `variant="image"` on `Attachment.Media` and render an `<img>` inside it. Use `orientation="vertical"` to stack the media above the content.

```svelte
<script lang="ts">
  import XIcon from "@lucide/svelte/icons/x";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
  const images = [
    {
      name: "workspace.png",
      meta: "PNG  820 KB",
      src: "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80",
      alt: "Workspace"
    },
    {
      name: "desk-reference.jpg",
      meta: "JPG  1.1 MB",
      src: "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=900&auto=format&fit=crop&q=80",
      alt: "Desk"
    },
    {
      name: "office-reference.jpg",
      meta: "JPG  940 KB",
      src: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=900&auto=format&fit=crop&q=80",
      alt: "Office"
    }
 ];
</script>
<div class="mx-auto w-full max-w-sm py-12">
  <Attachment.Group class="w-full">
    {#each images as image (image.name)}
      <Attachment.Root orientation="vertical">
        <Attachment.Media variant="image">
          <img src={image.src} alt={image.alt} />
        </Attachment.Media>
        <Attachment.Content>
          <Attachment.Title>{image.name}</Attachment.Title>
          <Attachment.Description>{image.meta}</Attachment.Description>
        </Attachment.Content>
        <Attachment.Actions>
          <Attachment.Action aria-label="Remove {image.name}">
            <XIcon />
          </Attachment.Action>
        </Attachment.Actions>
        <Attachment.Trigger>
          {#snippet child({ props })}
            <a
              href={image.src}
              target="_blank"
              rel="noreferrer"
              aria-label="Open {image.name}"
              {...props}
            ></a>
          {/snippet}
        </Attachment.Trigger>
      </Attachment.Root>
    {/each}
  </Attachment.Group>
</div>
```

View Code

## [States](#states)

Set `state` to reflect the upload lifecycle. `uploading` and `processing` shimmer the title, and `error` switches to a destructive treatment.

```svelte
<script lang="ts">
  import CheckIcon from "@lucide/svelte/icons/check";
  import ClockIcon from "@lucide/svelte/icons/clock";
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import FileWarningIcon from "@lucide/svelte/icons/file-warning";
  import RefreshCwIcon from "@lucide/svelte/icons/refresh-cw";
  import XIcon from "@lucide/svelte/icons/x";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="mx-auto flex w-full max-w-sm flex-col gap-2 py-12">
  <Attachment.Root state="idle" class="w-full">
    <Attachment.Media>
      <ClockIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>selected-file.pdf</Attachment.Title>
      <Attachment.Description>Ready to upload</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Remove selected-file.pdf">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
  <Attachment.Root state="uploading" class="w-full">
    <Attachment.Media>
      <Spinner />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>design-system.zip</Attachment.Title>
      <Attachment.Description>Uploading  64%</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Cancel upload">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
  <Attachment.Root state="processing" class="w-full">
    <Attachment.Media>
      <FileTextIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>market-research.pdf</Attachment.Title>
      <Attachment.Description>Processing document</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Remove market-research.pdf">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
  <Attachment.Root state="error" class="w-full">
    <Attachment.Media>
      <FileWarningIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>financial-model.xlsx</Attachment.Title>
      <Attachment.Description>Upload failed. Try again.</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Retry upload">
        <RefreshCwIcon />
      </Attachment.Action>
      <Attachment.Action aria-label="Remove financial-model.xlsx">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
  <Attachment.Root state="done" class="w-full">
    <Attachment.Media>
      <CheckIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>uploaded-report.pdf</Attachment.Title>
      <Attachment.Description>Uploaded  1.8 MB</Attachment.Description>
    </Attachment.Content>
    <Attachment.Actions>
      <Attachment.Action aria-label="Remove uploaded-report.pdf">
        <XIcon />
      </Attachment.Action>
    </Attachment.Actions>
  </Attachment.Root>
</div>
```

View Code

## [Sizes](#sizes)

Use `size` to switch between `default`, `sm`, and `xs`.

```svelte
<script lang="ts">
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
</script>
<div class="mx-auto flex w-full max-w-sm flex-col gap-3 py-12">
  <Attachment.Root size="default" class="w-full">
    <Attachment.Media>
      <FileTextIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>Default attachment</Attachment.Title>
      <Attachment.Description>PDF  2.4 MB</Attachment.Description>
    </Attachment.Content>
  </Attachment.Root>
  <Attachment.Root size="sm" class="w-full">
    <Attachment.Media>
      <FileTextIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>Small attachment</Attachment.Title>
      <Attachment.Description>PDF  2.4 MB</Attachment.Description>
    </Attachment.Content>
  </Attachment.Root>
  <Attachment.Root size="xs" class="w-full">
    <Attachment.Media>
      <FileTextIcon />
    </Attachment.Media>
    <Attachment.Content>
      <Attachment.Title>Extra small attachment</Attachment.Title>
    </Attachment.Content>
  </Attachment.Root>
</div>
```

View Code

## [Group](#group)

Wrap attachments in `Attachment.Group` to lay them out in a horizontally scrollable, snapping row with an edge fade.

```svelte
<script lang="ts">
  import FileCodeIcon from "@lucide/svelte/icons/file-code";
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import TableIcon from "@lucide/svelte/icons/table";
  import XIcon from "@lucide/svelte/icons/x";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
  import type { Component } from "svelte";
  type Item = {
    name: string;
    meta: string;
    icon?: Component;
    src?: string;
  };
  const items: Item[] = [
    { name: "briefing-notes.pdf", meta: "PDF  1.4 MB", icon: FileTextIcon },
    {
      name: "workspace.png",
      meta: "PNG  820 KB",
      src: "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80"
    },
    { name: "customers.csv", meta: "CSV  18 KB", icon: TableIcon },
    { name: "renderer.tsx", meta: "TSX  12 KB", icon: FileCodeIcon }
 ];
</script>
<div class="mx-auto w-full max-w-sm py-12">
  <Attachment.Group class="w-full">
    {#each items as item (item.name)}
      {@const Icon = item.icon}
      <Attachment.Root class="w-64">
        {#if item.src}
          <Attachment.Media variant="image">
            <img src={item.src} alt={item.name} />
          </Attachment.Media>
        {:else if Icon}
          <Attachment.Media>
            <Icon />
          </Attachment.Media>
        {/if}
        <Attachment.Content>
          <Attachment.Title>{item.name}</Attachment.Title>
          <Attachment.Description>{item.meta}</Attachment.Description>
        </Attachment.Content>
        <Attachment.Actions>
          <Attachment.Action aria-label="Remove {item.name}">
            <XIcon />
          </Attachment.Action>
        </Attachment.Actions>
      </Attachment.Root>
    {/each}
  </Attachment.Group>
</div>
```

View Code

## [Trigger](#trigger)

Add an `Attachment.Trigger` to make the whole card open a link or dialog. It fills the card behind the actions, so the actions stay clickable.

```svelte
<script lang="ts">
  import CopyIcon from "@lucide/svelte/icons/copy";
  import FileSearchIcon from "@lucide/svelte/icons/file-search";
  import XIcon from "@lucide/svelte/icons/x";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
</script>
<div class="mx-auto w-full max-w-sm py-12">
  <Dialog.Root>
    <Attachment.Root class="w-full">
      <Attachment.Media>
        <FileSearchIcon />
      </Attachment.Media>
      <Attachment.Content>
        <Attachment.Title>research-summary.pdf</Attachment.Title>
        <Attachment.Description>Open preview dialog</Attachment.Description>
      </Attachment.Content>
      <Attachment.Actions>
        <Attachment.Action aria-label="Copy link">
          <CopyIcon />
        </Attachment.Action>
        <Attachment.Action aria-label="Remove research-summary.pdf">
          <XIcon />
        </Attachment.Action>
      </Attachment.Actions>
      <Dialog.Trigger>
        {#snippet child({ props })}
          <Attachment.Trigger
            {...props}
            aria-label="Preview research-summary.pdf"
          />
        {/snippet}
      </Dialog.Trigger>
    </Attachment.Root>
    <Dialog.Content class="sm:max-w-md">
      <Dialog.Header>
        <Dialog.Title>research-summary.pdf</Dialog.Title>
        <Dialog.Description>
          The attachment trigger fills the card and opens the dialog, while the
          actions stay independently clickable above it.
        </Dialog.Description>
      </Dialog.Header>
    </Dialog.Content>
  </Dialog.Root>
</div>
```

View Code

```svelte
<Dialog.Root>
  <Attachment.Root>
    <Dialog.Trigger>
      {#snippet child({ props })}
        <Attachment.Trigger
          aria-label="Preview research-summary.pdf"
          {...props}
        />
      {/snippet}
    </Dialog.Trigger>
  </Attachment.Root>
  <Dialog.Content></Dialog.Content>
</Dialog.Root>
```

## [Accessibility](#accessibility) `Attachment.Action` renders a `Button`, and `Attachment.Trigger` renders a real `<button>` (or your element via the `child` snippet). Follow the guidance below so both are operable and announced.

### [Label icon-only actions](#label-icon-only-actions) `Attachment.Action` is usually icon-only, so give each one an `aria-label` describing the action and its target.

```svelte
<Attachment.Action aria-label="Remove sales-dashboard.pdf">
  <XIcon />
</Attachment.Action>
```

### [Label the trigger](#label-the-trigger) `Attachment.Trigger` covers the card with no text of its own, so give it an `aria-label` for what activating it does.

```svelte
<Attachment.Trigger>
  {#snippet child({ props })}
    <a
      href={url}
      target="_blank"
      rel="noreferrer"
      aria-label="Open workspace.png"
      {...props}
    ></a>
  {/snippet}
</Attachment.Trigger>
```

The trigger sits behind the actions in the stacking order, so an `Attachment.Action` and the `Attachment.Trigger` never trap each other. Both remain separately focusable and clickable.

### [Keyboard scrolling](#keyboard-scrolling)

An `Attachment.Group` scrolls horizontally. When its attachments are interactive (a trigger or actions), keyboard users reach off-screen items by tabbing to them. For a row of presentational attachments, make the group itself focusable and scrollable by adding `tabindex={0}`, `role="group"`, and an `aria-label`.

### [Meaning beyond color](#meaning-beyond-color)

The `error` state uses a destructive color. Keep the failure reason in `Attachment.Description` so the state is not conveyed by color alone.

## [API Reference](#api-reference)

### [Attachment](#attachment)

The root attachment container.

| Prop                         | Type                                                                | Default               | Description                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `state`       | `"idle" \| "uploading" \| "processing" \| "error" \| "done"` | `"done"`       | The upload state. Drives styling and the shimmer.               |
| `size`        | `"default" \| "sm" \| "xs"`                                  | `"default"`    | The attachment size.                                            |
| `orientation` | `"horizontal" \| "vertical"`                                 | `"horizontal"` | Lay the media beside or above the content.                      |
| `class`       | `string`                                                     | -                     | Additional classes to apply to the root element. | ### [Attachment.Media](#attachmentmedia)

The media slot for an icon or image preview.

| Prop                     | Type                       | Default         | Description                                                   |
| ------------------------------------------------------ | -------------------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `variant` | `"icon" \| "image"` | `"icon"` | Whether the media holds an icon or an `<img>`.  |
| `class`   | `string`            | -               | Additional classes to apply to the media slot. | ### [Attachment.Content](#attachmentcontent)

Wraps the title and description.

| Prop                   | Type            | Default | Description                                                     |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the content slot. | ### [Attachment.Title](#attachmenttitle)

The attachment name. Shimmers while the attachment is `uploading` or `processing`.

| Prop                   | Type            | Default | Description                                              |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the title. | ### [Attachment.Description](#attachmentdescription)

Secondary metadata such as the file type, size, or upload status.

| Prop                   | Type            | Default | Description                                                    |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the description. | ### [Attachment.Actions](#attachmentactions)

A container for one or more actions, aligned to the end of the attachment.

| Prop                   | Type            | Default | Description                                                |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the actions. | ### [Attachment.Action](#attachmentaction)

An action button. Renders a [`Button`](https://shadcn-svelte.com/docs/components/button) and accepts all of its props.

| Prop                      | Type                  | Default            | Description                                                           |
| ------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `size`     | `Button` size  | `"icon-xs"` | The button size.                                                      |
| `...props` | `Button` props | -                  | Props spread to the underlying `Button`. | ### [Attachment.Trigger](#attachmenttrigger)

A full-card overlay that activates the attachment. Renders a `<button>` by default.

| Prop                   | Type             | Default | Description                                                |
| ---------------------------------------------------- | ---------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `child` | `snippet` | -       | Render as the child element, such as a link.               |
| `class` | `string`  | -       | Additional classes to apply to the trigger. | ### [Attachment.Group](#attachmentgroup)

Lays out attachments in a horizontally scrollable, snapping row.

| Prop                   | Type            | Default | Description                                              |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the group. |