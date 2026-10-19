# Message Scroller

A chat scroll container that anchors turns, opens saved transcripts, follows streamed responses, loads history without jumping, and jumps to any message.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import GlobeIcon from "@lucide/svelte/icons/globe";
  import ImageIcon from "@lucide/svelte/icons/image";
  import MessageCircleDashedIcon from "@lucide/svelte/icons/message-circle-dashed";
  import PaperclipIcon from "@lucide/svelte/icons/paperclip";
  import PlusIcon from "@lucide/svelte/icons/plus";
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import TelescopeIcon from "@lucide/svelte/icons/telescope";
  import { Chat } from "@ai-sdk/svelte";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as Empty from "$lib/components/ui/empty/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import MessageAnimated from "$lib/components/message-animated.svelte";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const script = createChat()
    .user(
      "I'm building a chat for our app and the scroll behavior is driving me nuts. Every time the AI streams a reply, the whole thread jumps around."
    )
    .sleep(1000)
    .assistant(
      "That's the classic streaming scroll problem. Wrap your message list in `MessageScroller` and turn on `autoScroll`  the viewport pins to the bottom as tokens arrive, so users always see the latest text land in place.\n\nThe important part: it only auto-scrolls while the reader is already at the bottom. The moment they scroll up to read something earlier, auto-scroll backs off and their position is preserved. You get smooth streaming without fighting the user's intent."
    )
    .user(
      "Okay, but when someone sends a new message the view still feels jarring  like the whole conversation reloads from the top."
    )
    .sleep(1000)
    .assistant(
      "MessageScrollerItem fixes that with turn anchoring. Set `scrollAnchor` on the turn that should settle near the top instead of blindly snapping to the document bottom.\n\nIt also leaves a small peek of the previous exchange visible above the anchor, so context isn't lost. The reply starts in view without that disorienting jump you get from a plain overflow container."
    )
    .user(
      "And if they've scrolled up to re-read an older answer? I don't want to yank them back down."
    )
    .sleep(1000)
    .assistant(
      "You won't. Auto-scroll only runs when the viewport is already pinned to the bottom, so scrolling up is a deliberate opt-out  their place in the thread stays put even as new tokens keep arriving below.\n\nWhen there is content they haven't seen yet, `MessageScrollerButton` appears at the bottom of the viewport. One tap jumps them back to the newest message and re-engages auto-scroll. Same pattern as Slack or iMessage: quiet when you're caught up, helpful when you're not."
    )
    .user("Last one  does this work with assistive tech?")
    .sleep(1000)
    .assistant(
      '`MessageScrollerContent` sets `role="log"` and `aria-relevant="additions"` by default, so screen readers announce new messages as they stream in.\n\nThe scroll button is a real `<button>` with an sr-only label, and it's removed from the tab order when you're already at the bottom  no ghost focus stops.'
    );
  const initialMessages = script.get(0);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat({ messages: initialMessages, transport });
  const nextMessage = $derived(script.next(chat.messages));
  const isBusy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    if (!nextMessage || isBusy) {
      return;
    }
    void chat.sendMessage(nextMessage);
  }
