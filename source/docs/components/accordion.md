# Accordion

A vertically stacked set of interactive headings that each reveal a section of content.

[Docs](https://bits-ui.com/docs/components/accordion)

[API Reference](https://bits-ui.com/docs/components/accordion#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as Accordion from "$lib/components/ui/accordion/index.js";
</script>
<Accordion.Root type="single" value="shipping" class="max-w-lg">
 <Accordion.Item value="shipping">
  <Accordion.Trigger>What are your shipping options?</Accordion.Trigger>
  <Accordion.Content>
   We offer standard (5-7 days), express (2-3 days), and overnight shipping. Free shipping on
   international orders.
  </Accordion.Content>
 </Accordion.Item>
 <Accordion.Item value="returns">
  <Accordion.Trigger>What is your return policy?</Accordion.Trigger>
  <Accordion.Content>
   Returns accepted within 30 days. Items must be unused and in original packaging. Refunds
   processed within 5-7 business days.
  </Accordion.Content>
 </Accordion.Item>
 <Accordion.Item value="support">
  <Accordion.Trigger>How can I contact customer support?</Accordion.Trigger>
  <Accordion.Content>
   Reach us via email, live chat, or phone. We respond within 24 hours during business days.
  </Accordion.Content>
 </Accordion.Item>
</Accordion.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add accordion
```

```bash
npx shadcn-svelte@latest add accordion
```

```bash
bun x shadcn-svelte@latest add accordion
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Accordion from "$lib/components/ui/accordion/index.js";
</script>
```

```svelte
<Accordion.Root type="single">
  <Accordion.Item value="item-1">
    <Accordion.Trigger>Is it accessible?</Accordion.Trigger>
    <Accordion.Content>
      Yes. It adheres to the WAI-ARIA design pattern.
    </Accordion.Content>
  </Accordion.Item>
</Accordion.Root>
```

## [Basic](#basic)

A basic accordion that shows one item at a time. The first item is open by default.

```svelte
<script lang="ts">
 import * as Accordion from "$lib/components/ui/accordion/index.js";
 const items = [
  {
   value: "item-1",
   trigger: "How do I reset my password?",
   content:
    "Click on 'Forgot Password' on the login page, enter your email address, and we'll send you a link to reset your password. The link will expire in 24 hours.",
  },
  {
   value: "item-2",
   trigger: "Can I change my subscription plan?",
   content:
    "Yes, you can upgrade or downgrade your plan at any time from your account settings. Changes will be reflected in your next billing cycle.",
  },
  {
   value: "item-3",
   trigger: "What payment methods do you accept?",
   content:
    "We accept all major credit cards, PayPal, and bank transfers. All payments are processed securely through our payment partners.",
  },
];
</script>
<Accordion.Root type="single" value="item-1" class="max-w-lg">
 {#each items as item (item.value)}
  <Accordion.Item value={item.value}>
   <Accordion.Trigger>{item.trigger}</Accordion.Trigger>
   <Accordion.Content>{item.content}</Accordion.Content>
  </Accordion.Item>
 {/each}
</Accordion.Root>
```

View Code

## [Multiple](#multiple)

Use `type="multiple"` to allow multiple items to be open at the same time.

```svelte
<script lang="ts">
 import * as Accordion from "$lib/components/ui/accordion/index.js";
 const items = [
  {
   value: "notifications",
   trigger: "Notification Settings",
   content:
    "Manage how you receive notifications. You can enable email alerts for updates or push notifications for mobile devices.",
  },
  {
   value: "privacy",
   trigger: "Privacy & Security",
   content:
    "Control your privacy settings and security preferences. Enable two-factor authentication, manage connected devices, review active sessions, and configure data sharing preferences. You can also download your data or delete your account.",
  },
  {
   value: "billing",
   trigger: "Billing & Subscription",
   content:
    "View your current plan, payment history, and upcoming invoices. Update your payment method, change your subscription tier, or cancel your subscription.",
  },
];
</script>
<Accordion.Root type="multiple" value={["notifications"]} class="max-w-lg">
 {#each items as item (item.value)}
  <Accordion.Item value={item.value}>
   <Accordion.Trigger>{item.trigger}</Accordion.Trigger>
   <Accordion.Content>{item.content}</Accordion.Content>
  </Accordion.Item>
 {/each}
</Accordion.Root>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop on `Accordion.Item` to disable individual items.

```svelte
<script lang="ts">
 import * as Accordion from "$lib/components/ui/accordion/index.js";
</script>
<Accordion.Root type="single" class="w-full">
 <Accordion.Item value="item-1">
  <Accordion.Trigger>Can I access my account history?</Accordion.Trigger>
  <Accordion.Content>
   Yes, you can view your complete account history including all transactions, plan changes, and
   support tickets in the Account History section of your dashboard.
  </Accordion.Content>
 </Accordion.Item>
 <Accordion.Item value="item-2" disabled>
  <Accordion.Trigger>Premium feature information</Accordion.Trigger>
  <Accordion.Content>
   This section contains information about premium features. Upgrade your plan to access this
   content.
  </Accordion.Content>
 </Accordion.Item>
 <Accordion.Item value="item-3">
  <Accordion.Trigger>How do I update my email address?</Accordion.Trigger>
  <Accordion.Content>
   You can update your email address in your account settings. You'll receive a verification
   email at your new address to confirm the change.
  </Accordion.Content>
 </Accordion.Item>
</Accordion.Root>
```

View Code

## [Borders](#borders)

Add `border` to the `Accordion.Root` and `border-b last:border-b-0` to the `Accordion.Item` to add borders to the items.

```svelte
<script lang="ts">
 import * as Accordion from "$lib/components/ui/accordion/index.js";
 const items = [
  {
   value: "billing",
   trigger: "How does billing work?",
   content:
    "We offer monthly and annual subscription plans. Billing is charged at the beginning of each cycle, and you can cancel anytime. All plans include automatic backups, 24/7 support, and unlimited team members.",
  },
  {
   value: "security",
   trigger: "Is my data secure?",
   content:
    "Yes. We use end-to-end encryption, SOC 2 Type II compliance, and regular third-party security audits. All data is encrypted at rest and in transit using industry-standard protocols.",
  },
  {
   value: "integration",
   trigger: "What integrations do you support?",
   content:
    "We integrate with 500+ popular tools including Slack, Zapier, Salesforce, HubSpot, and more. You can also build custom integrations using our REST API and webhooks.",
  },
];
</script>
<Accordion.Root type="single" value="billing" class="max-w-lg rounded-lg border">
 {#each items as item (item.value)}
  <Accordion.Item value={item.value} class="border-b px-4 last:border-b-0">
   <Accordion.Trigger>{item.trigger}</Accordion.Trigger>
   <Accordion.Content>{item.content}</Accordion.Content>
  </Accordion.Item>
 {/each}
</Accordion.Root>
```

View Code

## [Card](#card)

Wrap the `Accordion.Root` in a `Card` component.

```svelte
<script lang="ts">
 import * as Accordion from "$lib/components/ui/accordion/index.js";
 import * as Card from "$lib/components/ui/card/index.js";
 const items = [
  {
   value: "plans",
   trigger: "What subscription plans do you offer?",
   content:
    "We offer three subscription tiers: Starter ($9/month), Professional ($29/month), and Enterprise ($99/month). Each plan includes increasing storage limits, API access, priority support, and team collaboration features.",
  },
  {
   value: "billing",
   trigger: "How does billing work?",
   content:
    "Billing occurs automatically at the start of each billing cycle. We accept all major credit cards, PayPal, and ACH transfers for enterprise customers. You'll receive an invoice via email after each payment.",
  },
  {
   value: "cancel",
   trigger: "How do I cancel my subscription?",
   content:
    "You can cancel your subscription anytime from your account settings. There are no cancellation fees or penalties. Your access will continue until the end of your current billing period.",
  },
];
</script>
<Card.Root class="w-full max-w-sm">
 <Card.Header>
  <Card.Title>Subscription & Billing</Card.Title>
  <Card.Description>
   Common questions about your account, plans, payments and cancellations.
  </Card.Description>
 </Card.Header>
 <Card.Content>
  <Accordion.Root type="single" value="plans">
   {#each items as item (item.value)}
    <Accordion.Item value={item.value}>
     <Accordion.Trigger>{item.trigger}</Accordion.Trigger>
     <Accordion.Content>{item.content}</Accordion.Content>
    </Accordion.Item>
   {/each}
  </Accordion.Root>
 </Card.Content>
</Card.Root>
```

View Code