# Chapter 08 First-order Logic

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_08/chapter_08_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_08_First-order%20Logic.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter08_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter08/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Logic](codeAndExercises/aima-python-master/notebooks/logic.ipynb)
- [Logic (Python File)](codeAndExercises/aima-python-master/notebooks/logic.py)


#### **Bài tập**


##### Bài tập 8.1

Một knowledge base logic biểu diễn thế giới bằng một tập hợp các câu không có cấu trúc tường minh. Ngược lại, một biểu diễn <b>analogical</b> có cấu trúc vật lý tương ứng trực tiếp với cấu trúc của sự vật được biểu diễn. Hãy xem xét bản đồ đường bộ của quốc gia bạn như một biểu diễn analogical của các sự kiện về quốc gia đó—nó biểu diễn các sự kiện bằng ngôn ngữ bản đồ. Cấu trúc hai chiều của bản đồ tương ứng với bề mặt hai chiều của khu vực.<br>

1.  Đưa ra năm ví dụ về các <i>symbols</i> trong ngôn ngữ bản đồ.<br>

2.  Một câu <i>explicit</i> là một câu mà người tạo ra biểu diễn thực sự viết ra. Một câu <i>implicit</i> là một câu phát sinh từ các câu explicit do các thuộc tính của biểu diễn analogical. Đưa ra ba ví dụ về các câu <i>implicit</i> và ba ví dụ về các câu <i>explicit</i> trong ngôn ngữ bản đồ.<br>

3.  Đưa ra ba ví dụ về các sự kiện liên quan đến cấu trúc vật lý của quốc gia bạn mà không thể biểu diễn trong ngôn ngữ bản đồ.<br>

4.  Đưa ra hai ví dụ về các sự kiện dễ biểu diễn hơn nhiều trong ngôn ngữ bản đồ so với logic bậc nhất.<br>

5.  Đưa ra hai ví dụ khác về các biểu diễn analogical hữu ích. Ưu và nhược điểm của mỗi ngôn ngữ này là gì?


---

##### Bài tập 8.2

Xem xét một knowledge base chỉ chứa hai câu: $P(a)$ và $P(b)$. Knowledge base này có suy ra $\forall\,x\ P(x)$ không? Giải thích câu trả lời của bạn theo các mô hình (models).


---

##### Bài tập 8.3

Câu ${\exists\,x,y\;\;} x{{\,=\,}}y$ có hợp lệ (valid) không? Giải thích.


---

##### Bài tập 8.4

Viết một câu logic sao cho mọi thế giới mà nó đúng chứa chính xác một đối tượng.


---

##### Bài tập 8.5

Viết một câu logic sao cho mọi thế giới mà nó đúng chứa chính xác hai đối tượng.


---

##### Bài tập 8.6

Xem xét một bộ từ vựng ký hiệu chứa $c$ ký hiệu hằng số, $p_k$ ký hiệu vị từ có mỗi arity $k$, và $f_k$ ký hiệu hàm có mỗi arity $k$, với $1\leq k\leq A$. Giả sử kích thước miền (domain size) được cố định là $D$. Đối với bất kỳ mô hình (model) nào, mỗi ký hiệu vị từ hoặc hàm được ánh xạ tới một quan hệ hoặc hàm tương ứng, có cùng arity. Bạn có thể giả định rằng các hàm trong mô hình cho phép một số bộ giá trị đầu vào không có giá trị cho hàm (tức là, giá trị là đối tượng vô hình). Hãy suy ra một công thức cho số lượng các mô hình có thể có cho một miền có $D$ phần tử. Đừng bận tâm đến việc loại bỏ các tổ hợp dư thừa.


---

##### Bài tập 8.7

Những câu nào sau đây là hợp lệ (luôn đúng)?<br>

1.  $(\exists x\ x{{\,=\,}}x) {\:\;{\Rightarrow}\:\;}({\forall\,y\;\;} \exists z\ y{{\,=\,}}z)$. <br>

2.  ${\forall\,x\;\;} P(x) \lor \lnot P(x)$.<br>

3.  ${\forall\,x\;\;} {Smart}(x) \lor (x{{\,=\,}}x)$.<br>


---

##### Bài tập 8.8

Xem xét một phiên bản ngữ nghĩa (semantics) cho logic bậc nhất mà trong đó các mô hình có miền rỗng (empty domains) được cho phép. Đưa ra ít nhất hai ví dụ về các câu hợp lệ theo ngữ nghĩa tiêu chuẩn nhưng không hợp lệ theo ngữ nghĩa mới. Thảo luận xem kết quả nào có ý nghĩa trực quan hơn cho các ví dụ của bạn.


---

##### Bài tập 8.9

