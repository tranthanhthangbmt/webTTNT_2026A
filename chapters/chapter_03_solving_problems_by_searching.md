# Chapter 03 Solving Problems by Searching

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_03/chapter_03_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_03_Solving%20Problems%20by%20Searching.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter03_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter03/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Simple-Problem-Solving-Agent.md" target="_blank">SIMPLE-PROBLEM-SOLVING-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Tree-Search-and-Graph-Search.md" target="_blank">BEST-FIRST-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Breadth-First-Search.md" target="_blank">BREADTH-FIRST-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Iterative-Deepening-Search.md" target="_blank">ITERATIVE-DEEPENING-SEARCH</a>
- <a href="codeAndExercises/aima-pseudocode-master/" target="_blank" data-ignore>BIBF-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Uniform-Cost-Search.md" target="_blank">UNIFORM-COST-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Depth-Limited-Search.md" target="_blank">DEPTH-LIMITED-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Recursive-Best-First-Search.md" target="_blank">RECURSIVE-BEST-FIRST-SEARCH</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Search**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/search.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/search.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/search.ipynb" download>Tải .ipynb</a>



#### **Bài tập**

##### Bài tập 3.1

Giải thích tại sao việc định nghĩa vấn đề (problem formulation) phải theo sau việc định nghĩa mục tiêu (goal formulation).


---

##### Bài tập 3.2

Đưa ra một problem formulation hoàn chỉnh cho mỗi bài toán sau đây.
Chọn một định nghĩa đủ chính xác để có thể triển khai được.<br>

1.  Có sáu hộp thủy tinh xếp thành một hàng, mỗi hộp có một ổ khóa. Mỗi hộp trong số
    năm hộp đầu tiên chứa một chiếc chìa khóa để mở hộp tiếp theo trong hàng; hộp
    cuối cùng chứa một quả chuối. Bạn có chìa khóa của hộp đầu tiên, và bạn
    muốn lấy quả chuối.<br>

2.  Bạn bắt đầu với chuỗi ABABAECCEC, hoặc nói chung là bất kỳ chuỗi nào
    được tạo từ A, B, C, và E. Bạn có thể biến đổi chuỗi này bằng cách sử dụng các
    đẳng thức sau: AC = E, AB = BC, BB = E, và E$x$ = $x$ đối với
    bất kỳ $x$ nào. Ví dụ, ABBC có thể được biến đổi thành AEC, và sau đó thành AC,
    và cuối cùng là E. Mục tiêu của bạn là tạo ra chuỗi E.<br>

3.  Có một lưới hình vuông kích thước $n \times n$, ban đầu mỗi ô vuông
    là sàn chưa sơn hoặc là một cái hố không đáy. Bạn bắt đầu đứng
    trên một ô sàn chưa sơn, và có thể chọn sơn ô vuông dưới chân
    bạn hoặc di chuyển sang một ô sàn chưa sơn liền kề. Bạn muốn
    toàn bộ sàn được sơn.<br>

4.  Một tàu chở container đang ở cảng, chất đầy các container. Có 13
    hàng container, mỗi hàng rộng 13 container và cao 5 container.
    Bạn điều khiển một cần cẩu có thể di chuyển đến bất kỳ vị trí nào phía trên con tàu,
    nhấc container bên dưới nó lên, và di chuyển nó lên bến tàu. Bạn muốn
    con tàu được dỡ hàng.


---

##### Bài tập 3.3

Mục tiêu của bạn là điều hướng một rô-bốt ra khỏi mê cung. Rô-bốt bắt đầu ở
trung tâm của mê cung và quay mặt về hướng bắc. Bạn có thể quay rô-bốt để đối mặt với hướng bắc,
đông, nam, hoặc tây. Bạn có thể chỉ định rô-bốt di chuyển về phía trước một khoảng cách
nhất định, mặc dù nó sẽ dừng lại trước khi đâm vào một bức tường.<br>

1.  Formulate (định nghĩa) bài toán này. Kích thước của state space (không gian trạng thái) là bao nhiêu?<br>

2.  Trong việc điều hướng một mê cung, nơi duy nhất chúng ta cần rẽ là tại điểm
    giao nhau của hai hoặc nhiều hành lang. Hãy định nghĩa lại bài toán này
    dựa trên quan sát này. Kích thước của state space bây giờ là bao nhiêu?<br>

3.  Từ mỗi điểm trong mê cung, chúng ta có thể di chuyển theo bất kỳ hướng nào trong số bốn
    hướng cho đến khi chúng ta đạt đến một điểm rẽ, và đây là
    hành động duy nhất chúng ta cần làm. Hãy định nghĩa lại bài toán sử dụng các hành động này.
    Bây giờ chúng ta có cần theo dõi hướng của rô-bốt không?<br>

