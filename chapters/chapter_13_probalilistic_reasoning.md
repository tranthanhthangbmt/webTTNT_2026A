# Chapter 13 Probalilistic Reasoning

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_13_Probalilistic%20Reasoning/chapter_13_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_13_Probalilistic%20Reasoning.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**
*(Chưa có slide)*

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [ENUMERATION-ASK](codeAndExercises/aima-pseudocode-master/md/Enumeration-Ask.md)
- [ELIMINATION-ASK](codeAndExercises/aima-pseudocode-master/md/Elimination-Ask.md)
- [PRIOR-SAMPLE](codeAndExercises/aima-pseudocode-master/md/Prior-Sample.md)
- [REJECTION-SAMPLING](codeAndExercises/aima-pseudocode-master/md/Rejection-Sampling.md)
- [LIKELIHOOD-WEIGHTING](codeAndExercises/aima-pseudocode-master/md/Likelihood-Weighting.md)
- [GIBBS-ASK](codeAndExercises/aima-pseudocode-master/md/Gibbs-Ask.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Probability](codeAndExercises/aima-python-master/notebooks/probability.ipynb)
- [Probability (Python File)](codeAndExercises/aima-python-master/notebooks/probability.py)


#### **Bài tập**

##### Bài tập 13.1

Show from first principles that $P(a{{\,|\,}}b\land a) = 1$.


---

##### Bài tập 13.2

Using the axioms of probability, prove that any
probability distribution on a discrete random variable must sum to 1.


---

##### Bài tập 13.3

For each of the following statements, either prove it is true or give a
counterexample.<br>

1.  If $P(a {{\,|\,}}b, c) = P(b {{\,|\,}}a, c)$, then
    $P(a {{\,|\,}}c) = P(b {{\,|\,}}c)$ <br>

2.  If $P(a {{\,|\,}}b, c) = P(a)$, then $P(b {{\,|\,}}c) = P(b)$ <br>

3.  If $P(a {{\,|\,}}b) = P(a)$, then
    $P(a {{\,|\,}}b, c) = P(a {{\,|\,}}c)$<br>


---

##### Bài tập 13.4

Would it be rational for an agent to hold the three beliefs
$P(A) = 0.4$, $P(B) = 0.3$, and
$P(A \lor B) = 0.5$? If so, what range of probabilities would
be rational for the agent to hold for $A \land B$? Make up a table like
the one in Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/de-finetti-table.png">de-finetti-table</a>, and show how it
supports your argument about rationality. Then draw another version of
the table where $P(A \lor B) = 0.7$. Explain why it is rational to have this probability,
even though the table shows one case that is a loss and three that just
break even. (<i>Hint:</i> what is Agent 1 committed to about the
probability of each of the four cases, especially the case that is a
loss?)


---

##### Bài tập 13.5

This question deals with the properties
of possible worlds, defined on page <a class="pageRef" title="" href="#">possible-worlds-page</a> as assignments to all
random variables. We will work with propositions that correspond to
exactly one possible world because they pin down the assignments of all
the variables. In probability theory, such propositions are called <b>atomic event</b>. For
example, with Boolean variables $X_1$, $X_2$, $X_3$, the proposition
$x_1\land \lnot x_2 \land \lnot x_3$ fixes the assignment of the
variables; in the language of propositional logic, we would say it has
exactly one model.<br>


1.  Prove, for the case of $n$ Boolean variables, that any two distinct
    atomic events are mutually exclusive; that is, their conjunction is
    equivalent to ${false}$.<br>

2.  Prove that the disjunction of all possible atomic events is
    logically equivalent to ${true}$.<br>

3.  Prove that any proposition is logically equivalent to the
    disjunction of the atomic events that entail its truth.<br>


---

##### Bài tập 13.6

