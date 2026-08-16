# Chapter 17 Multiagent decision making

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_17_Multiagent%20decision%20making/chapter_17_vi.html?v=2" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_17_Multiagent%20decision%20making.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide/chapter17+21.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter17_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter17_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter17/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [VALUE-ITERATION](codeAndExercises/aima-pseudocode-master/md/Value-Iteration.md)
- [POLICY-ITERATION](codeAndExercises/aima-pseudocode-master/md/Policy-Iteration.md)
- [POMDP-VALUE-ITERATION](codeAndExercises/aima-pseudocode-master/md/POMDP-Value-Iteration.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Game Theory](codeAndExercises/aima-python-master/notebooks/game_theory.ipynb)
- [Game Theory (Python File)](codeAndExercises/aima-python-master/notebooks/game_theory.py)


#### **Bài tập**


##### Bài tập 17.1

Đối với thế giới $4\times 3$ được hiển thị trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sequential-decision-world-figure.png">sequential-decision-world-figure</a>, hãy tính toán
những ô vuông nào có thể đạt được từ (1,1) bằng chuỗi hành động
$[{Up},{Up},{Right},{Right},{Right}]$ và với xác suất nào. Giải thích cách tính toán này liên quan đến tác vụ dự đoán (xem Phần <a href="#">general-filtering-section</a> cho một hidden Markov model.


---

##### Bài tập 17.2

Đối với thế giới $4\times 3$ được hiển thị trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sequential-decision-world-figure.png">sequential-decision-world-figure</a>, hãy tính toán
những ô vuông nào có thể đạt được từ (1,1) bằng chuỗi hành động
$[{Right},{Right},{Right},{Up},{Up}]$ và với xác suất nào. Giải thích cách tính toán này liên quan đến tác vụ dự đoán (xem Phần <a class="sectionRef" title="" href="#">general-filtering-section</a>) cho một hidden Markov model.


---

##### Bài tập 17.3

Chọn một thành viên cụ thể trong tập hợp các policies tối ưu cho
$R(s)>0$ như được hiển thị trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sequential-decision-policies-figure.png">sequential-decision-policies-figure</a>(b), và
tính toán tỷ lệ thời gian agent dành ở mỗi state, trong giới hạn, nếu policy được thực thi mãi mãi. (<i>Gợi ý</i>:
Xây dựng ma trận xác suất chuyển đổi từ state sang state tương ứng với policy và xem
Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_2/">markov-convergence-exercise</a>.)


---

##### Bài tập 17.4

Giả sử rằng chúng ta định nghĩa utility của một chuỗi state
là phần thưởng *tối đa* thu được ở bất kỳ state nào trong chuỗi. Chứng minh rằng hàm utility này không dẫn đến sở thích tĩnh giữa các chuỗi state. Liệu vẫn có thể định nghĩa một hàm utility trên các state sao cho việc ra quyết định theo MEU mang lại hành vi tối ưu?


---

##### Bài tập 17.5

Liệu bất kỳ bài toán search hữu hạn nào có thể được dịch chính xác thành một Markov decision problem sao cho một giải pháp tối ưu của cái sau cũng là một giải pháp tối ưu của cái trước không? Nếu có, hãy giải thích *chính xác* cách dịch bài toán và cách dịch giải pháp trở lại; nếu không, hãy giải thích *chính xác* tại sao không (tức là, đưa ra một phản ví dụ).


---

##### Bài tập 17.6

Đôi khi MDPs được xây dựng với một hàm phần thưởng $R(s,a)$ phụ thuộc vào hành động được thực hiện hoặc với một hàm phần thưởng $R(s,a,s')$ cũng phụ thuộc vào state kết quả.<br>

1.  Viết các phương trình Bellman cho các công thức này.<br>

2.  Chỉ ra cách một MDP với hàm phần thưởng $R(s,a,s')$ có thể được biến đổi thành một MDP khác với hàm phần thưởng $R(s,a)$, sao cho các policies tối ưu trong MDP mới tương ứng chính xác với các policies tối ưu trong MDP gốc.<br>

3.  Bây giờ hãy làm tương tự để chuyển đổi MDPs với $R(s,a)$ thành MDPs với $R(s)$.<br>


---

##### Bài tập 17.7

Đối với môi trường được hiển thị trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sequential-decision-world-figure.png">sequential-decision-world-figure</a>, tìm tất cả các
giá trị ngưỡng cho $R(s)$ sao cho policy tối ưu thay đổi khi vượt qua ngưỡng. Bạn sẽ cần một cách để tính toán policy tối ưu và giá trị của nó cho $R(s)$ cố định. (<i>Gợi ý</i>: Chứng minh rằng giá trị của bất kỳ policy cố định nào thay đổi tuyến tính với $R(s)$.)


---

##### Bài tập 17.8

Phương trình (<a class="equationRef" title="" href="#">vi-contraction-equation</a>) trên trang <a class="pageRef" title="" href="#">vi-contraction-equation</a> nói rằng toán tử Bellman là một phép co. <br>

1.  Chứng minh rằng, với bất kỳ hàm $f$ và $g$ nào,
    $$|\max_a f(a) - \max_a g(a)| \leq \max_a |f(a) - g(a)|\ .$$<br>

2.  Viết ra một biểu thức cho $$|(B\,U_i - B\,U'_i)(s)|$$ và sau đó áp dụng
    kết quả từ (1) để hoàn thành chứng minh rằng toán tử Bellman
    là một phép co.<br>


---

###### Bài tập 17.9

Bài tập này xem xét các MDP hai người chơi tương ứng với các trò chơi tổng bằng không, chơi luân phiên như trong
Chương <a class="chapterRef" href="{{site.baseurl}}/game-playing-exercises/">game-playing-chapter</a>. Gọi người chơi là $A$ và $B$, và gọi $R(s)$ là phần thưởng cho người chơi $A$ trong state $s$. (Phần thưởng cho $B$ luôn bằng và đối lập.)<br>

1.  Gọi $U_A(s)$ là utility của state $s$ khi đến lượt $A$ di chuyển trong $s$, và gọi $U_B(s)$ là utility của state $s$ khi đến lượt $B$ di chuyển trong $s$. Tất cả phần thưởng và utility đều được tính từ góc nhìn của $A$ (giống như trong cây minimax game). Viết các phương trình Bellman định nghĩa $U_A(s)$ và $U_B(s)$.<br>

2.  Giải thích cách thực hiện two-player value iteration với các phương trình này, và định nghĩa một tiêu chí dừng phù hợp.<br>

3.  Xem xét trò chơi được mô tả trong
    Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/line-game4-figure.png">line-game4-figure</a> trên trang <a class="pageRef" id="pageref" title="" href="#">line-game4-figure</a>.
    Vẽ không gian state (thay vì cây game), hiển thị các nước đi của $A$ bằng các đường liền nét và các nước đi của $B$ bằng các đường nét đứt. Đánh dấu mỗi state với $R(s)$. Bạn sẽ thấy hữu ích khi sắp xếp các state
    $(s_A,s_B)$ trên một lưới hai chiều, sử dụng $s_A$ và $s_B$ làm “tọa độ.”<br>

4.  Bây giờ áp dụng two-player value iteration để giải trò chơi này, và suy ra policy tối ưu.<br>


    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/grid-mdp-figure.svg" alt="grid-mdp-figure" id="grid-mdp-figure" style="width:100%">
      <figcaption><center><b>(a) Thế giới $3 \times 3$ cho Bài tập <a href="#">3x3-mdp-exercise</a>. Phần thưởng cho mỗi state được chỉ ra. Ô vuông trên cùng bên phải là một state kết thúc. (b) Thế giới $101 \times 3$ cho Bài tập <a href="#">101x3-mdp-exercise</a> (bỏ qua 93 cột giống hệt nhau ở giữa).
      State bắt đầu có phần thưởng 0.</b></center></figcaption>
    </figure>


---

##### Bài tập 17.10

Xem xét thế giới $3 \times 3$ được hiển thị trong
Hình <a class="insideExercisesFigRef"  href="#grid-mdp-figure">grid-mdp-figure</a>(a). Mô hình chuyển đổi giống như trong
Hình <a class="insideBookFigRef" id="insidebookfigref" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sequential-decision-world-figure.png">sequential-decision-world-figure</a> $4\times 3$: 80% thời gian agent đi theo hướng nó chọn; phần còn lại thời gian nó di chuyển vuông góc với hướng dự định.<br>

Triển khai value iteration cho thế giới này với mỗi giá trị của $r$ dưới đây.
Sử dụng phần thưởng chiết khấu với hệ số chiết khấu là 0.99. Hiển thị policy thu được trong mỗi trường hợp. Giải thích trực quan tại sao giá trị của $r$ dẫn đến mỗi policy.<br>

1.  $r = -100$<br>

2.  $r = -3$<br>

3.  $r = 0$<br>

4.  $r = +3$<br>


---

##### Bài tập 17.11

Xem xét thế giới $101 \times 3$ được hiển thị trong
Hình <a class="insideExercisesFigRef"  href="#grid-mdp-figure">grid-mdp-figure</a>(b). Trong state bắt đầu, agent có lựa chọn hai hành động xác định, *Up* hoặc
*Down*, nhưng trong các state khác, agent có một hành động xác định, *Right*. Giả sử hàm phần thưởng chiết khấu, với những giá trị nào của hệ số chiết khấu $\gamma$ thì agent nên chọn *Up* và với những giá trị nào thì nên chọn *Down*? Tính toán utility của mỗi hành động như một hàm của $\gamma$. (Lưu ý rằng ví dụ đơn giản này thực sự phản ánh nhiều tình huống thực tế trong đó người ta phải cân nhắc giá trị của một hành động tức thời so với các hậu quả lâu dài liên tục có thể xảy ra, chẳng hạn như chọn đổ chất ô nhiễm vào hồ.)


---

##### Bài tập 17.12

Xem xét một MDP không chiết khấu có ba state, (1, 2, 3), với phần thưởng lần lượt là $-1$, $-2$, $0$. State 3 là một state kết thúc. Trong các state 1 và 2 có hai hành động khả thi: $a$ và $b$. Mô hình chuyển đổi như sau:<br>

-   Trong state 1, hành động $a$ đưa agent đến state 2 với xác suất 0.8 và giữ nguyên agent với xác suất 0.2.<br>

-   Trong state 2, hành động $a$ đưa agent đến state 1 với xác suất 0.8 và giữ nguyên agent với xác suất 0.2.<br>

-   Trong cả state 1 hoặc state 2, hành động $b$ đưa agent đến state 3 với xác suất 0.1 và giữ nguyên agent với xác suất 0.9.<br>

Trả lời các câu hỏi sau:<br>

1.  Có thể xác định *chất lượng* gì về policy tối ưu trong các state 1 và 2?<br>

2.  Áp dụng policy iteration, hiển thị từng bước đầy đủ, để xác định policy tối ưu và giá trị của các state 1 và 2. Giả sử policy ban đầu có hành động $b$ ở cả hai state.<br>

3.  Điều gì xảy ra với policy iteration nếu policy ban đầu có hành động $a$ ở cả hai state? Liệu chiết khấu có giúp ích không? Liệu policy tối ưu có phụ thuộc vào hệ số chiết khấu không?<br>


---

##### Bài tập 17.13

Xem xét thế giới $4\times 3$ được hiển thị trong
Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sequential-decision-world-figure.png">sequential-decision-world-figure</a><br>.

1.  Triển khai một trình mô phỏng môi trường cho môi trường này, sao cho địa lý cụ thể của môi trường có thể dễ dàng thay đổi. Một số mã cho việc này đã có trong kho mã trực tuyến.<br>

2.  Tạo một agent sử dụng policy iteration, và đo lường hiệu suất của nó trong trình mô phỏng môi trường từ các state bắt đầu khác nhau. Thực hiện nhiều thử nghiệm từ mỗi state bắt đầu, và so sánh phần thưởng tổng trung bình nhận được mỗi lần chạy với utility của state, như được xác định bởi thuật toán của bạn.<br>

3.  Thử nghiệm với việc tăng kích thước của môi trường. Thời gian chạy cho policy iteration thay đổi như thế nào với kích thước của môi trường?<br>


---

##### Bài tập 17.14

Thuật toán xác định giá trị có thể được sử dụng như thế nào để tính toán tổn thất kỳ vọng mà một agent trải qua khi sử dụng một bộ ước tính utility ${U}$ và một mô hình ước tính ${P}$, so với một agent sử dụng các giá trị chính xác?


---

##### Bài tập 17.15

Cho belief state ban đầu $b_0$ cho POMDP $4\times 3$ trên trang <a class="pageRef" title="" href="#">4x3-pomdp-page</a> là phân phối đều trên các state không kết thúc, tức là
$< \frac{1}{9},\frac{1}{9},\frac{1}{9},\frac{1}{9},\frac{1}{9},\frac{1}{9},\frac{1}{9},\frac{1}{9},\frac{1}{9},0,0 >$.
Tính toán belief state chính xác $b_1$ sau khi agent di chuyển và cảm biến của nó báo cáo 1 bức tường liền kề. Cũng tính toán $b_2$ giả sử điều tương tự xảy ra một lần nữa.


---

##### Bài tập 17.16

Độ phức tạp thời gian của $d$ bước POMDP value iteration cho một môi trường không có cảm biến là bao nhiêu?


---

##### Bài tập 17.17

Xem xét một phiên bản của POMDP hai state trên trang <a class="pageRef" title="" href="#">2state-pomdp-page</a> trong đó cảm biến có độ tin cậy 90% trong state 0 nhưng không cung cấp thông tin trong state 1 (tức là, nó báo cáo 0 hoặc 1 với xác suất bằng nhau). Phân tích, định tính hoặc định lượng, hàm utility và policy tối ưu cho bài toán này.


---

##### Bài tập 17.18

Chứng minh rằng một dominant strategy equilibrium là một Nash equilibrium, nhưng ngược lại thì không.


---

##### Bài tập 17.19

Trong trò chơi oẳn tù tì của trẻ em, mỗi người chơi đồng thời đưa ra lựa chọn kéo, búa hoặc giấy. Giấy gói đá, đá làm cùn kéo, và kéo cắt giấy. Trong phiên bản mở rộng rock–paper–scissors–fire–water, lửa thắng đá, giấy và kéo; đá, giấy và kéo thắng nước; và nước thắng lửa. Viết ma trận thanh toán và tìm một giải pháp chiến lược hỗn hợp cho trò chơi này.


---

##### Bài tập 17.20

Giải trò chơi *ba* ngón Morra.


---

##### Bài tập 17.21

Trong *Prisoner’s Dilemma*, xem xét trường hợp sau mỗi vòng, Alice và Bob có xác suất $X$ gặp lại nhau. Giả sử cả hai người chơi đều chọn chiến lược trừng phạt vĩnh viễn (trong đó mỗi người sẽ chọn ${refuse}$ trừ khi người kia đã từng chơi ${testify}$). Giả sử chưa có người chơi nào chơi ${testify}$. Lợi ích tổng tương lai kỳ vọng cho việc chọn ${testify}$ so với ${refuse}$ khi $X = .2$ là bao nhiêu? Còn khi $X = .05$ thì sao? Với giá trị nào của $X$ thì lợi ích tổng tương lai kỳ vọng là như nhau cho dù người ta chọn ${testify}$ hay ${refuse}$ trong vòng hiện tại?


---

##### Bài tập 17.22

Ma trận thanh toán sau đây, từ @Blinder:1983 qua <a class="paperRef" title="" href="">Bernstein:1996</a>, cho thấy một trò chơi giữa các chính trị gia và Cục Dự trữ Liên bang.<br>

$$
\begin{array} 
	{|r|r|}\hline  & Fed: contract & Fed: do nothing & Fed: expand \\ 
	\hline
		Pol: contract & F=7, P=1 & F=9, P=4 & F=6, P=6 \\ 
		Pol: do nothing & F=8, P=2 & F=5, P=5 & F=4, P=9 \\ 
		Pol: expand & F=3, P=3 & F=2, P=7 & F=1, P=8\\ 
	\hline  
\end{array}
$$

<br>
Các chính trị gia có thể mở rộng hoặc thu hẹp chính sách tài khóa, trong khi Fed có thể mở rộng hoặc thu hẹp chính sách tiền tệ. (Và tất nhiên, cả hai bên đều có thể chọn không làm gì cả.) Mỗi bên cũng có sở thích về việc ai nên làm gì—không bên nào muốn trông giống như kẻ xấu. Các khoản thanh toán được hiển thị đơn giản là thứ hạng: 9 cho lựa chọn đầu tiên đến 1 cho lựa chọn cuối cùng. Tìm Nash equilibrium của trò chơi ở các chiến lược thuần túy. Đây có phải là một giải pháp Pareto-optimal không? Bạn có thể muốn phân tích các chính sách của các chính quyền gần đây dưới ánh sáng này.


---

##### Bài tập 17.23

Một cuộc đấu giá kiểu Hà Lan tương tự như một cuộc đấu giá kiểu Anh, nhưng thay vì bắt đầu đấu giá ở mức giá thấp và tăng dần, trong một cuộc đấu giá kiểu Hà Lan, người bán bắt đầu ở mức giá cao và giảm dần giá cho đến khi có ít nhất một người mua chấp nhận mức giá đó. (Nếu nhiều người trả giá chấp nhận mức giá, một người sẽ được chọn tùy ý làm người thắng cuộc.) Chính thức hơn, người bán bắt đầu với mức giá $p$ và giảm dần $p$ theo các bước tăng $d$ cho đến khi ít nhất một người mua chấp nhận mức giá đó. Giả sử tất cả người mua đều hành động hợp lý, liệu có đúng là với $d$ nhỏ tùy ý, một cuộc đấu giá kiểu Hà Lan sẽ luôn dẫn đến việc người trả giá có giá trị cao nhất cho món hàng sẽ nhận được món hàng đó không? Nếu có, hãy chứng minh bằng toán học tại sao. Nếu không, hãy giải thích làm thế nào có thể xảy ra trường hợp người trả giá có giá trị cao nhất cho món hàng không nhận được nó.


---

##### Bài tập 17.24

Hãy tưởng tượng một cơ chế đấu giá giống như một cuộc đấu giá tăng giá, ngoại trừ việc cuối cùng, người thắng cuộc, người trả giá $b_{max}$, chỉ phải trả $b_{max}/2$ thay vì $b_{max}$. Giả sử tất cả các agent đều hợp lý, doanh thu kỳ vọng của người bán cho cơ chế này so với một cuộc đấu giá tăng giá tiêu chuẩn là bao nhiêu?


---

##### Bài tập 17.25

Các đội trong National Hockey League theo lịch sử nhận được 2 điểm cho mỗi trận thắng và 0 cho mỗi trận thua. Nếu trận đấu hòa, một hiệp phụ sẽ được chơi; nếu không ai thắng trong hiệp phụ, trận đấu sẽ hòa và mỗi đội nhận được 1 điểm. Nhưng các quan chức giải đấu cảm thấy rằng các đội đã chơi quá thận trọng trong hiệp phụ (để tránh thua), và sẽ thú vị hơn nếu hiệp phụ tạo ra người thắng cuộc. Vì vậy, vào năm 1999, các quan chức đã thử nghiệm thiết kế cơ chế: các quy tắc đã được thay đổi, cho đội thua trong hiệp phụ 1 điểm, không phải 0. Vẫn là 2 điểm cho một trận thắng và 1 cho một trận hòa.<br>

1.  Trò chơi khúc côn cầu có phải là trò chơi tổng bằng không trước khi thay đổi luật không? Sau đó thì sao?<br>

2.  Giả sử rằng tại một thời điểm $t$ nhất định trong một trận đấu, đội chủ nhà có xác suất $p$ thắng trong thời gian thi đấu chính thức, xác suất $0.78-p$ thua, và xác suất 0.22 phải thi đấu hiệp phụ, nơi họ có xác suất $q$ thắng, $.9-q$ thua, và .1 hòa.
    Đưa ra các phương trình cho giá trị kỳ vọng cho đội chủ nhà và đội khách.<br>

3.  Hãy tưởng tượng rằng việc hai đội tham gia vào một thỏa thuận, trong đó họ đồng ý sẽ hòa trong thời gian thi đấu chính thức, và sau đó cả hai đều cố gắng hết sức để thắng trong hiệp phụ, là hợp pháp và có đạo đức.
    Trong những điều kiện nào, theo $p$ và $q$, thì việc cả hai đội đồng ý với thỏa thuận này là hợp lý?<br>

4.  <a class="paperRef" title="" href="">Longley+Sankaran:2005</a> báo cáo rằng kể từ khi thay đổi luật, tỷ lệ các trận đấu có người thắng trong hiệp phụ đã tăng 18.2%, như mong muốn, nhưng tỷ lệ các trận đấu hiệp phụ cũng tăng 3.6%. Điều đó gợi ý gì về khả năng thông đồng hoặc chơi thận trọng sau khi thay đổi luật?<br>

<!-- tabs:end -->
