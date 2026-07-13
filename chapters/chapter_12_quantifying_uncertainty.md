# Chapter 12 Quantifying uncertainty

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_12_Quantifying%20uncertainty/chapter_12_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_12_Quantifying%20uncertainty.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**
*(Chưa có slide)*

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [DT-AGENT](codeAndExercises/aima-pseudocode-master/md/DT-Agent.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Probability](codeAndExercises/aima-python-master/notebooks/probability.ipynb)
- [Probability (Python File)](codeAndExercises/aima-python-master/notebooks/probability.py)


#### **Bài tập**

##### Bài tập 12.1

Define an ontology in first-order logic for tic-tac-toe. The ontology
should contain situations, actions, squares, players, marks (X, O, or
blank), and the notion of winning, losing, or drawing a game. Also
define the notion of a forced win (or draw): a position from which a
player can force a win (or draw) with the right sequence of actions.
Write axioms for the domain. (Note: The axioms that enumerate the
different squares and that characterize the winning positions are rather
long. You need not write these out in full, but indicate clearly what
they look like.)


---

##### Bài tập 12.2

You are to create a system for advising computer science undergraduates
on what courses to take over an extended period in order to satisfy the
program requirements. (Use whatever requirements are appropriate for
your institution.) First, decide on a vocabulary for representing all
the information, and then represent it; then formulate a query to the
system that will return a legal program of study as a solution. You
should allow for some tailoring to individual students, in that your
system should ask what courses or equivalents the student has already
taken, and not generate programs that repeat those courses.

Suggest ways in which your system could be improved—for example to take
into account knowledge about student preferences, the workload, good and
bad instructors, and so on. For each kind of knowledge, explain how it
could be expressed logically. Could your system easily incorporate this
information to find all feasible programs of study for a student? Could
it find the <i>best</i> program?


---

##### Bài tập 12.3

Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/ontology-figure.png">ontology-figure</a> shows the top levels of a
hierarchy for everything. Extend it to include as many real categories
as possible. A good way to do this is to cover all the things in your
everyday life. This includes objects and events. Start with waking up,
and proceed in an orderly fashion noting everything that you see, touch,
do, and think about. For example, a random sampling produces music,
news, milk, walking, driving, gas, Soda Hall, carpet, talking, Professor
Fateman, chicken curry, tongue, \$ 7, sun, the daily newspaper, and so on.<br>

You should produce both a single hierarchy chart (on a large sheet of
paper) and a listing of objects and categories with the relations
satisfied by members of each category. Every object should be in a
category, and every category should be in the hierarchy.


---

##### Bài tập 12.4

Develop a representational system for reasoning
about windows in a window-based computer interface. In particular, your
representation should be able to describe:<br>


-   The state of a window: minimized, displayed, or nonexistent.<br>

-   Which window (if any) is the active window.<br>

-   The position of every window at a given time.<br>

-   The order (front to back) of overlapping windows.<br>

-   The actions of creating, destroying, resizing, and moving windows;
    changing the state of a window; and bringing a window to the front.
    Treat these actions as atomic; that is, do not deal with the issue
    of relating them to mouse actions. Give axioms describing the
    effects of actions on fluents. You may use either event or
    situation calculus.<br>

Assume an ontology containing <i>situations,</i>
<i>actions,</i> <i>integers</i> (for $x$ and $y$
coordinates) and <i>windows</i>. Define a language over this
ontology; that is, a list of constants, function symbols, and predicates
with an English description of each. If you need to add more categories
to the ontology (e.g., pixels), you may do so, but be sure to specify
these in your write-up. You may (and should) use symbols defined in the
text, but be sure to list these explicitly.


---

##### Bài tập 12.5

State the following in the language you developed for the previous
exercise:<br>

1.  In situation $S_0$, window $W_1$ is behind $W_2$ but sticks out on
    the top and bottom. Do <i>not</i> state exact coordinates
    for these; describe the <i>general</i> situation.<br>

2.  If a window is displayed, then its top edge is higher than its
    bottom edge.<br>

