# Chapter 07 Logical Agents

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_07/chapter_07_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_07_Logical%20Agents.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter07_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter07/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
<div id="quiz-container" data-chapter="07"></div>

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/KB-Agent.md" target="_blank">KB-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/TT-Entails.md" target="_blank">TT-ENTAILS</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/PL-Resolution.md" target="_blank">PL-RESOLUTION</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/PL-FC-Entails.md" target="_blank">PL-FC-ENTAILS?</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/DPLL-Satisfiable.md" target="_blank">DPLL-SATISFIABLE?</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/WalkSAT.md" target="_blank">WALKSAT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Hybrid-Wumpus-Agent.md" target="_blank">HYBRID-WUMPUS-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/SATPlan.md" target="_blank">SATPLAN</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Logic**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/logic.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/logic.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/logic.ipynb" download>Tải .ipynb</a>
- **Improving Sat Algorithms**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/improving_sat_algorithms.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/improving_sat_algorithms.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/improving_sat_algorithms.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 7.1

Giả sử agent đã tiến đến điểm được hiển thị trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/wumpus-seq35-figure.png">wumpus-seq35-figure</a>(a), trang <a class="pageRef" title="" href="#">wumpus-seq35-figure</a>,
sau khi nhận thức được không có gì ở [1,1], có một luồng gió ở [2,1], và một mùi hôi
ở [1,2], và bây giờ đang quan tâm đến nội dung của [1,3], [2,2],
và [3,1]. Mỗi vị trí này có thể chứa một cái hố, và tối đa một vị trí có thể
chứa một con wumpus. Theo ví dụ của
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/wumpus-entailment-figure.png">wumpus-entailment-figure</a>, hãy xây dựng tập hợp các
thế giới khả dĩ. (Bạn sẽ tìm thấy 32 thế giới.) Đánh dấu các thế giới mà
KB đúng và các thế giới mà mỗi câu sau đây đúng:
<br>

$\alpha_2$ = “Không có hố nào ở [2,2].”<br>

$\alpha_3$ = “Có một con wumpus ở [1,3].”<br>

Do đó, hãy chỉ ra rằng ${KB} {\models}\alpha_2$ và
${KB} {\models}\alpha_3$.


---

##### Bài tập 7.2

(Chuyển thể từ <a class="paperRef" title="" href="">Barwise+Etchemendy:1993</a> .) Với những thông tin sau, bạn có thể chứng minh rằng kỳ lân là
huyền thoại không? Còn về phép thuật? Có sừng?<br>

Lưu ý: Nếu kỳ lân là huyền thoại, thì nó bất tử, nhưng nếu nó không
huyền thoại, thì nó là một loài động vật có vú phàm trần. Nếu kỳ lân hoặc
bất tử hoặc là động vật có vú, thì nó có sừng. Kỳ lân là phép thuật nếu nó
có sừng.<br>


---

##### Bài tập 7.3

Xem xét bài toán xác định xem một câu logic mệnh đề có đúng trong một mô hình cho trước hay không.<br>

1.  Viết một thuật toán đệ quy PL-True?$ (s, m )$ trả về ${true}$ nếu và
    chỉ nếu câu $s$ đúng trong mô hình $m$ (trong đó $m$ gán một giá trị chân lý
    cho mọi ký hiệu trong $s$). Thuật toán nên chạy trong thời gian tuyến tính theo kích thước của câu. (Hoặc, sử dụng một phiên bản của hàm này từ kho mã trực tuyến.)<br>

2.  Đưa ra ba ví dụ về các câu có thể được xác định là đúng
    hoặc sai trong một mô hình <i>chưa hoàn chỉnh</i> không chỉ định giá trị chân lý
    cho một số ký hiệu.<br>

3.  Chứng tỏ rằng giá trị chân lý (nếu có) của một câu trong mô hình chưa hoàn chỉnh
    không thể được xác định một cách hiệu quả nói chung.<br>

4.  Sửa đổi thuật toán của bạn để nó có thể đôi khi phán đoán chân lý từ các mô hình chưa hoàn chỉnh, đồng thời giữ nguyên cấu trúc đệ quy và thời gian chạy tuyến tính. Đưa ra ba ví dụ về các câu mà chân lý của chúng trong mô hình chưa hoàn chỉnh <i>không</i> được thuật toán của bạn phát hiện.<br>

