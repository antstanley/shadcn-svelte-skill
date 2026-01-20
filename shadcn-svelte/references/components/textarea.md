# Textarea

Displays a form textarea or a component that looks like a textarea.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add textarea
```

```bash
npx shadcn-svelte@latest add textarea
```

```bash
bun x shadcn-svelte@latest add textarea
```

## Usage

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>

<Textarea />
```

## Examples

### Default

```svelte
<Textarea placeholder="Type your message here." />
```

### Disabled

```svelte
<Textarea disabled placeholder="Type your message here." />
```

### With Label

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>

<div class="grid w-full gap-1.5">
  <Label for="message">Your message</Label>
  <Textarea placeholder="Type your message here." id="message" />
</div>
```

### With Description Text

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>

<div class="grid w-full gap-1.5">
  <Label for="message">Your Message</Label>
  <Textarea placeholder="Type your message here." id="message" />
  <p class="text-muted-foreground text-sm">
    Your message will be copied to the support team.
  </p>
</div>
```

### With Button

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

## Props

The Textarea component accepts all standard HTML textarea attributes:

- `placeholder` - Placeholder text
- `disabled` - Whether the textarea is disabled
- `required` - Whether the textarea is required
- `name` - Name for form submission
- `value` - Textarea value (bindable)
- `rows` - Number of visible text lines
- `class` - Additional CSS classes
