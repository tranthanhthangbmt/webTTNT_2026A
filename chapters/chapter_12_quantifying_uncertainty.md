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

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter12_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter12/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
<div id="quiz-container" data-chapter="12"></div>

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/DT-Agent.md" target="_blank">DT-AGENT</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Probability**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/probability.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/probability.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/probability.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 12.1

Định nghĩa một ontology bằng logic bậc nhất cho trò chơi cờ caro. Ontology
nên bao gồm các tình huống (situations), hành động (actions), ô vuông (squares), người chơi (players), ký hiệu (marks - X, O, hoặc trống), và khái niệm thắng, thua, hoặc hòa. Cũng định nghĩa khái niệm thắng (hoặc hòa) bắt buộc: một vị trí mà từ đó một người chơi có thể buộc phải thắng (hoặc hòa) với chuỗi hành động đúng đắn.
Viết các tiên đề (axioms) cho miền này. (Lưu ý: Các tiên đề liệt kê các ô vuông khác nhau và đặc trưng hóa các vị trí thắng khá dài. Bạn không cần viết chúng ra đầy đủ, nhưng hãy chỉ rõ chúng trông như thế nào.)


---

##### Bài tập 12.2

Bạn cần tạo một hệ thống để tư vấn cho sinh viên đại học ngành khoa học máy tính về các khóa học cần học trong một khoảng thời gian dài để đáp ứng các yêu cầu của chương trình. (Sử dụng bất kỳ yêu cầu nào phù hợp với tổ chức của bạn.) Đầu tiên, hãy quyết định một từ vựng để biểu diễn tất cả thông tin, sau đó biểu diễn nó; tiếp theo, xây dựng một truy vấn cho hệ thống sẽ trả về một chương trình học hợp lệ làm giải pháp. Bạn nên cho phép tùy chỉnh cho từng sinh viên, theo đó hệ thống của bạn sẽ hỏi sinh viên đã học những khóa học nào hoặc tương đương, và không tạo ra các chương trình lặp lại các khóa học đó.

Đề xuất các cách để cải thiện hệ thống của bạn—ví dụ: để tính đến kiến thức về sở thích của sinh viên, khối lượng công việc, giảng viên tốt và xấu, v.v. Đối với mỗi loại kiến thức, hãy giải thích cách nó có thể được diễn đạt bằng logic. Hệ thống của bạn có thể dễ dàng kết hợp thông tin này để tìm tất cả các chương trình học khả thi cho sinh viên không? Nó có thể tìm ra chương trình *tốt nhất* không?


---

##### Bài tập 12.3

Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/ontology-figure.png">ontology-figure</a> hiển thị các cấp cao nhất của một
hệ thống phân cấp cho mọi thứ. Hãy mở rộng nó để bao gồm càng nhiều danh mục thực tế càng tốt. Một cách tốt để làm điều này là bao quát tất cả những thứ trong cuộc sống hàng ngày của bạn. Điều này bao gồm các đối tượng và sự kiện. Bắt đầu bằng việc thức dậy, và tiến hành một cách có trật tự ghi lại mọi thứ bạn nhìn thấy, chạm vào, làm và suy nghĩ về. Ví dụ, một mẫu ngẫu nhiên cho ra âm nhạc, tin tức, sữa, đi bộ, lái xe, xăng, Soda Hall, thảm, nói chuyện, Giáo sư Fateman, cà ri gà, lưỡi, 7 đô la, mặt trời, báo hàng ngày, v.v.<br>

Bạn nên tạo cả một biểu đồ phân cấp duy nhất (trên một tờ giấy lớn) và một danh sách các đối tượng và danh mục với các quan hệ được thỏa mãn bởi các thành viên của mỗi danh mục. Mọi đối tượng phải nằm trong một danh mục, và mọi danh mục phải nằm trong hệ thống phân cấp.


---

##### Bài tập 12.4

Phát triển một hệ thống biểu diễn để suy luận
về các cửa sổ trong giao diện máy tính dựa trên cửa sổ. Đặc biệt, biểu diễn của bạn phải có khả năng mô tả:<br>


-   Trạng thái của một cửa sổ: thu nhỏ (minimized), hiển thị (displayed), hoặc không tồn tại (nonexistent).<br>

-   Cửa sổ nào (nếu có) là cửa sổ đang hoạt động (active window).<br>

