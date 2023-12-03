---
title: "The [latest] GPTs family"
description: "Cutting-Edge AI meeting Human Expertise to fuel your coding journey."
layout: base
date: 2023-11-15
---
## Introduction
Recent advancements in Large Language Models (LLMs) and generative AI have significantly enhanced our ability to process and utilize vast amounts of information. Tools like ChatGPT have showcased impressive adeptness in understanding programming languages, offering coding assistance, and even generating code snippets. Despite its proficiency, ChatGPT and similar models inherently face a crucial limitation: the knowledge cut-off. 
Due to the time gap between their training and deployment, these AI models often lack the most current updates and understandings of rapidly evolving programming languages, libraries, and frameworks, which is crucial for developers in fast-evolving domains like software development.

**[latest] GPTs** addresses this issue by implementing a dynamic, continuously updated knowledge base, effectively bridging the knowledge gap.

## Available [latest] GPTs

- <img src="/assets/vuejs/vuejs-logo.svg" height="16" /> [Vue.js GPTs](/gpts/vuejs/)
- <img src="/assets/fastapi/fastapi-logo.svg" height="20" style="margin-right:4px;"/>[FastAPI GPTs](/gpts/fastapi/)
- 🗳️ What's next? [You decide..](https://app.formbricks.com/s/clpiu0pdy2vylqg72ki5ikev0)

### Knowledge retrieval

All the **[latest] GPTs** are equiped with a curated knowledge file that describes all new features, breaking changes, deprecations and bug fixes of a library since the last version that the GPT-4 is literate in. 
To create these knowledge files, an **hybrid approach** is employed, combining the powers of AI with human experience🤯. First AI algorithms skim through vast amounts of data to summarize key changes. Each AI-generated summary then undergoes a **human review**. This step ensures the accuracy, relevance, and comprehensiveness of the information, filtering out noise and preserving only what’s crucial.
The goal is to condense this ocean of information into a compact, potent knowledge file🤌. This **minimizes knowledge retrieval time**, whilst empowering developers with swift, **state-of-the-art** coding asssistance. 

### Presets/Conversation starters ⚙️

For many libraries and frameworks, there is more than one way to "do it right". Take [Vue.js](https://vuejs.org) for example, some people prefere to use its Options API, without TypeScritp, while other use the Composition API with TypeScript. It quickly becomes tiresome to always have to explain to your coding assistant which syntax/API you want to use. Therefore we are utilizing the "Conversation starters" feature of the OpenAI GPTs to quickly let you enhance the assistant with important context information 🚀.

If you have an idea for a preset, [leave us feedback](/README.md#contribution-guidelines) or create an issue.

### Tests & Performance 🌡️

Our promise: Coding assistants that are always up-to-date with the latest features of your favorite libraries and frameworks 😇. To ensure this, we are conducting several tests with each of our **[latest] GPTs**. Each test focuses on a feature/deprecation of a specific version of a library. The tests are conducted with the **[latest] GPT** and a "plain GPT" that has the same instructions as the **[latest] GPT** but no access to a knowledge file. This way we can compare the performance of the **[latest] GPTs** to that of ChatGPT.

If you have an idea for a test, [leave us feedback](/README.md#contribution-guidelines) or create an issue.
