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

## [Examples](#examples)

### [Default](#default)

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Textarea placeholder="Type your message here." />
```

View Code

### [Disabled](#disabled)

```svelte
<script lang="ts">
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<Textarea disabled placeholder="Type your message here." />
```

View Code

### [With Label](#with-label)

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

View Code

### [With Text](#with-text)

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
<div class="grid w-full gap-1.5">
  <Label for="message-2">Your Message</Label>
  <Textarea placeholder="Type your message here." id="message-2" />
  <p class="text-sm text-muted-foreground">
    Your message will be copied to the support team.
  </p>
</div>
```

View Code

### [With Button](#with-button)

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