4.  Trong mô tả ban đầu của chúng ta về bài toán, chúng ta đã trừu tượng hóa khỏi
    thế giới thực, hạn chế các action (hành động) và loại bỏ các chi tiết. Hãy liệt kê ba
    sự đơn giản hóa như vậy mà chúng ta đã thực hiện.<br>


---

##### Bài tập 3.4

Bạn có một lưới các ô vuông $9 \times 9$, mỗi ô có thể được tô màu
đỏ hoặc xanh lam. Ban đầu, lưới được tô toàn bộ màu xanh lam, nhưng bạn có thể thay đổi
màu của bất kỳ ô vuông nào một số lần bất kỳ. Tưởng tượng rằng lưới được chia
thành chín lưới con $3 \times 3$, bạn muốn mỗi lưới con chỉ có một
màu duy nhất nhưng các lưới con lân cận nhau phải có màu khác nhau.<br>

1.  Formulate bài toán này theo một cách đơn giản. Tính toán kích thước
    của state space.<br>

2.  Bạn chỉ cần tô màu một ô vuông một lần duy nhất. Hãy định nghĩa lại, và tính toán kích thước
    của state space. Liệu thuật toán breadth-first graph search có hoạt động nhanh hơn
    trên bài toán này so với bài toán ở phần (a) không? Còn đối với iterative
    deepening tree search thì sao?<br>

3.  Với mục tiêu đã cho, chúng ta chỉ cần xem xét các cách tô màu mà mỗi
    lưới con được tô đồng màu. Hãy định nghĩa lại bài toán và tính toán
    kích thước của state space.<br>

4.  Bài toán này có bao nhiêu giải pháp (solutions)?<br>

5.  Các phần (b) và (c) đã lần lượt trừu tượng hóa bài toán ban đầu (a).
    Bạn có thể đưa ra một phép biến đổi từ các giải pháp trong bài toán (c) sang
    các giải pháp trong bài toán (b), và từ các giải pháp trong bài toán (b) sang
    các giải pháp cho bài toán (a) không?<br>


---

##### Bài tập 3.5

Giả sử hai người bạn sống ở các thành phố khác nhau trên
một bản đồ, chẳng hạn như bản đồ Romania. Ở mỗi lượt, chúng ta có thể
đồng thời di chuyển mỗi người bạn đến một thành phố lân cận trên bản đồ.
Lượng thời gian cần thiết để di chuyển từ thành phố $i$ đến thành phố lân cận $j$ bằng với
khoảng cách đường bộ $d(i,j)$ giữa hai thành phố, nhưng ở mỗi lượt, người
bạn đến trước phải đợi cho đến khi người kia đến (và
gọi cho người đến trước qua điện thoại di động) trước khi lượt tiếp theo có thể bắt đầu.
Chúng ta muốn hai người bạn gặp nhau càng nhanh càng tốt.<br>

1.  Viết một problem formulation chi tiết cho search problem này. (Bạn sẽ thấy
    hữu ích khi định nghĩa một số ký hiệu hình thức ở đây.)<br>

2.  Giả sử $D(i,j)$ là khoảng cách đường thẳng giữa các thành phố $i$ và
    $j$. Hàm heuristic nào sau đây là admissible? (i)
    $D(i,j)$; (ii) $2\cdot D(i,j)$; (iii) $D(i,j)/2$. <br>

3.  Có tồn tại các bản đồ được kết nối hoàn toàn mà không có giải pháp nào không? <br>

4.  Có tồn tại các bản đồ mà mọi giải pháp đều yêu cầu một người bạn đến thăm
    cùng một thành phố hai lần không?


---

##### Bài tập 3.6

Hãy chứng minh rằng các state (trạng thái) của trò chơi 8-puzzle được chia
thành hai tập rời rạc, sao cho bất kỳ state nào cũng có thể đạt được từ bất kỳ
state nào khác trong cùng một tập hợp, trong khi không có state nào có thể đạt được từ bất kỳ state nào trong
tập hợp còn lại. (<i>Gợi ý:</i> Xem <a class="paperRef" title="" href="#">Berlekamp+al:1982</a>). Thiết kế một thủ tục để quyết định
xem một state cho trước nằm trong tập hợp nào, và giải thích tại sao điều này lại hữu ích cho
việc tạo ra các state ngẫu nhiên.


---

##### Bài tập 3.7

Hãy xem xét bài toán $n$-queens bằng cách sử dụng
problem formulation gia tăng "hiệu quả" được đưa ra trên trang <a class="pageRef" title="" href="#">nqueens-page</a>. Hãy giải thích tại sao state
space có ít nhất $\sqrt[3]{n!}$ states và ước tính giá trị $n$ lớn nhất
mà việc khám phá toàn diện (exhaustive exploration) là khả thi. (<i>Gợi ý</i>:
Suy ra giới hạn dưới của branching factor bằng cách xem xét số ô
tối đa mà một quân hậu có thể tấn công trong bất kỳ cột nào.)


