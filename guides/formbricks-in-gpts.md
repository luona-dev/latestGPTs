---
title: Enhancing GPTs with Formbricks
description: Learn how to add polls, star ratings and more to your custom GPTs for free.
layout: post
date: 2022-12-01
---

**📝 How to add Polls, Feedback Forms and more to your custom GPTs**

At [luona.dev], we aimed to add user feedback to our GPTs from the beginning. As a first workaround, we simply prompted our GPTs to refer to a Github Issues page, whenever a user criticizes the output. While this works, it might be quite a barrier, expecially for non-technical users. Therefore, I decided to look for a better solution and while at it, I thought "Why not integrate polls and star ratings as well?". I think the results turned out great and am convinced that other GPT creators can benefit from this as well. Therefore, I decided to share my solution with you.

## 🧭 Navigation

- [📐 What we will build: An interactive example](#-what-we-will-build-an-interactive-example)
- [❓ Why Formbricks?](#-why-formbricks)
- [⚙️ Preparation](#️-preparation)
- [📋 Creating a Survey](#-creating-a-survey)
- [🔑 Obtaining the necessary meta data](#-obtaining-the-necessary-meta-data)
- [📄 Creating an Actions OpenAPI spec](#-creating-an-actions-openapi-spec)
    - [🔍 Details about the created OpenAPI schema](#-details-about-the-created-openapi-schema)
- [🪄 Adding Actions to the GPT](#-adding-actions-to-the-gpt)
- [✏️ Adding Instructions](#️-adding-instructions)
- [🎉 The juicy part: Go try it out!](#-the-juicy-part-go-try-it-out)




## 📐 What we will build: An interactive example

At the end of this article, we will have a GPT that can follow three commands:
- `/feedback <user feedback>` 
- `/vote <option 1> <option 2> ...`
- `/rate <number of stars>`

What's more is that our GPT will perform validation on the inputs, for example check that the rating is between 1 and 5 and that the vote options are among the valid options. If not, it will ask for clarification. 

[Over here](https://chat.openai.com/g/g-OBulCRHm5-luona-dev-guide-polls-and-ratings-for-your-gpts) you can find a GPT that is both, an interactive example of what we will build and an interactive assistant to this guide. I think interactive guides are an extremely interesting use case for custom GPTs and this is my first go at it. Go ahead an try it out, the feedback form is right included ;)

## ❓ Why Formbricks?

I am **in no way affiliated** with Formbricks and I am not getting paid a dime. I was simply looking for an easy way to accomplish what I was aiming for and after working with it for a while, I am convinced that I found a solid solution. The criteria I searched for were:

- ✅ Open Source
- ✅ Option to self-host
- ✅ Free and easy to get started
- ✅ An API to integrate it into my GPTs

Formbricks **ticks all of these boxes**. It is open source, you can easily self-host it, but also just get started with the cloud version which is free for up to 250 submissions per month. And most importantly: It has an API that allows us to integrate it into our GPTs. 
There are probably **other solutions out there**, but I stopped searching after I realized that Formbricks is a great fit for my needs.

## ⚙️ Preparation

To follow along, you will need a **ChatGPT Plus subscription** to be able to create custom GPTs. I mean if you're here, you probably have one, but still. I would recommend to create a **new Test GPT** to try and then just copy the parts that you need into your production GPTs.  
Furthermore, you will need a free **Formbricks account**. You can create one [here](https://app.formbricks.com/auth/signup). After registration you will be asked a few questions that you might skip. You are also asked to create a first *Product*. From what I understand, this is a concept to seperate concerns on a more higher up level than individual surveys. I recommend to use a *Product* for each of your GPTs. For now, simply add a *Test Product*.

## 📋 Creating a Survey

In production, you will probably want to create a seperate survey for different aspects such as user feedback, ratings and polls. But for the sake of simplicity, we will create **a single survey** with three different types of questions. On your *Surveys Dashboard* click on *Start from scratch*. The survey creation tool will open. On the right side, you can always see a preview of your survey. On the left side, you can add questions, logic and other elements.

![Formbricks Survey Creation Tool](/assets/guides/formbricks-in-gpts/formbricks-survey-creation-tool.png)

On the top, where it says *New Survey*, you may change the name of your survey.
The first, default question will be our **feedback formular**. You may change the *Question*, *Description* and *Placeholder* to your liking. The only important thing is that you keep the *Input Type* as text and that you **uncheck** the *Required* checkbox. This is important because we don't want to force users who give feedback to also answer the poll and rate the GPT.  
When you're happy, click on *Add Questions* and select *Multi-Select*. This will be our **poll**. Again, customize it to your needs, uncheck *Required* and add some options. For this tutorial, I did not add an *Other* option. If you decide to do so, you will have to slightly tweak the GPT's validation instructions that we will later create.     
Finally, we will add a **star rating**. Click on *Add Questions*, select *Rating*, uncheck *Required* and, you guessed it, customize it to your liking.  
Since we're using the API to submit answers and a GPT as the user interface, you do not have to worry about *Thank You Cards* or custom logic. As soon as you're happy with your survey, click on *Continue to Settings*. Great news: You don't have to worry about any settings🎊. Read everything to satisfy your curiosity, then just click *Publish*.

## 🔑 Obtaining the necessary meta data

Next we will have to obtain all the necessary meta data to make our API calls. That is:
- the `environmentId`
- the `surveyId`
- all `questionIds`
- all question details such as `type` and `options`

Formbricks differentiates between the *Public Client API* to create responses and the *Management API* to add/update survey etc. While our GPTs will use the *Public Client API*, I found that using the *Management API* is the easiest way to obtain all the necessary IDs. 

➡️ Here is the one drawback I found so far with Formbricks: The *Public Client API* is, well, public ⚠️ There is no way to add authentication, so a malicious user might retrieve all the necessary IDs from your GPTs and spam your survey. For now, I would call that an acceptable risk. But with more popular GPTs it might be worth it to add some kind of authentication proxy between your GPT and Formbricks.

To get a *Management API Key*, you click on *Settings* in the header menu, then on *API Keys* in the sidebar under the *Product* section. Add a new API Key and store it in the password manager of your choice. You will need for the next step.

To make our lifes easier, I created a Python script that will come in handy. You can find it [here](/assets/guides/formbricks-in-gpts/formbricks_to_gpt.py). It handles three purposes:

1. Retrieve all our survey meta data
2. Convert it into a OpenAPI spec that our GPTs can understand
3. Create example instructions for your GPTs

If you don't want to use this script and/or no *Management API*, you will have to do quite some copy and pasting. But here is how you can obtain the necessary IDs manually:
<details>
    <summary style="cursor:pointer">Click to expand</summary>
    <br>
    The <code class="language-plaintext highlighter-rouge">environmentId</code> as well as the <code class="language-plaintext highlighter-rouge">surveyId</code> can best be scraped right from the URL of your Formbricks Dashboard. After publishing your should already be on the page with your surveys details. If you've navigated away already, click on *Surveys* in the header menu, then on the survey you just created. The URL is structured like this: <br>
    <br>
    <blockquote>
    <p>
    `https://app.formbricks.com/environments/<strong>[environment-id]</strong>/surveys/<strong>[survery-id]</strong>/summary
    </p>
    </blockquote>
    <br>
    To get the `questionIds` you will have to go back into editing mode for your survey. For each question, click on *Show Advanced Settings* and you will find the questionId in the greyed-out boy at the bottom.<br><br>
</details>
<br>

To get everything you need with the script, simply run:

> `python formbricks_to_gpt.py get [API_KEY] [HOST (default: app.formbricks.com)]`

This will save a `surveys.json` file at your current location. Inspect it if you like, but its main purpose is to serve as the input for the next step. You may well delete the Management API Key again. You won't need it anymore. If you decide to keep it, it is a good practice to delete the last command from your shell history. The following *should* do the trick on all operating systems, but I only used it on Ubuntu:

> `history -d $(history | tail -n 2 | awk '{print $1}')`

Now, after we have obtained all the necessary meta data, we are ready to switch to the GPT part!

## 📄 Creating an Actions OpenAPI spec
If you are here, reading this article, you probably already know how to create a custom GPT, so we skip to the point where we define our actions.
Actions are defined using the OpenAPI sepcification with some Open*AI* specific fields. From the [Formbricks API Docs](https://formbricks.com/docs/api/client/responses) we know that a *Response Request Body* should look like this:
    
```json
{
  "userId": "1",
  "surveyId": "cloqzeuu70000z8khcirufo60",
  "finished": true,
  "data": {
      "clfqjny0v0003yzgscnog1j9i": 10,
      "clfqjtn8n0070yzgs6jgx9rog": "I love Formbricks"
    }
}
```
Two facts make it a bit tricky to cast this into a schema that OpenAI accepts:
1. The `data` object uses the dyamic `questionId` as keys. 
2. The values for the `questionId` keys are of different types.  
Normally, we could simply define a schema like this:

```json
...
"data": {
    "type": "object",
    "additionalProperties": {
        "oneOf": [
            {
              "type": "string"
            },
            {
              "type": "array"
            },
            ...
          ]
        }
      }
...
```

But OpenAI requries us to be very specific about what exactly goes into each Action and using `additionalProperties` won't work. Therefore we have to hardcode each `questionId` along with its type into the schema. This is were the second command of the script comes into play. It will transform the `surveys.json` file into an OpenAPI spec that we can use in our GPTs. So far this only works for the three questions types that we used in this tutorial: `openText`, `multiSelectMulti` and `rating`. If you want to use other question types, you will have to add them to the script. But I think it should be pretty straight forward.

To generate the OpenAPI spec, simply run:
> `python get_survey_meta.py oapi [PATH (default surveys.json)] [HOST (default: app.formbricks.com)]`

This will create a `surveys_oapi.json` file that should comply with OpenAIs requirements for custom GPT actions. If you did not use the script to generate the `surveys.json` file, you can have a look at the [`example_surveys_oapi.json`](/assets/guides/formbricks-in-gpts/example_surveys_oapi.json) and copy and paste your IDs into it. Read the following section in case you run into any problems.

### 🔍 Details about the created OpenAPI schema
If you are only interested in the result, you can simply skip to [the next section](#️-adding-instructions). But if you want to understand what is going on, here are some details about the created OpenAPI schema.

#### The `paths`object
The Formbricks *Response API* endpoint runs on a per *environment* basis. Therefore, even if you have multiple surveys, you will only have a single path per environment/*Product* like this:

```json
```json
"paths": {
        "/client/{environmentId}/responses": {
            ...
        }
    }
```

#### The `operationId` and `x-openai-isConsequential` fields
OpenAI requires us to define an `operationId` for each operation on a path. To easily automate this, the script simply uses the `environmentId` to populate this field, but you can change it to a more meaningful name if you like (just make sur to also change the instructions).  
Another special OpenAI field is `x-openai-isConsequential`. It is a flag that decides how (often) the user is asked for consent before an API call is made. From the docs:

>If the x-openai-isConsequential field is true, we treat the operation as "must always prompt the user for confirmation before running" and don't show an "always allow" button (both are new features of GPTs designed to give users more control).
If the x-openai-isConsequential field is false, we show the "always allow button".
If the field isn't present, we default all GET operations to false and all other operations to true. [source](https://platform.openai.com/docs/actions/consequential-flag)

Since a user will only ever purposefully call a command and the call will not have any *consequences* for the user, it should be set to `false` here.

#### Undocumented `ttc` field
Actually, I am not quiete sure about this one... The Formbricks API docs do not mention a `ttc` field at all and I could only find one [Github issue](https://github.com/formbricks/formbricks/issues/1104) that mentions it. From this issue I learned that it stands for *Time to Complete* and that it is used to calculate the estimated time to complete a survey. The weird part is:  
The first time I implemented a poll for a GPT using formbricks, I only had one question in the survey and it worked just fined without the `ttc` field. But when I created the survey for this guide, I run into the error `"Fields are missing or incorrectly formatted ... "ttc": "Required"`. Since `ttc` takes a time per `questionId`, it's schema also had to be hardcoded into the OpenAPI spec. Quite a lot of boilerplate for a feature that doesn't make any sense in the context of GPTs. But there you have it. If you only have one question in your survey, feel free to remove it from the schema and from the instructions.

## 🪄 Adding Actions to the GPT

With your OpenAPI spec at hands, hop over to your GPT builder, scroll down to *Actions* section and click on *Create new action*. Then paste the contents of the `survey_oapi.json` file into the *Schema* text field. You can tell if everything worked, if you see no red error messages below the text field and instead see an *Action* pop up in the *Available actions* sections.  
You might be tempted to hit *Test* and you can certainly go for it, but it will not pass. Your GPT will call the endpoint without any parameters as long as you don't add any instructions.  
Before we do that, there is one more important step to take: If you want your GPT to be publicly available (and I'd guess thats the case if you add feedback and ratings to it), you are required to add a *Privacy Policy*. I am not a lawyer, but from my perspective users won't submit any personal data and all we do would be legitimate interest, so it should be fine to just add the Formbricks Privacy Policy `https://formbricks.com/privacy-policy`.

## ✏️ Adding Instructions

Finally, it is time to tell our GPT how to use these delicious new features. Of course there are many ways to do it, but we will go with the good old *slash commands*. I think they are very intuitive in a chat context and GPTs seem to understand them quite well. The instructions are structured like this:
> /command with parameters - validation instructions - instructions to call the actions - payload for the call

So for example:
> /rate [rating] - Check if the [rating] is a number between 1 and 5. If so, call the app.formbricks.com API with the clpm....zmqf operation and the following payload: ...

With the script™ you can generate instructions for your survey like this:
> `python formbricks_to_gpt.py instructions [PATH (default surveys.json)]`

This will create an `surveys_instructions.md` file at your current location. The instructions include validation, to check if the rating is within the range that you specified in Formbricks, to check if the users choice is among the valid options, and it will check if the feedback is an english sentence and not nonsense. These validation steps are not meant to be a security measure, but rather to improve the user experience. People will be able to circumvent them if they want to.  
Over [here](/assets/guides/formbricks-in-gpts/example_instructions.md) you can find a set of example instructions for a `/vote`, `/feedback` and `/rate` command. 

### 📦 Additional Instructions

Depending on your use case, you might want to add some additional instructions. For instance, you might not want to put the burden on your user to figure out that there is a feedback command, but rather instruct your GPT to offer that possibility if a user criticizes the output, or always after providing an answer or any other rule. Furthermore, you migh want to add a `/help` command that lists all available commands and their parameters. The possibilities are endless and I am sure you will come up with some great ideas.

## 🎉 The juicy part: Go try it out!

If you followed along, you should now be able to use the defined commands and see the answer dropping in your Formbricks Dashboard. If you haven't followed along and just want to try it out, you can find an example GPT [here](https://chat.openai.com/g/g-OBulCRHm5-luona-dev-guide-polls-and-ratings-for-your-gpts). If you run into any problems, feel free to reach out to me on [Twitter](https://twitter.com/luonaDev) or [Discord](https://discordapp.com/users/luona.dev). I am always happy to help, though I can't promise to be fast about it.

If you want to stay up to date with our research, guides and [latest] GPTs, I would be happy to welcome you to our [**newsletter**](https://newsletter.luona.dev/subscription/form). No hype, no spam, just a ping every now and then when we have something to share.

And if you want to truly make my day, you can buy me some time which allows me to create more content like this at [buymeacoffee.com](https://www.buymeacoffee.com/kon.foo). I would be very grateful for your support.