Sự kiện $\lnot {Spouse}({George},{Laura})$ có suy ra từ các sự kiện ${Jim}\neq {George}$ và ${Spouse}({Jim},{Laura})$ không? Nếu có, hãy đưa ra một chứng minh; nếu không, hãy cung cấp các tiên đề bổ sung khi cần thiết. Điều gì xảy ra nếu chúng ta sử dụng ${Spouse}$ như một ký hiệu hàm một ngôi (unary function symbol) thay vì một vị từ hai ngôi (binary predicate)?


---

##### Bài tập 8.10

Bài tập này sử dụng ký hiệu hàm ${MapColor}$ và các vị từ ${In}(x,y)$, ${Borders}(x,y)$, và ${Country}(x)$, có các đối số là các vùng địa lý, cùng với các ký hiệu hằng số cho các vùng khác nhau. Trong mỗi trường hợp sau đây, chúng tôi đưa ra một câu tiếng Anh và một số biểu thức logic ứng viên. Đối với mỗi biểu thức logic, hãy cho biết liệu nó (1) biểu diễn đúng câu tiếng Anh; (2) không hợp lệ về mặt cú pháp và do đó vô nghĩa; hay (3) hợp lệ về mặt cú pháp nhưng không biểu diễn ý nghĩa của câu tiếng Anh.<br>

1.  Paris và Marseilles đều ở Pháp.<br>

    1.  ${In}({Paris} \land {Marseilles}, {France})$.<br>

    2.  ${In}({Paris},{France}) \land {In}({Marseilles},{France})$.<br>

    3.  ${In}({Paris},{France}) \lor {In}({Marseilles},{France})$.<br>

2.  Có một quốc gia giáp cả Iraq và Pakistan.<br>

    1.  ${\exists\,c\;\;}$
        ${Country}(c) \land {Border}(c,{Iraq}) \land {Border}(c,{Pakistan})$.<br>

    2.  ${\exists\,c\;\;}$
        ${Country}(c) {\:\;{\Rightarrow}\:\;}[{Border}(c,{Iraq}) \land {Border}(c,{Pakistan})]$.<br>

    3.  $[{\exists\,c\;\;}$
        ${Country}(c)] {\:\;{\Rightarrow}\:\;}[{Border}(c,{Iraq}) \land {Border}(c,{Pakistan})]$.<br>

    4.  ${\exists\,c\;\;}$
        ${Border}({Country}(c),{Iraq} \land {Pakistan})$.<br>

3.  Tất cả các quốc gia giáp Ecuador đều ở Nam Mỹ.<br>

    1.  ${\forall\,c\;\;}  Country(c) \land {Border}(c,{Ecuador}) {\:\;{\Rightarrow}\:\;}{In}(c,{SouthAmerica})$.<br>

    2.  ${\forall\,c\;\;}  {Country}(c) {\:\;{\Rightarrow}\:\;}[{Border}(c,{Ecuador}) {\:\;{\Rightarrow}\:\;}{In}(c,{SouthAmerica})]$.<br>

    3.  ${\forall\,c\;\;}  [{Country}(c) {\:\;{\Rightarrow}\:\;}{Border}(c,{Ecuador})] {\:\;{\Rightarrow}\:\;}{In}(c,{SouthAmerica})$.<br>

    4.  ${\forall\,c\;\;}  Country(c) \land {Border}(c,{Ecuador}) \land {In}(c,{SouthAmerica})$.<br>

4.  Không có vùng nào ở Nam Mỹ giáp với vùng nào ở Châu Âu.<br>

    1.  $\lnot [{\exists\,c,d\;\;}  {In}(c,{SouthAmerica}) \land {In}(d,{Europe}) \land {Borders}(c,d)]$.<br>

    2.  ${\forall\,c,d\;\;}  [{In}(c,{SouthAmerica}) \land {In}(d,{Europe})] {\:\;{\Rightarrow}\:\;}\lnot {Borders}(c,d)]$.<br>

    3.  $\lnot {\forall\,c\;\;} {In}(c,{SouthAmerica}) {\:\;{\Rightarrow}\:\;}{\exists\,d\;\;} {In}(d,{Europe}) \land<br> \lnot {Borders}(c,d)$.

    4.  ${\forall\,c\;\;} {In}(c,{SouthAmerica}) {\:\;{\Rightarrow}\:\;}{\forall\,d\;\;} {In}(d,{Europe}) {\:\;{\Rightarrow}\:\;}\lnot {Borders}(c,d)$.<br>