---

##### Bài tập 3.8

Đưa ra một problem formulation hoàn chỉnh cho mỗi bài toán sau đây. Chọn một
formulation đủ chính xác để có thể thực thi được.<br>

1.  Chỉ sử dụng bốn màu, bạn phải tô màu một bản đồ phẳng sao cho
    không có hai vùng liền kề nào có cùng màu.<br>

2.  Một con khỉ cao 3 foot đang ở trong một căn phòng nơi một số quả chuối bị treo
    trên trần nhà cao 8 foot. Nó muốn lấy quả chuối. Căn phòng
    chứa hai chiếc thùng cao 3 foot có thể xếp chồng lên nhau, di chuyển được, và có thể leo lên được.<br>

3.  Bạn có một chương trình xuất ra thông báo "bản ghi đầu vào bất hợp pháp"
    khi được nạp một tệp tin chứa các bản ghi đầu vào nhất định. Bạn biết rằng việc xử lý
    của mỗi bản ghi là độc lập với các bản ghi khác. Bạn muốn
    khám phá xem bản ghi nào là bất hợp pháp.<br>

4.  Bạn có ba cái bình, có dung tích lần lượt là 12 gallon, 8 gallon, và 3 gallon,
    và một vòi nước. Bạn có thể đổ đầy các bình hoặc đổ hết nước từ bình
    này sang bình khác hoặc đổ xuống đất. Bạn cần đong ra chính xác
    một gallon.<br>


---

##### Bài tập 3.9

Hãy xem xét bài toán tìm path (đường đi) ngắn nhất
giữa hai điểm trên một mặt phẳng có các chướng ngại vật là đa giác lồi
như hình minh họa. Đây là một sự lý tưởng hóa của một bài toán mà rô-bốt phải
giải quyết để điều hướng trong một môi trường đông đúc.<br>

1.  Giả sử state space bao gồm tất cả các vị trí $(x,y)$ trên
    mặt phẳng. Có bao nhiêu state? Có bao nhiêu path để đi đến
    goal (mục tiêu)?<br>

2.  Giải thích ngắn gọn tại sao path ngắn nhất từ một đỉnh đa giác này đến bất kỳ
    đỉnh nào khác trong cảnh phải bao gồm các đoạn thẳng nối
    một số đỉnh của các đa giác. Hãy định nghĩa một state space tốt ngay bây giờ.
    Kích thước của state space này là bao nhiêu?<br>

3.  Định nghĩa các hàm cần thiết để thực hiện search problem này,
    bao gồm một hàm lấy đầu vào là một đỉnh và trả về một tập hợp
    các vectơ, mỗi vectơ ánh xạ đỉnh hiện tại đến một trong những
    đỉnh có thể tiếp cận được bằng một đường thẳng. (Đừng quên các
    đỉnh kề trên cùng một đa giác.) Sử dụng khoảng cách đường thẳng cho
    hàm heuristic.<br>

4.  Áp dụng một hoặc nhiều thuật toán trong chương này để giải quyết một loạt
    các bài toán trong miền này, và nhận xét về hiệu suất của chúng.<br>


---

##### Bài tập 3.10

Ở trang <a class="pageRef" title="" href="#">non-negative-g</a>, chúng ta đã nói rằng chúng ta sẽ không xem xét các bài toán
có chi phí đường đi (path costs) âm. Trong bài tập này, chúng ta sẽ khám phá quyết định này sâu hơn.<br>

1.  Giả sử rằng các action (hành động) có thể có chi phí âm lớn tùy ý;
    hãy giải thích tại sao khả năng này sẽ buộc bất kỳ thuật toán tối ưu nào cũng phải
    khám phá toàn bộ state space.<br>

2.  Việc chúng ta yêu cầu step costs (chi phí bước) phải lớn hơn hoặc
    bằng một hằng số âm $c$ nào đó có giúp ích gì không? Hãy xem xét đối với cả trees và graphs.<br>

3.  Giả sử rằng một tập hợp các action tạo thành một vòng lặp (loop) trong state space sao
    cho việc thực hiện tập hợp đó theo một thứ tự nhất định sẽ không làm thay đổi tổng thể
    state. Nếu tất cả các action này đều có chi phí âm, điều này
    ngụ ý gì về hành vi tối ưu cho một agent trong một
    môi trường như vậy?<br>

