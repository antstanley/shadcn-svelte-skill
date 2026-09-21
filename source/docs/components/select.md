# Select

Displays a list of options for the user to pick fromtriggered by a button.

[Docs](https://bits-ui.com/docs/components/select)

[API Reference](https://bits-ui.com/docs/components/select#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
  const fruits = [
    { value: "apple", label: "Apple" },
    { value: "banana", label: "Banana" },
    { value: "blueberry", label: "Blueberry" },
    { value: "grapes", label: "Grapes", disabled: true },
    { value: "pineapple", label: "Pineapple" }
 ];
  let value = $state("");
</script>
<Select.Root type="single" name="favoriteFruit" items={fruits} bind:value>
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Select a fruit" />
  </Select.Trigger>
  <Select.Content>
    <Select.Group>
      <Select.Label>Fruits</Select.Label>
      {#each fruits as fruit (fruit.value)}
        <Select.Item
          value={fruit.value}
          label={fruit.label}
          disabled={fruit.disabled}
        >
          {fruit.label}
        </Select.Item>
      {/each}
    </Select.Group>
  </Select.Content>
</Select.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add select
```

```bash
npx shadcn-svelte@latest add select
```

```bash
bun x shadcn-svelte@latest add select
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
</script>
```

```svelte
<Select.Root type="single">
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Select a theme" />
  </Select.Trigger>
  <Select.Content>
    <Select.Item value="light">Light</Select.Item>
    <Select.Item value="dark">Dark</Select.Item>
    <Select.Item value="system">System</Select.Item>
  </Select.Content>
</Select.Root>
``` `Select.Value` renders the label of the selected item, falling back to `placeholder` when nothing is selected.

It reads the label from the matching `Select.Item`, which only exists in the DOM while the menu is open. Pass `items` to `Select.Root` so the label survives the menu closing:

```svelte
<script lang="ts">
  const themes = [
    { value: "light", label: "Light" },
    { value: "dark", label: "Dark" },
    { value: "system", label: "System" },
 ];
</script>
<Select.Root type="single" items={themes}>
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Select a theme" />
  </Select.Trigger>
  <Select.Content>
    {#each themes as theme (theme.value)}
      <Select.Item value={theme.value}>{theme.label}</Select.Item>
    {/each}
  </Select.Content>
</Select.Root>
```

Without `items` the trigger falls back to the raw value, so you only need it when an item's label differs from its value.

## [Examples](#examples)

### [Scrollable](#scrollable)

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
  const timezones = [
    {
      label: "North America",
      options: [
        { value: "est", label: "Eastern Standard Time (EST)" },
        { value: "cst", label: "Central Standard Time (CST)" },
        { value: "mst", label: "Mountain Standard Time (MST)" },
        { value: "pst", label: "Pacific Standard Time (PST)" },
        { value: "akst", label: "Alaska Standard Time (AKST)" },
        { value: "hst", label: "Hawaii Standard Time (HST)" }
     ]
    },
    {
      label: "Europe & Africa",
      options: [
        { value: "gmt", label: "Greenwich Mean Time (GMT)" },
        { value: "cet", label: "Central European Time (CET)" },
        { value: "eet", label: "Eastern European Time (EET)" },
        { value: "west", label: "Western European Summer Time (WEST)" },
        { value: "cat", label: "Central Africa Time (CAT)" },
        { value: "eat", label: "East Africa Time (EAT)" }
     ]
    },
    {
      label: "Asia",
      options: [
        { value: "msk", label: "Moscow Time (MSK)" },
        { value: "ist", label: "India Standard Time (IST)" },
        { value: "cst_china", label: "China Standard Time (CST)" },
        { value: "jst", label: "Japan Standard Time (JST)" },
        { value: "kst", label: "Korea Standard Time (KST)" },
        {
          value: "ist_indonesia",
          label: "Indonesia Central Standard Time (WITA)"
        }
     ]
    },
    {
      label: "Australia & Pacific",
      options: [
        { value: "awst", label: "Australian Western Standard Time (AWST)" },
        { value: "acst", label: "Australian Central Standard Time (ACST)" },
        { value: "aest", label: "Australian Eastern Standard Time (AEST)" },
        { value: "nzst", label: "New Zealand Standard Time (NZST)" },
        { value: "fjt", label: "Fiji Time (FJT)" }
     ]
    },
    {
      label: "South America",
      options: [
        { value: "art", label: "Argentina Time (ART)" },
        { value: "bot", label: "Bolivia Time (BOT)" },
        { value: "brt", label: "Brasilia Time (BRT)" },
        { value: "clt", label: "Chile Standard Time (CLT)" }
     ]
    }
  ];
  const items = timezones.flatMap((group) => group.options);
</script>
<Select.Root type="single" {items}>
  <Select.Trigger class="w-[280px]">
    <Select.Value placeholder="Select a timezone" />
  </Select.Trigger>
  <Select.Content class="max-h-[300px]">
    {#each timezones as group (group.label)}
      <Select.Group>
        <Select.Label>{group.label}</Select.Label>
        {#each group.options as option (option.value)}
          <Select.Item value={option.value} label={option.label}
            >{option.label}</Select.Item
          >
        {/each}
      </Select.Group>
    {/each}
  </Select.Content>
</Select.Root>
```

View Code