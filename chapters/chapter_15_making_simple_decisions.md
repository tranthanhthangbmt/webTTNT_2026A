# Chapter 15 Making simple decisions

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_15_Making%20simple%20decisions/chapter_15_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_15_Making%20simple%20decisions.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter15_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter15_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter15/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/oupm.md" target="_blank" data-ignore>OUPM</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/net-visa.md" target="_blank" data-ignore>NET-VISA</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/radar.md" target="_blank" data-ignore>RADAR</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/generate-image.md" target="_blank" data-ignore>GENERATE-IMAGE</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/generate-markov-letters.md" target="_blank" data-ignore>GENERATE-MARKOV-LETTERS</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Dynamic Decision Network**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/dynamic_decision_network.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/dynamic_decision_network.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/dynamic_decision_network.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 15.1

Chứng minh rằng mọi quá trình Markov bậc hai đều có thể được viết lại thành quá trình Markov bậc nhất với tập biến trạng thái được tăng cường. Liệu điều này có thể luôn luôn được thực hiện một cách <i>tiết kiệm</i>, tức là, mà không làm tăng số lượng tham số cần thiết để xác định mô hình chuyển tiếp không?


---

##### Bài tập 15.2

Trong bài tập này, chúng ta xem xét điều gì xảy ra với các xác suất trong thế giới ô dù khi chuỗi thời gian trở nên rất dài.<br>

1. Giả sử chúng ta quan sát một chuỗi ngày không ngừng nghỉ mà trong đó chiếc ô xuất hiện. Chứng minh rằng, khi các ngày trôi qua, xác suất mưa vào ngày hiện tại tăng đơn điệu về một điểm cố định. Tính toán điểm cố định này.<br>

2. Bây giờ, hãy xem xét việc <i>dự báo</i> xa hơn và xa hơn vào tương lai, chỉ dựa trên hai quan sát ô đầu tiên. Đầu tiên, tính toán xác suất $P(r_{2+k}|u_1,u_2)$ cho $k=1 \ldots 20$ và vẽ biểu đồ kết quả. Bạn sẽ thấy rằng xác suất hội tụ về một điểm cố định. Chứng minh rằng giá trị chính xác của điểm cố định này là 0.5.


---

##### Bài tập 15.3

Bài tập này phát triển một biến thể tiết kiệm không gian của thuật toán forward–backward được mô tả trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/forward-backward-algorithm.png">forward-backward-algorithm</a> (trang <a class="pageRef" title="" href="#">forward-backward-algorithm</a>). Chúng ta muốn tính $\textbf{P} (\textbf{X}_k|\textbf{e}_{1:t})$ cho $k=1,\ldots ,t$. Điều này sẽ được thực hiện bằng phương pháp chia để trị.<br>

1. Giả sử, để đơn giản, rằng $t$ là số lẻ, và điểm giữa là $h=(t+1)/2$. Chứng minh rằng $\textbf{P} (\textbf{X}_k|\textbf{e}_{1:t}) $ có thể được tính cho $k=1,\ldots ,h$ chỉ với thông điệp forward ban đầu $\textbf{f}_{1:0}$, thông điệp backward $\textbf{b}_{h+1:t}$, và bằng chứng $\textbf{e}_{1:h}$.<br>

2. Chứng minh một kết quả tương tự cho nửa sau của chuỗi.<br>

3. Dựa trên kết quả của (a) và (b), một thuật toán chia để trị đệ quy có thể được xây dựng bằng cách chạy forward dọc theo chuỗi trước, sau đó chạy backward từ cuối, chỉ lưu trữ các thông điệp cần thiết ở giữa và ở các đầu. Sau đó, thuật toán được gọi trên mỗi nửa. Viết chi tiết thuật toán.<br>

4. Tính toán độ phức tạp về thời gian và không gian của thuật toán theo $t$, độ dài của chuỗi. Điều này thay đổi như thế nào nếu chúng ta chia đầu vào thành nhiều hơn hai phần?<br>


---

##### Bài tập 15.4