-   Vị trí của mọi cửa sổ tại một thời điểm nhất định.<br>

-   Thứ tự (từ trước ra sau) của các cửa sổ chồng lên nhau.<br>

-   Các hành động tạo, xóa, thay đổi kích thước và di chuyển cửa sổ;
    thay đổi trạng thái của cửa sổ; và đưa một cửa sổ lên phía trước.
    Coi các hành động này là nguyên tử (atomic); nghĩa là, không xem xét
    vấn đề liên hệ chúng với các hành động chuột. Đưa ra các tiên đề mô tả
    ảnh hưởng của các hành động lên các fluent. Bạn có thể sử dụng event calculus hoặc situation calculus.<br>

Giả sử một ontology chứa các <i>situations,</i>
<i>actions,</i> <i>integers</i> (cho tọa độ $x$ và $y$) và
<i>windows</i>. Định nghĩa một ngôn ngữ trên ontology này; nghĩa là,
một danh sách các hằng số, ký hiệu hàm và vị từ với mô tả tiếng Anh
cho mỗi cái. Nếu bạn cần thêm các danh mục vào ontology (ví dụ: pixels),
bạn có thể làm vậy, nhưng hãy chắc chắn chỉ định chúng trong bài viết
của bạn. Bạn có thể (và nên) sử dụng các ký hiệu được định nghĩa trong
văn bản, nhưng hãy chắc chắn liệt kê chúng một cách rõ ràng.


---

##### Bài tập 12.5

Phát biểu các điều sau đây bằng ngôn ngữ bạn đã phát triển cho bài
tập trước:<br>

1.  Trong tình huống $S_0$, cửa sổ $W_1$ nằm sau $W_2$ nhưng nhô ra
    ở trên và dưới. *Không* nêu tọa độ chính xác cho những điều này;
    mô tả tình huống *chung*.<br>

2.  Nếu một cửa sổ được hiển thị, thì cạnh trên của nó cao hơn cạnh
    dưới của nó.<br>

3.  Sau khi bạn tạo một cửa sổ $w$, nó sẽ được hiển thị.<br>

4.  Một cửa sổ chỉ có thể được thu nhỏ nếu nó đang được hiển thị.<br>


---

##### Bài tập 12.6

Phát biểu các điều sau đây bằng ngôn ngữ bạn đã phát triển cho bài
tập trước:<br>

1.  Trong tình huống $S_0$, cửa sổ $W_1$ nằm sau $W_2$ nhưng nhô ra
    ở trên và dưới. *Không* nêu tọa độ chính xác cho những điều này;
    mô tả tình huống *chung*.<br>

2.  Nếu một cửa sổ được hiển thị, thì cạnh trên của nó cao hơn cạnh
    dưới của nó.<br>

3.  Sau khi bạn tạo một cửa sổ $w$, nó sẽ được hiển thị.<br>

4.  Một cửa sổ chỉ có thể được thu nhỏ nếu nó đang được hiển thị.<br>


---

##### Bài tập 12.7

(Chuyển thể từ một ví dụ của Doug Lenat.) Nhiệm vụ của bạn là nắm bắt,
dưới dạng logic, đủ kiến thức để trả lời một loạt câu hỏi về kịch bản
đơn giản sau:<br>
<Br>
<i> Hôm qua John đã đến siêu thị Safeway ở North Berkeley và</i><br>
<i> mua hai pound cà chua và một pound thịt bò xay.</i>

Bắt đầu bằng cách cố gắng biểu diễn nội dung của câu thành một loạt các
khẳng định. Bạn nên viết các câu có cấu trúc logic đơn giản (ví dụ:
các phát biểu rằng các đối tượng có thuộc tính nhất định, rằng các đối
tượng có quan hệ với nhau theo những cách nhất định, rằng tất cả các đối
tượng thỏa mãn một thuộc tính đều thỏa mãn một thuộc tính khác). Những
điều sau đây có thể giúp bạn bắt đầu:<br>

-   Bạn sẽ cần những lớp (classes), đối tượng (objects) và quan hệ
    (relations) nào? Cha mẹ, anh chị em của chúng là gì, v.v.? (Bạn sẽ
    cần các sự kiện (events) và thứ tự thời gian (temporal ordering),
    trong số những thứ khác.)<br>

-   Chúng sẽ phù hợp ở đâu trong một hệ thống phân cấp tổng quát hơn?<br>