5.  Không có hai quốc gia liền kề nào có cùng màu bản đồ.<br>

    1.  ${\forall\,x,y\;\;} \lnot {Country}(x) \lor \lnot {Country}(y) \lor \lnot {Borders}(x,y) \lor {}$\
        $\lnot ({MapColor}(x) = {MapColor}(y))$.<br>

    2.  ${\forall\,x,y\;\;} ({Country}(x) \land {Country}(y) \land {Borders}(x,y) \land \lnot(x=y)) {\:\;{\Rightarrow}\:\;}{}$\
        $\lnot ({MapColor}(x) = {MapColor}(y))$.<br>

    3.  ${\forall\,x,y\;\;} {Country}(x) \land {Country}(y) \land {Borders}(x,y) \land {}$\
        $\lnot ({MapColor}(x) = {MapColor}(y))$.<br>

    4.  ${\forall\,x,y\;\;} ({Country}(x) \land {Country}(y) \land {Borders}(x,y) ) {\:\;{\Rightarrow}\:\;}{MapColor}(x\neq y)$.
<br>


---

##### Bài tập 8.11

Xem xét một bộ từ vựng chứa các ký hiệu sau:<br>

> ${Occupation}(p,o)$: Vị từ. Người $p$ có nghề nghiệp $o$.

> ${Customer}(p1,p2)$: Vị từ. Người $p1$ là khách hàng của người $p2$.

> ${Boss}(p1,p2)$: Vị từ. Người $p1$ là sếp của người $p2$.

> ${Doctor}$, $ {Surgeon}$, $ {Lawyer}$, $ {Actor}$: Các hằng số biểu thị nghề nghiệp.

> ${Emily}$, $ {Joe}$: Các hằng số biểu thị người.

Sử dụng các ký hiệu này để viết các khẳng định sau đây bằng logic bậc nhất:<br>

1.  Emily hoặc là bác sĩ phẫu thuật hoặc là luật sư.<br>

2.  Joe là diễn viên, nhưng anh ấy còn có một công việc khác.<br>

3.  Tất cả bác sĩ phẫu thuật đều là bác sĩ.<br>

4.  Joe không có luật sư (tức là không phải là khách hàng của bất kỳ luật sư nào).<br>

5.  Emily có một người sếp là luật sư.<br>

6.  Tồn tại một luật sư mà tất cả khách hàng của người đó đều là bác sĩ.<br>

7.  Mọi bác sĩ phẫu thuật đều có một luật sư.<br>


---

##### Bài tập 8.12

Trong mỗi trường hợp sau đây, chúng tôi đưa ra một câu tiếng Anh và một số biểu thức logic ứng viên. Đối với mỗi biểu thức logic, hãy cho biết liệu nó (1) biểu diễn đúng câu tiếng Anh; (2) không hợp lệ về mặt cú pháp và do đó vô nghĩa; hay (3) hợp lệ về mặt cú pháp nhưng không biểu diễn ý nghĩa của câu tiếng Anh.<br>

1.  Mọi con mèo đều yêu mẹ hoặc cha của nó.<br>

    1.  ${\forall\,x\;\;} {Cat}(x) {\:\;{\Rightarrow}\:\;}{Loves}(x,{Mother}(x)\lor {Father}(x))$.<br>

    2.  ${\forall\,x\;\;} \lnot {Cat}(x) \lor {Loves}(x,{Mother}(x)) \lor {Loves}(x,{Father}(x))$.<br>

    3.  ${\forall\,x\;\;} {Cat}(x) \land ({Loves}(x,{Mother}(x))\lor {Loves}(x,{Father}(x)))$.<br>

2.  Mọi con chó yêu một trong những người anh em của nó đều hạnh phúc.<br>

    1.  ${\forall\,x\;\;} {Dog}(x) \land (\exists y\ {Brother}(y,x) \land {Loves}(x,y)) {\:\;{\Rightarrow}\:\;}{Happy}(x)$.<br>

    2.  ${\forall\,x,y\;\;} {Dog}(x) \land {Brother}(y,x) \land {Loves}(x,y) {\:\;{\Rightarrow}\:\;}{Happy}(x)$.<br>

    3.  ${\forall\,x\;\;} {Dog}(x) \land [{\forall\,y\;\;} {Brother}(y,x) {\;\;{\Leftrightarrow}\;\;}{Loves}(x,y)] {\:\;{\Rightarrow}\:\;}{Happy}(x)$.<br>

3.  Không có con chó nào cắn con của chủ sở hữu của nó.<br>

    1.  ${\forall\,x\;\;} {Dog}(x) {\:\;{\Rightarrow}\:\;}\lnot {Bites}(x,{Child}({Owner}(x)))$.<br>

    2.  $\lnot {\exists\,x,y\;\;} {Dog}(x) \land {Child}(y,{Owner}(x)) \land {Bites}(x,y)$.<br>

    3.  ${\forall\,x\;\;} {Dog}(x) {\:\;{\Rightarrow}\:\;}({\forall\,y\;\;} {Child}(y,{Owner}(x)) {\:\;{\Rightarrow}\:\;}\lnot {Bites}(x,y))$.<br>

    4.  $\lnot {\exists\,x\;\;} {Dog}(x) {\:\;{\Rightarrow}\:\;}({\exists\,y\;\;} {Child}(y,{Owner}(x)) \land {Bites}(x,y))$.<br>

