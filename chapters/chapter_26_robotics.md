# Chapter 26 Robotics

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_26_Robotics/chapter_26_vi.html?v=1" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_26_Robotics.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Robot học (Robotics)

## Chương 25

---
## Phác thảo

Robot, Cơ quan tác động và Cảm biến

Bản địa hóa và lập bản đồ

Lập kế hoạch chuyển động

Điều khiển động cơ

---
## Robot di động

 [Hình ảnh: \epsffile{figures/raibert-1leg.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/robocup.eps}] 

 [Hình ảnh: \epsffile{figures/raibert-1leg.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/robocup.eps}] 

---
## Bộ điều khiển 

,7\textwidth
[Hình ảnh: \fig{figures/stanford-arm.eps}]

Cấu hình của robot được xác định bởi 6 số
  
$\implies$ 6 \defn{bậc tự do} (DOF)

6 là số lượng tối thiểu cần thiết để định vị bộ phận tác động cuối một cách tùy ý.

Đối với các hệ thống động lực, hãy thêm vận tốc cho mỗi DOF.

---
## Robot không ba chiều

,4\textwidth
[Hình ảnh: \fig{figures/car-like.eps}]

Một chiếc ô tô có nhiều DOF (3) hơn điều khiển (2), nên \defn{non-holonomic};

nói chung không thể chuyển đổi giữa hai cấu hình cực kỳ gần nhau

---
## Cảm biến

\defn{Công cụ tìm phạm vi}: sonar (trên cạn, dưới nước), công cụ tìm phạm vi laser, radar (máy bay),[Hình ảnh: \epsffile{figures/robot0124bw.eps}]
cảm biến xúc giác, GPS

 [Hình ảnh: \epsffile{figures/sick.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/robot0124bw.eps}] 

\defn{Cảm biến hình ảnh}: camera (hình ảnh, hồng ngoại)

\defn{ Cảm biến bản quyền }: bộ giải mã trục (khớp, bánh xe), cảm biến quán tính, 

cảm biến lực, cảm biến mô-men xoắn

---
## Bản địa hóa---Tôi đang ở đâu?

Tính toán vị trí và hướng hiện tại (\defn{pose}) dựa trên các quan sát:

,7\textwidth
[Hình ảnh: \fig{figures/robotics-ddn.eps}]

---
## Tiếp theo bản địa hóa

\twofig{figures/robotics-pic2.eps}{figures/range-scan-model.eps}

Giả sử nhiễu Gaussian trong dự đoán chuyển động, đo phạm vi cảm biến

---
## Tiếp theo bản địa hóa

Có thể sử dụng tính năng lọc hạt để tạo ra ước tính vị trí gần đúng

\threefig{figures/first.ps}{figures/second.ps}{figures/third.ps}

---
## Tiếp theo bản địa hóa

Cũng có thể sử dụng bộ lọc Kalman mở rộng \defn{} cho các trường hợp đơn giản:

,75\textwidth
[Hình ảnh: \fig{figures/robotics-pic6.eps}]

Giả sử rằng các điểm mốc là *có thể nhận dạng được*---nếu không,
sau là đa phương thức

---
## Ánh xạ

Bản địa hóa: bản đồ đã cho và các mốc quan sát, cập nhật phân bổ tư thế

Lập bản đồ: tư thế đã cho và các mốc quan sát, cập nhật phân bổ bản đồ

SLAM: đưa ra các mốc quan sát, cập nhật tư thế và phân bổ bản đồ

Công thức xác suất của SLAM: 
  
 thêm các vị trí mốc $L_1,\ldots,L_k$ vào vectơ trạng thái,
  
 tiến hành như đối với việc bản địa hóa

---
### Tiếp theo ánh xạ 

 &nbsp;&nbsp;&nbsp;&nbsp; 

\epsfysize=0,37\textheight<img src="../TaiLieu/slide_md/figures/arena033.png" style="width:100%; height:auto;"> &nbsp;&nbsp;&nbsp;&nbsp; \epsfysize=0,37\textheight<img src="../TaiLieu/slide_md/figures/arena034.png" style="width:100%; height:auto;">
\epsfysize=0,37\textheight<img src="../TaiLieu/slide_md/figures/arena033.png" style="width:100%; height:auto;"> &nbsp;&nbsp;&nbsp;&nbsp; \epsfysize=0,37\textheight<img src="../TaiLieu/slide_md/figures/arena034.png" style="width:100%; height:auto;">