5.  Điều tra xem thuật toán đã sửa đổi có làm cho $TT-Entails?$ hiệu quả hơn không.


---

##### Bài tập 7.4

Câu nào sau đây là đúng?<br>

1.  ${False} \models {True}$.<br>

2.  ${True} \models {False}$.<br>

3.  $(A\land B)  \models (A{\;\;{\Leftrightarrow}\;\;}B)$.<br>

4.  $A{\;\;{\Leftrightarrow}\;\;}B \models A \lor B$.<br>

5.  $A{\;\;{\Leftrightarrow}\;\;}B \models \lnot A \lor B$.<br>

6.  $(A\land B){\:\;{\Rightarrow}\:\;}C \models (A{\:\;{\Rightarrow}\:\;}C)\lor(B{\:\;{\Rightarrow}\:\;}C)$.<br>

7.  $(C\lor (\lnot A \land \lnot B)) \equiv ((A{\:\;{\Rightarrow}\:\;}C) \land (B {\:\;{\Rightarrow}\:\;}C))$.<br>

8.  $(A\lor B) \land (\lnot C\lor\lnot D\lor E) \models (A\lor B)$.<br>

9.  $(A\lor B) \land (\lnot C\lor\lnot D\lor E) \models (A\lor B) \land (\lnot D\lor E)$.<br>

10. $(A\lor B) \land \lnot(A {\:\;{\Rightarrow}\:\;}B)$ là thỏa mãn.<br>

11. $(A{\;\;{\Leftrightarrow}\;\;}B) \land (\lnot A \lor B)$
    là thỏa mãn.<br>

12. $(A{\;\;{\Leftrightarrow}\;\;}B) {\;\;{\Leftrightarrow}\;\;}C$ có
    cùng số lượng mô hình với $(A{\;\;{\Leftrightarrow}\;\;}B)$ cho
    bất kỳ tập hợp các ký hiệu mệnh đề cố định nào bao gồm $A$, $B$, $C$.<br>


---

##### Bài tập 7.5

Câu nào sau đây là đúng?<br>

1.  ${False} \models {True}$.<br>

2.  ${True} \models {False}$.<br>

3.  $(A\land B)  \models (A{\;\;{\Leftrightarrow}\;\;}B)$.<br>

4.  $A{\;\;{\Leftrightarrow}\;\;}B \models A \lor B$.<br>

5.  $A{\;\;{\Leftrightarrow}\;\;}B \models \lnot A \lor B$.<br>

6.  $(A\lor B) \land (\lnot C\lor\lnot D\lor E) \models (A\lor B\lor C) \land (B\land C\land D{\:\;{\Rightarrow}\:\;}E)$.<br>

7.  $(A\lor B) \land (\lnot C\lor\lnot D\lor E) \models (A\lor B) \land (\lnot D\lor E)$.<br>

8.  $(A\lor B) \land \lnot(A {\:\;{\Rightarrow}\:\;}B)$ là thỏa mãn.<br>

9.  $(A\land B){\:\;{\Rightarrow}\:\;}C \models (A{\:\;{\Rightarrow}\:\;}C)\lor(B{\:\;{\Rightarrow}\:\;}C)$.<br>

10. $(C\lor (\lnot A \land \lnot B)) \equiv ((A{\:\;{\Rightarrow}\:\;}C) \land (B {\:\;{\Rightarrow}\:\;}C))$.<br>

11. $(A{\;\;{\Leftrightarrow}\;\;}B) \land (\lnot A \lor B)$
    là thỏa mãn.<br>

12. $(A{\;\;{\Leftrightarrow}\;\;}B) {\;\;{\Leftrightarrow}\;\;}C$ có
    cùng số lượng mô hình với $(A{\;\;{\Leftrightarrow}\;\;}B)$ cho
    bất kỳ tập hợp các ký hiệu mệnh đề cố định nào bao gồm $A$, $B$, $C$.<br>


---

##### Bài tập 7.6

Chứng minh mỗi khẳng định sau đây:<br>

