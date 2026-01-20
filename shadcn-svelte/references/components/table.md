# Table

A responsive table component.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add table
```

```bash
npx shadcn-svelte@latest add table
```

```bash
bun x shadcn-svelte@latest add table
```

## Usage

```svelte
<script lang="ts">
  import * as Table from "$lib/components/ui/table/index.js";
</script>

<Table.Root>
  <Table.Caption>A list of your recent invoices.</Table.Caption>
  <Table.Header>
    <Table.Row>
      <Table.Head class="w-[100px]">Invoice</Table.Head>
      <Table.Head>Status</Table.Head>
      <Table.Head>Method</Table.Head>
      <Table.Head class="text-right">Amount</Table.Head>
    </Table.Row>
  </Table.Header>
  <Table.Body>
    <Table.Row>
      <Table.Cell class="font-medium">INV001</Table.Cell>
      <Table.Cell>Paid</Table.Cell>
      <Table.Cell>Credit Card</Table.Cell>
      <Table.Cell class="text-right">$250.00</Table.Cell>
    </Table.Row>
  </Table.Body>
  <Table.Footer>
    <Table.Row>
      <Table.Cell colspan={3}>Total</Table.Cell>
      <Table.Cell class="text-right">$2,500.00</Table.Cell>
    </Table.Row>
  </Table.Footer>
</Table.Root>
```

## Examples

### With Data

```svelte
<script lang="ts">
  import * as Table from "$lib/components/ui/table/index.js";

  const invoices = [
    { invoice: "INV001", status: "Paid", method: "Credit Card", amount: "$250.00" },
    { invoice: "INV002", status: "Pending", method: "PayPal", amount: "$150.00" },
    { invoice: "INV003", status: "Unpaid", method: "Bank Transfer", amount: "$350.00" },
  ];
</script>

<Table.Root>
  <Table.Header>
    <Table.Row>
      <Table.Head>Invoice</Table.Head>
      <Table.Head>Status</Table.Head>
      <Table.Head>Method</Table.Head>
      <Table.Head class="text-right">Amount</Table.Head>
    </Table.Row>
  </Table.Header>
  <Table.Body>
    {#each invoices as invoice}
      <Table.Row>
        <Table.Cell class="font-medium">{invoice.invoice}</Table.Cell>
        <Table.Cell>{invoice.status}</Table.Cell>
        <Table.Cell>{invoice.method}</Table.Cell>
        <Table.Cell class="text-right">{invoice.amount}</Table.Cell>
      </Table.Row>
    {/each}
  </Table.Body>
</Table.Root>
```

## Components

- **Table.Root** - Main container
- **Table.Header** - Table header section
- **Table.Body** - Table body section
- **Table.Footer** - Table footer section
- **Table.Row** - Table row
- **Table.Head** - Header cell
- **Table.Cell** - Body cell
- **Table.Caption** - Table caption

## Advanced Usage

For sorting, filtering, and pagination, combine with [TanStack Table](/docs/components/data-table).
