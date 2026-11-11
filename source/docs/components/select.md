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
  { value: "grapes", label: "Grapes" },
  { value: "pineapple", label: "Pineapple" },
];
 let value = $state("");
</script>
<Select.Root type="single" name="favoriteFruit" items={fruits} bind:value>
 <Select.Trigger class="w-full max-w-48">
  <Select.Value placeholder="Select a fruit" />
 </Select.Trigger>
 <Select.Content>
  <Select.Group>
   <Select.Label>Fruits</Select.Label>
   {#each fruits as fruit (fruit.value)}
    <Select.Item value={fruit.value} label={fruit.label}>
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

## [Groups](#groups)

Use `Select.Group`, `Select.Label`, and `Select.Separator` to organize items.

```svelte
<script lang="ts">
 import * as Select from "$lib/components/ui/select/index.js";
 const fruits = [
  { value: "apple", label: "Apple" },
  { value: "banana", label: "Banana" },
  { value: "blueberry", label: "Blueberry" },
];
 const vegetables = [
  { value: "carrot", label: "Carrot" },
  { value: "broccoli", label: "Broccoli" },
  { value: "spinach", label: "Spinach" },
];
 let value = $state("");
</script>
<Select.Root type="single" items={[...fruits, ...vegetables]} bind:value>
 <Select.Trigger class="w-full max-w-48">
  <Select.Value placeholder="Select a fruit" />
 </Select.Trigger>
 <Select.Content>
  <Select.Group>
   <Select.Label>Fruits</Select.Label>
   {#each fruits as fruit (fruit.value)}
    <Select.Item value={fruit.value} label={fruit.label}>{fruit.label}</Select.Item>
   {/each}
  </Select.Group>
  <Select.Separator />
  <Select.Group>
   <Select.Label>Vegetables</Select.Label>
   {#each vegetables as vegetable (vegetable.value)}
    <Select.Item value={vegetable.value} label={vegetable.label}>{vegetable.label}</Select.Item>
   {/each}
  </Select.Group>
 </Select.Content>
</Select.Root>
```

View Code

## [Scrollable](#scrollable)

A select with many items that scrolls.

```svelte
<script lang="ts">
 import * as Select from "$lib/components/ui/select/index.js";
 const timezones = [
  {
   label: "North America",
   options: [
    { value: "est", label: "Eastern Standard Time" },
    { value: "cst", label: "Central Standard Time" },
    { value: "mst", label: "Mountain Standard Time" },
    { value: "pst", label: "Pacific Standard Time" },
    { value: "akst", label: "Alaska Standard Time" },
    { value: "hst", label: "Hawaii Standard Time" },
  ],
  },
  {
   label: "Europe & Africa",
   options: [
    { value: "gmt", label: "Greenwich Mean Time" },
    { value: "cet", label: "Central European Time" },
    { value: "eet", label: "Eastern European Time" },
    { value: "west", label: "Western European Summer Time" },
    { value: "cat", label: "Central Africa Time" },
    { value: "eat", label: "East Africa Time" },
  ],
  },
  {
   label: "Asia",
   options: [
    { value: "msk", label: "Moscow Time" },
    { value: "ist", label: "India Standard Time" },
    { value: "cst_china", label: "China Standard Time" },
    { value: "jst", label: "Japan Standard Time" },
    { value: "kst", label: "Korea Standard Time" },
    { value: "ist_indonesia", label: "Indonesia Central Standard Time" },
  ],
  },
  {
   label: "Australia & Pacific",
   options: [
    { value: "awst", label: "Australian Western Standard Time" },
    { value: "acst", label: "Australian Central Standard Time" },
    { value: "aest", label: "Australian Eastern Standard Time" },
    { value: "nzst", label: "New Zealand Standard Time" },
    { value: "fjt", label: "Fiji Time" },
  ],
  },
  {
   label: "South America",
   options: [
    { value: "art", label: "Argentina Time" },
    { value: "bot", label: "Bolivia Time" },
    { value: "brt", label: "Brasilia Time" },
    { value: "clt", label: "Chile Standard Time" },
  ],
  },
 ];
 const items = timezones.flatMap((group) => group.options);
</script>
<Select.Root type="single" {items}>
 <Select.Trigger class="w-full max-w-64">
  <Select.Value placeholder="Select a timezone" />
 </Select.Trigger>
 <Select.Content>
  {#each timezones as group (group.label)}
   <Select.Group>
    <Select.Label>{group.label}</Select.Label>
    {#each group.options as option (option.value)}
     <Select.Item value={option.value} label={option.label}>{option.label}</Select.Item>
    {/each}
   </Select.Group>
  {/each}
 </Select.Content>
</Select.Root>
```

View Code

## [Disabled](#disabled)

```svelte
<script lang="ts">
 import * as Select from "$lib/components/ui/select/index.js";
 const fruits = [
  { value: "apple", label: "Apple" },
  { value: "banana", label: "Banana" },
  { value: "blueberry", label: "Blueberry" },
  { value: "grapes", label: "Grapes", disabled: true },
  { value: "pineapple", label: "Pineapple" },
];
 let value = $state("");
</script>
<Select.Root type="single" items={fruits} bind:value disabled>
 <Select.Trigger class="w-full max-w-48">
  <Select.Value placeholder="Select a fruit" />
 </Select.Trigger>
 <Select.Content>
  <Select.Group>
   {#each fruits as fruit (fruit.value)}
    <Select.Item value={fruit.value} label={fruit.label} disabled={fruit.disabled}>
     {fruit.label}
    </Select.Item>
   {/each}
  </Select.Group>
 </Select.Content>
</Select.Root>
```

View Code

## [Invalid](#invalid)

Add the `data-invalid` attribute to the `Field.Field` component and the `aria-invalid` attribute to the `Select.Trigger` component to show an error state.

```svelte
<Field.Field data-invalid>
  <Field.Label>Fruit</Field.Label>
  <Select.Trigger aria-invalid>
    <Select.Value />
  </Select.Trigger>
</Field.Field>
```

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import * as Select from "$lib/components/ui/select/index.js";
 const fruits = [
  { value: "apple", label: "Apple" },
  { value: "banana", label: "Banana" },
  { value: "blueberry", label: "Blueberry" },
];
 let value = $state("");
</script>
<Field.Field data-invalid class="w-full max-w-48">
 <Field.Label>Fruit</Field.Label>
 <Select.Root type="single" items={fruits} bind:value>
  <Select.Trigger aria-invalid>
   <Select.Value placeholder="Select a fruit" />
  </Select.Trigger>
  <Select.Content>
   <Select.Group>
    {#each fruits as fruit (fruit.value)}
     <Select.Item value={fruit.value} label={fruit.label}>{fruit.label}</Select.Item>
    {/each}
   </Select.Group>
  </Select.Content>
 </Select.Root>
 <Field.Error>Please select a fruit.</Field.Error>
</Field.Field>
```

View Code