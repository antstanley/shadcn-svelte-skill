# Test Results

Displays a test run by the agent, with its suites and failures.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import CheckIcon from "@lucide/svelte/icons/check";
 import CircleDashedIcon from "@lucide/svelte/icons/circle-dashed";
 import FileCodeIcon from "@lucide/svelte/icons/file-code";
 import FlaskConicalIcon from "@lucide/svelte/icons/flask-conical";
 import XIcon from "@lucide/svelte/icons/x";
 import { Chat } from "@ai-sdk/svelte";
 import { untrack } from "svelte";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import type { UIDataTypes, UIMessage } from "ai";
 type Test = {
  name: string;
  status: "passed" | "failed" | "skipped";
  error?: string;
 };
 type ChatMessage = UIMessage<
  unknown,
  UIDataTypes,
  {
   runTests: {
    input: { command: string };
    output: { suites: { name: string; tests: Test[] }[] };
   };
  }
 >;
 type ToolPart = Extract<ChatMessage["parts"][number], { type: "tool-runTests" }>;
 const script = createChat<ChatMessage>()
  .user("Run the checkout tests.")
  .assistant(({ writer }) => {
   writer
    .tool("runTests", { input: { command: "pnpm test checkout" } })
    .sleep(1500)
    .output({
     suites: [
      {
       name: "cart.test.ts",
       tests: [
        { name: "adds an item", status: "passed" },
        { name: "removes an item", status: "passed" },
        { name: "applies a discount code", status: "passed" },
      ],
      },
      {
       name: "payment.test.ts",
       tests: [
        { name: "charges the saved card", status: "passed" },
        {
         name: "retries a declined card",
         status: "failed",
         error: `Expected 2 charge attempts, received 1
  at Object.<anonymous> (src/payment.test.ts:58:22)`,
        },
      ],
      },
     ],
    });
   writer.text(
    "One test failed. The payment client does not retry a declined card, so the second charge attempt never happens."
   );
  });
 const transcript = script.get();
 const [question] = script.get(1);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat<ChatMessage>({ messages: transcript, transport });
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 function countTests(tests: Test[]) {
  return {
   total: tests.length,
   failed: tests.filter((test) => test.status === "failed").length,
   skipped: tests.filter((test) => test.status === "skipped").length,
  };
 }
 function formatCounts({ total, failed, skipped }: ReturnType<typeof countTests>) {
  return [`${total} tests`, failed > 0 && `${failed} failed`, skipped > 0 && `${skipped} skipped`]
   .filter(Boolean)
   .join(", ");
 }
