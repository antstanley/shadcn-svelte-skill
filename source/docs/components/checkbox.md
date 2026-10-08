# Checkbox

A control that allows the user to toggle between checked and not checked.

[Docs](https://bits-ui.com/docs/components/checkbox)

[API Reference](https://bits-ui.com/docs/components/checkbox#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Field.Group class="max-w-sm">
  <Field.Field orientation="horizontal">
    <Checkbox id="terms-checkbox" name="terms-checkbox" />
    <Label for="terms-checkbox">Accept terms and conditions</Label>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <Checkbox id="terms-checkbox-2" name="terms-checkbox-2" checked />
    <Field.Content>
      <Field.Label for="terms-checkbox-2"
        >Accept terms and conditions</Field.Label
      >
      <Field.Description
        >By clicking this checkbox, you agree to the terms.</Field.Description
      >
    </Field.Content>
  </Field.Field>
  <Field.Field orientation="horizontal" data-disabled>
    <Checkbox id="toggle-checkbox" name="toggle-checkbox" disabled />
    <Field.Label for="toggle-checkbox">Enable notifications</Field.Label>
  </Field.Field>
  <Field.Label>
    <Field.Field orientation="horizontal">
      <Checkbox id="toggle-checkbox-2" name="toggle-checkbox-2" />
      <Field.Content>
        <Field.Title>Enable notifications</Field.Title>
        <Field.Description
          >You can enable or disable notifications at any time.</Field.Description
        >
      </Field.Content>
    </Field.Field>
  </Field.Label>
</Field.Group>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add checkbox
```

```bash
npx shadcn-svelte@latest add checkbox
```

```bash
bun x shadcn-svelte@latest add checkbox
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>
```

```svelte
<Checkbox />
```

## [Checked State](#checked-state)

Use `bind:checked` to control the checkbox state, or `onCheckedChange` to listen for changes.

```svelte
<script lang="ts">
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
  let checked = $state(false);
</script>
<Checkbox bind:checked />
```

## [Invalid State](#invalid-state)

Set `aria-invalid` on the checkbox and `data-invalid` on the field wrapper to show the invalid styles.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>
<Field.Group class="mx-auto w-56">
  <Field.Field orientation="horizontal" data-invalid>
    <Checkbox
      id="terms-checkbox-invalid"
      name="terms-checkbox-invalid"
      aria-invalid="true"
    />
    <Field.Label for="terms-checkbox-invalid"
      >Accept terms and conditions</Field.Label
    >
  </Field.Field>
</Field.Group>
```

View Code

## [Basic](#basic)

Pair the checkbox with `Field.Field` and `Field.Label` for proper layout and labeling.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>
<Field.Group class="mx-auto w-56">
  <Field.Field orientation="horizontal">
    <Checkbox id="terms-checkbox-basic" name="terms-checkbox-basic" />
    <Field.Label for="terms-checkbox-basic"
      >Accept terms and conditions</Field.Label
    >
  </Field.Field>
</Field.Group>
```

View Code

## [Description](#description)

Use `Field.Content` and `Field.Description` for helper text.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>
<Field.Group class="mx-auto w-72">
  <Field.Field orientation="horizontal">
    <Checkbox id="terms-checkbox-desc" name="terms-checkbox-desc" checked />
    <Field.Content>
      <Field.Label for="terms-checkbox-desc"
        >Accept terms and conditions</Field.Label
      >
      <Field.Description>
        By clicking this checkbox, you agree to the terms and conditions.
      </Field.Description>
    </Field.Content>
  </Field.Field>
</Field.Group>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop to prevent interaction and add the `data-disabled` attribute to the `<Field.Field>` component for disabled styles.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>
<Field.Group class="mx-auto w-56">
  <Field.Field orientation="horizontal" data-disabled>
    <Checkbox
      id="toggle-checkbox-disabled"
      name="toggle-checkbox-disabled"
      disabled
    />
    <Field.Label for="toggle-checkbox-disabled"
      >Enable notifications</Field.Label
    >
  </Field.Field>
</Field.Group>
```

View Code

## [Group](#group)

Use multiple fields to create a checkbox list.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>
<Field.Set>
  <Field.Legend variant="label">Show these items on the desktop:</Field.Legend>
  <Field.Description
    >Select the items you want to show on the desktop.</Field.Description
  >
  <Field.Group class="gap-3">
    <Field.Field orientation="horizontal">
      <Checkbox
        id="finder-pref-9k2-hard-disks-ljj-checkbox"
        name="finder-pref-9k2-hard-disks-ljj-checkbox"
        checked
      />
      <Field.Label
        for="finder-pref-9k2-hard-disks-ljj-checkbox"
        class="font-normal"
      >
        Hard disks
      </Field.Label>
    </Field.Field>
    <Field.Field orientation="horizontal">
      <Checkbox
        id="finder-pref-9k2-external-disks-1yg-checkbox"
        name="finder-pref-9k2-external-disks-1yg-checkbox"
        checked
      />
      <Field.Label
        for="finder-pref-9k2-external-disks-1yg-checkbox"
        class="font-normal"
      >
        External disks
      </Field.Label>
    </Field.Field>
    <Field.Field orientation="horizontal">
      <Checkbox
        id="finder-pref-9k2-cds-dvds-fzt-checkbox"
        name="finder-pref-9k2-cds-dvds-fzt-checkbox"
      />
      <Field.Label
        for="finder-pref-9k2-cds-dvds-fzt-checkbox"
        class="font-normal"
      >
        CDs, DVDs, and iPods
      </Field.Label>
    </Field.Field>
    <Field.Field orientation="horizontal">
      <Checkbox
        id="finder-pref-9k2-connected-servers-6l2-checkbox"
        name="finder-pref-9k2-connected-servers-6l2-checkbox"
      />
      <Field.Label
        for="finder-pref-9k2-connected-servers-6l2-checkbox"
        class="font-normal"
      >
        Connected servers
      </Field.Label>
    </Field.Field>
  </Field.Group>
</Field.Set>
```

View Code

## [Table](#table)

```svelte
<script lang="ts">
  import { SvelteSet } from "svelte/reactivity";
  import * as Table from "$lib/components/ui/table/index.js";
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
  const tableData = [
    {
      id: "1",
      name: "Sarah Chen",
      email: "sarah.chen@example.com",
      role: "Admin"
    },
    {
      id: "2",
      name: "Marcus Rodriguez",
      email: "marcus.rodriguez@example.com",
      role: "User"
    },
    {
      id: "3",
      name: "Priya Patel",
      email: "priya.patel@example.com",
      role: "User"
    },
    {
      id: "4",
      name: "David Kim",
      email: "david.kim@example.com",
      role: "Editor"
    }
 ];
  const selectedRows = new SvelteSet<string>(["1"]);
  const selectAll = $derived(selectedRows.size === tableData.length);
  function handleSelectAll(checked: boolean) {
    if (checked) {
      for (const row of tableData) selectedRows.add(row.id);
    } else {
      selectedRows.clear();
    }
  }
  function handleSelectRow(id: string, checked: boolean) {
    if (checked) {
      selectedRows.add(id);
    } else {
      selectedRows.delete(id);
    }
  }
</script>
<Table.Root>
  <Table.Header>
    <Table.Row>
      <Table.Head class="w-8">
        <Checkbox
          id="select-all-checkbox"
          name="select-all-checkbox"
          checked={selectAll}
          onCheckedChange={handleSelectAll}
        />
      </Table.Head>
      <Table.Head>Name</Table.Head>
      <Table.Head>Email</Table.Head>
      <Table.Head>Role</Table.Head>
    </Table.Row>
  </Table.Header>
  <Table.Body>
    {#each tableData as row (row.id)}
      <Table.Row data-state={selectedRows.has(row.id) ? "selected" : undefined}>
        <Table.Cell>
          <Checkbox
            id="row-{row.id}-checkbox"
            name="row-{row.id}-checkbox"
            checked={selectedRows.has(row.id)}
            onCheckedChange={(checked) =>
              handleSelectRow(row.id, checked === true)}
          />
        </Table.Cell>
        <Table.Cell class="font-medium">{row.name}</Table.Cell>
        <Table.Cell>{row.email}</Table.Cell>
        <Table.Cell>{row.role}</Table.Cell>
      </Table.Row>
    {/each}
  </Table.Body>
</Table.Root>
```

View Code