4.  Người ta có thể dễ dàng tưởng tượng ra những action có chi phí âm cao, ngay cả trong
    các miền như tìm kiếm tuyến đường. Ví dụ, một số đoạn đường
    có thể có phong cảnh đẹp đến mức vượt xa những
    chi phí thông thường về thời gian và nhiên liệu. Hãy giải thích, bằng các thuật ngữ chính xác, trong
    bối cảnh của state-space search, tại sao con người không lái xe vòng quanh
    các cung đường ngắm cảnh vô thời hạn, và giải thích cách định nghĩa state space
    và actions cho việc tìm đường để các artificial agents (tác tử nhân tạo) cũng có thể
    tránh được các vòng lặp.<br>

5.  Bạn có thể nghĩ ra một lĩnh vực thực tế nào mà trong đó step costs có thể
    gây ra các vòng lặp không?<br>


---

##### Bài tập 3.11

Bài toán thường được phát biểu như sau. Có ba
nhà truyền giáo và ba kẻ ăn thịt người ở một bên bờ sông, cùng với
một chiếc thuyền có thể chở một hoặc hai người. Tìm cách đưa tất cả mọi người sang
bờ bên kia mà không bao giờ để một nhóm nhà truyền giáo nào ở một nơi bị
áp đảo về số lượng bởi những kẻ ăn thịt người ở nơi đó. Bài toán này rất nổi tiếng trong AI
bởi vì nó là chủ đề của bài báo đầu tiên tiếp cận problem formulation
từ một góc nhìn phân tích <a href="#" class="paperRef" title="">Amarel:1968</a>. <br>

1.  Định nghĩa bài toán một cách chính xác, chỉ đưa ra những sự phân biệt
    cần thiết để đảm bảo có một giải pháp hợp lệ. Vẽ sơ đồ của toàn bộ
    state space.<br>

2.  Thực thi và giải quyết bài toán một cách tối ưu bằng cách sử dụng một thuật toán
    search (tìm kiếm) thích hợp. Việc kiểm tra các repeated states (trạng thái lặp) có phải là một ý kiến hay không? <br>

3.  Bạn nghĩ tại sao mọi người lại gặp khó khăn khi giải quyết câu đố này, mặc dù
    rằng state space là rất đơn giản? <br>


---

##### Bài tập 3.12

Định nghĩa theo ngôn ngữ của riêng bạn các thuật ngữ sau: state, state space, search
tree, search node, goal, action, transition model, và branching factor.


---

##### Bài tập 3.13

Sự khác biệt giữa world state (trạng thái thế giới), state description (mô tả trạng thái), và một
search node là gì? Tại sao sự khác biệt này lại hữu ích?


---

##### Bài tập 3.14

Một action như vậy thực sự bao gồm một chuỗi dài các action nhỏ hơn: bật xe, nhả phanh, tăng tốc về phía trước, v.v.
Việc có các composite actions (hành động tổng hợp) loại này làm giảm số bước trong một
chuỗi solution (giải pháp), do đó giảm thời gian search. Giả sử chúng ta áp dụng
điều này đến mức cực đoan logic, bằng cách tạo ra các siêu-hành động-tổng-hợp từ
mọi chuỗi hành động khả thi. Khi đó mỗi instance của bài toán được
giải quyết bởi một siêu-hành động-tổng-hợp duy nhất. Hãy giải thích xem
search sẽ hoạt động như thế nào trong cách định nghĩa này. Đây có phải là một cách tiếp cận thực tế để
tăng tốc độ giải quyết bài toán không?


---

##### Bài tập 3.15

Có phải một state space hữu hạn luôn dẫn đến một search tree hữu hạn không? Thế còn
một state space hữu hạn là một cây (tree) thì sao? Bạn có thể trình bày chính xác hơn về những
loại state spaces nào luôn dẫn đến search trees hữu hạn không? (Phỏng theo
, 1996.)


---

##### Bài tập 3.16

Hãy chứng minh rằng thỏa mãn
thuộc tính tách đồ thị được minh họa trong . (<i>Gợi ý</i>: Bắt đầu bằng cách
chỉ ra rằng thuộc tính này đúng lúc ban đầu, sau đó chỉ ra rằng nếu nó đúng
trước một lần lặp của thuật toán, nó cũng sẽ đúng sau đó.) Mô tả một
thuật toán search vi phạm thuộc tính này.


---

##### Bài tập 3.17

Những câu nào sau đây là đúng và câu nào là sai? Giải thích các
câu trả lời của bạn.<br>

1.  Thuật toán Depth-first search (tìm kiếm theo chiều sâu) luôn duyệt (expands) số lượng nodes ít nhất bằng với thuật toán A search
    với một admissible heuristic. <br>

2.  $h(n)=0$ là một admissible heuristic đối với trò chơi 8-puzzle. <br>

3.  A không có tác dụng trong robotics vì các percepts (nhận thức), states, và actions
    đều liên tục.<br>

4.  Breadth-first search là complete (hoàn chỉnh) ngay cả khi chi phí mỗi bước bằng không (zero step costs)
    được cho phép. <br>