3.  After you create a window $w$, it is displayed.<br>

4.  A window can be minimized only if it is displayed.<br>


---

##### Bài tập 12.6

State the following in the language you developed for the previous
exercise:<br>

1.  In situation $S_0$, window $W_1$ is behind $W_2$ but sticks out on
    the top and bottom. Do <i>not</i> state exact coordinates
    for these; describe the <i>general</i> situation.<br>

2.  If a window is displayed, then its top edge is higher than its
    bottom edge.<br>

3.  After you create a window $w$, it is displayed.<br>

4.  A window can be minimized only if it is displayed.<br>


---

##### Bài tập 12.7

(Adapted from an example by Doug Lenat.) Your mission is to capture, in
logical form, enough knowledge to answer a series of questions about the
following simple scenario:<br>
<Br>
<i> Yesterday John went to the North Berkeley Safeway supermarket and</i><br>
<i> bought two pounds of tomatoes and a pound of ground beef.</i>

Start by trying to represent the content of the sentence as a series of
assertions. You should write sentences that have straightforward logical
structure (e.g., statements that objects have certain properties, that
objects are related in certain ways, that all objects satisfying one
property satisfy another). The following might help you get started:<br>

-   Which classes, objects, and relations would you need? What are their
    parents, siblings and so on? (You will need events and temporal
    ordering, among other things.)<br>

-   Where would they fit in a more general hierarchy?<br>

-   What are the constraints and interrelationships among them?<br>

-   How detailed must you be about each of the various concepts?<br>

To answer the questions below, your knowledge base must include
background knowledge. You’ll have to deal with what kind of things are
at a supermarket, what is involved with purchasing the things one
selects, what the purchases will be used for, and so on. Try to make
your representation as general as possible. To give a trivial example:
don’t say “People buy food from Safeway,” because that won’t help you
with those who shop at another supermarket. Also, don’t turn the
questions into answers; for example, question (c) asks “Did John buy any
meat?”—not “Did John buy a pound of ground beef?”<br>

Sketch the chains of reasoning that would answer the questions. If
possible, use a logical reasoning system to demonstrate the sufficiency
of your knowledge base. Many of the things you write might be only
approximately correct in reality, but don’t worry too much; the idea is
to extract the common sense that lets you answer these questions at all.
A truly complete answer to this question is <i>extremely</i>
difficult, probably beyond the state of the art of current knowledge
representation. But you should be able to put together a consistent set
of axioms for the limited questions posed here.<br>

1.  Is John a child or an adult? [Adult]<br>

2.  Does John now have at least two tomatoes? [Yes]<br>

3.  Did John buy any meat? [Yes]<br>

4.  If Mary was buying tomatoes at the same time as John, did he see
    her? [Yes]<br>

5.  Are the tomatoes made in the supermarket? [No]<br>

6.  What is John going to do with the tomatoes? [Eat them]<br>

7.  Does Safeway sell deodorant? [Yes]<br>

8.  Did John bring some money or a credit card to the supermarket?
    [Yes]<br>

9.  Does John have less money after going to the supermarket? [Yes]<br>


---

##### Bài tập 12.8

Make the necessary additions or changes to your knowledge base from the
previous exercise so that the questions that follow can be answered.
Include in your report a discussion of your changes, explaining why they
were needed, whether they were minor or major, and what kinds of
questions would necessitate further changes.<br>

1.  Are there other people in Safeway while John is there?
    [Yes—staff!]<br>

2.  Is John a vegetarian? [No]<br>

3.  Who owns the deodorant in Safeway? [Safeway Corporation]<br>

4.  Did John have an ounce of ground beef? [Yes]<br>

5.  Does the Shell station next door have any gas? [Yes]<br>

6.  Do the tomatoes fit in John’s car trunk? [Yes]<br>


---

##### Bài tập 12.9

Represent the following seven sentences using and extending the
representations developed in the chapter: <br>

1.  Water is a liquid between 0 and 100 degrees.<br>

2.  Water boils at 100 degrees.<br>