-   Các ràng buộc (constraints) và mối quan hệ tương hỗ (interrelationships)
    giữa chúng là gì?<br>

-   Bạn cần chi tiết đến mức nào về từng khái niệm khác nhau?<br>

Để trả lời các câu hỏi dưới đây, cơ sở kiến thức của bạn phải bao gồm
kiến thức nền. Bạn sẽ phải xử lý những loại thứ có ở siêu thị, những gì
liên quan đến việc mua những thứ bạn chọn, những gì việc mua hàng sẽ
được sử dụng cho, v.v. Hãy cố gắng làm cho biểu diễn của bạn càng tổng
quát càng tốt. Để đưa ra một ví dụ tầm thường: đừng nói “Mọi người mua
thực phẩm từ Safeway,” vì điều đó sẽ không giúp bạn với những người mua
sắm ở siêu thị khác. Ngoài ra, đừng biến câu hỏi thành câu trả lời; ví
dụ, câu hỏi (c) hỏi “John có mua thịt không?”—không phải “John có mua
một pound thịt bò xay không?”<br>

Phác thảo các chuỗi suy luận sẽ trả lời các câu hỏi. Nếu có thể, hãy sử
dụng một hệ thống suy luận logic để chứng minh tính đầy đủ của cơ sở
kiến thức của bạn. Nhiều thứ bạn viết có thể chỉ đúng gần đúng trong
thực tế, nhưng đừng quá lo lắng; ý tưởng là trích xuất common sense cho
phép bạn trả lời những câu hỏi này. Một câu trả lời hoàn chỉnh thực sự
cho câu hỏi này là *cực kỳ* khó, có lẽ vượt quá trạng thái hiện tại
của knowledge representation. Nhưng bạn sẽ có thể xây dựng một tập hợp
các tiên đề nhất quán cho các câu hỏi giới hạn được đặt ra ở đây.<br>

1.  John là trẻ con hay người lớn? [Người lớn]<br>

2.  John bây giờ có ít nhất hai quả cà chua không? [Có]<br>

3.  John có mua thịt không? [Có]<br>

4.  Nếu Mary đang mua cà chua cùng lúc với John, thì anh ấy có nhìn
    thấy cô ấy không? [Có]<br>

5.  Cà chua có được làm trong siêu thị không? [Không]<br>

6.  John sẽ làm gì với cà chua? [Ăn chúng]<br>

7.  Safeway có bán chất khử mùi không? [Có]<br>

8.  John có mang theo tiền hoặc thẻ tín dụng đến siêu thị không?
    [Có]<br>

9.  John có ít tiền hơn sau khi đi siêu thị không? [Có]<br>


---

##### Bài tập 12.8

Thực hiện các bổ sung hoặc thay đổi cần thiết cho cơ sở kiến thức của
bạn từ bài tập trước để các câu hỏi sau đây có thể được trả lời. Bao gồm
trong báo cáo của bạn một cuộc thảo luận về những thay đổi của bạn, giải
thích tại sao chúng cần thiết, liệu chúng có nhỏ hay lớn, và những loại
câu hỏi nào sẽ đòi hỏi những thay đổi tiếp theo.<br>

1.  Có những người nào khác trong Safeway khi John ở đó không?
    [Có—nhân viên!]<br>

2.  John có ăn chay không? [Không]<br>

3.  Ai sở hữu chất khử mùi trong Safeway? [Safeway Corporation]<br>

4.  John có một ounce thịt bò xay không? [Có]<br>

5.  Trạm Shell bên cạnh có xăng không? [Có]<br>

6.  Cà chua có vừa với cốp xe của John không? [Có]<br>


---

##### Bài tập 12.9

Biểu diễn bảy câu sau đây bằng cách sử dụng và mở rộng các biểu diễn
đã phát triển trong chương:<br>

1.  Nước là chất lỏng ở nhiệt độ từ 0 đến 100 độ.<br>

2.  Nước sôi ở 100 độ.<br>

3.  Nước trong chai nước của John bị đóng băng.<br>

4.  Perrier là một loại nước.<br>

5.  John có Perrier trong chai nước của mình.<br>

6.  Tất cả các chất lỏng đều có điểm đóng băng.<br>

7.  Một lít nước nặng hơn một lít rượu.<br>


---

##### Bài tập 12.10

