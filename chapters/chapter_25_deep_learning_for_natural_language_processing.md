# Chapter 25 Deep learning for natural language processing

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_25_Deep%20learning%20for%20natural%20language%20processing/chapter_25_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_25_Deep%20learning%20for%20natural%20language%20processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide/chapter25.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter25/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**


##### Bài tập 25.1

Monte Carlo localization là một thuật toán <i>thiên vị</i> với bất kỳ kích thước mẫu hữu hạn nào—tức là, giá trị kỳ vọng của vị trí được tính toán bởi thuật toán khác với giá trị kỳ vọng thực—do cách hoạt động của bộ lọc hạt. Trong câu hỏi này, bạn được yêu cầu định lượng sự thiên vị này.<br>

Để đơn giản hóa, hãy xem xét một thế giới với bốn vị trí robot có thể có: $X=\{x_1,x_2,x_3,x_4\}$. Ban đầu, chúng ta rút ra $N\geq {{\rm 1}}$ mẫu đồng nhất từ ​​trong số các vị trí đó. Như thường lệ, hoàn toàn chấp nhận được nếu có nhiều hơn một mẫu được tạo ra cho bất kỳ vị trí nào trong $X$. Gọi $Z$ là một biến cảm biến Boolean được đặc trưng bởi các xác suất có điều kiện sau:<br>


$$\begin{aligned}
P(z | x_1) = 0.8 \qquad\qquad P(\neg z | x_1) = 0.2  \\
P(z | x_2) = 0.4 \qquad\qquad P(\neg z | x_2) = 0.6  \\
P(z | x_3) = 0.1 \qquad\qquad P(\neg z | x_3) = 0.9  \\
P(z | x_4) = 0.1 \qquad\qquad P(\neg z | x_4) = 0.9 
\end{aligned}$$


<br>

MCL sử dụng các xác suất này để tạo ra trọng số hạt, sau đó được chuẩn hóa và sử dụng trong quá trình lấy mẫu lại. Để đơn giản, hãy giả sử chúng ta chỉ tạo ra một mẫu mới trong quá trình lấy mẫu lại, bất kể $N$. Mẫu này có thể tương ứng với bất kỳ vị trí nào trong bốn vị trí trong $X$. Do đó, quá trình lấy mẫu xác định một phân phối xác suất trên $X$.<br>

1.  Phân phối xác suất kết quả trên $X$ cho mẫu mới này là gì? Trả lời câu hỏi này riêng biệt cho $N=1,\ldots,10$, và cho $N=\infty$.<br>

2.  Sự khác biệt giữa hai phân phối xác suất $P$ và $Q$ có thể được đo bằng độ phân kỳ KL, được định nghĩa là
    $${KL}(P,Q) = \sum_i P(x_i)\log\frac{P(x_i)}{Q(x_i)}\ .$$ Độ phân kỳ KL giữa các phân phối trong (a) và posterior thực sự là gì?<br>

3.  Cần sửa đổi công thức bài toán (không phải thuật toán!) như thế nào để đảm bảo rằng ước lượng cụ thể trên là không thiên vị ngay cả đối với các giá trị hữu hạn của $N$? Cung cấp ít nhất hai sửa đổi như vậy (mỗi sửa đổi đều đủ).<br>


---

###### Bài tập 25.2

Triển khai Monte Carlo localization cho một robot mô phỏng với các cảm biến đo khoảng cách. Bản đồ lưới và dữ liệu đo khoảng cách có sẵn từ kho mã nguồn tại
<a href="http://aima.cs.berkeley.edu">aima.cs.berkeley.edu</a>. Bạn nên chứng minh khả năng định vị toàn cục thành công của robot.

<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/figRobot2.svg" alt="figRobot2" id="figRobot2" style="width:100%">
  <figcaption><center><b>Một bộ thao tác robot trong hai cấu hình có thể có của nó.</b></center></figcaption>
</figure>


---

##### Bài tập 25.3