3.  The water in John’s water bottle is frozen.<br>

4.  Perrier is a kind of water.<br>

5.  John has Perrier in his water bottle.<br>

6.  All liquids have a freezing point.<br>

7.  A liter of water weighs more than a liter of alcohol.<br>


---

##### Bài tập 12.10

Write definitions for the following:<br>

1.  ${ExhaustivePartDecomposition}$<br>

2.  ${PartPartition}$<br>

3.  ${PartwiseDisjoint}$<br>

These should be analogous to the definitions for
${ExhaustiveDecomposition}$, ${Partition}$, and ${Disjoint}$. Is
it the case that ${PartPartition}(s,{BunchOf}(s))$? If so, prove it;
if not, give a counterexample and define sufficient conditions under
which it does hold.


---

##### Bài tập 12.11

An alternative scheme for representing measures
involves applying the units function to an abstract length object. In
such a scheme, one would write ${Inches}({Length}(L_1)) = {1.5}$.
How does this scheme compare with the one in the chapter? Issues include
conversion axioms, names for abstract quantities (such as “50 dollars”),
and comparisons of abstract measures in different units (50 inches is
more than 50 centimeters).


---

##### Bài tập 12.12

Write a set of sentences that allows one to calculate the price of an
individual tomato (or other object), given the price per pound. Extend
the theory to allow the price of a bag of tomatoes to be calculated.


---

##### Bài tập 12.13

Add sentences to extend the definition of the
predicate ${Name}(s, c)$ so that a string such as “laptop computer”
matches the appropriate category names from a variety of stores. Try to
make your definition general. Test it by looking at ten online stores,
and at the category names they give for three different categories. For
example, for the category of laptops, we found the names “Notebooks,”
“Laptops,” “Notebook Computers,” “Notebook,” “Laptops and Notebooks,”
and “Notebook PCs.” Some of these can be covered by explicit ${Name}$
facts, while others could be covered by sentences for handling plurals,
conjunctions, etc.


---

##### Bài tập 12.14

Write event calculus axioms to describe the actions in the wumpus world.


---

##### Bài tập 12.15

State the interval-algebra relation that holds between every pair of the
following real-world events:<br>

> $LK$: The life of President Kennedy.<br>

> $IK$: The infancy of President Kennedy.<br>

> $PK$: The presidency of President Kennedy.<br>

> $LJ$: The life of President Johnson.<br>

> $PJ$: The presidency of President Johnson.<br>

> $LO$: The life of President Obama.<br>


---

##### Bài tập 12.16

This exercise concerns the problem of planning a route for a robot to
take from one city to another. The basic action taken by the robot is
${Go}(x,y)$, which takes it from city $x$ to city $y$ if there is a
route between those cities. ${Road}(x, y)$ is true if and only if
there is a road connecting cities $x$ and $y$; if there is, then
${Distance}(x, y)$ gives the length of the road. See the map on
page <a class="pageRef" title="" href="#">romania-distances-figure</a> for an example. The robot begins in Arad and must
reach Bucharest.<br>

1.  Write a suitable logical description of the initial situation of
    the robot.<br>

2.  Write a suitable logical query whose solutions provide possible
    paths to the goal.<br>

3.  Write a sentence describing the ${Go}$ action.<br>

4.  Now suppose that the robot consumes fuel at the rate of .02 gallons
    per mile. The robot starts with 20 gallons of fuel. Augment your
    representation to include these considerations.<br>

5.  Now suppose some of the cities have gas stations at which the robot
    can fill its tank. Extend your representation and write all the
    rules needed to describe gas stations, including the
    ${Fillup}$ action.<br>


---

##### Bài tập 12.17

Investigate ways to extend the event calculus to handle
<i>simultaneous</i> events. Is it possible to avoid a
combinatorial explosion of axioms?


---

##### Bài tập 12.18

Construct a representation for exchange rates
between currencies that allows for daily fluctuations.


---

##### Bài tập 12.19

Define the predicate ${Fixed}$, where
${Fixed}({Location}(x))$ means that the location of object $x$ is
fixed over time.