Viết định nghĩa cho các thuật ngữ sau:<br>

1.  ${ExhaustivePartDecomposition}$<br>

2.  ${PartPartition}$<br>

3.  ${PartwiseDisjoint}$<br>

Các định nghĩa này nên tương tự như các định nghĩa cho
${ExhaustiveDecomposition}$, ${Partition}$, và ${Disjoint}$. Có phải
${PartPartition}(s,{BunchOf}(s))$ đúng không? Nếu có, hãy chứng minh;
nếu không, hãy đưa ra một phản ví dụ và định nghĩa các điều kiện đủ mà
trong đó nó đúng.


---

##### Bài tập 12.11

Một sơ đồ thay thế để biểu diễn các phép đo
liên quan đến việc áp dụng hàm đơn vị (units function) cho một đối tượng
chiều dài trừu tượng. Trong một sơ đồ như vậy, người ta sẽ viết
${Inches}({Length}(L_1)) = {1.5}$. Sơ đồ này so với sơ đồ trong
chương như thế nào? Các vấn đề bao gồm các tiên đề chuyển đổi, tên cho
các đại lượng trừu tượng (như “50 đô la”), và so sánh các phép đo trừu
tượng với các đơn vị khác nhau (50 inch lớn hơn 50 centimet).


---

##### Bài tập 12.12

Viết một tập hợp các câu cho phép tính giá của một quả cà chua riêng
lẻ (hoặc đối tượng khác), với giá mỗi pound. Mở rộng lý thuyết để cho phép
tính giá của một túi cà chua.


---

##### Bài tập 12.13

Thêm các câu để mở rộng định nghĩa của vị từ
${Name}(s, c)$ sao cho một chuỗi như “laptop computer” khớp với tên
danh mục phù hợp từ nhiều cửa hàng khác nhau. Hãy cố gắng làm cho định
nghĩa của bạn trở nên tổng quát. Kiểm tra nó bằng cách xem xét mười
cửa hàng trực tuyến và tên danh mục mà họ đưa ra cho ba danh mục khác
nhau. Ví dụ, đối với danh mục máy tính xách tay, chúng tôi tìm thấy các
tên “Notebooks,” “Laptops,” “Notebook Computers,” “Notebook,” “Laptops
and Notebooks,” và “Notebook PCs.” Một số trong số này có thể được bao
phủ bởi các sự kiện ${Name}$ rõ ràng, trong khi những sự kiện khác có
thể được bao phủ bởi các câu để xử lý số nhiều, phép nối, v.v.


---

##### Bài tập 12.14

Viết các tiên đề event calculus để mô tả các hành động trong thế giới
wumpus.


---

##### Bài tập 12.15

Phát biểu quan hệ interval-algebra giữa mọi cặp các sự kiện thế giới
thực sau đây:<br>

> $LK$: Cuộc đời của Tổng thống Kennedy.<br>

> $IK$: Thời thơ ấu của Tổng thống Kennedy.<br>

> $PK$: Nhiệm kỳ tổng thống của Tổng thống Kennedy.<br>

> $LJ$: Cuộc đời của Tổng thống Johnson.<br>

> $PJ$: Nhiệm kỳ tổng thống của Tổng thống Johnson.<br>

> $LO$: Cuộc đời của Tổng thống Obama.<br>


---

##### Bài tập 12.16

Bài tập này liên quan đến vấn đề lập kế hoạch lộ trình cho một robot đi
từ thành phố này sang thành phố khác. Hành động cơ bản mà robot thực hiện
là ${Go}(x,y)$, đưa nó từ thành phố $x$ đến thành phố $y$ nếu có một
tuyến đường giữa hai thành phố đó. ${Road}(x, y)$ đúng khi và chỉ khi
có một con đường nối các thành phố $x$ và $y$; nếu có, thì
${Distance}(x, y)$ cho biết độ dài của con đường. Xem bản đồ trên trang
<a class="pageRef" title="" href="#">romania-distances-figure</a> để biết ví dụ. Robot bắt đầu ở Arad và phải đến
Bucharest.<br>

1.  Viết mô tả logic phù hợp về tình huống ban đầu của robot.<br>

2.  Viết một truy vấn logic phù hợp mà các giải pháp của nó cung cấp
    các đường dẫn khả thi đến mục tiêu.<br>

3.  Viết một câu mô tả hành động ${Go}$.<br>

