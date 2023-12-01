---
title: "Addressing Experiment"
description: "Whats the best way to address an OpenAI custom GPT in its instructions? An comprehensive experiment."
layout: post
date: 2023-11-20
---
**How to address OpenAIs custom GPTs and assistants in their instructions👋**

<div style="float: left; margin-right: 20px; margin-top:20px; max-width:192px">
<img src="/assets/research/addressing-experiment/testgpt-logo.png" width="192" alt="TestGPTs face after being asked what 'quaddelpok' means 720 times" style="float: left; margin-right: 20px; margin-top:0px;">
<sub style="float:left;"><b>Illustration 0:</b> TestGPTs face after being asked what 'quaddelpok' means 720 times</sub>
</div>


The recent weeks have seen a flood of new [OpenAIs GPTs](https://openai.com/blog/introducing-gpts) comming into being. Upon inspection of what the community has created, it is evident that GPTs are still an emerging technology and no "best-practices" have developed yet. 
One aspect that has seen diverse approaches is the way of addressing GPTs in their instructions. While the GPT builder addresses the them by their title in the automatically generated instructions, it is clear that neither is this know to be "the" best way of doing it, nor is it the only way that is used. Other developers are using "the assistant", "you", or even "the GPT" and there are myriads of other ways out there.

The aim of this experiment is to figure out, how to best address a GPT in it's instructions. 

---

## Navigation:

- [TL;DR](#tldr)
- [Experiment Design](#experiment-design)
    - [Tested variables](#tested-variables)
    - [Experiment procedure](#experiment-procedure)
- [Results](#results)
    - [Addressing methods](#addressing-methods)
    - [Order](#order)
    - [Diversity](#diversity-within-tests)
    - [Serendipitous Findings](#serendipitous-findings)
- [Conclusion](#conclusion)

---

## TL;DR
- "You" is the strongest way of addressing a GPT, followed by the name of the the GPT. 
- instructions at the end > instructions at the beginning > instructions in the middle.

---

## Experiment Design 

### Tested variables

**Ways of addressing**:

- "the assistant"
- "the GPT"
- "you"
- "I"
- "{GPT_title}"

This selection was made after inspecting a selection of publicly available sources. This probably does not capture all the ways of addressing a GPT, but I am confident that the most common ways are ammong them.

**Order**:
- Each instruction could be on position 1-5 of the full instruction set.

### Experiment procedure

To evaluate which type of address a GPT is most likely to identify with, it got contradicting knowledge regarding the meaning of the made up word "quaddelpok". "Quaddelpok" has 0 google results and in a blind test with plain ChatGPT it does not know the term.
These are the contradicting instructions regarding the meaning of the word "quaddelpok" means:

- **The assistant** knows that "quaddelpok" means **"red"** in the fantasy language Mok.
- **I** know that "quaddelpok" means **"blue"** in the fantasy language Mok.
- **You** know that "quaddelpok" means **"green"** in the fantasy language Mok.
- **TestGPT** knows that "quaddelpok" means **"black"** in the fantasy language Mok.
- **The GPT** knows that "quaddelpok" means **"yellow"** in the fantasy language Mok.


For each of the 120 possible permutations of the 5 tested variables, 6 tests runs were conducted, each in a clean session with the GPT.
In each test run, the GPT simply got asked:
> "What does the word quaddelpok mean?". 

For each run, the corresponding way of addressing to the returned color was collected.

---

## Results

### Addressing methods:

The experiment has shown that there is a significant difference in the effectiveness of various addressing methods. 
![Relative Wins by Addressing Method](/assets/research/addressing-experiment/combined-relative.png)

"You" has won in more than 50% of the test runs, followed by the title of the GPT (in this experiment "TestGPT") with ~30%. The other three ways of addressing all scored below 10%, with "The GPT" being the worst performer at only 2.50% wins.

### Order:
The experiment made clear: Order matters. Instructions at the end end have a particularly strong influence. 
![Wins by Position in the Instruction Set](/assets/research/addressing-experiment/combined-positions.png)
The instruction that was given the last, won in 50% of the test runs. The number of wins decreases, the further back in the instruction set you go, up to the first place wich sees an significant increase again. 

![Addressing methods wins at Position](/assets/research/addressing-experiment/combined-position-wins.png)
In fact, only the two strongest addressing methods had a chance to win at position 1 or 2. Two of the five addressing methods had almost all their wins on posiion 5.

### Diversity within Tests

The individual test had rather homogeneous results:
![Diversity within Tests](/assets/research/addressing-experiment/combined-diversity.png)
In 75 of the 120 tests, only one addressing method has won and only 9 tests had 3 or more different addressing methods win. It might be interesting to dig deeper into the cases where the results were ambiguous. However, for now this is not part of the scope of this experiment.

### ➡️ Serendipitous Findings

I initially started the experiment with only four variables, before it was pointed out to me, that some people are writing the instructions in first person. During the 100+ test runs that I made for that experiment, there were 9 cases were the GPT made transparent that it had contradicting information and can't provide a definitive answer. However, this occured not once during the experiment with 5 variables. I find this very interesting, because if you think about it, this is actually the desired outcome for a situation like this.

![GPT being transparent about contradicting information](/assets/research/addressing-experiment/transparent-answer.png)

---

## Conclusion

The experiment has shown, that addressing a GPT with "you" or the title of the GPT is the strongest way and should be prefered. Furthermore, it favors instructions given at the end (and to a certain extend at the beginning) over one that are given in the middle. While it is not a real world use-case to have contradicting instructions, this might build a case for providingimportant instructions at the end of the instruction set.

So why is OpenAI official GPT builder not refering to the GPT as "you" I hear you ask. During research I stumbled across a plausible explanation (by @RonaldGRuckus)[https://community.openai.com/t/custom-gpt-instructions-using-2nd-vs-3rd-person/497663/7?u=luona.dev]: Since the generated instructions have to be part of GPT builders context, it would get confused if these would be written in 2nd person aka "you". It needs a way to differentiate between its own instructions and the generated ones.

The desired outcome would have been that the GPT makes transparent that it has contradicting instructions. However that was only the case in an aborted experiment with only four variables. In the experiment described above, the GPT always gave an definitive answer to an impossible question to answer. This might be a phenomenom to further investigate.

---

## Epilogue

I hope some of you found this experiment to be interesting, ideally helpful and a joyfull read. I would like to do more stuff like this in the future. If you can and want to support me, you can buy me some time for this on [buymeacoffee](https://www.buymeacoffee.com/kon.foo)

If you have any feedback, please contact me on [Twitter](https://twitter.com/LuonaDev) or [Discord](https://discordapp.com/users/luona.dev).


## Resources

- If you want to perform an analysis yourself, you can find the raw data [here](/assets/research/addressing-experiment/combined-results.csv). The data is stored in a CSV format. The information about the instruction order is encoded in the test ID. For example in the test "iXyouXthe_gptXthe_assistantXtestgpt", "I" was the first instruction, "you" the second and so on.

- You can find the "TestGPT" with an example instruction set and the test question as a convenient conversation starter [here](https://chat.openai.com/g/g-ikpbT40PS-testgpt)