---

##### Bài tập 12.20

Describe the event of trading something for something else. Describe
buying as a kind of trading in which one of the objects traded is a sum
of money.


---

##### Bài tập 12.21

The two preceding exercises assume a fairly primitive notion of
ownership. For example, the buyer starts by <i>owning</i> the
dollar bills. This picture begins to break down when, for example, one’s
money is in the bank, because there is no longer any specific collection
of dollar bills that one owns. The picture is complicated still further
by borrowing, leasing, renting, and bailment. Investigate the various
commonsense and legal concepts of ownership, and propose a scheme by
which they can be represented formally.


---

##### Bài tập 12.22

(Adapted from <a class="paperRef" title="" href="">Fagin+al:1995</a>.) Consider a game played
with a deck of just 8 cards, 4 aces and 4 kings. The three players,
Alice, Bob, and Carlos, are dealt two cards each. Without looking at
them, they place the cards on their foreheads so that the other players
can see them. Then the players take turns either announcing that they
know what cards are on their own forehead, thereby winning the game, or
saying “I don’t know.” Everyone knows the players are truthful and are
perfect at reasoning about beliefs.<br>

1.  Game 1. Alice and Bob have both said “I don’t know.” Carlos sees
    that Alice has two aces (A-A) and Bob has two kings (K-K). What
    should Carlos say? (<i>Hint</i>: consider all three possible
    cases for Carlos: A-A, K-K, A-K.)<br>

2.  Describe each step of Game 1 using the notation of modal logic.<br>

3.  Game 2. Carlos, Alice, and Bob all said “I don’t know” on their
    first turn. Alice holds K-K and Bob holds A-K. What should Carlos
    say on his second turn?<br>

4.  Game 3. Alice, Carlos, and Bob all say “I don’t know” on their first
    turn, as does Alice on her second turn. Alice and Bob both hold A-K.
    What should Carlos say?<br>

5.  Prove that there will always be a winner to this game.<br>


---

##### Bài tập 12.23

The assumption of <i>logical omniscience,</i> discussed on
page <a class="pageRef" title="" href="#">logical-omniscience</a>, is of course not true of any actual reasoners.
Rather, it is an <i>idealization</i> of the reasoning process
that may be more or less acceptable depending on the applications.
Discuss the reasonableness of the assumption for each of the following
applications of reasoning about knowledge:<br>

1.  Partial knowledge adversary games, such as card games. Here one
    player wants to reason about what his opponent knows about the state
    of the game.<br>

2.  Chess with a clock. Here the player may wish to reason about the
    limits of his opponent’s or his own ability to find the best move in
    the time available. For instance, if player A has much more time
    left than player B, then A will sometimes make a move that greatly
    complicates the situation, in the hopes of gaining an advantage
    because he has more time to work out the proper strategy.<br>

3.  A shopping agent in an environment in which there are costs of
    gathering information.<br>

4.  Reasoning about public key cryptography, which rests on the
    intractability of certain computational problems.


---

##### Bài tập 12.24

The assumption of <i>logical omniscience,</i> discussed on
page <a class="pageRef" title="" href="#">logical-omniscience</a>, is of course not true of any actual reasoners.
Rather, it is an <i>idealization</i> of the reasoning process
that may be more or less acceptable depending on the applications.
Discuss the reasonableness of the assumption for each of the following
applications of reasoning about knowledge:<br>

1.  Partial knowledge adversary games, such as card games. Here one
    player wants to reason about what his opponent knows about the state
    of the game.<br>

2.  Chess with a clock. Here the player may wish to reason about the
    limits of his opponent’s or his own ability to find the best move in
    the time available. For instance, if player A has much more time
    left than player B, then A will sometimes make a move that greatly
    complicates the situation, in the hopes of gaining an advantage
    because he has more time to work out the proper strategy.<br>

3.  A shopping agent in an environment in which there are costs of
    gathering information.<br>

4.  Reasoning about public key cryptography, which rests on the
    intractability of certain computational problems.


---

