# Pagination

Pagination with page navigation, next and previous links.

[Docs](https://bits-ui.com/docs/components/pagination)

[API Reference](https://bits-ui.com/docs/components/pagination#api-reference)

```svelte
<script lang="ts">
  import * as Pagination from "$lib/components/ui/pagination/index.js";
</script>
<Pagination.Root count={30} page={2}>
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

## Installation

```bash
pnpm dlx shadcn-svelte@latest add pagination
```

```bash
npx shadcn-svelte@latest add pagination
```

```bash
bun x shadcn-svelte@latest add pagination
```

## Usage

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