5.  Giả sử rằng một quân xe có thể di chuyển trên bàn cờ vua với một số lượng ô vuông bất kỳ theo
    một đường thẳng, dọc hoặc ngang, nhưng không thể nhảy qua
    các quân cờ khác. Khoảng cách Manhattan là một admissible heuristic cho
    bài toán di chuyển quân xe từ ô A sang ô B với số lần di chuyển
    ít nhất.<br>


---

##### Bài tập 3.18

Hãy xem xét một state space mà state bắt đầu là số 1 và mỗi state
$k$ có hai state kế tiếp: các số $2k$ và $2k+1$. <br>

1.  Vẽ một phần của state space cho các states từ 1 đến 15. <br>

2.  Giả sử goal state là 11. Liệt kê thứ tự mà các nodes sẽ được
    truy cập đối với thuật toán breadth-first search, depth-limited search (có giới hạn độ sâu là 3),
    và iterative deepening search. <br>

3.  Thuật toán bidirectional search sẽ hoạt động tốt như thế nào đối với bài toán này? Branching factor
    trong mỗi hướng của thuật toán bidirectional search là bao nhiêu?<br>

4.  Câu trả lời cho (c) có gợi ý về một cách định nghĩa lại bài toán
    cho phép bạn giải quyết bài toán đi từ state 1 đến một
    goal state nhất định mà hầu như không cần phải search không? <br>

5.  Gọi action đi từ $k$ đến $2k$ là Trái (Left), và action đi đến
    $2k+1$ là Phải (Right). Bạn có thể tìm thấy một thuật toán xuất ra solution cho
    bài toán này mà không cần thực hiện bất kỳ thuật toán search nào không?


---

##### Bài tập 3.19

Một bộ xe lửa đồ chơi bằng gỗ cơ bản chứa các mảnh ghép như được hiển thị trong
hình minh họa. Nhiệm vụ là kết nối các mảnh này thành một đường ray không có
các đoạn đường ray chồng chéo lên nhau và không có các đầu nối lỏng lẻo nơi một đoàn tàu có thể trật bánh rơi xuống
sàn nhà.<br>

1.  Giả sử rằng các mảnh ghép khớp với nhau một cách <i>chính xác</i> không có
    khe hở. Hãy đưa ra một problem formulation chính xác cho nhiệm vụ này như một search problem.<br>

2.  Xác định một thuật toán uninformed search (tìm kiếm mù) phù hợp cho nhiệm vụ này và
    giải thích sự lựa chọn của bạn.<br>

3.  Giải thích tại sao việc loại bỏ bất kỳ mảnh "ngã ba" ("fork") nào lại khiến cho
    bài toán không thể giải quyết được. <br>

4.  Đưa ra một giới hạn trên cho tổng kích thước của state space được định nghĩa bởi
    problem formulation của bạn. (<i>Gợi ý</i>: hãy nghĩ về giá trị lớn nhất của
    branching factor cho quá trình lắp ráp và độ sâu tối đa (maximum depth),
    bỏ qua vấn đề về các mảnh ghép chồng chéo và các đầu nối lỏng lẻo. Hãy bắt đầu bằng cách
    giả vờ rằng mỗi mảnh ghép đều là duy nhất.)


---

##### Bài tập 3.20

Triển khai hai phiên bản của hàm cho trò chơi 8-puzzle: một phiên bản sao chép
và chỉnh sửa cấu trúc dữ liệu cho parent node $s$ và một phiên bản
trực tiếp thay đổi parent state (hoàn tác các thay đổi khi
cần). Viết các phiên bản của thuật toán iterative deepening depth-first search
sử dụng các hàm này và so sánh hiệu suất của chúng.


---

##### Bài tập 3.21

Ở trang <a class="pageRef" title="" href="#">iterative-lengthening-page</a>,
chúng ta đã đề cập đến thuật toán <b>iterative lengthening search</b>,
một dạng lặp (iterative) tương tự của thuật toán uniform cost search. Ý tưởng là sử dụng các giới hạn tăng dần cho
path cost (chi phí đường đi). Nếu một node được tạo ra mà path cost của nó vượt quá giới hạn
hiện tại, nó ngay lập tức bị loại bỏ. Đối với mỗi vòng lặp mới, giới hạn được
đặt bằng với path cost thấp nhất của bất kỳ node nào bị loại bỏ trong vòng lặp
trước đó.<br>

1.  Hãy chứng minh rằng thuật toán này là tối ưu (optimal) đối với các path costs tổng quát.<br>

2.  Hãy xem xét một cây đồng nhất (uniform tree) với branching factor $b$, độ sâu giải pháp
    (solution depth) $d$, và step costs bằng đơn vị. Iterative
    lengthening sẽ yêu cầu bao nhiêu vòng lặp?<br>

