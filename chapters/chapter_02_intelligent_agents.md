# Chapter 02 Intelligent Agents

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_02/chapter_02_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_02_Intelligent%20Agents.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter02_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter02/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Table-Driven-Agent.md" target="_blank">TABLE-DRIVEN-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Reflex-Vacuum-Agent.md" target="_blank">REFLEX-VACUUM-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Simple-Reflex-Agent.md" target="_blank">SIMPLE-REFLEX-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Model-Based-Reflex-Agent.md" target="_blank">MODEL-BASED-REFLEX-AGENT</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Agents**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/agents.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/agents.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/agents.ipynb" download>Tải .ipynb</a>
- **Vacuum World**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/vacuum_world.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/vacuum_world.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/vacuum_world.ipynb" download>Tải .ipynb</a>



#### **Bài tập**

##### Bài tập 2.1

Giả sử rằng thước đo hiệu suất (performance measure) chỉ quan tâm đến
$T$ bước thời gian đầu tiên của environment và bỏ qua mọi thứ sau đó.
Hãy chỉ ra rằng hành động của một rational agent có thể không chỉ phụ thuộc vào state của
environment mà còn phụ thuộc vào bước thời gian mà nó đã đạt tới.


---

##### Bài tập 2.2

Hãy xem xét rationality của các
agent function hút bụi khác nhau.<br>
1.  Chỉ ra rằng agent function hút bụi đơn giản được mô tả trong
    Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-agent-function-table.png">vacuum-agent-function-table</a> thực sự là
    rational theo các giả định được liệt kê ở trang <a class="pageRef" title="" href="#">vacuum-rationality-page</a><br>

2.  Mô tả một agent function rational cho trường hợp mỗi
    chuyển động tốn một điểm. Liệu agent program tương ứng có
    yêu cầu internal state không?<br>

3.  Thảo luận về các thiết kế agent có thể có cho các trường hợp mà các ô sạch
    có thể trở nên bẩn và địa lý của environment là chưa biết.
    Có hợp lý không khi agent học từ kinh nghiệm của nó trong
    những trường hợp này? Nếu có, nó nên học những gì? Nếu không, tại sao không?<br>


---

##### Bài tập 2.3

Viết một bài luận về mối quan hệ giữa tiến hóa và một hoặc nhiều khía cạnh sau:
sự tự chủ (autonomy), trí thông minh (intelligence), và học tập (learning).


---

##### Bài tập 2.4

Đối với mỗi khẳng định sau đây, hãy cho biết nó đúng hay sai
và ủng hộ câu trả lời của bạn bằng các ví dụ hoặc phản ví dụ ở nơi
thích hợp.<br>

1.  Một agent chỉ nhận thức được thông tin một phần về state thì không thể
    perfectly rational.<br>

2.  Tồn tại các task environment trong đó không có pure reflex agent nào có thể
    hoạt động một cách rational.<br>

3.  Tồn tại một task environment trong đó mọi agent đều rational.<br>

4.  Đầu vào của một agent program giống với đầu vào của
    agent function.<br>

5.  Mọi agent function đều có thể được triển khai bằng một
    sự kết hợp program/machine nào đó.<br>

6.  Giả sử một agent chọn hành động của nó một cách ngẫu nhiên đều đặn từ tập hợp
    các hành động khả thi. Tồn tại một deterministic task environment
    trong đó agent này là rational.<br>

7.  Có thể xảy ra trường hợp một agent cụ thể là perfectly rational trong hai
    task environment khác biệt.<br>

8.  Mọi agent đều rational trong một unobservable environment.<br>

9.  Một poker-playing agent perfectly rational sẽ không bao giờ thua.<br>


---

##### Bài tập 2.5

Đối với mỗi hoạt động sau đây, hãy đưa ra mô tả PEAS
về task environment và mô tả đặc điểm của nó theo các
thuộc tính được liệt kê trong Phần <a class="sectionRef" title="" href="#">env-properties-subsection</a><br>

-   Chơi bóng đá.<br>

-   Khám phá các đại dương dưới bề mặt của Titan.<br>

-   Mua sắm sách AI cũ trên Internet.<br>

-   Chơi một trận quần vợt.<br>

-   Tập đánh quần vợt vào tường.<br>

-   Thực hiện nhảy cao.<br>

-   Đan một chiếc áo len.<br>

-   Đấu giá một món hàng tại một cuộc đấu giá.<br>


---

##### Bài tập 2.6

Đối với mỗi hoạt động sau đây, hãy đưa ra mô tả PEAS
về task environment và mô tả đặc điểm của nó theo các
thuộc tính được liệt kê trong Phần <a class="sectionRef" title="" href="#">env-properties-subsection</a><br>

-   Thực hiện bài biểu diễn thể dục dụng cụ trên sàn.<br>

-   Khám phá các đại dương dưới bề mặt của Titan.<br>

-   Chơi bóng đá.<br>

-   Mua sắm sách AI cũ trên Internet.<br>

-   Tập đánh quần vợt vào tường.<br>

-   Thực hiện nhảy cao.<br>

-   Đấu giá một món hàng tại cuộc đấu giá.<br>


---

##### Bài tập 2.7

Định nghĩa theo ngôn ngữ của riêng bạn các thuật ngữ sau: agent, agent function,
agent program, rationality, autonomy, reflex agent, model-based agent,
goal-based agent, utility-based agent, learning agent.


---

##### Bài tập 2.8

Bài tập này khám phá sự khác biệt giữa
agent functions và agent programs.<br>