Trên trang <a class="pageRef" title="" href="#">flawed-viterbi-page</a>, chúng tôi đã phác thảo một quy trình sai lầm để tìm chuỗi trạng thái có khả năng xảy ra nhất, với một chuỗi quan sát. Quy trình này bao gồm việc tìm trạng thái có khả năng xảy ra nhất tại mỗi bước thời gian, sử dụng làm mịn, và trả về chuỗi bao gồm các trạng thái này. Chứng minh rằng, đối với một số mô hình xác suất thời gian và chuỗi quan sát, quy trình này trả về một chuỗi trạng thái không thể xảy ra (tức là, xác suất hậu nghiệm của chuỗi bằng không).


---

##### Bài tập 15.5

Phương trình (<a class="equationRef" title="" href="#">matrix-filtering-equation</a>) mô tả quá trình lọc cho công thức ma trận của HMM. Đưa ra một phương trình tương tự cho việc tính toán các likelihood, được mô tả chung trong Phương trình (<a class="equationRef" title="" href="#">forward-likelihood-equation</a>).


---

##### Bài tập 15.6

Xem xét các thế giới hút bụi của Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-maze-ch4-figure.png">vacuum-maze-ch4-figure</a> (cảm biến hoàn hảo) và Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-maze-hmm2-figure.png">vacuum-maze-hmm2-figure</a> (cảm biến nhiễu). Giả sử rằng robot nhận được một chuỗi quan sát sao cho, với cảm biến hoàn hảo, chỉ có một vị trí khả dĩ mà nó có thể ở đó. Liệu vị trí này có nhất thiết là vị trí có khả năng xảy ra nhất dưới cảm biến nhiễu với xác suất nhiễu $\epsilon$ đủ nhỏ không? Chứng minh khẳng định của bạn hoặc tìm một phản ví dụ.


---

##### Bài tập 15.7

Trong Mục <a class="sectionRef" title="" href="#">hmm-localization-section</a>, phân phối tiên nghiệm trên các vị trí là đồng nhất và mô hình chuyển tiếp giả định xác suất di chuyển đến bất kỳ ô vuông lân cận nào là như nhau. Điều gì sẽ xảy ra nếu các giả định đó sai? Giả sử vị trí ban đầu thực sự được chọn đồng nhất từ góc phần tư tây bắc của căn phòng và hành động thực tế có xu hướng di chuyển về phía đông nam. Giữ nguyên mô hình HMM, khám phá ảnh hưởng đến độ chính xác của định vị và đường đi khi xu hướng đông nam tăng lên, với các giá trị khác nhau của $\epsilon$.


---

##### Bài tập 15.8

Xem xét một phiên bản của robot hút bụi (trang <a class="pageRef" title="" href="#">vacuum-maze-hmm2-figure</a>) có chính sách đi thẳng càng lâu càng tốt; chỉ khi gặp chướng ngại vật, nó mới chuyển sang một hướng mới (được chọn ngẫu nhiên). Để mô hình hóa robot này, mỗi trạng thái trong mô hình bao gồm một cặp <i>(vị trí, hướng)</i>. Triển khai mô hình này và xem thuật toán Viterbi có thể theo dõi robot với mô hình này tốt như thế nào. Chính sách của robot bị ràng buộc hơn robot đi ngẫu nhiên; điều đó có nghĩa là dự đoán về đường đi có khả năng xảy ra nhất sẽ chính xác hơn không?


---

##### Bài tập 15.9

Chúng ta đã mô tả ba chính sách cho robot hút bụi: (1) đi bộ ngẫu nhiên đồng nhất, (2) thiên về đi lang thang về phía đông nam, như được mô tả trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_7/">hmm-robust-exercise</a>, và (3) chính sách được mô tả trong Bài tập <a href="#">roomba-viterbi-exercise</a>. Giả sử một người quan sát nhận được chuỗi quan sát từ một robot hút bụi, nhưng không chắc chắn robot đang tuân theo một trong ba chính sách nào. Người quan sát nên sử dụng phương pháp nào để tìm đường đi có khả năng xảy ra nhất, với các quan sát đã cho? Triển khai phương pháp này và kiểm tra nó. Độ chính xác định vị bị suy giảm bao nhiêu, so với trường hợp người quan sát biết chính sách mà robot đang tuân theo?


---

##### Bài tập 15.10

