![TestGPTs face after being asked what "quaddelpok" means 720 times](/assets/research/addressing-experiment/testgpt-logo.png)

# Adressing Experiment

The recent weeks have seen a flood of new [OpenAIs GPTs](https://openai.com/blog/introducing-gpts) comming into being. Upon inspection of what the community has created, it is evident that GPTs are still an emerging technology and no "best-practices" have developed yet. 
One aspect that has seen diverse approaches is the way of adressing GPTs in their instructions. While the GPT builder adresses the them by their title in the automatically generated instructions, it is clear that neither is this know to be "the" best way of doing it, nor is it the only way that is used. Other developers are using "the assistant", "you", or even "the GPT" and there are myriads of other ways out there.

The aim of this experiment is to figure out, how to best adress a GPT in it's instructions. 

## Navigation:

- [TL;DR](#tldr)
- [Experiment Design](#experiment-design)
    - [Tested variables](#tested-variables)
    - [Experiment procedure](#experiment-procedure)
- [Results](#results)
    - [Adressing methods](#adressing-methods)
    - [Order](#order)
    - [Diversity](#diversity-within-tests)
- [Conclusion](#conclusion)

## TL;DR
- "You" is the strongest way of adressing a GPT, followed by the name of the the GPT. 
- Instructions at the end outperform instructions in the middle by a huge margin.

## Experiment Design 

### Tested variables

**Ways of adressing**:

- "the assistant"
- "the GPT"
- "you"
- "I"
- "{GPT_title}"

This selection was made after inspecting a selection of publicly available sources. This probably does not capture all the ways of adressing a GPT, but I am confident that the most common ways are ammong them.

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


## Results

### Adressing methods:

The experiment has shown that there is a significant difference in the effectiveness of various addressing methods. 
![Relative Wins by Adressing Method](/assets/research/addressing-experiment/combined-relative.png)

"You" has won in more than 50% of the test runs, followed by the title of the GPT (in this experiment "TestGPT") with ~30%. The other three ways of adressing all scored below 10%, with "The GPT" being the worst performer at only 2.50% wins.

### Order:
The experiment made clear: Order matters. Instructions at the end end have a particularly strong influence. 
![Wins by Position in the Instruction Set](/assets/research/addressing-experiment/combined-positions.png)
The instruction that was given the last, won in 50% of the test runs. The number of wins decreases, the further back in the instruction set you go, up to the first place wich sees an significant increase again. 

![Adressing methods wins at Position](/assets/research/addressing-experiment/combined-position-wins.png)
In fact, only the two strongest adressing methods had a chance to win at position 1 or 2. Two of the five adressing methods had almost all their wins on posiion 5.

### Diversity within Tests

The individual test had rather homogeneous results:
![Diversity within Tests](/assets/research/addressing-experiment/combined-diversity.png)
In 75 of the 120 tests, only one adressing method has won and only 9 tests had 3 or more different adressing methods win. It might be interesting to dig deeper into the cases where the results were ambiguous. However, for now this is not part of the scope of this experiment.

### Side findings

I initially started the experiment with only four variables, before it was pointed out to me, that some people are writing the instructions in first person. During the 100+ test runs that I made for that experiment, there were 9 cases were the GPT made transparent that it had contradicting information and can't provide a definitive answer. However, this occured not once during the experiment with 5 variables. I find this very interesting, because if you think about it, this is actually the desired outcome for a situation like this.

![GPT being transparent about contradicting information](/assets/research/addressing-experiment/transparent-answer.png)


## Conclusion

The experiment has shown, that adressing a GPT with "you" or the title of the GPT is the strongest way and should be prefered. Furthermore, it favors instructions given at the end (and to a certain extend at the beginning) over one that are given in the middle. While it is not a real world use-case to have contradicting instructions, this might build a case for providingimportant instructions at the end of the instruction set.

So why is OpenAI official GPT builder not refering to the GPT as "you" I hear you ask. During research I stumbled across a plausible explanation: Since the generated instructions will have to be part of GPT builders context window, it would get confused if these would use "you". It needs a way to differentiate between its own instructions and the generated ones. (Unfortunately I haven't noted the source, I will add it as soon as possible)

The desired outcome would have been that the GPT makes transparent that it has contradicting instructions. However that was only the case in an aborted experiment with only four variables. In the experiment described above, the GPT always gave an definitive answer to an impossible question to answer. This might be a phenomenom to further investigate.

## Resources

- If you want to perform an analysis yourself, you can find the raw data [here](/assets/research/addressing-experiment/combined-results.csv). The data is stored in a CSV format. The information about the instruction order is encoded in the test ID. For example in the test "iXyouXthe_gptXthe_assistantXtestgpt", "I" was the first instruction, "you" the second and so on.

- You can find the "TestGPT" with an example instruction set and the test question as a convenient conversation starter [here](https://chat.openai.com/g/g-ikpbT40PS-testgpt)
