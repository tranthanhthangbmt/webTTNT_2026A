# Chapter 14 Probabilistic Reasoning over time

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_14_Probabilistic%20Reasoning%20over%20time/chapter_14_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_14_Probabilistic%20Reasoning%20over%20time.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter14_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter14_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter14_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter14/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/Forward-Backward.md" target="_blank" data-ignore>FORWARD-BACKWARD</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Fixed-Lag-Smoothing.md" target="_blank" data-ignore>FIXED-LAG-SMOOTHING</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Particle-Filtering.md" target="_blank" data-ignore>PARTICLE-FILTERING</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Probability**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/probability.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/probability.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/probability.ipynb" download>Tải .ipynb</a>
- **Kalman Filter**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/kalman_filter.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/kalman_filter.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/kalman_filter.ipynb" download>Tải .ipynb</a>
- **Viterbi Algorithm**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/viterbi_algorithm.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/viterbi_algorithm.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/viterbi_algorithm.ipynb" download>Tải .ipynb</a>
- **Expectation Maximization**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/expectation_maximization.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/expectation_maximization.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/expectation_maximization.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 14.1

Chúng ta có một túi gồm ba đồng xu không cân bằng $a$, $b$, và $c$ với xác suất ra mặt ngửa lần lượt là 20%, 60%, và 80%. Một đồng xu được rút ngẫu nhiên từ túi (với xác suất rút mỗi đồng xu là như nhau), sau đó đồng xu được lật ba lần để tạo ra các kết quả $X_1$, $X_2$, và $X_3$.<br>

1.  Vẽ mạng Bayes tương ứng với thiết lập này và định nghĩa các CPT cần thiết.<br>

2.  Tính toán đồng xu nào có khả năng được rút ra từ túi nhất nếu các lần lật quan sát được cho ra hai mặt ngửa và một mặt sấp.


---

##### Bài tập 14.2

Chúng ta có một túi gồm ba đồng xu không cân bằng $a$, $b$, và $c$ với xác suất ra mặt ngửa lần lượt là 30%, 60%, và 75%. Một đồng xu được rút ngẫu nhiên từ túi (với xác suất rút mỗi đồng xu là như nhau), sau đó đồng xu được lật ba lần để tạo ra các kết quả $X_1$, $X_2$, và $X_3$.<br>

1.  Vẽ mạng Bayes tương ứng với thiết lập này và định nghĩa các CPT cần thiết.<br>

2.  Tính toán đồng xu nào có khả năng được rút ra từ túi nhất nếu các lần lật quan sát được cho ra hai mặt ngửa và một mặt sấp.<br>


---

##### Bài tập 14.3

