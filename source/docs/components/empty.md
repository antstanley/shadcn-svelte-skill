# Empty

Use the Empty component to display an empty state.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add empty
```

```bash
npx shadcn-svelte@latest add empty
```

```bash
bun x shadcn-svelte@latest add empty
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Empty from "$lib/components/ui/empty/index.js";
  import FolderCodeIcon from "@tabler/icons-svelte/icons/folder-code";
</script>
```

```svelte
<Empty.Root>
  <Empty.Header>
    <Empty.Media variant="icon">
      <FolderCodeIcon />
    </Empty.Media>
    <Empty.Title>No data</Empty.Title>
    <Empty.Description>No data found</Empty.Description>
  </Empty.Header>
  <Empty.Content>
    <Button>Add data</Button>
  </Empty.Content>
</Empty.Root>
```

## [Examples](#examples)

### [Outline](#outline)

Use the `border` utility class to create an outline empty state.

View Code

### [Background](#background)

Use the `bg-*` and `bg-gradient-*` utilities to add a background to the empty state.

View Code

### [Avatar](#avatar)

Use the `EmptyMedia` component to display an avatar in the empty state.

View Code

### [Avatar Group](#avatar-group)

Use the `EmptyMedia` component to display an avatar group in the empty state.

View Code

### [InputGroup](#inputgroup)

You can add an `InputGroup` component to the `EmptyContent` component.

View Code