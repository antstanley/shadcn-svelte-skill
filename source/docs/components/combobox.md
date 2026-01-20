# Combobox

Autocomplete input and command palette with a list of suggestions.

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
    {
      value: "sveltekit",
      label: "SvelteKit"
    },
    {
      value: "next.js",
      label: "Next.js"
    },
    {
      value: "nuxt.js",
      label: "Nuxt.js"
    },
    {
      value: "remix",
      label: "Remix"
    },
    {
      value: "astro",
      label: "Astro"
    }
 ];
  let open = $state(false);
  let value = $state("");
  let triggerRef = $state<HTMLButtonElement>(null!);
  const selectedValue = $derived(
    frameworks.find((f) => f.value === value)?.label
  );
  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
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

## Installation

The Combobox is built using a composition of the `<Popover />` and the `<Command />` components.

See installation instructions for the [Popover](https://shadcn-svelte.com/docs/components/popover#installation) and the [Command](https://shadcn-svelte.com/docs/components/command#installation) components.

## Usage

Expand

lib/components/example-combobox.svelte

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
    {
      value: "sveltekit",
      label: "SvelteKit",
    },
    {
      value: "next.js",
      label: "Next.js",
    },
    {
      value: "nuxt.js",
      label: "Nuxt.js",
    },
    {
      value: "remix",
      label: "Remix",
    },
    {
      value: "astro",
      label: "Astro",
    },
 ];
  let open = $state(false);
  let value = $state("");
  let triggerRef = $state<HTMLButtonElement>(null!);
  const selectedValue = $derived(
    frameworks.find((f) => f.value === value)?.label
  );
  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
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
        variant="outline"
        class="w-[200px] justify-between"
        {...props}
        role="combobox"
        aria-expanded={open}
      >
        {selectedValue || "Select a framework..."}
        <ChevronsUpDownIcon class="ms-2 size-4 shrink-0 opacity-50" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No framework found.</Command.Empty>
        <Command.Group>
          {#each frameworks as framework}
            <Command.Item
              value={framework.value}
              onSelect={() => {
                value = framework.value;
                closeAndFocusTrigger();
              }}
            >
              <CheckIcon
                class={cn(
                  "me-2 size-4",
                  value !== framework.value && "text-transparent"
                )}
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

Expand

## Examples

### Combobox

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
    {
      value: "sveltekit",
      label: "SvelteKit"
    },
    {
      value: "next.js",
      label: "Next.js"
    },
    {
      value: "nuxt.js",
      label: "Nuxt.js"
    },
    {
      value: "remix",
      label: "Remix"
    },
    {
      value: "astro",
      label: "Astro"
    }
 ];
  let open = $state(false);
  let value = $state("");
  let triggerRef = $state<HTMLButtonElement>(null!);
  const selectedValue = $derived(
    frameworks.find((f) => f.value === value)?.label
  );
  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
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

### Popover

