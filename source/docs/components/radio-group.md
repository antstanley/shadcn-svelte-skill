# Radio Group

A set of checkable buttonsknown as radio buttonswhere no more than one of the buttons can be checked at a time.

[Docs](https://bits-ui.com/docs/components/radio-group)

[API Reference](https://bits-ui.com/docs/components/radio-group#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<RadioGroup.Root value="comfortable" class="w-fit">
  <div class="flex items-center gap-3">
    <RadioGroup.Item value="default" id="r1" />
    <Label for="r1">Default</Label>
  </div>
  <div class="flex items-center gap-3">
    <RadioGroup.Item value="comfortable" id="r2" />
    <Label for="r2">Comfortable</Label>
  </div>
  <div class="flex items-center gap-3">
    <RadioGroup.Item value="compact" id="r3" />
    <Label for="r3">Compact</Label>
  </div>
</RadioGroup.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add radio-group
```

```bash
npx shadcn-svelte@latest add radio-group
```

```bash
bun x shadcn-svelte@latest add radio-group
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
</script>
```

```svelte
<RadioGroup.Root value="option-one">
  <div class="flex items-center gap-3">
    <RadioGroup.Item value="option-one" id="option-one" />
    <Label for="option-one">Option One</Label>
  </div>
  <div class="flex items-center gap-3">
    <RadioGroup.Item value="option-two" id="option-two" />
    <Label for="option-two">Option Two</Label>
  </div>
</RadioGroup.Root>
```

## [Description](#description)

Radio group items with a description using the `Field` component.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
</script>
<RadioGroup.Root value="comfortable" class="w-fit">
  <Field.Field orientation="horizontal">
    <RadioGroup.Item value="default" id="desc-r1" />
    <Field.Content>
      <Field.Label for="desc-r1">Default</Field.Label>
      <Field.Description>Standard spacing for most use cases.</Field.Description
      >
    </Field.Content>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <RadioGroup.Item value="comfortable" id="desc-r2" />
    <Field.Content>
      <Field.Label for="desc-r2">Comfortable</Field.Label>
      <Field.Description>More space between elements.</Field.Description>
    </Field.Content>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <RadioGroup.Item value="compact" id="desc-r3" />
    <Field.Content>
      <Field.Label for="desc-r3">Compact</Field.Label>
      <Field.Description>Minimal spacing for dense layouts.</Field.Description>
    </Field.Content>
  </Field.Field>
</RadioGroup.Root>
```

View Code

## [Choice Card](#choice-card)

Use `Field.Label` to wrap the entire `Field.Field` for a clickable card-style selection.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
</script>
<RadioGroup.Root value="plus" class="max-w-sm">
  <Field.Label for="plus-plan">
    <Field.Field orientation="horizontal">
      <Field.Content>
        <Field.Title>Plus</Field.Title>
        <Field.Description>For individuals and small teams.</Field.Description>
      </Field.Content>
      <RadioGroup.Item value="plus" id="plus-plan" />
    </Field.Field>
  </Field.Label>
  <Field.Label for="pro-plan">
    <Field.Field orientation="horizontal">
      <Field.Content>
        <Field.Title>Pro</Field.Title>
        <Field.Description>For growing businesses.</Field.Description>
      </Field.Content>
      <RadioGroup.Item value="pro" id="pro-plan" />
    </Field.Field>
  </Field.Label>
  <Field.Label for="enterprise-plan">
    <Field.Field orientation="horizontal">
      <Field.Content>
        <Field.Title>Enterprise</Field.Title>
        <Field.Description>For large teams and enterprises.</Field.Description>
      </Field.Content>
      <RadioGroup.Item value="enterprise" id="enterprise-plan" />
    </Field.Field>
  </Field.Label>
</RadioGroup.Root>
```

View Code

## [Fieldset](#fieldset)

Use `Field.Set` and `Field.Legend` to group radio items with a label and description.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
</script>
<Field.Set class="w-full max-w-xs">
  <Field.Legend variant="label">Subscription Plan</Field.Legend>
  <Field.Description
    >Yearly and lifetime plans offer significant savings.</Field.Description
  >
  <RadioGroup.Root value="monthly">
    <Field.Field orientation="horizontal">
      <RadioGroup.Item value="monthly" id="plan-monthly" />
      <Field.Label for="plan-monthly" class="font-normal"
        >Monthly ($9.99/month)</Field.Label
      >
    </Field.Field>
    <Field.Field orientation="horizontal">
      <RadioGroup.Item value="yearly" id="plan-yearly" />
      <Field.Label for="plan-yearly" class="font-normal"
        >Yearly ($99.99/year)</Field.Label
      >
    </Field.Field>
    <Field.Field orientation="horizontal">
      <RadioGroup.Item value="lifetime" id="plan-lifetime" />
      <Field.Label for="plan-lifetime" class="font-normal"
        >Lifetime ($299.99)</Field.Label
      >
    </Field.Field>
  </RadioGroup.Root>
</Field.Set>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop on `RadioGroup.Item` to disable individual items.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
</script>
<RadioGroup.Root value="option2" class="w-fit">
  <Field.Field orientation="horizontal" data-disabled>
    <RadioGroup.Item value="option1" id="disabled-1" disabled />
    <Field.Label for="disabled-1" class="font-normal">Disabled</Field.Label>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <RadioGroup.Item value="option2" id="disabled-2" />
    <Field.Label for="disabled-2" class="font-normal">Option 2</Field.Label>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <RadioGroup.Item value="option3" id="disabled-3" />
    <Field.Label for="disabled-3" class="font-normal">Option 3</Field.Label>
  </Field.Field>
</RadioGroup.Root>
```

View Code

## [Invalid](#invalid)

Use `aria-invalid` on `RadioGroup.Item` and `data-invalid` on `Field.Field` to show validation errors.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
</script>
<Field.Set class="w-full max-w-xs">
  <Field.Legend variant="label">Notification Preferences</Field.Legend>
  <Field.Description
    >Choose how you want to receive notifications.</Field.Description
  >
  <RadioGroup.Root value="email">
    <Field.Field orientation="horizontal" data-invalid>
      <RadioGroup.Item value="email" id="invalid-email" aria-invalid />
      <Field.Label for="invalid-email" class="font-normal"
        >Email only</Field.Label
      >
    </Field.Field>
    <Field.Field orientation="horizontal" data-invalid>
      <RadioGroup.Item value="sms" id="invalid-sms" aria-invalid />
      <Field.Label for="invalid-sms" class="font-normal">SMS only</Field.Label>
    </Field.Field>
    <Field.Field orientation="horizontal" data-invalid>
      <RadioGroup.Item value="both" id="invalid-both" aria-invalid />
      <Field.Label for="invalid-both" class="font-normal"
        >Both Email & SMS</Field.Label
      >
    </Field.Field>
  </RadioGroup.Root>
</Field.Set>
```

View Code