# Pagination

Pagination with page navigation, next and previous links.

[Docs](https://bits-ui.com/docs/components/pagination)

[API Reference](https://bits-ui.com/docs/components/pagination#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Pagination from "$lib/components/ui/pagination/index.js";
</script>
<Pagination.Root count={30} perPage={10} page={2}>
  {#snippet children({ pages, currentPage })}
    <Pagination.Content>
      <Pagination.Item>
        <Pagination.Previous />
      </Pagination.Item>
      {#each pages as page (page.key)}
        {#if page.type === "ellipsis"}
          <Pagination.Item>
            <Pagination.Ellipsis />
          </Pagination.Item>
        {:else}
          <Pagination.Item>
            <Pagination.Link {page} isActive={currentPage === page.value}>
              {page.value}
            </Pagination.Link>
          </Pagination.Item>
        {/if}
      {/each}
      <Pagination.Item>
        <Pagination.Ellipsis />
      </Pagination.Item>
      <Pagination.Item>
        <Pagination.Next />
      </Pagination.Item>
    </Pagination.Content>
  {/snippet}
</Pagination.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add pagination
```

```bash
npx shadcn-svelte@latest add pagination
```

```bash
bun x shadcn-svelte@latest add pagination
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Pagination from "$lib/components/ui/pagination/index.js";
</script>
```

```svelte
<Pagination.Root count={100} perPage={10}>
  {#snippet children({ pages, currentPage })}
    <Pagination.Content>
      <Pagination.Item>
        <Pagination.Previous />
      </Pagination.Item>
      {#each pages as page (page.key)}
        {#if page.type === "ellipsis"}
          <Pagination.Item>
            <Pagination.Ellipsis />
          </Pagination.Item>
        {:else}
          <Pagination.Item>
            <Pagination.Link {page} isActive={currentPage === page.value}>
              {page.value}
            </Pagination.Link>
          </Pagination.Item>
        {/if}
      {/each}
      <Pagination.Item>
        <Pagination.Next />
      </Pagination.Item>
    </Pagination.Content>
  {/snippet}
</Pagination.Root>
```

## [Simple](#simple)

A simple pagination with only page numbers.

```svelte
<script lang="ts">
  import * as Pagination from "$lib/components/ui/pagination/index.js";
</script>
<Pagination.Root count={50} perPage={10} page={2}>
  {#snippet children({ pages, currentPage })}
    <Pagination.Content>
      {#each pages as page (page.key)}
        {#if page.type === "page"}
          <Pagination.Item>
            <Pagination.Link {page} isActive={currentPage === page.value}>
              {page.value}
            </Pagination.Link>
          </Pagination.Item>
        {/if}
      {/each}
    </Pagination.Content>
  {/snippet}
</Pagination.Root>
```

View Code

## [Icons Only](#icons-only)

Use just the previous and next buttons without page numbers. This is useful for data tables with a rows per page selector.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Pagination from "$lib/components/ui/pagination/index.js";
  import * as Select from "$lib/components/ui/select/index.js";
  const rowsPerPage = ["10", "25", "50", "100"];
  let perPage = $state("25");
</script>
<div class="flex items-center justify-between gap-4">
  <Field.Field orientation="horizontal" class="w-fit">
    <Field.Label for="select-rows-per-page">Rows per page</Field.Label>
    <Select.Root type="single" bind:value={perPage}>
      <Select.Trigger class="w-20" id="select-rows-per-page">
        <Select.Value />
      </Select.Trigger>
      <Select.Content align="start">
        <Select.Group>
          {#each rowsPerPage as rows (rows)}
            <Select.Item value={rows} label={rows}>{rows}</Select.Item>
          {/each}
        </Select.Group>
      </Select.Content>
    </Select.Root>
  </Field.Field>
  <Pagination.Root count={100} perPage={Number(perPage)} class="mx-0 w-auto">
    <Pagination.Content>
      <Pagination.Item>
        <Pagination.Previous />
      </Pagination.Item>
      <Pagination.Item>
        <Pagination.Next />
      </Pagination.Item>
    </Pagination.Content>
  </Pagination.Root>
</div>
```

View Code