4.  Mã zip của mọi người trong một tiểu bang có cùng chữ số đầu tiên.<br>

    1.  ${\forall\,x,s,z_1\;\;} [{State}(s) \land {LivesIn}(x,s) \land {Zip}(x){{\,=\,}}z_1] {\:\;{\Rightarrow}\:\;}{}$\
        $[{\forall\,y,z_2\;\;} {LivesIn}(y,s) \land {Zip}(y){{\,=\,}}z_2 {\:\;{\Rightarrow}\:\;}{Digit}(1,z_1) {{\,=\,}}{Digit}(1,z_2) ]$.<br>

    2.  ${\forall\,x,s\;\;} [{State}(s) \land {LivesIn}(x,s) \land {\exists\,z_1\;\;} {Zip}(x){{\,=\,}}z_1] {\:\;{\Rightarrow}\:\;}{}$\
        $ [{\forall\,y,z_2\;\;} {LivesIn}(y,s) \land {Zip}(y){{\,=\,}}z_2 \land {Digit}(1,z_1) {{\,=\,}}{Digit}(1,z_2) ]$.<br>

    3.  ${\forall\,x,y,s\;\;} {State}(s) \land {LivesIn}(x,s) \land {LivesIn}(y,s) {\:\;{\Rightarrow}\:\;}{Digit}(1,{Zip}(x){{\,=\,}}{Zip}(y))$.<br>

    4.  ${\forall\,x,y,s\;\;} {State}(s) \land {LivesIn}(x,s) \land {LivesIn}(y,s) {\:\;{\Rightarrow}\:\;}{}$\
        ${Digit}(1,{Zip}(x)) {{\,=\,}}{Digit}(1,{Zip}(y))$.
<br>


---

##### Bài tập 8.13

Hoàn thành các bài tập sau về các câu logic:<br>

1.  Dịch sang tiếng Anh *hay, tự nhiên* (không có $x$ hay $y$!):<br>

$$
{\forall\,x,y,l\;\;} SpeaksLanguage(x, l) \land SpeaksLanguage(y, l)
    \implies Understands(x, y) \land Understands(y,x).<br>
$$

2.  Giải thích tại sao câu này được suy ra từ câu<br>

$$
{\forall\,x,y,l\;\;} SpeaksLanguage(x, l) \land SpeaksLanguage(y, l)
    \implies Understands(x, y).<br>
$$

3.  Dịch sang logic bậc nhất các câu sau:<br>

    1.  Sự thấu hiểu dẫn đến tình bạn.<br>

    2.  Tình bạn có tính bắc cầu.<br>

    Nhớ định nghĩa tất cả các vị từ, hàm và hằng số bạn sử dụng.


---

##### Bài tập 8.14

Đúng hay sai? Giải thích.<br>

1.  ${\exists\,x\;\;} x{{\,=\,}}{Rumpelstiltskin}$ là một câu hợp lệ (luôn đúng) của logic bậc nhất.<br>

2.  Mọi câu lượng từ hóa tồn tại (existentially quantified sentence) trong logic bậc nhất đều đúng trong bất kỳ mô hình nào chứa chính xác một đối tượng.<br>

3.  ${\forall\,x,y\;\;} x{{\,=\,}}y$ có thể thỏa mãn (satisfiable).<br>


---

##### Bài tập 8.15

Viết lại hai tiên đề Peano đầu tiên trong Phần <a class="sectionRef" title="" href="#">Peano-section</a> thành một tiên đề duy nhất định nghĩa ${NatNum}(x)$ để loại trừ khả năng có các số tự nhiên ngoại trừ những số được tạo ra bởi hàm kế tiếp (successor function).


---

##### Bài tập 8.16

Phương trình (<a class="equationRef" title="" href="#">pit-biconditional-equation</a>) trên trang <a class="pageRef" title="" href="#">pit-biconditional-equation</a> định nghĩa các điều kiện mà theo đó một ô vuông bị gió thổi. Ở đây chúng ta xem xét hai cách khác để mô tả khía cạnh này của thế giới wumpus.<br>

1.  Chúng ta có thể viết [quy tắc chẩn đoán] dẫn từ các hiệu ứng quan sát được đến các nguyên nhân ẩn. Để tìm các hố, các quy tắc chẩn đoán rõ ràng nói rằng nếu một ô vuông bị gió thổi, thì một ô vuông liền kề phải chứa một hố; và nếu một ô vuông không bị gió thổi, thì không có ô vuông liền kề nào chứa hố. Viết hai quy tắc này bằng logic bậc nhất và cho thấy rằng phép hội của chúng tương đương logic với Phương trình (<a href="#">pit-biconditional-equation</a>).<br>