1.  $\alpha$ là hợp lệ nếu và chỉ nếu ${True}{\models}\alpha$.<br>

2.  Với mọi $\alpha$, ${False}{\models}\alpha$.<br>

3.  $\alpha{\models}\beta$ nếu và chỉ nếu câu
    $(\alpha {\:\;{\Rightarrow}\:\;}\beta)$ là hợp lệ.<br>

4.  $\alpha \equiv \beta$ nếu và chỉ nếu câu
    $(\alpha{\;\;{\Leftrightarrow}\;\;}\beta)$ là hợp lệ.<br>

5.  $\alpha{\models}\beta$ nếu và chỉ nếu câu
    $(\alpha \land \lnot \beta)$ là không thỏa mãn.


---

##### Bài tập 7.7

Chứng minh, hoặc tìm phản ví dụ cho, mỗi khẳng định sau đây:<br>

1.  Nếu $\alpha\models\gamma$ hoặc $\beta\models\gamma$ (hoặc cả hai) thì
    $(\alpha\land \beta)\models\gamma$<br>

2.  Nếu $(\alpha\land \beta)\models\gamma$ thì $\alpha\models\gamma$ hoặc
    $\beta\models\gamma$ (hoặc cả hai).<br>

3.  Nếu $\alpha\models (\beta \lor \gamma)$ thì $\alpha \models \beta$
    hoặc $\alpha \models \gamma$ (hoặc cả hai).<br>


---

##### Bài tập 7.8

Chứng minh, hoặc tìm phản ví dụ cho, mỗi khẳng định sau đây:<br>

1.  Nếu $\alpha\models\gamma$ hoặc $\beta\models\gamma$ (hoặc cả hai) thì
    $(\alpha\land \beta)\models\gamma$<br>

2.  Nếu $\alpha\models (\beta \land \gamma)$ thì $\alpha \models \beta$
    và $\alpha \models \gamma$.<br>

3.  Nếu $\alpha\models (\beta \lor \gamma)$ thì $\alpha \models \beta$
    hoặc $\alpha \models \gamma$ (hoặc cả hai).<br>


---

##### Bài tập 7.9

Xem xét một từ vựng chỉ có bốn mệnh đề, $A$, $B$, $C$, và
$D$. Có bao nhiêu mô hình cho các câu sau đây?<br>

1.  $B\lor C$.<br>

2.  $\lnot A\lor \lnot B \lor \lnot C \lor \lnot D$.<br>

3.  $(A{\:\;{\Rightarrow}\:\;}B) \land A \land \lnot B \land C \land D$.<br>


---

##### Bài tập 7.10

Chúng ta đã định nghĩa bốn phép toán logic nhị phân.<br>

1.  Có phép toán nào khác có thể hữu ích không?<br>

2.  Có bao nhiêu phép toán nhị phân có thể tồn tại?<br>

3.  Tại sao một số trong số chúng không hữu ích lắm?<br>


---

##### Bài tập 7.11

Sử dụng phương pháp bạn chọn, hãy xác minh
mỗi phép tương đương trong
Bảng <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/logical-equivalence-table.png">logical-equivalence-table</a> (trang <a class="pageRef" title="" href="#">logical-equivalence-table</a>).


---

##### Bài tập 7.12

Quyết định xem mỗi câu sau đây
là hợp lệ, không thỏa mãn, hay không phải cả hai. Xác minh các quyết định của bạn bằng bảng chân lý hoặc các quy tắc tương đương của
Bảng <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/logical-equivalence-table.png">logical-equivalence-table</a> (trang <a class="pageRef" title="" href="#">logical-equivalence-table</a>).

1.  ${Smoke} {\:\;{\Rightarrow}\:\;}{Smoke}$<br>

2.  ${Smoke} {\:\;{\Rightarrow}\:\;}{Fire}$<br>

3.  $({Smoke} {\:\;{\Rightarrow}\:\;}{Fire}) {\:\;{\Rightarrow}\:\;}(\lnot {Smoke} {\:\;{\Rightarrow}\:\;}\lnot {Fire})$<br>

4.  ${Smoke} \lor {Fire} \lor \lnot {Fire}$<br>

