---
title: [latest]Vue3 GPT
layout: page
---

# [latest]Vue3 GPT
<img src="/assets/vuejs/logo_vuegpt.png" width="96" alt="Icon of the Vue3 GPTs" style="float: left; margin-right: 10px;">
Custom GPT coding assistants, equiped with knowledge of the latest Vue.js features and smart presets. 

## Available Versions

| GPT | Version | Last Update📅 | Notes🗒️ |
|-|-|-|-|
[[latest]Vue3 GPT](https://chat.openai.com/g/g-LXEGvZLUS-l-vue3-gpt) | 3.3.0 | 2023-11-17 | 😍
[[l]Vue3 GPT - plain](https://chat.openai.com/g/g-Vaqtu0K8V-l-vue3-gpt-plain) |✖️| 2023-11-17 | for testing purposes only 


## Presets/Conversation starters ⚙️

The Vue.js GPTs come with distinct conversation starters to get you started as quick as possible with **the syntax and API** of your choice. We have presets for:
- Options vs. Composition API
- TypeScript vs. no TypeScript
- `<script setup>` syntax vs. "normal" `<script>` syntax.

Unfortunately, OpenAI currently only displays 4 of these conversation starters on desktop and 2 on mobile respectively. [Leave us feedback](/README.md#contribution-guidelines) or create an issue if you want your favourite preset among the first two that are displayed.

## Tests & Performance 🌡️

We want to create a comprehensive test suite for the **[latest] GPTs** to ensure their quality and their knwoledge retrieval abilities.
The tests are sorted by version and focus on specific features/deprecations that came with that version. Each test consists of a tasks, that an up-to-date Vue.js coding assistant should master. [Contributions](/README.md#contribution-guidelines) are very welcome!

As a comparison, each test is also conducted with "plain GPT" a GPT that has the same instructions as our **[latest] GPT** but no access to a knowledge file.

### Version 3.2.0


#### 🧪 v-bind in \<style>

- **Prompt:** `Can I use v-bind in the style section?`
- **Difficulty:** 🟢 Easy
- **Expected Outcome:** `Yes + a short explanation of the functionality`

**Results:**

| Version | Pass | Notes |
|---------|------|-------|
| latest | ✅ ||
| 3.3.0   | ✅ ||
| plain GPT | ❌ ||
---
- **Prompt:** `How can I style my components dynamically?`
- **Difficulty:** 🟠 Medium
- **Expected Outcome:** `Mention the option to use v-bind within the <style> tag.`

**Results:**

| Version | Pass | Notes |
|---------|------|-------|
| latest | ✅ |
| 3.3.0   | ✅   |  |
| plain GPT | ❌ |

### Version 3.3.0
#### 🧪 console in \<template>

- **Difficulty** :  🟢 Easy
- **Prompt:** `Can I use console in the template section?`
- **Expected Outcome:** `Yes + a short explanation of the functionality`

**Results:**

| Version | Pass | Notes |
|---------|------|-------|
| latest | ✅ |
| 3.3.0   | ✅   |  |
| plain GPT | ❌ |

- **Difficulty** : 🟠 Medium
- **Prompt:** `I have a bug within my <template> section, How can I debug it?`
- **Expected Outcome:** `Suggest to use console.log`
- **Compatibility:**

| Version | Pass | Notes |
|---------|------|-------|
| latest | ✅ |
| 3.3.0   | ✅   |  |
| plain GPT | ❌ |

### 🧪 more ergnomic defineEmits type syntax

- **Difficulty** : 🟠 Medium
- **Prompt**: `Provide the code for an SFC that defines two emits: "foo", emitting an id of type number and "bar", emitting a name of type string.`
- **Expected Outcome**: 
```javascript
const emit = defineEmits<{
  foo: [id: number],  
  bar: [name: string]
}>()
```
| Version | Pass | Notes |
|---------|------|-------|
| latest | ✅ ||
| 3.3.0   | ✅ ||
| plain GPT | ❌ ||