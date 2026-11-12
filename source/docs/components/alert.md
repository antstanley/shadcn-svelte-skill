# Alert

Displays a callout for user attention.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import InfoIcon from "@lucide/svelte/icons/info";
 import * as Alert from "$lib/components/ui/alert/index.js";
</script>
<div class="grid w-full max-w-md items-start gap-4">
 <Alert.Root>
  <CircleCheckIcon />
  <Alert.Title>Payment successful</Alert.Title>
  <Alert.Description>
   Your payment of $29.99 has been processed. A receipt has been sent to your email address.
  </Alert.Description>
 </Alert.Root>
 <Alert.Root>
  <InfoIcon />
  <Alert.Title>New feature available</Alert.Title>
  <Alert.Description>
   We've added dark mode support. You can enable it in your account settings.
  </Alert.Description>
 </Alert.Root>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add alert
```

```bash
npx shadcn-svelte@latest add alert
```

```bash
bun x shadcn-svelte@latest add alert
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Alert from "$lib/components/ui/alert/index.js";
</script>
```

```svelte
<Alert.Root>
  <InfoIcon />
  <Alert.Title>Heads up!</Alert.Title>
  <Alert.Description>
    You can add components and dependencies to your app using the cli.
  </Alert.Description>
  <Alert.Action>
    <Button variant="outline">Enable</Button>
  </Alert.Action>
</Alert.Root>
```

## [Basic](#basic)

A basic alert with an icon, title and description.

```svelte
<script lang="ts">
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import * as Alert from "$lib/components/ui/alert/index.js";
</script>
<Alert.Root class="max-w-md">
 <CircleCheckIcon />
 <Alert.Title>Account updated successfully</Alert.Title>
 <Alert.Description>
  Your profile information has been saved. Changes will be reflected immediately.
 </Alert.Description>
</Alert.Root>
```

View Code

## [Destructive](#destructive)

Use `variant="destructive"` to create a destructive alert.

```svelte
<script lang="ts">
 import CircleAlertIcon from "@lucide/svelte/icons/circle-alert";
 import * as Alert from "$lib/components/ui/alert/index.js";
</script>
<Alert.Root variant="destructive" class="max-w-md">
 <CircleAlertIcon />
 <Alert.Title>Payment failed</Alert.Title>
 <Alert.Description>
  Your payment could not be processed. Please check your payment method and try again.
 </Alert.Description>
</Alert.Root>
```

View Code

## [Action](#action)

Use `Alert.Action` to add a button or other action element to the alert.

```svelte
<script lang="ts">
 import * as Alert from "$lib/components/ui/alert/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
<Alert.Root class="max-w-md">
 <Alert.Title>Dark mode is now available</Alert.Title>
 <Alert.Description>Enable it under your profile settings to get started.</Alert.Description>
 <Alert.Action>
  <Button size="xs" variant="default">Enable</Button>
 </Alert.Action>
</Alert.Root>
```

View Code

## [Custom Colors](#custom-colors)

You can customize the alert colors by adding custom classes such as `bg-amber-50 dark:bg-amber-950` to the `Alert.Root` component.

```svelte
<script lang="ts">
 import TriangleAlertIcon from "@lucide/svelte/icons/triangle-alert";
 import * as Alert from "$lib/components/ui/alert/index.js";
</script>
<Alert.Root
 class="max-w-md border-amber-200 bg-amber-50 text-amber-900 dark:border-amber-900 dark:bg-amber-950 dark:text-amber-50"
>
 <TriangleAlertIcon />
 <Alert.Title>Your subscription will expire in 3 days.</Alert.Title>
 <Alert.Description>
  Renew now to avoid service interruption or upgrade to a paid plan to continue using the service.
 </Alert.Description>
</Alert.Root>
```

View Code