---
title: FastAPI GPTs from [latest] GPTs
description: A custom GPT coding assistant, equiped with knowledge of the latest FastAPI features and smart presets.
layout: base
---
# [latest]FastAPI GPT

<img src="/assets/fastapi/logo_fastapigpt.png" width="96" alt="Icon of the FastAPI GPTs" style="float: left; margin-right: 10px;">
Custom GPT coding assistants, equiped with knowledge of the latest FastAPI features and smart presets. 

## Available Versions

| GPT | Version | Last Update📅 | Notes🗒️ |
|---|---|---|---|
| [[latest]FastAPI GPT](https://chat.openai.com/g/g-BhYCAfVXk-latest-fastapi-gpt) | 0.104.0 | 2023-11-22 | 😍 |
| [[l]FastAPI GPT- plain](https://chat.openai.com/g/g-UXYVWTbat-latest-fastapi-gpt-plain) | ✖️ | 2023-11-22 | for testing purposes only |


## Tests & Performance 🌡️

We want to create a comprehensive test suite for the **[latest] GPTs** to ensure their quality and their knwoledge retrieval abilities.
The tests are sorted by version and focus on specific features/deprecations that came with that version. Each test consists of a tasks, that an up-to-date Vue.js coding assistant should master. [Contributions](/README.md#contribution-guidelines) are very welcome!

As a comparison, each test is also conducted with "plain GPT" a GPT that has the same instructions as our **[latest] GPT** but no access to a knowledge file.

### Version 0.89.0

#### 🧪 return type annotations to declare the response_model

- **Prompt:** `Can OpenAPI deduce the response_model from the return type annotation?`
- **Difficulty:** 🟢 Easy
- **Expected Outcome:** `Yes + a short explanation of the functionality`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| plain GPT | ❌ |   |

---
- **Prompt:** `Show me an example route that returns a object of type Item(BaseModel).`
- **Difficulty:** 🔴 Hard
- **Expected Outcome:** `The usage of a return type annotation instead of using the response_model parameter`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ❌ | Often suggest to use a return type, but it does not explain why.  |
| plain GPT | ❌ |   |

---
### Version 0.93.0

#### 🧪 lifespan async context managers

- **Prompt:** `I have some heavy computation to do once for my entire application. How can I do that?`
- **Difficulty:** 🟡 Medium
- **Expected Outcome:** `suggest @asynccontextmanager and lifespan events instead of startup and shutdown`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| plain GPT | ❌ |   |

---

### Version 0.95.0

#### 🧪 Usage of Annotated

- **Prompt:** `How do I declare dependencies in my FastAPI route?`
- **Difficulty:** 🟢 Easy
- **Expected Outcome:** `something like async def handler(dep: Annotated[MyClass, Depends(my_dependency)]): instead of default value syntax`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| plain GPT | ❌ |   |

---


### Version 0.100.0

#### 🧪 Usage of model_config instead of class `Config` in pydantic models

- **Prompt:** `How can I add an example to use with OpenAPI for my Pydantic model?`
- **Difficulty:** 🟢 Easy
- **Expected Outcome:** `usage of a model_config dictionary instead of a class Config`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| plain GPT | ❌ |   |

---

### Version 0.101.0

#### 🧪 Usage of computed_field in pydantic models

- **Prompt:** `How can I add a computed field to my Pydantic model?`
- **Difficulty:** 🟢 Easy
- **Expected Outcome:** `usage of the computed_field decorator`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| plain GPT | ❌ |   |


- **Prompt:** `I need a Pydantic model with a field that is based on another field. It is fairly computationally heavy. How can I do that?`
- **Difficulty:** 🟡 Medium
- **Expected Outcome:** `usage of the computed_field decorator`

**Results:**

| Version | Pass | Notes |
|---|---|---|
| latest | ✅ |   |
| plain GPT | ❌ |   |


