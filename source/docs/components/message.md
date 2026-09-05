# Message

Displays a message in a conversation, with optional avatar, header, footer, and alignment.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Marker from "$lib/components/ui/marker/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-6 py-12">
  <Message.Root align="end">
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/10.png" alt="@me" />
        <Avatar.Fallback>ME</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Root>
        <Bubble.Content>Deploying to prod real quick.</Bubble.Content>
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root>
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/02.png" alt="@rabbit" />
        <Avatar.Fallback>R</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Root variant="muted">
        <Bubble.Content>It's 4:55 PM. On a Friday.</Bubble.Content>
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root align="end">
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/10.png" alt="@me" />
        <Avatar.Fallback>ME</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Root>
        <Bubble.Content>It's a one-line change.</Bubble.Content>
      </Bubble.Root>
      <Message.Footer>Delivered</Message.Footer>
    </Message.Content>
  </Message.Root>
  <Message.Root>
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/02.png" alt="@rabbit" />
        <Avatar.Fallback>R</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Group>
        <Bubble.Root variant="muted">
          <Bubble.Content>It's always a one-line change .</Bubble.Content>
        </Bubble.Root>
        <Bubble.Root variant="muted">
          <Bubble.Content>Alright, let me take a look.</Bubble.Content>
          <Bubble.Reactions aria-label="Reactions: thumbs up">
            <span></span>
          </Bubble.Reactions>
        </Bubble.Root>
      </Bubble.Group>
    </Message.Content>
  </Message.Root>
  <Marker.Root role="status">
    <Marker.Content class="shimmer">
      <span class="font-medium">Oliver</span> is typing...
    </Marker.Content>
  </Marker.Root>
</div>
```

View Code

The `Message` component lays out a single message in a conversation. It handles the avatar, alignment, header, and footer around the message surface.

For AI apps, you can render reasoning steps, tool calls and assistant messages using the `Message` component.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add message
```

```bash
npx shadcn-svelte@latest add message
```

```bash
bun x shadcn-svelte@latest add message
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
```

```svelte
<Message.Root>
  <Message.Avatar>
    <Avatar.Root>
      <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
      <Avatar.Fallback>CN</Avatar.Fallback>
    </Avatar.Root>
  </Message.Avatar>
  <Message.Content>
    <Bubble.Root>
      <Bubble.Content>How can I help you today?</Bubble.Content>
    </Bubble.Root>
  </Message.Content>
</Message.Root>
```

