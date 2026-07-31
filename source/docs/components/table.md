# Table

A responsive table component.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add table
```

```bash
npx shadcn-svelte@latest add table
```

```bash
bun x shadcn-svelte@latest add table
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Table from "$lib/components/ui/table/index.js";
</script>
```

```svelte
<Table.Root>
  <Table.Caption>A list of your recent invoices.</Table.Caption>
  <Table.Header>
    <Table.Row>
      <Table.Head class="w-[100px]">Invoice</Table.Head>
      <Table.Head>Status</Table.Head>
      <Table.Head>Method</Table.Head>
      <Table.Head class="text-end">Amount</Table.Head>
    </Table.Row>
  </Table.Header>
  <Table.Body>
    <Table.Row>
      <Table.Cell class="font-medium">INV001</Table.Cell>
      <Table.Cell>Paid</Table.Cell>
      <Table.Cell>Credit Card</Table.Cell>
      <Table.Cell class="text-end">$250.00</Table.Cell>
    </Table.Row>
  </Table.Body>
</Table.Root>
```

## [Data Table](#data-table)

You can use the `<Table />` component to build more complex data tables. Combine it with [@tanstack/table](https://tanstack.com/table) to create tables with sorting, filtering and pagination.

See the [Data Table](https://shadcn-svelte.com/docs/components/data-table) documentation for more information.

You can also see an example of a data table in the [Tasks](https://shadcn-svelte.com/examples/tasks) demo.