---
## Ví dụ về bản đồ 3D

\twofig{figures/mine-robot.eps}{figures/mine-data.eps}

---
## Lập kế hoạch chuyển động

Ý tưởng: sơ đồ trong không gian cấu hình \defn{} được xác định bởi DOF của robot

[Hình ảnh: \epsffile{figures/armExampleConfSpace.eps}]

 [Hình ảnh: \epsffile{figures/armExampleWorkSpace.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/armExampleConfSpace.eps}] 

Giải là quỹ đạo điểm trong không gian C tự do

---
## Quy hoạch không gian cấu hình

Vấn đề cơ bản: $\infty^d$ khẳng định! Chuyển đổi sang không gian trạng thái *hữu hạn*.

\defn{Phân hủy tế bào}:
  
  chia không gian thành các ô \defn{đơn giản}, 
  
  mỗi trong số đó có thể được duyệt qua một cách “dễ dàng” (ví dụ: lồi)

\defn{ Khung xương }: 
  
  xác định số lượng hữu hạn các điểm/đường được kết nối dễ dàng
  
  tạo thành một biểu đồ sao cho hai điểm bất kỳ được kết nối
  
  bởi một đường dẫn trên đồ thị

---
## Ví dụ về phân hủy ô

 &nbsp;&nbsp;&nbsp;&nbsp; 

 [Hình ảnh: \epsffile{figures/armDPwithoutPotentialWorkspaceCoarse.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/armDPwithoutPotentialCoarse.eps}] 

Sự cố: có thể không có đường dẫn trong các ô không gian trống thuần túy

Giải pháp: phân rã đệ quy các ô hỗn hợp (tự do + chướng ngại vật)

---
## Skeletonization: Sơ đồ Voronoi

Sơ đồ Voronoi: quỹ tích các điểm cách đều chướng ngại vật

,44\textwidth
[Hình ảnh: \fig{figures/armVoronoi.eps}]

Vấn đề: không mở rộng tốt sang các kích thước cao hơn

---
## Skeletonization: Lộ trình xác suất

Lộ trình xác suất được tạo bằng cách tạo các điểm ngẫu nhiên trong
C-space và giữ chúng trong không gian tự do; tạo biểu đồ bằng cách tham gia
cặp theo đường thẳng

,44\textwidth
[Hình ảnh: \fig{figures/armRoadmap.eps}]

Vấn đề: cần tạo đủ điểm để đảm bảo rằng mọi
cặp điểm bắt đầu/mục tiêu được kết nối thông qua biểu đồ

---
## Điều khiển động cơ

Có thể xem vấn đề điều khiển động cơ dưới dạng vấn đề tìm kiếm

trong không gian trạng thái \note{dynamic} thay vì \note{kinematic}:
  
-- không gian trạng thái được xác định bởi $x_1,x_2,\ldots,\dot{x_1},\dot{x_2},\ldots$
  
-- liên tục, đa chiều (Sarcos hình người: 162 chiều)

Kiểm soát xác định: nhiều vấn đề có thể giải quyết chính xác

đặc biệt nếu tuyến tính, ít chiều, được biết chính xác, có thể quan sát được

Luật điều khiển \defn{đơn giản} có hiệu lực đối với các chuyển động cụ thể

Stochastic \defn{điều khiển tối ưu}: rất ít vấn đề có thể giải được chính xác
  
$\implies$ phương pháp gần đúng/thích ứng

---
## Điều khiển động cơ sinh học

Hệ thống điều khiển động cơ được đặc trưng bởi sự dư thừa lớn

Vô số quỹ đạo đạt được bất kỳ nhiệm vụ nhất định nào

Ví dụ: cánh tay 3 liên kết di chuyển trong mặt phẳng ném vào mục tiêu
    
  bộ điều khiển 12 tham số đơn giản, một bậc tự do tại mục tiêu
    
  Không gian liên tục 11 chiều của bộ điều khiển tối ưu

Ý tưởng: nếu cánh tay ồn ào, chỉ có chính sách tối ưu " một "
giảm thiểu sai sót ở mục tiêu

