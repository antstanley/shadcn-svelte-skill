# Combobox

Autocomplete input and command palette with a list of suggestions.

## Installation

The Combobox is built using a composition of the `<Popover />` and the `<Command />` components.

See installation instructions for the [Popover](/docs/components/popover#installation) and the [Command](/docs/components/command#installation) components.

## Usage

```svelte
<script lang="ts">
  import CheckIcon from "@lucide/svelte/icons/check";
  import ChevronsUpDownIcon from "@lucide/svelte/icons/chevrons-up-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { cn } from "$lib/utils.js";

  const frameworks = [
    { value: "sveltekit", label: "SvelteKit" },
    { value: "next.js", label: "Next.js" },
    { value: "nuxt.js", label: "Nuxt.js" },
    { value: "remix", label: "Remix" },
    { value: "astro", label: "Astro" }
  ];

  let open = $state(false);
  let value = $state("");
  let triggerRef = $state<HTMLButtonElement>(null!);

  const selectedValue = $derived(
    frameworks.find((f) => f.value === value)?.label
  );

  function closeAndFocusTrigger() {
    open = false;
    tick().then(() => {
      triggerRef.focus();
    });
  }
</script>

<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between"
        role="combobox"
        aria-expanded={open}
      >
        {selectedValue || "Select a framework..."}
        <ChevronsUpDownIcon class="opacity-50" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No framework found.</Command.Empty>
        <Command.Group value="frameworks">
          {#each frameworks as framework (framework.value)}
            <Command.Item
              value={framework.value}
              onSelect={() => {
                value = framework.value;
                closeAndFocusTrigger();
              }}
            >
              <CheckIcon
                class={cn(value !== framework.value && "text-transparent")}
              />
              {framework.label}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

## Examples

### Status Popover

Display a status selector with icons:

```svelte
<script lang="ts">
  import CircleIcon from "@lucide/svelte/icons/circle";
  import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
  // ... more status icons

  const statuses = [
    { value: "backlog", label: "Backlog", icon: CircleHelpIcon },
    { value: "todo", label: "Todo", icon: CircleIcon },
    { value: "in progress", label: "In Progress", icon: CircleArrowUpIcon },
    { value: "done", label: "Done", icon: CircleCheckIcon },
    { value: "canceled", label: "Canceled", icon: CircleXIcon }
  ];
</script>
```

### With Dropdown Menu

Combine with dropdown menu for contextual actions:

```svelte
<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    <Button variant="ghost" size="sm">
      <EllipsisIcon />
    </Button>
  </DropdownMenu.Trigger>
  <DropdownMenu.Content>
    <DropdownMenu.Sub>
      <DropdownMenu.SubTrigger>
        <TagsIcon class="me-2 size-4" />
        Apply label
      </DropdownMenu.SubTrigger>
      <DropdownMenu.SubContent class="p-0">
        <Command.Root>
          <Command.Input placeholder="Filter label..." />
          <Command.List>
            {#each labels as label}
              <Command.Item value={label} onSelect={() => selectedLabel = label}>
                {label}
              </Command.Item>
            {/each}
          </Command.List>
        </Command.Root>
      </DropdownMenu.SubContent>
    </DropdownMenu.Sub>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

### Responsive

Use `<Popover />` on desktop and `<Drawer />` on mobile:

```svelte
<script lang="ts">
  import { onMount } from "svelte";
  import { browser } from "$app/environment";

  let isDesktop = $state(false);

  onMount(() => {
    if (browser) {
      isDesktop = window.innerWidth >= 768;
      window.addEventListener("resize", () => {
        isDesktop = window.innerWidth >= 768;
      });
    }
  });
</script>

{#if isDesktop}
  <Popover.Root>
    <!-- Popover content -->
  </Popover.Root>
{:else}
  <Drawer.Root>
    <!-- Drawer content -->
  </Drawer.Root>
{/if}
```