5.  $(( {Smoke} \land {Heat}) {\:\;{\Rightarrow}\:\;}{Fire}) {\;\;{\Leftrightarrow}\;\;}(({Smoke} {\:\;{\Rightarrow}\:\;}{Fire}) \lor ({Heat} {\:\;{\Rightarrow}\:\;}{Fire}))$<br>

6.  $({Smoke} {\:\;{\Rightarrow}\:\;}{Fire}) {\:\;{\Rightarrow}\:\;}(({Smoke} \land {Heat}) {\:\;{\Rightarrow}\:\;}{Fire}) $<br>

7.  ${Big} \lor {Dumb} \lor ({Big} {\:\;{\Rightarrow}\:\;}{Dumb})$<br>


---

##### Bài tập 7.13

Quyết định xem mỗi câu sau đây
là hợp lệ, không thỏa mãn, hay không phải cả hai. Xác minh các quyết định của bạn bằng bảng chân lý hoặc các quy tắc tương đương của
Bảng <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/logical-equivalence-table.png">logical-equivalence-table</a> (trang <a class="pageRef" title="" href="#">logical-equivalence-table</a>).<br>

1.  ${Smoke} {\:\;{\Rightarrow}\:\;}{Smoke}$<br>

2.  ${Smoke} {\:\;{\Rightarrow}\:\;}{Fire}$<br>

3.  $({Smoke} {\:\;{\Rightarrow}\:\;}{Fire}) {\:\;{\Rightarrow}\:\;}(\lnot {Smoke} {\:\;{\Rightarrow}\:\;}\lnot {Fire})$<br>

4.  ${Smoke} \lor {Fire} \lor \lnot {Fire}$<br>

5.  $(( {Smoke} \land {Heat}) {\:\;{\Rightarrow}\:\;}{Fire}) {\;\;{\Leftrightarrow}\;\;}(({Smoke} {\:\;{\Rightarrow}\:\;}{Fire}) \lor ({Heat} {\:\;{\Rightarrow}\:\;}{Fire}))$<br>

6.  ${Big} \lor {Dumb} \lor ({Big} {\:\;{\Rightarrow}\:\;}{Dumb})$<br>

7.  $({Big} \land {Dumb}) \lor \lnot {Dumb}$<br>


---

##### Bài tập 7.14

Bất kỳ câu logic mệnh đề nào cũng tương đương logic với khẳng định rằng mỗi thế giới khả dĩ mà nó sai đều không xảy ra. Từ quan sát này, hãy chứng minh rằng bất kỳ câu nào cũng có thể được viết dưới dạng CNF.


---

##### Bài tập 7.15

Sử dụng phương pháp resolution để chứng minh câu $\lnot A \land \lnot B$ từ các mệnh đề trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/knowledge-logic-exercises/ex_25/">convert-clausal-exercise</a>.


---

##### Bài tập 7.16

Bài tập này xem xét mối quan hệ giữa
các mệnh đề và các câu kéo theo.<br>

1.  Chứng minh rằng mệnh đề $(\lnot P_1 \lor \cdots \lor \lnot P_m \lor Q)$
    tương đương logic với câu kéo theo
    $(P_1 \land \cdots \land P_m) {\;{\Rightarrow}\;}Q$.<br>

2.  Chứng minh rằng mọi mệnh đề (bất kể số lượng
    mệnh đề dương) có thể được viết dưới dạng
    $(P_1 \land \cdots \land P_m) {\;{\Rightarrow}\;}(Q_1 \lor \cdots \lor Q_n)$,
    trong đó các $P$ và $Q$ là các ký hiệu mệnh đề. Một cơ sở tri thức bao gồm các câu như vậy được gọi là dạng chuẩn kéo theo hoặc <b>dạng Kowalski</b> <a class="paperRef" title="" href="">Kowalski:1979</a>.<br>

3.  Viết quy tắc resolution đầy đủ cho các câu ở dạng chuẩn kéo theo.<br>


---

##### Bài tập 7.17

Theo một số nhà bình luận chính trị, một người cấp tiến ($R$) có thể được bầu ($E$) nếu anh ta/cô ta là bảo thủ ($C$), nhưng nếu không thì không thể được bầu.<br>

