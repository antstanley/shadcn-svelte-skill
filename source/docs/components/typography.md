# Typography

Styles for headings, paragraphs, lists, etc.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

We do not ship any typography styles by default. This page is an example of how you can use utility classes to style your text.

## [h1](#h1)

```svelte
<h1
  class="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance"
>
  Taxing Laughter: The Joke Tax Chronicles
</h1>
```

View Code

## [h2](#h2)

```svelte
<h2
  class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0"
>
  The People of the Kingdom
</h2>
```

View Code

## [h3](#h3)

```svelte
<h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">The Joke Tax</h3>
```

View Code

## [h4](#h4)

```svelte
<h4 class="scroll-m-20 text-xl font-semibold tracking-tight">
  People stopped telling jokes
</h4>
```

View Code

## [p](#p)

```svelte
<p class="leading-7 [&:not(:first-child)]:mt-6">
  The king, seeing how much happier his subjects were, realized the error of his
  ways and repealed the joke tax.
</p>
```

View Code

## [blockquote](#blockquote)

```svelte
<blockquote class="mt-6 border-s-2 ps-6 italic">
  "After all," he said, "everyone enjoys a good joke, so it's only fair that
  they should pay for the privilege."
</blockquote>
```

View Code

## [table](#table)

```svelte
<div class="my-6 w-full overflow-y-auto">
  <table class="w-full">
    <thead>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <th
          class="border px-4 py-2 text-start font-bold [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          King's Treasury
        </th>
        <th
          class="border px-4 py-2 text-start font-bold [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          People's happiness
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <td
          class="border px-4 py-2 text-start [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          Empty
        </td>
        <td
          class="border px-4 py-2 text-start [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          Overflowing
        </td>
      </tr>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <td
          class="border px-4 py-2 text-start [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          Modest
        </td>
        <td
          class="border px-4 py-2 text-start [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          Satisfied
        </td>
      </tr>
      <tr class="m-0 border-t p-0 even:bg-muted">
        <td
          class="border px-4 py-2 text-start [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          Full
        </td>
        <td
          class="border px-4 py-2 text-start [&[align=center]]:text-center [&[align=right]]:text-end"
        >
          Ecstatic
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

View Code

## [list](#list)

```svelte
<ul class="my-6 ms-6 list-disc [&>li]:mt-2">
  <li>1st level of puns: 5 gold coins</li>
  <li>2nd level of jokes: 10 gold coins</li>
  <li>3rd level of one-liners : 20 gold coins</li>
</ul>
```

View Code

## [Inline code](#inline-code)

```svelte
<code
  class="relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold"
>
  @lucide/svelte
</code>
```

View Code

## [Lead](#lead)

```svelte
<p class="text-xl text-muted-foreground">
  A modal dialog that interrupts the user with important content and expects a
  response.
</p>
```

View Code

## [Large](#large)

```svelte
<div class="text-lg font-semibold">Are you absolutely sure?</div>
```

View Code

## [Small](#small)

```svelte
<small class="text-sm leading-none font-medium">Email address</small>
```

View Code

## [Muted](#muted)

```svelte
<p class="text-sm text-muted-foreground">Enter your email address.</p>
```

View Code