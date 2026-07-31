# Sheet

Extends the Dialog component to display content that complements the main content of the screen.

[Docs](https://bits-ui.com/docs/components/dialog)

[API Reference](https://bits-ui.com/docs/components/dialog#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add sheet
```

```bash
npx shadcn-svelte@latest add sheet
```

```bash
bun x shadcn-svelte@latest add sheet
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Sheet from "$lib/components/ui/sheet/index.js";
</script>
```

```svelte
<Sheet.Root>
  <Sheet.Trigger>Open</Sheet.Trigger>
  <Sheet.Content>
    <Sheet.Header>
      <Sheet.Title>Are you sure absolutely sure?</Sheet.Title>
      <Sheet.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </Sheet.Description>
    </Sheet.Header>
  </Sheet.Content>
</Sheet.Root>
```

## [Examples](#examples)

### [Side](#side)

Pass the `side` property to `<Sheet.Content />` to indicate the edge of the screen where the component will appear. The values can be `top`, `right`, `bottom` or `left`.

### [Size](#size)

You can adjust the size of the sheet using CSS classes:

```svelte
<Sheet.Root>
  <Sheet.Trigger>Open</Sheet.Trigger>
  <Sheet.Content class="w-[400px] sm:w-[540px]">
    <Sheet.Header>
      <Sheet.Title>Are you absolutely sure?</Sheet.Title>
      <Sheet.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </Sheet.Description>
    </Sheet.Header>
  </Sheet.Content>
</Sheet.Root>
```