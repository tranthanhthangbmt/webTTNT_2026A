# Chapter 20 Knowledge in Learning

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_20_Knowledge%20in%20Learning/chapter_20_vi.html?v=2" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_20_Knowledge%20in%20Learning.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter20_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter20/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/knowledge_current_best.ipynb"  target="_blank" data-ignore>Knowledge Current Best</a>
- <a href="python_runner.html?file=codeAndExercises/aima-python-master/notebooks/knowledge_current_best.py"  target="_blank" data-ignore>Knowledge Current Best (Python File)</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/knowledge_foil.ipynb"  target="_blank" data-ignore>Knowledge Foil</a>
- <a href="python_runner.html?file=codeAndExercises/aima-python-master/notebooks/knowledge_foil.py"  target="_blank" data-ignore>Knowledge Foil (Python File)</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/knowledge_version_space.ipynb"  target="_blank" data-ignore>Knowledge Version Space</a>
- <a href="python_runner.html?file=codeAndExercises/aima-python-master/notebooks/knowledge_version_space.py"  target="_blank" data-ignore>Knowledge Version Space (Python File)</a>


#### **Bài tập**




##### Bài tập 20.1
Dữ liệu được sử dụng cho 
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/bayes-candy-figure.png">bayes-candy-figure</a> ở trang <a class="pageRef" id="pageref" title="" href="#">bayes-candy-figure</a> có thể được xem như được sinh ra bởi $h_5$. Đối với mỗi hypothesis trong bốn hypothesis còn lại, hãy generate một data set có độ dài 100 và vẽ các đồ thị tương ứng cho $P(h_i|d_1,\ldots,d_N)$ và $P(D_{N+1}=lime|d_1,\ldots,d_N)$. Hãy đưa ra nhận xét về các kết quả của bạn.


---


##### Bài tập 20.2
Lặp lại Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/bayesian-learning-exercises/ex_1/">bayes-candy-exercise</a>, lần này hãy vẽ các giá trị của $P(D_{N+1}=lime|h_{MAP})$ và $P(D_{N+1}=lime|h_{ML})$.


---


##### Bài tập 20.3
Giả sử utility của Ann đối với kẹo vị cherry và vị lime lần lượt là $c_A$ và $\ell_A$, trong khi utility của Bob là $c_B$ và $\ell_B$. (Nhưng một khi Ann đã bóc một viên kẹo, Bob sẽ không mua nó nữa.) Có lẽ, nếu Bob thích kẹo vị lime hơn Ann rất nhiều, sẽ khôn ngoan nếu Ann bán túi kẹo của mình một khi cô ấy đủ chắc chắn về hàm lượng vị lime trong đó. Mặt khác, nếu Ann bóc quá nhiều kẹo trong quá trình này, túi kẹo sẽ có giá trị thấp hơn. Hãy thảo luận về bài toán xác định thời điểm tối ưu để bán túi kẹo. Hãy xác định expected utility của quy trình tối ưu, cho trước prior distribution từ Mục <a class="sectionRef" title="" href="#">statistical-learning-section</a>.


---


##### Bài tập 20.4
Hai nhà thống kê đi khám bác sĩ và đều nhận được cùng một tiên lượng: 40% khả năng vấn đề là căn bệnh chết người $A$, và 60% khả năng là căn bệnh chết người $B$. May thay, có sẵn các loại thuốc chống $A$ và chống $B$ với giá rẻ, hiệu quả 100%, và không có tác dụng phụ. Các nhà thống kê có lựa chọn dùng một loại thuốc, cả hai loại, hoặc không dùng loại nào cả. Nhà thống kê thứ nhất (một tín đồ Bayesian nhiệt thành) sẽ làm gì? Còn nhà thống kê thứ hai, người luôn sử dụng maximum likelihood hypothesis, thì sao?<br>

Bác sĩ thực hiện một số nghiên cứu và phát hiện ra rằng căn bệnh $B$ thực thực tế có hai biến thể, dextro-$B$ và levo-$B$, có xác suất xảy ra như nhau và đều có thể chữa khỏi như nhau bằng thuốc chống $B$. Bây giờ, khi có ba hypothesis, hai nhà thống kê sẽ làm gì?


---


##### Bài tập 20.5
Hãy giải thích cách áp dụng phương pháp boosting của Chương <a class="chapterRef" href="{{site.baseurl}}/concept-learning-exercises/">concept-learning-chapter</a> cho naive Bayes learning. Hãy kiểm tra hiệu năng của thuật toán thu được trên bài toán learning nhà hàng.


---


##### Bài tập 20.6
Xét $N$ data point $(x_j,y_j)$, trong đó các $y_j$ được sinh ra từ các $x_j$ theo linear Gaussian model trong Phương trình (<a class="equationRef" id="equationref" title="" href="#">linear-gaussian-likelihood-equation</a>). Hãy tìm các giá trị của $\theta_1$, $\theta_2$, và $\sigma$ để tối đa hóa conditional log likelihood của data.


---


##### Bài tập 20.7
Xét noisy-OR model cho sốt được mô tả trong Mục <a class="sectionRef" title="" href="#">canonical-distribution-section</a>. Hãy giải thích cách áp dụng maximum-likelihood learning để fit các parameter của một model như vậy vào một tập complete data. (<i>Gợi ý</i>: sử dụng chain rule cho đạo hàm riêng.)


---


##### Bài tập 20.8
Bài tập này nghiên cứu các tính chất của Beta distribution được định nghĩa trong Phương trình (<a class="equationRef" title="" href="#">beta-equation</a>).
<br>

