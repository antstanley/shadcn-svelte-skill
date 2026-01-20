# Select

Displays a list of options for the user to pick fromtriggered by a button.

[Docs](https://bits-ui.com/docs/components/select)

[API Reference](https://bits-ui.com/docs/components/select#api-reference)

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
  const fruits = [
    { value: "apple", label: "Apple" },
    { value: "banana", label: "Banana" },
    { value: "blueberry", label: "Blueberry" },
    { value: "grapes", label: "Grapes" },
    { value: "pineapple", label: "Pineapple" }
 ];
  let value = $state("");
  const triggerContent = $derived(
    fruits.find((f) => f.value === value)?.label ?? "Select a fruit"
  );
</script>
<Select.Root type="single" name="favoriteFruit" bind:value>
  <Select.Trigger class="w-[180px]">
    {triggerContent}
  </Select.Trigger>
  <Select.Content>
    <Select.Group>
      <Select.Label>Fruits</Select.Label>
      {#each fruits as fruit (fruit.value)}
        <Select.Item
          value={fruit.value}
          label={fruit.label}
          disabled={fruit.value === "grapes"}
        >
          {fruit.label}
        </Select.Item>
      {/each}
    </Select.Group>
  </Select.Content>
</Select.Root>
```

## Installation

```bash
pnpm dlx shadcn-svelte@latest add select
```

```bash
npx shadcn-svelte@latest add select
```

```bash
bun x shadcn-svelte@latest add select
```

## Usage

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
</script>
```

```svelte
<Select.Root type="single">
  <Select.Trigger class="w-[180px]"></Select.Trigger>
  <Select.Content>
    <Select.Item value="light">Light</Select.Item>
    <Select.Item value="dark">Dark</Select.Item>
    <Select.Item value="system">System</Select.Item>
  </Select.Content>
</Select.Root>
```

## Examples

### Scrollable

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
</script>
<Select.Root type="single">
  <Select.Trigger class="w-[280px]">Select a timezone</Select.Trigger>
  <Select.Content>
    <Select.Group>
      <Select.Label>North America</Select.Label>
      <Select.Item value="est">Eastern Standard Time (EST)</Select.Item>
      <Select.Item value="cst">Central Standard Time (CST)</Select.Item>
      <Select.Item value="mst">Mountain Standard Time (MST)</Select.Item>
      <Select.Item value="pst">Pacific Standard Time (PST)</Select.Item>
      <Select.Item value="akst">Alaska Standard Time (AKST)</Select.Item>
      <Select.Item value="hst">Hawaii Standard Time (HST)</Select.Item>
    </Select.Group>
    <Select.Group>
      <Select.Label>Europe & Africa</Select.Label>
      <Select.Item value="gmt">Greenwich Mean Time (GMT)</Select.Item>
      <Select.Item value="cet">Central European Time (CET)</Select.Item>
      <Select.Item value="eet">Eastern European Time (EET)</Select.Item>
      <Select.Item value="west">Western European Summer Time (WEST)</Select.Item
      >
      <Select.Item value="cat">Central Africa Time (CAT)</Select.Item>
      <Select.Item value="eat">East Africa Time (EAT)</Select.Item>
    </Select.Group>
    <Select.Group>
      <Select.Label>Asia</Select.Label>
      <Select.Item value="msk">Moscow Time (MSK)</Select.Item>
      <Select.Item value="ist">India Standard Time (IST)</Select.Item>
      <Select.Item value="cst_china">China Standard Time (CST)</Select.Item>
      <Select.Item value="jst">Japan Standard Time (JST)</Select.Item>
      <Select.Item value="kst">Korea Standard Time (KST)</Select.Item>
      <Select.Item value="ist_indonesia"
        >Indonesia Central Standard Time (WITA)</Select.Item
      >
    </Select.Group>
    <Select.Group>
      <Select.Label>Australia & Pacific</Select.Label>
      <Select.Item value="awst"
        >Australian Western Standard Time (AWST)</Select.Item
      >
      <Select.Item value="acst"
        >Australian Central Standard Time (ACST)</Select.Item
      >
      <Select.Item value="aest"
        >Australian Eastern Standard Time (AEST)</Select.Item
      >
      <Select.Item value="nzst">New Zealand Standard Time (NZST)</Select.Item>
      <Select.Item value="fjt">Fiji Time (FJT)</Select.Item>
    </Select.Group>
    <Select.Group>
      <Select.Label>South America</Select.Label>
      <Select.Item value="art">Argentina Time (ART)</Select.Item>
      <Select.Item value="bot">Bolivia Time (BOT)</Select.Item>
      <Select.Item value="brt">Brasilia Time (BRT)</Select.Item>
      <Select.Item value="clt">Chile Standard Time (CLT)</Select.Item>
    </Select.Group>
  </Select.Content>
</Select.Root>
```