4.  Bây giờ giả sử rằng robot tiêu thụ nhiên liệu với tốc độ 0,02
    gallon mỗi dặm. Robot bắt đầu với 20 gallon nhiên liệu. Bổ sung biểu
    diễn của bạn để bao gồm các cân nhắc này.<br>

5.  Bây giờ giả sử một số thành phố có trạm xăng nơi robot có thể đổ
    đầy bình. Mở rộng biểu diễn của bạn và viết tất cả các quy tắc cần
    thiết để mô tả các trạm xăng, bao gồm cả hành động ${Fillup}$.<br>


---

##### Bài tập 12.17

Điều tra các cách để mở rộng event calculus để xử lý các sự kiện
*đồng thời* (simultaneous). Có thể tránh được sự bùng nổ tổ hợp (combinatorial explosion) của các tiên đề không?


---

##### Bài tập 12.18

Xây dựng một biểu diễn cho tỷ giá hối đoái
giữa các loại tiền tệ cho phép biến động hàng ngày.


---

##### Bài tập 12.19

Định nghĩa vị từ ${Fixed}$, trong đó
${Fixed}({Location}(x))$ có nghĩa là vị trí của đối tượng $x$ là
cố định theo thời gian.


---

##### Bài tập 12.20

Mô tả sự kiện trao đổi một thứ gì đó lấy một thứ khác. Mô tả việc mua
hàng như một loại trao đổi mà một trong những đối tượng được trao đổi là
một khoản tiền.


---

##### Bài tập 12.21

Hai bài tập trước giả định một khái niệm sở hữu khá sơ khai. Ví dụ, người
mua bắt đầu bằng cách *sở hữu* các tờ đô la. Bức tranh này bắt đầu
tan vỡ khi, ví dụ, tiền của một người ở trong ngân hàng, bởi vì không còn
bất kỳ tập hợp các tờ đô la cụ thể nào mà người đó sở hữu. Bức tranh
còn phức tạp hơn nữa bởi việc vay mượn, cho thuê, thuê dài hạn và gửi
giữ. Điều tra các khái niệm sở hữu thông thường và pháp lý khác nhau,
và đề xuất một sơ đồ mà theo đó chúng có thể được biểu diễn một cách hình
thức.


---

##### Bài tập 12.22

(Chuyển thể từ <a class="paperRef" title="" href="">Fagin+al:1995</a>.) Xem xét một trò chơi được chơi với một bộ bài chỉ có 8 lá, 4 quân Át và 4 quân Vua. Ba người chơi, Alice, Bob và Carlos, được chia hai lá bài mỗi người. Không nhìn vào chúng, họ đặt các lá bài lên trán để những người chơi khác có thể nhìn thấy chúng. Sau đó, những người chơi lần lượt thông báo rằng họ biết những lá bài nào trên trán của mình, qua đó thắng trò chơi, hoặc nói "Tôi không biết." Mọi người đều biết rằng những người chơi này trung thực và có khả năng suy luận hoàn hảo về niềm tin (beliefs).<br>

1.  Trò chơi 1. Alice và Bob đều nói "Tôi không biết." Carlos nhìn thấy Alice có hai quân Át (A-A) và Bob có hai quân Vua (K-K). Carlos nên nói gì? ( *Gợi ý*: xem xét cả ba trường hợp có thể xảy ra đối với Carlos: A-A, K-K, A-K.)<br>

2.  Mô tả từng bước của Trò chơi 1 bằng ký hiệu logic modal (modal logic).<br>

3.  Trò chơi 2. Carlos, Alice và Bob đều nói "Tôi không biết" trong lượt đầu tiên của họ. Alice cầm K-K và Bob cầm A-K. Carlos nên nói gì trong lượt thứ hai của mình?<br>

4.  Trò chơi 3. Alice, Carlos và Bob đều nói "Tôi không biết" trong lượt đầu tiên, cũng như Alice trong lượt thứ hai của cô ấy. Alice và Bob đều cầm A-K. Carlos nên nói gì?<br>

5.  Chứng minh rằng trò chơi này luôn có người thắng.<br>


---

##### Bài tập 12.23

