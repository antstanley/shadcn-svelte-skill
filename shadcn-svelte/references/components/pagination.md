# Pagination

Pagination with page navigation, next and previous links.

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

<Pagination.Root count={100} perPage={10}>
  {#snippet children({ pages, currentPage })}
    <Pagination.Content>
      <Pagination.Item>
        <Pagination.PrevButton />
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
        <Pagination.NextButton />
      </Pagination.Item>
    </Pagination.Content>
  {/snippet}
</Pagination.Root>
```

## Components

- **Pagination.Root** - Main container with `count` and `perPage` props
- **Pagination.Content** - Wrapper for pagination items
- **Pagination.Item** - Individual pagination item wrapper
- **Pagination.Link** - Page number link
- **Pagination.PrevButton** - Previous page button
- **Pagination.NextButton** - Next page button
- **Pagination.Ellipsis** - Indicator for skipped pages

## Props

### Root

- `count` - Total number of items
- `perPage` - Items per page
- `page` - Current page (controlled)
- `onPageChange` - Callback when page changes
