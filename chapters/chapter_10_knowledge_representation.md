# Chapter 10 Knowledge Representation

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_10/chapter_10_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_10_Knowledge%20Representation.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**
*(Chưa có slide)*

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Logic](codeAndExercises/aima-python-master/notebooks/logic.ipynb)
- [Logic (Python File)](codeAndExercises/aima-python-master/notebooks/logic.py)


#### **Bài tập**

##### Bài tập 10.1

Consider a robot whose operation is described by the following PDDL
operators:<br>

$$
Op({Go(x,y)},{At(Robot,x)},{\lnot At(Robot,x) \land At(Robot,y)})
$$
$$
Op({Pick(o)},{At(Robot,x)\land At(o,x)},{\lnot At(o,x) \land Holding(o)})
$$
$$
Op({Drop(o)},{At(Robot,x)\land Holding(o)},{At(o,x) \land \lnot Holding(o)}
$$

1.  The operators allow the robot to hold more than one object. Show how
    to modify them with an $EmptyHand$ predicate for a robot that can
    hold only one object.<br>

2.  Assuming that these are the only actions in the world, write a
    successor-state axiom for $EmptyHand$.<br>


---

##### Bài tập 10.2

Describe the differences and similarities between problem solving and
planning.


---

##### Bài tập 10.3

Given the action schemas and initial state
from Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/airport-pddl-algorithm.png">airport-pddl-algorithm</a>, what are all the
applicable concrete instances of ${Fly}(p,{from},{to})$ in the
state described by<br>

$$
At(P_1,JFK) \land At(P_2,SFO) \land Plane(P_1) \land Plane(P_2) \land Airport(JFK) \land Airport(SFO)?
$$


---

##### Bài tập 10.4

The monkey-and-bananas problem is faced by a monkey in a laboratory with
some bananas hanging out of reach from the ceiling. A box is available
that will enable the monkey to reach the bananas if he climbs on it.
Initially, the monkey is at $A$, the bananas at $B$, and the box at $C$.
The monkey and box have height ${Low}$, but if the monkey climbs onto
the box he will have height ${High}$, the same as the bananas. The
actions available to the monkey include ${Go}$ from one place to
another, ${Push}$ an object from one place to another, ${ClimbUp}$
onto or ${ClimbDown}$ from an object, and ${Grasp}$ or ${Ungrasp}$
an object. The result of a ${Grasp}$ is that the monkey holds the
object if the monkey and object are in the same place at the same
height.<br>

1.  Write down the initial state description.<br>

2.  Write the six action schemas.<br>

3.  Suppose the monkey wants to fool the scientists, who are off to tea,
    by grabbing the bananas, but leaving the box in its original place.
    Write this as a general goal (i.e., not assuming that the box is
    necessarily at C) in the language of situation calculus. Can this
    goal be solved by a classical planning system?<br>

4.  Your schema for pushing is probably incorrect, because if the object
    is too heavy, its position will remain the same when the ${Push}$
    schema is applied. Fix your action schema to account for
    heavy objects.<br>


---

##### Bài tập 10.5

The original {Strips} planner was designed to control Shakey the robot.
Figure <a class="insideExercisesFigRef" href="#shakey-figure">shakey-figure</a> shows a version of Shakey’s world
consisting of four rooms lined up along a corridor, where each room has
a door and a light switch. The actions in Shakey’s world include moving from place to place,
pushing movable objects (such as boxes), climbing onto and down from
rigid objects (such as boxes), and turning light switches on and off.
The robot itself could not climb on a box or toggle a switch, but the
planner was capable of finding and printing out plans that were beyond
the robot’s abilities. Shakey’s six actions are the following:<br>

-   ${Go}(x,y,r)$, which requires that Shakey be ${At}$ $x$ and that
    $x$ and $y$ are locations ${In}$ the same room $r$. By convention
    a door between two rooms is in both of them.<br>

-   Push a box $b$ from location $x$ to location $y$ within the same
    room: ${Push}(b,x,y,r)$. You will need the predicate ${Box}$ and
    constants for the boxes.<br>

-   Climb onto a box from position $x$: ${ClimbUp}(x, b)$; climb down
    from a box to position $x$: ${ClimbDown}(b, x)$. We will need the
    predicate ${On}$ and the constant ${Floor}$.<br>

-   Turn a light switch on or off: ${TurnOn}(s,b)$;
    ${TurnOff}(s,b)$. To turn a light on or off, Shakey must be on top
    of a box at the light switch’s location.<br>

Write PDDL sentences for Shakey’s six actions and the initial state from
Construct a plan for Shakey to
get ${Box}{}_2$ into ${Room}{}_2$.<br>

  <figure>
    <img src="https://aimacode.github.io/aima-exercises/figures/shakey2.svg" alt="shakey-figure" id="shakey-figure" style="width:100%">
    <figcaption><center><b>Shakey's world. Shakey can move between landmarks within a room, can pass through the door between rooms, can climb climbable objects and push pushable objects, and can flip light switches.</b></center></figcaption>
  </figure>


---

##### Bài tập 10.6

A finite Turing machine has a finite one-dimensional tape of cells, each
cell containing one of a finite number of symbols. One cell has a read
and write head above it. There is a finite set of states the machine can
be in, one of which is the accept state. At each time step, depending on
the symbol on the cell under the head and the machine’s current state,
there are a set of actions we can choose from. Each action involves
writing a symbol to the cell under the head, transitioning the machine
to a state, and optionally moving the head left or right. The mapping
that determines which actions are allowed is the Turing machine’s
program. Your goal is to control the machine into the accept state.<br>
<br>
Represent the Turing machine acceptance problem as a planning problem.
If you can do this, it demonstrates that determining whether a planning
problem has a solution is at least as hard as the Turing acceptance
problem, which is PSPACE-hard.<br>


---

##### Bài tập 10.7

Explain why dropping negative effects from
every action schema results in a relaxed problem, provided that
preconditions and goals contain only positive literals.


---

##### Bài tập 10.8

Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sussman-anamoly-figure.png">sussman-anomaly-figure</a>
(page <a class="pageRef" title="" href="#">sussman-anomaly-figure</a>) shows a blocks-world problem that is known as the {Sussman anomaly}.
The problem was considered anomalous because the noninterleaved planners
of the early 1970s could not solve it. Write a definition of the problem
and solve it, either by hand or with a planning program. A
noninterleaved planner is a planner that, when given two subgoals
$G_{1}$ and $G_{2}$, produces either a plan for $G_{1}$ concatenated
with a plan for $G_{2}$, or vice versa. Can a noninterleaved planner
solve this problem? How, or why not?


---

##### Bài tập 10.9

Prove that backward search with PDDL problems is complete.


---

##### Bài tập 10.10

Construct levels 0, 1, and 2 of the planning graph for the problem in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/airport-pddl-algorithm.png">airport-pddl-algorithm</a>


---

##### Bài tập 10.11

Prove the following assertions about
planning graphs:<br>

1.  A literal that does not appear in the final level of the graph
    cannot be achieved.<br>

2.  The level cost of a literal in a serial graph is no greater than the
    actual cost of an optimal plan for achieving it.<br>


---

##### Bài tập 10.12

We saw that planning graphs can handle only propositional actions. What
if we want to use planning graphs for a problem with variables in the
goal, such as ${At}(P_{1}, x) \land {At}(P_{2}, x)$, where $x$ is assumed to be bound by an
existential quantifier that ranges over a finite domain of locations?
How could you encode such a problem to work with planning graphs?


---

##### Bài tập 10.13

The set-level heuristic (see page <a class="pageRef" title="" href="#">set-level-page</a> uses a planning graph
to estimate the cost of achieving a conjunctive goal from the current
state. What relaxed problem is the set-level heuristic the solution to?


---

##### Bài tập 10.14

Examine the definition of <b>bidirectional search</b> in Chapter <a class="chapterRef" title="" href="{{site.baseurl}}/search-exercises/">search-chapter</a>.<br>

1.  Would bidirectional state-space search be a good idea for planning?<br>

2.  What about bidirectional search in the space of partial-order plans?<br>

3.  Devise a version of partial-order planning in which an action can be
    added to a plan if its preconditions can be achieved by the effects
    of actions already in the plan. Explain how to deal with conflicts
    and ordering constraints. Is the algorithm essentially identical to
    forward state-space search?<br>


---

##### Bài tập 10.15

We contrasted forward and backward state-space searchers with
partial-order planners, saying that the latter is a plan-space searcher.
Explain how forward and backward state-space search can also be
considered plan-space searchers, and say what the plan refinement
operators are.


---

##### Bài tập 10.16

Up to now we have assumed that the
plans we create always make sure that an action’s preconditions are
satisfied. Let us now investigate what propositional successor-state
axioms such as ${HaveArrow}^{t+1} {\;\;{\Leftrightarrow}\;\;}{}$
$({HaveArrow}^t \land \lnot {Shoot}^t)$ have to say about actions whose preconditions
are not satisfied.<br>

1.  Show that the axioms predict that nothing will happen when an action
    is executed in a state where its preconditions are not satisfied.<br>

2.  Consider a plan $p$ that contains the actions required to achieve a
    goal but also includes illegal actions. Is it the case that
$$
initial state \land successor-state axioms \land
p {\models} goal ?
$$

3.  With first-order successor-state axioms in situation calculus, is it
    possible to prove that a plan containing illegal actions will
    achieve the goal?<br>


---

##### Bài tập 10.17

Consider how to translate a set of action
schemas into the successor-state axioms of situation calculus.<br>

1.  Consider the schema for ${Fly}(p,{from},{to})$. Write a
    logical definition for the predicate
    ${Poss}({Fly}(p,{from},{to}),s)$, which is true if the
    preconditions for ${Fly}(p,{from},{to})$ are satisfied in
    situation $s$.<br>

2.  Next, assuming that ${Fly}(p,{from},{to})$ is the only action
    schema available to the agent, write down a successor-state axiom
    for ${At}(p,x,s)$ that captures the same information as the
    action schema.<br>

3.  Now suppose there is an additional method of travel:
    ${Teleport}(p,{from},{to})$. It has the additional
    precondition $\lnot {Warped}(p)$ and the additional effect
    ${Warped}(p)$. Explain how the situation calculus knowledge base
    must be modified.<br>

4.  Finally, develop a general and precisely specified procedure for
    carrying out the translation from a set of action schemas to a set
    of successor-state axioms.<br>


---

##### Bài tập 10.18

In the $SATPlan$ algorithm in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/satplan-agent-algorithm.png">satplan-agent-algorithm</a> (page <a class="pageRef" title="" href="#">satplan-agent-algorithm</a>,
each call to the satisfiability algorithm asserts a goal $g^T$, where
$T$ ranges from 0 to $T_{max}$. Suppose instead that the
satisfiability algorithm is called only once, with the goal
$g^0 \vee g^1 \vee \cdots \vee g^{T_{max}}$. <br>

1.  Will this always return a plan if one exists with length less than
    or equal to $T_{max}$? <br>

2.  Does this approach introduce any new spurious “solutions”?<br>

3.  Discuss how one might modify a satisfiability algorithm such as $WalkSAT$ so
    that it finds short solutions (if they exist) when given a
    disjunctive goal of this form.<br>


---


<!-- tabs:end -->