</script>
{#snippet testRow(test: Test)}
 {#if test.status === "failed"}
  <Trace.Collapsible open>
   <Trace.CollapsibleTrigger>
    <Trace.Line status="error">
     <Trace.Icon>
      <XIcon />
     </Trace.Icon>
     <Trace.Title>{test.name}</Trace.Title>
    </Trace.Line>
   </Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent>
    <CodeBlock.Root size="sm">
     <CodeBlock.Content wrap class="max-h-64" code={test.error ?? ""} />
    </CodeBlock.Root>
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 {:else}
  <Trace.Line>
   <Trace.Icon>
    {#if test.status === "skipped"}
     <CircleDashedIcon />
    {:else}
     <CheckIcon />
    {/if}
   </Trace.Icon>
   <Trace.Title>
    {test.status === "skipped" ? `Skipped ${test.name}` : test.name}
   </Trace.Title>
  </Trace.Line>
 {/if}
{/snippet}
{#snippet testResultsRow(part: ToolPart, streaming: boolean)}
 {@const command = part.input?.command}
 {#if part.state !== "output-available"}
  {@const running = streaming && part.state !== "output-error"}
  <Trace.Line status={running ? "running" : "error"}>
   <Trace.Icon>
    <FlaskConicalIcon />
   </Trace.Icon>
   <Trace.Title>
    {running ? "Running" : "Failed to run"}
    {command}
   </Trace.Title>
  </Trace.Line>
 {:else}
  {@const suites = part.output.suites}
  {@const summary = countTests(suites.flatMap((suite) => suite.tests))}
  <Trace.Collapsible open={untrack(() => summary.failed > 0)}>
   <Trace.CollapsibleTrigger>
    <Trace.Line status={summary.failed > 0 ? "error" : undefined}>
     <Trace.Icon>
      <FlaskConicalIcon />
     </Trace.Icon>
     <Trace.Title>Ran {formatCounts(summary)}</Trace.Title>
    </Trace.Line>
   </Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent>
    <Trace.Root>
     {#each suites as suite, suiteIndex (suiteIndex)}
      {@const counts = countTests(suite.tests)}
      <Trace.Collapsible open={untrack(() => counts.failed > 0)}>
       <Trace.CollapsibleTrigger>
        <Trace.Line status={counts.failed > 0 ? "error" : undefined}>
         <Trace.Icon>
          <FileCodeIcon />
         </Trace.Icon>
         <Trace.Title>
          {suite.name}, {formatCounts(counts)}
         </Trace.Title>
        </Trace.Line>
       </Trace.CollapsibleTrigger>
       <Trace.CollapsibleContent>
        <Trace.Root>
         {#each suite.tests as test, testIndex (testIndex)}
          {@render testRow(test)}
         {/each}
        </Trace.Root>
       </Trace.CollapsibleContent>
      </Trace.Collapsible>
     {/each}
    </Trace.Root>
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 {/if}
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
   {@const tools = message.parts.filter((part) => part.type === "tool-runTests")}
   {@const text = getMessageText(message)}
   <Message.Root>
    <Message.Content class="gap-4">
     {#if tools.length > 0}
      <Trace.Root>
       {#each tools as part (part.toolCallId)}
        {@render testResultsRow(part, streaming)}
       {/each}
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

Test Results is a test run by the agent. The summary line counts what passed and failed. Open it to see each suite, its tests, and the error for each failure.

Test Results is built with `Trace` with a `Trace.Collapsible` for the run and for each suite.

## [Installation](#installation)

Test Results is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) and [Code Block](https://shadcn-svelte.com/docs/components/code-block) components.

```bash
pnpm dlx shadcn-svelte@latest add trace code-block
```

```bash
npx shadcn-svelte@latest add trace code-block
```

```bash
bun x shadcn-svelte@latest add trace code-block
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
</script>
```

```svelte
<Trace.Root>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line status="error">
        <Trace.Icon>
          <FlaskConicalIcon />
        </Trace.Icon>
        <Trace.Title>Ran 2 tests, 1 failed</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        <Trace.Line>
          <Trace.Icon>
            <CheckIcon />
          </Trace.Icon>
          <Trace.Title>creates a user</Trace.Title>
        </Trace.Line>
        <Trace.Collapsible>
          <Trace.CollapsibleTrigger>
            <Trace.Line status="error">
              <Trace.Icon>
                <XIcon />
              </Trace.Icon>
              <Trace.Title>updates a user profile</Trace.Title>
            </Trace.Line>
          </Trace.CollapsibleTrigger>
          <Trace.CollapsibleContent>
            <CodeBlock.Root size="sm">
              <CodeBlock.Content
                wrap
                class="max-h-64"
                code="Expected status 200, received 500"
              />
            </CodeBlock.Root>
          </Trace.CollapsibleContent>
        </Trace.Collapsible>
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Suites](#suites)

Group tests by file. Each suite is a collapsible line with a `Trace` of its tests. Open the suites that have a failure.

```svelte
<script lang="ts">
 import CheckIcon from "@lucide/svelte/icons/check";
 import CircleDashedIcon from "@lucide/svelte/icons/circle-dashed";
 import FileCodeIcon from "@lucide/svelte/icons/file-code";
 import FlaskConicalIcon from "@lucide/svelte/icons/flask-conical";
 import XIcon from "@lucide/svelte/icons/x";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 type Test = {
  name: string;
  status: "passed" | "failed" | "skipped";
  error?: string;
 };
 const suites: { name: string; tests: Test[] }[] = [
  {
   name: "auth.test.ts",
   tests: [
    { name: "logs in with valid credentials", status: "passed" },
    { name: "rejects an invalid password", status: "passed" },
    { name: "refreshes an expired token", status: "passed" },
  ],
  },
  {
   name: "user-api.test.ts",
   tests: [
    { name: "creates a user", status: "passed" },
    {
     name: "updates a user profile",
     status: "failed",
     error: `Expected status 200, received 500
  at Object.<anonymous> (src/user-api.test.ts:45:12)`,
    },
    { name: "deletes a user", status: "skipped" },
  ],
  },
  {
   name: "db.test.ts",
   tests: [
    { name: "connects to the database", status: "passed" },
    {
     name: "times out a slow query",
     status: "failed",
     error: `Exceeded timeout of 5000 ms for a test.
  at Object.<anonymous> (src/db.test.ts:22:3)`,
    },
  ],
  },
 ];
 function countTests(tests: Test[]) {
  return {
   total: tests.length,
   failed: tests.filter((test) => test.status === "failed").length,
   skipped: tests.filter((test) => test.status === "skipped").length,
  };
 }
 function formatCounts({ total, failed, skipped }: ReturnType<typeof countTests>) {
  return [`${total} tests`, failed > 0 && `${failed} failed`, skipped > 0 && `${skipped} skipped`]
   .filter(Boolean)
   .join(", ");
 }
 const summary = countTests(suites.flatMap((suite) => suite.tests));
</script>
{#snippet testRow(test: Test)}
 {#if test.status === "failed"}
  <Trace.Collapsible>
   <Trace.CollapsibleTrigger>
    <Trace.Line status="error">
     <Trace.Icon>
      <XIcon />
     </Trace.Icon>
     <Trace.Title>{test.name}</Trace.Title>
    </Trace.Line>
   </Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent>
    <CodeBlock.Root size="sm">
     <CodeBlock.Content wrap class="max-h-64" code={test.error ?? ""} />
    </CodeBlock.Root>
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 {:else}
  <Trace.Line>
   <Trace.Icon>
    {#if test.status === "skipped"}
     <CircleDashedIcon />
    {:else}
     <CheckIcon />
    {/if}
   </Trace.Icon>
   <Trace.Title>
    {test.status === "skipped" ? `Skipped ${test.name}` : test.name}
   </Trace.Title>
  </Trace.Line>
 {/if}
{/snippet}
<Trace.Root class="max-w-sm">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line status={summary.failed > 0 ? "error" : undefined}>
    <Trace.Icon>
     <FlaskConicalIcon />
    </Trace.Icon>
    <Trace.Title>Ran {formatCounts(summary)}</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <Trace.Root>
    {#each suites as suite, suiteIndex (suiteIndex)}
     {@const counts = countTests(suite.tests)}
     <Trace.Collapsible open={counts.failed > 0}>
      <Trace.CollapsibleTrigger>
       <Trace.Line status={counts.failed > 0 ? "error" : undefined}>
        <Trace.Icon>
         <FileCodeIcon />
        </Trace.Icon>
        <Trace.Title>
         {suite.name}, {formatCounts(counts)}
        </Trace.Title>
       </Trace.Line>
      </Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>
       <Trace.Root>
        {#each suite.tests as test, testIndex (testIndex)}
         {@render testRow(test)}
        {/each}
       </Trace.Root>
      </Trace.CollapsibleContent>
     </Trace.Collapsible>
    {/each}
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</Trace.Root>
```

View Code

```svelte
<Trace.Collapsible open={failed > 0}>
  <Trace.CollapsibleTrigger>
    <Trace.Line status={failed > 0 ? "error" : undefined}>
      <Trace.Icon>
        <FileCodeIcon />
      </Trace.Icon>
      <Trace.Title>user-api.test.ts, 14 tests, 2 failed</Trace.Title>
    </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
    <Trace.Root></Trace.Root>
  </Trace.CollapsibleContent>
</Trace.Collapsible>
```

## [AI SDK](#ai-sdk)

Run the tests as a tool and render its output. The tool states map the same way as in [Tool](https://shadcn-svelte.com/docs/ai-elements/tool#states).

```svelte
{@const tests = part.output.suites.flatMap((suite) => suite.tests)}
{@const failed = tests.filter((test) => test.status === "failed").length}
<Trace.Collapsible open={untrack(() => failed > 0)}>
  <Trace.CollapsibleTrigger>
    <Trace.Line status={failed > 0 ? "error" : undefined}>
      <Trace.Icon>
        <FlaskConicalIcon />
      </Trace.Icon>
      <Trace.Title>
        Ran {tests.length} tests{failed > 0 ? `, ${failed} failed` : ""}
      </Trace.Title>
    </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent></Trace.CollapsibleContent>
</Trace.Collapsible>
```

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).