1.  Có thể có nhiều hơn một agent program thực hiện một
    agent function nhất định không? Đưa ra một ví dụ, hoặc chứng minh tại sao điều đó là không thể.<br>

2.  Có những agent function nào không thể được thực hiện bởi bất kỳ agent
    program nào không?<br>

3.  Cho một kiến trúc máy (machine architecture) cố định, có phải mỗi agent program
    thực hiện chính xác một agent function không?<br>

4.  Cho một kiến trúc có $n$ bit bộ nhớ lưu trữ, có bao nhiêu
    agent programs khả thi khác nhau?<br>

5.  Giả sử chúng ta giữ nguyên agent program nhưng tăng tốc máy tính lên
    gấp đôi. Điều đó có thay đổi agent function không?<br>


---

##### Bài tập 2.9

Viết mã giả (pseudocode) cho agent programs của goal-based agent và utility-based
agent.


---

##### Bài tập 2.10

Hãy xem xét một bộ điều nhiệt đơn giản sẽ bật lò sưởi khi
nhiệt độ thấp hơn ít nhất 3 độ so với mức cài đặt, và tắt
lò sưởi khi nhiệt độ cao hơn ít nhất 3 độ so với mức cài đặt. Liệu
bộ điều nhiệt này là một ví dụ về simple reflex agent, model-based reflex
agent, hay goal-based agent?


---

##### Bài tập 2.11

Triển khai một environment simulator đo lường hiệu suất
cho thế giới máy hút bụi được mô tả trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-world-figure.png">vacuum-world-figure</a> và được chỉ định ở
trang <a class="pageRef" title="" href="#">vacuum-rationality-page</a>. Việc triển khai của bạn nên có tính mô-đun hóa để
sensors, actuators, và đặc điểm của environment (kích thước, hình dạng, vị trí
bụi bẩn, v.v.) có thể thay đổi dễ dàng. (Lưu ý: đối với một số
lựa chọn ngôn ngữ lập trình và hệ điều hành, đã có sẵn
các bản triển khai trong kho mã trực tuyến.)


---

##### Bài tập 2.12

Triển khai một simple reflex agent cho vacuum environment trong
Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_10/">vacuum-start-exercise</a>. Chạy environment
với agent này cho tất cả các cấu hình bụi bẩn ban đầu và vị trí agent
khả thi. Ghi lại điểm hiệu suất cho từng cấu hình và
điểm trung bình tổng thể.


---

##### Bài tập 2.13

Hãy xem xét một phiên bản sửa đổi của
vacuum environment trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_10/">vacuum-start-exercise</a>,
trong đó agent bị phạt một điểm cho mỗi lần di chuyển.<br>

1.  Liệu một simple reflex agent có thể perfectly rational đối với
    environment này không? Giải thích.<br>

2.  Thế còn một reflex agent có state thì sao? Hãy thiết kế một agent như vậy.<br>

3.  Câu trả lời của bạn cho ý 1 và 2 sẽ
    thay đổi thế nào nếu percepts của agent cho nó biết trạng thái sạch/bẩn của
    mọi ô vuông trong environment?


---

##### Bài tập 2.14

Hãy xem xét một phiên bản sửa đổi của
vacuum environment trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_10/">vacuum-start-exercise</a>,
trong đó địa lý của environment—phạm vi, ranh giới, và
chướng ngại vật—là không xác định, cũng như cấu hình bụi bẩn ban đầu. (Agent
có thể đi Lên và Xuống cũng như Trái và Phải.)<br>

1.  Liệu một simple reflex agent có thể perfectly rational đối với
    environment này không? Giải thích.<br>

2.  Liệu một simple reflex agent với một agent function ngẫu nhiên hóa (randomized)
    có thể vượt trội hơn một simple reflex agent không? Hãy thiết kế một agent như vậy và
    đo lường hiệu suất của nó trên một số environments.<br>

3.  Bạn có thể thiết kế một environment mà trong đó agent ngẫu nhiên hóa của bạn sẽ
    hoạt động kém không? Hãy hiển thị kết quả của bạn.<br>

4.  Liệu một reflex agent có state có thể vượt trội hơn một simple reflex agent không?
    Hãy thiết kế một agent như vậy và đo lường hiệu suất của nó trên một số
    environments. Bạn có thể thiết kế một rational agent thuộc loại này không?


---

##### Bài tập 2.15

Lặp lại Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_13/">vacuum-unknown-geog-exercise</a> cho trường hợp mà
trong đó location sensor (cảm biến vị trí) được thay thế bằng một "bump" sensor (cảm biến va chạm) phát hiện
các nỗ lực của agent di chuyển vào chướng ngại vật hoặc vượt qua ranh giới
của environment. Giả sử "bump" sensor ngừng hoạt động; agent
nên hoạt động như thế nào?


---

##### Bài tập 2.16

Các vacuum environments trong các
bài tập trước đều là deterministic. Thảo luận về các agent programs có thể có
cho mỗi phiên bản stochastic sau đây:<br>

1.  Định luật Murphy: 25% số lần, hành động Suck
    sẽ thất bại trong việc làm sạch sàn nhà nếu nó bẩn và thả bụi bẩn xuống
    sàn nhà nếu sàn nhà đang sạch. Agent program của bạn bị ảnh hưởng như thế nào nếu
    dirt sensor đưa ra câu trả lời sai 10% số lần?<br>

2.  Trẻ nhỏ: Tại mỗi bước thời gian, mỗi ô sạch có 10%
    khả năng trở nên bẩn. Bạn có thể đưa ra một thiết kế rational agent
    cho trường hợp này không?


---


<!-- tabs:end -->