Bài tập này liên quan đến lọc trong một môi trường không có mốc. Xem xét một robot hút bụi trong một căn phòng trống, được biểu diễn bằng một lưới chữ nhật $n \times m$. Vị trí của robot bị ẩn; bằng chứng duy nhất có sẵn cho người quan sát là một cảm biến vị trí nhiễu cung cấp một ước tính gần đúng về vị trí của robot. Nếu robot ở vị trí $(x, y)$ thì với xác suất 0.1 cảm biến cho vị trí chính xác, với xác suất 0.05 mỗi lần nó báo cáo một trong 8 vị trí ngay xung quanh $(x, y)$, với xác suất 0.025 mỗi lần nó báo cáo một trong 16 vị trí bao quanh 8 vị trí đó, và với xác suất còn lại là 0.1 nó báo cáo "không có đọc". Chính sách của robot là chọn một hướng và đi theo hướng đó với xác suất 0.8 ở mỗi bước; robot chuyển sang một hướng mới được chọn ngẫu nhiên với xác suất 0.2 (hoặc với xác suất 1 nếu nó gặp tường). Triển khai điều này như một HMM và thực hiện lọc để theo dõi robot. Chúng ta có thể theo dõi đường đi của robot chính xác đến mức nào?


---

###### Bài tập 15.11

Bài tập này liên quan đến lọc trong một môi trường không có mốc. Xem xét một robot hút bụi trong một căn phòng trống, được biểu diễn bằng một lưới chữ nhật $n \times m$. Vị trí của robot bị ẩn; bằng chứng duy nhất có sẵn cho người quan sát là một cảm biến vị trí nhiễu cung cấp một ước tính gần đúng về vị trí của robot. Nếu robot ở vị trí $(x, y)$ thì với xác suất 0.1 cảm biến cho vị trí chính xác, với xác suất 0.05 mỗi lần nó báo cáo một trong 8 vị trí ngay xung quanh $(x, y)$, với xác suất 0.025 mỗi lần nó báo cáo một trong 16 vị trí bao quanh 8 vị trí đó, và với xác suất còn lại là 0.1 nó báo cáo "không có đọc". Chính sách của robot là chọn một hướng và đi theo hướng đó với xác suất 0.7 ở mỗi bước; robot chuyển sang một hướng mới được chọn ngẫu nhiên với xác suất 0.3 (hoặc với xác suất 1 nếu nó gặp tường). Triển khai điều này như một HMM và thực hiện lọc để theo dõi robot. Chúng ta có thể theo dõi đường đi của robot chính xác đến mức nào?

<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/switching-kf.svg" alt="switching-kf-figure" id="switching-kf-figure" style="width:100%">
  <figcaption><center><b>Một biểu diễn mạng Bayesian của bộ lọc Kalman chuyển mạch. Biến chuyển mạch $S_t$ là một biến trạng thái rời rạc có giá trị xác định mô hình chuyển tiếp cho các biến trạng thái liên tục $\textbf{X}_t$. Đối với bất kỳ trạng thái rời rạc $\textit{i}$ nào, mô hình chuyển tiếp $\textbf{P}(\textbf{X}_{t+1}|\textbf{X}_t,S_t= i)$ là một mô hình Gaussian tuyến tính, giống như trong bộ lọc Kalman thông thường. Mô hình chuyển tiếp cho trạng thái rời rạc, $\textbf{P}(S_{t+1}|S_t)$, có thể được coi là một ma trận, giống như trong mô hình Markov ẩn.</b></center></figcaption>
</figure>


---

##### Bài tập 15.12

Thông thường, chúng ta muốn giám sát một hệ thống trạng thái liên tục có hành vi chuyển đổi không thể đoán trước giữa một tập hợp $k$ "chế độ" riêng biệt. Ví dụ, một máy bay cố gắng né tránh tên lửa có thể thực hiện một loạt các thao tác khác nhau mà tên lửa có thể cố gắng theo dõi. Một biểu diễn mạng Bayesian của mô hình <b>switching Kalman filter</b> như vậy được hiển thị trong Hình <a class="insideExercisesFigRef"  href="#switching-kf-figure">switching-kf-figure</a>.<br><br>

