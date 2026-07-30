# Radio Group

A set of checkable buttonsknown as radio buttonswhere no more than one of the buttons can be checked at a time.

[Docs](https://bits-ui.com/docs/components/radio-group)

[API Reference](https://bits-ui.com/docs/components/radio-group#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

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
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="option-one" id="option-one" />
    <Label for="option-one">Option One</Label>
  </div>
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="option-two" id="option-two" />
    <Label for="option-two">Option Two</Label>
  </div>
</RadioGroup.Root>
```