Xem xét một robot có hai bộ thao tác đơn giản, như được hiển thị trong hình 
<a href="#figRobot2">figRobot2</a>. Bộ thao tác A là một khối vuông cạnh 2 có thể trượt tới lui trên một thanh chạy dọc theo trục x từ x=-10 đến x=10. Bộ thao tác B là một khối vuông cạnh 2 có thể trượt tới lui trên một thanh chạy dọc theo trục y từ y=-10 đến y=10. Các thanh nằm ngoài mặt phẳng thao tác, vì vậy các thanh không cản trở chuyển động của các khối. Một cấu hình sau đó là một cặp ${\langle}x,y{\rangle}$ trong đó $x$ là tọa độ x của tâm của bộ thao tác A và $y$ là tọa độ y của tâm của bộ thao tác B. Vẽ không gian cấu hình cho robot này, chỉ ra các vùng được phép và bị loại trừ.


---

##### Bài tập 25.4

Giả sử bạn đang làm việc với robot trong Bài tập 
<a class="exerciseRef" href="{{ site.baseurl }}/nlp-english-exercises/ex_3/">AB-manipulator-ex</a> và bạn được giao nhiệm vụ tìm một đường đi từ cấu hình ban đầu của hình 
<a class="insideExercisesFigRef" href="#figRobot2">figRobot2</a> đến cấu hình kết thúc. Xem xét một hàm thế năng
$$D(A, {Goal})^2 + D(B, {Goal})^2 + \frac{1}{D(A, B)^2}$$
trong đó $D(A,B)$ là khoảng cách giữa các điểm gần nhất của A và B.<br>

1.  Chứng minh rằng leo đồi trong trường thế năng này sẽ bị kẹt ở cực tiểu cục bộ.<br>

2.  Mô tả một trường thế năng mà leo đồi sẽ giải quyết được bài toán cụ thể này. Bạn không cần phải tính toán các hệ số số chính xác cần thiết, chỉ cần dạng chung của giải pháp. (Gợi ý: Thêm một số hạng "thưởng" cho người leo đồi khi di chuyển A ra khỏi đường đi của B, ngay cả trong trường hợp như thế này, nơi mà điều này không làm giảm khoảng cách từ A đến B theo nghĩa trên.)<br>


---

##### Bài tập 25.5

Xem xét cánh tay robot được hiển thị trong
Hình 
<a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/FigArm1.png">FigArm1</a>. Giả sử rằng phần tử cơ sở của robot dài 60cm và cánh tay trên và cánh tay dưới mỗi chiếc dài 40cm. Như đã lập luận trên trang 
<a class="pageRef" title="" href="#">inverse-kinematics-not-unique</a>, động học ngược của robot thường không duy nhất. Nêu một giải pháp dạng đóng rõ ràng cho động học ngược của cánh tay này. Dưới những điều kiện chính xác nào thì giải pháp là duy nhất?


---

##### Bài tập 25.6

Xem xét cánh tay robot được hiển thị trong
Hình 
<a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/FigArm1.png">FigArm1</a>. Giả sử rằng phần tử cơ sở của robot dài 70cm và cánh tay trên và cánh tay dưới mỗi chiếc dài 50cm. Như đã lập luận trên trang 
<a class="pageRef" title="" href="#">inverse-kinematics-not-unique</a>, động học ngược của robot thường không duy nhất. Nêu một giải pháp dạng đóng rõ ràng cho động học ngược của cánh tay này. Dưới những điều kiện chính xác nào thì giải pháp là duy nhất?


---

##### Bài tập 25.7

Triển khai một thuật toán để tính toán biểu đồ Voronoi của một môi trường 2D tùy ý, được mô tả bởi một mảng Boolean $n\times n$. Minh họa thuật toán của bạn bằng cách vẽ biểu đồ Voronoi cho 10 bản đồ thú vị. Độ phức tạp của thuật toán của bạn là bao nhiêu?


---

###### Bài tập 25.8

Bài tập này khám phá mối quan hệ giữa không gian làm việc và không gian cấu hình bằng cách sử dụng các ví dụ được hiển thị trong Hình 
<a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>.