Phương trình (<a href="#">parameter-joint-repn-equation</a> trên trang <a class="pageRef" title="" href="#">parameter-joint-repn-equation</a> định nghĩa phân phối liên hợp được biểu diễn bởi một mạng Bayes theo các tham số $\theta(X_i{{\,|\,}}{Parents}(X_i))$. Bài tập này yêu cầu bạn suy ra sự tương đương giữa các tham số và xác suất có điều kiện ${\textbf{ P}}(X_i{{\,|\,}}{Parents}(X_i))$ từ định nghĩa này.<br>

1.  Xem xét một mạng đơn giản $X\rightarrow Y\rightarrow Z$ với ba biến Boolean. Sử dụng các phương trình (<a class="equationRef" title="" href="#">conditional-probability-equation</a> và (<a class="pageRef" title="" href="#">marginalization-equation</a> (trang <a href="#">conditional-probability-equation</a> và <a href="#">marginalization-equation</a>) để biểu diễn xác suất có điều kiện $P(z{{\,|\,}}y)$ dưới dạng tỷ lệ của hai tổng, mỗi tổng trên các mục trong phân phối liên hợp ${\textbf{P}}(X,Y,Z)$.<br>

2.  Bây giờ sử dụng Phương trình (<a class="equationRef" title="" href="#">parameter-joint-repn-equation</a> để viết biểu thức này theo các tham số mạng $\theta(X)$, $\theta(Y{{\,|\,}}X)$, và $\theta(Z{{\,|\,}}Y)$.<br>

3.  Tiếp theo, khai triển các phép tổng trong biểu thức của bạn từ phần (b), viết rõ ràng các số hạng cho các giá trị đúng và sai của mỗi biến được tổng. Giả sử rằng tất cả các tham số mạng thỏa mãn ràng buộc $\sum_{x_i} \theta(x_i{{\,|\,}}{parents}(X_i)){{\,=\,}}1$, chứng minh rằng biểu thức kết quả rút gọn thành $\theta(z{{\,|\,}}y)$.<br>

4.  Tổng quát hóa suy luận này để chứng minh rằng $\theta(X_i{{\,|\,}}{Parents}(X_i)) = {\textbf{P}}(X_i{{\,|\,}}{Parents}(X_i))$ cho bất kỳ mạng Bayes nào.<br>


---

##### Bài tập 14.4

Thao tác <b>đảo ngược cung</b> trong mạng Bayes cho phép chúng ta thay đổi hướng của một cung $X\rightarrow Y$ trong khi vẫn bảo toàn phân phối xác suất liên hợp mà mạng biểu diễn <a class="paperRef" title="" href="">Shachter:1986</a>. Đảo ngược cung có thể yêu cầu giới thiệu các cung mới: tất cả các cha của $X$ cũng trở thành cha của $Y$, và tất cả các cha của $Y$ cũng trở thành cha của $X$.<br>

1.  Giả sử $X$ và $Y$ ban đầu có lần lượt $m$ và $n$ cha, và tất cả các biến có $k$ giá trị. Bằng cách tính toán sự thay đổi kích thước cho CPT của $X$ và $Y$, chứng minh rằng tổng số tham số trong mạng không thể giảm trong quá trình đảo ngược cung. (<i>Gợi ý</i>: các cha của $X$ và $Y$ không nhất thiết phải rời nhau.)<br>

2.  Trong trường hợp nào thì tổng số có thể không đổi?<br>

3.  Đặt các cha của $X$ là $\textbf{U} \cup \textbf{V}$ và các cha của $Y$ là $\textbf{V} \cup \textbf{W}$, trong đó $\textbf{U}$ và $\textbf{W}$ là rời nhau. Các công thức cho CPT mới sau khi đảo ngược cung như sau: $$\begin{aligned} {\textbf{P}}(Y | \textbf{U},\textbf{V},\textbf{W}) &=& \sum_x {\textbf{P}}(Y | \textbf{V},\textbf{W}, x) {\textbf{P}}(x | \textbf{U}, \textbf{V}) \\ {\textbf{P}}(X | \textbf{U},\textbf{V},\textbf{W}, Y) &=& {\textbf{P}}(Y | X, \textbf{V}, \textbf{W}) {\textbf{P}}(X | \textbf{U}, \textbf{V}) / {\textbf{P}}(Y | \textbf{U},\textbf{V},\textbf{W})\ .\end{aligned}$$
    Chứng minh rằng mạng mới biểu diễn cùng một phân phối liên hợp trên tất cả các biến như mạng ban đầu.<br>


---

##### Bài tập 14.5

Xem xét mạng Bayes trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/burglary-figure.png">burglary-figure.</a><br>

1.  Nếu không có bằng chứng nào được quan sát, thì ${Burglary}$ và ${Earthquake}$ có độc lập không? Chứng minh điều này từ ngữ nghĩa số học và từ ngữ nghĩa tô pô.<br>

2.  Nếu chúng ta quan sát ${Alarm}{{\,=\,}}{true}$, thì ${Burglary}$ và ${Earthquake}$ có độc lập không? Giải thích câu trả lời của bạn bằng cách tính toán xem các xác suất liên quan có thỏa mãn định nghĩa về sự độc lập có điều kiện hay không.<br>


---

###### Bài tập 14.6

Giả sử rằng trong một mạng Bayes chứa một biến chưa được quan sát $Y$, tất cả các biến trong mạng Markov ${MB}(Y)$ đã được quan sát.<br>

1.  Chứng minh rằng việc loại bỏ nút $Y$ khỏi mạng sẽ không ảnh hưởng đến phân phối hậu nghiệm cho bất kỳ biến chưa được quan sát nào khác trong mạng.<br>

2.  Thảo luận xem chúng ta có thể loại bỏ $Y$ hay không nếu chúng ta dự định sử dụng (i) lấy mẫu loại trừ và (ii) trọng số khả năng.<br>


    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/handedness1.svg" alt="handedness-figure" id="handedness-figure" style="width:100%">
      <figcaption><center><b>Ba cấu trúc có thể có cho một mạng Bayes mô tả sự di truyền thuận tay.</b></center></figcaption>
    </figure>


---

##### Bài tập 14.7

Đặt $H_x$ là một biến ngẫu nhiên biểu thị thuận tay của một cá nhân $x$, với các giá trị có thể là $l$ hoặc $r$. Một giả thuyết phổ biến là thuận tay trái hoặc phải được di truyền theo một cơ chế đơn giản; nghĩa là, có lẽ có một gen $G_x$, cũng có các giá trị $l$ hoặc $r$, và có lẽ thuận tay thực tế phần lớn giống nhau (với một xác suất $s$) như gen mà một cá nhân sở hữu. Hơn nữa, có lẽ gen tự nó có khả năng được di truyền như nhau từ một trong hai cha mẹ của một cá nhân, với một xác suất nhỏ khác không $m$ của một đột biến ngẫu nhiên làm đảo ngược thuận tay.<br>

1.  Ba mạng nào trong Hình <a class="insideExercisesFigRef" href="#handedness-figure">handedness-figure</a> khẳng định rằng $ {\textbf{P}}(G_{father},G_{mother},G_{child}) = {\textbf{P}}(G_{father}){\textbf{P}}(G_{mother}){\textbf{P}}(G_{child})$?<br>

2.  Ba mạng nào đưa ra các khẳng định độc lập nhất quán với giả thuyết về sự di truyền thuận tay?<br>

3.  Ba mạng nào là mô tả tốt nhất cho giả thuyết?<br>

4.  Viết bảng CPT cho nút $G_{child}$ trong mạng (a), theo $s$ và $m$.<br>

5.  Giả sử rằng $P(G_{father}{{\,=\,}}l)=P(G_{mother}{{\,=\,}}l)=q$. Trong mạng (a), hãy suy ra một biểu thức cho $P(G_{child}{{\,=\,}}l)$ chỉ theo $m$ và $q$, bằng cách điều kiện hóa trên các nút cha của nó.<br>

6.  Trong điều kiện cân bằng di truyền, chúng ta mong đợi phân phối gen sẽ giống nhau qua các thế hệ. Sử dụng điều này để tính giá trị của $q$, và, dựa trên những gì bạn biết về thuận tay ở người, giải thích tại sao giả thuyết được mô tả ở đầu câu hỏi này phải sai.<br>


---

###### Bài tập 14.8

<b>Mạng Markov</b> của một biến được định nghĩa trên trang <a href="#">markov-blanket-page</a>. Chứng minh rằng một biến độc lập với tất cả các biến khác trong mạng, khi biết mạng Markov của nó và suy ra Phương trình (<a class="equationRef" title="" href="#">markov-blanket-equation</a>) (trang <a class="pageRef" title="" href="#">markov-blanket-equation</a>).
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/car-starts.svg" alt="car-starts-figure" id="car-starts-figure" style="width:100%">
    <figcaption><center><b>Một mạng Bayes mô tả một số đặc điểm của hệ thống điện và động cơ ô tô. Mỗi biến là Boolean, và giá trị <i>true</i> cho biết khía cạnh tương ứng của xe đang hoạt động tốt.</b></center></figcaption>
</figure>


---

##### Bài tập 14.9

Xem xét mạng cho chẩn đoán ô tô được hiển thị trong Hình <a class="insideExercisesFigRef" href="#car-starts-figure">car-starts-figure</a><br>.

1.  Mở rộng mạng với các biến Boolean ${IcyWeather}$ và ${StarterMotor}$.<br>

2.  Đưa ra các bảng xác suất có điều kiện hợp lý cho tất cả các nút.<br>

3.  Có bao nhiêu giá trị độc lập trong phân phối xác suất liên hợp cho tám nút Boolean, giả sử không có mối quan hệ độc lập có điều kiện nào được biết là đúng giữa chúng?<br>

4.  Các bảng mạng của bạn chứa bao nhiêu giá trị xác suất độc lập?<br>

5.  Phân phối có điều kiện cho ${Starts}$ có thể được mô tả là phân phối <b>noisy-AND</b>. Định nghĩa họ này nói chung và liên hệ nó với phân phối noisy-OR.<br>


---

##### Bài tập 14.10

Xem xét họ mạng Bayes tuyến tính Gaussian, như được định nghĩa trên trang <a class="pageRef" title="" href="#">LG-network-page</a><br>.

1.  Trong một mạng hai biến, đặt $X_1$ là cha của $X_2$, đặt $X_1$ có phân phối tiên nghiệm Gaussian, và đặt ${\textbf{P}}(X_2{{\,|\,}}X_1)$ là một phân phối Gaussian tuyến tính. Chứng minh rằng phân phối liên hợp $P(X_1,X_2)$ là một Gaussian đa biến, và tính toán ma trận hiệp phương sai của nó.<br>

2.  Chứng minh bằng quy nạp rằng phân phối liên hợp cho một mạng Gaussian tuyến tính tổng quát trên $X_1,\ldots,X_n$ cũng là một Gaussian đa biến.<br>


---

##### Bài tập 14.11

Phân phối probit được định nghĩa trên trang <a class="pageRef" title="" href="#">probit-page</a> mô tả phân phối xác suất cho một con có điều kiện Boolean, khi biết một cha liên tục duy nhất.<br>

1.  Định nghĩa có thể được mở rộng như thế nào để bao gồm nhiều cha liên tục?<br>

2.  Nó có thể được mở rộng như thế nào để xử lý một biến con <i>đa giá trị</i>? Xem xét cả hai trường hợp mà các giá trị của con được sắp xếp (như khi chọn số truyền khi lái xe, tùy thuộc vào tốc độ, độ dốc, gia tốc mong muốn, v.v.) và các trường hợp mà chúng không được sắp xếp (như khi chọn xe buýt, tàu hỏa hoặc ô tô để đi làm). (<i>Gợi ý</i>: Xem xét các cách để chia các giá trị có thể có thành hai tập hợp, để bắt chước một biến Boolean.)<br>


---

##### Bài tập 14.12

Tại nhà máy điện hạt nhân địa phương của bạn, có một báo động cảm nhận khi một đồng hồ đo nhiệt độ vượt quá một ngưỡng nhất định. Đồng hồ đo nhiệt độ của lõi. Xem xét các biến Boolean $A$ (báo động kêu), $F_A$ (báo động bị lỗi), và $F_G$ (đồng hồ đo bị lỗi) và các nút đa giá trị $G$ (chỉ số đồng hồ đo) và $T$ (nhiệt độ lõi thực tế).<br>

1.  Vẽ một mạng Bayes cho miền này, với giả định rằng đồng hồ đo có nhiều khả năng bị lỗi khi nhiệt độ lõi quá cao.<br>

2.  Mạng của bạn có phải là một polytree không? Tại sao có hoặc tại sao không?<br>

3.  Giả sử chỉ có hai nhiệt độ thực tế và đo được có thể có, bình thường và cao; xác suất đồng hồ đo cho nhiệt độ chính xác là $x$ khi nó hoạt động, nhưng $y$ khi nó bị lỗi. Đưa ra bảng xác suất có điều kiện liên quan đến $G$.<br>

4.  Giả sử báo động hoạt động chính xác trừ khi nó bị lỗi, trong trường hợp đó nó không bao giờ kêu. Đưa ra bảng xác suất có điều kiện liên quan đến $A$.<br>

5.  Giả sử báo động và đồng hồ đo đang hoạt động và báo động kêu. Tính toán một biểu thức cho xác suất nhiệt độ lõi quá cao, theo các xác suất có điều kiện khác nhau trong mạng.<br>


---

##### Bài tập 14.13

Hai nhà thiên văn học ở các nơi khác nhau trên thế giới thực hiện các phép đo $M_1$ và $M_2$ về số lượng sao $N$ trong một vùng nhỏ trên bầu trời, sử dụng kính thiên văn của họ. Thông thường, có một khả năng nhỏ $e$ sai số lên đến một sao ở mỗi hướng. Mỗi kính thiên văn cũng có thể (với xác suất nhỏ hơn nhiều $f$) bị mất nét nghiêm trọng (các sự kiện $F_1$ và $F_2$), trong trường hợp đó nhà khoa học sẽ đếm thiếu ba sao trở lên (hoặc nếu $N$ nhỏ hơn 3, không phát hiện được sao nào cả). Xem xét ba mạng được hiển thị trong Hình <a class="insideExercisesFigRef" href="#telescope-nets-figure">telescope-nets-figure</a>.<br>

1.  Ba mạng Bayes nào trong số này là biểu diễn chính xác (nhưng không nhất thiết hiệu quả) của thông tin trước đó?<br>

2.  Mạng nào là tốt nhất? Giải thích.<br>

3.  Viết ra một phân phối có điều kiện cho ${\textbf{P}}(M_1{{\,|\,}}N)$, cho trường hợp $N{{\,\in\\,}}\{1,2,3\}$ và $M_1{{\,\in\\,}}\{0,1,2,3,4\}$. Mỗi mục trong phân phối có điều kiện nên được biểu thị dưới dạng hàm của các tham số $e$ và/hoặc $f$.<br>

4.  Giả sử $M_1{{\,=\,}}1$ và $M_2{{\,=\,}}3$. Có bao nhiêu số sao <i>có thể có</i> nếu bạn giả định không có ràng buộc tiên nghiệm nào về các giá trị của $N$?<br>

5.  Số lượng sao <i>có khả năng nhất</i> là bao nhiêu, với các quan sát này? Giải thích cách tính toán, hoặc nếu không thể tính toán, giải thích thông tin bổ sung nào là cần thiết và nó sẽ ảnh hưởng đến kết quả như thế nào.<br>


---

###### Bài tập 14.14

Xem xét mạng trong Hình <a class="insideExercisesFigRef" href="#telescope-nets-figure">(ii)</a>, và giả sử hai kính thiên văn hoạt động giống hệt nhau. $N{{\,\in\\,}}\{1,2,3\}$ và $M_1,M_2{{\,\in\\,}}\{0,1,2,3,4\}$, với các CPT tượng trưng như được mô tả trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/bayes-nets-exercises/ex_14/">telescope-exercise</a>. Sử dụng thuật toán lấy mẫu liệt kê (Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/enumeration-algorithm.png">enumeration-algorithm</a> trên trang <a class="pageRef" title="" href="#">enumeration-algorithm</a>), tính toán phân phối xác suất ${\textbf{P}}(N{{\,|\,}}M_1{{\,=\,}}2,M_2{{\,=\,}}2)$.<br>


<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/telescope-nets.svg" alt="telescope-nets-figure" id="telescope-nets-figure" style="width:100%">
  <figcaption><center><b>Ba mạng có thể có cho bài toán kính thiên văn.</b></center></figcaption>
</figure>


---

###### Bài tập 14.15

Xem xét mạng Bayes trong Hình <a class="insideExercisesFigRef" href="#politics-figure">politics-figure</a><br>.

1.  Cấu trúc mạng khẳng định điều nào sau đây?<br>

    1.  ${\textbf{P}}(B,I,M) = {\textbf{P}}(B){\textbf{P}}(I){\textbf{P}}(M)$.<br>

    2.  ${\textbf{P}}(J|G) = {\textbf{P}}(J|G,I)$.<br>

    3.  ${\textbf{P}}(M|G,B,I) = {\textbf{P}}(M|G,B,I,J)$.<br>

2.  Tính giá trị của $P(b,i,\lnot m,g,j)$.<br>

3.  Tính xác suất một người bị bỏ tù biết rằng họ đã vi phạm pháp luật, bị truy tố và đối mặt với một công tố viên có động cơ chính trị.<br>

4.  <b>Sự độc lập theo ngữ cảnh cụ thể</b> (xem trang <a class="pageRef" title="" href="#">CSI-page</a>) cho phép một biến độc lập với một số cha của nó khi biết các giá trị nhất định của những biến khác. Ngoài các sự độc lập có điều kiện thông thường được cho bởi cấu trúc đồ thị, những sự độc lập theo ngữ cảnh cụ thể nào tồn tại trong mạng Bayes trong Hình <a class="insideExercisesFigRef" href="#politics-figure">politics-figure</a>?<br>

5.  Giả sử chúng ta muốn thêm biến $P={PresidentialPardon}$ vào mạng; vẽ mạng mới và giải thích ngắn gọn bất kỳ liên kết nào bạn thêm.<br>
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/politics.svg" alt="politics-figure" id="politics-figure" style="width:100%">
  <figcaption><center><b>Một mạng Bayes đơn giản với các biến Boolean B = {BrokeElectionLaw}, I = {Indicted}, M = {PoliticallyMotivatedProsecutor}, G= {FoundGuilty}, J = {Jailed}.</b></center></figcaption>
</figure>


---

##### Bài tập 14.16

Xem xét mạng Bayes trong Hình <a class="insideExercisesFigRef" href="#politics-figure">politics-figure</a><br>.

1.  Cấu trúc mạng khẳng định điều nào sau đây?<br>

    1.  ${\textbf{P}}(B,I,M) = {\textbf{P}}(B){\textbf{P}}(I){\textbf{P}}(M)$.<br>

    2.  ${\textbf{P}}(J|G) = {\textbf{P}}(J|G,I)$.<br>

    3.  ${\textbf{P}}(M|G,B,I) = {\textbf{P}}(M|G,B,I,J)$.<br>

2.  Tính giá trị của $P(b,i,\lnot m,g,j)$.<br>

3.  Tính xác suất một người bị bỏ tù biết rằng họ đã vi phạm pháp luật, bị truy tố và đối mặt với một công tố viên có động cơ chính trị.<br>

4.  <b>Sự độc lập theo ngữ cảnh cụ thể</b> (xem trang <a class="pageRef" id="pageref" title="" href="#">CSI-page</a>) cho phép một biến độc lập với một số cha của nó khi biết các giá trị nhất định của những biến khác. Ngoài các sự độc lập có điều kiện thông thường được cho bởi cấu trúc đồ thị, những sự độc lập theo ngữ cảnh cụ thể nào tồn tại trong mạng Bayes trong Hình <a class="insideExercisesFigRef" id="insideexercisesfigref" href="#politics-figure">politics-figure</a>?<br>

5.  Giả sử chúng ta muốn thêm biến $P={PresidentialPardon}$ vào mạng; vẽ mạng mới và giải thích ngắn gọn bất kỳ liên kết nào bạn thêm.<br>


---

##### Bài tập 14.17

Xem xét thuật toán loại bỏ biến trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/elimination-ask-algorithm.png">elimination-ask-algorithm</a> (trang <a class="pageRef" title="" href="#">elimination-ask-algorithm</a>).<br>

1.  Phần <a class="sectionRef" title="" href="#">exact-inference-section</a> áp dụng loại bỏ biến cho truy vấn $${\textbf{P}}({Burglary}{{\,|\,}}{JohnCalls}{{\,=\,}}{true},{MaryCalls}{{\,=\,}}{true})\ .$$
    Thực hiện các phép tính được chỉ định và kiểm tra xem câu trả lời có đúng không.<br>

2.  Đếm số phép toán số học được thực hiện và so sánh nó với số phép toán được thực hiện bởi thuật toán liệt kê.<br>

3.  Giả sử một mạng có dạng một <i>chuỗi</i>: một dãy các biến Boolean $X_1,\ldots, X_n$ trong đó ${Parents}(X_i){{\,=\,}}\{X_{i-1}\}$ cho $i{{\,=\,}}2,\ldots,n$. Độ phức tạp của việc tính toán ${\textbf{P}}(X_1{{\,|\,}}X_n{{\,=\,}}{true})$ bằng cách liệt kê là bao nhiêu? Bằng cách loại bỏ biến?<br>

4.  Chứng minh rằng độ phức tạp của việc chạy loại bỏ biến trên một mạng polytree là tuyến tính theo kích thước của cây cho bất kỳ thứ tự biến nào phù hợp với cấu trúc mạng.<br>


---

##### Bài tập 14.18

Điều tra độ phức tạp của suy luận chính xác trong các mạng Bayes nói chung:<br>

1.  Chứng minh rằng bất kỳ bài toán 3-SAT nào cũng có thể được quy về suy luận chính xác trong một mạng Bayes được xây dựng để biểu diễn bài toán cụ thể và do đó suy luận chính xác là NP-hard. (<i>Gợi ý</i>: Xem xét một mạng có một biến cho mỗi ký hiệu mệnh đề, một cho mỗi mệnh đề, và một cho phép hội của các mệnh đề.)<br>

2.  Bài toán đếm số lượng các phép gán thỏa mãn cho một bài toán 3-SAT là \#P-complete. Chứng minh rằng suy luận chính xác ít nhất khó bằng bài toán này.<br>


---

##### Bài tập 14.19

Xem xét vấn đề tạo một mẫu ngẫu nhiên từ một phân phối được chỉ định trên một biến duy nhất. Giả sử bạn có một trình tạo số ngẫu nhiên trả về một số ngẫu nhiên phân phối đều trong khoảng từ 0 đến 1.<br>

1.  Đặt $X$ là một biến rời rạc với $P(X{{\,=\,}}x_i){{\,=\,}}p_i$ cho $i{{\,\in\\,}}\{1,\ldots,k\}$. <b>Phân phối tích lũy</b> của $X$ cho xác suất $X{{\,\in\\,}}\{x_1,\ldots,x_j\}$ cho mỗi $j$ có thể có. (Xem thêm Phụ lục [math-appendix].) Giải thích cách tính phân phối tích lũy trong thời gian $O(k)$ và cách tạo một mẫu duy nhất của $X$ từ nó. Mẫu thứ hai có thể được thực hiện trong thời gian ít hơn $O(k)$ không?<br>

2.  Bây giờ giả sử chúng ta muốn tạo $N$ mẫu của $X$, trong đó $N\gg k$. Giải thích cách thực hiện điều này với thời gian chạy kỳ vọng trên mỗi mẫu là <i>hằng số</i> (tức là độc lập với $k$).<br>

3.  Bây giờ xem xét một biến có giá trị liên tục với phân phối tham số hóa (ví dụ: Gaussian). Làm thế nào để tạo mẫu từ một phân phối như vậy?<br>

4.  Giả sử bạn muốn truy vấn một biến có giá trị liên tục và bạn đang sử dụng một thuật toán lấy mẫu như LIKELIHOODWEIGHTING để thực hiện suy luận. Bạn sẽ phải sửa đổi quy trình trả lời truy vấn như thế nào?<br>


---

##### Bài tập 14.20

Xem xét truy vấn ${\textbf{P}}({Rain}{{\,|\,}}{Sprinkler}{{\,=\,}}{true},{WetGrass}{{\,=\,}}{true})$ trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/rain-clustering-figure.png">rain-clustering-figure</a>(a) (trang <a class="pageRef" title="" href="#">rain-clustering-figure</a>) và cách Gibbs sampling có thể trả lời nó.<br>

1.  Chuỗi Markov có bao nhiêu trạng thái?<br>

2.  Tính toán <b>ma trận chuyển tiếp</b> ${\textbf{Q}}$ chứa $q({\textbf{y}}$ $\rightarrow$ ${\textbf{y}}')$ cho tất cả ${\textbf{y}}$, ${\textbf{y}}'$.<br>

3.  ${\textbf{ Q}}^2$, bình phương của ma trận chuyển tiếp, đại diện cho điều gì?<br>

4.  Còn ${\textbf{Q}}^n$ khi $n\to \infty$ thì sao?<br>

5.  Giải thích cách thực hiện suy luận xác suất trong mạng Bayes, giả sử ${\textbf{Q}}^n$ có sẵn. Đây có phải là một cách thực tế để thực hiện suy luận không?<br>


---

##### Bài tập 14.21

Bài tập này khám phá phân phối dừng cho các phương pháp Gibbs sampling.<br>

1.  Tổ hợp lồi $[\alpha, q_1; 1-\alpha, q_2]$ của $q_1$ và $q_2$ là một phân phối xác suất chuyển tiếp mà trước tiên chọn một trong $q_1$ và $q_2$ với xác suất $\alpha$ và $1-\alpha$, tương ứng, sau đó áp dụng bất kỳ cái nào được chọn. Chứng minh rằng nếu $q_1$ và $q_2$ cân bằng chi tiết với $\pi$, thì tổ hợp lồi của chúng cũng cân bằng chi tiết với $\pi$. (<i>Lưu ý</i>: kết quả này biện minh cho một biến thể của GIBBS-ASK trong đó các biến được chọn ngẫu nhiên thay vì lấy mẫu theo một trình tự cố định.)<br>

2.  Chứng minh rằng nếu mỗi $q_1$ và $q_2$ có $\pi$ là phân phối dừng của chúng, thì tổ hợp tuần tự $q {{\,=\,}}q_1 \circ q_2$ cũng có $\pi$ là phân phối dừng của chúng.<br>


---

##### Bài tập 14.22

Thuật toán <b>Metropolis--Hastings</b> là một thành viên của họ MCMC; do đó, nó được thiết kế để tạo ra các mẫu $\textbf{x}$ (cuối cùng) theo xác suất mục tiêu $\pi(\textbf{x})$. (Thông thường chúng ta quan tâm đến việc lấy mẫu từ $\pi(\textbf{x}){{\,=\,}}P(\textbf{x}{{\,|\,}}\textbf{e})$.) Giống như simulated annealing, Metropolis–Hastings hoạt động theo hai giai đoạn. Đầu tiên, nó lấy mẫu một trạng thái mới $\textbf{x'}$ từ <b>phân phối đề xuất</b> $q(\textbf{x'}{{\,|\,}}\textbf{x})$, khi biết trạng thái hiện tại $\textbf{x}$. Sau đó, nó chấp nhận hoặc từ chối $\textbf{x'}$ một cách có xác suất theo <b>xác suất chấp nhận</b> $$\alpha(\textbf{x'}{{\,|\,}}\textbf{x}) = \min\ \left(1,\frac{\pi(\textbf{x'})q(\textbf{x}{{\,|\,}}\textbf{x'})}{\pi(\textbf{x})q(\textbf{x'}{{\,|\,}}\textbf{x})}  \right)\ .$$
Nếu đề xuất bị từ chối, trạng thái vẫn ở $\textbf{x}$.<br>

1.  Xem xét một bước Gibbs sampling thông thường cho một biến cụ thể $X_i$. Chứng minh rằng bước này, được xem như một đề xuất, được đảm bảo sẽ được chấp nhận bởi Metropolis–Hastings. (Do đó, Gibbs sampling là một trường hợp đặc biệt của Metropolis–Hastings.)<br>

2.  Chứng minh rằng quy trình hai bước trên, được xem như một phân phối xác suất chuyển tiếp, cân bằng chi tiết với $\pi$.<br>


---

##### Bài tập 14.23

Ba đội bóng đá $A$, $B$, và $C$, thi đấu với nhau một lần. Mỗi trận đấu là giữa hai đội, và có thể thắng, hòa, hoặc thua. Mỗi đội có một mức độ chất lượng cố định, không xác định—một số nguyên trong khoảng từ 0 đến 3—và kết quả của một trận đấu phụ thuộc một cách có xác suất vào sự khác biệt về chất lượng giữa hai đội.<br>

1.  Xây dựng một mô hình xác suất quan hệ để mô tả miền này, và đề xuất các giá trị số cho tất cả các phân phối xác suất cần thiết.<br>

2.  Xây dựng mạng Bayes tương đương cho ba trận đấu.<br>

3.  Giả sử rằng trong hai trận đấu đầu tiên $A$ đánh bại $B$ và hòa với $C$. Sử dụng một thuật toán suy luận chính xác tùy chọn của bạn, tính toán phân phối hậu nghiệm cho kết quả của trận đấu thứ ba.<br>

4.  Giả sử có $n$ đội trong giải đấu và chúng ta có kết quả của tất cả các trận đấu trừ trận cuối cùng. Độ phức tạp của việc dự đoán trận đấu cuối cùng thay đổi với $n$ như thế nào?<br>

5.  Điều tra việc áp dụng MCMC cho bài toán này. Nó hội tụ nhanh như thế nào trong thực tế và nó mở rộng tốt như thế nào?<br>


---

<!-- tabs:end -->
