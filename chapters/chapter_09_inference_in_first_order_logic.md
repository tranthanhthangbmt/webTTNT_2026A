# Chapter 09 Inference in First-order Logic

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_09/chapter_09_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_09_Inference%20in%20First-order%20Logic.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter09_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter09_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter09_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter09/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/Unify.md" target="_blank" data-ignore>UNIFY</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/FOL-FC-Ask.md" target="_blank" data-ignore>FOL-FC-ASK</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/FOL-BC-Ask.md" target="_blank" data-ignore>FOL-BC-ASK</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Append.md" target="_blank" data-ignore>APPEND</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Logic**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/logic.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/logic.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/logic.ipynb" download>Tải .ipynb</a>



#### **Bài tập**




##### Bài tập 9.1
Chứng minh rằng Universal Instantiation là sound và Existential Instantiation tạo ra một knowledge base tương đương về mặt suy luận (inferentially equivalent).


---


##### Bài tập 9.2
Từ ${Likes}({Jerry},{IceCream})$ có vẻ hợp lý khi suy luận ra
${\exists\,x\;\;} {Likes}(x,{IceCream})$. Hãy viết ra một inference rule tổng quát cho phép thực hiện suy luận này. Nêu rõ các điều kiện cần được thỏa mãn bởi các biến và terms liên quan.


---


##### Bài tập 9.3
Giả sử một knowledge base chỉ chứa một câu duy nhất,
$\exists\,x\ {AsHighAs}(x,{Everest})$. Câu nào trong số các câu sau đây là
kết quả hợp lệ của việc áp dụng Existential Instantiation?<br>

1.  ${AsHighAs}({Everest},{Everest})$.<br>

2.  ${AsHighAs}({Kilimanjaro},{Everest})$.<br>

3.  ${AsHighAs}({Kilimanjaro},{Everest}) \land {AsHighAs}({BenNevis},{Everest})$\
    (sau hai lần áp dụng).<br>


---


##### Bài tập 9.4
Đối với mỗi cặp câu nguyên tử (atomic sentences), hãy đưa ra most general unifier nếu nó tồn tại:<br>

1.  $P(A,B,B)$, $P(x,y,z)$.<br>

2.  $Q(y,G(A,B))$, $Q(G(x,x),y)$.<br>

3.  ${Older}({Father}(y),y)$, ${Older}({Father}(x),{John})$.<br>

4.  ${Knows}({Father}(y),y)$, ${Knows}(x,x)$.<br>


---


##### Bài tập 9.5
Đối với mỗi cặp câu nguyên tử (atomic sentences), hãy đưa ra most general unifier nếu nó
tồn tại:<br>

1.  $P(A,B,B)$, $P(x,y,z)$.<br>

2.  $Q(y,G(A,B))$, $Q(G(x,x),y)$.<br>

3.  ${Older}({Father}(y),y)$, ${Older}({Father}(x),{John})$.<br>

4.  ${Knows}({Father}(y),y)$, ${Knows}(x,x)$.<br>


---


