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



#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter10/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Logic**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/logic.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/logic.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/logic.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 10.1

Xem xét một robot có hoạt động được mô tả bởi các toán tử PDDL sau:<br>

$$
Op({Go(x,y)},{At(Robot,x)},{\lnot At(Robot,x) \land At(Robot,y)})
$$
$$
Op({Pick(o)},{At(Robot,x)\land At(o,x)},{\lnot At(o,x) \land Holding(o)})
$$
$$
Op({Drop(o)},{At(Robot,x)\land Holding(o)},{At(o,x) \land \lnot Holding(o)}
$$

1.  Các toán tử cho phép robot giữ nhiều hơn một vật thể. Hãy chỉ ra cách
    sửa đổi chúng với một predicate $EmptyHand$ cho một robot chỉ có thể
    giữ một vật thể.<br>

2.  Giả sử đây là các hành động duy nhất trong thế giới, hãy viết một
    successor-state axiom cho $EmptyHand$.<br>


---

##### Bài tập 10.2

Mô tả sự khác biệt và tương đồng giữa problem solving và
planning.<br>


---

##### Bài tập 10.3

Cho các lược đồ hành động và trạng thái ban đầu
từ Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/airport-pddl-algorithm.png">airport-pddl-algorithm</a>, tất cả các
thể hiện cụ thể áp dụng được của ${Fly}(p,{from},{to})$ trong
trạng thái được mô tả bởi<br>

$$
At(P_1,JFK) \land At(P_2,SFO) \land Plane(P_1) \land Plane(P_2) \land Airport(JFK) \land Airport(SFO)?
$$


---

##### Bài tập 10.4

Bài toán khỉ và chuối đối mặt với một con khỉ trong phòng thí nghiệm với một số quả chuối treo ngoài tầm với từ trần nhà. Một chiếc hộp có sẵn sẽ cho phép con khỉ đạt được quả chuối nếu nó leo lên đó.
Ban đầu, con khỉ ở $A$, quả chuối ở $B$, và chiếc hộp ở $C$.
Con khỉ và chiếc hộp có chiều cao ${Low}$, nhưng nếu con khỉ leo lên hộp, nó sẽ có chiều cao ${High}$, giống như quả chuối. Các hành động có sẵn cho con khỉ bao gồm ${Go}$ từ nơi này đến nơi khác, ${Push}$ một vật thể từ nơi này đến nơi khác, ${ClimbUp}$ lên hoặc ${ClimbDown}$ xuống khỏi một vật thể, và ${Grasp}$ hoặc ${Ungrasp}$ một vật thể. Kết quả của ${Grasp}$ là con khỉ giữ vật thể nếu con khỉ và vật thể ở cùng một vị trí với cùng chiều cao.<br>

1.  Viết mô tả trạng thái ban đầu.<br>

2.  Viết sáu lược đồ hành động.<br>

3.  Giả sử con khỉ muốn đánh lừa các nhà khoa học, những người đang đi uống trà, bằng cách lấy quả chuối, nhưng để chiếc hộp ở nguyên vị trí ban đầu.
    Viết điều này dưới dạng một mục tiêu chung (tức là, không giả định rằng chiếc hộp nhất thiết phải ở $C$) bằng ngôn ngữ của situation calculus. Mục tiêu này có thể được giải quyết bởi một classical planning system không?<br>

4.  Lược đồ của bạn để đẩy có thể không chính xác, bởi vì nếu vật thể quá nặng, vị trí của nó sẽ không thay đổi khi lược đồ ${Push}$ được áp dụng. Sửa đổi lược đồ hành động của bạn để tính đến các vật thể nặng.<br>


---

###### Bài tập 10.5

Trình lập kế hoạch {Strips} ban đầu được thiết kế để điều khiển robot Shakey.
Hình <a class="insideExercisesFigRef" href="#shakey-figure">shakey-figure</a> cho thấy một phiên bản thế giới của Shakey bao gồm bốn phòng xếp dọc theo một hành lang, mỗi phòng có một cánh cửa và một công tắc đèn. Các hành động trong thế giới của Shakey bao gồm di chuyển từ nơi này sang nơi khác, đẩy các vật thể có thể di chuyển (như hộp), leo lên và xuống khỏi các vật thể cứng (như hộp), và bật tắt công tắc đèn. Bản thân robot không thể leo lên hộp hoặc bật công tắc, nhưng trình lập kế hoạch có khả năng tìm và in ra các kế hoạch vượt quá khả năng của robot. Sáu hành động của Shakey như sau:<br>

-   ${Go}(x,y,r)$, yêu cầu Shakey phải ${At}$ $x$ và $x$ và $y$ là các vị trí ${In}$ cùng một phòng $r$. Theo quy ước, một cánh cửa giữa hai phòng thuộc về cả hai phòng đó.<br>

-   Đẩy một hộp $b$ từ vị trí $x$ đến vị trí $y$ trong cùng một phòng: ${Push}(b,x,y,r)$. Bạn sẽ cần predicate ${Box}$ và các hằng số cho các hộp.<br>

-   Leo lên một hộp từ vị trí $x$: ${ClimbUp}(x, b)$; leo xuống khỏi một hộp đến vị trí $x$: ${ClimbDown}(b, x)$. Chúng ta sẽ cần predicate ${On}$ và hằng số ${Floor}$.<br>

-   Bật hoặc tắt một công tắc đèn: ${TurnOn}(s,b)$;
    ${TurnOff}(s,b)$. Để bật hoặc tắt đèn, Shakey phải ở trên đỉnh một chiếc hộp tại vị trí của công tắc đèn.<br>

Viết các câu PDDL cho sáu hành động của Shakey và trạng thái ban đầu từ
Xây dựng một kế hoạch để Shakey lấy ${Box}{}_2$ vào ${Room}{}_2$.<br>

  <figure>
    <img src="https://aimacode.github.io/aima-exercises/figures/shakey2.svg" alt="shakey-figure" id="shakey-figure" style="width:100%">
    <figcaption><center><b>Thế giới của Shakey. Shakey có thể di chuyển giữa các mốc trong một phòng, có thể đi qua cửa giữa các phòng, có thể leo lên các vật thể có thể leo và đẩy các vật thể có thể đẩy, và có thể bật tắt công tắc đèn.</b></center></figcaption>
  </figure>


---

##### Bài tập 10.6

Một máy Turing hữu hạn có một băng một chiều hữu hạn gồm các ô, mỗi ô chứa một trong một số hữu hạn các ký hiệu. Một ô có một đầu đọc và ghi phía trên nó. Có một tập hợp hữu hạn các trạng thái mà máy có thể ở, một trong số đó là trạng thái chấp nhận. Tại mỗi bước thời gian, tùy thuộc vào ký hiệu trên ô dưới đầu đọc và trạng thái hiện tại của máy, có một tập hợp các hành động mà chúng ta có thể chọn. Mỗi hành động bao gồm việc ghi một ký hiệu vào ô dưới đầu đọc, chuyển máy sang một trạng thái, và tùy chọn di chuyển đầu đọc sang trái hoặc sang phải. Ánh xạ xác định hành động nào được phép là chương trình của máy Turing. Mục tiêu của bạn là điều khiển máy sang trạng thái chấp nhận.<br>
<br>
Biểu diễn bài toán chấp nhận máy Turing như một bài toán planning.
Nếu bạn có thể làm điều này, nó chứng tỏ rằng việc xác định xem một bài toán planning có giải pháp hay không ít nhất cũng khó như bài toán chấp nhận Turing, vốn là PSPACE-hard.<br>


---

##### Bài tập 10.7

Giải thích tại sao việc loại bỏ các hiệu ứng phủ định khỏi
mọi lược đồ hành động lại dẫn đến một relaxed problem, với điều kiện là các
preconditions và goals chỉ chứa các literal dương.


---

##### Bài tập 10.8

Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sussman-anamoly-figure.png">sussman-anomaly-figure</a>
(trang <a class="pageRef" title="" href="#">sussman-anomaly-figure</a>) cho thấy một bài toán blocks-world được gọi là {Sussman anomaly}.
Bài toán này được coi là bất thường vì các trình lập kế hoạch không xen kẽ của đầu những năm 1970 không thể giải quyết nó. Viết định nghĩa của bài toán và giải nó, bằng tay hoặc bằng một chương trình planning. Một
trình lập kế hoạch không xen kẽ là một trình lập kế hoạch, khi được cho hai mục tiêu phụ
$G_{1}$ và $G_{2}$, sẽ tạo ra một kế hoạch cho $G_{1}$ nối với một kế hoạch cho $G_{2}$, hoặc ngược lại. Một trình lập kế hoạch không xen kẽ có thể giải quyết bài toán này không? Như thế nào, hoặc tại sao không?<br>


---

##### Bài tập 10.9

Chứng minh rằng backward search với các bài toán PDDL là hoàn chỉnh.


---

##### Bài tập 10.10

Xây dựng các cấp độ 0, 1 và 2 của planning graph cho bài toán trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/airport-pddl-algorithm.png">airport-pddl-algorithm</a>


---

##### Bài tập 10.11

Chứng minh các khẳng định sau về
planning graphs:<br>

1.  Một literal không xuất hiện ở cấp độ cuối cùng của đồ thị
    không thể đạt được.<br>

2.  Chi phí cấp độ của một literal trong đồ thị tuần tự không lớn hơn
    chi phí thực tế của một kế hoạch tối ưu để đạt được nó.<br>


---

##### Bài tập 10.12

Chúng ta đã thấy rằng planning graphs chỉ có thể xử lý các hành động mệnh đề. Điều gì sẽ xảy ra nếu chúng ta muốn sử dụng planning graphs cho một bài toán có biến trong goal, chẳng hạn như ${At}(P_{1}, x) \land {At}(P_{2}, x)$, trong đó $x$ được giả định được ràng buộc bởi một lượng từ tồn tại chạy trên một miền hữu hạn các vị trí?
Làm thế nào bạn có thể mã hóa một bài toán như vậy để hoạt động với planning graphs?


---

##### Bài tập 10.13

Heuristic mức tập hợp (xem trang <a class="pageRef" title="" href="#">set-level-page</a>) sử dụng một planning graph để ước tính chi phí đạt được một conjunctive goal từ trạng thái hiện tại. Bài toán relaxed nào mà heuristic mức tập hợp là giải pháp cho nó?


---

##### Bài tập 10.14

Xem xét định nghĩa về <b>bidirectional search</b> trong Chương <a class="chapterRef" title="" href="{{site.baseurl}}/search-exercises/">search-chapter</a>.<br>

1.  Bidirectional state-space search có phải là một ý tưởng hay cho planning không?<br>

2.  Còn bidirectional search trong không gian của các partial-order plans thì sao?<br>

3.  Thiết kế một phiên bản của partial-order planning trong đó một hành động có thể được thêm vào một kế hoạch nếu các preconditions của nó có thể đạt được bởi các hiệu ứng của các hành động đã có trong kế hoạch. Giải thích cách xử lý các xung đột và ràng buộc thứ tự. Thuật toán có về cơ bản giống với forward state-space search không?<br>


---

##### Bài tập 10.15

Chúng ta đã đối chiếu các bộ tìm kiếm forward và backward state-space với các trình lập kế hoạch partial-order, nói rằng cái sau là một bộ tìm kiếm plan-space.
Giải thích làm thế nào các bộ tìm kiếm forward và backward state-space cũng có thể được coi là bộ tìm kiếm plan-space, và cho biết các toán tử tinh chỉnh kế hoạch là gì.<br>


---

##### Bài tập 10.16

Cho đến nay, chúng ta đã giả định rằng các
kế hoạch mà chúng ta tạo ra luôn đảm bảo rằng các preconditions của hành động được thỏa mãn. Bây giờ chúng ta hãy điều tra xem các propositional successor-state axioms như ${HaveArrow}^{t+1} {\;\;{\Leftrightarrow}\;\;}{}$
$({HaveArrow}^t \land \lnot {Shoot}^t)$ nói gì về các hành động mà preconditions của chúng không được thỏa mãn.<br>

1.  Chứng minh rằng các axioms dự đoán rằng không có gì xảy ra khi một hành động được thực thi trong một trạng thái mà các preconditions của nó không được thỏa mãn.<br>

2.  Xem xét một kế hoạch $p$ chứa các hành động cần thiết để đạt được một mục tiêu nhưng cũng bao gồm các hành động bất hợp pháp. Có phải là
$$
initial state \land successor-state axioms \land
p {\models} goal ?
$$

3.  Với first-order successor-state axioms trong situation calculus, có thể chứng minh rằng một kế hoạch chứa các hành động bất hợp pháp sẽ đạt được mục tiêu không?<br>


---

##### Bài tập 10.17

Xem xét cách dịch một tập hợp các lược đồ hành động
thành các successor-state axioms của situation calculus.<br>

1.  Xem xét lược đồ cho ${Fly}(p,{from},{to})$. Viết một định nghĩa logic cho predicate
    ${Poss}({Fly}(p,{from},{to}),s)$, là đúng nếu các preconditions cho ${Fly}(p,{from},{to})$ được thỏa mãn trong situation $s$.<br>

2.  Tiếp theo, giả sử ${Fly}(p,{from},{to})$ là lược đồ hành động duy nhất có sẵn cho agent, hãy viết một successor-state axiom cho ${At}(p,x,s)$ nắm bắt cùng thông tin như lược đồ hành động.<br>

3.  Bây giờ giả sử có một phương thức di chuyển bổ sung:
    ${Teleport}(p,{from},{to})$. Nó có precondition bổ sung $\lnot {Warped}(p)$ và hiệu ứng bổ sung ${Warped}(p)$. Giải thích cách cơ sở tri thức situation calculus phải được sửa đổi.<br>

4.  Cuối cùng, phát triển một quy trình chung và được chỉ định chính xác để thực hiện việc dịch từ một tập hợp các lược đồ hành động sang một tập hợp các successor-state axioms.<br>


---

##### Bài tập 10.18

Trong thuật toán $SATPlan$ trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/satplan-agent-algorithm.png">satplan-agent-algorithm</a> (trang <a class="pageRef" title="" href="#">satplan-agent-algorithm</a>,
mỗi lần gọi thuật toán satisfiability sẽ khẳng định một goal $g^T$, trong đó $T$ chạy từ 0 đến $T_{max}$. Thay vào đó, giả sử thuật toán satisfiability chỉ được gọi một lần, với goal
$g^0 \vee g^1 \vee \cdots \vee g^{T_{max}}$. <br>

1.  Điều này có luôn trả về một kế hoạch nếu một kế hoạch tồn tại với độ dài nhỏ hơn hoặc bằng $T_{max}$ không?<br>

2.  Cách tiếp cận này có đưa ra bất kỳ "giải pháp" giả nào mới không?<br>

3.  Thảo luận về cách bạn có thể sửa đổi một thuật toán satisfiability như $WalkSAT$ để nó tìm các giải pháp ngắn (nếu có) khi được cung cấp một goal phân biệt dạng này.<br>


---

<!-- tabs:end -->