1.  Xem xét các cấu hình robot được hiển thị trong
    Hình 
    <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(a) đến (c), bỏ qua chướng ngại vật được hiển thị trong mỗi sơ đồ. Vẽ các cấu hình cánh tay tương ứng trong không gian cấu hình. (<i>Gợi ý:</i> Mỗi cấu hình cánh tay ánh xạ tới một điểm duy nhất trong không gian cấu hình, như minh họa trong Hình 
    <a class="insideExercisesFigRef"  href="#FigEx2">FigArm1</a>(b).)<br>

2.  Vẽ không gian cấu hình cho mỗi sơ đồ không gian làm việc trong Hình 
    <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(a)–(c). (<i>Gợi ý:</i> Không gian cấu hình chia sẻ với không gian được hiển thị trong
    Hình 
    <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(a) vùng tương ứng với va chạm tự thân, nhưng sự khác biệt phát sinh từ việc thiếu các chướng ngại vật bao quanh và các vị trí khác nhau của chướng ngại vật trong các hình riêng lẻ này.)<br>

3.  Đối với mỗi dấu chấm đen trong Hình 
    <a href="#">FigEx2</a>(e)–(f), vẽ các cấu hình cánh tay robot tương ứng trong không gian làm việc.
    Vui lòng bỏ qua các vùng tô bóng trong bài tập này.<br>

4.  Không gian cấu hình được hiển thị trong
    Hình 
    <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(e)–(f) đều được tạo ra bởi một chướng ngại vật không gian làm việc duy nhất (tô bóng tối), cộng với các ràng buộc phát sinh từ ràng buộc va chạm tự thân (tô bóng nhạt). Vẽ, cho mỗi sơ đồ, chướng ngại vật không gian làm việc tương ứng với vùng tô bóng tối.<br>

5.  Hình 
    <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(d) minh họa rằng một chướng ngại vật phẳng duy nhất có thể phân chia không gian làm việc thành hai vùng không kết nối.
    Số lượng vùng không kết nối tối đa có thể được tạo ra bằng cách chèn một chướng ngại vật phẳng vào một không gian làm việc không có chướng ngại vật, kết nối, cho robot 2DOF là bao nhiêu? Đưa ra một ví dụ và lập luận tại sao không thể tạo ra số lượng vùng không kết nối lớn hơn. Còn chướng ngại vật không phẳng thì sao?<br>

    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseRobot1.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(a)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseRobot3.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(b)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseRobot6.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(c)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseConf2.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(d)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseConf4.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(e)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseConf5.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(f)</b></center></figcaption>
    </figure>


---

###### Bài tập 25.9

Xem xét một robot di động di chuyển trên bề mặt ngang. Giả sử rằng robot có thể thực hiện hai loại chuyển động:<br>

-   Lăn về phía trước một khoảng cách xác định.<br>

-   Quay tại chỗ một góc xác định.<br>

Trạng thái của một robot như vậy có thể được đặc trưng bởi ba tham số ${\langle}x,y,\phi$, tọa độ x và y của robot (chính xác hơn là tâm quay của nó) và hướng của robot được biểu thị bằng góc so với trục x dương. Hành động “$Roll(D)$” có tác dụng thay đổi trạng thái ${\langle}x,y,\phi$ thành ${\langle}x+D \cos(\phi), y+D \sin(\phi), \phi {\rangle}$, và hành động $Rotate(\theta)$ có tác dụng thay đổi trạng thái<br>
${\langle}x,y,\phi {\rangle}$ thành
${\langle}x,y, \phi + \theta {\rangle}$.

1.  Giả sử robot ban đầu ở ${\langle}0,0,0 {\rangle}$ và sau đó thực hiện các hành động $Rotate(60^{\circ})$, $Roll(1)$, $Rotate(25^{\circ})$, $Roll(2)$. Trạng thái cuối cùng của robot là gì?<br>

2.  Bây giờ giả sử rằng robot có khả năng kiểm soát việc quay của mình không hoàn hảo, và nếu nó cố gắng quay một góc $\theta$, nó có thể thực sự quay một góc bất kỳ trong khoảng $\theta-10^{\circ}$ và $\theta+10^{\circ}$. Trong trường hợp đó, nếu robot cố gắng thực hiện chuỗi hành động trong (A), sẽ có một phạm vi các trạng thái kết thúc có thể. Giá trị nhỏ nhất và lớn nhất của tọa độ x, tọa độ y và hướng trong trạng thái cuối cùng là gì?<br>