Tức là, khả năng chịu tiếng ồn có thể giải thích hành vi vận động thực tế

Harris \& Wolpert (*Nature*, 1998): nhiễu phụ thuộc vào tín hiệu

giải thích hồ sơ vận tốc mắt chớp một cách hoàn hảo

---
### Cài đặt

Giả sử một bộ điều khiển có các tham số điều khiển "dự kiến" $\theta_0$

bị hỏng do nhiễu, tạo ra $\theta$ được rút ra từ $P_{\theta_0}$

Đầu ra (ví dụ: khoảng cách từ mục tiêu) $y = F(\theta)$; 

,7\maxfigwidth
<img src="../TaiLieu/slide_md/figures/arm-setup.png" style="width:100%; height:auto;">

---
## Thuật toán học đơn giản: Độ dốc ngẫu nhiên

Giảm thiểu $E_{\theta}[y^2]$ bằng cách giảm độ dốc:
\begin{eqnarray*}
\nabla_{\theta_0} E_{\theta}[y^2]
  &=&  \nabla_{\theta_0} \int P_{\theta_0}(\theta)F(\theta)^2 d\theta 

  &=&  \int \frac{\nabla_{\theta_0} P_{\theta_0}(\theta)}{P_{\theta_0}(\theta)}
            F(\theta)^2 P_{\theta_0}(\theta)d\theta 

  &=&  E_{\theta}[\frac{\nabla_{\theta_0} P_{\theta_0}(\theta)}
                       {P_{\theta_0}(\theta)}
                  y^2]
\end{eqnarray*}
Cho mẫu $(\theta_j,y_j)$, $j=1,\ldots,N$, ta có
\[
  \hat{\nabla_{\theta_0} E_{\theta}[y^2]} =
  \frac{1}{N}\sum_{j=1}^N
     \frac{\nabla_{\theta_0} P_{\theta_0}(\theta_j)}
                       {P_{\theta_0}(\theta_j)}
                  y_j^2
\]
Đối với nhiễu Gaussian có hiệp phương sai $\Sigma$, tức là
$P_{\theta_0}(\theta) = N(\theta_0,\Sigma)$, chúng tôi thu được
\[
  \hat{\nabla_{\theta_0} E_{\theta}[y^2]} =
  \frac{1}{N}\sum_{j=1}^N \Sigma^{-1}(\theta_j - \theta_0) y_j^2
\]

---
### Thuật toán đang làm gì

,7\maxfigwidth
<img src="../TaiLieu/slide_md/figures/control-noise-distort.png" style="width:100%; height:auto;">

---
### Kết quả cho bộ điều khiển 2--D

,75\textwidth
 <img src="../TaiLieu/slide_md/figures/progress3-theta.png" style="width:100%; height:auto;"> 

---
### Kết quả cho bộ điều khiển 2--D

,75\textwidth
 <img src="../TaiLieu/slide_md/figures/progress3-theta-zoom.png" style="width:100%; height:auto;"> 

---
### Kết quả cho bộ điều khiển 2--D

,75\textwidth
 <img src="../TaiLieu/slide_md/figures/progress3-score.png" style="width:100%; height:auto;"> 

---
## Tóm tắt

Cao su rơi xuống đường

Robot di động và người thao tác

Bậc tự do xác định cấu hình robot

Bản địa hóa và ánh xạ dưới dạng các vấn đề suy luận xác suất
  
  (yêu cầu mô hình cảm biến và chuyển động tốt)

Lập kế hoạch chuyển động trong không gian cấu hình
  
  yêu cầu một số phương pháp để hoàn thiện




#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter26/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Monte-Carlo-Localization.md" target="_blank">MONTE-CARLO-LOCALIZATION</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**


##### Bài tập 26.1

Xem xét danh sách các "hạn chế" được cho là của máy móc của Turing, xác định những gì đã đạt được, những gì có thể đạt được về nguyên tắc bằng một chương trình và những gì vẫn còn là vấn đề vì chúng đòi hỏi các trạng thái tinh thần có ý thức.


---

##### Bài tập 26.2

Tìm và phân tích một bài báo trên phương tiện truyền thông đại chúng về một hoặc nhiều lập luận cho rằng AI là không thể.


---

##### Bài tập 26.3

