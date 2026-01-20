# Data Table

Powerful table and datagrids built using TanStack Table.

## About

This guide teaches you how to build custom data tables using TanStack Table v8 and Svelte 5. The approach emphasizes flexibility rather than one-size-fits-all solutions.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add table
pnpm add @tanstack/table-core
```

```bash
npx shadcn-svelte@latest add table
npm install @tanstack/table-core
```

```bash
bun x shadcn-svelte@latest add table
bun add @tanstack/table-core
```

## Project Structure

```
src/routes/payments/
├── columns.ts          # Column definitions
├── data-table.svelte   # Main table component
├── data-table-actions.svelte
└── +page.svelte
```

## Basic Setup

### Define Columns

```ts
// columns.ts
import type { ColumnDef } from "@tanstack/table-core";

export type Payment = {
  id: string;
  amount: number;
  status: "pending" | "processing" | "success" | "failed";
  email: string;
};

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "status",
    header: "Status",
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "amount",
    header: "Amount",
  },
];
```

### Create Data Table

```svelte
<!-- data-table.svelte -->
<script lang="ts">
  import { createSvelteTable, getCoreRowModel, flexRender } from "@tanstack/svelte-table";
  import * as Table from "$lib/components/ui/table/index.js";
  import { columns, type Payment } from "./columns.js";

  let { data }: { data: Payment[] } = $props();

  const table = createSvelteTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });
</script>

<Table.Root>
  <Table.Header>
    {#each table.getHeaderGroups() as headerGroup}
      <Table.Row>
        {#each headerGroup.headers as header}
          <Table.Head>
            {#if !header.isPlaceholder}
              {flexRender(header.column.columnDef.header, header.getContext())}
            {/if}
          </Table.Head>
        {/each}
      </Table.Row>
    {/each}
  </Table.Header>
  <Table.Body>
    {#each table.getRowModel().rows as row}
      <Table.Row>
        {#each row.getVisibleCells() as cell}
          <Table.Cell>
            {flexRender(cell.column.columnDef.cell, cell.getContext())}
          </Table.Cell>
        {/each}
      </Table.Row>
    {/each}
  </Table.Body>
</Table.Root>
```

## Features

The data table supports:

- **Cell formatting** - Custom rendering for currency, dates, etc.
- **Row actions** - Dropdown menus for per-row operations
- **Pagination** - Built-in page navigation
- **Sorting** - Clickable column headers
- **Filtering** - Search inputs to filter data
- **Column visibility** - Toggle columns on/off
- **Row selection** - Checkboxes for selecting rows

See the [TanStack Table documentation](https://tanstack.com/table/latest) for more details.