1.  Câu nào sau đây là biểu diễn đúng của khẳng định này?<br>

    1.  $(R\land E)\iff C$<br>

    2.  $R{\:\;{\Rightarrow}\:\;}(E\iff C)$<br>

    3.  $R{\:\;{\Rightarrow}\:\;}((C{\:\;{\Rightarrow}\:\;}E) \lor \lnot E)$<br>

2.  Câu nào trong số các câu ở (a) có thể được biểu diễn dưới dạng Horn?<br>


---

##### Bài tập 7.18

Câu hỏi này xem xét việc biểu diễn các bài toán thỏa mãn (SAT) dưới dạng CSP.<br>

1.  Vẽ đồ thị ràng buộc tương ứng với bài toán SAT
    $$(\lnot X_1 \lor X_2) \land (\lnot X_2 \lor X_3) \land \ldots \land (\lnot X_{n-1} \lor X_n)$$
    cho trường hợp cụ thể $n{{\,=\,}}5$.<br>

2.  Có bao nhiêu nghiệm cho bài toán SAT tổng quát này theo hàm của $n$?<br>

3.  Giả sử chúng ta áp dụng {Backtracking-Search} (trang <a class="pageRef" title="" href="#">backtracking-search-algorithm</a>) để tìm <i>tất cả</i>
    nghiệm cho một SAT CSP thuộc loại được đưa ra ở (a). (Để tìm <i>tất cả</i> nghiệm cho một CSP, chúng ta chỉ cần sửa đổi thuật toán cơ bản
    sao cho nó tiếp tục tìm kiếm sau khi mỗi nghiệm được tìm thấy.)
    Giả sử các biến được sắp xếp $X_1,\ldots,X_n$ và ${false}$
    được sắp xếp trước ${true}$. Thuật toán sẽ mất bao lâu để kết thúc? (Viết biểu thức $O(\cdot)$ theo hàm của $n$.)<br>

4.  Chúng ta biết rằng các bài toán SAT ở dạng Horn có thể được giải trong thời gian tuyến tính
    bằng cách sử dụng forward chaining (unit propagation). Chúng ta cũng biết rằng mọi
    CSP nhị phân có cấu trúc cây với miền rời rạc, hữu hạn có thể được giải trong thời gian tuyến tính theo số lượng biến
    (Mục <a class="sectionRef" title="" href="#">csp-structure-section</a>). Hai sự thật này có liên quan với nhau không? Thảo luận.<br>


---

##### Bài tập 7.19

Câu hỏi này xem xét việc biểu diễn các bài toán thỏa mãn (SAT) dưới dạng CSP.<br>

1.  Vẽ đồ thị ràng buộc tương ứng với bài toán SAT
    $$(\lnot X_1 \lor X_2) \land (\lnot X_2 \lor X_3) \land \ldots \land (\lnot X_{n-1} \lor X_n)$$
    cho trường hợp cụ thể $n{{\,=\,}}4$.<br>

2.  Có bao nhiêu nghiệm cho bài toán SAT tổng quát này theo hàm của $n$?<br>

3.  Giả sử chúng ta áp dụng {Backtracking-Search} (trang <a class="pageRef" title="" href="#">backtracking-search-algorithm</a>) để tìm <i>tất cả</i>
    nghiệm cho một SAT CSP thuộc loại được đưa ra ở (a). (Để tìm <i>tất cả</i> nghiệm cho một CSP, chúng ta chỉ cần sửa đổi thuật toán cơ bản
    sao cho nó tiếp tục tìm kiếm sau khi mỗi nghiệm được tìm thấy.)
    Giả sử các biến được sắp xếp $X_1,\ldots,X_n$ và ${false}$
    được sắp xếp trước ${true}$. Thuật toán sẽ mất bao lâu để kết thúc? (Viết biểu thức $O(\cdot)$ theo hàm của $n$.)<br>

4.  Chúng ta biết rằng các bài toán SAT ở dạng Horn có thể được giải trong thời gian tuyến tính
    bằng cách sử dụng forward chaining (unit propagation). Chúng ta cũng biết rằng mọi
    CSP nhị phân có cấu trúc cây với miền rời rạc, hữu hạn có thể được giải trong thời gian tuyến tính theo số lượng biến
    (Mục <a class="sectionRef" title="" href="#">csp-structure-section</a>). Hai sự thật này có liên quan với nhau không? Thảo luận.<br>