```svelte
<script lang="ts">
  import CircleIcon from "@lucide/svelte/icons/circle";
  import CircleArrowUpIcon from "@lucide/svelte/icons/circle-arrow-up";
  import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
  import CircleHelpIcon from "@lucide/svelte/icons/circle-help";
  import CircleXIcon from "@lucide/svelte/icons/circle-x";
  import { type Component, tick } from "svelte";
  import { useId } from "bits-ui";
  import { cn } from "$lib/utils.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import * as Command from "$lib/components/ui/command/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  type Status = {
    value: string;
    label: string;
    icon: Component;
  };
  const statuses: Status[] = [
    {
      value: "backlog",
      label: "Backlog",
      icon: CircleHelpIcon
    },
    {
      value: "todo",
      label: "Todo",
      icon: CircleIcon
    },
    {
      value: "in progress",
      label: "In Progress",
      icon: CircleArrowUpIcon
    },
    {
      value: "done",
      label: "Done",
      icon: CircleCheckIcon
    },
    {
      value: "canceled",
      label: "Canceled",
      icon: CircleXIcon
    }
 ];
  let open = $state(false);
  let value = $state("");
  const selectedStatus = $derived(statuses.find((s) => s.value === value));
  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
  function closeAndFocusTrigger(triggerId: string) {
    open = false;
    tick().then(() => {
      document.getElementById(triggerId)?.focus();
    });
  }
  const triggerId = useId();
</script>
<div class="flex items-center space-x-4">
  <p class="text-muted-foreground text-sm">Status</p>
  <Popover.Root bind:open>
    <Popover.Trigger
      id={triggerId}
      class={buttonVariants({
        variant: "outline",
        size: "sm",
        class: "w-[150px] justify-start"
      })}
    >
      {#if selectedStatus}
        {@const Icon = selectedStatus.icon}
        <Icon class="me-2 size-4 shrink-0" />
        {selectedStatus.label}
      {:else}
        + Set status
      {/if}
    </Popover.Trigger>
    <Popover.Content class="w-[200px] p-0" side="right" align="start">
      <Command.Root>
        <Command.Input placeholder="Change status..." />
        <Command.List>
          <Command.Empty>No results found.</Command.Empty>
          <Command.Group>
            {#each statuses as status (status.value)}
              <Command.Item
                value={status.value}
                onSelect={() => {
                  value = status.value;
                  closeAndFocusTrigger(triggerId);
                }}
              >
                {@const Icon = status.icon}
                <Icon
                  class={cn(
                    "me-2 size-4",
                    status.value !== selectedStatus?.value &&
                      "text-foreground/40"
                  )}
                />
                <span>
                  {status.label}
                </span>
              </Command.Item>
            {/each}
          </Command.Group>
        </Command.List>
      </Command.Root>
    </Popover.Content>
  </Popover.Root>
</div>
```

### Dropdown menu

```svelte
<script lang="ts">
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import EllipsisIcon from "@lucide/svelte/icons/ellipsis";
  import TagsIcon from "@lucide/svelte/icons/tags";
  import TrashIcon from "@lucide/svelte/icons/trash";
  import UserIcon from "@lucide/svelte/icons/user";
  import { tick } from "svelte";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as Command from "$lib/components/ui/command/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const labels = [
    "feature",
    "bug",
    "enhancement",
    "documentation",
    "design",
    "question",
    "maintenance"
 ];
  let open = $state(false);
  let selectedLabel = $state("feature");
  let triggerRef = $state<HTMLButtonElement>(null!);
  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
  function closeAndFocusTrigger() {
    open = false;
    tick().then(() => {
      triggerRef.focus();
    });
  }
</script>
<div
  class="flex w-full flex-col items-start justify-between rounded-md border px-4 py-3 sm:flex-row sm:items-center"
>
  <p class="text-sm leading-none font-medium">
    <span
      class="bg-primary text-primary-foreground me-2 rounded-lg px-2 py-1 text-xs"
    >
      {selectedLabel}
    </span>
    <span class="text-muted-foreground">Create a new project</span>
  </p>
  <DropdownMenu.Root bind:open>
    <DropdownMenu.Trigger bind:ref={triggerRef}>
      {#snippet child({ props })}
        <Button variant="ghost" size="sm" {...props} aria-label="Open menu">
          <EllipsisIcon />
        </Button>
      {/snippet}
    </DropdownMenu.Trigger>
    <DropdownMenu.Content class="w-[200px]" align="end">
      <DropdownMenu.Group>
        <DropdownMenu.Label>Actions</DropdownMenu.Label>
        <DropdownMenu.Item>
          <UserIcon class="me-2 size-4" />
          Assign to...
        </DropdownMenu.Item>
        <DropdownMenu.Item>
          <CalendarIcon class="me-2 size-4" />
          Set due date...
        </DropdownMenu.Item>
        <DropdownMenu.Separator />
        <DropdownMenu.Sub>
          <DropdownMenu.SubTrigger>
            <TagsIcon class="me-2 size-4" />
            Apply label
          </DropdownMenu.SubTrigger>
          <DropdownMenu.SubContent class="p-0">
            <Command.Root value={selectedLabel}>
              <Command.Input autofocus placeholder="Filter label..." />
              <Command.List>
                <Command.Empty>No label found.</Command.Empty>
                <Command.Group>
                  {#each labels as label (label)}
                    <Command.Item
                      value={label}
                      onSelect={() => {
                        selectedLabel = label;
                        closeAndFocusTrigger();
                      }}
                    >
                      {label}
                    </Command.Item>
                  {/each}
                </Command.Group>
              </Command.List>
            </Command.Root>
          </DropdownMenu.SubContent>
        </DropdownMenu.Sub>
        <DropdownMenu.Separator />
        <DropdownMenu.Item class="text-red-600">
          <TrashIcon class="me-2 size-4" />
          Delete
          <DropdownMenu.Shortcut></DropdownMenu.Shortcut>
        </DropdownMenu.Item>
      </DropdownMenu.Group>
    </DropdownMenu.Content>
  </DropdownMenu.Root>
</div>
```

