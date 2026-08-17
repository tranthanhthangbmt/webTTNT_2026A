# Chapter 06 Adversarial Search And Games

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_06/chapter_06_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_06_Adversarial%20Search%20And%20Games.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter06_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter06/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/AC-3.md" target="_blank">AC-3</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Backtracking-Search.md" target="_blank">BACKTRACKING-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Min-Conflicts.md" target="_blank">MIN-CONFLICTS</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Tree-CSP-Solver.md" target="_blank">TREE-CSP-SOLVER</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Games**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/games.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/games.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/games.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 6.1

Có bao nhiêu nghiệm cho bài toán tô màu bản đồ trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/australia-figure.png">australia-figure</a>? Có bao nhiêu nghiệm nếu cho phép bốn màu? Hai màu?


---

##### Bài tập 6.2

Xem xét bài toán đặt $k$ quân mã trên bàn cờ $n\times n$ sao cho không có hai quân mã nào tấn công lẫn nhau, với $k$ được cho trước và $k\leq n^2$.<br>

1.  Chọn một công thức CSP. Trong công thức của bạn, các biến là gì?<br>

2.  Các giá trị có thể có của mỗi biến là gì?<br>

3.  Những tập hợp biến nào bị ràng buộc, và bằng cách nào?<br>

4.  Bây giờ hãy xem xét bài toán đặt *càng nhiều quân mã càng tốt* trên bàn cờ mà không có bất kỳ cuộc tấn công nào. Giải thích cách giải bài toán này bằng local search bằng cách định nghĩa các hàm ACTIONS và RESULT phù hợp và một hàm mục tiêu hợp lý.<br>


---

##### Bài tập 6.3

Xem xét bài toán <a href="#footnote1">xây dựng</a> (không phải giải) các câu đố ô chữ bằng cách khớp các từ vào một lưới hình chữ nhật. Lưới, được cung cấp như một phần của bài toán, chỉ định ô nào trống và ô nào bị tô bóng. Giả sử rằng một danh sách các từ (tức là một từ điển) được cung cấp và nhiệm vụ là điền vào các ô trống bằng cách sử dụng bất kỳ tập con nào của danh sách. Hãy định nghĩa chính xác bài toán này theo hai cách:<br>

1.  Dưới dạng một bài toán search tổng quát. Chọn một thuật toán search phù hợp và chỉ định một hàm heuristic. Việc điền vào các ô trống từng chữ cái hay từng từ một sẽ tốt hơn?<br>

2.  Dưới dạng một bài toán constraint satisfaction. Các biến nên là từ hay chữ cái?<br>

Bạn nghĩ công thức nào sẽ tốt hơn? Tại sao?<br>


---

##### Bài tập 6.4

Đưa ra các công thức chính xác cho mỗi bài toán sau đây dưới dạng bài toán constraint satisfaction:<br>

1.  Rectilinear floor-planning: tìm các vị trí không chồng lấn trong một hình chữ nhật lớn cho một số hình chữ nhật nhỏ hơn.<br>

2.  Lập lịch lớp học: có một số lượng cố định các giáo sư và phòng học, một danh sách các lớp học sẽ được cung cấp và một danh sách các khung giờ có thể có cho các lớp học. Mỗi giáo sư có một tập hợp các lớp học mà họ có thể dạy.<br>

3.  Hamiltonian tour: cho một mạng lưới các thành phố được kết nối bằng đường bộ, chọn một thứ tự để ghé thăm tất cả các thành phố trong một quốc gia mà không lặp lại bất kỳ thành phố nào.<br>


---

##### Bài tập 6.5

Giải bài toán cryptarithmetic trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/cryptarithmetic-figure.png">cryptarithmetic-figure</a> bằng tay, sử dụng chiến lược backtracking với forward checking và các heuristic MRV và least-constraining-value.


---

##### Bài tập 6.6

Chỉ ra cách một ràng buộc ternary duy nhất như “$A + B = C$” có thể được chuyển đổi thành ba ràng buộc nhị phân bằng cách sử dụng một biến phụ trợ. Bạn có thể giả định các miền hữu hạn. (*Gợi ý:* Xem xét một biến mới nhận các giá trị là các cặp của các giá trị khác, và xem xét các ràng buộc như “$X$ là phần tử đầu tiên của cặp $Y$.”) Tiếp theo, chỉ ra cách các ràng buộc có nhiều hơn ba biến có thể được xử lý tương tự. Cuối cùng, chỉ ra cách các ràng buộc đơn có thể được loại bỏ bằng cách thay đổi các miền của biến. Điều này hoàn thành việc chứng minh rằng bất kỳ CSP nào cũng có thể được chuyển đổi thành một CSP chỉ với các ràng buộc nhị phân.