1.  Bằng cách tích phân trên miền $[0,1]$, hãy chứng minh rằng normalization constant cho distribution ${{\rm beta}}[a,b]$ được cho bởi $\alpha = \Gamma(a+b)/\Gamma(a)\Gamma(b)$ trong đó $\Gamma(x)$ là <b>Gamma function</b>, được định nghĩa bởi $\Gamma(x+1){{\,=\,}}x\cdot\Gamma(x)$ và $\Gamma(1){{\,=\,}}1$. (Đối với $x$ nguyên, $\Gamma(x+1){{\,=\,}}x!$.)<br>

2.  Chứng minh rằng mean là $a/(a+b)$.<br>

3.  Tìm mode (các giá trị có khả năng xảy ra cao nhất của $\theta$).<br>

4.  Mô tả distribution ${{\rm beta}}[\epsilon,\epsilon]$ với $\epsilon$ rất nhỏ. Điều gì xảy ra khi một distribution như vậy được update?


---


##### Bài tập 20.9
Xét một Bayes net bất kỳ, một complete data set cho Bayes net đó, và likelihood của data set theo Bayes net. Hãy đưa ra một chứng minh đơn giản rằng likelihood của data không thể giảm nếu chúng ta thêm một link mới vào Bayes net và tính toán lại các giá trị maximum-likelihood parameter.


---


##### Bài tập 20.10
Xét một Boolean random variable đơn lẻ $Y$ (“phân loại”). Hãy để prior probability $P(Y=true)$ là $\pi$. Hãy thử tìm $\pi$, cho trước một training set $D=(y_1,\ldots,y_N)$ với $N$ sample độc lập của $Y$. Hơn nữa, giả sử có $p$ trong số $N$ sample là dương tính và $n$ trong số $N$ sample là âm tính.<br>

1.  Viết biểu thức cho likelihood của $D$ (nghĩa là xác suất quan sát thấy chuỗi ví dụ cụ thể này, cho trước một giá trị cố định của $\pi$) theo $\pi$, $p$, và $n$.<br>

2.  Bằng cách lấy đạo hàm log likelihood $L$, hãy tìm giá trị của $\pi$ làm tối đa hóa likelihood.<br>

3.  Bây giờ giả sử chúng ta thêm vào $k$ Boolean random variable $X_1, X_2,\ldots,X_k$ (“thuộc tính”) mô tả mỗi sample, và giả sử chúng ta giả định rằng các thuộc tính là độc lập có điều kiện với nhau khi cho trước mục tiêu $Y$. Vẽ Bayes net tương ứng với giả định này.<br>

4.  Viết likelihood cho data bao gồm cả các thuộc tính, sử dụng thêm các ký hiệu sau:<br>

    -   $\alpha_i$ là $P(X_i=true \| Y=true)$.<br>

    -   $\beta_i$ là $P(X_i=true \| Y=false)$.<br>

    -   $p_i^+$ là số lượng sample mà tại đó $X_i=true$ và $Y=true$.<br>

    -   $n_i^+$ là số lượng sample mà tại đó $X_i=false$ và $Y=true$.<br>

    -   $p_i^-$ là số lượng sample mà tại đó $X_i=true$ và $Y=false$.<br>

    -   $n_i^-$ là số lượng sample mà tại đó $X_i=false$ và $Y=false$.<br>

    \[<i>Gợi ý</i>: trước tiên hãy xét xác suất quan sát thấy một sample đơn lẻ với các giá trị được chỉ định cho $X_1, X_2,\ldots,X_k$ và $Y$.\]<br>

5.  Bằng cách lấy đạo hàm log likelihood $L$, hãy tìm các giá trị của $\alpha_i$ và $\beta_i$ (theo các bộ đếm khác nhau) làm tối đa hóa likelihood và diễn giải bằng lời các giá trị này đại diện cho điều gì.<br>

6.  Cho $k = 2$, và xét một data set với cả 4 ví dụ có thể có của hàm xor. Tính các ước lượng maximum likelihood của $\pi$, $\alpha_1$, $\alpha_2$, $\beta_1$, và $\beta_2$.<br>

7.  Cho trước các ước lượng này của $\pi$, $\alpha_1$, $\alpha_2$, $\beta_1$, và $\beta_2$, posterior probabilities $P(Y=true | x_1,x_2)$ cho mỗi ví dụ là gì?<br>


---


##### Bài tập 20.11
Xét việc áp dụng EM để learn các parameter cho network trong Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/mixture-networks-figure.png">mixture-networks-figure</a>(a), cho trước các true parameter trong Phương trình (<a class="equationRef" title="" href="#">candy-true-equation</a>).

1.  Giải thích tại sao thuật toán EM sẽ không hoạt động nếu chỉ có hai thuộc tính trong model thay vì ba.

2.  Trình bày các phép tính cho iteration đầu tiên của EM bắt đầu từ Phương trình (<a class="equationRef" title="" href="#">candy-64-equation</a>).

3.  Điều gì xảy ra nếu chúng ta bắt đầu với tất cả các parameter được đặt thành cùng một giá trị $p$? (<i>Gợi ý</i>: bạn có thể thấy việc khảo sát điều này một cách thực nghiệm trước khi dẫn xuất ra kết quả tổng quát là rất hữu ích.)

4.  Viết biểu thức cho log likelihood của bảng dữ liệu kẹo ở trang <a class="pageRef" title="" href="#">candy-counts-page</a> theo các parameter, tính các đạo hàm riêng đối với từng parameter, và khảo sát bản chất của fixed point đạt được ở phần (c).


---

<!-- tabs:end -->
