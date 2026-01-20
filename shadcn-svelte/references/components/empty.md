# Empty

Use the Empty component to display a empty state.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add empty
```

```bash
npx shadcn-svelte@latest add empty
```

```bash
bun x shadcn-svelte@latest add empty
```

## Usage

```svelte
<script lang="ts">
  import * as Empty from "$lib/components/ui/empty/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import FolderIcon from "@lucide/svelte/icons/folder";
</script>

<Empty.Root>
  <Empty.Header>
    <Empty.Media variant="icon">
      <FolderIcon />
    </Empty.Media>
    <Empty.Title>No projects</Empty.Title>
    <Empty.Description>
      Get started by creating a new project.
    </Empty.Description>
  </Empty.Header>
  <Empty.Content>
    <Button>Create project</Button>
  </Empty.Content>
</Empty.Root>
```

## Components

- **Empty.Root** - Main wrapper container
- **Empty.Header** - Contains media, title, and description
- **Empty.Media** - Displays icons, avatars, or avatar groups
- **Empty.Title** - Headline text
- **Empty.Description** - Supporting text
- **Empty.Content** - Action buttons or interactive elements

## Examples

### With Outline Border

```svelte
<Empty.Root class="border border-dashed">
  <!-- content -->
</Empty.Root>
```

### With Background

```svelte
<Empty.Root class="bg-gradient-to-b from-muted/50 to-muted">
  <!-- content -->
</Empty.Root>
```

### With Avatar

```svelte
<Empty.Media variant="avatar">
  <Avatar.Root>
    <Avatar.Image src="/avatar.png" />
    <Avatar.Fallback>JD</Avatar.Fallback>
  </Avatar.Root>
</Empty.Media>
```

### With Search Input

```svelte
<Empty.Content>
  <InputGroup.Root>
    <InputGroup.Input placeholder="Search..." />
    <InputGroup.Addon>
      <Kbd>⌘K</Kbd>
    </InputGroup.Addon>
  </InputGroup.Root>
</Empty.Content>
```

## Common Use Cases

- Project creation prompts
- File upload interfaces
- Notification centers
- Team member invitations
- 404 error pages
- Search results with no matches
