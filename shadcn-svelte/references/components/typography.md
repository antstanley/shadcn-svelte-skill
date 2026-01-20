# Typography

Styles for headings, paragraphs, lists, etc.

We do not ship any typography styles by default. Use Tailwind CSS utility classes to style text elements.

## Headings

### h1

```svelte
<h1 class="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
  Taxing Laughter: The Joke Tax Chronicles
</h1>
```

### h2

```svelte
<h2 class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0">
  The People of the Kingdom
</h2>
```

### h3

```svelte
<h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">
  The Joke Tax
</h3>
```

### h4

```svelte
<h4 class="scroll-m-20 text-xl font-semibold tracking-tight">
  People stopped telling jokes
</h4>
```

## Paragraph

```svelte
<p class="leading-7 [&:not(:first-child)]:mt-6">
  The king, seeing how much happier his subjects were, realized the error of his
  ways and repealed the joke tax.
</p>
```

## Blockquote

```svelte
<blockquote class="mt-6 border-s-2 ps-6 italic">
  "After all," he said, "everyone enjoys a good joke, so it's only fair that
  they should pay for the privilege."
</blockquote>
```

## List

```svelte
<ul class="my-6 ms-6 list-disc [&>li]:mt-2">
  <li>1st level of puns: 5 gold coins</li>
  <li>2nd level of jokes: 10 gold coins</li>
  <li>3rd level of one-liners: 20 gold coins</li>
</ul>
```

## Table

```svelte
<div class="my-6 w-full overflow-y-auto">
  <table class="w-full">
    <thead>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <th class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
          King's Treasury
        </th>
        <th class="border px-4 py-2 text-left font-bold [&[align=center]]:text-center [&[align=right]]:text-right">
          People's happiness
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
          Empty
        </td>
        <td class="border px-4 py-2 text-left [&[align=center]]:text-center [&[align=right]]:text-right">
          Overflowing
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Inline Code

```svelte
<code class="bg-muted relative rounded px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold">
  @radix-ui/react-alert-dialog
</code>
```

## Lead

```svelte
<p class="text-muted-foreground text-xl">
  A modal dialog that interrupts the user with important content and expects a
  response.
</p>
```

## Large

```svelte
<div class="text-lg font-semibold">Are you absolutely sure?</div>
```

## Small

```svelte
<small class="text-sm font-medium leading-none">Email address</small>
```

## Muted

```svelte
<p class="text-muted-foreground text-sm">Enter your email address.</p>
```