3.  Bây giờ hãy xem xét các step costs được lấy từ phạm vi liên tục
    $[\epsilon,1]$, trong đó $0 < \epsilon < 1$. Cần bao nhiêu vòng lặp
    trong trường hợp xấu nhất? <br>

4.  Thực thi thuật toán và áp dụng nó vào các instance của trò chơi 8-puzzle
    và bài toán người bán hàng đi dạo (traveling salesperson). So sánh hiệu suất của thuật toán
    với thuật toán uniform-cost search, và nhận xét về
    kết quả của bạn. <br>


---

##### Bài tập 3.22

Mô tả một state space trong đó thuật toán iterative deepening search có hiệu suất tệ hơn nhiều
so với thuật toán depth-first search (ví dụ: $O(n^{2})$ so với $O(n)$).


---

##### Bài tập 3.23

Viết một chương trình lấy đầu vào là hai URL của trang web và tìm một
path của các liên kết từ trang này sang trang kia. Đâu là một chiến lược search thích hợp? Thuật toán bidirectional search có phải là một ý kiến hay không? Một công cụ search có thể được
sử dụng để thực thi một hàm predecessor không?


---

##### Bài tập 3.24

Hãy xem xét bài toán vacuum-world (thế giới máy hút bụi) được định nghĩa trong tài liệu.<br>

1.  Những thuật toán nào được định nghĩa trong chương này sẽ thích hợp
    cho bài toán này? Thuật toán nên sử dụng tree search hay graph
    search?<br>

2.  Áp dụng thuật toán bạn đã chọn để tính toán một chuỗi tối ưu các
    action cho một thế giới $3\times 3$ có state ban đầu là có bụi bẩn ở
    ba ô vuông trên cùng và agent (tác tử) ở trung tâm.<br>

3.  Xây dựng một search agent cho vacuum world, và đánh giá hiệu suất của nó
    trong một tập hợp các thế giới $3\times 3$ với xác suất là 0.2 có
    bụi bẩn ở mỗi ô vuông. Đưa search cost (chi phí tìm kiếm) cũng như path cost (chi phí đường đi) vào
    thước đo hiệu suất, sử dụng một tỷ giá hối đoái hợp lý.<br>

4.  So sánh search agent tốt nhất của bạn với một randomized reflex agent (tác tử phản xạ ngẫu nhiên) đơn giản
    có chức năng hút nếu có bụi bẩn và ngược lại di chuyển một cách ngẫu nhiên.<br>

5.  Hãy xem xét điều gì sẽ xảy ra nếu thế giới được mở rộng thành
    $n \times n$. Hiệu suất của search agent và của
    reflex agent thay đổi như thế nào theo $n$? <br>


---

##### Bài tập 3.25

Chứng minh mỗi nhận định sau đây,
hoặc đưa ra một phản ví dụ (counterexample): <br>

1.  Breadth-first search là một trường hợp đặc biệt của uniform-cost search.<br>

2.  Depth-first search là một trường hợp đặc biệt của best-first tree search.<br>

3.  Uniform-cost search là một trường hợp đặc biệt của A search.<br>


---

##### Bài tập 3.26

So sánh hiệu suất của A và RBFS trên một tập hợp các bài toán
được tạo ngẫu nhiên trong các miền 8-puzzle (với khoảng cách Manhattan) và TSP (với MST—xem
tài liệu). Thảo luận về kết quả của bạn. Điều gì xảy ra với hiệu suất của RBFS
khi một số ngẫu nhiên nhỏ được thêm vào các giá trị heuristic trong miền
8-puzzle?


---

##### Bài tập 3.27

Theo dõi hoạt động của thuật toán A search được áp dụng cho bài toán đi đến
Bucharest từ Lugoj bằng cách sử dụng heuristic là khoảng cách đường thẳng. Tức là,
hãy hiển thị chuỗi các nodes mà thuật toán sẽ xem xét và các điểm số
$f$, $g$, và $h$ cho mỗi node.


---

##### Bài tập 3.28

Đôi khi không có một hàm đánh giá (evaluation function) tốt cho một bài toán nhưng lại có
một phương pháp so sánh tốt: một cách để cho biết một node có tốt hơn
node khác hay không mà không cần gán giá trị số cho cả hai. Chứng minh rằng
điều này là đủ để thực hiện một thuật toán best-first search. Có một phiên bản tương tự của thuật toán A cho
thiết lập này không?


---

##### Bài tập 3.29

Thiết kế một state space trong đó thuật toán A sử dụng trả về một
solution không tối ưu với một hàm $h(n)$ mà nó là admissible nhưng
không nhất quán (inconsistent).


---

##### Bài tập 3.30