---

##### Bài tập 7.20

Giải thích tại sao mọi mệnh đề logic 3-SAT không rỗng, tự nó, đều thỏa mãn. Chứng minh một cách chặt chẽ rằng mọi tập hợp gồm năm mệnh đề 3-SAT đều thỏa mãn, với điều kiện mỗi mệnh đề đề cập đến đúng ba biến phân biệt. Tập hợp nhỏ nhất gồm các mệnh đề như vậy mà không thỏa mãn là gì? Hãy xây dựng một tập hợp như vậy.


---

##### Bài tập 7.21

Một biểu thức <i>2-CNF</i> logic mệnh đề là một phép hội của các mệnh đề, mỗi mệnh đề chứa <i>chính xác 2</i> literal, ví dụ:
$$(A\lor B) \land (\lnot A \lor C) \land (\lnot B \lor D) \land (\lnot
  C \lor G) \land (\lnot D \lor G)\ .$$<br>

1.  Chứng minh bằng phương pháp resolution rằng câu trên kéo theo $G$.<br>

2.  Hai mệnh đề được gọi là <i>khác biệt về ngữ nghĩa</i> nếu chúng không tương đương logic. Có bao nhiêu mệnh đề 2-CNF khác biệt về ngữ nghĩa có thể được xây dựng từ $n$ ký hiệu mệnh đề?<br>

3.  Sử dụng câu trả lời của bạn cho (b), chứng minh rằng phương pháp resolution logic luôn kết thúc trong thời gian đa thức theo $n$ với một câu 2-CNF không chứa quá $n$ ký hiệu phân biệt.<br>

4.  Giải thích tại sao lập luận của bạn trong (c) không áp dụng cho 3-CNF.<br>


---

##### Bài tập 7.22

Chứng minh mỗi khẳng định sau đây:<br>

1.  Mọi cặp mệnh đề logic hoặc không có resolvent, hoặc tất cả các resolvent của chúng đều tương đương logic.<br>

2.  Không có mệnh đề nào, khi được resolve với chính nó, sẽ tạo ra (sau khi factoring) mệnh đề $(\lnot P \lor \lnot Q)$.<br>

3.  Nếu một mệnh đề logic $C$ có thể được resolve với một bản sao của chính nó, thì nó phải tương đương logic với $ True $.


---

##### Bài tập 7.23

Xem xét câu sau:<br>
$$[ ({Food} {\:\;{\Rightarrow}\:\;}{Party}) \lor ({Drinks} {\:\;{\Rightarrow}\:\;}{Party}) ] {\:\;{\Rightarrow}\:\;}[ ( {Food} \land {Drinks} )  {\:\;{\Rightarrow}\:\;}{Party}]\ .$$<br>

1.  Xác định, bằng cách liệt kê, liệu câu này có hợp lệ, thỏa mãn (nhưng không hợp lệ), hay không thỏa mãn.<br>

2.  Chuyển đổi vế trái và vế phải của phép kéo theo chính thành CNF, hiển thị từng bước, và giải thích cách các kết quả xác nhận câu trả lời của bạn cho (a).<br>

3.  Chứng minh câu trả lời của bạn cho (a) bằng phương pháp resolution.<br>


---

##### Bài tập 7.24

Một câu được gọi là ở dạng chuẩn tuyển (DNF) nếu nó là phép tuyển của các phép hội của các literal. Ví dụ, câu
$(A \land B \land \lnot C) \lor (\lnot A \land C) \lor (B \land \lnot C)$
là ở dạng DNF.<br>

1.  Bất kỳ câu logic mệnh đề nào cũng tương đương logic với khẳng định rằng một thế giới khả dĩ nào đó mà nó đúng thực sự xảy ra. Từ quan sát này, hãy chứng minh rằng bất kỳ câu nào cũng có thể được viết dưới dạng DNF.<br>

2.  Xây dựng một thuật toán chuyển đổi bất kỳ câu nào ở dạng logic mệnh đề sang DNF. (<i>Gợi ý</i>: Thuật toán tương tự như thuật toán chuyển đổi sang CNF được đưa ra trong Mục <a class="sectionRef" title="" href="#">pl-resolution-section</a>.)<br>