---

##### Bài tập 6.7

Xem xét câu đố logic sau: Trong năm ngôi nhà, mỗi ngôi nhà có một màu khác nhau, sống năm người thuộc các quốc tịch khác nhau, mỗi người thích một thương hiệu kẹo khác nhau, một loại đồ uống khác nhau và một con vật cưng khác nhau. Dựa trên các sự kiện sau, các câu hỏi cần trả lời là “Con ngựa vằn sống ở đâu, và họ uống nước trong ngôi nhà nào?”<br>

Người Anh sống trong ngôi nhà màu đỏ.<br>

Người Tây Ban Nha sở hữu con chó.<br>

Người Na Uy sống trong ngôi nhà đầu tiên bên trái.<br>

Ngôi nhà màu xanh lá cây nằm ngay bên phải ngôi nhà màu ngà.<br>

Người ăn kẹo Hershey sống trong ngôi nhà bên cạnh người có con cáo.<br>

Kẹo Kit Kats được ăn trong ngôi nhà màu vàng.<br>

Người Na Uy sống cạnh ngôi nhà màu xanh lam.<br>

Người ăn kẹo Smarties sở hữu ốc sên.<br>

Người ăn kẹo Snickers uống nước cam.<br>

Người Ukraine uống trà.<br>

Người Nhật ăn kẹo Milky Ways.<br>

Kẹo Kit Kats được ăn trong một ngôi nhà cạnh ngôi nhà có con ngựa.<br>

Cà phê được uống trong ngôi nhà màu xanh lá cây.<br>

Sữa được uống trong ngôi nhà giữa.<br>

Thảo luận về các biểu diễn khác nhau của bài toán này dưới dạng CSP. Tại sao lại ưu tiên biểu diễn này hơn biểu diễn khác?


---

##### Bài tập 6.8

Xem xét đồ thị có 8 nút $A_1$, $A_2$, $A_3$, $A_4$, $H$, $T$, $F_1$, $F_2$. $A_i$ được nối với $A_{i+1}$ cho mọi $i$, mỗi $A_i$ được nối với $H$, $H$ được nối với $T$, và $T$ được nối với mỗi $F_i$. Tìm một phép tô màu 3 màu cho đồ thị này bằng tay bằng cách sử dụng chiến lược sau: backtracking với conflict-directed backjumping, thứ tự biến $A_1$, $H$, $A_4$, $F_1$, $A_2$, $F_2$, $A_3$, $T$, và thứ tự giá trị $R$, $G$, $B$.


---

##### Bài tập 6.9

Giải thích tại sao việc chọn biến *bị ràng buộc nhất* nhưng giá trị *ít ràng buộc nhất* trong một CSP search lại là một heuristic tốt.


---

##### Bài tập 6.10

Tạo các trường hợp ngẫu nhiên của bài toán tô màu bản đồ như sau: rải $n$ điểm trên hình vuông đơn vị; chọn ngẫu nhiên một điểm $X$, nối $X$ bằng một đường thẳng đến điểm gần nhất $Y$ sao cho $X$ chưa được nối với $Y$ và đường thẳng không cắt bất kỳ đường thẳng nào khác; lặp lại bước trước cho đến khi không còn kết nối nào có thể thực hiện được. Các điểm đại diện cho các vùng trên bản đồ và các đường thẳng nối các vùng lân cận. Bây giờ hãy thử tìm các phép tô màu $k$ màu cho mỗi bản đồ, cho cả $k3$ và $k4$, bằng cách sử dụng min-conflicts, backtracking, backtracking với forward checking và backtracking với MAC. Lập một bảng thời gian chạy trung bình cho mỗi thuật toán với các giá trị của $n$ cho đến giá trị lớn nhất bạn có thể thực hiện được. Nhận xét về kết quả của bạn.


---

##### Bài tập 6.11

Sử dụng thuật toán AC-3 để chứng minh rằng arc consistency có thể phát hiện sự không nhất quán của phép gán một phần
${{WA}}{green},V{red}$ cho bài toán được hiển thị trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/australia-figure.png">australia-figure</a>.