1. Giả sử trạng thái rời rạc $S_t$ có $k$ giá trị khả dĩ và ước tính trạng thái liên tục tiên nghiệm ${\textbf{P}}(\textbf{X}_0)$ là một phân phối Gaussian đa biến. Chứng minh rằng dự đoán ${\textbf{P}}(\textbf{X}_1)$ là một <b>hỗn hợp các phân phối Gaussian</b>—tức là, một tổng có trọng số của các phân phối Gaussian sao cho các trọng số có tổng bằng 1.<br><br>

2. Chứng minh rằng nếu ước tính trạng thái liên tục hiện tại ${\textbf{P}}(\textbf{X}_t|\textbf{e}_{1:t})$ là một hỗn hợp của $m$ phân phối Gaussian, thì trong trường hợp tổng quát, ước tính trạng thái cập nhật ${\textbf{P}}(\textbf{X}_{t+1}|\textbf{e}_{1:t+1})$ sẽ là một hỗn hợp của $km$ phân phối Gaussian.<br><br>

3. Khía cạnh nào của quá trình thời gian mà các trọng số trong hỗn hợp Gaussian đại diện?<br><br>

Các kết quả trong (a) và (b) cho thấy rằng biểu diễn của hậu nghiệm tăng lên không giới hạn ngay cả đối với các bộ lọc Kalman chuyển mạch, vốn là một trong những mô hình động lai đơn giản nhất.


---

##### Bài tập 15.13

Hoàn thành bước còn thiếu trong quá trình suy luận Phương trình (<a class="equationRef" title="" href="#">kalman-one-step-equation</a>) trên trang <a class="pageRef" title="" href="#">kalman-one-step-equation</a>, bước cập nhật đầu tiên cho bộ lọc Kalman một chiều.


---

##### Bài tập 15.14

Hãy xem xét hành vi của cập nhật phương sai trong Phương trình (<a class="equationRef" title="" href="#">kalman-univariate-equation</a>) (trang <a class="pageRef" title="" href="#">kalman-univariate-equation</a>).<br>

1. Vẽ biểu đồ giá trị của $\sigma_t^2$ theo $t$, với các giá trị khác nhau cho $\sigma_x^2$ và $\sigma_z^2$.<br>

2. Chứng minh rằng phép cập nhật có một điểm cố định $\sigma^2$ sao cho $\sigma_t^2 \rightarrow \sigma^2$ khi $t \rightarrow \infty$, và tính giá trị của $\sigma^2$.<br>

3. Đưa ra một lời giải thích định tính về những gì xảy ra khi $\sigma_x^2\rightarrow 0$ và khi $\sigma_z^2\rightarrow 0$.


---

##### Bài tập 15.15

Một giáo sư muốn biết liệu sinh viên có ngủ đủ giấc hay không. Mỗi ngày, giáo sư quan sát xem sinh viên có ngủ trong lớp hay không, và liệu họ có bị đỏ mắt hay không. Giáo sư có lý thuyết miền sau:<br>

- Xác suất tiên nghiệm của việc ngủ đủ giấc, khi không có quan sát nào, là 0.7.<br>

- Xác suất ngủ đủ giấc vào đêm $t$ là 0.8 nếu sinh viên đã ngủ đủ giấc vào đêm trước, và 0.3 nếu không.<br>

- Xác suất bị đỏ mắt là 0.2 nếu sinh viên ngủ đủ giấc, và 0.7 nếu không.<br>

- Xác suất ngủ trong lớp là 0.1 nếu sinh viên ngủ đủ giấc, và 0.3 nếu không.<br>

Xây dựng thông tin này thành một mạng Bayesian động mà giáo sư có thể sử dụng để lọc hoặc dự đoán từ một chuỗi các quan sát. Sau đó, xây dựng lại nó thành một mô hình Markov ẩn chỉ có một biến quan sát duy nhất. Đưa ra các bảng xác suất hoàn chỉnh cho mô hình.<br>


---

##### Bài tập 15.16

Một giáo sư muốn biết liệu sinh viên có ngủ đủ giấc hay không. Mỗi ngày, giáo sư quan sát xem sinh viên có ngủ trong lớp hay không, và liệu họ có bị đỏ mắt hay không. Giáo sư có lý thuyết miền sau:<br>