Giả định về sự *toàn tri logic* (logical omniscience), được thảo luận trên trang <a class="pageRef" title="" href="#">logical-omniscience</a>, tất nhiên không đúng với bất kỳ người suy luận thực tế nào. Thay vào đó, đó là một *lý tưởng hóa* (idealization) của quá trình suy luận có thể chấp nhận được nhiều hơn hoặc ít hơn tùy thuộc vào các ứng dụng. Thảo luận về tính hợp lý của giả định đối với từng ứng dụng sau đây của suy luận về kiến thức:<br>

1.  Các trò chơi đối kháng với kiến thức không đầy đủ (Partial knowledge adversary games), chẳng hạn như các trò chơi bài. Ở đây, một người chơi muốn suy luận về những gì đối thủ của mình biết về trạng thái của trò chơi.<br>

2.  Cờ vua có đồng hồ. Ở đây, người chơi có thể muốn suy luận về giới hạn khả năng tìm ra nước đi tốt nhất của đối thủ hoặc của chính mình trong thời gian có sẵn. Ví dụ, nếu người chơi A còn nhiều thời gian hơn người chơi B, thì A đôi khi sẽ thực hiện một nước đi làm phức tạp tình huống lên rất nhiều, với hy vọng giành được lợi thế vì anh ta có nhiều thời gian hơn để tìm ra chiến lược phù hợp.<br>

3.  Một agent mua sắm trong một môi trường có chi phí thu thập thông tin.<br>

4.  Suy luận về mật mã khóa công khai (public key cryptography), dựa trên tính khó khăn của các bài toán tính toán nhất định.


---

##### Bài tập 12.24

Giả định về sự *toàn tri logic* (logical omniscience), được thảo luận trên trang <a class="pageRef" title="" href="#">logical-omniscience</a>, tất nhiên không đúng với bất kỳ người suy luận thực tế nào. Thay vào đó, đó là một *lý tưởng hóa* (idealization) của quá trình suy luận có thể chấp nhận được nhiều hơn hoặc ít hơn tùy thuộc vào các ứng dụng. Thảo luận về tính hợp lý của giả định đối với từng ứng dụng sau đây của suy luận về kiến thức:<br>

1.  Các trò chơi đối kháng với kiến thức không đầy đủ (Partial knowledge adversary games), chẳng hạn như các trò chơi bài. Ở đây, một người chơi muốn suy luận về những gì đối thủ của mình biết về trạng thái của trò chơi.<br>

2.  Cờ vua có đồng hồ. Ở đây, người chơi có thể muốn suy luận về giới hạn khả năng tìm ra nước đi tốt nhất của đối thủ hoặc của chính mình trong thời gian có sẵn. Ví dụ, nếu người chơi A còn nhiều thời gian hơn người chơi B, thì A đôi khi sẽ thực hiện một nước đi làm phức tạp tình huống lên rất nhiều, với hy vọng giành được lợi thế vì anh ta có nhiều thời gian hơn để tìm ra chiến lược phù hợp.<br>

3.  Một agent mua sắm trong một môi trường có chi phí thu thập thông tin.<br>

4.  Suy luận về mật mã khóa công khai (public key cryptography), dựa trên tính khó khăn của các bài toán tính toán nhất định.


---

##### Bài tập 12.25

Dịch biểu thức logic mô tả (description logic expression) sau đây (từ trang <a class="pageRef" title="" href="#">description-logic-ex</a>) sang logic bậc nhất, và nhận xét về kết quả:<br>
$$
And(Man, AtLeast(3,Son), AtMost(2,Daughter), \\All(Son,And(Unemployed,Married, All(Spouse,Doctor ))), \\All(Daughter,And(Professor, Fills(Department ,Physics,Math))))
$$


---

##### Bài tập 12.26

Nhớ lại rằng thông tin kế thừa (inheritance information) trong mạng ngữ nghĩa (semantic networks) có thể được nắm bắt bằng logic thông qua các câu kéo theo phù hợp. Bài tập này điều tra hiệu quả của việc sử dụng các câu như vậy cho việc kế thừa.<br>

1.  Xem xét thông tin trong một danh mục xe đã qua sử dụng như Kelly’s Blue Book—ví dụ, rằng xe van Dodge đời 1973 có giá trị (hoặc có lẽ từng có giá trị) 575 đô la. Giả sử tất cả thông tin này (cho 11.000 mẫu xe) được mã hóa dưới dạng các câu logic, như gợi ý trong chương. Viết ba câu như vậy, bao gồm cả câu cho xe van Dodge đời 1973. Bạn sẽ sử dụng các câu này như thế nào để tìm giá trị của một chiếc xe *cụ thể*, với một trình chứng minh định lý theo kiểu backward-chaining như Prolog?<br>

