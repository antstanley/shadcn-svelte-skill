# Combobox

Autocomplete input with a list of suggestions.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"];
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {value || "Select a framework"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No items found.</Command.Empty>
        <Command.Group>
          {#each frameworks as framework (framework)}
            <Command.Item
              value={framework}
              data-checked={value === framework}
              onSelect={() => {
                value = framework;
                closeAndFocusTrigger();
              }}
            >
              {framework}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Installation](#installation)

The Combobox is built using a composition of the `<Popover />` and the `<Command />` components.

See installation instructions for the [Popover](https://shadcn-svelte.com/docs/components/popover#installation) and the [Command](https://shadcn-svelte.com/docs/components/command#installation) components.

## [Usage](#usage)

Expand

lib/components/example-combobox.svelte

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"];
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {value || "Select a framework"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No items found.</Command.Empty>
        <Command.Group>
          {#each frameworks as framework (framework)}
            <Command.Item
              value={framework}
              data-checked={value === framework}
              onSelect={() => {
                value = framework;
                closeAndFocusTrigger();
              }}
            >
              {framework}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

Expand

## [Basic](#basic)

A simple combobox with a list of frameworks.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"];
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {value || "Select a framework"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No items found.</Command.Empty>
        <Command.Group>
          {#each frameworks as framework (framework)}
            <Command.Item
              value={framework}
              data-checked={value === framework}
              onSelect={() => {
                value = framework;
                closeAndFocusTrigger();
              }}
            >
              {framework}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Groups](#groups)

Use `<Command.Group />` and `<Command.Separator />` to group items.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const timezones = [
    {
      value: "Americas",
      items: [
        "(GMT-5) New York",
        "(GMT-8) Los Angeles",
        "(GMT-6) Chicago",
        "(GMT-5) Toronto",
        "(GMT-8) Vancouver",
        "(GMT-3) So Paulo"
     ]
    },
    {
      value: "Europe",
      items: [
        "(GMT+0) London",
        "(GMT+1) Paris",
        "(GMT+1) Berlin",
        "(GMT+1) Rome",
        "(GMT+1) Madrid",
        "(GMT+1) Amsterdam"
     ]
    },
    {
      value: "Asia/Pacific",
      items: [
        "(GMT+9) Tokyo",
        "(GMT+8) Shanghai",
        "(GMT+8) Singapore",
        "(GMT+4) Dubai",
        "(GMT+11) Sydney",
        "(GMT+9) Seoul"
     ]
    }
  ];
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-60 justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {value || "Select a timezone"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-60 p-0">
    <Command.Root>
      <Command.Input placeholder="Search timezone..." />
      <Command.List>
        <Command.Empty>No timezones found.</Command.Empty>
        {#each timezones as group, index (group.value)}
          <Command.Group heading={group.value}>
            {#each group.items as item (item)}
              <Command.Item
                value={item}
                data-checked={value === item}
                onSelect={() => {
                  value = item;
                  closeAndFocusTrigger();
                }}
              >
                {item}
              </Command.Item>
            {/each}
          </Command.Group>
          {#if index < timezones.length - 1} <Command.Separator />
          {/if}
        {/each}
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Custom Items](#custom-items)

You can render a custom component inside `<Command.Item />`.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Item from "$lib/components/ui/item/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const countries = [
    { code: "", value: "", continent: "", label: "Select country" },
    {
      code: "ar",
      value: "argentina",
      label: "Argentina",
      continent: "South America"
    },
    {
      code: "au",
      value: "australia",
      label: "Australia",
      continent: "Oceania"
    },
    {
      code: "br",
      value: "brazil",
      label: "Brazil",
      continent: "South America"
    },
    {
      code: "ca",
      value: "canada",
      label: "Canada",
      continent: "North America"
    },
    { code: "cn", value: "china", label: "China", continent: "Asia" },
    {
      code: "co",
      value: "colombia",
      label: "Colombia",
      continent: "South America"
    },
    { code: "eg", value: "egypt", label: "Egypt", continent: "Africa" },
    { code: "fr", value: "france", label: "France", continent: "Europe" },
    { code: "de", value: "germany", label: "Germany", continent: "Europe" },
    { code: "it", value: "italy", label: "Italy", continent: "Europe" },
    { code: "jp", value: "japan", label: "Japan", continent: "Asia" },
    { code: "ke", value: "kenya", label: "Kenya", continent: "Africa" },
    {
      code: "mx",
      value: "mexico",
      label: "Mexico",
      continent: "North America"
    },
    {
      code: "nz",
      value: "new-zealand",
      label: "New Zealand",
      continent: "Oceania"
    },
    { code: "ng", value: "nigeria", label: "Nigeria", continent: "Africa" },
    {
      code: "za",
      value: "south-africa",
      label: "South Africa",
      continent: "Africa"
    },
    {
      code: "kr",
      value: "south-korea",
      label: "South Korea",
      continent: "Asia"
    },
    {
      code: "gb",
      value: "united-kingdom",
      label: "United Kingdom",
      continent: "Europe"
    },
    {
      code: "us",
      value: "united-states",
      label: "United States",
      continent: "North America"
    }
 ];
  const items = countries.filter((country) => country.code !== "");
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {items.find((country) => country.value === value)?.label ||
          "Select country"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search countries..." />
      <Command.List>
        <Command.Empty>No countries found.</Command.Empty>
        <Command.Group>
          {#each items as country (country.code)}
            <Command.Item
              value={country.label}
              data-checked={value === country.value}
              onSelect={() => {
                value = country.value;
                closeAndFocusTrigger();
              }}
            >
              <Item.Root size="xs" class="p-0">
                <Item.Content>
                  <Item.Title class="whitespace-nowrap"
                    >{country.label}</Item.Title
                  >
                  <Item.Description>
                    {country.continent} ({country.code})
                  </Item.Description>
                </Item.Content>
              </Item.Root>
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Invalid](#invalid)

Use the `aria-invalid` prop to make the combobox invalid.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"];
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between font-normal"
        role="combobox"
        aria-expanded={open}
        aria-invalid="true"
      >
        {value || "Select a framework"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No items found.</Command.Empty>
        <Command.Group>
          {#each frameworks as framework (framework)}
            <Command.Item
              value={framework}
              data-checked={value === framework}
              onSelect={() => {
                value = framework;
                closeAndFocusTrigger();
              }}
            >
              {framework}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop to disable the combobox.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"];
  let open = $state(false);
  let value = $state("");
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef} disabled>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-[200px] justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {value || "Select a framework"}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.List>
        <Command.Empty>No items found.</Command.Empty>
        <Command.Group>
          {#each frameworks as framework (framework)}
            <Command.Item
              value={framework}
              data-checked={value === framework}
              onSelect={() => {
                value = framework;
                closeAndFocusTrigger();
              }}
            >
              {framework}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Popup](#popup)

You can trigger the combobox from a button or any other component by using the `child` snippet on `<Popover.Trigger />`. Place the `<Command.Input />` inside the `<Popover.Content />`.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { tick } from "svelte";
  import * as Command from "$lib/components/ui/command/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const countries = [
    { code: "", value: "", continent: "", label: "Select country" },
    {
      code: "ar",
      value: "argentina",
      label: "Argentina",
      continent: "South America"
    },
    {
      code: "au",
      value: "australia",
      label: "Australia",
      continent: "Oceania"
    },
    {
      code: "br",
      value: "brazil",
      label: "Brazil",
      continent: "South America"
    },
    {
      code: "ca",
      value: "canada",
      label: "Canada",
      continent: "North America"
    },
    { code: "cn", value: "china", label: "China", continent: "Asia" },
    {
      code: "co",
      value: "colombia",
      label: "Colombia",
      continent: "South America"
    },
    { code: "eg", value: "egypt", label: "Egypt", continent: "Africa" },
    { code: "fr", value: "france", label: "France", continent: "Europe" },
    { code: "de", value: "germany", label: "Germany", continent: "Europe" },
    { code: "it", value: "italy", label: "Italy", continent: "Europe" },
    { code: "jp", value: "japan", label: "Japan", continent: "Asia" },
    { code: "ke", value: "kenya", label: "Kenya", continent: "Africa" },
    {
      code: "mx",
      value: "mexico",
      label: "Mexico",
      continent: "North America"
    },
    {
      code: "nz",
      value: "new-zealand",
      label: "New Zealand",
      continent: "Oceania"
    },
    { code: "ng", value: "nigeria", label: "Nigeria", continent: "Africa" },
    {
      code: "za",
      value: "south-africa",
      label: "South Africa",
      continent: "Africa"
    },
    {
      code: "kr",
      value: "south-korea",
      label: "South Korea",
      continent: "Asia"
    },
    {
      code: "gb",
      value: "united-kingdom",
      label: "United Kingdom",
      continent: "Europe"
    },
    {
      code: "us",
      value: "united-states",
      label: "United States",
      continent: "North America"
    }
 ];
  let open = $state(false);
  let value = $state(countries[0].label);
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
<Popover.Root bind:open>
  <Popover.Trigger bind:ref={triggerRef}>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        class="w-64 justify-between font-normal"
        role="combobox"
        aria-expanded={open}
      >
        {value}
        <ChevronDownIcon class="text-muted-foreground" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-64 p-0">
    <Command.Root>
      <Command.Input placeholder="Search" />
      <Command.List>
        <Command.Empty>No items found.</Command.Empty>
        <Command.Group>
          {#each countries as country (country.code)}
            <Command.Item
              value={country.label}
              data-checked={value === country.label}
              onSelect={() => {
                value = country.label;
                closeAndFocusTrigger();
              }}
            >
              {country.label}
            </Command.Item>
          {/each}
        </Command.Group>
      </Command.List>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

View Code