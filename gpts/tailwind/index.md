---
title: Tailwind CSS GPT from [latest] GPTs family
description: A custom GPT coding assistant, equiped with knowledge of the latest Tailwind CSS features and smart presets.
layout: base
date: 2023-12-04
---
# [latest] Tailwind CSS GPT

<img src="/assets/gpts/tailwind/logo_tailwindgpt.webp" width="96" alt="Icon of the Tailwind GPTs" style="float: left; margin-right: 10px;">
An up-to-date, state-of-the-art coding assistant for Tailwind CSS, the utility-first CSS framework. As [all our coding assistants](/gpts/), it is equiped with curated knowledge of the latest Tailwind CSS features and smart presets. 

<br>
## Available Versions

| GPT | Version | Last Update📅 | Notes🗒️ |
|---|---|---|---|
| [[latest] Tailwind CSS GPT](https://chat.openai.com/g/g-qrreXSScH-latest-tailwind-css-gpt) | 3.4.1 | 2024-01-08 | 😍 |
| [[3.3.7] Tailwind CSS GPT](https://chat.openai.com/g/g-qPiMDcJT7) | 3.3.7 | 2023-12-18 | |

## Presets

The coding assistant is configured to be a concise and meticulous Web developer that adheres to latest standards and best practices. It should optimize for performance and accessibility, DRY code and modern CSS features. For now it does not make use of any conversation starters to customize developer experience, but feel free to let us know if there is anything we should add to the presets by [opening an issue](/README.md#contribution-guidelines).

## Tests & Performance 🌡️

### Version 3.4.0

#### 🧪 `has-*`, `group-has-*`, and `peer-has-*`

- **Difficulty** : 🟠 Medium
- **Prompt**: `I want to style a parent container based on its child. Is that posiible?`
- **Expected Outcome**: `Yes with the new :has() pseudo-class`

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ | Sometimes gives a not working example of the has-* variant  |
| 3.3.7   | ❌ |   |

#### 🧪 `text-wrap` utilities

- **Difficulty** : 🟠 Medium
- **Prompt**: `I don't want to have a single word on a line in my headlines. How can I prevent that?`
- **Expected Outcome**: `Use the new text-wrap balanced utility`

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| 3.3.7   | ❌ |   |

#### 🧪 `size-` utilities

- **Difficulty** : 🟢 Easy
- **Prompt**: `How can I set the width and height of an element at the same time?`
- **Expected Outcome**: `Use the size-* utility`

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| 3.3.7   | ❌ |   |

- **Difficulty** : 🔴 Hard
- **Prompt**: `I need a square element. How can I achieve that?`
- **Expected Outcome**: `Use the size-* utility instead of w-* and h-*`

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| 3.3.7   | ❌ |   |

#### 🧪 direct child selector

- **Difficulty** : 🟢 Easy
- **Prompt**: `How can I style the children of an element?`
- **Expected Outcome**: `Use the * variant`

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| 3.3.7   | ❌ |   |

- **Difficulty** : 🟠 Medium
- **Prompt**: `I have a list of <div> elements within a container and want to style them all at once. How can I do that?`
- **Expected Outcome**: `Use the * variant to style all direct children of the`

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| 3.3.7   | ❌ |   |


### Version 3.3.3

Tests will follow.