Các heuristics chính xác không nhất thiết làm giảm thời gian search trong trường hợp xấu
nhất. Cho một độ sâu $d$ bất kỳ, hãy định nghĩa một search problem có goal node ở
độ sâu $d$, và viết một hàm heuristic sao cho $|h(n) - h^\*(n)|  \le O(\log h^\*(n))$ nhưng $A^*$ lại truy cập tất cả các nodes có độ sâu nhỏ
hơn $d$.


---

##### Bài tập 3.31

Thuật toán <b>heuristic path algorithm</b> <a class="paperRef" title="" href="#">Pohl:1977</a> là một thuật toán best-first search trong đó hàm đánh giá
là $f(n) = (2-w)g(n) + wh(n)$. Thuật toán này complete (hoàn chỉnh) đối với những giá trị nào của $w$? Nó tối ưu
đối với những giá trị nào, giả sử rằng $h$ là admissible? Thuật toán này thực hiện loại
search nào đối với $w=0$, $w=1$, và $w=2$?


---

##### Bài tập 3.32

Hãy xem xét phiên bản không giới hạn (unbounded) của một lưới 2D thông thường như trong hình minh họa. State
bắt đầu ở gốc tọa độ, (0,0), và goal state ở $(x,y)$.<br>

1.  Branching factor $b$ trong state space này là gì?<br>

2.  Có bao nhiêu state riêng biệt ở độ sâu $k$ (với $k>0$)?<br>

3.  Số lượng node tối đa được truy cập (expanded) bởi thuật toán breadth-first tree
    search là bao nhiêu?<br>

4.  Số lượng node tối đa được truy cập (expanded) bởi thuật toán breadth-first graph
    search là bao nhiêu?<br>

5.  $h = |u-x| + |v-y|$ có phải là một admissible heuristic đối với một state ở vị trí
    $(u,v)$ không? Giải thích.<br>

6.  Có bao nhiêu node được truy cập bởi thuật toán A graph search sử dụng $h$?<br>

7.  Liệu $h$ có còn admissible nếu một số liên kết (links) bị loại bỏ không?<br>

8.  Liệu $h$ có còn admissible nếu một số liên kết (links) được thêm vào giữa các
    state không liền kề nhau không?


---

##### Bài tập 3.33

$n$ phương tiện chiếm các ô từ $(1,1)$ đến $(n,1)$ (tức là, hàng
dưới cùng) của một lưới $n\times n$. Các phương tiện phải được di chuyển lên hàng trên cùng
nhưng theo thứ tự ngược lại; do đó phương tiện $i$ bắt đầu ở $(i,1)$ phải kết thúc
ở $(n-i+1,n)$. Ở mỗi bước thời gian, mỗi phương tiện trong số $n$ phương tiện có thể
di chuyển một ô lên, xuống, trái, hoặc phải, hoặc đứng yên; nhưng nếu một phương tiện
đứng yên, một phương tiện lân cận khác (nhưng không nhiều hơn một) có thể nhảy
qua nó. Hai phương tiện không thể chiếm cùng một ô. <br>

1.  Tính kích thước của state space như là một hàm của $n$.<br>

2.  Tính branching factor như là một hàm của $n$.<br>

3.  Giả sử rằng phương tiện $i$ đang ở vị trí $(x_i,y_i)$; hãy viết một
    admissible heuristic $h_i$ không tầm thường (nontrivial) cho số lần di chuyển mà nó sẽ cần
    để đi đến vị trí goal của nó $(n-i+1,n)$, giả sử không có phương tiện nào khác
    nằm trên lưới.<br>

4.  Hàm heuristic nào sau đây là admissible đối với bài toán
    di chuyển tất cả $n$ phương tiện đến điểm đến của chúng? Giải thích.<br>

    1.  $\sum_{i= 1}^{n} h_i$.<br>

    2.  $\max\{h_1,\ldots,h_n\}$.<br>

    3.  $\min\{h_1,\ldots,h_n\}$.<br>


---

##### Bài tập 3.34

Hãy xem xét bài toán di chuyển $k$ quân mã từ $k$ ô xuất phát
$s_1,\ldots,s_k$ đến $k$ ô mục tiêu $g_1,\ldots,g_k$, trên một bàn cờ vua
không giới hạn, tuân theo quy tắc rằng không có hai quân mã nào có thể đáp xuống cùng một
ô vuông cùng một lúc. Mỗi action bao gồm việc di chuyển <i>tối đa</i> $k$ quân mã đồng thời. Chúng ta muốn hoàn thành
quá trình này với số lượng actions ít nhất.<br>

1.  Branching factor tối đa trong state space này là gì, được biểu thị
    như là một hàm của $k$?<br>

