---
title: "Conversation Starters"
description: "All conversation starters of ChatGPT"
layout: post
date: 2023-12-18
---
I collected all conversation starters that OpenAI suggest when you start a conversation with ChatGPT. At the time of writing, there are 58 of them. From creative ones:
> Make up a story about Sharky, a tooth-brushing shark superhero.
to more practical ones:
> Give me ideas for what to do with my kids' art.

The most interesting finding was that OpenAI uses the following scheme for the conversation starters:
```json
{
    "title": "Help me pick",
    "description": "an outfit that will look good on camera",
    "prompt": "I have a photoshoot tomorrow. Can you recommend me some colors and outfit options that will look good on camera?"
}
```
This differentiation between title/description and the prompt that is actually used to start the conversation is something I hoped to get for custom GPTs. This makes it possible to hide complex instructions from the user, while still giving them a good idea of what the conversation starter is about. An example:

**Visible:**
> Suggest some names for my cafe-by-day, bar-by-night business
**Actual prompt:**
> Come up with 5 sophisticated names for my coffee shop that becomes a bar at night – like "The Page Turner". Include a short sentence explaining what it means!


You can find the complete list (date: 2023-12-18) [here](/assets/research/conversation-starters.json).

If you want to be informed about little tidbits like this, or want to be updated about our research and projects you can follow me on [Twitter](https://twitter.com/LuonDev) or [subscribe to the newsletter](https://newsletter.luona.dev/subscription/form) - No hype, no spam, just a ping when I publish something new.