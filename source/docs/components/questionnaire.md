# Questionnaire

A multi-step questionnaire with single-choice, multiple-choice, freeform, and skippable questions.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    {
      choices: [
        { value: "tool-calls" },
        { value: "approvals" },
        { value: "handoffs" }
     ],
      name: "direction",
      required: true
    },
    {
      choices: [
        { value: "progress" },
        { value: "decisions" },
        { value: "risks" },
        { value: "next-step" }
     ],
      name: "signals"
    },
    {
      choices: [
        { value: "now" },
        { value: "next-cycle" },
        { value: "backlog" }
     ],
      name: "timing",
      required: true
    }
  ] as const;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    const answers = {
      direction: formData.get("direction"),
      signals: formData.getAll("signals"),
      timing: formData.get("timing")
    };
    toast("Agent plan saved", {
      description: `Direction: ${answers.direction ?? "None"}  Progress signals: ${answers.signals.join(", ") || "None"}  Timing: ${answers.timing ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="direction"
  {items}
  shortcuts="letters"
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress />
  <Questionnaire.Item name="direction" required>
    <Questionnaire.Title>What should the agent build next?</Questionnaire.Title>
    <Questionnaire.Description>
      Choose a direction or describe another task.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="tool-calls">
        <span class="font-medium">Tool call timeline</span>
        <span class="text-muted-foreground"
          >Show what the agent ran and what came back.</span
        >
      </Questionnaire.Choice>
      <Questionnaire.Choice value="approvals">
        <span class="font-medium">Approval checkpoints</span>
        <span class="text-muted-foreground"
          >Ask before sensitive or destructive actions.</span
        >
      </Questionnaire.Choice>
      <Questionnaire.Choice value="handoffs">
        <span class="font-medium">Sub-agent handoffs</span>
        <span class="text-muted-foreground">
          Make delegated work and results easier to follow.
        </span>
      </Questionnaire.Choice>
      <Questionnaire.Input
        aria-label="Another agent feature"
        placeholder="Describe another feature"
      />
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="signals" multiple>
    <Questionnaire.Title
      >What should every progress update include?</Questionnaire.Title
    >
    <Questionnaire.Description
      >Select all that apply, or skip this question.</Questionnaire.Description
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="progress">Progress</Questionnaire.Choice>
      <Questionnaire.Choice value="decisions">Decisions</Questionnaire.Choice>
      <Questionnaire.Choice value="risks">Risks</Questionnaire.Choice>
      <Questionnaire.Choice value="next-step">Next step</Questionnaire.Choice>
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="timing" required>
    <Questionnaire.Title>When should work begin?</Questionnaire.Title>
    <Questionnaire.Description
      >Choose when the agent should begin the work.</Questionnaire.Description
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="now">Start now</Questionnaire.Choice>
      <Questionnaire.Choice value="next-cycle"
        >Next development cycle</Questionnaire.Choice
      >
      <Questionnaire.Choice value="backlog"
        >Add it to the backlog</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Skip />
    <Questionnaire.Next>Next</Questionnaire.Next>
    <Questionnaire.Submit>Save plan</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add questionnaire
```

```bash
npx shadcn-svelte@latest add questionnaire
```

```bash
bun x shadcn-svelte@latest add questionnaire
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    {
      name: "direction",
      required: true,
      prompt: "What should we prototype next?",
      description: "Choose a direction or write your own.",
      choices: [
        {
          value: "delegation",
          label: "Delegation",
          description: "Show how work moves to a specialist.",
        },
        {
          value: "questions",
          label: "Question prompts",
          description: "Show choices while the interface waits.",
        },
        { value: "both", label: "Both together" },
     ],
      input: { label: "Another answer", placeholder: "Type another answer" },
    },
    {
      name: "detail",
      required: false,
      prompt: "How much detail should it include?",
      description: "Skip this if you are not sure yet.",
      choices: [
        { value: "focused", label: "Focused" },
        { value: "complete", label: "Complete flow" },
     ],
    },
  ] as const;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const answers = new FormData(event.currentTarget as HTMLFormElement);
    // answers.get("direction"), answers.getAll(...) for multiple items.
  }
</script>
```

Define the collection once: pass it to `Questionnaire.Root` for progress, actions, and shortcuts, then map it into the parts.

```svelte
<Questionnaire.Root {items} onSubmit={handleSubmit}>
  <Questionnaire.Progress />
  {#each items as question (question.name)}
    <Questionnaire.Item name={question.name} required={question.required}>
      <Questionnaire.Title>{question.prompt}</Questionnaire.Title>
      <Questionnaire.Description
        >{question.description}</Questionnaire.Description
      >
      <Questionnaire.Choices>
        {#each question.choices as choice (choice.value)}
          <Questionnaire.Choice value={choice.value}>
            <span class="font-medium">{choice.label}</span>
            {#if "description" in choice}
              <span class="text-muted-foreground">{choice.description}</span>
            {/if}
          </Questionnaire.Choice>
        {/each}
        {#if "input" in question}
          <Questionnaire.Input
            aria-label={question.input.label}
            placeholder={question.input.placeholder}
          />
        {/if}
      </Questionnaire.Choices>
      <Questionnaire.Error />
    </Questionnaire.Item>
  {/each}
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Skip />
    <Questionnaire.Next />
    <Questionnaire.Submit />
  </Questionnaire.Actions>
</Questionnaire.Root>
```

## [Composition](#composition)

```text
Questionnaire.Root
 Questionnaire.Progress
 Questionnaire.Item
    Questionnaire.Title
    Questionnaire.Description
    Questionnaire.Choices
       Questionnaire.Choice
          Questionnaire.ChoiceDescription
       Questionnaire.Input
    Questionnaire.Error
 Questionnaire.Actions
     Questionnaire.Previous
     Questionnaire.Skip
     Questionnaire.Next
     Questionnaire.Submit
```

Questionnaire owns the ordered items, active item, answer state, validation, progress, and navigation. The containing page, card, dialog, or drawer owns close and cancellation behavior, persistence, transport, and branching.

## [Server Rendering](#server-rendering)

Pass `items` to server-render the active item, progress, actions, and answer shortcuts. See `@shadcn-svelte/primitives/questionnaire` for the complete behavior.

## [Multiple Selection](#multiple-selection)

Use `multiple` for an item that accepts more than one fixed answer.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    {
      choices: [
        { value: "source" },
        { value: "tests" },
        { value: "docs" },
        { value: "history" }
     ],
      name: "context",
      required: true
    }
  ] as const;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const context = new FormData(event.currentTarget as HTMLFormElement).getAll(
      "context"
    );
    toast("Context selected", {
      description: `Context: ${context.join(", ") || "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  {items}
  shortcuts="letters"
  onSubmit={handleSubmit}
>
  <Questionnaire.Item name="context" multiple required>
    <Questionnaire.Title
      >What context should the agent inspect?</Questionnaire.Title
    >
    <Questionnaire.Description>
      Select every source that may affect the implementation.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="source"
        >Relevant source files</Questionnaire.Choice
      >
      <Questionnaire.Choice value="tests">Existing tests</Questionnaire.Choice>
      <Questionnaire.Choice value="docs"
        >Architecture documentation</Questionnaire.Choice
      >
      <Questionnaire.Choice value="history"
        >Recent commit history</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Submit>Share context</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Freeform Answer](#freeform-answer)

Compose `Questionnaire.Input` with fixed choices when the user can provide another answer.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    {
      choices: [
        { value: "incremental" },
        { value: "module" },
        { value: "rewrite" }
     ],
      name: "approach",
      required: true
    }
  ] as const;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const approach = new FormData(event.currentTarget as HTMLFormElement).get(
      "approach"
    );
    toast("Approach selected", {
      description: `Approach: ${approach ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  {items}
  shortcuts="letters"
  onSubmit={handleSubmit}
>
  <Questionnaire.Item name="approach" required>
    <Questionnaire.Title
      >How should the agent approach this refactor?</Questionnaire.Title
    >
    <Questionnaire.Description>
      Choose a strategy or write a more specific instruction.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="incremental"
        >Make the smallest safe change</Questionnaire.Choice
      >
      <Questionnaire.Choice value="module"
        >Refactor one module at a time</Questionnaire.Choice
      >
      <Questionnaire.Choice value="rewrite"
        >Replace the implementation completely</Questionnaire.Choice
      >
      <Questionnaire.Input
        aria-label="Another refactoring approach"
        placeholder="Describe another approach"
      />
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Submit>Use this approach</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Explicit Skip](#explicit-skip)

Add `Questionnaire.Skip` when an optional item may be intentionally left unanswered.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  import type { QuestionnaireItemStatus } from "@shadcn-svelte/primitives/questionnaire";
  const items = [
    { name: "task", required: true },
    { name: "constraints" },
    { name: "review", required: true }
 ] as const;
  let constraintStatus = $state<QuestionnaireItemStatus>("unanswered");
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    const answers = {
      task: formData.get("task"),
      constraints: formData.get("constraints"),
      constraintStatus,
      review: formData.get("review")
    };
    toast("Agent brief submitted", {
      description: `Task: ${answers.task ?? "None"}  Constraints: ${
        answers.constraintStatus === "skipped"
          ? "Skipped"
          : (answers.constraints ?? "None")
      }  Review: ${answers.review ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="task"
  {items}
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress />
  <Questionnaire.Item name="task" required>
    <Questionnaire.Title>What kind of change is this?</Questionnaire.Title>
    <Questionnaire.Description>
      Choose the category that best describes the work.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="feature">New feature</Questionnaire.Choice>
      <Questionnaire.Choice value="fix">Bug fix</Questionnaire.Choice>
      <Questionnaire.Choice value="refactor">Refactor</Questionnaire.Choice>
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item
    name="constraints"
    onStatusChange={(status) => (constraintStatus = status)}
  >
    <Questionnaire.Title
      >Are there any implementation constraints?</Questionnaire.Title
    >
    <Questionnaire.Description>
      Answer if needed, or intentionally skip this question.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="no-dependencies"
        >Do not add dependencies</Questionnaire.Choice
      >
      <Questionnaire.Choice value="no-migrations"
        >Do not change the database</Questionnaire.Choice
      >
      <Questionnaire.Choice value="preserve-api"
        >Preserve the public API</Questionnaire.Choice
      >
      <Questionnaire.Input
        aria-label="Another implementation constraint"
        placeholder="Describe another constraint"
      />
    </Questionnaire.Choices>
  </Questionnaire.Item>
  <Questionnaire.Item name="review" required>
    <Questionnaire.Title>How should the work be reviewed?</Questionnaire.Title>
    <Questionnaire.Description>
      Choose the checks the agent should complete before handoff.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="tests"
        >Run the test suite</Questionnaire.Choice
      >
      <Questionnaire.Choice value="diff"
        >Review the final diff</Questionnaire.Choice
      >
      <Questionnaire.Choice value="both"
        >Tests and diff review</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Skip />
    <Questionnaire.Next>Next</Questionnaire.Next>
    <Questionnaire.Submit>Submit brief</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Shortcuts](#shortcuts)

Assign a letter or number key to each answer with `shortcuts`.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  import type { QuestionnaireShortcutMode } from "@shadcn-svelte/primitives/questionnaire";
  const items = [
    {
      choices: [{ value: "inspect" }, { value: "tests" }, { value: "patch" }],
      name: "action",
      required: true
    }
  ] as const;
  let shortcutSelect = $state("letters");
  const shortcuts = $derived(
    shortcutSelect === "letters" || shortcutSelect === "numbers"
      ? (shortcutSelect as QuestionnaireShortcutMode)
      : undefined
  );
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const action = new FormData(event.currentTarget as HTMLFormElement).get(
      "action"
    );
    toast("Next action selected", {
      description: `Action: ${action ?? "None"}  Shortcuts: ${shortcuts ?? "none"}` });
  }
</script>
<div class="relative mx-auto flex h-full w-full max-w-md flex-col">
  <NativeSelect.Root
    aria-label="Shortcut style"
    class="absolute end-0 top-0"
    bind:value={shortcutSelect}
  >
    <NativeSelect.Option value="none">No shortcuts</NativeSelect.Option>
    <NativeSelect.Option value="letters">Letters</NativeSelect.Option>
    <NativeSelect.Option value="numbers">Numbers</NativeSelect.Option>
  </NativeSelect.Root>
  <Questionnaire.Root
    class="mt-auto"
    {items}
    {shortcuts}
    onSubmit={handleSubmit}
  >
    <Questionnaire.Item name="action" required>
      <Questionnaire.Title>What should the agent do next?</Questionnaire.Title>
      <Questionnaire.Description>
        Use the displayed shortcut or navigate with the keyboard.
      </Questionnaire.Description>
      <Questionnaire.Choices>
        <Questionnaire.Choice value="inspect"
          >Inspect the implementation</Questionnaire.Choice
        >
        <Questionnaire.Choice value="tests"
          >Run the relevant tests</Questionnaire.Choice
        >
        <Questionnaire.Choice value="patch"
          >Prepare the patch</Questionnaire.Choice
        >
      </Questionnaire.Choices>
      <Questionnaire.Error />
    </Questionnaire.Item>
    <Questionnaire.Actions>
      <Questionnaire.Submit>Confirm action</Questionnaire.Submit>
    </Questionnaire.Actions>
  </Questionnaire.Root>
</div>
```

View Code

## [Custom Validation](#custom-validation)

Combine controlled navigation with an external schema such as Zod to return to an invalid item and present its error.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import { z } from "zod";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    { name: "detail", required: true },
    { name: "audience", required: true }
 ] as const;
  const questionnaireSchema = z
    .object({
      detail: z.enum(["summary", "complete"]),
      audience: z.enum(["team", "public"])
    })
    .superRefine((answers, context) => {
      if (answers.audience === "public" && answers.detail === "summary") {
        context.addIssue({
          code: "custom",
          message:
            "Public answers need enough context. Choose a complete answer.",
          path: ["detail"]
        });
      }
    });
  type QuestionnaireItemName = keyof z.infer<typeof questionnaireSchema>;
  type QuestionnaireErrors = Partial<Record<QuestionnaireItemName, string>>;
  let item = $state("detail");
  let errors = $state<QuestionnaireErrors>({});
  function clearError(name: QuestionnaireItemName) {
    if (!errors[name]) return;
    const nextErrors = { ...errors };
    delete nextErrors[name];
    errors = nextErrors;
  }
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const result = questionnaireSchema.safeParse(
      Object.fromEntries(new FormData(event.currentTarget as HTMLFormElement))
    );
    if (result.success) {
      errors = {};
      toast("Agent response configured", {
        description: `Detail: ${result.data.detail}  Audience: ${result.data.audience}` });
      return;
    }
    const nextErrors: QuestionnaireErrors = {};
    for (const issue of result.error.issues) {
      const name = issue.path[0];
      if ((name === "detail" || name === "audience") && !nextErrors[name]) {
        nextErrors[name] = issue.message;
      }
    }
    const firstInvalidItem = result.error.issues[0]?.path[0];
    errors = nextErrors;
    if (firstInvalidItem === "detail" || firstInvalidItem === "audience") {
      item = firstInvalidItem;
    }
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  bind:item
  {items}
  onSubmit={handleSubmit}
>
  <Card.Root class="w-full">
    <Questionnaire.Item invalid={Boolean(errors.detail)} name="detail" required>
      <Card.Header>
        <Questionnaire.Title
          >How much detail should the answer include?</Questionnaire.Title
        >
        <Questionnaire.Description
          >Choose the response depth.</Questionnaire.Description
        >
        <Card.Action>
          <Questionnaire.Progress class="min-w-0">
            {#snippet child({ props, current, total })}
              <div {...props}>{current} / {total}</div>
            {/snippet}
          </Questionnaire.Progress>
        </Card.Action>
      </Card.Header>
      <Card.Content>
        <Questionnaire.Choices>
          <Questionnaire.Choice
            value="summary"
            onChange={() => clearError("detail")}
          >
            Concise summary
          </Questionnaire.Choice>
          <Questionnaire.Choice
            value="complete"
            onChange={() => clearError("detail")}
          >
            Complete answer
          </Questionnaire.Choice>
        </Questionnaire.Choices>
        <Questionnaire.Error>{errors.detail}</Questionnaire.Error>
      </Card.Content>
    </Questionnaire.Item>
    <Questionnaire.Item
      invalid={Boolean(errors.audience)}
      name="audience"
      required
    >
      <Card.Header>
        <Questionnaire.Title>Who will read the answer?</Questionnaire.Title>
        <Questionnaire.Description
          >Public answers require complete context.</Questionnaire.Description
        >
        <Card.Action>
          <Questionnaire.Progress class="min-w-0">
            {#snippet child({ props, current, total })}
              <div {...props}>{current} / {total}</div>
            {/snippet}
          </Questionnaire.Progress>
        </Card.Action>
      </Card.Header>
      <Card.Content>
        <Questionnaire.Choices>
          <Questionnaire.Choice
            value="team"
            onChange={() => clearError("audience")}
          >
            My team
          </Questionnaire.Choice>
          <Questionnaire.Choice
            value="public"
            onChange={() => clearError("audience")}
          >
            Public audience
          </Questionnaire.Choice>
        </Questionnaire.Choices>
        <Questionnaire.Error>{errors.audience}</Questionnaire.Error>
      </Card.Content>
    </Questionnaire.Item>
    <Card.Footer>
      <Questionnaire.Actions>
        <Questionnaire.Previous />
        <Questionnaire.Next>Next</Questionnaire.Next>
        <Questionnaire.Submit>Validate answers</Questionnaire.Submit>
      </Questionnaire.Actions>
    </Card.Footer>
  </Card.Root>
</Questionnaire.Root>
```

View Code

## [Controlled](#controlled)

Control the active item from host state, such as returning to an invalid step.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    { name: "scope", required: true },
    { name: "checks", required: true },
    { name: "output", required: true }
 ] as const;
  const itemLabels: Record<string, string> = {
    scope: "Change scope",
    checks: "Verification",
    output: "Final output"
  };
  let item = $state("scope");
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    toast("Agent workflow configured", {
      description: `Scope: ${formData.get("scope") ?? "None"}  Verification: ${formData.get("checks") ?? "None"}  Output: ${formData.get("output") ?? "None"}` });
  }
</script>
<div class="relative mx-auto flex h-full w-full max-w-md flex-col">
  <p class="absolute end-0 top-0 text-sm text-muted-foreground" role="status">
    Current checkpoint: {itemLabels[item]}
  </p>
  <Questionnaire.Root class="mt-auto" bind:item {items} onSubmit={handleSubmit}>
    <Questionnaire.Progress />
    <Questionnaire.Item name="scope" required>
      <Questionnaire.Title>What may the agent change?</Questionnaire.Title>
      <Questionnaire.Description>
        The host stores the active checkpoint while Questionnaire navigates.
      </Questionnaire.Description>
      <Questionnaire.Choices>
        <Questionnaire.Choice value="component"
          >Only the target component</Questionnaire.Choice
        >
        <Questionnaire.Choice value="tests"
          >Component and related tests</Questionnaire.Choice
        >
        <Questionnaire.Choice value="feature"
          >The complete feature area</Questionnaire.Choice
        >
      </Questionnaire.Choices>
      <Questionnaire.Error />
    </Questionnaire.Item>
    <Questionnaire.Item name="checks" required>
      <Questionnaire.Title
        >Which verification level should it use?</Questionnaire.Title
      >
      <Questionnaire.Choices>
        <Questionnaire.Choice value="targeted"
          >Targeted tests</Questionnaire.Choice
        >
        <Questionnaire.Choice value="package"
          >Package tests and typecheck</Questionnaire.Choice
        >
        <Questionnaire.Choice value="full"
          >Full workspace verification</Questionnaire.Choice
        >
      </Questionnaire.Choices>
      <Questionnaire.Error />
    </Questionnaire.Item>
    <Questionnaire.Item name="output" required>
      <Questionnaire.Title
        >What should the agent return when finished?</Questionnaire.Title
      >
      <Questionnaire.Choices>
        <Questionnaire.Choice value="summary"
          >Concise summary</Questionnaire.Choice
        >
        <Questionnaire.Choice value="diff"
          >Summary with changed files</Questionnaire.Choice
        >
        <Questionnaire.Choice value="handoff"
          >Detailed implementation handoff</Questionnaire.Choice
        >
      </Questionnaire.Choices>
      <Questionnaire.Error />
    </Questionnaire.Item>
    <Questionnaire.Actions>
      <Questionnaire.Previous />
      <Questionnaire.Next>Next</Questionnaire.Next>
      <Questionnaire.Submit>Save workflow</Questionnaire.Submit>
    </Questionnaire.Actions>
  </Questionnaire.Root>
</div>
```

View Code

## [Resume](#resume)

Restore a saved active item and default answers, then reset changes back to that saved state.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const items = [
    { name: "change", required: true },
    { name: "verification", required: true },
    { name: "notes" }
 ] as const;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    const answers = {
      change: formData.get("change"),
      verification: formData.getAll("verification"),
      notes: formData.get("notes")
    };
    toast("Draft updated", {
      description: `Migration: ${answers.change ?? "None"}  Verification: ${answers.verification.join(", ") || "None"}  Notes: ${answers.notes || "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="verification"
  {items}
  onReset={() => toast("Saved answers restored")}
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress />
  <Questionnaire.Item name="change" required>
    <Questionnaire.Title>What kind of migration is this?</Questionnaire.Title>
    <Questionnaire.Description>
      This answer was saved during the previous session.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="incremental" defaultChecked
        >Incremental migration</Questionnaire.Choice
      >
      <Questionnaire.Choice value="cutover">Single cutover</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="verification" multiple required>
    <Questionnaire.Title
      >How should the migration be verified?</Questionnaire.Title
    >
    <Questionnaire.Description>
      These checks were selected during the previous session.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="tests" defaultChecked
        >Run migration tests</Questionnaire.Choice
      >
      <Questionnaire.Choice value="typecheck" defaultChecked
        >Run the typecheck</Questionnaire.Choice
      >
      <Questionnaire.Choice value="manual"
        >Perform a manual smoke test</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="notes">
    <Questionnaire.Title
      >Anything else the agent should remember?</Questionnaire.Title
    >
    <Questionnaire.Description
      >This note was saved with the draft.</Questionnaire.Description
    >
    <Questionnaire.Input
      aria-label="Saved migration note"
      defaultValue="Keep the existing public API stable."
    />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Button type="reset" variant="outline">Reset changes</Button>
    <Questionnaire.Previous />
    <Questionnaire.Next>Next</Questionnaire.Next>
    <Questionnaire.Submit>Update draft</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Conditional Items](#conditional-items)

Disable items that do not apply to the user's earlier answers.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  let runtime = $state("local");
  const items = $derived([
    { name: "runtime", required: true },
    {
      disabled: runtime !== "cloud",
      name: "environment",
      required: true
    },
    { name: "approval", required: true }
 ]);
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    toast("Execution plan saved", {
      description: `Runtime: ${formData.get("runtime") ?? "None"}  Environment: ${formData.get("environment") ?? "Not applicable"}  Approval: ${formData.get("approval") ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="runtime"
  {items}
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress />
  <Questionnaire.Item name="runtime" required>
    <Questionnaire.Title>Where should the agent run?</Questionnaire.Title>
    <Questionnaire.Description>
      Cloud runs add an environment question to this flow.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice
        checked={runtime === "local"}
        value="local"
        onChange={() => (runtime = "local")}
      >
        Local workspace
      </Questionnaire.Choice>
      <Questionnaire.Choice
        checked={runtime === "cloud"}
        value="cloud"
        onChange={() => (runtime = "cloud")}
      >
        Cloud workspace
      </Questionnaire.Choice>
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item
    disabled={runtime !== "cloud"}
    name="environment"
    required
  >
    <Questionnaire.Title
      >Which cloud environment should it use?</Questionnaire.Title
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="preview">Preview</Questionnaire.Choice>
      <Questionnaire.Choice value="staging">Staging</Questionnaire.Choice>
      <Questionnaire.Choice value="isolated"
        >Isolated sandbox</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="approval" required>
    <Questionnaire.Title
      >When should the agent request approval?</Questionnaire.Title
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="writes"
        >Before writing files</Questionnaire.Choice
      >
      <Questionnaire.Choice value="commands"
        >Before running commands</Questionnaire.Choice
      >
      <Questionnaire.Choice value="sensitive"
        >Only for sensitive actions</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Next>Next</Questionnaire.Next>
    <Questionnaire.Submit>Save execution plan</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Navigation State](#navigation-state)

Read item status to opt into disabled navigation and custom action styling.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  import type { QuestionnaireItemStatus } from "@shadcn-svelte/primitives/questionnaire";
  const items = [
    { name: "permission", required: true },
    { name: "verification", required: true }
 ] as const;
  type ItemName = "permission" | "verification";
  let item = $state<ItemName>("permission");
  let statuses = $state<Record<ItemName, QuestionnaireItemStatus>>({
    permission: "unanswered",
    verification: "unanswered"
  });
  const unanswered = $derived(statuses[item] === "unanswered");
  function setStatus(name: ItemName, status: QuestionnaireItemStatus) {
    statuses = { ...statuses, [name]: status };
  }
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    toast("Permissions saved", {
      description: `Permission: ${formData.get("permission") ?? "None"}  Verification: ${formData.get("verification") ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  bind:item
  {items}
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress />
  <Questionnaire.Item
    name="permission"
    required
    onStatusChange={(status) => setStatus("permission", status)}
  >
    <Questionnaire.Title>What may the agent modify?</Questionnaire.Title>
    <Questionnaire.Description>
      Next is intentionally disabled until an answer is selected.
    </Questionnaire.Description>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="files">Project files</Questionnaire.Choice>
      <Questionnaire.Choice value="tests"
        >Project files and tests</Questionnaire.Choice
      >
      <Questionnaire.Choice value="config"
        >Files, tests, and configuration</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item
    name="verification"
    required
    onStatusChange={(status) => setStatus("verification", status)}
  >
    <Questionnaire.Title>What must pass before completion?</Questionnaire.Title>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="tests">Tests</Questionnaire.Choice>
      <Questionnaire.Choice value="types">Tests and types</Questionnaire.Choice>
      <Questionnaire.Choice value="all"
        >Tests, types, and visual QA</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Next
      class="data-[status=unanswered]:opacity-50"
      disabled={unanswered}
      variant="secondary"
    >
      Next
    </Questionnaire.Next>
    <Questionnaire.Submit disabled={unanswered}
      >Save permissions</Questionnaire.Submit
    >
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Custom Progress](#custom-progress)

Use the Progress `child` snippet to build a custom progress indicator.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    { name: "scope", required: true },
    { name: "strategy", required: true },
    { name: "tests", required: true },
    { name: "delivery", required: true }
 ] as const;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    toast("Pull request plan ready", {
      description: `Scope: ${formData.get("scope") ?? "None"}  Commits: ${formData.get("strategy") ?? "None"}  Tests: ${formData.get("tests") ?? "None"}  Delivery: ${formData.get("delivery") ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="scope"
  {items}
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress class="w-full">
    {#snippet child({ props, current, total })}
      <div {...props}>
        <div class="mb-2 flex gap-1.5" aria-hidden="true">
          {#each Array.from({ length: total }, (_, index) => index) as index (index)}
            <span
              class={index < current
                ? "h-1.5 flex-1 rounded-full bg-primary"
                : "h-1.5 flex-1 rounded-full bg-muted"}
            ></span>
          {/each}
        </div>
        <span>Checkpoint {current} of {total}</span>
      </div>
    {/snippet}
  </Questionnaire.Progress>
  <Questionnaire.Item name="scope" required>
    <Questionnaire.Title>How large is the change?</Questionnaire.Title>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="small">Small patch</Questionnaire.Choice>
      <Questionnaire.Choice value="medium"
        >Feature-sized change</Questionnaire.Choice
      >
      <Questionnaire.Choice value="large"
        >Cross-package change</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="strategy" required>
    <Questionnaire.Title>How should commits be organized?</Questionnaire.Title>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="single">Single commit</Questionnaire.Choice>
      <Questionnaire.Choice value="logical"
        >Logical commits</Questionnaire.Choice
      >
      <Questionnaire.Choice value="squash"
        >Squash before review</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="tests" required>
    <Questionnaire.Title>Which tests should run?</Questionnaire.Title>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="targeted"
        >Targeted tests</Questionnaire.Choice
      >
      <Questionnaire.Choice value="package">Package suite</Questionnaire.Choice>
      <Questionnaire.Choice value="workspace"
        >Full workspace</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item name="delivery" required>
    <Questionnaire.Title>How should the work be delivered?</Questionnaire.Title>
    <Questionnaire.Choices>
      <Questionnaire.Choice value="patch">Patch only</Questionnaire.Choice>
      <Questionnaire.Choice value="commit"
        >Committed locally</Questionnaire.Choice
      >
      <Questionnaire.Choice value="branch"
        >Push a review branch</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Next>Next</Questionnaire.Next>
    <Questionnaire.Submit>Finish plan</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Animated Items](#animated-items)

Animate the active item while keeping progress and navigation stationary.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    { name: "task", required: true },
    { name: "review", required: true },
    { name: "delivery", required: true }
 ] as const;
  const itemClass =
    "data-active:animate-in data-active:fade-in-0 data-active:slide-in-from-bottom-2 data-active:duration-300 motion-reduce:animate-none";
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    toast("Agent workflow saved", {
      description: `Task: ${formData.get("task") ?? "None"}  Review: ${formData.get("review") ?? "None"}  Delivery: ${formData.get("delivery") ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="task"
  {items}
  onSubmit={handleSubmit}
>
  <Questionnaire.Progress />
  <Questionnaire.Item class={itemClass} name="task" required>
    <Questionnaire.Title>What should the agent do?</Questionnaire.Title>
    <Questionnaire.Description
      >Choose the task for this run.</Questionnaire.Description
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="implement"
        >Implement the requested change</Questionnaire.Choice
      >
      <Questionnaire.Choice value="debug"
        >Debug the current behavior</Questionnaire.Choice
      >
      <Questionnaire.Choice value="review"
        >Review the implementation</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item class={itemClass} name="review" required>
    <Questionnaire.Title>How should the work be reviewed?</Questionnaire.Title>
    <Questionnaire.Description
      >Select the verification depth.</Questionnaire.Description
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="targeted"
        >Targeted checks</Questionnaire.Choice
      >
      <Questionnaire.Choice value="complete"
        >Complete test suite</Questionnaire.Choice
      >
      <Questionnaire.Choice value="manual"
        >Tests and manual QA</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Item class={itemClass} name="delivery" required>
    <Questionnaire.Title
      >How should the result be delivered?</Questionnaire.Title
    >
    <Questionnaire.Description
      >Choose the final handoff format.</Questionnaire.Description
    >
    <Questionnaire.Choices>
      <Questionnaire.Choice value="summary"
        >Concise summary</Questionnaire.Choice
      >
      <Questionnaire.Choice value="diff"
        >Summary and changed files</Questionnaire.Choice
      >
      <Questionnaire.Choice value="handoff"
        >Detailed review handoff</Questionnaire.Choice
      >
    </Questionnaire.Choices>
    <Questionnaire.Error />
  </Questionnaire.Item>
  <Questionnaire.Actions>
    <Questionnaire.Previous />
    <Questionnaire.Next>Next</Questionnaire.Next>
    <Questionnaire.Submit>Save workflow</Questionnaire.Submit>
  </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Card](#card)

Compose Questionnaire with Card slots while keeping the question title and description semantic.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  const items = [
    {
      choices: [{ value: "fix" }, { value: "refactor" }, { value: "docs" }],
      name: "task",
      required: true
    },
    {
      choices: [{ value: "summary" }, { value: "files" }, { value: "review" }],
      name: "output",
      required: true
    }
  ] as const;
  const uid = $props.id();
  const taskTitleId = `${uid}-task`;
  const outputTitleId = `${uid}-output`;
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    toast("Agent task created", {
      description: `Task: ${formData.get("task") ?? "None"}  Handoff: ${formData.get("output") ?? "None"}` });
  }
</script>
<Questionnaire.Root
  class="mx-auto max-w-md"
  defaultItem="task"
  {items}
  shortcuts="numbers"
  onSubmit={handleSubmit}
>
  <Card.Root>
    <Questionnaire.Item aria-labelledby={taskTitleId} name="task" required>
      <Card.Header>
        <Questionnaire.Title id={taskTitleId}>
          {#snippet child({ props })}
            <Card.Title {...props}>What should the agent work on?</Card.Title>
          {/snippet}
        </Questionnaire.Title>
        <Questionnaire.Description>
          {#snippet child({ props })}
            <Card.Description {...props}
              >Choose the task that should be handled next.</Card.Description
            >
          {/snippet}
        </Questionnaire.Description>
        <Card.Action>
          <Questionnaire.Progress />
        </Card.Action>
      </Card.Header>
      <Card.Content>
        <Questionnaire.Choices>
          <Questionnaire.Choice value="fix"
            >Fix the failing tests</Questionnaire.Choice
          >
          <Questionnaire.Choice value="refactor"
            >Refactor the data layer</Questionnaire.Choice
          >
          <Questionnaire.Choice value="docs"
            >Update the integration guide</Questionnaire.Choice
          >
        </Questionnaire.Choices>
        <Questionnaire.Error />
      </Card.Content>
    </Questionnaire.Item>
    <Questionnaire.Item aria-labelledby={outputTitleId} name="output" required>
      <Card.Header>
        <Questionnaire.Title id={outputTitleId}>
          {#snippet child({ props })}
            <Card.Title {...props}
              >What should the final handoff include?</Card.Title
            >
          {/snippet}
        </Questionnaire.Title>
        <Questionnaire.Description>
          {#snippet child({ props })}
            <Card.Description {...props}
              >Pick the level of detail needed for review.</Card.Description
            >
          {/snippet}
        </Questionnaire.Description>
        <Card.Action>
          <Questionnaire.Progress />
        </Card.Action>
      </Card.Header>
      <Card.Content>
        <Questionnaire.Choices>
          <Questionnaire.Choice value="summary"
            >Summary only</Questionnaire.Choice
          >
          <Questionnaire.Choice value="files"
            >Summary and changed files</Questionnaire.Choice
          >
          <Questionnaire.Choice value="review"
            >Full review handoff</Questionnaire.Choice
          >
        </Questionnaire.Choices>
        <Questionnaire.Error />
      </Card.Content>
    </Questionnaire.Item>
    <Card.Footer>
      <Questionnaire.Actions class="w-full">
        <Questionnaire.Previous />
        <Questionnaire.Next>Next</Questionnaire.Next>
        <Questionnaire.Submit>Create task</Questionnaire.Submit>
      </Questionnaire.Actions>
    </Card.Footer>
  </Card.Root>
</Questionnaire.Root>
```

View Code

## [Dialog](#dialog)

Compose Questionnaire inside a Dialog while keeping cancellation and dismissal host-owned.

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const items = [
    { name: "scope", required: true },
    { name: "tests", required: true }
 ] as const;
  let open = $state(false);
  function handleSubmit(event: SubmitEvent) {
    event.preventDefault();
    const formData = new FormData(event.currentTarget as HTMLFormElement);
    open = false;
    toast("Clarification sent", {
      description: `Scope: ${formData.get("scope") ?? "None"}  Verification: ${formData.get("tests") ?? "None"}` });
  }
</script>
<Dialog.Root bind:open>
  <Dialog.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline">Open clarification</Button>
    {/snippet}
  </Dialog.Trigger>
  <Dialog.Content>
    <Questionnaire.Root defaultItem="scope" {items} onSubmit={handleSubmit}>
      <Questionnaire.Item name="scope" required>
        <Dialog.Header>
          <Questionnaire.Progress />
          <Questionnaire.Title>
            {#snippet child({ props })}
              <Dialog.Title {...props}>Which files are in scope?</Dialog.Title>
            {/snippet}
          </Questionnaire.Title>
          <Questionnaire.Description>
            {#snippet child({ props })}
              <Dialog.Description {...props}>
                Choose how broadly the agent can update the workspace.
              </Dialog.Description>
            {/snippet}
          </Questionnaire.Description>
        </Dialog.Header>
        <Questionnaire.Choices>
          <Questionnaire.Choice value="component"
            >Component only</Questionnaire.Choice
          >
          <Questionnaire.Choice value="feature"
            >Complete feature directory</Questionnaire.Choice
          >
          <Questionnaire.Choice value="workspace"
            >Any related workspace file</Questionnaire.Choice
          >
        </Questionnaire.Choices>
        <Questionnaire.Error />
      </Questionnaire.Item>
      <Questionnaire.Item name="tests" required>
        <Dialog.Header>
          <Questionnaire.Progress />
          <Questionnaire.Title>
            {#snippet child({ props })}
              <Dialog.Title {...props}
                >How much verification is needed?</Dialog.Title
              >
            {/snippet}
          </Questionnaire.Title>
          <Questionnaire.Description>
            {#snippet child({ props })}
              <Dialog.Description {...props}>
                Choose the checks the agent should run before handoff.
              </Dialog.Description>
            {/snippet}
          </Questionnaire.Description>
        </Dialog.Header>
        <Questionnaire.Choices>
          <Questionnaire.Choice value="targeted"
            >Targeted tests</Questionnaire.Choice
          >
          <Questionnaire.Choice value="package"
            >Package tests</Questionnaire.Choice
          >
          <Questionnaire.Choice value="full"
            >Full workspace verification</Questionnaire.Choice
          >
        </Questionnaire.Choices>
        <Questionnaire.Error />
      </Questionnaire.Item>
      <Dialog.Footer>
        <Dialog.Close>
          {#snippet child({ props })}
            <Button {...props} type="button" variant="outline">Cancel</Button>
          {/snippet}
        </Dialog.Close>
        <Questionnaire.Actions>
          <Questionnaire.Previous />
          <Questionnaire.Next>Next</Questionnaire.Next>
          <Questionnaire.Submit>Send answer</Questionnaire.Submit>
        </Questionnaire.Actions>
      </Dialog.Footer>
    </Questionnaire.Root>
  </Dialog.Content>
</Dialog.Root>
```

View Code

## [Accessibility](#accessibility) `Questionnaire.Item` renders a `fieldset`, and `Questionnaire.Title` renders its `legend`. Descriptions and active errors are associated with the current item, and invalid items and answer controls expose `aria-invalid`.

Fixed choices preserve native radio and checkbox behavior. Progress is exposed as a named progressbar, navigation uses real buttons, and inactive items and actions are hidden and inert. Successful navigation focuses the newly active item; failed validation focuses an available answer control.

Always give `Questionnaire.Input` an accessible name with a visible label, `aria-label`, or `aria-labelledby`. A placeholder is not a label.

## [Unstyled](#unstyled)

The behavior in `Questionnaire` comes from the `@shadcn-svelte/primitives` package. Import the headless parts from `@shadcn-svelte/primitives/questionnaire` when you want your own markup and styles.

## [API Reference](#api-reference)

The props, data attributes, and render states for every part live on the unstyled `Questionnaire` primitives in `@shadcn-svelte/primitives/questionnaire`. The styled components inherit the corresponding unstyled props. Navigation components also accept Button `size` and `variant` props, and `Questionnaire.Actions` is a styled-only layout helper.