### Responsive

You can create a responsive combobox by using the `<Popover />` on desktop and the `<Drawer />` components on mobile.

```svelte
<script lang="ts">
  import { browser } from "$app/environment";
  import { Button } from "$lib/components/ui/button/index.js";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Drawer from "$lib/components/ui/drawer/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { onMount } from "svelte";
  type Status = {
    value: string;
    label: string;
  };
  const statuses: Status[] = [
    {
      value: "backlog",
      label: "Backlog"
    },
    {
      value: "todo",
      label: "Todo"
    },
    {
      value: "in progress",
      label: "In Progress"
    },
    {
      value: "done",
      label: "Done"
    },
    {
      value: "canceled",
      label: "Canceled"
    }
 ];
  let open = $state(false);
  let selectedStatus: Status | null = $state(null);
  let isDesktop = $state(false);
  function checkScreenSize() {
    isDesktop = window.innerWidth >= 768;
  }
  onMount(() => {
    if (browser) {
      checkScreenSize();
      window.addEventListener("resize", checkScreenSize);
      return () => window.removeEventListener("resize", checkScreenSize);
    }
  });
  function handleStatusSelect(value: string) {
    selectedStatus = statuses.find((status) => status.value === value) || null;
    open = false;
  }
</script>
{#if isDesktop}
  <Popover.Root bind:open>
    <Popover.Trigger>
      <Button variant="outline" class="w-[150px] justify-start">
        {selectedStatus ? selectedStatus.label : "+ Set status"}
      </Button>
    </Popover.Trigger>
    <Popover.Content class="w-[200px] p-0" align="start">
      <Command.Root>
        <Command.Input placeholder="Filter status..." />
        <Command.List>
          <Command.Empty>No results found.</Command.Empty>
          <Command.Group>
            {#each statuses as status (status.value)}
              <Command.Item
                value={status.value}
                onSelect={() => handleStatusSelect(status.value)}
              >
                {status.label}
              </Command.Item>
            {/each}
          </Command.Group>
        </Command.List>
      </Command.Root>
    </Popover.Content>
  </Popover.Root>
{:else}
  <Drawer.Root bind:open>
    <Drawer.Trigger>
      <Button variant="outline" class="w-[150px] justify-start">
        {selectedStatus ? selectedStatus.label : "+ Set status"}
      </Button>
    </Drawer.Trigger>
    <Drawer.Content>
      <div class="mt-4 border-t">
        <Command.Root>
          <Command.Input placeholder="Filter status..." />
          <Command.List>
            <Command.Empty>No results found.</Command.Empty>
            <Command.Group>
              {#each statuses as status (status.value)}
                <Command.Item
                  value={status.value}
                  onSelect={() => handleStatusSelect(status.value)}
                >
                  {status.label}
                </Command.Item>
              {/each}
            </Command.Group>
          </Command.List>
        </Command.Root>
      </div>
    </Drawer.Content>
  </Drawer.Root>
{/if}
```