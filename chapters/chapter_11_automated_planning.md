# Chapter 11 Automated Planning

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi/chapter_11_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_11_Automated%20Planning.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**
*(Chưa có slide)*

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [AIR-CARGO-TRANSPORT-PROBLEM](codeAndExercises/aima-pseudocode-master/md/Air-Cargo-Transport-Problem.md)
- [SPARE-TIRE-PROBLEM](codeAndExercises/aima-pseudocode-master/md/Spare-Tire-Problem.md)
- [BLOCKS-WORLD](codeAndExercises/aima-pseudocode-master/md/Blocks-World.md)
- [HAVE-CAKE-AND-EAT-CAKE-TOO-PROBLEM](codeAndExercises/aima-pseudocode-master/md/Have-Cake-And-Eat-Cake-Too.md)
- [GRAPHPLAN](codeAndExercises/aima-pseudocode-master/md/GraphPlan.md)
- [REFINEMENT-HIGH-LEVEL-ACTIONS](codeAndExercises/aima-pseudocode-master/md/Refinement-High-Level-Actions.md)
- [HIERARCHICAL-SEARCH](codeAndExercises/aima-pseudocode-master/md/Hierarchical-Search.md)
- [ANGELIC-SEARCH](codeAndExercises/aima-pseudocode-master/md/Angelic-Search.md)
- [JOB-SHOP-SCHEDULING-PROBLEM](codeAndExercises/aima-pseudocode-master/md/Job-Shop-Scheduling-Problem.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Planning](codeAndExercises/aima-python-master/notebooks/planning.ipynb)
- [Planning (Python File)](codeAndExercises/aima-python-master/notebooks/planning.py)
- [Classical Planning Approaches](codeAndExercises/aima-python-master/notebooks/classical_planning_approaches.ipynb)
- [Classical Planning Approaches (Python File)](codeAndExercises/aima-python-master/notebooks/classical_planning_approaches.py)
- [Planning Angelic Search](codeAndExercises/aima-python-master/notebooks/planning_angelic_search.ipynb)
- [Planning Angelic Search (Python File)](codeAndExercises/aima-python-master/notebooks/planning_angelic_search.py)
- [Planning Graph Plan](codeAndExercises/aima-python-master/notebooks/planning_graph_plan.ipynb)
- [Planning Graph Plan (Python File)](codeAndExercises/aima-python-master/notebooks/planning_graph_plan.py)
- [Planning Hierarchical Search](codeAndExercises/aima-python-master/notebooks/planning_hierarchical_search.ipynb)
- [Planning Hierarchical Search (Python File)](codeAndExercises/aima-python-master/notebooks/planning_hierarchical_search.py)
- [Planning Partial Order Planner](codeAndExercises/aima-python-master/notebooks/planning_partial_order_planner.ipynb)
- [Planning Partial Order Planner (Python File)](codeAndExercises/aima-python-master/notebooks/planning_partial_order_planner.py)
- [Planning Total Order Planner](codeAndExercises/aima-python-master/notebooks/planning_total_order_planner.ipynb)
- [Planning Total Order Planner (Python File)](codeAndExercises/aima-python-master/notebooks/planning_total_order_planner.py)


#### **Bài tập**

##### Bài tập 11.1

The goals we have considered so far all ask the planner to make the
world satisfy the goal at just one time step. Not all goals can be
expressed this way: you do not achieve the goal of suspending a
chandelier above the ground by throwing it in the air. More seriously,
you wouldn’t want your spacecraft life-support system to supply oxygen
one day but not the next. A <i>maintenance goal</i> is achieved
when the agent’s plan causes a condition to hold continuously from a
given state onward. Describe how to extend the formalism of this chapter
to support maintenance goals.


---

##### Bài tập 11.2

You have a number of trucks with which to deliver a set of packages.
Each package starts at some location on a grid map, and has a
destination somewhere else. Each truck is directly controlled by moving
forward and turning. Construct a hierarchy of high-level actions for
this problem. What knowledge about the solution does your hierarchy
encode?


---

##### Bài tập 11.3

Suppose that a high-level action has exactly one
implementation as a sequence of primitive actions. Give an algorithm for
computing its preconditions and effects, given the complete refinement
hierarchy and schemas for the primitive actions.


---

##### Bài tập 11.4

Suppose that the optimistic reachable set of a high-level plan is a
superset of the goal set; can anything be concluded about whether the
plan achieves the goal? What if the pessimistic reachable set doesn’t
intersect the goal set? Explain.