Cố gắng viết định nghĩa cho các thuật ngữ "intelligence," "thinking," và "consciousness." Đề xuất một số phản đối có thể có đối với định nghĩa của bạn.


---

##### Bài tập 26.4

Việc bác bỏ lập luận phòng Trung Quốc có nhất thiết chứng minh rằng các máy tính được lập trình phù hợp có các trạng thái tinh thần không? Việc chấp nhận lập luận có nhất thiết có nghĩa là máy tính không thể có các trạng thái tinh thần không?


---

##### Bài tập 26.5

Trong lập luận thay thế não, điều quan trọng là phải có khả năng phục hồi não của đối tượng về trạng thái bình thường, sao cho hành vi bên ngoài của nó giống như thể hoạt động đã không diễn ra. Liệu người hoài nghi có thể phản đối một cách hợp lý rằng điều này sẽ đòi hỏi phải cập nhật các đặc tính thần kinh sinh lý của các tế bào thần kinh liên quan đến trải nghiệm có ý thức, khác với những đặc tính liên quan đến hành vi chức năng của các tế bào thần kinh không?


---

##### Bài tập 26.6

Giả sử rằng một chương trình Prolog chứa nhiều mệnh đề về các quy tắc quốc tịch Anh được biên dịch và chạy trên một máy tính thông thường. Phân tích các "brain states" của máy tính dưới nội dung rộng và hẹp.


---

##### Bài tập 26.7

Alan Perlis [<a class="paperRef" title="" href="">Perlis:1982</a>] đã viết, "Một năm dành cho artificial intelligence là đủ để khiến người ta tin vào Chúa". Ông cũng viết, trong một lá thư gửi Philip Davis, rằng một trong những giấc mơ trung tâm của khoa học máy tính là "thông qua hiệu suất của máy tính và các chương trình của chúng, chúng ta sẽ loại bỏ mọi nghi ngờ rằng chỉ có sự khác biệt hóa học giữa thế giới sống và không sống." Mức độ nào mà tiến bộ đã đạt được cho đến nay trong artificial intelligence soi sáng các vấn đề này? Giả sử rằng vào một ngày nào đó trong tương lai, nỗ lực AI đã hoàn toàn thành công; nghĩa là, chúng ta đã xây dựng được các intelligent agents có khả năng thực hiện bất kỳ nhiệm vụ nhận thức nào của con người ở cấp độ năng lực của con người. Mức độ nào mà điều đó sẽ soi sáng các vấn đề này?


---

##### Bài tập 26.8

So sánh tác động xã hội của artificial intelligence trong năm mươi năm qua với tác động xã hội của việc giới thiệu các thiết bị điện và động cơ đốt trong trong năm mươi năm từ 1890 đến 1940.


---

##### Bài tập 26.9

I. J. Good cho rằng intelligence là phẩm chất quan trọng nhất, và việc xây dựng các máy móc siêu thông minh sẽ thay đổi mọi thứ. Một con báo có tri giác phản bác rằng "Thực ra tốc độ quan trọng hơn; nếu chúng ta có thể chế tạo máy móc siêu tốc, điều đó sẽ thay đổi mọi thứ," và một con voi có tri giác tuyên bố "Cả hai bạn đều sai; cái chúng ta cần là máy móc siêu mạnh." Bạn nghĩ gì về những lập luận này?


---

##### Bài tập 26.10

Phân tích các mối đe dọa tiềm ẩn từ công nghệ AI đối với xã hội. Những mối đe dọa nào là nghiêm trọng nhất và làm thế nào chúng có thể được đối phó? Chúng so sánh như thế nào với các lợi ích tiềm năng?


---

##### Bài tập 26.11

Các mối đe dọa tiềm ẩn từ công nghệ AI so sánh như thế nào với các mối đe dọa từ các công nghệ khoa học máy tính khác, và với công nghệ sinh học, công nghệ nano và công nghệ hạt nhân?


---

##### Bài tập 26.12

Một số nhà phê bình phản đối rằng AI là không thể, trong khi những người khác phản đối rằng nó là *quá* có thể và các máy móc siêu thông minh gây ra mối đe dọa. Bạn nghĩ rằng những phản đối nào có khả năng xảy ra hơn? Liệu có mâu thuẫn khi một người giữ cả hai quan điểm này không?


---

<!-- tabs:end -->