##### Bài tập 9.6
Xét các subsumption lattice được thể hiện
trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/subsumption-lattice-figure.png">subsumption-lattice-figure</a>
(trang <a class="pageRef" title="" href="#">subsumption-lattice-figure</a><br>.

1.  Xây dựng lattice cho câu
    ${Employs}({Mother}({John}),{Father}({Richard}))$.<br>

2.  Xây dựng lattice cho câu ${Employs}({IBM},y)$
    (“Mọi người đều làm việc cho IBM”). Hãy nhớ bao gồm mọi loại query
    unify với câu này.<br>

3.  Giả sử index mỗi câu dưới mọi node trong
    subsumption lattice của nó. Giải thích cách thức hoạt động khi một số câu này
    chứa biến; hãy lấy các câu ở (a) và (b) làm ví dụ
    cùng với query ${Employs}(x,{Father}(x))$.


---


##### Bài tập 9.7
Viết các biểu diễn logic cho các câu sau đây, thích hợp để sử dụng với Generalized Modus Ponens:<br>

1.  Horses, cows, and pigs are mammals.<br>

2.  An offspring của a horse là a horse.<br>

3.  Bluebeard là a horse.<br>

4.  Bluebeard là Charlie’s parent.<br>

5.  Offspring và parent là các quan hệ nghịch đảo (inverse relations).<br>

6.  Mọi mammal đều có a parent.<br>


---


##### Bài tập 9.8
Các câu hỏi này liên quan đến các vấn đề về substitution và Skolemization.<br>

1.  Cho tiền đề ${\forall\,x\;\;} {\exists\,y\;\;} P(x,y)$, việc kết luận rằng ${\exists\,q\;\;} P(q,q)$ là không hợp lệ. Hãy đưa ra một ví dụ về một predicate $P$ mà trong đó mệnh đề thứ nhất là đúng nhưng mệnh đề thứ hai là sai.<br>

2.  Giả sử rằng một inference engine được viết một cách không chính xác khi bỏ qua occurs check, do đó nó cho phép một literal như $P(x,F(x))$ được unify với $P(q,q)$. (Như đã đề cập, hầu hết các cài đặt chuẩn của Prolog thực tế đều cho phép điều này.) Hãy chứng minh rằng một inference engine như vậy sẽ cho phép kết luận ${\exists\,y\;\;} P(q,q)$ được suy ra từ tiền đề ${\forall\,x\;\;} {\exists\,y\;\;} P(x,y)$.<br>

3.  Giả sử rằng một thủ tục chuyển đổi logic bậc nhất (first-order logic) sang clausal form thực hiện Skolemization sai cho ${\forall\,x\;\;} {\exists\,y\;\;} P(x,y)$ thành $P(x,Sk0)$—tức là nó thay thế $y$ bằng một Skolem constant thay vì bằng một Skolem function của $x$. Hãy chứng minh rằng một inference engine sử dụng thủ tục đó cũng sẽ cho phép ${\exists\,q\;\;} P(q,q)$ được suy ra từ tiền đề ${\forall\,x\;\;} {\exists\,y\;\;} P(x,y)$.<br>

4.  Một lỗi phổ biến ở học sinh/sinh viên là cho rằng, trong unification, người ta được phép substitute một term cho một Skolem constant thay vì cho một variable. Ví dụ, họ sẽ nói rằng các công thức $P(Sk1)$ và $P(A)$ có thể được unify theo substitution $\{ Sk1/A \}$. Hãy đưa ra một ví dụ mà ở đó điều này dẫn đến một phép suy luận không hợp lệ.<br>


---


##### Bài tập 9.9
Câu hỏi này xem xét các Horn KB, ví dụ như sau:
$$\begin{array}{l}
P(F(x)) {\:\;{\Rightarrow}\:\;}P(x)\\
Q(x) {\:\;{\Rightarrow}\:\;}P(F(x))\\
P(A)\\
Q(B)
\end{array}$$ Cho FC là một thuật toán forward-chaining theo chiều rộng liên tục thêm vào tất cả các hệ quả của các rule hiện đang thỏa mãn; cho BC là một thuật toán backward-chaining theo chiều sâu từ trái sang phải thử các clause theo thứ tự được đưa ra trong KB. Phát biểu nào sau đây là đúng?<br>

1.  FC sẽ suy diễn ra literal $Q(A)$.<br>

2.  FC sẽ suy diễn ra literal $P(B)$.<br>

3.  Nếu FC không suy diễn được một literal cho trước, thì literal đó không được entail bởi KB.<br>

4.  BC sẽ trả về ${true}$ khi nhận được query $P(B)$.<br>

5.  Nếu BC không trả về ${true}$ khi nhận được một query literal, thì literal đó không được entail bởi KB.<br>


---


##### Bài tập 9.10
Hãy giải thích cách biểu diễn bất kỳ bài toán 3-SAT cho trước nào với kích thước tùy ý bằng cách sử dụng một first-order definite clause duy nhất và không quá 30 ground facts.


---


##### Bài tập 9.11
Giả sử cho trước các tiên đề sau:<br>

 1. $0 \leq 3$.<br>
 2. $7 \leq 9$.<br>
 3. ${\forall\,x\;\;} \; \; x \leq x$.<br>
 4. ${\forall\,x\;\;} \; \; x \leq x+0$.<br>
 5. ${\forall\,x\;\;} \; \; x+0 \leq x$.<br>
 6. ${\forall\,x,y\;\;} \; \; x+y \leq y+x$.<br>
 7. ${\forall\,w,x,y,z\;\;} \; \; w \leq y$ $\wedge$ $x \leq z$ ${\:\;{\Rightarrow}\:\;}$ $w+x \leq y+z$.<br>
 8. ${\forall\,x,y,z\;\;} \; \; x \leq y \wedge y \leq z \: {\:\;{\Rightarrow}\:\;}\: x \leq z$ <br>
<br>
1.  Hãy đưa ra một phép chứng minh backward-chaining cho mệnh đề $7 \leq 3+9$. (Hãy chắc chắn rằng, tất nhiên, bạn chỉ sử dụng các tiên đề được cho ở đây, chứ không phải bất kỳ điều gì khác mà bạn có thể biết về số học.) Chỉ hiển thị các bước dẫn đến thành công, không hiển thị các bước không liên quan.<br>

2.  Hãy đưa ra một phép chứng minh forward-chaining cho mệnh đề $7 \leq 3+9$. Một lần nữa, chỉ hiển thị các bước dẫn đến thành công.<br>


---


##### Bài tập 9.12
Giả sử bạn được cho các tiên đề sau:<br>

> 1. $0 \leq 4$.<br>

> 2. $5 \leq 9$.<br>

> 3. ${\forall\,x\;\;} \; \; x \leq x$.<br>

> 4. ${\forall\,x\;\;} \; \; x \leq x+0$.<br>

> 5. ${\forall\,x\;\;} \; \; x+0 \leq x$.<br>

> 6. ${\forall\,x,y\;\;} \; \; x+y \leq y+x$.<br>

> 7. ${\forall\,w,x,y,z\;\;} \; \; w \leq y$ $\wedge$ $x \leq z {\:\;{\Rightarrow}\:\;}$ $w+x \leq y+z$.<br>

> 8. ${\forall\,x,y,z\;\;} \; \; x \leq y \wedge y \leq z \: {\:\;{\Rightarrow}\:\;}\: x \leq z$<br>
<br>
1.  Hãy đưa ra một chứng minh backward-chaining cho câu $5 \leq 4+9$. (Hãy
    chắc chắn rằng, tất nhiên, bạn chỉ sử dụng các tiên đề được cho ở đây, chứ không dùng bất kỳ điều
    gì khác mà bạn biết về số học.) Chỉ hiển thị các bước dẫn đến
    thành công, không hiển thị các bước không liên quan.<br>

2.  Hãy đưa ra một chứng minh forward-chaining cho câu $5 \leq 4+9$. Một lần nữa,
    chỉ hiển thị các bước dẫn đến thành công.


---


##### Bài tập 9.13
Một câu đố trẻ em phổ biến là “Brothers and sisters have I none, but that man’s father is my father’s son.” Hãy sử dụng các quy tắc của domain gia đình (Mục <a class="sectionRef" title="" href="#">kinship-domain-section</a> ở trang <a class="pageRef" title="" href="#">kinship-domain-section</a>) để chỉ ra người đàn ông đó là ai. Bạn có thể áp dụng bất kỳ phương pháp inference nào được mô tả trong chương này. Tại sao bạn nghĩ câu đố này lại khó?

---


##### Bài tập 9.14
Giả sử chúng ta đưa vào một logical knowledge base một phân đoạn dữ liệu điều tra dân số của Hoa Kỳ liệt kê age, city of residence, date of birth, và mother của mọi người, sử dụng số an sinh xã hội làm hằng số định danh cho từng người. Do đó, age của George được cho bởi ${Age}(443-65-1282, 56)$. Những scheme indexing nào từ S1–S5 cho phép giải quyết hiệu quả cho những query nào từ Q1–Q4 (giả sử dùng backward chaining thông thường)?<br>
<br>
- <b>S1</b>: một index cho mỗi atom ở mỗi vị trí.<br>
- <b>S2</b>: một index cho mỗi first argument.<br>
- <b>S3</b>: một index cho mỗi predicate atom.<br>
- <b>S4</b>: một index cho mỗi <i>combination</i> của predicate và first argument.<br>
- <b>S5</b>: một index cho mỗi <i>combination</i> của predicate và second argument và một index cho mỗi first argument.<br>
- <b>Q1</b>: ${Age}(\mbox 443-44-4321,x)$<br>
- <b>Q2</b>: ${ResidesIn}(x,{Houston})$<br>
- <b>Q3</b>: ${Mother}(x,y)$<br>
- <b>Q4</b>: ${Age}(x,{34}) \land {ResidesIn}(x,{TinyTownUSA})$<br>


---


##### Bài tập 9.15
One might suppose that we can avoid the
problem of variable conflict in unification during backward chaining by
standardizing apart all of the sentences in the knowledge base once and
for all. Show that, for some sentences, this approach cannot work.
(<i>Hint</i>: Consider a sentence in which one part unifies with
another.)


---


##### Bài tập 9.16
Trong bài tập này, hãy sử dụng các câu bạn đã viết trong
Exercise <a href="#">fol-horses-exercise</a> để trả lời một câu hỏi bằng
cách sử dụng thuật toán backward-chaining.<br>

1.  Vẽ proof tree được tạo ra bởi thuật toán exhaustive backward-chaining
    cho query ${\exists\,h\;\;}{Horse}(h)$, trong đó các
    clause được khớp theo thứ tự đã cho.<br>

2.  Bạn nhận thấy điều gì về domain này?<br>

3.  Có bao nhiêu solution cho $h$ thực sự suy ra từ các câu của bạn?<br>

4.  Bạn có nghĩ ra cách nào để tìm tất cả chúng không? (<i>Gợi ý</i>:
    Xem <a class="paperRef" title="" href="#">Smith+al:1986</a>.)<br>


---


##### Bài tập 9.17
Trace the execution of the backward-chaining
algorithm in Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/backward-chaining-algorithm">backward-chaining-algorithm</a>
(page <a class="pageRef" title="" href="#">backward-chaining-algorithm</a> when it is applied to solve the crime problem
(page <A href="#">west-problem-page</a>. Show the sequence of values taken on by the
${goals}$ variable, and arrange them into a tree.


---


##### Bài tập 9.18
Đoạn mã Prolog sau đây định nghĩa một vị từ (predicate) P. (Hãy nhớ rằng các thuật ngữ viết hoa là các biến, không phải hằng số, trong Prolog.)<br>

        P(X,[X|Y]).<br>
        P(X,[Y|Z]) :- P(X,Z).<br>

1.  Hãy biểu diễn proof tree và các nghiệm cho các query
    P(A,[2,1,3]) và P(2,[1,A,3]).<br>

2.  P đại diện cho thao tác trên list chuẩn nào?<br>


---


##### Bài tập 9.19
Đoạn mã Prolog sau đây định nghĩa một vị từ P. (Hãy nhớ rằng
các thuật ngữ viết hoa là các biến, không phải là hằng số, trong Prolog.)<br>

        P(X,[X|Y]).<br>
        P(X,[Y|Z]) :- P(X,Z).<br>

1.  Hiển thị proof tree và các nghiệm cho các query
    P(A,[1,2,3]) và P(2,[1,A,3]).<br>

2.  P đại diện cho list operation tiêu chuẩn nào?<br>


---


##### Bài tập 9.20
This exercise looks at sorting in Prolog.<br>

1.  Write Prolog clauses that define the predicate
    sorted(L), which is true if and only if list
    L is sorted in ascending order.<br>

2.  Write a Prolog definition for the predicate perm(L,M),
    which is true if and only if L is a permutation of
    M.<br>

3.  Define sort(L,M) (M is a sorted version of
    L) using perm and sorted.<br>

4.  Run sort on longer and longer lists until you lose
    patience. What is the time complexity of your program?<br>

5.  Write a faster sorting algorithm, such as insertion sort or
    quicksort, in Prolog.<br>


---


##### Bài tập 9.21
This exercise looks at the recursive
application of rewrite rules, using logic programming. A rewrite rule
(or <b>demodulator</b> in terminology) is an
equation with a specified direction. For example, the rewrite rule
$x+0 \rightarrow x$ suggests replacing any expression that matches $x+0$
with the expression $x$. Rewrite rules are a key component of equational
reasoning systems. Use the predicate rewrite(X,Y) to
represent rewrite rules. For example, the earlier rewrite rule is
written as rewrite(X+0,X). Some terms are
<i>primitive</i> and cannot be further simplified; thus, we
write primitive(0) to say that 0 is a primitive term.<br>

1.  Write a definition of a predicate simplify(X,Y), that
    is true when Y is a simplified version of
    X—that is, when no further rewrite rules apply to any
    subexpression of Y.<br>

2.  Write a collection of rules for the simplification of expressions
    involving arithmetic operators, and apply your simplification
    algorithm to some sample expressions.<br>

3.  Write a collection of rewrite rules for symbolic differentiation,
    and use them along with your simplification rules to differentiate
    and simplify expressions involving arithmetic expressions,
    including exponentiation.<br>


---


##### Bài tập 9.22
Bài tập này xem xét việc cài đặt các search algorithm trong Prolog. Giả sử rằng `successor(X,Y)` đúng khi state `Y` là một successor của state `X`; và `goal(X)` đúng khi `X` là một goal state. Hãy viết định nghĩa cho `solve(X,P)`, có nghĩa là `P` là một path (danh sách các state) bắt đầu bằng `X`, kết thúc ở một goal state, và bao gồm một chuỗi các bước đi hợp lệ được định nghĩa bởi `successor`. Bạn sẽ thấy rằng depth-first search là cách dễ nhất để làm điều này. Sẽ dễ dàng thế nào nếu thêm heuristic search control?

---


##### Bài tập 9.23
Giả sử một knowledge base chỉ chứa các First-order Horn clause sau đây:<br>

$$
Ancestor(Mother(x),x)
$$
$$
Ancestor(x,y) \land Ancestor(y,z) \implies Ancestor(x,z)
$$

Xét một forward chaining algorithm mà tại vòng lặp thứ $j$, sẽ dừng lại nếu KB chứa một câu unifies với query, ngược lại sẽ thêm vào KB mọi atomic sentence có thể được suy luận từ các câu đã có trong KB sau vòng lặp thứ $j-1$.<br>

1.  Với mỗi query sau đây, hãy cho biết thuật toán sẽ (1) đưa ra câu trả lời (nếu có, hãy viết ra câu trả lời đó); hoặc (2) kết thúc mà không có câu trả lời; hoặc (3) không bao giờ kết thúc.<br>

    1.  $Ancestor(Mother(y),John)$<br>

    2.  $Ancestor(Mother(Mother(y)),John)$<br>

    3.  $Ancestor(Mother(Mother(Mother(y))),Mother(y))$<br>

    4.  $Ancestor(Mother(John),Mother(Mother(John)))$<br>

2.  Liệu một resolution algorithm có thể chứng minh câu $\lnot Ancestor(John,John)$ từ knowledge base ban đầu hay không? Giải thích tại sao có, hoặc tại sao không.<br>

3.  Giả sử chúng ta thêm khẳng định rằng $\lnot(Mother(x){{\,=\,}}x)$ và bổ sung vào resolution algorithm các inference rule cho phép toán bằng nhau. Khi đó câu trả lời cho phần (b) là gì?<br>


---


##### Bài tập 9.24
Cho $\cal L$ là ngôn ngữ bậc nhất với một vị từ duy nhất
$S(p,q)$, có nghĩa là “$p$ cạo râu cho $q$.” Giả sử miền xét là tập hợp những con người.<br>

1.  Xét câu “Tồn tại một người $P$ cạo râu cho tất cả những ai không tự cạo râu cho chính mình, và chỉ những người không tự cạo râu cho chính mình.” Hãy biểu diễn câu này trong $\cal L$.<br>

2.  Chuyển câu ở phần (a) về dạng clausal form.<br>

3.  Xây dựng một chứng minh bằng resolution để chỉ ra rằng các clause trong phần (b) là mâu thuẫn một cách hiển nhiên. (Lưu ý: bạn không cần thêm bất kỳ axiom nào khác.)


---


##### Bài tập 9.25
Làm thế nào có thể sử dụng resolution để chứng minh rằng một sentence là valid?
Unsatisfiable?


---


##### Bài tập 9.26
Construct an example of two clauses that can be resolved together in two
different ways giving two different outcomes.


---


##### Bài tập 9.27
Từ câu “Ngựa là động vật,” suy ra “Đầu của một con ngựa là đầu của một con động vật.” Hãy chứng minh rằng inference này là valid bằng cách thực hiện các bước sau:<br>

1.  Translate giả thiết và kết luận sang ngôn ngữ của first-order logic. Sử dụng ba predicate: ${HeadOf}(h,x)$ (có nghĩa là “$h$ là đầu của $x$”), ${Horse}(x)$, và ${Animal}(x)$.<br>

2.  Negate kết luận, và chuyển đổi giả thiết cùng với kết luận đã bị negate thành conjunctive normal form.<br>

3.  Sử dụng resolution để chỉ ra rằng kết luận suy ra từ giả thiết.<br>


---


##### Bài tập 9.28
Từ mệnh đề “Sheep are animals,” suy ra được “The head of a sheep is the head of an animal.” Hãy chứng minh rằng phép suy luận này là hợp lệ bằng cách thực hiện các bước sau:<br>

1.  Translate premise và conclusion sang ngôn ngữ của first-order logic. Sử dụng ba predicate: ${HeadOf}(h,x)$ (có nghĩa là “$h$ là head của $x$”), ${Sheep}(x)$, và ${Animal}(x)$.<br>

2.  Negate conclusion, sau đó chuyển đổi premise và negated conclusion về dạng conjunctive normal form.<br>

3.  Sử dụng resolution để chứng minh rằng conclusion suy ra được từ premise.


---


##### Bài tập 9.29
Here are two sentences in the language of
first-order logic:<br>

-   <b>(A)</b>
    ${\forall\,x\;\;} {\exists\,y\;\;} ( x \geq y )$

-   <b>(B)</b>
    ${\exists\,y\;\;} {\forall\,x\;\;} ( x \geq y )$

1.  Assume that the variables range over all the natural numbers
    $0,1,2,\ldots, \infty$ and that the “$\geq$” predicate means “is
    greater than or equal to.” Under this interpretation, translate (A)
    and (B) into English.<br>

2.  Is (A) true under this interpretation?<br>

3.  Is (B) true under this interpretation?<br>

4.  Does (A) logically entail (B)?<br>

5.  Does (B) logically entail (A)?<br>

6.  Using resolution, try to prove that (A) follows from (B). Do this
    even if you think that (B) does not logically entail (A); continue
    until the proof breaks down and you cannot proceed (if it does
    break down). Show the unifying substitution for each resolution
    step. If the proof fails, explain exactly where, how, and why it
    breaks down.<br>

7.  Now try to prove that (B) follows from (A).<br>


---


##### Bài tập 9.30
Resolution có thể tạo ra các nonconstructive proof cho các query có chứa variables, vì vậy chúng ta phải giới thiệu các cơ chế đặc biệt để trích xuất definite answers. Hãy giải thích tại sao vấn đề này không phát sinh với các knowledge base chỉ chứa các definite clause.


---


##### Bài tập 9.31
Chúng ta đã nói trong chương này rằng resolution không thể được dùng để sinh ra tất cả các logical consequence của một tập hợp các câu. Liệu có thuật toán nào làm được điều này không?


---

<!-- tabs:end -->