3.  Hãy sửa đổi mô hình trong (B) thành một mô hình xác suất, trong đó, khi robot cố gắng quay một góc $\theta$, góc quay thực tế của nó tuân theo phân phối Gaussian với giá trị trung bình $\theta$ và độ lệch chuẩn $10^{\circ}$. Giả sử robot thực hiện các hành động $Rotate(90^{\circ})$, $Roll(1)$. Đưa ra một lập luận đơn giản rằng (a) giá trị kỳ vọng của vị trí ở cuối không bằng kết quả của việc quay chính xác $90^{\circ}$ và sau đó lăn về phía trước 1 đơn vị, và (b) phân phối các vị trí ở cuối không tuân theo phân phối Gaussian. (Không cố gắng tính toán giá trị trung bình thực hoặc phân phối thực.)<br>

    Điểm của bài tập này là sự không chắc chắn về góc quay nhanh chóng dẫn đến nhiều sự không chắc chắn về vị trí và việc xử lý sự không chắc chắn về góc quay rất khó khăn, cho dù sự không chắc chắn được xem xét theo các khoảng cứng hay theo xác suất, do mối quan hệ giữa hướng và vị trí vừa phi tuyến tính vừa không đơn điệu.<br>
<figure>
  <img src="http://aimacode.github.io/aima-exercises/figures/robotics-pic7.svg" alt="FigEx3" id="FigEx3" style="width:100%">
    <figcaption><center><b>Robot đơn giản hóa trong mê cung. Xem Bài tập <a href="#">robot-exploration-exercise</a></b></center></figcaption>
</figure>


---

##### Bài tập 25.10

Xem xét robot đơn giản hóa được hiển thị trong
Hình 
<a class="insideExercisesFigRef"  href="#FigEx3">FigEx3</a>. Giả sử tọa độ Descartes của robot được biết tại mọi thời điểm, cũng như tọa độ của vị trí mục tiêu của nó. Tuy nhiên, vị trí của các chướng ngại vật là không xác định. Robot có thể cảm nhận các chướng ngại vật ở gần nó, như minh họa trong hình này. Để đơn giản, hãy giả sử chuyển động của robot không có nhiễu, và không gian trạng thái là rời rạc. Hình 
<a class="insideExercisesFigRef"  href="#FigEx3">FigEx3</a> chỉ là một ví dụ; trong bài tập này, bạn được yêu cầu giải quyết tất cả các thế giới lưới có đường đi hợp lệ từ điểm bắt đầu đến vị trí mục tiêu.<br>

1.  Thiết kế một bộ điều khiển có chủ đích đảm bảo rằng robot luôn đạt được vị trí mục tiêu nếu có thể. Bộ điều khiển có chủ đích có thể ghi nhớ các phép đo dưới dạng một bản đồ đang được thu thập khi robot di chuyển. Giữa các lần di chuyển riêng lẻ, nó có thể dành thời gian tùy ý để suy nghĩ.<br>

2.  Bây giờ hãy thiết kế một bộ điều khiển <i>phản ứng</i> cho cùng một nhiệm vụ.
    Bộ điều khiển này không được phép ghi nhớ các phép đo cảm biến trong quá khứ. (Nó không được xây dựng bản đồ!) Thay vào đó, nó phải đưa ra tất cả các quyết định dựa trên phép đo hiện tại, bao gồm kiến thức về vị trí của chính nó và vị trí của mục tiêu. Thời gian để đưa ra quyết định phải độc lập với kích thước môi trường hoặc số lượng các bước thời gian trước đó. Số bước tối đa mà robot của bạn có thể mất để đến đích là bao nhiêu?<br>