##### Bài tập 12.25

Translate the following description logic expression (from
page <a class="pageRef" title="" href="#">description-logic-ex</a>) into first-order logic, and comment on the result:
<br>
$$
And(Man, AtLeast(3,Son), AtMost(2,Daughter), \\All(Son,And(Unemployed,Married, All(Spouse,Doctor ))), \\All(Daughter,And(Professor, Fills(Department ,Physics,Math))))
$$


---

##### Bài tập 12.26

Recall that inheritance information in semantic networks can be captured
logically by suitable implication sentences. This exercise investigates
the efficiency of using such sentences for inheritance.<br>

1.  Consider the information in a used-car catalog such as Kelly’s Blue
    Book—for example, that 1973 Dodge vans are (or perhaps were once)
    worth 575. Suppose all this information (for 11,000 models) is
    encoded as logical sentences, as suggested in the chapter. Write
    down three such sentences, including that for 1973 Dodge vans. How
    would you use the sentences to find the value of a
    <i>particular</i> car, given a backward-chaining theorem
    prover such as Prolog?<br>

2.  Compare the time efficiency of the backward-chaining method for
    solving this problem with the inheritance method used in
    semantic nets.<br>

3.  Explain how forward chaining allows a logic-based system to solve
    the same problem efficiently, assuming that the KB contains only the
    11,000 sentences about prices.<br>

4.  Describe a situation in which neither forward nor backward chaining
    on the sentences will allow the price query for an individual car to
    be handled efficiently.<br>

5.  Can you suggest a solution enabling this type of query to be solved
    efficiently in all cases in logic systems? <i>Hint:</i>
    Remember that two cars of the same year and model have the
    same price.)


---

##### Bài tập 12.27

One might suppose that the syntactic
distinction between unboxed links and singly boxed links in semantic
networks is unnecessary, because singly boxed links are always attached
to categories; an inheritance algorithm could simply assume that an
unboxed link attached to a category is intended to apply to all members
of that category. Show that this argument is fallacious, giving examples
of errors that would arise.


---

##### Bài tập 12.28

One part of the shopping process that was not covered in this chapter is
checking for compatibility between items. For example, if a digital
camera is ordered, what accessory batteries, memory cards, and cases are
compatible with the camera? Write a knowledge base that can determine
the compatibility of a set of items and suggest replacements or
additional items if the shopper makes a choice that is not compatible.
The knowledge base should works with at least one line of products and
extend easily to other lines.


---

##### Bài tập 12.29

A complete solution to the problem of
inexact matches to the buyer’s description in shopping is very difficult
and requires a full array of natural language processing and information
retrieval techniques. (See Chapters <a class="chapterRef" title="" href="{{site.baseurl}}/nlp1-exercises/">nlp1-chapter</a>
and <a class="chapterRef" title="" href="{{site.baseurl}}/nlp-communicating-exercises/">nlp-english-chapter</a>.) One small step is to allow the user to
specify minimum and maximum values for various attributes. The buyer
must use the following grammar for product descriptions:<br>

$$
Description \rightarrow Category \space [Connector \space Modifier]*
$$
$$
Connector \rightarrow "with" \space | "and" | ","
$$
$$
Modifier \rightarrow Attribute \space |\space Attribute \space Op \space Value
$$
$$
Op \rightarrow "=" | "\gt" | "\lt"
$$

Here, ${Category}$ names a product category, ${Attribute}$ is some
feature such as “CPU” or “price,” and ${Value}$ is the target value
for the attribute. So the query “computer with at least a 2.5 GHz CPU
for under 500” must be re-expressed as “computer with CPU $>$ 2.5 GHz
and price $<$ 500.” Implement a shopping agent that accepts descriptions
in this language.


---

##### Bài tập 12.30

Our description of Internet shopping omitted the
all-important step of actually <i>buying</i> the product.
Provide a formal logical description of buying, using event calculus.
That is, define the sequence of events that occurs when a buyer submits
a credit-card purchase and then eventually gets billed and receives the
product.


---


<!-- tabs:end -->
