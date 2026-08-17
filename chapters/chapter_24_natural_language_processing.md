# Chapter 24 Natural Language Processing

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_24_Natural%20Language%20Processing/chapter_24_vi.html?v=1" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_24_Natural%20Language%20Processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide/chapter24.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter24/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/nlp.ipynb"  target="_blank" data-ignore>Nlp</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/nlp.ipynb"   target="_blank" data-ignore>Nlp (Python File)</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/nlp_apps.ipynb"  target="_blank" data-ignore>Nlp Apps</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/nlp_apps.ipynb"   target="_blank" data-ignore>Nlp Apps (Python File)</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/text.ipynb"  target="_blank" data-ignore>Text</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/text.ipynb"   target="_blank" data-ignore>Text (Python File)</a>


#### **Bài tập**


##### Bài tập 24.1

Dưới bóng cây có tán lá rậm rạp, người ta nhìn thấy một số đốm sáng. Điều đáng ngạc nhiên là tất cả chúng đều có vẻ tròn. Tại sao? Xét cho cùng, các khe hở giữa các lá cây mà ánh nắng chiếu qua khó có thể có hình tròn.

---

##### Bài tập 24.2

Hãy xem xét một bức ảnh chụp một quả cầu trắng lơ lửng trước phông nền đen. Đường cong hình ảnh phân tách các pixel trắng và đen đôi khi được gọi là "đường viền" của quả cầu. Chứng minh rằng đường viền của một quả cầu, khi nhìn qua một camera phối cảnh, có thể là một hình ellipse. Tại sao quả cầu không trông giống hình ellipse đối với bạn?

---

##### Bài tập 24.3

Hãy xem xét một hình trụ dài vô hạn có bán kính $r$ được định hướng với trục của nó dọc theo trục $y$. Hình trụ có bề mặt Lambertian và được quan sát bởi một camera dọc theo trục $z$ dương. Bạn sẽ mong đợi nhìn thấy gì trong ảnh nếu hình trụ được chiếu sáng bởi một nguồn sáng điểm ở vô cùng nằm trên trục $x$ dương? Vẽ các đường đồng mức có độ sáng không đổi trong ảnh chiếu. Các đường đồng mức có độ sáng bằng nhau có cách đều nhau không?

---

##### Bài tập 24.4

Các cạnh trong một ảnh có thể tương ứng với nhiều sự kiện khác nhau trong một cảnh. Hãy xem xét Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/illuminationfigure.png">illuminationfigure</a> (trang <a class="pageRef" title="" href="#">illuminationfigure</a>, và giả sử đó là ảnh chụp một cảnh ba chiều thực tế. Xác định mười cạnh sáng khác nhau trong ảnh, và đối với mỗi cạnh, hãy cho biết nó tương ứng với sự gián đoạn về (a) độ sâu, (b) hướng bề mặt, (c) phản xạ, hay (d) chiếu sáng.

---

##### Bài tập 24.5

Một hệ thống lập thể đang được xem xét để lập bản đồ địa hình. Nó sẽ bao gồm hai camera CCD, mỗi camera có ${512}\times {512}$ pixel trên một cảm biến vuông 10 cm $\times$ 10 cm. Các ống kính được sử dụng có tiêu cự 16 cm, với tiêu điểm cố định ở vô cực. Đối với các điểm tương ứng ($u_1,v_1$) trong ảnh trái và ($u_2,v_2$) trong ảnh phải, $v_1=v_2$ vì các trục $x$ trong hai mặt phẳng ảnh song song với các đường epipolar—các đường nối từ vật thể đến camera. Các trục quang học của hai camera song song. Khoảng cách giữa hai camera là 1 mét.<br>

1. Nếu khoảng cách gần nhất cần đo là 16 mét, thì độ lệch lớn nhất sẽ xảy ra là bao nhiêu (tính bằng pixel)?<br>

2. Độ phân giải khoảng cách ở 16 mét, do khoảng cách giữa các pixel, là bao nhiêu?<br>

3. Khoảng cách nào tương ứng với độ lệch một pixel?<br>

---

##### Bài tập 24.6

Phát biểu nào sau đây là đúng, và phát biểu nào là sai?<br>

1. Tìm các điểm tương ứng trong ảnh lập thể là giai đoạn dễ nhất của quá trình tìm độ sâu lập thể.<br>

2. Shape-from-texture có thể được thực hiện bằng cách chiếu một lưới các dải sáng lên cảnh.<br>

3. Các đường có độ dài bằng nhau trong cảnh luôn chiếu thành các đường có độ dài bằng nhau trong ảnh.<br>

4. Các đường thẳng trong ảnh nhất thiết tương ứng với các đường thẳng trong cảnh.

---

###### Bài tập 24.7

Phát biểu nào sau đây là đúng, và phát biểu nào là sai?<br>

1. Tìm các điểm tương ứng trong ảnh lập thể là giai đoạn dễ nhất của quá trình tìm độ sâu lập thể.<br>

2. Trong các góc nhìn lập thể của cùng một cảnh, độ chính xác cao hơn trong các phép tính độ sâu sẽ đạt được nếu hai vị trí camera cách xa nhau hơn.<br>

3. Các đường có độ dài bằng nhau trong cảnh luôn chiếu thành các đường có độ dài bằng nhau trong ảnh.<br>

4. Các đường thẳng trong ảnh nhất thiết tương ứng với các đường thẳng trong cảnh.<br>

<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/bottle-stereo.svg" alt="bottle-figure" id="bottle-figure" style="width:100%">
  <figcaption><center><b>Nhìn từ trên xuống của hệ thống hai camera quan sát một chai rượu với bức tường phía sau.</b></center></figcaption>
</figure>

---

##### Bài tập 24.8

(Được cung cấp bởi Pietro Perona.) Hình <a class="insideExercisesFigRef" href="#bottle-figure">bottle-figure</a> cho thấy hai camera ở X và Y đang quan sát một cảnh. Vẽ ảnh nhìn thấy ở mỗi camera, giả sử tất cả các điểm được đặt tên đều nằm trên cùng một mặt phẳng ngang. Có thể rút ra kết luận gì từ hai ảnh này về khoảng cách tương đối của các điểm A, B, C, D và E so với đường cơ sở của camera, và dựa trên cơ sở nào?

<!-- tabs:end -->
