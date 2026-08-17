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



#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter19/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Decision-Tree-Learning.md" target="_blank">LEARN-DECISION-TREE</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Cross-Validation-Wrapper.md" target="_blank">CROSS-VALIDATION-WRAPPER</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Decision-List-Learning.md" target="_blank">DECISION-LIST-LEARNING</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/AdaBoost.md" target="_blank">ADABOOST</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Current-Best-Learning.md" target="_blank">CURRENT-BEST-LEARNING</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Version-Space-Learning.md" target="_blank">VERSION-SPACE-LEARNING</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Minimal-Consistent-Det.md" target="_blank">MINIMAL-CONSISTENT-DET</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Foil.md" target="_blank">FOIL</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Learning**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/learning.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/learning.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/learning.ipynb" download>Tải .ipynb</a>
- **Learning Apps**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/learning_apps.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/learning_apps.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/learning_apps.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 19.1

Hãy chứng minh, bằng cách chuyển đổi sang dạng chuẩn liên kết (conjunctive normal form) và áp dụng phương pháp phân giải (resolution), rằng kết luận được rút ra trên trang <a class="pageRef" title="" href="#">dbsig-page</a> liên quan đến người Brazil là hợp lý.


---

##### Bài tập 19.2

Đối với mỗi xác định sau đây, hãy viết biểu diễn logic và giải thích tại sao xác định đó đúng (nếu có):<br>

1.  Thiết kế và mệnh giá xác định khối lượng của một đồng xu.<br>

2.  Đối với một chương trình cho trước, đầu vào xác định đầu ra.<br>

3.  Khí hậu, lượng thức ăn nạp vào, tập thể dục và trao đổi chất xác định sự tăng và giảm cân.<br>

4.  Hói đầu được xác định bởi tình trạng hói đầu (hoặc không hói đầu) của ông ngoại.<br>


---

##### Bài tập 19.3

Đối với mỗi xác định sau đây, hãy viết biểu diễn logic và giải thích tại sao xác định đó đúng (nếu có):<br>

1.  Mã bưu điện xác định tiểu bang (Hoa Kỳ).<br>

2.  Thiết kế và mệnh giá xác định khối lượng của một đồng xu.<br>

3.  Khí hậu, lượng thức ăn nạp vào, tập thể dục và trao đổi chất xác định sự tăng và giảm cân.<br>

4.  Hói đầu được xác định bởi tình trạng hói đầu (hoặc không hói đầu) của ông ngoại.<br>


---

##### Bài tập 19.4

Liệu một phiên bản xác định dựa trên xác suất có hữu ích không? Đề xuất một định nghĩa.


---

##### Bài tập 19.5

Điền các giá trị còn thiếu cho các mệnh đề $C_1$ hoặc $C_2$ (hoặc cả hai) trong các tập hợp mệnh đề sau, biết rằng $C$ là kết quả phân giải của $C_1$ và $C_2$:<br>

1.  $C = {True} \Rightarrow P(A,B)$,
    $C_1 = P(x,y) \Rightarrow Q(x,y)$, $C_2 = ??$.<br>

2.  $C = {True} \Rightarrow P(A,B)$, $C_1 = ??$,
    $C_2 = ??$.<br>

3.  $C = P(x,y) \Rightarrow P(x,f(y))$, $C_1 = ??$,
    $C_2 = ??$.<br>

Nếu có nhiều hơn một giải pháp khả thi, hãy cung cấp một ví dụ cho mỗi loại khác nhau.<br>


---

##### Bài tập 19.6

Giả sử người ta viết một chương trình logic thực hiện một bước suy luận phân giải. Tức là, ${Resolve}(c_1,c_2,c)$ thành công nếu $c$ là kết quả của việc phân giải $c_1$ và $c_2$. Thông thường, ${Resolve}$ sẽ được sử dụng như một phần của bộ chứng minh định lý bằng cách gọi nó với $c_1$ và $c_2$ được gán giá trị cho các mệnh đề cụ thể, từ đó tạo ra mệnh đề phân giải $c$. Bây giờ, giả sử thay vào đó, chúng ta gọi nó với $c$ được gán giá trị và $c_1$ và $c_2$ không được gán giá trị. Liệu điều này có thành công trong việc tạo ra các kết quả phù hợp của một bước phân giải ngược (inverse resolution step) không? Bạn có cần bất kỳ sửa đổi đặc biệt nào đối với hệ thống lập trình logic để điều này hoạt động không?


---

##### Bài tập 19.7

Giả sử đang xem xét việc thêm một mệnh đề (literal) vào một mệnh đề (clause) bằng cách sử dụng một vị từ nhị phân $P$ và các mệnh đề trước đó (bao gồm cả đầu của mệnh đề) chứa năm biến khác nhau.<br>

1.  Có bao nhiêu mệnh đề khác biệt về mặt chức năng có thể được tạo ra? Hai mệnh đề được coi là giống hệt nhau về mặt chức năng nếu chúng chỉ khác nhau về tên của các biến *mới* mà chúng chứa.<br>

2.  Bạn có thể tìm thấy một công thức tổng quát cho số lượng mệnh đề khác nhau với một vị từ có số ngôi (arity) là $r$ khi có $n$ biến đã được sử dụng trước đó không?<br>

3.  Tại sao không cho phép các mệnh đề không chứa biến nào đã được sử dụng trước đó?<br>


---

##### Bài tập 19.8

Sử dụng dữ liệu từ cây gia đình trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/family2-figure.png">family2-figure</a>, hoặc một tập con của nó, hãy áp dụng thuật toán để học một định nghĩa cho vị từ ${Ancestor}$.


---

<!-- tabs:end -->