2.  Chúng ta có thể viết [quy tắc nhân quả] dẫn từ nguyên nhân đến hiệu ứng. Một quy tắc nhân quả rõ ràng là một hố gây ra tất cả các ô vuông liền kề bị gió thổi. Viết quy tắc này bằng logic bậc nhất, giải thích tại sao nó không đầy đủ so với Phương trình (<a href="#">pit-biconditional-equation</a>), và cung cấp tiên đề còn thiếu.<br>


---

###### Bài tập 8.17

Viết các tiên đề mô tả các vị từ ${Grandchild}$, ${Greatgrandparent}$, ${Ancestor}$, ${Brother}$, ${Sister}$, ${Daughter}$, ${Son}$, ${FirstCousin}$, ${BrotherInLaw}$, ${SisterInLaw}$, ${Aunt}$, và ${Uncle}$. Tìm hiểu định nghĩa chính xác của $m$th cousin $n$ times removed, và viết định nghĩa bằng logic bậc nhất. Bây giờ hãy viết các sự kiện cơ bản được mô tả trong cây gia đình ở Hình <a class="insideExerciseFigRef" href="#family1-figure">family1-figure</a>. Sử dụng một hệ thống suy luận logic phù hợp, hãy chứng minh tất cả các câu bạn đã viết, và xác định ai là cháu của Elizabeth, anh rể của Diana, ông cố của Zara, và tổ tiên của Eugenie.<br>


<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/family1.svg" alt="family1-figure" id="family1-figure" style="width:100%">
  <figcaption><center><b>Một cây gia đình điển hình. Ký hiệu $\bowtie$ nối các cặp vợ chồng và các mũi tên chỉ đến con cái.</b></center></figcaption>
</figure>


---

##### Bài tập 8.18

Viết một câu khẳng định rằng + là một hàm giao hoán. Câu của bạn có suy ra từ các tiên đề Peano không? Nếu có, giải thích tại sao; nếu không, hãy đưa ra một mô hình mà các tiên đề đúng và câu của bạn sai.


---

##### Bài tập 8.19

Giải thích điều gì sai với định nghĩa được đề xuất sau đây cho vị từ thuộc tập hợp <br>
$$ {\forall,x,s;;} x \in {x|s} $$ $$ {\forall,x,s;;} x \in {s} \implies {\forall,y;;} x \in {y|s} $$


---

##### Bài tập 8.20

Sử dụng các tiên đề tập hợp làm ví dụ, hãy viết các tiên đề cho miền danh sách (list domain), bao gồm tất cả các hằng số, hàm và vị từ được đề cập trong chương.


---

##### Bài tập 8.21

Giải thích điều gì sai với định nghĩa được đề xuất sau đây cho các ô vuông liền kề trong thế giới wumpus:
$${\forall\,x,y\;\;} {Adjacent}([x,y], [x+1, y]) \land {Adjacent}([x,y], [x, y+1])\ .$$


---

##### Bài tập 8.22

Viết ra các tiên đề cần thiết để suy luận về vị trí của wumpus, sử dụng một ký hiệu hằng số ${Wumpus}$ và một vị từ hai ngôi ${At}({Wumpus}, {Location})$. Hãy nhớ rằng chỉ có một wumpus.


---

##### Bài tập 8.23

Giả sử các vị từ ${Parent}(p,q)$ và ${Female}(p)$ và các hằng số ${Joan}$ và ${Kevin}$, với ý nghĩa rõ ràng, hãy biểu diễn mỗi câu sau đây bằng logic bậc nhất. (Bạn có thể sử dụng ký hiệu viết tắt $\exists^{1}$ để chỉ "tồn tại duy nhất một.")<br>

1.  Joan có một cô con gái (có thể nhiều hơn một, và có thể cả con trai).<br>

2.  Joan có đúng một cô con gái (nhưng có thể có cả con trai).<br>

3.  Joan có đúng một đứa con, là con gái.<br>

4.  Joan và Kevin có đúng một đứa con chung.<br>

5.  Joan có ít nhất một đứa con với Kevin, và không có con với ai khác.


---

##### Bài tập 8.24

Các khẳng định số học có thể được viết bằng logic bậc nhất với ký hiệu vị từ $<$, các ký hiệu hàm ${+}$ và ${\times}$, và các ký hiệu hằng số 0 và 1. Các vị từ bổ sung cũng có thể được định nghĩa bằng các phép tương đương hai chiều (biconditionals).<br>

1.  Biểu diễn thuộc tính “$x$ là một số chẵn.”<br>

2.  Biểu diễn thuộc tính “$x$ là số nguyên tố.”<br>

