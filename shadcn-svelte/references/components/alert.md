# Alert

Displays a callout for user attention.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add alert
```

```bash
npx shadcn-svelte@latest add alert
```

```bash
bun x shadcn-svelte@latest add alert
```

## Usage

```svelte
<script lang="ts">
  import * as Alert from "$lib/components/ui/alert/index.js";
</script>

<Alert.Root>
  <Alert.Title>Heads up!</Alert.Title>
  <Alert.Description>
    You can add components to your app using the CLI.
  </Alert.Description>
</Alert.Root>
```

## Examples

### Default

```svelte
<Alert.Root>
  <Alert.Title>Heads up!</Alert.Title>
  <Alert.Description>
    You can add components to your app using the CLI.
  </Alert.Description>
</Alert.Root>
```

### With Icon

```svelte
<script lang="ts">
  import Terminal from "@lucide/svelte/icons/terminal";
  import * as Alert from "$lib/components/ui/alert/index.js";
</script>

<Alert.Root>
  <Terminal class="size-4" />
  <Alert.Title>Heads up!</Alert.Title>
  <Alert.Description>
    You can add components to your app using the CLI.
  </Alert.Description>
</Alert.Root>
```

### Destructive

```svelte
<script lang="ts">
  import CircleAlert from "@lucide/svelte/icons/circle-alert";
  import * as Alert from "$lib/components/ui/alert/index.js";
</script>

<Alert.Root variant="destructive">
  <CircleAlert class="size-4" />
  <Alert.Title>Error</Alert.Title>
  <Alert.Description>
    Your session has expired. Please log in again.
  </Alert.Description>
</Alert.Root>
```

## Components

- **Alert.Root** - Main container (accepts `variant` prop)
- **Alert.Title** - Alert heading
- **Alert.Description** - Alert body text

## Variants

- **default** - Standard alert styling
- **destructive** - Error/warning styling
