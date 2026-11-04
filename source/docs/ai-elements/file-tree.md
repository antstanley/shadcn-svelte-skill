# File Tree

The files the agent changed, as a folder tree.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import FileTreeNode, { type FileNode } from "$lib/components/file-tree/file-tree-node.svelte";
 const files: FileNode[] = [
  {
   type: "folder",
   name: "app",
   path: "app",
   children: [
    { type: "file", name: "layout.tsx", path: "app/layout.tsx" },
    { type: "file", name: "page.tsx", path: "app/page.tsx" },
  ],
  },
  {
   type: "folder",
   name: "components",
   path: "components",
   children: [
    {
     type: "folder",
     name: "ui",
     path: "components/ui",
     children: [
      {
       type: "file",
       name: "button.tsx",
       path: "components/ui/button.tsx",
      },
    ],
    },
    {
     type: "file",
     name: "login-form.tsx",
     path: "components/login-form.tsx",
    },
   ],
  },
 ];
 let selected = $state("components/ui/button.tsx");
</script>
<div class="flex w-full max-w-xs flex-col py-6 text-sm">
 {#each files as node (node.path)}
  <FileTreeNode {node} {selected} onSelect={(path) => (selected = path)} />
 {/each}
</div>
```

View Code

File Tree is the files the agent changed, shown as folders you can open. A folder is a [Collapsible](https://shadcn-svelte.com/docs/components/collapsible). A file is a [Button](https://shadcn-svelte.com/docs/components/button). For a single file the agent read or edited, use a [Tool](https://shadcn-svelte.com/docs/ai-elements/tool) line instead.

## [Installation](#installation)

File Tree is built with the [Collapsible](https://shadcn-svelte.com/docs/components/collapsible) and [Button](https://shadcn-svelte.com/docs/components/button) components.

```bash
pnpm dlx shadcn-svelte@latest add collapsible button
```

```bash
npx shadcn-svelte@latest add collapsible button
```

```bash
bun x shadcn-svelte@latest add collapsible button
```

## [Usage](#usage)

Render nodes recursively. Nest each folder's children in its `Collapsible.Content`.

```svelte
{#if node.type === "folder"}
  <Collapsible.Root open class="group/folder">
    <Collapsible.Trigger>
      {#snippet child({ props })}
        <Button
          {...props}
          variant="ghost"
          size="sm"
          class="w-full justify-start"
        >
          <ChevronRightIcon
            class="transition-transform group-data-[state=open]/folder:rotate-90"
          />
          <FolderIcon />
          {node.name}
        </Button>
      {/snippet}
    </Collapsible.Trigger>
    <Collapsible.Content>
      <div class="ml-4 flex flex-col">
        {#each node.children as child (child.path)}
          <FileTreeNode node={child} />
        {/each}
      </div>
    </Collapsible.Content>
  </Collapsible.Root>
{/if}
```

```svelte
<Button
  variant="ghost"
  size="sm"
  class="w-full justify-start"
  onclick={() => onSelect(node.path)}
>
  <FileIcon />
  {node.name}
</Button>
```

See [Collapsible](https://shadcn-svelte.com/docs/components/collapsible#file-tree).