---

##### Bài tập 6.12

Sử dụng thuật toán AC-3 để chứng minh rằng arc consistency có thể phát hiện sự không nhất quán của phép gán một phần
${{WA}}{red},V{blue}$ cho bài toán được hiển thị trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/australia-figure.png">australia-figure</a>.


---

##### Bài tập 6.13

Độ phức tạp trường hợp xấu nhất khi chạy AC-3 trên một CSP có cấu trúc cây là bao nhiêu?


---

##### Bài tập 6.14

AC-3 đưa trở lại hàng đợi *mọi* cung ($X_{k}, X_{i}$) bất cứ khi nào *bất kỳ* giá trị nào bị xóa khỏi miền của $X_{i}$, ngay cả khi mỗi giá trị của $X_{k}$ nhất quán với nhiều giá trị còn lại của $X_{i}$. Giả sử rằng, đối với mọi cung ($X_{k}, X_{i}$), chúng ta theo dõi số lượng các giá trị còn lại của $X_{i}$ nhất quán với mỗi giá trị của $X_{k}$. Giải thích cách cập nhật các số này một cách hiệu quả và do đó chứng minh rằng arc consistency có thể được thực thi trong tổng thời gian $O(n^2d^2)$.


---

##### Bài tập 6.15

Thuật toán Tree-CSP-Solver (Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/tree-csp-figure.png">tree-csp-figure</a>) làm cho các cung nhất quán bắt đầu từ các lá và làm việc ngược về phía gốc. Tại sao nó lại làm như vậy? Điều gì sẽ xảy ra nếu nó đi theo hướng ngược lại?


---

##### Bài tập 6.16

Chúng ta đã giới thiệu Sudoku như một CSP để giải bằng search trên các phép gán một phần vì đó là cách mọi người thường giải Sudoku. Tất nhiên, cũng có thể tấn công các bài toán này bằng local search trên các phép gán hoàn chỉnh. Một solver cục bộ sử dụng heuristic min-conflicts sẽ hoạt động tốt như thế nào trên các bài toán Sudoku?


---

##### Bài tập 6.17

Định nghĩa bằng lời của riêng bạn các thuật ngữ constraint, backtracking search, arc consistency, backjumping, min-conflicts và cycle cutset.


---

##### Bài tập 6.18

Định nghĩa bằng lời của riêng bạn các thuật ngữ constraint, commutativity, arc consistency, backjumping, min-conflicts và cycle cutset.


---

##### Bài tập 6.19

Giả sử rằng một đồ thị được biết là có một cycle cutset không quá $k$ nút. Mô tả một thuật toán đơn giản để tìm một cycle cutset tối thiểu có thời gian chạy không quá $O(n^k)$ cho một CSP có $n$ biến. Tìm kiếm tài liệu về các phương pháp tìm cycle cutset gần tối thiểu trong thời gian đa thức theo kích thước của cutset. Sự tồn tại của các thuật toán như vậy có làm cho phương pháp cycle cutset trở nên thực tế không?


---

##### Bài tập 6.20

Xem xét bài toán lát một bề mặt (bao phủ hoàn toàn và chính xác) bằng $n$ quân domino ($2\times 1$ hình chữ nhật). Bề mặt là một tập hợp tùy ý các hình vuông $1\times 1$ được kết nối cạnh (tức là liền kề theo một cạnh, không chỉ theo góc) với tổng số $2n$ hình vuông (ví dụ: một bàn cờ, một bàn cờ với một số ô bị thiếu, một hàng 10 ô vuông, v.v.).<br>

1.  Định nghĩa chính xác bài toán này dưới dạng một CSP trong đó các quân domino là các biến.<br>

2.  Định nghĩa chính xác bài toán này dưới dạng một CSP trong đó các ô vuông là các biến, giữ cho không gian trạng thái nhỏ nhất có thể. (*Gợi ý:* liệu việc quân domino nào được đặt trên một cặp ô vuông cụ thể có quan trọng không?)<br>

3.  Xây dựng một bề mặt gồm 6 ô vuông sao cho công thức CSP của bạn từ phần (b) có một đồ thị ràng buộc *có cấu trúc cây*.<br>

4.  Mô tả chính xác tập hợp các trường hợp có thể giải được có đồ thị ràng buộc có cấu trúc cây.<br>


---

<!-- tabs:end -->
