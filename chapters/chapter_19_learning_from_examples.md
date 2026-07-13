# Chapter 19 Learning from examples

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_19_Learning%20from%20examples/chapter_19_vi.html?v=2" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_19_Learning%20from%20examples.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**
*(Chưa có slide)*

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [LEARN-DECISION-TREE](codeAndExercises/aima-pseudocode-master/md/Decision-Tree-Learning.md)
- [CROSS-VALIDATION-WRAPPER](codeAndExercises/aima-pseudocode-master/md/Cross-Validation-Wrapper.md)
- [DECISION-LIST-LEARNING](codeAndExercises/aima-pseudocode-master/md/Decision-List-Learning.md)
- [ADABOOST](codeAndExercises/aima-pseudocode-master/md/AdaBoost.md)
- [CURRENT-BEST-LEARNING](codeAndExercises/aima-pseudocode-master/md/Current-Best-Learning.md)
- [VERSION-SPACE-LEARNING](codeAndExercises/aima-pseudocode-master/md/Version-Space-Learning.md)
- [MINIMAL-CONSISTENT-DET](codeAndExercises/aima-pseudocode-master/md/Minimal-Consistent-Det.md)
- [FOIL](codeAndExercises/aima-pseudocode-master/md/Foil.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Learning](codeAndExercises/aima-python-master/notebooks/learning.ipynb)
- [Learning (Python File)](codeAndExercises/aima-python-master/notebooks/learning.py)
- [Learning Apps](codeAndExercises/aima-python-master/notebooks/learning_apps.ipynb)
- [Learning Apps (Python File)](codeAndExercises/aima-python-master/notebooks/learning_apps.py)


#### **Bài tập**

##### Bài tập 19.1

Show, by translating into conjunctive normal form and
applying resolution, that the conclusion drawn on page <a class="pageRef" title="" href="#">dbsig-page</a>
concerning Brazilians is sound.


---

##### Bài tập 19.2

For each of the following determinations, write down the logical
representation and explain why the determination is true (if it is):<br>

1.  Design and denomination determine the mass of a coin.<br>

2.  For a given program, input determines output.<br>

3.  Climate, food intake, exercise, and metabolism determine weight gain
    and loss.<br>

4.  Baldness is determined by the baldness (or lack thereof) of one’s
    maternal grandfather. <br>


---

##### Bài tập 19.3

For each of the following determinations, write down the logical
representation and explain why the determination is true (if it is):<br>

1.  Zip code determines the state (U.S.).<br>

2.  Design and denomination determine the mass of a coin.<br>

3.  Climate, food intake, exercise, and metabolism determine weight gain
    and loss.<br>

4.  Baldness is determined by the baldness (or lack thereof) of one’s
    maternal grandfather.<br>


---

##### Bài tập 19.4

Would a probabilistic version of determinations be useful? Suggest a
definition.


---

##### Bài tập 19.5

Fill in the missing values for the clauses $C_1$ or
$C_2$ (or both) in the following sets of clauses, given that $C$ is the
resolvent of $C_1$ and $C_2$:<br>

1.  $C = {True} \Rightarrow P(A,B)$,
    $C_1 = P(x,y) \Rightarrow Q(x,y)$, $C_2 = ??$.<br>

2.  $C = {True} \Rightarrow P(A,B)$, $C_1 = ??$,
    $C_2 = ??$.<br>

3.  $C = P(x,y) \Rightarrow P(x,f(y))$, $C_1 = ??$,
    $C_2 = ??$.<br>

If there is more than one possible solution, provide one example of each
different kind.<br>


---

##### Bài tập 19.6

Suppose one writes a logic program that carries
out a resolution inference step. That is, let ${Resolve}(c_1,c_2,c)$
succeed if $c$ is the result of resolving $c_1$ and $c_2$. Normally,
${Resolve}$ would be used as part of a theorem prover by calling it
with $c_1$ and $c_2$ instantiated to particular clauses, thereby
generating the resolvent $c$. Now suppose instead that we call it with
$c$ instantiated and $c_1$ and $c_2$ uninstantiated. Will this succeed
in generating the appropriate results of an inverse resolution step?
Would you need any special modifications to the logic programming system
for this to work?


---

##### Bài tập 19.7

Suppose that is considering adding a literal
to a clause using a binary predicate $P$ and that previous literals
(including the head of the clause) contain five different variables.<br>

1.  How many functionally different literals can be generated? Two
    literals are functionally identical if they differ only in the names
    of the *new* variables that they contain.<br>

2.  Can you find a general formula for the number of different literals
    with a predicate of arity $r$ when there are $n$ variables
    previously used?<br>

3.  Why does not allow literals that contain no previously used
    variables?<br>


---

##### Bài tập 19.8

Using the data from the family tree in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/family2-figure.png">family2-figure</a>, or a subset thereof, apply the
algorithm to learn a definition for the ${Ancestor}$ predicate.


---


<!-- tabs:end -->