---

##### Bài tập 11.5

Write an algorithm that takes an initial
state (specified by a set of propositional literals) and a sequence of
HLAs (each defined by preconditions and angelic specifications of
optimistic and pessimistic reachable sets) and computes optimistic and
pessimistic descriptions of the reachable set of the sequence.


---

##### Bài tập 11.6

In Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/jobshop-cpm-figure.png">jobshop-cpm-figure</a> we showed how to describe
actions in a scheduling problem by using separate fields for , , and .
Now suppose we wanted to combine scheduling with nondeterministic
planning, which requires nondeterministic and conditional effects.
Consider each of the three fields and explain if they should remain
separate fields, or if they should become effects of the action. Give an
example for each of the three.


---

##### Bài tập 11.7

Some of the operations in standard programming languages can be modeled
as actions that change the state of the world. For example, the
assignment operation changes the contents of a memory location, and the
print operation changes the state of the output stream. A program
consisting of these operations can also be considered as a plan, whose
goal is given by the specification of the program. Therefore, planning
algorithms can be used to construct programs that achieve a given
specification. <br>

1.  Write an action schema for the assignment operator (assigning the
    value of one variable to another). Remember that the original value
    will be overwritten! <br>

2.  Show how object creation can be used by a planner to produce a plan
    for exchanging the values of two variables by using a
    temporary variable. <br>


---

##### Bài tập 11.8

Consider the following argument: In a framework that allows uncertain
initial states, <b>nondeterministic effects</b>
are just a notational convenience, not a source of additional
representational power. For any action schema $a$ with nondeterministic
effect $P \lor Q$, we could always replace it with the conditional
effects ${~R{:}~P} \land {~\lnot R{:}~Q}$, which in turn can be
reduced to two regular actions. The proposition $R$ stands for a random
proposition that is unknown in the initial state and for which there are
no sensing actions. Is this argument correct? Consider separately two
cases, one in which only one instance of action schema $a$ is in the
plan, the other in which more than one instance is.


---

##### Bài tập 11.9

Suppose the ${Flip}$ action
always changes the truth value of variable $L$. Show how to define its
effects by using an action schema with conditional effects. Show that,
despite the use of conditional effects, a 1-CNF belief state
representation remains in 1-CNF after a ${Flip}$.


---

##### Bài tập 11.10

In the blocks world we were forced to introduce two action schemas,
${Move}$ and ${MoveToTable}$, in order to maintain the ${Clear}$
predicate properly. Show how conditional effects can be used to
represent both of these cases with a single action.


---

##### Bài tập 11.11

Conditional effects were illustrated for the
${Suck}$ action in the vacuum world—which square becomes clean depends
on which square the robot is in. Can you think of a new set of
propositional variables to define states of the vacuum world, such that
${Suck}$ has an <i>unconditional</i> description? Write out
the descriptions of ${Suck}$, ${Left}$, and ${Right}$, using your
propositions, and demonstrate that they suffice to describe all possible
states of the world.


---

##### Bài tập 11.12

Find a suitably dirty carpet, free of obstacles, and vacuum it. Draw the
path taken by the vacuum cleaner as accurately as you can. Explain it,
with reference to the forms of planning discussed in this chapter.


---

##### Bài tập 11.13

The following quotes are from the backs of shampoo bottles. Identify
each as an unconditional, conditional, or execution-monitoring plan. (a)
“Lather. Rinse. Repeat.” (b) “Apply shampoo to scalp and let it remain
for several minutes. Rinse and repeat if necessary.” (c) “See a doctor
if problems persist.”


---

##### Bài tập 11.14

Consider the following problem: A patient arrives at the doctor’s office
with symptoms that could have been caused either by dehydration or by
disease $D$ (but not both). There are two possible actions: ${Drink}$,
which unconditionally cures dehydration, and ${Medicate}$, which cures
disease $D$ but has an undesirable side effect if taken when the patient
is dehydrated. Write the problem description, and diagram a sensorless
plan that solves the problem, enumerating all relevant possible worlds.


---

##### Bài tập 11.15

To the medication problem in the previous exercise, add a ${Test}$
action that has the conditional effect ${CultureGrowth}$ when
${Disease}$ is true and in any case has the perceptual effect
${Known}({CultureGrowth})$. Diagram a conditional plan that solves
the problem and minimizes the use of the ${Medicate}$ action.


---


<!-- tabs:end -->
