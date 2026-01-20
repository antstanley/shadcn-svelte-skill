# Textarea

Displays a form textarea or a component that looks like a textarea.

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Textarea placeholder="Type your message here." />
```

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
```

```svelte
<Textarea />
```

## Examples

### Default

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Textarea placeholder="Type your message here." />
```

### Disabled

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
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

### With Text

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<div class="grid w-full gap-1.5">
  <Label for="message-2">Your Message</Label>
  <Textarea placeholder="Type your message here." id="message-2" />
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