3.  Xây dựng một thuật toán đơn giản nhận đầu vào là một câu ở dạng DNF và trả về một phép gán thỏa mãn nếu có, hoặc báo cáo rằng không có phép gán thỏa mãn nào tồn tại.<br>

4.  Áp dụng các thuật toán trong (b) và (c) cho tập hợp các câu sau:<br>

 $A {\Rightarrow} B$<bR>

 $B {\Rightarrow} C$<br>

 $C {\Rightarrow} A$<br>

5.  Vì thuật toán trong (b) rất giống với thuật toán chuyển đổi sang CNF, và vì thuật toán trong (c) đơn giản hơn nhiều so với bất kỳ thuật toán nào để giải một tập hợp các câu ở dạng CNF, tại sao kỹ thuật này không được sử dụng trong suy luận tự động?<br>


---

##### Bài tập 7.25

Chuyển đổi tập hợp các câu sau sang dạng mệnh đề.<br>

1.  S1: $A {\;\;{\Leftrightarrow}\;\;}(B \lor E)$.<br>

2.  S2: $E {\:\;{\Rightarrow}\:\;}D$.<br>

3.  S3: $C \land F {\:\;{\Rightarrow}\:\;}\lnot B$.<br>

4.  S4: $E {\:\;{\Rightarrow}\:\;}B$.<br>

5.  S5: $B {\:\;{\Rightarrow}\:\;}F$.<br>

6.  S6: $B {\:\;{\Rightarrow}\:\;}C$<br>

Cung cấp một dấu vết thực thi của DPLL trên phép hội của các mệnh đề này.


---

##### Bài tập 7.26

Chuyển đổi tập hợp các câu sau sang dạng mệnh đề.<br>

1.  S1: $A {\;\;{\Leftrightarrow}\;\;}(B \lor E)$.<br>

2.  S2: $E {\:\;{\Rightarrow}\:\;}D$.<br>

3.  S3: $C \land F {\:\;{\Rightarrow}\:\;}\lnot B$.<br>

4.  S4: $E {\:\;{\Rightarrow}\:\;}B$.<br>

5.  S5: $B {\:\;{\Rightarrow}\:\;}F$.<br>

6.  S6: $B {\:\;{\Rightarrow}\:\;}C$<br>

Cung cấp một dấu vết thực thi của DPLL trên phép hội của các mệnh đề này.


---

##### Bài tập 7.27

Một câu 4-CNF được tạo ngẫu nhiên với $n$ ký hiệu và $m$ mệnh đề có khả năng được giải quyết hơn hay kém hơn một câu 3-CNF được tạo ngẫu nhiên với $n$ ký hiệu và $m$ mệnh đề? Giải thích.<br>


---

##### Bài tập 7.28

Minesweeper, trò chơi máy tính nổi tiếng, có liên quan chặt chẽ đến thế giới wumpus. Một thế giới minesweeper là một lưới hình chữ nhật gồm $N$ ô vuông với $M$ quả mìn vô hình nằm rải rác trong đó. Bất kỳ ô vuông nào cũng có thể được dò bởi agent; cái chết ngay lập tức sẽ xảy ra nếu dò phải một quả mìn. Minesweeper cho biết sự hiện diện của mìn bằng cách tiết lộ, trong mỗi ô vuông được dò, <i>số lượng</i> mìn ở các ô liền kề trực tiếp hoặc đường chéo. Mục tiêu là dò tất cả các ô vuông không có mìn.

1.  Đặt $X_{i,j}$ là đúng nếu ô vuông [i,j] chứa một quả mìn. Viết khẳng định rằng có đúng hai quả mìn liền kề với \[1,1\] dưới dạng một câu bao gồm một số tổ hợp logic của các mệnh đề
    $X_{i,j}$.

2.  Tổng quát hóa khẳng định của bạn từ (a) bằng cách giải thích cách xây dựng một câu CNF khẳng định rằng $k$ trong số $n$ ô liền kề chứa mìn.