**Note:** `Message` owns the row layoutavatar, alignment, header, and footer. Render the visible message surface inside it with [`Bubble`](https://shadcn-svelte.com/docs/components/bubble).

## [Composition](#composition)

Use the following composition to build a message:

```text
Message.Root
 Message.Avatar
 Message.Content
     Message.Header
     Bubble.Root
     Message.Footer
```

Use `Message.Group` to stack consecutive messages from the same sender:

```text
Message.Group
 Message.Root
 Message.Root
```

## [Features](#features)

- Start and end alignment for sender and receiver rows via the `align` prop
- Avatar slot that anchors to the bottom of the message and stays clear of the footer  
- Header and footer slots for sender names, status, and message actions  
- Footer follows the message side; actions stay aligned on `align="end"` rows
- Group wrapper for stacking consecutive messages from the same sender  
- Customizable styling through the `class` prop on every part

## [Avatar](#avatar)

Use `Message.Avatar` to render an avatar next to the message. Set `align="end"` on the message to align the avatar to the end of the message.

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-6 py-12">
  <Message.Root>
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/03.png" alt="@avatar" />
        <Avatar.Fallback>R</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Root variant="muted">
        <Bubble.Content
          >The build failed during dependency installation.</Bubble.Content
        >
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root align="end">
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/10.png" alt="@avatar" />
        <Avatar.Fallback>R</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Root>
        <Bubble.Content>Can you share the exact error?</Bubble.Content>
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root>
    <Message.Avatar>
      <Avatar.Root>
        <Avatar.Image src="/avatars/03.png" alt="@avatar" />
        <Avatar.Fallback>R</Avatar.Fallback>
      </Avatar.Root>
    </Message.Avatar>
    <Message.Content>
      <Bubble.Group>
        <Bubble.Root variant="muted">
          <Bubble.Content>Here's the error from the logs</Bubble.Content>
        </Bubble.Root>
        <Bubble.Root variant="muted">
          <Bubble.Content>
            Something went wrong with the build. The libraries are not installed
            correctly. Try running the build again.
          </Bubble.Content>
        </Bubble.Root>
      </Bubble.Group>
    </Message.Content>
  </Message.Root>
</div>
```

View Code

| align                  | Description                                                      |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `start` | Align the message to the start of the conversation.              |
| `end`   | Align the message to the end of the conversation. |

## [Group](#group)

Use `Message.Group` to stack consecutive messages from the same sender. Render an empty `Message.Avatar` on the earlier messages to keep them aligned with the avatar on the last one.

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-6 py-12">
  <Message.Group>
    <Message.Root>
      <Message.Avatar />
      <Message.Content>
        <Bubble.Root variant="muted">
          <Bubble.Content>I checked the registry addresses.</Bubble.Content>
        </Bubble.Root>
      </Message.Content>
    </Message.Root>
    <Message.Root>
      <Message.Avatar>
        <Avatar.Root>
          <Avatar.Image src="/avatars/02.png" alt="@avatar" />
          <Avatar.Fallback>CN</Avatar.Fallback>
        </Avatar.Root>
      </Message.Avatar>
      <Message.Content>
        <Bubble.Root variant="muted">
          <Bubble.Content>
            The component and example JSON now live under the UI registry.
          </Bubble.Content>
        </Bubble.Root>
      </Message.Content>
    </Message.Root>
  </Message.Group>
</div>
```

View Code

## [Header and Footer](#header-and-footer)

Use `Message.Header` for a sender name and `Message.Footer` for metadata such as a delivery or read status.

```svelte
<script lang="ts">
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Message.Root>
    <Message.Content>
      <Message.Header>Olivia</Message.Header>
      <Bubble.Root variant="muted">
        <Bubble.Content>I already checked the logs.</Bubble.Content>
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root align="end">
    <Message.Content>
      <Bubble.Root>
        <Bubble.Content
          >Send the report to the team. Ping @shadcn if you need help.</Bubble.Content
        >
      </Bubble.Root>
      <Message.Footer>
        <div>
          Read <span class="font-normal">Yesterday</span>
        </div>
      </Message.Footer>
    </Message.Content>
  </Message.Root>
</div>
```

View Code

## [Actions](#actions)

Place message-level actions in `Message.Footer`, such as copy, retry, or feedback buttons.

```svelte
<script lang="ts">
  import CopyIcon from "@lucide/svelte/icons/copy";
  import RefreshCcwIcon from "@lucide/svelte/icons/refresh-ccw";
  import ThumbsDownIcon from "@lucide/svelte/icons/thumbs-down";
  import ThumbsUpIcon from "@lucide/svelte/icons/thumbs-up";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Message.Root>
    <Message.Content>
      <Bubble.Root variant="muted">
        <Bubble.Content
          >The install failure is coming from the workspace package.</Bubble.Content
        >
      </Bubble.Root>
      <Message.Footer>
        <Button variant="ghost" size="icon" aria-label="Copy" title="Copy">
          <CopyIcon />
        </Button>
        <Button variant="ghost" size="icon" aria-label="Like" title="Like">
          <ThumbsUpIcon />
        </Button>
        <Button
          variant="ghost"
          size="icon"
          aria-label="Dislike"
          title="Dislike"
        >
          <ThumbsDownIcon />
        </Button>
      </Message.Footer>
    </Message.Content>
  </Message.Root>
  <Message.Root align="end">
    <Message.Content>
      <Bubble.Root>
        <Bubble.Content>Okay drop me a link. Taking a look...</Bubble.Content>
      </Bubble.Root>
      <Message.Footer class="gap-2">
        <span class="font-normal text-destructive">Failed to send</span>
        <Button variant="ghost" size="icon-xs" title="Retry" aria-label="Retry">
          <RefreshCcwIcon />
        </Button>
      </Message.Footer>
    </Message.Content>
  </Message.Root>
</div>
```

View Code

## [Attachment](#attachment)

```svelte
<script lang="ts">
  import DownloadIcon from "@lucide/svelte/icons/download";
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import * as Attachment from "$lib/components/ui/attachment/index.js";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-8 py-12">
  <Message.Root align="end">
    <Message.Content>
      <Attachment.Root orientation="vertical">
        <Attachment.Media variant="image">
          <img
            src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80"
            alt="Workspace"
          />
        </Attachment.Media>
      </Attachment.Root>
      <Bubble.Root>
        <Bubble.Content>
          Here's the image. Can you add it to the PDF? Use it for the cover
          page.
        </Bubble.Content>
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root>
    <Message.Content>
      <Bubble.Root variant="muted">
        <Bubble.Content>
          Done. Here's the PDF with the image added as the cover page.
        </Bubble.Content>
      </Bubble.Root>
      <Attachment.Root>
        <Attachment.Media>
          <FileTextIcon />
        </Attachment.Media>
        <Attachment.Content>
          <Attachment.Title>sales-dashboard.pdf</Attachment.Title>
          <Attachment.Description>PDF  2.4 MB</Attachment.Description>
        </Attachment.Content>
        <Attachment.Actions>
          <Attachment.Action
            type="button"
            title="Download"
            aria-label="Download"
            size="icon-sm"
            variant="secondary"
          >
            <DownloadIcon />
          </Attachment.Action>
        </Attachment.Actions>
      </Attachment.Root>
    </Message.Content>
  </Message.Root>
  <Message.Root align="end">
    <Message.Content>
      <Bubble.Root>
        <Bubble.Content>Thanks. Looks good.</Bubble.Content>
      </Bubble.Root>
    </Message.Content>
  </Message.Root>
</div>
```

View Code

## [Accessibility](#accessibility) `Message` is a presentational layout wrapper. Accessibility comes from the content you place inside it.

### [Label icon-only actions](#label-icon-only-actions)

Action buttons in `Message.Footer` are usually icon-only, so give each one an `aria-label`.

```svelte
<Message.Footer>
  <Button variant="ghost" size="icon" aria-label="Copy">
    <CopyIcon />
  </Button>
</Message.Footer>
```

### [Status updates](#status-updates)

For in-progress messages, use a [`Marker`](https://shadcn-svelte.com/docs/components/marker) with `role="status"` so assistive tech announces the update as it appears.

```svelte
<Message.Root>
  <Marker.Root role="status">
    <Marker.Icon>
      <Spinner />
    </Marker.Icon>
    <Marker.Content>Checking the logs...</Marker.Content>
  </Marker.Root>
</Message.Root>
```

## [API Reference](#api-reference)

### [Message](#message)

The message row wrapper.

| Prop                   | Type                      | Default          | Description                                            |
| ---------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `align` | `"start" \| "end"` | `"start"` | The alignment of the message in the conversation.      |
| `class` | `string`           | -                | Additional classes to apply to the row. | ### [Message.Group](#messagegroup)

Groups consecutive messages from the same sender.

| Prop                   | Type            | Default | Description                                                   |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the group root. | ### [Message.Avatar](#messageavatar)

The avatar slot, aligned to the bottom of the message. When the message has a `Message.Footer`, the avatar shifts up to stay aligned with the message surface instead of the footer.

| Prop                   | Type            | Default | Description                                                    |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the avatar slot. | ### [Message.Content](#messagecontent)

Wraps the header, message surface, and footer.

| Prop                   | Type            | Default | Description                                                     |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the content slot. | ### [Message.Header](#messageheader)

Displays content above the message, such as a sender name. Stays aligned to the start regardless of `align`.

| Prop                   | Type            | Default | Description                                               |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the header. | ### [Message.Footer](#messagefooter)

Displays content below the message, such as status or actions. Aligns to the message side.

| Prop                   | Type            | Default | Description                                               |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the footer. |