3.  Giả thuyết Goldbach là giả thuyết (chưa được chứng minh) rằng mọi số chẵn đều bằng tổng của hai số nguyên tố. Biểu diễn giả thuyết này dưới dạng một câu logic.


---

##### Bài tập 8.25

Trong Chương <a class="chapterRef" title="" href="{{site.baseurl}}/csp-exercises/">csp-chapter</a>, chúng ta đã sử dụng phép bằng để chỉ mối quan hệ giữa một biến và giá trị của nó. Ví dụ, chúng ta đã viết ${WA}{{\,=\,}}{red}$ để có nghĩa là Tây Úc được tô màu đỏ. Khi biểu diễn điều này bằng logic bậc nhất, chúng ta phải viết một cách dài dòng hơn là ${ColorOf}({WA}){{\,=\,}}{red}$. Suy luận sai nào có thể được rút ra nếu chúng ta viết trực tiếp các câu như ${WA}{{\,=\,}}{red}$ dưới dạng các khẳng định logic?


---

##### Bài tập 8.26

Viết bằng logic bậc nhất khẳng định rằng mọi chìa khóa và ít nhất một trong mỗi cặp tất sẽ cuối cùng bị mất vĩnh viễn, chỉ sử dụng bộ từ vựng sau: ${Key}(x)$, $x$ là một chìa khóa; ${Sock}(x)$, $x$ là một chiếc tất; ${Pair}(x,y)$, $x$ và $y$ là một cặp; ${Now}$, thời điểm hiện tại; ${Before}(t_1,t_2)$, thời điểm $t_1$ đến trước thời điểm $t_2$; ${Lost}(x,t)$, đối tượng $x$ bị mất tại thời điểm $t$.


---

##### Bài tập 8.27

Đối với mỗi câu tiếng Anh sau đây, hãy quyết định xem câu logic bậc nhất đi kèm có phải là bản dịch tốt hay không. Nếu không, hãy giải thích tại sao không và sửa lại. (Một số câu có thể có nhiều hơn một lỗi!)<br>