- Xác suất tiên nghiệm của việc ngủ đủ giấc, khi không có quan sát nào, là 0.7.<br>

- Xác suất ngủ đủ giấc vào đêm $t$ là 0.8 nếu sinh viên đã ngủ đủ giấc vào đêm trước, và 0.3 nếu không.<br>

- Xác suất bị đỏ mắt là 0.2 nếu sinh viên ngủ đủ giấc, và 0.7 nếu không.<br>

- Xác suất ngủ trong lớp là 0.1 nếu sinh viên ngủ đủ giấc, và 0.3 nếu không.<br>

Xây dựng thông tin này thành một mạng Bayesian động mà giáo sư có thể sử dụng để lọc hoặc dự đoán từ một chuỗi các quan sát. Sau đó, xây dựng lại nó thành một mô hình Markov ẩn chỉ có một biến quan sát duy nhất. Đưa ra các bảng xác suất hoàn chỉnh cho mô hình.<br>


---

##### Bài tập 15.17

Đối với DBN được chỉ định trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_15/">sleep1-exercise</a> và các giá trị bằng chứng<br>

$\textbf{e}_1 = không\space đỏ\space mắt,\space không\space ngủ\space trong\space lớp$<br>
$\textbf{e}_2 = đỏ\space mắt,\space không\space ngủ\space trong\space lớp$<br>
$\textbf{e}_3 = đỏ\space mắt,\space ngủ\space trong\space lớp$<br>

thực hiện các phép tính sau:<br>

1. Ước tính trạng thái: Tính $P({EnoughSleep}_t | \textbf{e}_{1:t})$ cho mỗi $t = 1,2,3$.<br>

2. Làm mịn: Tính $P({EnoughSleep}_t | \textbf{e}_{1:3})$ cho mỗi $t = 1,2,3$.<br>

3. So sánh xác suất lọc và làm mịn cho $t=1$ và $t=2$.<br>


---

##### Bài tập 15.18

Giả sử rằng một sinh viên cụ thể xuất hiện với đôi mắt đỏ và ngủ trong lớp mỗi ngày. Với mô hình được mô tả trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_15/">sleep1-exercise</a>, hãy giải thích tại sao xác suất rằng sinh viên đã ngủ đủ giấc vào đêm trước đó hội tụ về một điểm cố định thay vì tiếp tục giảm khi chúng ta thu thập thêm bằng chứng từ các ngày. Điểm cố định đó là gì? Trả lời cả bằng số (bằng cách tính toán) và bằng phân tích.<br>


---

##### Bài tập 15.19

Bài tập này phân tích chi tiết hơn mô hình lỗi dai dẳng cho cảm biến pin trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/battery-persistence-figure.png">battery-persistence-figure</a>(a) (trang <a class="pageRef" title="" href="#">battery-persistence-figure</a>).<br>

1. Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/battery-persistence-figure.png">battery-persistence-figure</a>(b) dừng ở $t=32$. Mô tả định tính những gì sẽ xảy ra khi $t\to\infty$ nếu cảm biến tiếp tục đọc 0.<br>

2. Giả sử nhiệt độ bên ngoài ảnh hưởng đến cảm biến pin theo cách mà các lỗi tạm thời trở nên có khả năng xảy ra hơn khi nhiệt độ tăng. Chứng minh cách bổ sung cấu trúc DBN trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/battery-persistence-figure.png">battery-persistence-figure</a>(a), và giải thích bất kỳ thay đổi nào cần thiết đối với CPTs.<br>

3. Với cấu trúc mạng mới, liệu các đọc pin có thể được robot sử dụng để suy ra nhiệt độ hiện tại không?<br>


---

##### Bài tập 15.20

Xem xét việc áp dụng thuật toán loại bỏ biến cho DBN ô dù được mở rộng cho ba lát cắt, trong đó truy vấn là ${\textbf{P}}(R_3|u_1,u_2,u_3)$. Chứng minh rằng độ phức tạp không gian của thuật toán—kích thước của yếu tố lớn nhất—là như nhau, bất kể các biến mưa được loại bỏ theo thứ tự tiến hay lùi.


---

<!-- tabs:end -->
