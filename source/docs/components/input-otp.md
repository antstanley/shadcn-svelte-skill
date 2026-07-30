# Input OTP

Accessible one-time password component with copy paste functionality.

[Docs](https://bits-ui.com/docs/components/pin-input)

[API Reference](https://bits-ui.com/docs/components/pin-input#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [About](#about)

Input OTP is built on top of Bits UI's [PinInput](https://bits-ui.com/docs/components/pin-input) which is inspired by [@guilherme\_rodz](https://twitter.com/guilherme_rodz)'s Input OTP component.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add input-otp
```

```bash
npx shadcn-svelte@latest add input-otp
```

```bash
bun x shadcn-svelte@latest add input-otp
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
```

```svelte
<InputOTP.Root maxlength={6}>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells.slice(0, 3) as cell}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
    <InputOTP.Separator />
    <InputOTP.Group>
      {#each cells.slice(3, 6) as cell}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>
```

## [Examples](#examples)

### [Pattern](#pattern)

Use the `pattern` prop to define a custom pattern for the OTP input.

View Code

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
  import { REGEXP_ONLY_DIGITS_AND_CHARS } from "bits-ui";
</script>
<InputOTP.Root maxlength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
</InputOTP.Root>
```

### [Separator](#separator)

You can use the `InputOTP.Separator` component to add a separator between the groups of cells.

View Code

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
<InputOTP.Root maxlength={4}>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells.slice(0, 2) as cell}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
    <InputOTP.Separator />
    <InputOTP.Group>
      {#each cells.slice(2, 4) as cell}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>
```

### [Controlled](#controlled)

View Code

### [Form](#form)

View Code