3.  Bộ điều khiển của bạn từ (a) và (b) sẽ hoạt động như thế nào nếu bất kỳ điều kiện nào sau đây áp dụng: không gian trạng thái liên tục, nhiễu trong nhận thức, nhiễu trong chuyển động, nhiễu trong cả nhận thức và chuyển động, vị trí mục tiêu không xác định (mục tiêu chỉ có thể phát hiện khi trong phạm vi cảm biến), hoặc chướng ngại vật di chuyển. Đối với mỗi điều kiện và mỗi bộ điều khiển, hãy đưa ra một ví dụ về một tình huống mà robot thất bại (hoặc giải thích tại sao nó không thể thất bại).<br>


---

##### Bài tập 25.11

Trong Hình 
<a class="insideExercisesFigRef" href="#">Fig5</a>(b) trên trang 
<a class="pageRef" title="" href="#">Fig5</a>, chúng ta đã gặp một máy trạng thái hữu hạn tăng cường để điều khiển một chân duy nhất của robot lục giác. Trong bài tập này, mục tiêu là thiết kế một AFSM, khi kết hợp với sáu bản sao của bộ điều khiển chân riêng lẻ, sẽ dẫn đến khả năng di chuyển hiệu quả, ổn định. Vì mục đích này, bạn phải tăng cường bộ điều khiển chân riêng lẻ để truyền tin nhắn đến AFSM mới của bạn và đợi cho đến khi các tin nhắn khác đến. Lập luận tại sao bộ điều khiển của bạn hiệu quả, theo đó nó không lãng phí năng lượng một cách không cần thiết (ví dụ: bằng cách làm trượt chân), và theo đó nó đẩy robot với tốc độ tương đối cao. Chứng minh rằng bộ điều khiển của bạn thỏa mãn điều kiện ổn định đa giác được đưa ra trên trang 
<a href="#">polygon-stability-condition-page</a>.


---

##### Bài tập 25.12

(Bài tập này ban đầu được Michael Genesereth và Nils Nilsson nghĩ ra. Nó phù hợp với học sinh lớp một đến sinh viên sau đại học.) Con người rất giỏi trong các công việc gia đình cơ bản đến nỗi họ thường quên đi sự phức tạp của những công việc này. Trong bài tập này, bạn sẽ khám phá sự phức tạp và tái hiện lại 30 năm phát triển trong lĩnh vực robot. Xem xét nhiệm vụ xây dựng một vòm bằng ba khối. Mô phỏng một robot với bốn người như sau:<br>

<b>Bộ não.</b> Bộ não chỉ đạo các bàn tay thực hiện một kế hoạch để đạt được mục tiêu. Bộ não nhận đầu vào từ Mắt, nhưng <i>không thể nhìn trực tiếp cảnh vật</i>. Bộ não là người duy nhất biết mục tiêu là gì.<br>

<b>Mắt.</b> Mắt báo cáo một mô tả ngắn gọn về cảnh vật cho Bộ não: “Có một hộp màu đỏ đứng trên một hộp màu xanh lá cây, đang nằm nghiêng.” Mắt cũng có thể trả lời các câu hỏi từ Bộ não như, “Có khoảng trống nào giữa Tay trái và hộp màu đỏ không?” Nếu bạn có máy quay video, hãy hướng nó vào cảnh vật và cho phép mắt nhìn vào kính ngắm của máy quay video, nhưng không nhìn trực tiếp vào cảnh vật.<br>

<b>Tay trái</b> và <b>tay phải.</b> Một người đóng vai mỗi Tay. Hai Tay đứng cạnh nhau, mỗi người đeo một chiếc găng tay lò nướng trên một tay, Tay chỉ thực hiện các lệnh đơn giản từ Bộ não—ví dụ, “Tay trái, di chuyển hai inch về phía trước.” Chúng không thể thực hiện các lệnh khác ngoài chuyển động; ví dụ, chúng không thể được ra lệnh “Nhặt hộp lên.” Tay phải <i>bị bịt mắt</i>. Khả năng cảm nhận duy nhất của chúng là khả năng nhận biết khi đường đi của chúng bị chặn bởi một chướng ngại vật không thể di chuyển như bàn hoặc Tay kia. Trong những trường hợp như vậy, chúng có thể kêu bíp để thông báo cho Bộ não về khó khăn.


---

<!-- tabs:end -->