2.  So sánh hiệu quả thời gian của phương pháp backward-chaining để giải quyết vấn đề này với phương pháp kế thừa được sử dụng trong mạng ngữ nghĩa.<br>

3.  Giải thích làm thế nào forward chaining cho phép một hệ thống dựa trên logic giải quyết cùng một vấn đề một cách hiệu quả, giả sử rằng KB chỉ chứa 11.000 câu về giá.<br>

4.  Mô tả một tình huống mà cả forward chaining và backward chaining trên các câu sẽ không cho phép truy vấn giá cho một chiếc xe riêng lẻ được xử lý hiệu quả.<br>

5.  Bạn có thể đề xuất một giải pháp cho phép loại truy vấn này được giải quyết hiệu quả trong mọi trường hợp trong các hệ thống logic không? *Gợi ý*: Hãy nhớ rằng hai chiếc xe cùng năm và cùng mẫu có cùng giá.)


---

##### Bài tập 12.27

Người ta có thể cho rằng sự phân biệt cú pháp giữa các liên kết không được đóng khung (unboxed links) và các liên kết được đóng khung đơn (singly boxed links) trong mạng ngữ nghĩa là không cần thiết, bởi vì các liên kết được đóng khung đơn luôn được gắn vào các danh mục; một thuật toán kế thừa có thể đơn giản giả định rằng một liên kết không được đóng khung gắn vào một danh mục được dự định áp dụng cho tất cả các thành viên của danh mục đó. Chứng minh rằng lập luận này là sai lầm, đưa ra các ví dụ về các lỗi có thể xảy ra.


---

##### Bài tập 12.28

Một phần của quá trình mua sắm chưa được đề cập trong chương này là kiểm tra tính tương thích giữa các mặt hàng. Ví dụ, nếu một máy ảnh kỹ thuật số được đặt hàng, thì những pin phụ kiện, thẻ nhớ và vỏ máy nào tương thích với máy ảnh đó? Viết một cơ sở kiến thức có thể xác định tính tương thích của một tập hợp các mặt hàng và đề xuất các sản phẩm thay thế hoặc bổ sung nếu người mua đưa ra lựa chọn không tương thích. Cơ sở kiến thức nên hoạt động với ít nhất một dòng sản phẩm và dễ dàng mở rộng sang các dòng khác.


---

##### Bài tập 12.29

Một giải pháp hoàn chỉnh cho vấn đề
khớp không chính xác với mô tả của người mua trong mua sắm là rất khó
và đòi hỏi một bộ đầy đủ các kỹ thuật xử lý ngôn ngữ tự nhiên và truy
xuất thông tin. (Xem Chương <a class="chapterRef" title="" href="{{site.baseurl}}/nlp1-exercises/">nlp1-chapter</a>
và <a class="chapterRef" title="" href="{{site.baseurl}}/nlp-communicating-exercises/">nlp-english-chapter</a>.) Một bước nhỏ là cho phép người dùng chỉ định giá trị tối thiểu và tối đa cho các thuộc tính khác nhau. Người mua phải sử dụng ngữ pháp sau đây cho mô tả sản phẩm:<br>

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

Ở đây, ${Category}$ đặt tên cho một danh mục sản phẩm, ${Attribute}$ là một
tính năng nào đó như “CPU” hoặc “price,” và ${Value}$ là giá trị mục
tiêu cho thuộc tính. Vì vậy, truy vấn “computer with at least a 2.5 GHz
CPU for under 500” phải được diễn đạt lại thành “computer with CPU $>$
2.5 GHz and price $<$ 500.” Triển khai một agent mua sắm chấp nhận mô tả
theo ngôn ngữ này.


---

##### Bài tập 12.30

Mô tả của chúng ta về mua sắm trên Internet đã bỏ qua bước quan trọng
nhất là *mua* sản phẩm.
Cung cấp một mô tả logic hình thức về việc mua hàng, sử dụng event
calculus. Nghĩa là, định nghĩa chuỗi các sự kiện xảy ra khi người mua
gửi thanh toán bằng thẻ tín dụng và sau đó cuối cùng nhận được hóa đơn
và sản phẩm.


---

<!-- tabs:end -->