2.  Giả sử $h_i$ là một admissible heuristic cho bài toán di chuyển tự bản thân
    quân mã $i$ đến goal $g_i$. Hàm heuristic nào sau đây là admissible đối với bài toán $k$-quân mã? Trong số đó,
    hàm nào là tốt nhất?<br>

    1.  $\min\{h_1,\ldots,h_k\}$.<br>

    2.  $\max\{h_1,\ldots,h_k\}$.<br>

    3.  $\sum_{i= 1}^{k} h_i$.<br>

3.  Lặp lại câu (b) cho trường hợp bạn chỉ được phép di chuyển một
    quân mã tại một thời điểm.


---

##### Bài tập 3.35

Chúng ta đã thấy trên trang <a class="pageRef" title="" href="#">I-to-F</a> rằng heuristic khoảng cách đường thẳng dẫn thuật toán greedy
best-first search đi sai hướng trong bài toán đi từ Iasi đến Fagaras.
Tuy nhiên, heuristic này lại hoàn hảo cho bài toán ngược lại: đi từ
Fagaras đến Iasi. Có những bài toán nào mà heuristic này
gây hiểu lầm ở cả hai hướng không?


---

##### Bài tập 3.36

Phát minh ra một hàm heuristic cho trò chơi 8-puzzle đôi khi đánh giá
cao hơn thực tế (overestimates), và chỉ ra cách mà nó có thể dẫn đến một solution không tối ưu trên một
bài toán cụ thể. (Bạn có thể sử dụng máy tính để trợ giúp nếu muốn.) Hãy chứng minh
rằng nếu $h$ không bao giờ đánh giá quá mức (overestimates) hơn $c$, thuật toán A sử dụng $h$ sẽ trả về một
solution có chi phí vượt quá solution tối ưu không lớn hơn
$c$.


---

##### Bài tập 3.37

Hãy chứng minh rằng nếu một heuristic là
nhất quán (consistent), thì nó phải admissible. Hãy xây dựng một admissible heuristic
mà nó không nhất quán (not consistent).


---

##### Bài tập 3.38

Bài toán người bán hàng đi dạo (TSP) có thể được
giải quyết với heuristic cây khung nhỏ nhất (minimum-spanning-tree - MST), công cụ dùng để ước tính
chi phí hoàn thành một chuyến đi, giả sử rằng một phần của chuyến đi đã
được xây dựng xong. MST cost của một tập hợp các thành phố là tổng nhỏ nhất của
các path costs của bất kỳ cây nào kết nối tất cả các thành phố.<br>

1.  Chỉ ra cách mà heuristic này có thể được rút ra từ một phiên bản được nới lỏng (relaxed version) của
    TSP.<br>

2.  Chứng minh rằng heuristic MST chiếm ưu thế (dominates) hơn khoảng cách đường thẳng.<br>

3.  Viết một trình tạo bài toán cho các instance của TSP trong đó các thành phố được
    biểu diễn bằng các điểm ngẫu nhiên trong một ô vuông đơn vị.<br>

4.  Tìm một thuật toán hiệu quả trong tài liệu để xây dựng
    MST, và sử dụng nó với thuật toán A graph search để giải quyết các instances của TSP.


---

##### Bài tập 3.39

Trên trang <a class="pageRef" title="" href="#">Gaschnig-h-page</a> , chúng ta đã định nghĩa phiên bản nới lỏng của trò chơi 8-puzzle trong
đó một ô gạch có thể di chuyển từ ô A sang ô B nếu B là ô trống. Giải pháp chính xác
cho bài toán này định nghĩa <b>Gaschnig's heuristic</b> <a class="paperRef" title="" href="#">Gaschnig:1979</a>. Giải thích tại sao
heuristic của Gaschnig ít nhất là chính xác bằng với $h_1$ (các ô gạch đặt sai vị trí - misplaced tiles), và đưa ra các
trường hợp mà nó chính xác hơn cả $h_1$ và $h_2$ (khoảng cách Manhattan - Manhattan
distance). Giải thích cách tính toán heuristic của Gaschnig một cách hiệu quả.


---

##### Bài tập 3.40

Chúng ta đã đưa ra hai heuristics đơn giản cho trò chơi 8-puzzle: khoảng cách Manhattan và
các ô gạch sai vị trí (misplaced tiles). Một vài heuristics trong các tài liệu nhằm mục đích cải thiện
điều này — ví dụ, xem <a class="paperRef" title="" href="#">Nilsson:1971</a>,
<a class="paperRef" title="" href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.75.3333&rep=rep1&type=pdf">Mostow+Prieditis:1989</a>, và <a href="https://europepmc.org/abstract/med/1534722" title="" class="paperRef">Hansson+al:1992</a>. Kiểm tra những tuyên bố này bằng cách thực thi
các heuristics và so sánh hiệu suất của các thuật toán
tạo ra được.


---


<!-- tabs:end -->