3.  Giải thích chính xác cách một agent có thể sử dụng {DPLL} để chứng minh rằng một ô vuông cho trước có (hoặc không) chứa mìn, bỏ qua ràng buộc toàn cục rằng có tổng cộng $M$ quả mìn.

4.  Giả sử rằng ràng buộc toàn cục được xây dựng từ phương pháp của bạn trong phần (b). Số lượng mệnh đề phụ thuộc vào $M$ và $N$ như thế nào? Đề xuất một cách để sửa đổi {DPLL} sao cho ràng buộc toàn cục không cần được biểu diễn rõ ràng.

5.  Bất kỳ kết luận nào được rút ra bằng phương pháp ở phần (c) có bị vô hiệu hóa khi xem xét ràng buộc toàn cục không?

6.  Đưa ra các ví dụ về cấu hình các giá trị dò tìm gây ra <i>sự phụ thuộc tầm xa</i> sao cho nội dung của một ô vuông chưa dò tìm cho thông tin về nội dung của một ô vuông ở xa. (<i>Gợi ý</i>: xem xét một bảng $N\times 1$.)


---

##### Bài tập 7.29

Mất bao lâu để chứng minh
${KB}{\models}\alpha$ bằng {DPLL} khi $\alpha$ là một literal <i>đã có trong</i> ${KB}$? Giải thích.


---

##### Bài tập 7.30

Theo dõi hành vi của {DPLL} trên cơ sở tri thức trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/pl-horn-example-figure.png">pl-horn-example-figure</a> khi cố gắng chứng minh $Q$, và so sánh hành vi này với thuật toán forward-chaining.


---

##### Bài tập 7.31

Viết một tiên đề trạng thái kế tiếp cho vị từ ${Locked}$, áp dụng cho các cánh cửa, giả sử các hành động duy nhất có sẵn là ${Lock}$ và ${Unlock}$.


---

##### Bài tập 7.32

Thảo luận ý nghĩa của hành vi <i>tối ưu</i> trong thế giới wumpus. Chứng minh rằng {Hybrid-Wumpus-Agent} không tối ưu, và đề xuất các cách để cải thiện nó.


---

##### Bài tập 7.33

Giả sử một agent cư trú trong một thế giới có hai trạng thái, $S$ và $\lnot S$,
và chỉ có thể thực hiện một trong hai hành động, $a$ và $b$. Hành động $a$ không làm gì cả và hành động $b$ chuyển đổi giữa hai trạng thái. Đặt $S^t$ là mệnh đề rằng agent đang ở trạng thái $S$ tại thời điểm $t$, và đặt $a^t$ là mệnh đề rằng agent thực hiện hành động $a$ tại thời điểm $t$ (tương tự cho $b^t$).<br>

1.  Viết một tiên đề trạng thái kế tiếp cho $S^{t+1}$.<br>

2.  Chuyển đổi câu ở (a) sang CNF.<br>

3.  Trình bày một chứng minh bằng resolution refutation rằng nếu agent ở trạng thái $\lnot S$ tại thời điểm $t$ và thực hiện hành động $a$, thì nó vẫn sẽ ở trạng thái $\lnot S$ tại thời điểm $t+1$.


---

##### Bài tập 7.34

Mục <a class="sectionRef" title="" href="#">successor-state-section</a> cung cấp một số tiên đề trạng thái kế tiếp cần thiết cho thế giới wumpus. Viết các tiên đề cho tất cả các ký hiệu fluent còn lại.


---

##### Bài tập 7.35

Sửa đổi {Hybrid-Wumpus-Agent} để sử dụng phương pháp ước lượng trạng thái logic 1-CNF được mô tả trên trang <a class="pageRef" title="" href="#">1cnf-belief-state-page</a>. Chúng ta đã lưu ý trên trang đó rằng một agent như vậy sẽ không thể thu thập, duy trì và sử dụng các niềm tin phức tạp hơn như phép tuyển $P_{3,1}\lor P_{2,2}$. Đề xuất một phương pháp để khắc phục vấn đề này bằng cách định nghĩa các ký hiệu mệnh đề bổ sung, và thử nghiệm nó trong thế giới wumpus. Nó có cải thiện hiệu suất của agent không?


---

<!-- tabs:end -->