Prove
Equation (<a class="equationRef" title="" href="#">kolmogorov-disjunction-equation</a>) from
Equations <a class="equationRef" title="" href="#">basic-probability-axiom-equation</a>
and (<a class="equationRef" title="" href="#">proposition-probability-equation</a>.


---

##### Bài tập 13.7

Consider the set of all possible five-card poker hands dealt fairly from
a standard deck of fifty-two cards.<br>

1.  How many atomic events are there in the joint probability
    distribution (i.e., how many five-card hands are there)?<br>

2.  What is the probability of each atomic event?<br>

3.  What is the probability of being dealt a royal straight flush? Four
    of a kind?


---

##### Bài tập 13.8

Given the full joint distribution shown in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/dentist-joint-table.png">dentist-joint-table</a>, calculate the following:<br>

1.  $\textbf{P}({toothache})$.<br>

2.  $\textbf{P}({Cavity})$.<br>

3.  $\textbf{P}({Toothache}{{\,|\,}}{cavity})$.<br>

4.  $\textbf{P}({Cavity}{{\,|\,}}{toothache}\lor {catch})$.


---

##### Bài tập 13.9

Given the full joint distribution shown in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/dentist-joint-table.png">dentist-joint-table</a>, calculate the following:<br>

1.  $\textbf{P}({toothache})$.<br>

2.  $\textbf{P}({Catch})$.<br>

3.  $\textbf{P}({Cavity}{{\,|\,}}{catch})$.<br>

4.  $\textbf{P}({Cavity}{{\,|\,}}{toothache}\lor {catch})$.<br>


---

##### Bài tập 13.10

In his letter of August 24, 1654, Pascal
was trying to show how a pot of money should be allocated when a
gambling game must end prematurely. Imagine a game where each turn
consists of the roll of a die, player <i>E</i> gets a point when
the die is even, and player  <i>O</i> gets a point when the die
is odd. The first player to get 7 points wins the pot. Suppose the game
is interrupted with <i>E</i> leading 4–2. How should the money
be fairly split in this case? What is the general formula? (Fermat and
Pascal made several errors before solving the problem, but you should be
able to get it right the first time.)


---

##### Bài tập 13.11

Deciding to put probability theory to good use, we encounter a slot
machine with three independent wheels, each producing one of the four
symbols bar, bell, lemon, or
cherry with equal probability. The slot machine has the
following payout scheme for a bet of 1 coin (where “?” denotes that we
don’t care what comes up for that wheel): <br>

> bar/bar/bar pays 20 coins<br>

> bell/bell/bell pays 15 coins<br>

> lemon/lemon/lemon pays 5 coins<br>

> cherry/cherry/cherry pays 3 coins<br>

> cherry/cherry/? pays 2 coins<br>

> cherry/?/? pays 1 coin<br>

1.  Compute the expected “payback” percentage of the machine. In other
    words, for each coin played, what is the expected coin return?<br>

2.  Compute the probability that playing the slot machine once will
    result in a win.<br>

3.  Estimate the mean and median number of plays you can expect to make
    until you go broke, if you start with 10 coins. You can run a
    simulation to estimate this, rather than trying to compute an
    exact answer.<br>


---

##### Bài tập 13.12

Deciding to put probability theory to good use, we encounter a slot
machine with three independent wheels, each producing one of the four
symbols bar, bell, lemon, or
cherry with equal probability. The slot machine has the
following payout scheme for a bet of 1 coin (where “?” denotes that we
don’t care what comes up for that wheel): <br>

> bar/bar/bar pays 20 coins<br>

> bell/bell/bell pays 15 coins<br>

> lemon/lemon/lemon pays 5 coins<br>

> cherry/cherry/cherry pays 3 coins<br>

> cherry/cherry/? pays 2 coins<br>

> cherry/?/? pays 1 coin<br>

1.  Compute the expected “payback” percentage of the machine. In other
    words, for each coin played, what is the expected coin return?<br>

2.  Compute the probability that playing the slot machine once will
    result in a win.<br>

3.  Estimate the mean and median number of plays you can expect to make
    until you go broke, if you start with 10 coins. You can run a
    simulation to estimate this, rather than trying to compute an
    exact answer.<br>


---

##### Bài tập 13.13

We wish to transmit an $n$-bit message to a receiving agent. The bits in
the message are independently corrupted (flipped) during transmission
with $\epsilon$ probability each. With an extra parity bit sent along
with the original information, a message can be corrected by the
receiver if at most one bit in the entire message (including the parity
bit) has been corrupted. Suppose we want to ensure that the correct
message is received with probability at least $1-\delta$. What is the
maximum feasible value of $n$? Calculate this value for the case
$\epsilon = 0.001$, $\delta = 0.01$.


---

##### Bài tập 13.14

We wish to transmit an $n$-bit message to a receiving agent. The bits in
the message are independently corrupted (flipped) during transmission
with $\epsilon$ probability each. With an extra parity bit sent along
with the original information, a message can be corrected by the
receiver if at most one bit in the entire message (including the parity
bit) has been corrupted. Suppose we want to ensure that the correct
message is received with probability at least $1-\delta$. What is the
maximum feasible value of $n$? Calculate this value for the case
$\epsilon{{\,=\,}}0.002$, $\delta{{\,=\,}}0.01$.


---

##### Bài tập 13.15

Show that the three forms of independence in
Equation (<a class="equationRef" title="" href="#">independence-equation</a>) are equivalent.


---

##### Bài tập 13.16

Consider two medical tests, A and B, for a virus. Test A is 95%
effective at recognizing the virus when it is present, but has a 10%
false positive rate (indicating that the virus is present, when it is
not). Test B is 90% effective at recognizing the virus, but has a 5%
false positive rate. The two tests use independent methods of
identifying the virus. The virus is carried by 1% of all people. Say
that a person is tested for the virus using only one of the tests, and
that test comes back positive for carrying the virus. Which test
returning positive is more indicative of someone really carrying the
virus? Justify your answer mathematically.


---

##### Bài tập 13.17

Suppose you are given a coin that lands ${heads}$ with probability $x$
and ${tails}$ with probability $1 - x$. Are the outcomes of successive
flips of the coin independent of each other given that you know the
value of $x$? Are the outcomes of successive flips of the coin
independent of each other if you do <i>not</i> know the value of
$x$? Justify your answer.


---

##### Bài tập 13.18

After your yearly checkup, the doctor has bad news and good news. The
bad news is that you tested positive for a serious disease and that the
test is 99% accurate (i.e., the probability of testing positive when you
do have the disease is 0.99, as is the probability of testing negative
when you don’t have the disease). The good news is that this is a rare
disease, striking only 1 in 10,000 people of your age. Why is it good
news that the disease is rare? What are the chances that you actually
have the disease?


---

##### Bài tập 13.19

After your yearly checkup, the doctor has bad news and good news. The
bad news is that you tested positive for a serious disease and that the
test is 99% accurate (i.e., the probability of testing positive when you
do have the disease is 0.99, as is the probability of testing negative
when you don’t have the disease). The good news is that this is a rare
disease, striking only 1 in 100,000 people of your age. Why is it good
news that the disease is rare? What are the chances that you actually
have the disease?


---

##### Bài tập 13.20

It is quite often useful to consider the
effect of some specific propositions in the context of some general
background evidence that remains fixed, rather than in the complete
absence of information. The following questions ask you to prove more
general versions of the product rule and Bayes’ rule, with respect to
some background evidence $\textbf{e}$: <br>

1.  Prove the conditionalized version of the general product rule:
    $${\textbf{P}}(X,Y {{\,|\,}}\textbf{e}) = {\textbf{P}}(X{{\,|\,}}Y,\textbf{e}) {\textbf{P}}(Y{{\,|\,}}\textbf{e})\ .$$ <br>

2.  Prove the conditionalized version of Bayes’ rule in
    Equation (<a class="equationRef" title="" href="#">conditional-bayes-equation</a>). <br>


---

##### Bài tập 13.21

Show that the statement of conditional independence
$${\textbf{P}}(X,Y  | Z) = {\textbf{P}}(X | Z) {\textbf{P}}(Y | Z)$$
is equivalent to each of the statements
$${\textbf{P}}(X | Y,Z) = {\textbf{P}}(X | Z) \quad\mbox{and}\quad {\textbf{P}}(Y | X,Z) = {\textbf{P}}(Y | Z)\ .$$


---

##### Bài tập 13.22

Suppose you are given a bag containing $n$ unbiased coins. You are told
that $n-1$ of these coins are normal, with heads on one side and tails
on the other, whereas one coin is a fake, with heads on both sides. <br>

1.  Suppose you reach into the bag, pick out a coin at random, flip it,
    and get a head. What is the (conditional) probability that the coin
    you chose is the fake coin? <br>

2.  Suppose you continue flipping the coin for a total of $k$ times
    after picking it and see $k$ heads. Now what is the conditional
    probability that you picked the fake coin? <br>

3.  Suppose you wanted to decide whether the chosen coin was fake by
    flipping it $k$ times. The decision procedure returns ${fake}$ if
    all $k$ flips come up heads; otherwise it returns ${normal}$. What
    is the (unconditional) probability that this procedure makes an
    error?


---

##### Bài tập 13.23

In this exercise, you will complete the
normalization calculation for the meningitis example. First, make up a
suitable value for $P(s{{\,|\,}}\lnot m)$, and use it to calculate
unnormalized values for $P(m{{\,|\,}}s)$ and $P(\lnot m {{\,|\,}}s)$
(i.e., ignoring the $P(s)$ term in the Bayes’ rule expression,
Equation (<a class="equationRef" title="" href="#">meningitis-bayes-equation</a>). Now normalize
these values so that they add to 1.


---

##### Bài tập 13.24

This exercise investigates the way in which conditional independence
relationships affect the amount of information needed for probabilistic
calculations.<br>

1.  Suppose we wish to calculate $P(h{{\,|\,}}e_1,e_2)$ and we have no
    conditional independence information. Which of the following sets of
    numbers are sufficient for the calculation?<br>

    1.  ${\textbf{P}}(E_1,E_2)$, ${\textbf{P}}(H)$,
        ${\textbf{P}}(E_1{{\,|\,}}H)$,
        ${\textbf{P}}(E_2{{\,|\,}}H)$

    2.  ${\textbf{P}}(E_1,E_2)$, ${\textbf{P}}(H)$,
        ${\textbf{P}}(E_1,E_2{{\,|\,}}H)$<br>

    3.  ${\textbf{P}}(H)$,
        ${\textbf{P}}(E_1{{\,|\,}}H)$,
        ${\textbf{P}}(E_2{{\,|\,}}H)$<br>

2.  Suppose we know that
    ${\textbf{P}}(E_1{{\,|\,}}H,E_2)={\textbf{P}}(E_1{{\,|\,}}H)$
    for all values of $H$, $E_1$, $E_2$. Now which of the three sets are
    sufficient?


---

##### Bài tập 13.25

Let $X$, $Y$, $Z$ be Boolean random variables. Label the eight entries
in the joint distribution ${\textbf{P}}(X,Y,Z)$ as $a$ through
$h$. Express the statement that $X$ and $Y$ are conditionally
independent given $Z$, as a set of equations relating $a$ through $h$.
How many <i>nonredundant</i>equations are there?


---

##### Bài tập 13.26

(Adapted from Pearl [<a class="paperRef" title="" href="">Pearl:1988</a>].) Suppose you are a witness to a
nighttime hit-and-run accident involving a taxi in Athens. All taxis in
Athens are blue or green. You swear, under oath, that the taxi was blue.
Extensive testing shows that, under the dim lighting conditions,
discrimination between blue and green is 75% reliable. <br>

1.  Is it possible to calculate the most likely color for the taxi?
    (*Hint:* distinguish carefully between the proposition
    that the taxi *is* blue and the proposition that it
    *appears* blue.) <br>

2.  What if you know that 9 out of 10 Athenian taxis are green?<br>


---

##### Bài tập 13.27

Write out a general algorithm for answering queries of the form
${\textbf{P}}({Cause}{{\,|\,}}\textbf{e})$, using a naive Bayes
distribution. Assume that the evidence $\textbf{e}$ may assign values to
<i>any subset</i> of the effect variables.


---

##### Bài tập 13.28

Text categorization is the task of
assigning a given document to one of a fixed set of categories on the
basis of the text it contains. Naive Bayes models are often used for
this task. In these models, the query variable is the document category,
and the “effect” variables are the presence or absence of each word in
the language; the assumption is that words occur independently in
documents, with frequencies determined by the document category.<br>

1.  Explain precisely how such a model can be constructed, given as
    “training data” a set of documents that have been assigned
    to categories.<br>

2.  Explain precisely how to categorize a new document.<br>

3.  Is the conditional independence assumption reasonable? Discuss.<br>


---

##### Bài tập 13.29

In our analysis of the wumpus world, we used the fact that
each square contains a pit with probability 0.2, independently of the
contents of the other squares. Suppose instead that exactly $N/5$ pits
are scattered at random among the $N$ squares other than [1,1]. Are
the variables $P_{i,j}$ and $P_{k,l}$ still independent? What is the
joint distribution ${\textbf{P}}(P_{1,1},\ldots,P_{4,4})$ now?
Redo the calculation for the probabilities of pits in [1,3] and
[2,2].


---

##### Bài tập 13.30

Redo the probability calculation for pits in [1,3] and [2,2],
assuming that each square contains a pit with probability 0.01,
independent of the other squares. What can you say about the relative
performance of a logical versus a probabilistic agent in this case?


---

##### Bài tập 13.31

Implement a hybrid probabilistic agent for the wumpus world, based on
the hybrid agent in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/hybrid-wumpus-agent-algorithm.png">hybrid-wumpus-agent-algorithm</a> and the
probabilistic inference procedure outlined in this chapter.


---


<!-- tabs:end -->
