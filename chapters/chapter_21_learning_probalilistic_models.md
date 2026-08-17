# Chapter 21 Learning Probalilistic models

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_21_Learning%20Probalilistic%20models/chapter_21_vi.html?v=3" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_21_Learning%20Probalilistic%20models.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter21_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter21/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
<div id="quiz-container" data-chapter="21"></div>

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**


##### Bài tập 21.1

Triển khai một passive learning agent trong một môi trường đơn giản, ví dụ như thế giới $4\times 3$. Đối với trường hợp mô hình môi trường ban đầu không xác định, hãy so sánh hiệu suất học tập của các thuật toán direct utility estimation, TD và ADP. Thực hiện so sánh cho optimal policy và cho một vài random policies. Đối với trường hợp nào thì utility estimates hội tụ nhanh hơn? Điều gì xảy ra khi kích thước của môi trường được tăng lên? (Thử nghiệm với các môi trường có và không có chướng ngại vật.)


---

##### Bài tập 21.2

Chương <a class="chapterRef" href="{{site.baseurl}}/concept-decisions-exercise/">complex-decisions-chapter</a> đã định nghĩa một <b>proper policy</b> cho một MDP là một policy được đảm bảo sẽ đạt đến một terminal state. Chứng minh rằng có thể xảy ra trường hợp một passive ADP agent học được một transition model mà tại đó policy $\pi$ của nó là improper ngay cả khi $\pi$ là proper cho true MDP; với các mô hình như vậy, bước POLICY-EVALUATION có thể thất bại nếu $\gamma{{\,=\,}}1$. Chứng minh rằng vấn đề này không thể xảy ra nếu POLICY-EVALUATION chỉ được áp dụng cho mô hình đã học vào cuối một trial.


---

##### Bài tập 21.3

Bắt đầu với passive ADP agent, sửa đổi nó để sử dụng một approximate ADP algorithm như đã thảo luận trong văn bản. Thực hiện điều này theo hai bước:<br>

1.  Triển khai một priority queue cho các điều chỉnh đối với utility estimates. Bất cứ khi nào một state được điều chỉnh, tất cả các predecessors của nó cũng trở thành ứng cử viên để điều chỉnh và nên được thêm vào queue. Queue được khởi tạo với state mà từ đó quá trình chuyển đổi gần đây nhất đã diễn ra. Chỉ cho phép một số lượng điều chỉnh cố định.<br>

2.  Thử nghiệm với các heuristic khác nhau để sắp xếp priority queue, xem xét ảnh hưởng của chúng đến tốc độ học tập và thời gian tính toán.


---

##### Bài tập 21.4

Phương pháp direct utility estimation trong Mục <a class="sectionRef" href="#">passive-rl-section</a> sử dụng các distinguished terminal states để chỉ ra kết thúc của một trial. Làm thế nào nó có thể được sửa đổi cho các môi trường có discounted rewards và không có terminal states?


---

##### Bài tập 21.5

Viết ra các phương trình cập nhật tham số cho TD learning với
$$\hat{U}(x,y) = \theta_0 + \theta_1 x + \theta_2 y + \theta_3\,\sqrt{(x-x_g)^2 + (y-y_g)^2}\ .$$


---

##### Bài tập 21.6

Chuyển đổi vacuum world (Chương <a class="chapterRef" href="{{site.baseurl}}/agents-exercises/">agents-chapter</a>) cho reinforcement learning bằng cách bao gồm các phần thưởng cho các ô sạch. Làm cho thế giới trở nên observable bằng cách cung cấp các percept phù hợp. Bây giờ hãy thử nghiệm với các reinforcement learning agents khác nhau. Có cần thiết phải sử dụng function approximation để thành công không? Loại approximator nào phù hợp cho ứng dụng này?


---

##### Bài tập 21.7

Triển khai một exploring reinforcement learning agent sử dụng direct utility estimation. Tạo hai phiên bản—một với biểu diễn dạng bảng (tabular representation) và một sử dụng function approximator trong Phương trình (<a class="equationRef" title="" href="#">4x3-linear-approx-equation</a>). So sánh hiệu suất của chúng trong ba môi trường:<br>

1.  Thế giới $4\times 3$ được mô tả trong chương.<br>

2.  Thế giới ${10}\times {10}$ không có chướng ngại vật và phần thưởng +1 tại (10,10).<br>

3.  Thế giới ${10}\times {10}$ không có chướng ngại vật và phần thưởng +1 tại (5,5).


---

##### Bài tập 21.8

Thiết kế các features phù hợp cho reinforcement learning trong các stochastic grid worlds (các tổng quát hóa của thế giới $4\times 3$) chứa nhiều chướng ngại vật và nhiều terminal states với phần thưởng +1 hoặc -1.


---

##### Bài tập 21.9

Mở rộng môi trường chơi game tiêu chuẩn (Chương <a class="chapterRef" href="{{site.baseurl}}/game-playing-exercises/">game-playing-chapter</a>) để tích hợp tín hiệu phần thưởng. Đặt hai reinforcement learning agents vào môi trường (chúng có thể, tất nhiên, chia sẻ chương trình agent) và cho chúng chơi với nhau. Áp dụng quy tắc cập nhật TD tổng quát (generalized TD update rule) (Phương trình (<a class="equationRef" title="" href="#">generalized-td-equation</a>)) để cập nhật hàm đánh giá (evaluation function). Bạn có thể muốn bắt đầu với một hàm đánh giá tuyến tính trọng số đơn giản (simple linear weighted evaluation function) và một trò chơi đơn giản, chẳng hạn như tic-tac-toe.


---

##### Bài tập 21.10

Tính toán hàm utility thực sự và phép xấp xỉ tuyến tính tốt nhất theo $x$ và $y$ (như trong Phương trình (<a class="equationRef" title="" href="#">4x3-linear-approx-equation</a>)) cho các môi trường sau:<br>

1.  Thế giới ${10}\times {10}$ với một terminal state +1 duy nhất tại (10,10).<br>

2.  Như trong (a), nhưng thêm một terminal state -1 tại (10,1).<br>

3.  Như trong (b), nhưng thêm chướng ngại vật vào 10 ô ngẫu nhiên.<br>

4.  Như trong (b), nhưng đặt một bức tường kéo dài từ (5,2) đến (5,9).<br>

5.  Như trong (a), nhưng với terminal state tại (5,5).<br>

Các hành động là các bước di chuyển xác định theo bốn hướng. Trong mỗi trường hợp, so sánh kết quả bằng cách sử dụng các biểu đồ ba chiều. Đối với mỗi môi trường, đề xuất các features bổ sung (ngoài $x$ và $y$) sẽ cải thiện phép xấp xỉ và hiển thị kết quả.


---

##### Bài tập 21.11

Triển khai các thuật toán REINFORCE và PEGASUS và áp dụng chúng cho thế giới $4\times 3$, sử dụng một họ policy do bạn tự chọn. Nhận xét về kết quả.


---

##### Bài tập 21.12

Nghiên cứu ứng dụng các ý tưởng reinforcement learning vào việc mô hình hóa hành vi của con người và động vật.


---

##### Bài tập 21.13

Reinforcement learning có phải là một mô hình trừu tượng phù hợp cho sự tiến hóa không? Có mối liên hệ nào, nếu có, giữa các tín hiệu phần thưởng bẩm sinh (hardwired reward signals) và fitness tiến hóa không?


---

<!-- tabs:end -->