</script>
<MessageScroller.Provider>
  <div class="relative flex flex-col gap-4">
    <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
      <Card.Header class="gap-1 border-b">
        <Card.Title>New Chat</Card.Title>
        <Card.Description>How can I help you today?</Card.Description>
        <Card.Action>
          <Tooltip.Root>
            <Tooltip.Trigger>
              {#snippet child({ props })}
                <Button
                  {...props}
                  variant="outline"
                  size="icon"
                  aria-label="Reset conversation"
                  onclick={() => (chat.messages = initialMessages)}
                  disabled={isBusy}
                >
                  <RotateCwIcon />
                </Button>
              {/snippet}
            </Tooltip.Trigger>
            <Tooltip.Content>
              <p>Reset</p>
            </Tooltip.Content>
          </Tooltip.Root>
        </Card.Action>
      </Card.Header>
      <Card.Content class="flex-1 overflow-hidden p-0">
        {#if chat.messages.length === 0}
          <Empty.Root class="h-full">
            <Empty.Header>
              <Empty.Media variant="icon">
                <MessageCircleDashedIcon />
              </Empty.Media>
              <Empty.Title>Morning, shadcn!</Empty.Title>
              <Empty.Description>
                What are we working on today? Press send to start a new
                conversation
              </Empty.Description>
            </Empty.Header>
          </Empty.Root>
        {:else}
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content
                aria-busy={isBusy}
                class="p-(--card-spacing)"
              >
                {#each chat.messages as message (message.id)}
                  <MessageAnimated
                    {message}
                    scrollAnchor={message.role === "user"}
                  />
                {/each}
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        {/if}
      </Card.Content>
      <Card.Footer class="flex-col gap-2">
        <form onsubmit={handleSubmit} class="w-full">
          <InputGroup.Root>
            <div class="h-14 w-full px-3 py-2.5">
              <span
                class="line-clamp-2 opacity-60 data-[status=ready]:opacity-100"
                data-status={chat.status}
              >
                {#if nextMessage}
                  {getMessageText(nextMessage)}
                {:else}
                  <span class="text-muted-foreground">
                    No messages queued. Reset the conversation.
                  </span>
                {/if}
              </span>
            </div>
            <InputGroup.Addon align="block-end" class="pt-1">
              <DropdownMenu.Root>
                <DropdownMenu.Trigger>
                  {#snippet child({ props })}
                    <InputGroup.Button
                      {...props}
                      aria-label="Add files"
                      type="button"
                      size="icon-sm"
                      variant="outline"
                    >
                      <PlusIcon />
                    </InputGroup.Button>
                  {/snippet}
                </DropdownMenu.Trigger>
                <DropdownMenu.Content align="start" side="top" class="w-44">
                  <DropdownMenu.Item>
                    <PaperclipIcon />
                    Add Photos & Files
                  </DropdownMenu.Item>
                  <DropdownMenu.Separator />
                  <DropdownMenu.Item>
                    <ImageIcon />
                    Create Image
                  </DropdownMenu.Item>
                  <DropdownMenu.Item>
                    <TelescopeIcon />
                    Deep Research
                  </DropdownMenu.Item>
                  <DropdownMenu.Item>
                    <GlobeIcon />
                    Web Search
                  </DropdownMenu.Item>
                </DropdownMenu.Content>
              </DropdownMenu.Root>
              <InputGroup.Button
                type="submit"
                variant="default"
                size="icon-sm"
                disabled={!nextMessage || isBusy}
                class="ml-auto"
              >
                <ArrowUpIcon />
                <span class="sr-only">Send</span>
              </InputGroup.Button>
            </InputGroup.Addon>
          </InputGroup.Root>
        </form>
      </Card.Footer>
    </Card.Root>
    <div class="px-0.5 text-center text-xs text-muted-foreground">
      Demo is read only. Press send to send messages.
    </div>
  </div>
</MessageScroller.Provider>
```

View Code

## [What Makes a Great Streaming Chat Experience](#what-makes-a-great-streaming-chat-experience)

Building a chat interface used to be simple. You create an inverted list with an input. Type a message, it appends at the bottom. When a reply comes in, the list grows and scrolls. Done.

Streaming breaks that model. Messages arrive in chunks while you may still be reading, scrolling, or looking somewhere else entirely.

Now the challenge is preserving the reader's place while the conversation keeps changing. Get that wrong and the experience feels jumpy: people are pulled to the bottom, lose context, and have to find their way back.

In practice, this comes down to scroll: when to follow, when to hold, and when to let the reader decide. A great streaming chat should:

1. 
   **Move only when the reader asked to move.**
   If someone is reading, don’t pull them somewhere else. Auto-scroll should never be the default.
2. 
   **Follow only while they’re following.**
   If they’re at the live edge, keep the stream in view. If they scroll away, leave them there.
3. 
   **Every interaction is a signal.**
   Scrolling is not the only one. Selecting text, using the keyboard, opening a link, or searching should all stop the interface from moving.
4. 
   **Start a new turn near the top of the viewport.**
   This gives the new turn somewhere it can be read from the beginning.
5. 
   **Then stream in the answer.**
   The answer should grow into the screen, not immediately push everything away.
6. 
   **Keep part of the previous conversation in context.**
   The prompt and reply should stay visually connected, and enough of the previous turn should remain visible so the reader knows where they are.
7. 
   **Let new content arrive offscreen.**
   The conversation can keep streaming without changing what the reader is looking at.
8. 
   **Show what’s happening out of view.**
   Make it clear when a response is still streaming or when new messages have arrived.
9. 
   **Make it easy to return to the latest reply.**
   A Jump to latest action should bring the reader back and resume following.
10. 
    **Let people jump anywhere in the conversation.**
    Long threads need message links, search, unread markers, and direct navigation.
11. 
    **Reopen where the reader left off.**
    A saved conversation should open at the last meaningful turn. Often this is the last user message. Not the absolute bottom.
12. 
    **Keep the reader’s place when layout changes.**
    Images load. Markdown expands. Code blocks render. Older messages appear above. None of that should make the reader lose their place.
13. 
    **Handle interruptions without stealing position.**
    Stopping, retrying, regenerating, branching, or errors should not unexpectedly move the conversation.
14. 
    **Stay responsive in long threads.**
    Streaming text, markdown, code, images, and long history should still feel responsive.
15. 
    **Be accessible without the noise.**
    Keep the transcript navigable, preserve keyboard focus, and announce important events at a comfortable pace.

**Never move the reader against their intent.**

## [MessageScroller](#messagescroller)

MessageScroller is a chat transcript scroller built for these behaviors. `MessageScroller.Provider` owns the scroll state and transcript-row behavior: opening position, streamed output, new-turn anchoring, prepended history, visibility, and scroll controls. `MessageScroller.Root` is the styled frame that renders inside it.

MessageScroller is scoped to the scroll viewport. It does not own messages, AI state, transport, persistence, branching, or model state. Your product code stays focused on composing messages, markers, tools, attachments, and prompt inputs.

It gives you the scroll behavior that chat needs, without taking over the rest of the chat UI. And it stays fast, even in long conversations with rich markdown.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add message-scroller
```

```bash
npx shadcn-svelte@latest add message-scroller
```

```bash
bun x shadcn-svelte@latest add message-scroller
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Message from "$lib/components/ui/message/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
</script>
```

```svelte
<MessageScroller.Provider>
  <MessageScroller.Root>
    <MessageScroller.Viewport>
      <MessageScroller.Content>
        {#each messages as message (message.id)}
          <MessageScroller.Item
            messageId={message.id}
            scrollAnchor={message.role === "user"}
          >
            <Message.Root />
          </MessageScroller.Item>
        {/each}
      </MessageScroller.Content>
    </MessageScroller.Viewport>
    <MessageScroller.Button />
  </MessageScroller.Root>
</MessageScroller.Provider>
``` `MessageScroller` fills its parent, so place it inside a height-constrained container.

```svelte
<div class="flex h-screen flex-col">
  <MessageScroller.Provider>
    <MessageScroller.Root class="flex-1">
    </MessageScroller.Root>
  </MessageScroller.Provider>
</div>
```

## [Composition](#composition)

```svelte
<MessageScroller.Provider>
  <MessageScroller.Root>
    <MessageScroller.Viewport>
      <MessageScroller.Content>
        <MessageScroller.Item>
        </MessageScroller.Item>
        <MessageScroller.Item />
        <MessageScroller.Item />
      </MessageScroller.Content>
    </MessageScroller.Viewport>
    <MessageScroller.Button />
  </MessageScroller.Root>
</MessageScroller.Provider>
```

- **`MessageScroller.Provider`**  the headless root. Owns scroll state and the behavior props for opening position, auto-scroll, anchoring, scroll commands, and visibility tracking.
- **`MessageScroller.Root`**  the styled frame. Lays out the viewport, content, and controls inside the provider.
- **`MessageScroller.Viewport`**  the scrollable element. Receives native scroll events and preserves the visible row when older messages are prepended.
- **`MessageScroller.Content`**  the transcript container. Holds the rows and provides the live-region defaults for new messages.
- **`MessageScroller.Item`**  the transcript row boundary. Wrap every direct child of the content so the scroller can measure, anchor, preserve position, track visibility, and jump to it. An item can be a message, marker, typing indicator, separator, join/leave event, or "load earlier" row.
- **`MessageScroller.Button`**  the scroll control. Scrolls to the start or end of the transcript and is inert until there is content in its direction.

## [Core Concepts](#core-concepts)

### [Anchoring Turns](#anchoring-turns)

A turn is the part of the conversation that starts a new exchange. In a simple AI chat, that is usually the user's message and the assistant reply that follows.

An anchor is the row the viewport should treat as the start of that turn. Mark that row with `scrollAnchor`. When a new anchor is appended, the viewport moves it near the top and keeps a peek of the previous item above it, so the new turn does not feel detached from its context.

```svelte

<MessageScroller.Item
  messageId={message.id}
  scrollAnchor={message.role === "user"}
/>
```

Scroll anchors are not tied to message role. You can turn any row into an anchor: a user message, a system marker, a handoff event, or anything else that starts a meaningful turn. `MessageScroller` only needs to know which row should anchor the viewport.

In the following example, the user's message is anchored. When you send a new message, the viewport anchors it near the top and appends the assistant reply below it. Toggle the anchor to the assistant's message to see the difference.

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import MessageCircleDashedIcon from "@lucide/svelte/icons/message-circle-dashed";
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Empty from "$lib/components/ui/empty/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
  import MessageAnimated from "$lib/components/message-animated.svelte";
  import { Button } from "$lib/components/ui/button/index.js";
  type AnchorRole = "user" | "assistant";
  type ChatMessage = {
    id: string;
    role: AnchorRole;
    text: string;
  };
  const scriptedMessages: ChatMessage[] = [
    {
      id: "anchor-1-user",
      role: "user",
      text: "Can you show me how anchoring behaves when a new prompt starts the turn?"
    },
    {
      id: "anchor-1-assistant",
      role: "assistant",
      text: "Append the user prompt first, then append the assistant response. With User selected, the prompt settles near the top and the assistant response fills in below it."
    },
    {
      id: "anchor-2-user",
      role: "user",
      text: "What changes when assistant messages are the anchor?"
    },
    {
      id: "anchor-2-assistant",
      role: "assistant",
      text: "Now each assistant response is the item `MessageScroller` keeps in view. This is useful when the reply is the moment you want readers to land on after each turn."
    },
    {
      id: "anchor-3-user",
      role: "user",
      text: "Can I switch roles and keep adding turns?"
    },
    {
      id: "anchor-3-assistant",
      role: "assistant",
      text: "Yes. The next appended message with the selected role becomes the anchor, so you can compare user and assistant anchoring without resetting the demo."
    }
 ];
  let anchorRole = $state<AnchorRole>("user");
  let messages = $state<ChatMessage[]>([]);
  let messageIndex = $state(0);
  const nextMessage = $derived(scriptedMessages[messageIndex]);
  function handleAnchorChange(value: string) {
    if (value === "user" || value === "assistant") {
      anchorRole = value;
      messages = [];
      messageIndex = 0;
    }
  }
  function sendNextMessage() {
    if (!nextMessage) {
      return;
    }
    messages = [...messages, nextMessage];
    messageIndex += 1;
  }
</script>
<div class="relative flex flex-col gap-4">
  <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
    <Card.Header class="border-b">
      <Card.Title>Anchoring Turns</Card.Title>
      <Card.Description
        >Choose which role settles near the top edge.</Card.Description
      >
      <Card.Action>
        <Button
          type="button"
          variant="outline"
          size="icon"
          aria-label="Reset anchored turns"
          disabled={messages.length === 0}
          onclick={() => {
            messages = [];
            messageIndex = 0;
          }}
        >
          <RotateCwIcon />
        </Button>
      </Card.Action>
    </Card.Header>
    <Card.Content class="min-h-0 flex-1 overflow-hidden p-0">
      {#if messages.length === 0}
        <Empty.Root class="h-full">
          <Empty.Header>
            <Empty.Media variant="icon">
              <MessageCircleDashedIcon />
            </Empty.Media>
            <Empty.Title>No anchored messages yet</Empty.Title>
            <Empty.Description>
              Send the first message to see the selected role anchor.
            </Empty.Description>
          </Empty.Header>
        </Empty.Root>
      {:else}
        <MessageScroller.Provider>
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content class="p-(--card-spacing)">
                {#each messages as message (message.id)}
                  <MessageAnimated
                    {message}
                    scrollAnchor={message.role === anchorRole}
                    userVariant="muted"
                    assistantVariant="ghost"
                  />
                {/each}
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        </MessageScroller.Provider>
      {/if}
    </Card.Content>
    <Card.Footer>
      <ToggleGroup.Root
        type="single"
        aria-label="Select scroll anchor role"
        bind:value={() => anchorRole, handleAnchorChange}
      >
        <ToggleGroup.Item value="user" aria-label="Anchor user messages"
          >User</ToggleGroup.Item
        >
        <ToggleGroup.Item
          value="assistant"
          aria-label="Anchor assistant messages"
        >
          Assistant
        </ToggleGroup.Item>
      </ToggleGroup.Root>
      <Button
        type="button"
        size="icon"
        class="ml-auto"
        disabled={!nextMessage}
        onclick={sendNextMessage}
      >
        <ArrowUpIcon />
        <span class="sr-only">Send Message</span>
      </Button>
    </Card.Footer>
  </Card.Root>
  <div
    class="mx-auto max-w-xs px-0.5 text-center text-xs text-muted-foreground"
  >
    Toggle the anchor role, then send messages to compare where turns settle.
  </div>
</div>
```

View Code

### [Group Chat](#group-chat)

In a group chat, the turn boundary is more specific than "the user message". It is often the message that asks the model to respond, or a marker like "Marcus joined the chat". Typing indicators and history controls usually should not anchor.

Because anchoring is role-independent, you can anchor a marker just as easily as a message.

```svelte
<MessageScroller.Item messageId="marcus-joined" scrollAnchor>
  <Marker.Root variant="separator">
    <Marker.Content>Marcus joined the chat</Marker.Content>
  </Marker.Root>
</MessageScroller.Item>
```

```svelte
<script lang="ts">
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Marker from "$lib/components/ui/marker/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const currentUser = "Grace";
  type GroupChatItem =
    | {
        id: string;
        type: "event";
        text: string;
        scrollAnchor?: boolean;
      }
    | {
        id: string;
        type: "message";
        sender: string;
        role: "assistant" | "participant";
        text: string;
        scrollAnchor?: boolean;
      };
  const initialItems: GroupChatItem[] = [
    {
      id: "group-1",
      type: "message",
      sender: "Grace",
      role: "participant",
      text: "@mary, the astrophage line keeps matching Venus energy output. Can you check my math?"
    },
    {
      id: "group-2",
      type: "message",
      sender: "Mary (Agent)",
      role: "assistant",
      text: "Yes. Confirmed. The curve points to a microorganism harvesting stellar energy and breeding near carbon dioxide. If @rocky agrees, this is the clue we need."
    },
    {
      id: "group-3",
      type: "message",
      sender: "Grace",
      role: "participant",
      text: "ping @rocky",
      scrollAnchor: true
    }
 ];
  const rockyMarker: GroupChatItem = {
    id: "group-4",
    type: "event",
    text: "Rocky has joined the chat",
    scrollAnchor: true
  };
  const rockyMessage: GroupChatItem = {
    id: "group-5",
    type: "message",
    sender: "Rocky",
    role: "participant",
    text: "Amaze. Astrophage eats light, makes heat, goes to carbon dioxide. Rocky has fuel model. Grace is smart."
  };
  let demoKey = $state(0);
  let rockyTurn = $state<"idle" | "marker" | "message">("idle");
  const items = $derived(
    rockyTurn === "message"
      ? [...initialItems, rockyMarker, rockyMessage]
      : rockyTurn === "marker"
        ? [...initialItems, rockyMarker]
        : initialItems
  );
  const buttonLabel = $derived(
    rockyTurn === "idle" ? "Add Rocky" : "Send Message as Rocky"
  );
  const isComplete = $derived(rockyTurn === "message");
</script>
<MessageScroller.Provider>
  <div class="relative flex flex-col gap-4">
    <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
      <Card.Header class="gap-1 border-b">
        <Card.Title>Group Chat</Card.Title>
        <Card.Description>
          A group chat with several participants and an assistant. The Marker is
          marked as a turn.
        </Card.Description>
        <Card.Action>
          <Tooltip.Root>
            <Tooltip.Trigger>
              {#snippet child({ props })}
                <Button
                  {...props}
                  type="button"
                  variant="outline"
                  size="icon"
                  aria-label="Reset conversation"
                  disabled={rockyTurn === "idle"}
                  onclick={() => {
                    rockyTurn = "idle";
                    demoKey += 1;
                  }}
                >
                  <RotateCwIcon />
                </Button>
              {/snippet}
            </Tooltip.Trigger>
            <Tooltip.Content>
              <p>Reset</p>
            </Tooltip.Content>
          </Tooltip.Root>
        </Card.Action>
      </Card.Header>
      <Card.Content class="min-h-0 flex-1 p-0">
        {#key demoKey}
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content class="p-(--card-spacing)">
                {#each items as item (item.id)}
                  {#if item.type === "message"}
                    {@const isCurrentUser = item.sender === currentUser}
                    {@const variant = isCurrentUser
                      ? "muted"
                      : item.role === "assistant"
                        ? "ghost"
                        : "tinted"}
                    <MessageScroller.Item
                      messageId={item.id}
                      scrollAnchor={item.scrollAnchor}
                    >
                      <Message.Root align={isCurrentUser ? "end" : "start"}>
                        <Message.Content>
                          {#if !isCurrentUser}
                            <Message.Header>{item.sender}</Message.Header>
                          {/if}
                          <Bubble.Root {variant}>
                            <Bubble.Content>{item.text}</Bubble.Content>
                          </Bubble.Root>
                        </Message.Content>
                      </Message.Root>
                    </MessageScroller.Item>
                  {:else}
                    <MessageScroller.Item scrollAnchor={item.scrollAnchor}>
                      <Marker.Root variant="separator">
                        <Marker.Content>{item.text}</Marker.Content>
                      </Marker.Root>
                    </MessageScroller.Item>
                  {/if}
                {/each}
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        {/key}
      </Card.Content>
      <Card.Footer class="flex flex-col items-center gap-2 border-t">
        <Button
          type="button"
          disabled={isComplete}
          onclick={() =>
            (rockyTurn = rockyTurn === "idle" ? "marker" : "message")}
          class="w-full"
          variant="secondary"
        >
          {buttonLabel}
        </Button>
        <p class="text-xs text-muted-foreground">
          {rockyTurn === "idle"
            ? "This will create a marker and make it the anchor"
            : "Now send Rocky's reply into the conversation"}
        </p>
      </Card.Footer>
    </Card.Root>
    <div
      class="mx-auto max-w-sm px-0.5 text-center text-xs text-balance text-muted-foreground"
    >
      When a user joins, a marker is created. scrollAnchor on the marker marks
      it as the next turn
    </div>
  </div>
</MessageScroller.Provider>
```

View Code

### [Keeping Context Visible](#keeping-context-visible)

When a new turn starts, it should still feel like part of the same continuous thread. `scrollPreviousItemPeek` keeps a slice of the previous item visible above the anchor, so the reader keeps their context instead of feeling like the conversation restarted on a blank page.

```svelte

<MessageScroller.Provider scrollPreviousItemPeek={64}>
  <MessageScroller.Root>
  </MessageScroller.Root>
</MessageScroller.Provider>
```

Adjust the peek amount in the example below to see how it affects the conversation.

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import GlobeIcon from "@lucide/svelte/icons/globe";
  import ImageIcon from "@lucide/svelte/icons/image";
  import PaperclipIcon from "@lucide/svelte/icons/paperclip";
  import PlusIcon from "@lucide/svelte/icons/plus";
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import TelescopeIcon from "@lucide/svelte/icons/telescope";
  import { Chat } from "@ai-sdk/svelte";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import MessageAnimated from "$lib/components/message-animated.svelte";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Slider } from "$lib/components/ui/slider/index.js";
  const DEFAULT_PEEK = 64;
  const script = createChat()
    .user(
      "I'm building a chat for our app and the scroll behavior is driving me nuts. Every time the AI streams a reply, the whole thread jumps around."
    )
    .sleep(1000)
    .assistant(
      "That's the classic streaming scroll problem. Wrap your message list in `MessageScroller` and turn on `autoScroll`  the viewport pins to the bottom as tokens arrive, so users always see the latest text land in place.\n\nThe important part: it only auto-scrolls while the reader is already at the bottom. The moment they scroll up to read something earlier, auto-scroll backs off and their position is preserved. You get smooth streaming without fighting the user's intent."
    )
    .user(
      "Okay, but when someone sends a new message the view still feels jarring  like the whole conversation reloads from the top."
    )
    .sleep(1000)
    .assistant(
      "MessageScrollerItem fixes that with turn anchoring. Set `scrollAnchor` on the turn that should settle near the top instead of blindly snapping to the document bottom.\n\nIt also leaves a small peek of the previous exchange visible above the anchor, so context isn't lost. The reply starts in view without that disorienting jump you get from a plain overflow container."
    )
    .user(
      "And if they've scrolled up to re-read an older answer? I don't want to yank them back down."
    )
    .sleep(1000)
    .assistant(
      "You won't. Auto-scroll only runs when the viewport is already pinned to the bottom, so scrolling up is a deliberate opt-out  their place in the thread stays put even as new tokens keep arriving below.\n\nWhen there is content they haven't seen yet, `MessageScrollerButton` appears at the bottom of the viewport. One tap jumps them back to the newest message and re-engages auto-scroll. Same pattern as Slack or iMessage: quiet when you're caught up, helpful when you're not."
    )
    .user("Last one  does this work with assistive tech?")
    .sleep(1000)
    .assistant(
      '`MessageScrollerContent` sets `role="log"` and `aria-relevant="additions"` by default, so screen readers announce new messages as they stream in.\n\nThe scroll button is a real `<button>` with an sr-only label, and it's removed from the tab order when you're already at the bottom  no ghost focus stops.'
    );
  const initialMessages = script.get(2);
  const transport = script.transport({ delayMs: 35 });
  const chat = new Chat({ messages: initialMessages, transport });
  const nextMessage = $derived(script.next(chat.messages));
  const isBusy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  let demoKey = $state(0);
  let peek = $state(DEFAULT_PEEK);
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    if (!nextMessage || isBusy) {
      return;
    }
    void chat.sendMessage(nextMessage);
  }
  function reset() {
    chat.messages = initialMessages;
    peek = DEFAULT_PEEK;
    demoKey += 1;
  }
</script>
{#key demoKey}
  <MessageScroller.Provider scrollMargin={24} scrollPreviousItemPeek={peek}>
    <div class="relative flex flex-col gap-4">
      <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
        <Card.Header class="gap-1 border-b">
          <Card.Title>Keeping Context Visible</Card.Title>
          <Card.Description
            >New turns keep part of the previous reply in view.</Card.Description
          >
          <Card.Action>
            <Tooltip.Root>
              <Tooltip.Trigger>
                {#snippet child({ props })}
                  <Button
                    {...props}
                    variant="outline"
                    size="icon"
                    aria-label="Reset context example"
                    disabled={isBusy}
                    onclick={reset}
                  >
                    <RotateCwIcon />
                  </Button>
                {/snippet}
              </Tooltip.Trigger>
              <Tooltip.Content>
                <p>Reset</p>
              </Tooltip.Content>
            </Tooltip.Root>
          </Card.Action>
        </Card.Header>
        <Card.Content class="flex-1 overflow-hidden p-0">
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content
                aria-busy={isBusy}
                class="p-(--card-spacing)"
              >
                {#each chat.messages as message (message.id)}
                  <MessageAnimated
                    {message}
                    scrollAnchor={message.role === "user"}
                  />
                {/each}
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        </Card.Content>
        <Card.Footer class="flex-col gap-2">
          <form onsubmit={handleSubmit} class="w-full">
            <InputGroup.Root>
              <div class="h-14 w-full px-3 py-2.5">
                <span
                  class="line-clamp-2 opacity-60 data-[status=ready]:opacity-100"
                  data-status={chat.status}
                >
                  {#if nextMessage}
                    {getMessageText(nextMessage)}
                  {:else}
                    <span class="text-muted-foreground">
                      No messages queued. Reset the context.
                    </span>
                  {/if}
                </span>
              </div>
              <InputGroup.Addon align="block-end" class="pt-1">
                <DropdownMenu.Root>
                  <DropdownMenu.Trigger>
                    {#snippet child({ props })}
                      <InputGroup.Button
                        {...props}
                        aria-label="Add files"
                        type="button"
                        size="icon-sm"
                        variant="outline"
                      >
                        <PlusIcon />
                      </InputGroup.Button>
                    {/snippet}
                  </DropdownMenu.Trigger>
                  <DropdownMenu.Content align="start" side="top" class="w-44">
                    <DropdownMenu.Item>
                      <PaperclipIcon />
                      Add Photos & Files
                    </DropdownMenu.Item>
                    <DropdownMenu.Separator />
                    <DropdownMenu.Item>
                      <ImageIcon />
                      Create Image
                    </DropdownMenu.Item>
                    <DropdownMenu.Item>
                      <TelescopeIcon />
                      Deep Research
                    </DropdownMenu.Item>
                    <DropdownMenu.Item>
                      <GlobeIcon />
                      Web Search
                    </DropdownMenu.Item>
                  </DropdownMenu.Content>
                </DropdownMenu.Root>
                <div class="flex w-28 items-center gap-2">
                  <span class="text-xs text-muted-foreground tabular-nums"
                    >{peek}px</span
                  >
                  <Slider
                    type="single"
                    aria-label="Previous context peek"
                    bind:value={peek}
                    min={64}
                    max={128}
                    step={1}
                    disabled={isBusy}
                  />
                </div>
                <InputGroup.Button
                  type="submit"
                  variant="default"
                  size="icon-sm"
                  disabled={!nextMessage || isBusy}
                  class="ml-auto"
                >
                  <ArrowUpIcon />
                  <span class="sr-only">Send</span>
                </InputGroup.Button>
              </InputGroup.Addon>
            </InputGroup.Root>
          </form>
        </Card.Footer>
      </Card.Root>
      <div class="px-0.5 text-center text-xs text-muted-foreground">
        Adjust the slider and send. Observe the previous message peak
      </div>
    </div>
  </MessageScroller.Provider>
{/key}
```

View Code

### [Following the Live Edge](#following-the-live-edge)

When the reader is at the live edge, either because they stayed there or returned there, `autoScroll` keeps streamed replies in view as they grow. Scrolling away from the live edge releases the view, whether by wheel, touch, keyboard scroll keys, or dragging the scrollbar. An explicit message jump releases it too. New chunks can then arrive without moving the reader. `autoScroll` composes with turn anchoring. When a new turn anchors near the top, the view stays put while the reply streams into the room below it. Once the reply fills the viewport, the reader is back at the live edge and follow-output takes over from the anchor.

```svelte
<MessageScroller.Provider autoScroll>
  <MessageScroller.Root>
  </MessageScroller.Root>
</MessageScroller.Provider>
```

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import GlobeIcon from "@lucide/svelte/icons/globe";
  import ImageIcon from "@lucide/svelte/icons/image";
  import MessageCircleDashedIcon from "@lucide/svelte/icons/message-circle-dashed";
  import PaperclipIcon from "@lucide/svelte/icons/paperclip";
  import PlusIcon from "@lucide/svelte/icons/plus";
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import TelescopeIcon from "@lucide/svelte/icons/telescope";
  import { Chat } from "@ai-sdk/svelte";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as Empty from "$lib/components/ui/empty/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import MessageAnimated from "$lib/components/message-animated.svelte";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const script = createChat()
    .user(
      "I'm building a chat for our app and the scroll behavior is driving me nuts. Every time the AI streams a reply, the whole thread jumps around."
    )
    .sleep(1000)
    .assistant(
      "That's the classic streaming scroll problem. Wrap your message list in `MessageScroller` and turn on `autoScroll`  the viewport pins to the bottom as tokens arrive, so users always see the latest text land in place.\n\nThe important part: it only auto-scrolls while the reader is already at the bottom. The moment they scroll up to read something earlier, auto-scroll backs off and their position is preserved. You get smooth streaming without fighting the user's intent."
    )
    .user(
      "Okay, but when someone sends a new message the view still feels jarring  like the whole conversation reloads from the top."
    )
    .sleep(1000)
    .assistant(
      "MessageScrollerItem fixes that with turn anchoring. Set `scrollAnchor` on the turn that should settle near the top instead of blindly snapping to the document bottom.\n\nIt also leaves a small peek of the previous exchange visible above the anchor, so context isn't lost. The reply starts in view without that disorienting jump you get from a plain overflow container."
    )
    .user(
      "And if they've scrolled up to re-read an older answer? I don't want to yank them back down."
    )
    .sleep(1000)
    .assistant(
      "You won't. Auto-scroll only runs when the viewport is already pinned to the bottom, so scrolling up is a deliberate opt-out  their place in the thread stays put even as new tokens keep arriving below.\n\nWhen there is content they haven't seen yet, `MessageScrollerButton` appears at the bottom of the viewport. One tap jumps them back to the newest message and re-engages auto-scroll. Same pattern as Slack or iMessage: quiet when you're caught up, helpful when you're not."
    )
    .user("Last one  does this work with assistive tech?")
    .sleep(1000)
    .assistant(
      '`MessageScrollerContent` sets `role="log"` and `aria-relevant="additions"` by default, so screen readers announce new messages as they stream in.\n\nThe scroll button is a real `<button>` with an sr-only label, and it's removed from the tab order when you're already at the bottom  no ghost focus stops.'
    );
  const initialMessages = script.get(0);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat({ messages: initialMessages, transport });
  const nextMessage = $derived(script.next(chat.messages));
  const isBusy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    if (!nextMessage || isBusy) {
      return;
    }
    void chat.sendMessage(nextMessage);
  }
</script>
<MessageScroller.Provider autoScroll>
  <div class="relative flex flex-col gap-4">
    <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
      <Card.Header class="gap-1 border-b">
        <Card.Title>Streaming Messages</Card.Title>
        <Card.Description
          >Auto-scroll follows the live edge of the conversation.</Card.Description
        >
        <Card.Action>
          <Tooltip.Root>
            <Tooltip.Trigger>
              {#snippet child({ props })}
                <Button
                  {...props}
                  variant="outline"
                  size="icon"
                  aria-label="Reset stream"
                  onclick={() => (chat.messages = initialMessages)}
                  disabled={chat.messages.length === 0 || isBusy}
                >
                  <RotateCwIcon />
                </Button>
              {/snippet}
            </Tooltip.Trigger>
            <Tooltip.Content>
              <p>Reset</p>
            </Tooltip.Content>
          </Tooltip.Root>
        </Card.Action>
      </Card.Header>
      <Card.Content class="flex-1 overflow-hidden p-0">
        {#if chat.messages.length === 0}
          <Empty.Root class="h-full">
            <Empty.Header>
              <Empty.Media variant="icon">
                <MessageCircleDashedIcon />
              </Empty.Media>
              <Empty.Title>Ready to Stream</Empty.Title>
              <Empty.Description
                >Press send to stream a scripted launch summary.</Empty.Description
              >
            </Empty.Header>
          </Empty.Root>
        {:else}
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content
                aria-busy={isBusy}
                class="p-(--card-spacing)"
              >
                {#each chat.messages as message (message.id)}
                  <MessageAnimated
                    {message}
                    scrollAnchor={message.role === "user"}
                  />
                {/each}
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        {/if}
      </Card.Content>
      <Card.Footer class="flex-col gap-2">
        <form onsubmit={handleSubmit} class="w-full">
          <InputGroup.Root>
            <div class="h-14 w-full px-3 py-2.5">
              <span
                class="line-clamp-2 opacity-60 data-[status=ready]:opacity-100"
                data-status={chat.status}
              >
                {#if nextMessage}
                  {getMessageText(nextMessage)}
                {:else}
                  <span class="text-muted-foreground">
                    No messages queued. Reset the stream.
                  </span>
                {/if}
              </span>
            </div>
            <InputGroup.Addon align="block-end" class="pt-1">
              <DropdownMenu.Root>
                <DropdownMenu.Trigger>
                  {#snippet child({ props })}
                    <InputGroup.Button
                      {...props}
                      aria-label="Add files"
                      type="button"
                      size="icon-sm"
                      variant="outline"
                    >
                      <PlusIcon />
                    </InputGroup.Button>
                  {/snippet}
                </DropdownMenu.Trigger>
                <DropdownMenu.Content align="start" side="top" class="w-44">
                  <DropdownMenu.Item>
                    <PaperclipIcon />
                    Add Photos & Files
                  </DropdownMenu.Item>
                  <DropdownMenu.Separator />
                  <DropdownMenu.Item>
                    <ImageIcon />
                    Create Image
                  </DropdownMenu.Item>
                  <DropdownMenu.Item>
                    <TelescopeIcon />
                    Deep Research
                  </DropdownMenu.Item>
                  <DropdownMenu.Item>
                    <GlobeIcon />
                    Web Search
                  </DropdownMenu.Item>
                </DropdownMenu.Content>
              </DropdownMenu.Root>
              <InputGroup.Button
                type="submit"
                variant="default"
                size="icon-sm"
                disabled={!nextMessage || isBusy}
                class="ml-auto"
              >
                <ArrowUpIcon />
                <span class="sr-only">Send</span>
              </InputGroup.Button>
            </InputGroup.Addon>
          </InputGroup.Root>
        </form>
      </Card.Footer>
    </Card.Root>
    <div class="px-0.5 text-center text-xs text-muted-foreground">
      Streaming is simulated. `autoScroll` is enabled.
    </div>
  </div>
</MessageScroller.Provider>
```

View Code

Calling `scrollToEnd`, or pressing `MessageScroller.Button`, re-engages follow-output when `autoScroll` is enabled, so a reader who scrolled away can return to the live edge and keep following. The root and viewport expose `data-autoscrolling` while that programmatic scroll to the latest message runs, so you can conditionally apply styles during the transition.

### [Opening Saved Threads](#opening-saved-threads)

It can seem reasonable to reopen a saved thread at the absolute end of the transcript, but that often drops the reader into the conversation without enough context. A better default is `"last-anchor"`: show the last meaningful turn, like the user's latest message, with the reply below it.

That gives the reader an immediate place in the thread. They can see what they asked, where the answer starts, and continue from there without reconstructing the conversation from the bottom edge.

```svelte
<MessageScroller.Provider defaultScrollPosition="last-anchor">
  <MessageScroller.Root>
  </MessageScroller.Root>
</MessageScroller.Provider>
``` `"last-anchor"` is keyed on `scrollAnchor`, not message role. If no anchor exists, or the last anchored turn already fits in the viewport, it falls back to `"end"`.

Use `"start"` when you want to resume at the beginning of a conversation, or `"end"` when the absolute latest message is the right place to land.

### [Avoiding a Flash on Reload](#avoiding-a-flash-on-reload)

A scroll container always opens at the top. HTML has no way to set `scrollTop`, so a server-rendered transcript shows the oldest messages first. After JavaScript runs, `defaultScrollPosition` moves the view, and you see a jump.

When `defaultScrollPosition` is `"end"` or `"last-anchor"`, the viewport has `data-pending-scroll` until that position is applied. The styled viewport stays hidden while the attribute is present, so you see the frame instead of the jump. `"start"` does not need this.

If you want `"end"` visible on first paint, add an inline script right after the viewport. Give the viewport an `id`, scroll it to the bottom, and remove `data-pending-scroll`.

```svelte
<script>
  const scrollToEndScript = `(function () {
    var viewport = document.getElementById("messages")
    if (!viewport) {
      return
    }
    viewport.scrollTop = viewport.scrollHeight
    viewport.removeAttribute("data-pending-scroll")
  })()`;
</script>
<MessageScroller.Root>
  <MessageScroller.Viewport id="messages">
    <MessageScroller.Content>
    </MessageScroller.Content>
  </MessageScroller.Viewport>
  {@html `<script>${scrollToEndScript}</script>`}
  <MessageScroller.Button />
</MessageScroller.Root>
```

Put the script in your page, not in the scroller. It only works for `"end"`, and only when the messages are already in the HTML. If you use a Content Security Policy, pass a `nonce`.

Do not use this script with `"last-anchor"`. Skip it when messages load on the client.

### [Loading Earlier Messages](#loading-earlier-messages)

Loading earlier messages should not move the conversation the reader is already looking at. When older rows are prepended above the current transcript, `MessageScroller.Viewport` preserves the visible row so the reader stays in the same place while history loads above them.

This is enabled by default through `preserveScrollOnPrepend`.

```svelte
<script lang="ts">
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import { toast } from "svelte-sonner";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Marker from "$lib/components/ui/marker/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const script = createChat()
    .user("Can you summarize the incident channel?")
    .assistant(
      "The first alert was a delayed export job. It started backing up around 09:42 UTC and triggered the warning once the retry queue crossed the threshold.\n\nNo customer-facing checkout paths were affected, but exports for larger workspaces were running about 12 minutes behind."
    )
    .user("Was checkout affected?")
    .assistant(
      "No checkout errors were reported. Payment authorization, order creation, and confirmation emails stayed inside their normal latency bands.\n\nThe only elevated metric was export queue depth, which maps to analytics downloads instead of checkout."
    )
    .user("What changed in the last deploy?")
    .assistant(
      "Only the export queue worker changed. The deploy moved large CSV jobs onto the shared retry policy, which made each failed attempt hold a worker slot longer than before.\n\nThe app deploy did not include checkout, pricing, or billing API changes."
    )
    .user("Do we need to roll back?")
    .assistant(
      "Not yet. Queue depth is recovering after we reduced retry concurrency, and the oldest pending job is now under five minutes old.\n\nKeep rollback ready if the queue starts climbing again, but the current trend points toward recovery."
    )
    .user("Keep watching for customer-visible issues.")
    .assistant(
      "I will watch the queue and support tags for another 15 minutes. I am tracking export failures, delayed download requests, and any support thread that mentions missing reports.\n\nIf those stay quiet through the next batch window, we can close this as an internal degradation."
    );
  const history = script.get();
  const INITIAL_VISIBLE_COUNT = 5;
  let demoKey = $state(0);
  let visibleCount = $state(INITIAL_VISIBLE_COUNT);
  const visibleMessages = $derived(history.slice(-visibleCount));
  const canLoadHistory = $derived(visibleCount < history.length);
</script>
<MessageScroller.Provider>
  <div class="relative flex flex-col gap-4">
    <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
      <Card.Header class="gap-1 border-b">
        <Card.Title>Load History</Card.Title>
        <Card.Description>Prepended messages keep your place.</Card.Description>
        <Card.Action>
          <Tooltip.Root>
            <Tooltip.Trigger>
              {#snippet child({ props })}
                <Button
                  {...props}
                  type="button"
                  variant="outline"
                  size="icon"
                  aria-label="Reset loaded messages"
                  disabled={visibleCount === INITIAL_VISIBLE_COUNT}
                  onclick={() => {
                    visibleCount = INITIAL_VISIBLE_COUNT;
                    demoKey += 1;
                  }}
                >
                  <RotateCwIcon />
                </Button>
              {/snippet}
            </Tooltip.Trigger>
            <Tooltip.Content>
              <p>Reset</p>
            </Tooltip.Content>
          </Tooltip.Root>
        </Card.Action>
      </Card.Header>
      <Card.Content class="flex-1 overflow-hidden p-0">
        {#key demoKey}
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content class="p-(--card-spacing)">
                {#each visibleMessages as message (message.id)}
                  {@const isUserMessage = message.role === "user"}
                  {@const paragraphs = getMessageText(message)
                    .split(/\ns*\n/)
                    .map((paragraph: string) => paragraph.trim())
                    .filter(Boolean)}
                  <MessageScroller.Item messageId={message.id}>
                    <Message.Root align={isUserMessage ? "end" : "start"}>
                      <Message.Content>
                        <Bubble.Root
                          variant={isUserMessage ? "muted" : "ghost"}
                        >
                          <Bubble.Content class="space-y-2">
                            {#each paragraphs as paragraph, index (`${message.id}-${index}`)}
                              <p class="whitespace-pre-wrap">{paragraph}</p>
                            {/each}
                          </Bubble.Content>
                        </Bubble.Root>
                      </Message.Content>
                    </Message.Root>
                  </MessageScroller.Item>
                {/each}
                <MessageScroller.Item scrollAnchor={false}>
                  <Marker.Root variant="separator">
                    <Marker.Content>End of Conversation</Marker.Content>
                  </Marker.Root>
                </MessageScroller.Item>
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        {/key}
      </Card.Content>
      <Card.Footer class="flex flex-col items-center gap-2 border-t">
        <Button
          type="button"
          disabled={!canLoadHistory}
          onclick={() => {
            visibleCount = history.length;
            toast("History loaded", {
              description: "Scroll up to see earlier messages."
            });
          }}
          class="w-full"
          variant="secondary"
        >
          {canLoadHistory ? "Load History" : "History Loaded"}
        </Button>
        <p class="text-xs text-muted-foreground">
          Restore earlier messages while keeping your place.
        </p>
      </Card.Footer>
    </Card.Root>
    <div
      class="mx-auto max-w-sm px-0.5 text-center text-xs text-balance text-muted-foreground"
    >
      Click Load History to load the entire conversation
    </div>
  </div>
</MessageScroller.Provider>
```

View Code

Use stable `messageId` values for message rows. That gives the scroller a specific row to preserve instead of guessing from whichever pixel happens to sit at the viewport edge.

### [Animating New Messages](#animating-new-messages) `MessageScroller.Item` can be animated directly. Keep `messageId` and `scrollAnchor` on it, and use transform and opacity for the entrance.

A common chat pattern is to animate the user's message when it is sent, then let the assistant reply stream into a regular row below it. Start the user row below its final position so it feels like it rises from the live edge of the viewport.

```svelte
<MessageScroller.Item
  class="animate-in fade-in slide-in-from-bottom-2 duration-300"
  messageId={message.id}
  scrollAnchor
/>
```

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import MessageCircleDashedIcon from "@lucide/svelte/icons/message-circle-dashed";
  import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
  import { Chat } from "@ai-sdk/svelte";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Empty from "$lib/components/ui/empty/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import * as Select from "$lib/components/ui/select/index.js";
  import MessageAnimated from "$lib/components/message-animated.svelte";
  import { createChat } from "$lib/ai-sdk.js";
  import {
    MESSAGE_ANIMATIONS,
    type MessageAnimationId
  } from "$lib/message-animations.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const script = createChat()
    .user("Can user messages pop in like iMessage without breaking anchoring?")
    .sleep(1000)
    .assistant(
      "Yes. Animate the user row with transform and opacity, and let the assistant response stream normally below it.\n\nThat keeps the row measurement predictable while still giving the newly sent bubble a more tactile entrance."
    )
    .user("What makes the animation feel more like iMessage?")
    .sleep(1000)
    .assistant(
      "Use a quick spring from the trailing edge: a little scale, a small upward move, and no layout animation.\n\nThe bubble feels tactile, but the measured row stays predictable, so anchoring and auto-scroll do not have to fight a changing layout."
    )
    .user("Can I switch between presets while testing the same thread?")
    .sleep(1000)
    .assistant(
      "Yes. Keep the conversation in place while you change the preset, then send the next message to compare the new entrance against the same context.\n\nThat makes it easier to judge the difference between a subtle fade, a snappy pop, and a more dramatic 3D tilt without rebuilding the scenario each time."
    );
  const initialMessages = script.get(0);
  const transport = script.transport({ delayMs: 15 });
  const chat = new Chat({ messages: initialMessages, transport });
  const nextMessage = $derived(script.next(chat.messages));
  const isBusy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  let presetId = $state<MessageAnimationId>("fade");
  const preset = $derived(MESSAGE_ANIMATIONS[presetId]);
</script>
<div class="relative flex flex-col gap-4">
  <Card.Root class="mx-auto h-140 w-full max-w-sm gap-0">
    <Card.Header class="border-b">
      <Card.Title>Animation</Card.Title>
      <Card.Description>
        Choose how user messages are animated when they are added to the
        conversation.
      </Card.Description>
      <Card.Action class="flex items-center gap-2">
        <Button
          type="button"
          variant="outline"
          size="icon"
          aria-label="Reset animated messages"
          disabled={chat.messages.length === 0 || isBusy}
          onclick={() => (chat.messages = initialMessages)}
        >
          <RotateCwIcon />
        </Button>
      </Card.Action>
    </Card.Header>
    <Card.Content class="min-h-0 flex-1 overflow-hidden p-0">
      {#if chat.messages.length === 0}
        <Empty.Root class="h-full">
          <Empty.Header>
            <Empty.Media variant="icon">
              <MessageCircleDashedIcon />
            </Empty.Media>
            <Empty.Title>No Messages Yet</Empty.Title>
            <Empty.Description
              >Click the button below to send the first message.</Empty.Description
            >
          </Empty.Header>
        </Empty.Root>
      {:else}
        <MessageScroller.Provider>
          <MessageScroller.Root>
            <MessageScroller.Viewport>
              <MessageScroller.Content
                aria-busy={isBusy}
                class="p-(--card-spacing)"
              >
                {#each chat.messages as message (message.id)}
                  <MessageAnimated
                    {message}
                    animationPreset={preset}
                    userVariant="muted"
                    assistantVariant="ghost"
                  />
                {/each}
              </MessageScroller.Content>
            </MessageScroller.Viewport>
            <MessageScroller.Button />
          </MessageScroller.Root>
        </MessageScroller.Provider>
      {/if}
    </Card.Content>
    <Card.Footer class="border-t">
      <Select.Root type="single" bind:value={presetId}>
        <Select.Trigger aria-label="Animation preset"
          >{preset.name}</Select.Trigger
        >
        <Select.Content align="start" side="top">
          <Select.Group>
            {#each Object.values(MESSAGE_ANIMATIONS) as animation (animation.id)}
              <Select.Item value={animation.id} label={animation.name}
                >{animation.name}</Select.Item
              >
            {/each}
          </Select.Group>
        </Select.Content>
      </Select.Root>
      <Button
        type="button"
        size="icon"
        class="ml-auto"
        disabled={!nextMessage || isBusy}
        onclick={() => {
          if (!nextMessage || isBusy) {
            return;
          }
          void chat.sendMessage(nextMessage);
        }}
      >
        <ArrowUpIcon />
        <span class="sr-only">Send Message</span>
      </Button>
    </Card.Footer>
  </Card.Root>
  <div
    class="mx-auto max-w-sm px-0.5 text-center text-xs text-balance text-muted-foreground"
  >
    Select an animation then click send to see it in action.
  </div>
</div>
```

View Code

Avoid animating height, margin, or padding for row entrances; those changes can fight the scroller's positioning work. If the reader prefers reduced motion, skip the entrance animation and keep the scroll behavior the same.

### [Jumping to Messages](#jumping-to-messages)

Search results, permalinks, outline items, and toolbar buttons often need to drive the transcript from outside the message list. Use `useMessageScroller` for those controls. Because the hooks read from `MessageScroller.Provider`, they work in any component inside the provider, including controls rendered outside the `MessageScroller.Root` frame.

```svelte
<script lang="ts">
  import { useMessageScroller } from "$lib/components/ui/message-scroller/index.js";
  const { scrollToMessage, scrollToEnd, scrollToStart } = useMessageScroller();
</script>
``` `scrollToMessage` targets the `messageId` on `MessageScroller.Item`, so rows that need to be addressable should have stable ids. `scrollToMessage` returns `false` when the target is not mounted and cannot be queued. `scrollToMessage` can queue a target before items exist, which covers client-resolved permalinks while the transcript mounts. After rows have mounted, a missing id returns `false` instead of starting a guessed retry loop. A `true` result means the scroll ran or was queued, not that the row is already in view.

### [Tracking the Reader's Position](#tracking-the-readers-position)

Use `useMessageScrollerVisibility` to track the reader's position in the conversation. A common example is a table-of-contents or a jump menu that highlights the current anchored turn.

```svelte
<script lang="ts">
  import { useMessageScrollerVisibility } from "$lib/components/ui/message-scroller/index.js";
  const visibility = useMessageScrollerVisibility();
</script>
``` `currentAnchorId` answers "where am I" by reporting the current anchored turn, and it stays set after that anchor scrolls above the viewport. `visibleMessageIds` answers "what is on screen", in document order.

Visibility is pay-for-what-you-use. Tracking only runs while something subscribes to `useMessageScrollerVisibility`, and rows need a `messageId` to participate.

### [Reading Scroll State](#reading-scroll-state)

Use `useMessageScrollerScrollable` when you need scroll state in JavaScript, such as a status indicator or a custom "jump to latest" control. It reports which edges the viewport can still scroll toward; "at the start/end" is the negation (`!start` / `!end`), and "scrollable at all" is `start || end`. For styling the scroller itself, prefer the `data-scrollable` attribute.

```svelte
<script lang="ts">
  import { useMessageScrollerScrollable } from "$lib/components/ui/message-scroller/index.js";
  const scrollable = useMessageScrollerScrollable();
</script>
```

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  import MessageAnimated from "$lib/components/message-animated.svelte";
  import ScrollStateFooter from "$lib/components/message-scroller/scrollable-footer.svelte";
  const messages = Array.from({ length: 12 }, (_, index) => ({
    id: `scrollable-${index + 1}`,
    role: index % 2 === 0 ? "user" : "assistant",
    text:
      index % 2 === 0
        ? `Review scroll checkpoint ${index + 1}.` : `Checkpoint ${index + 1} is synced. The scrollable hook updates as the viewport moves.\n\nWhen the reader is at the first message, the footer should only point them down. Once they move into the middle of the transcript, it should explain that both directions are available.\n\nAt the latest message, the footer should switch again and only point them back up.` })) satisfies Array<{
    id: string;
    role: "user" | "assistant";
    text: string;
  }>;
</script>
<div class="mx-auto flex w-full max-w-sm flex-col gap-4">
  <Card.Root class="h-140 w-full gap-0 overflow-hidden">
    <Card.Header class="gap-1 border-b">
      <Card.Title>Scroll Status</Card.Title>
      <Card.Description>
        Where the reader can go scroll to based on current scroll position.
      </Card.Description>
    </Card.Header>
    <MessageScroller.Provider defaultScrollPosition="start">
      <Card.Content class="flex-1 overflow-hidden p-0">
        <MessageScroller.Root>
          <MessageScroller.Viewport>
            <MessageScroller.Content class="gap-4 p-(--card-spacing)">
              {#each messages as message (message.id)}
                <MessageAnimated
                  {message}
                  scrollAnchor={message.role === "user"}
                  userVariant="muted"
                  assistantVariant="ghost"
                />
              {/each}
            </MessageScroller.Content>
          </MessageScroller.Viewport>
          <MessageScroller.Button />
        </MessageScroller.Root>
      </Card.Content>
      <ScrollStateFooter />
    </MessageScroller.Provider>
  </Card.Root>
  <div class="px-0.5 text-center text-xs text-muted-foreground">
    Scroll the transcript to see the footer update.
  </div>
</div>
```

View Code

## [Performance](#performance) `MessageScroller` is benchmarked against large transcripts with markdown and composed message rows.

The scroll hot path stays outside of Svelte state: no transcript-row rerenders for scroll, no forced layout on every scroll, and as little off-screen paint work as the browser can avoid.

Scroll position, anchoring, and follow-output are tracked imperatively and mirrored onto the root and viewport through `data-*` attributes, so scrolling and streaming do not rerender transcript rows.

The styled `MessageScroller.Item` also ships with `content-visibility: auto` and `contain-intrinsic-size`. Rows stay in the DOM for selection, copy, find-in-page, SSR, and assistive tech, but the browser can skip rendering work for rows far outside the viewport.

Visibility tracking is pay-for-what-you-use. A jump menu or active turn indicator costs nothing until something subscribes to `useMessageScrollerVisibility`.

This is comfortable for the expected range of a chat transcript: hundreds to low thousands of turns, including messages with markdown and composed components.

## [Virtualization](#virtualization)

Virtualization is intentionally left outside the primitive. `MessageScroller` renders real DOM rows and stays fast well into the thousands of turns (see [Performance](#performance)), so most transcripts never need it.

When a transcript is large enough to need virtualization, use `MessageScroller.Viewport` as the scroll element and let the virtualizer own the rows.

```svelte
<script lang="ts">
  import { useVirtualizer } from "@shadcn-svelte/primitives/svelte-virtual";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
  let {
    messages,
  }: {
    messages: Array<{ id: string; content: import("svelte").Snippet }>;
  } = $props();
  let viewport = $state<HTMLDivElement | null>(null);
  const virtualizer = useVirtualizer({
    get count() {
      return messages.length;
    },
    getScrollElement: () => viewport,
    estimateSize: () => 86,
    getItemKey: (index) => messages[index]?.id ?? index,
    overscan: 8,
  });
</script>
<MessageScroller.Provider>
  <MessageScroller.Root>
    <MessageScroller.Viewport bind:ref={viewport}>
      <MessageScroller.Content class="block min-h-full">
        <div
          class="relative w-full"
          style="height: {virtualizer.getTotalSize()}px"
        >
          {#each virtualizer.getVirtualItems() as virtualItem (virtualItem.key)}
            {@const message = messages[virtualItem.index]}
            {#if message}
              <div
                data-index={virtualItem.index}
                class="absolute start-0 top-0 w-full"
                style="transform: translateY({virtualItem.start}px)"
                {@attach (node) => virtualizer.measureElement(node)}
              >
                <Message.Root>{@render message.content()}</Message.Root>
              </div>
            {/if}
          {/each}
        </div>
      </MessageScroller.Content>
    </MessageScroller.Viewport>
    <MessageScroller.Button />
  </MessageScroller.Root>
</MessageScroller.Provider>
```

## [Accessibility](#accessibility) `MessageScroller` keeps the scroll container keyboard reachable and the transcript announceable without forcing a specific message UI. `MessageScroller.Viewport` is a labelled, keyboard-focusable scroll region by default. It uses `role="region"`, `aria-label="Messages"`, and `tabindex={0}`, so keyboard users can focus the transcript and scroll it directly. `MessageScroller.Content` marks the transcript as a live region with `role="log"` and `aria-relevant="additions"`. New rows can be announced, but streamed text mutations do not have to be announced token by token.

```svelte
<MessageScroller.Content aria-busy={status === "streaming"}>
</MessageScroller.Content>
```

Pass `aria-busy` while a turn streams if announcements should wait for the completed message row. `MessageScroller.Button` renders a real button. When there is nothing to scroll toward, it sets `inert`, uses `tabindex={-1}`, and exposes `data-active="false"` so inactive scroll controls do not create extra focus stops.

## [Unstyled](#unstyled)

The behavior in `MessageScroller` comes from the `@shadcn-svelte/primitives` package. Import the headless parts from `@shadcn-svelte/primitives/message-scroller` when you want your own markup and styles.

## [API Reference](#api-reference)

The props, data attributes, and hooks for every part live on the unstyled `MessageScroller` primitives in `@shadcn-svelte/primitives/message-scroller`. They are identical for the styled component and the unstyled parts.