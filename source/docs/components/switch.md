# Switch

A control that allows the user to toggle between checked and not checked.

[Docs](https://bits-ui.com/docs/components/switch)

[API Reference](https://bits-ui.com/docs/components/switch#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<div class="flex items-center space-x-2">
  <Switch id="airplane-mode" />
  <Label for="airplane-mode">Airplane Mode</Label>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add switch
```

```bash
npx shadcn-svelte@latest add switch
```

```bash
bun x shadcn-svelte@latest add switch
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
```

```svelte
<Switch />
```

## [Description](#description)

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<Field.Field orientation="horizontal" class="max-w-sm">
  <Field.Content>
    <Field.Label for="switch-focus-mode">Share across devices</Field.Label>
    <Field.Description>
      Focus is shared across devices, and turns off when you leave the app.
    </Field.Description>
  </Field.Content>
  <Switch id="switch-focus-mode" />
</Field.Field>
```

View Code

## [Choice Card](#choice-card)

Card-style selection where `Field.Label` wraps the entire `Field.Field` for a clickable card pattern.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<Field.Group class="w-full max-w-sm">
  <Field.Label for="switch-share">
    <Field.Field orientation="horizontal">
      <Field.Content>
        <Field.Title>Share across devices</Field.Title>
        <Field.Description>
          Focus is shared across devices, and turns off when you leave the app.
        </Field.Description>
      </Field.Content>
      <Switch id="switch-share" />
    </Field.Field>
  </Field.Label>
  <Field.Label for="switch-notifications">
    <Field.Field orientation="horizontal">
      <Field.Content>
        <Field.Title>Enable notifications</Field.Title>
        <Field.Description>
          Receive notifications when focus mode is enabled or disabled.
        </Field.Description>
      </Field.Content>
      <Switch id="switch-notifications" checked />
    </Field.Field>
  </Field.Label>
</Field.Group>
```

View Code

## [Disabled](#disabled)

Add the `disabled` prop to the `Switch` component to disable the switch. Add the `data-disabled` prop to the `Field.Field` component for styling.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<Field.Field orientation="horizontal" data-disabled class="w-fit">
  <Switch id="switch-disabled-unchecked" disabled />
  <Field.Label for="switch-disabled-unchecked">Disabled</Field.Label>
</Field.Field>
```

View Code

## [Invalid](#invalid)

Add the `aria-invalid` prop to the `Switch` component to indicate an invalid state. Add the `data-invalid` prop to the `Field.Field` component for styling.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<Field.Field orientation="horizontal" class="max-w-sm" data-invalid>
  <Field.Content>
    <Field.Label for="switch-terms">Accept terms and conditions</Field.Label>
    <Field.Description
      >You must accept the terms and conditions to continue.</Field.Description
    >
  </Field.Content>
  <Switch id="switch-terms" aria-invalid />
</Field.Field>
```

View Code

## [Size](#size)

Use the `size` prop to change the size of the switch.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<Field.Group class="w-full max-w-[10rem]">
  <Field.Field orientation="horizontal">
    <Switch id="switch-size-sm" size="sm" />
    <Field.Label for="switch-size-sm">Small</Field.Label>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <Switch id="switch-size-default" size="default" />
    <Field.Label for="switch-size-default">Default</Field.Label>
  </Field.Field>
</Field.Group>
```

View Code