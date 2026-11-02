# Textarea

Displays a form textarea or a component that looks like a textarea.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Textarea placeholder="Type your message here." />
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add textarea
```

```bash
npx shadcn-svelte@latest add textarea
```

```bash
bun x shadcn-svelte@latest add textarea
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
```

```svelte
<Textarea />
```

## [Field](#field)

Use `Field.Field`, `Field.Label`, and `Field.Description` to create a textarea with a label and description.

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Field.Field>
 <Field.Label for="textarea-message">Message</Field.Label>
 <Field.Description>Enter your message below.</Field.Description>
 <Textarea id="textarea-message" placeholder="Type your message here." />
</Field.Field>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop to disable the textarea. To style the disabled state, add the `data-disabled` attribute to the `Field.Field` component.

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Field.Field data-disabled>
 <Field.Label for="textarea-disabled">Message</Field.Label>
 <Textarea id="textarea-disabled" placeholder="Type your message here." disabled />
</Field.Field>
```

View Code

## [Invalid](#invalid)

Use the `aria-invalid` prop to mark the textarea as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field.Field` component.

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Field.Field data-invalid>
 <Field.Label for="textarea-invalid">Message</Field.Label>
 <Textarea id="textarea-invalid" placeholder="Type your message here." aria-invalid />
 <Field.Description>Please enter a valid message.</Field.Description>
</Field.Field>
```

View Code

## [Button](#button)

Pair with `Button` to create a textarea with a submit button.

```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<div class="grid w-full gap-2">
 <Textarea placeholder="Type your message here." />
 <Button>Send message</Button>
</div>
```

View Code