1.  Không có hai người nào có cùng số an sinh xã hội.
    $$\lnot {\exists\,x,y,n\;\;} {Person}(x) \land {Person}(y) {\:\;{\Rightarrow}\:\;}[{HasSS}\#(x,n) \land {HasSS}\#(y,n)].$$<br>

2.  Số an sinh xã hội của John giống với của Mary.
    $${\exists\,n\;\;} {HasSS}\#({John},n) \land {HasSS}\#({Mary},n).$$<br>

3.  Số an sinh xã hội của mọi người đều có chín chữ số.<br>
    $${\forall\,x,n\;\;} {Person}(x) {\:\;{\Rightarrow}\:\;}[{HasSS}\#(x,n) \land {Digits}(n,9)].$$<br>

4.  Viết lại mỗi câu trên (chưa sửa lỗi) bằng cách sử dụng một ký hiệu hàm ${SS}\#$ thay vì vị từ ${HasSS}\#$.


---

##### Bài tập 8.28

Dịch sang logic bậc nhất câu “DNA của mỗi người là duy nhất và có nguồn gốc từ DNA của cha mẹ họ.” Bạn phải chỉ định ý nghĩa chính xác của các thuật ngữ từ vựng của mình. (*Gợi ý*: Đừng sử dụng vị từ ${Unique}(x)$, vì tính duy nhất thực sự không phải là thuộc tính của một đối tượng tự thân nó!)


---

##### Bài tập 8.29

Đối với mỗi câu tiếng Anh sau đây, hãy quyết định xem câu logic bậc nhất đi kèm có phải là bản dịch tốt hay không. Nếu không, hãy giải thích tại sao không và sửa lại.<br>

1.  Bất kỳ căn hộ nào ở London đều có giá thuê thấp hơn một số căn hộ ở Paris.<br>

$$
\forall {x} [{Apt}(x) \land {In}(x,{London})]
\implies \exists {y} ([{Apt}(y) \land {In}(y,{Paris})] \implies ({Rent}(x) < {Rent}(y)))
$$

2.  Chỉ có duy nhất một căn hộ ở Paris có giá thuê dưới 1000 đô la.<br>

$$
\exists {x} {Apt}(x) \land {In}(x,{Paris}) \land \forall{y} [{Apt}(y) \land {In}(y,{Paris}) \land ({Rent}(y) < {Dollars}(1000))] \implies (y = x)
$$

3.  Nếu một căn hộ đắt hơn tất cả các căn hộ ở London, thì nó phải ở Moscow.<br>

$$
\forall{x} {Apt}(x) \land [\forall{y} {Apt}(y) \land {In}(y,{London}) \land ({Rent}(x) > {Rent}(y))] \implies
{In}(x,{Moscow}).
$$


---

##### Bài tập 8.30

Biểu diễn các câu sau đây bằng logic bậc nhất, sử dụng một bộ từ vựng nhất quán (mà bạn phải định nghĩa):<br>

1.  Một số sinh viên đã học tiếng Pháp vào mùa xuân năm 2001.<br>

2.  Mọi sinh viên học tiếng Pháp đều vượt qua nó.<br>

3.  Chỉ có một sinh viên học tiếng Hy Lạp vào mùa xuân năm 2001.<br>

4.  Điểm cao nhất môn tiếng Hy Lạp luôn cao hơn điểm cao nhất môn tiếng Pháp.<br>

5.  Mọi người mua một hợp đồng bảo hiểm đều thông minh.<br>

6.  Không ai mua một hợp đồng bảo hiểm đắt tiền.<br>

7.  Có một agent bán hợp đồng bảo hiểm chỉ cho những người chưa được bảo hiểm.<br>

8.  Có một thợ cạo râu cạo cho tất cả đàn ông trong thị trấn không tự cạo râu.<br>

9.  Một người sinh ra ở Vương quốc Anh, mà mỗi phụ huynh của họ là công dân hoặc cư dân Vương quốc Anh, là công dân Vương quốc Anh theo khai sinh.<br>

10. Một người sinh ra bên ngoài Vương quốc Anh, mà một trong những phụ huynh của họ là công dân Vương quốc Anh theo khai sinh, là công dân Vương quốc Anh theo dòng dõi.<br>

11. Các chính trị gia có thể lừa dối một số người mọi lúc, và họ có thể lừa dối tất cả mọi người một lúc nào đó, nhưng họ không thể lừa dối tất cả mọi người mọi lúc.<br>

12. Tất cả người Hy Lạp nói cùng một ngôn ngữ. (Sử dụng ${Speaks}(x,l)$ để có nghĩa là người $x$ nói ngôn ngữ $l$.)


---

##### Bài tập 8.31

Biểu diễn các câu sau đây bằng logic bậc nhất, sử dụng một bộ từ vựng nhất quán (mà bạn phải định nghĩa):<br>

1.  Một số sinh viên đã học tiếng Pháp vào mùa xuân năm 2001.<br>

2.  Mọi sinh viên học tiếng Pháp đều vượt qua nó.<br>

3.  Chỉ có một sinh viên học tiếng Hy Lạp vào mùa xuân năm 2001.<br>

4.  Điểm cao nhất môn tiếng Hy Lạp luôn cao hơn điểm cao nhất môn tiếng Pháp.<br>

5.  Mọi người mua một hợp đồng bảo hiểm đều thông minh.<br>

6.  Không ai mua một hợp đồng bảo hiểm đắt tiền.<br>

7.  Có một agent bán hợp đồng bảo hiểm chỉ cho những người chưa được bảo hiểm.<br>

8.  Có một thợ cạo râu cạo cho tất cả đàn ông trong thị trấn không tự cạo râu.<br>

9.  Một người sinh ra ở Vương quốc Anh, mà mỗi phụ huynh của họ là công dân hoặc cư dân Vương quốc Anh, là công dân Vương quốc Anh theo khai sinh.<br>

10. Một người sinh ra bên ngoài Vương quốc Anh, mà một trong những phụ huynh của họ là công dân Vương quốc Anh theo khai sinh, là công dân Vương quốc Anh theo dòng dõi.<br>

11. Các chính trị gia có thể lừa dối một số người mọi lúc, và họ có thể lừa dối tất cả mọi người một lúc nào đó, nhưng họ không thể lừa dối tất cả mọi người mọi lúc.<br>

12. Tất cả người Hy Lạp nói cùng một ngôn ngữ. (Sử dụng ${Speaks}(x,l)$ để có nghĩa là người $x$ nói ngôn ngữ $l$.)


---

##### Bài tập 8.32

Viết một tập hợp các sự kiện và tiên đề chung để biểu diễn khẳng định “Wellington đã nghe về cái chết của Napoleon” và để trả lời đúng câu hỏi “Napoleon có nghe về cái chết của Wellington không?”


---

###### Bài tập 8.33

Mở rộng bộ từ vựng từ Phần <a class="sectionRef" title="" href="#">circuits-section</a> để định nghĩa phép cộng cho các số nhị phân $n$-bit. Sau đó mã hóa mô tả của bộ cộng bốn bit trong Hình <A href="#4bit-adder-figure">4bit-adder-figure</a>, và đặt các truy vấn cần thiết để xác minh rằng nó thực sự chính xác.<br>


<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/4bit-adder.svg" alt="4bit-adder-figure" id="4bit-adder-figure" style="width:100%">
  <figcaption><center><b>Một bộ cộng bốn bit. Mỗi ${Ad}_i$ là một bộ cộng một bit, như trong hình <a class="insideExercisesFigRef" id="insideexercisesfigref" href="#4bit-adder-figure">adder-figure</a> trên trang <a href=""#">adder-figure</a></b></center></figcaption>
</figure>


---

##### Bài tập 8.34

Biểu diễn mạch trong chương chi tiết hơn mức cần thiết nếu chúng ta chỉ quan tâm đến chức năng của mạch. Một cách diễn đạt đơn giản hơn mô tả bất kỳ cổng hoặc mạch $m$-đầu vào, $n$-đầu ra nào bằng một vị từ có $m+n$ đối số, sao cho vị từ đó đúng chính xác khi các đầu vào và đầu ra nhất quán. Ví dụ, các cổng NOT được mô tả bởi vị từ hai ngôi ${NOT}(i,o)$, với ${NOT}(0,1)$ và ${NOT}(1,0)$ đã biết. Các hợp của các cổng được định nghĩa bằng phép hội của các vị từ cổng mà các biến chung chỉ ra các kết nối trực tiếp. Ví dụ, một mạch NAND có thể được tạo thành từ các cổng ${AND}$ và ${NOT}$:
$${\forall\,i_1,i_2,o_a,o\;\;} {AND}(i_1,i_2,o_a) \land {NOT}(o_a,o) {\:\;{\Rightarrow}\:\;}{NAND}(i_1,i_2,o)\ .$$
Sử dụng biểu diễn này, hãy định nghĩa bộ cộng một bit trong Hình <a class="insideExercisesFigRef" href="#4bit-adder-figure">adder-figure</a> và bộ cộng bốn bit trong Hình <a class="insideExercisesFigRef" href="#4bit-adder-figure">adder-figure</a>, và giải thích các truy vấn bạn sẽ sử dụng để xác minh các thiết kế. Những loại truy vấn nào *không* được hỗ trợ bởi biểu diễn này mà *được* hỗ trợ bởi biểu diễn trong Phần <a class="sectionRef" title="" href="#">circuits-section</a>?


---

##### Bài tập 8.35

Lấy một đơn xin cấp hộ chiếu cho quốc gia của bạn, xác định các quy tắc xác định tính đủ điều kiện để được cấp hộ chiếu, và dịch chúng sang logic bậc nhất, tuân theo các bước được nêu trong Phần <a class="sectionRef" title="" href="#">circuits-section</a>


---

##### Bài tập 8.36

Xem xét một knowledge base logic bậc nhất mô tả các thế giới chứa người, bài hát, album (ví dụ: “Meet the Beatles”) và đĩa (tức là, các bản sao vật lý cụ thể của CD). Bộ từ vựng chứa các ký hiệu sau:<br>

> ${CopyOf}(d,a)$: Vị từ. Đĩa $d$ là bản sao của album $a$.

> ${Owns}(p,d)$: Vị từ. Người $p$ sở hữu đĩa $d$.

> ${Sings}(p,s,a)$: Album $a$ bao gồm bản thu âm bài hát $s$ do người $p$ hát.

> ${Wrote}(p,s)$: Người $p$ đã viết bài hát $s$.

> ${McCartney}$, ${Gershwin}$, ${BHoliday}$, ${Joe}$, ${EleanorRigby}$, ${TheManILove}$, ${Revolver}$: Các hằng số với ý nghĩa rõ ràng.

Biểu diễn các phát biểu sau đây bằng logic bậc nhất:<br>

1.  Gershwin đã viết “The Man I Love.”<br>

2.  Gershwin đã không viết “Eleanor Rigby.”<br>

3.  Hoặc Gershwin hoặc McCartney đã viết “The Man I Love.”<br>

4.  Joe đã viết ít nhất một bài hát.<br>

5.  Joe sở hữu một bản sao của *Revolver*.<br>

6.  Mọi bài hát mà McCartney hát trong *Revolver* đều được viết bởi McCartney.<br>

7.  Gershwin đã không viết bất kỳ bài hát nào trong *Revolver*.<br>

8.  Mọi bài hát mà Gershwin đã viết đều được thu âm trên một album nào đó. (Có thể các bài hát khác nhau được thu âm trên các album khác nhau.)<br>

9.  Có một album duy nhất chứa mọi bài hát mà Joe đã viết.<br>

10. Joe sở hữu một bản sao của một album có Billie Holiday hát “The Man I Love.”<br>

11. Joe sở hữu một bản sao của mọi album có bài hát do McCartney hát. (Tất nhiên, mỗi album khác nhau được thể hiện bằng một CD vật lý khác nhau.)<br>

12. Joe sở hữu một bản sao của mọi album mà tất cả các bài hát trên đó đều do Billie Holiday hát.<br>


---

<!-- tabs:end -->
