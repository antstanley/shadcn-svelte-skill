# Avatar

An image element with a fallback for representing the user.

[Docs](https://bits-ui.com/docs/components/avatar)

[API Reference](https://bits-ui.com/docs/components/avatar#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add avatar
```

```bash
npx shadcn-svelte@latest add avatar
```

```bash
bun x shadcn-svelte@latest add avatar
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
```

```svelte
<Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```