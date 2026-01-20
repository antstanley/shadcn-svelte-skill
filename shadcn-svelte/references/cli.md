# shadcn-svelte CLI Documentation

The shadcn-svelte CLI provides three main commands for managing components in Svelte projects:

## Init Command
The `init` command sets up a new project by installing dependencies, adding utilities, and configuring CSS variables. During setup, users configure import aliases and select a base color from options including slate, gray, zinc, neutral, or stone.

```bash
pnpm dlx shadcn-svelte@latest init
```

```bash
npx shadcn-svelte@latest init
```

```bash
bun x shadcn-svelte@latest init
```

## Add Command
This command installs individual components or all components to your project. Users can specify which components to add, skip dependency installation, and use the `--overwrite` flag to replace existing files.

```bash
pnpm dlx shadcn-svelte@latest add [component]
```

```bash
npx shadcn-svelte@latest add [component]
```

```bash
bun x shadcn-svelte@latest add [component]
```

## Registry Build Command
The `registry build` command generates registry JSON files from a `registry.json` source file, outputting them to the `static/r` directory by default.

## Proxy Support
The CLI supports proxy configurations through the `--proxy` option or by setting the `HTTP_PROXY` environment variable, enabling requests to work through proxy servers when accessing the shadcn-svelte registry.

All commands offer flexibility through various flags and options, making it easy to customize initialization and component installation workflows.
