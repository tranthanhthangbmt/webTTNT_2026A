# Chapter 16 Making Complex Decisions

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_16_Making%20Complex%20Decisions/chapter_16_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_16_Making%20Complex%20Decisions.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter16_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter16/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
<div id="quiz-container" data-chapter="16"></div>

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Information-Gathering-Agent.md" target="_blank">INFORMATION-GATHERING-AGENT</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Mdp**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/mdp.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/mdp.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/mdp.ipynb" download>Tải .ipynb</a>
- **Mdp Apps**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/mdp_apps.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/mdp_apps.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/mdp_apps.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 16.1

(Chuyển thể từ David Heckerman.) Bài tập này liên quan đến
<b>Trò chơi Lịch</b>, được các nhà phân tích quyết định sử dụng để hiệu chỉnh ước lượng số học. Đối với mỗi câu hỏi sau đây, hãy đưa ra phỏng đoán tốt nhất của bạn về câu trả lời, tức là một con số mà bạn nghĩ rằng có khả năng cao bằng khả năng thấp. Cũng đưa ra phỏng đoán của bạn về ước lượng phân vị thứ 25, tức là một con số mà bạn nghĩ có 25% khả năng quá cao và 75% khả năng quá thấp. Làm tương tự cho phân vị thứ 75. (Do đó, bạn nên đưa ra ba ước lượng tất cả—thấp, trung vị và cao—cho mỗi câu hỏi.)<br>

1. Số lượng hành khách bay giữa New York và Los Angeles vào năm 1989.<br>

2. Dân số Warsaw năm 1992.<br>

3. Năm Coronado phát hiện ra sông Mississippi.<br>

4. Số phiếu bầu mà Jimmy Carter nhận được trong cuộc bầu cử tổng thống năm 1976.<br>

5. Tuổi của cây sống lâu đời nhất, tính đến năm 2002.<br>

6. Chiều cao của Đập Hoover tính bằng feet.<br>

7. Số lượng trứng được sản xuất ở Oregon vào năm 1985.<br>

8. Số lượng Phật tử trên thế giới vào năm 1992.<br>

9. Số ca tử vong do AIDS ở Hoa Kỳ vào năm 1981.<br>

10. Số lượng bằng sáng chế của Hoa Kỳ được cấp vào năm 1901.<br>

Các câu trả lời đúng xuất hiện sau bài tập cuối cùng của chương này. Từ
quan điểm của phân tích quyết định, điều thú vị không phải là ước lượng trung vị của bạn gần với câu trả lời thực tế như thế nào, mà là tần suất câu trả lời thực tế nằm trong giới hạn 25% và 75% của bạn. Nếu nó xảy ra khoảng một nửa thời gian, thì giới hạn của bạn là chính xác. Nhưng nếu bạn giống như hầu hết mọi người, bạn sẽ tự tin hơn mức cần thiết, và ít hơn một nửa số câu trả lời sẽ nằm trong giới hạn. Với thực hành, bạn có thể tự hiệu chỉnh để đưa ra các giới hạn thực tế, và do đó hữu ích hơn trong việc cung cấp thông tin cho việc ra quyết định. Hãy thử bộ câu hỏi thứ hai này và xem có bất kỳ cải thiện nào không:<br>

1. Năm sinh của Zsa Zsa Gabor.<br>

2. Khoảng cách tối đa từ Sao Hỏa đến Mặt trời tính bằng dặm.<br>

3. Giá trị bằng đô la của xuất khẩu lúa mì từ Hoa Kỳ vào năm 1992.<br>

4. Số tấn hàng được xử lý tại cảng Honolulu vào năm 1991.<br>

5. Mức lương hàng năm bằng đô la của thống đốc California vào năm 1993.<br>

6. Dân số San Diego vào năm 1990.<br>

7. Năm Roger Williams thành lập Providence, Rhode Island.<br>

8. Chiều cao của núi Kilimanjaro tính bằng feet.<br>

9. Chiều dài của Cầu Brooklyn tính bằng feet.<br>

10. Số ca tử vong do tai nạn ô tô ở Hoa Kỳ vào năm 1992.<br>

---

##### Bài tập 16.2

Chris xem xét bốn chiếc xe đã qua sử dụng trước khi mua chiếc có
expected utility tối đa. Pat xem xét mười chiếc xe và làm tương tự.
Nếu mọi thứ khác đều như nhau, ai có nhiều khả năng có được chiếc xe
tốt hơn? Ai có nhiều khả năng thất vọng với chất lượng xe của mình?
Sự khác biệt là bao nhiêu (tính theo độ lệch chuẩn của expected quality)?

---

##### Bài tập 16.3

Chris xem xét năm chiếc xe đã qua sử dụng trước khi mua chiếc có
expected utility tối đa. Pat xem xét mười một chiếc xe và làm tương tự.
Nếu mọi thứ khác đều như nhau, ai có nhiều khả năng có được chiếc xe
tốt hơn? Ai có nhiều khả năng thất vọng với chất lượng xe của mình?
Sự khác biệt là bao nhiêu (tính theo độ lệch chuẩn của expected quality)?

---

##### Bài tập 16.4

Năm 1713, Nicolas Bernoulli đã đưa ra một câu đố,
nay được gọi là nghịch lý St. Petersburg, hoạt động như sau. Bạn có cơ hội
chơi một trò chơi trong đó một đồng xu công bằng được tung liên tục cho
đến khi xuất hiện mặt ngửa. Nếu mặt ngửa đầu tiên xuất hiện ở lần tung thứ $n$,
bạn thắng $2^n$ đô la.<br>

1. Chứng minh rằng giá trị tiền tệ kỳ vọng (expected monetary value) của trò chơi này là vô hạn.<br>

2. Cá nhân bạn sẽ trả bao nhiêu để chơi trò chơi này?<br>

3. Anh họ của Nicolas, Daniel Bernoulli, đã giải quyết nghịch lý rõ ràng vào năm 1738 bằng cách đề xuất rằng utility của tiền tệ được đo lường trên thang logarit (tức là, $U(S_{n}) = a\log_2 n +b$, trong đó $S_n$ là trạng thái có $n$). Giá trị utility kỳ vọng (expected utility) của trò chơi này là bao nhiêu theo giả định này?<br>

4. Số tiền tối đa mà một người có thể hợp lý (rational) để trả để chơi trò chơi này là bao nhiêu, giả sử tài sản ban đầu là $k$?

---

##### Bài tập 16.5

Viết một chương trình máy tính để tự động hóa quy trình trong Bài tập
<a href="#">assessment-exercise</a>. Hãy thử chương trình của bạn với
nhiều người có giá trị tài sản ròng và quan điểm chính trị khác nhau.
Nhận xét về tính nhất quán của kết quả của bạn, cả đối với một cá nhân
và giữa các cá nhân.

---

###### Bài tập 16.6

Công ty Kẹo Bất Ngờ sản xuất kẹo với hai hương vị: 75% là hương dâu và 25% là hương cá cơm. Mỗi viên kẹo mới ban đầu có hình tròn; khi nó di chuyển dọc theo dây chuyền sản xuất, một máy sẽ chọn ngẫu nhiên một tỷ lệ phần trăm nhất định để cắt thành hình vuông; sau đó, mỗi viên kẹo được gói trong một bao bì có màu được chọn ngẫu nhiên là đỏ hoặc nâu. 70% kẹo hương dâu là hình tròn và 70% có bao bì màu đỏ, trong khi 90% kẹo hương cá cơm là hình vuông và 90% có bao bì màu nâu. Tất cả kẹo được bán riêng lẻ trong các hộp đen giống hệt nhau, được niêm phong.<br>

Bây giờ bạn, khách hàng, vừa mua một viên kẹo Bất Ngờ tại cửa hàng nhưng chưa mở hộp. Hãy xem xét ba mạng Bayes trong Hình <a class="insideExercisesFigRef"  href="#3candy-figure">3candy-figure</a>.<br>

1. Mạng nào có thể biểu diễn chính xác ${\textbf{P}}(Flavor,Wrapper,Shape)$?<br>

2. Mạng nào là biểu diễn tốt nhất cho vấn đề này?<br>

3. Mạng (i) có khẳng định rằng ${\textbf{P}}(Wrapper|Shape){{\,=\,}}{\textbf{P}}(Wrapper)$ không?<br>

4. Xác suất để kẹo của bạn có bao bì màu đỏ là bao nhiêu?<br>

5. Trong hộp là một viên kẹo hình tròn có bao bì màu đỏ. Xác suất hương vị của nó là dâu là bao nhiêu?<br>

6. Một viên kẹo dâu không bọc có giá $s$ trên thị trường mở và một viên kẹo cá cơm không bọc có giá $a$. Viết một biểu thức cho giá trị của một hộp kẹo chưa mở.<br>

7. Một luật mới cấm giao dịch kẹo không bọc, nhưng vẫn hợp pháp để giao dịch kẹo đã bọc (ra khỏi hộp). Hộp kẹo chưa mở bây giờ có giá trị hơn, kém hơn, hay bằng như trước đây?<br>

    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/3candy.svg" alt="3candy-figure" id="3candy-figure" style="width:100%">
      <figcaption><center><b>Ba mạng Bayes được đề xuất cho bài toán Kẹo Bất Ngờ</b></center></figcaption>
    </figure>

---

##### Bài tập 16.7

Công ty Kẹo Bất Ngờ sản xuất kẹo với hai hương vị: 70% là hương dâu và 30% là hương cá cơm. Mỗi viên kẹo mới ban đầu có hình tròn; khi nó di chuyển dọc theo dây chuyền sản xuất, một máy sẽ chọn ngẫu nhiên một tỷ lệ phần trăm nhất định để cắt thành hình vuông; sau đó, mỗi viên kẹo được gói trong một bao bì có màu được chọn ngẫu nhiên là đỏ hoặc nâu. 80% kẹo hương dâu là hình tròn và 80% có bao bì màu đỏ, trong khi 90% kẹo hương cá cơm là hình vuông và 90% có bao bì màu nâu. Tất cả kẹo được bán riêng lẻ trong các hộp đen giống hệt nhau, được niêm phong.<br>

Bây giờ bạn, khách hàng, vừa mua một viên kẹo Bất Ngờ tại cửa hàng nhưng chưa mở hộp. Hãy xem xét ba mạng Bayes trong Hình <a class="insideExercisesFigRef"  href="#3candy-figure">3candy-figure</a>.<br>

1. Mạng nào có thể biểu diễn chính xác ${\textbf{P}}(Flavor,Wrapper,Shape)$?<br>

2. Mạng nào là biểu diễn tốt nhất cho vấn đề này?<br>

3. Mạng (i) có khẳng định rằng ${\textbf{P}}(Wrapper|Shape){{\,=\,}}{\textbf{P}}(Wrapper)$ không?<br>

4. Xác suất để kẹo của bạn có bao bì màu đỏ là bao nhiêu?<br>

5. Trong hộp là một viên kẹo hình tròn có bao bì màu đỏ. Xác suất hương vị của nó là dâu là bao nhiêu?<br>

6. Một viên kẹo dâu không bọc có giá $s$ trên thị trường mở và một viên kẹo cá cơm không bọc có giá $a$. Viết một biểu thức cho giá trị của một hộp kẹo chưa mở.<br>

7. Một luật mới cấm giao dịch kẹo không bọc, nhưng vẫn hợp pháp để giao dịch kẹo đã bọc (ra khỏi hộp). Hộp kẹo chưa mở bây giờ có giá trị hơn, kém hơn, hay bằng như trước đây?<br>

---

##### Bài tập 16.8

Chứng minh rằng các phán đoán $B \succ A$ và $C \succ D$ trong nghịch lý Allais (trang <a class="pageRef" title="" href="#">allais-page</a>) vi phạm tiên đề về tính thay thế (axiom of substitutability).

---

##### Bài tập 16.9

Xem xét nghịch lý Allais được mô tả trên trang <a class="pageRef" title="" href="#">allais-page</a>: một agent (người ra quyết định) ưa thích $B$ hơn $A$ (chọn phương án chắc chắn), và $C$ hơn $D$ (chọn phương án có EMV cao hơn) thì không hành động một cách hợp lý (rationally), theo lý thuyết utility. Bạn có nghĩ rằng điều này cho thấy một vấn đề đối với agent, một vấn đề đối với lý thuyết, hay không có vấn đề gì cả? Giải thích.

---

##### Bài tập 16.10

Vé số có giá 1. Có hai giải thưởng có thể xảy ra:
giải thưởng 10 với xác suất 1/50, và giải thưởng 1.000.000 với xác suất
1/2.000.000. Giá trị tiền tệ kỳ vọng (expected monetary value) của một vé số là bao nhiêu? Khi nào (nếu có) thì hợp lý để mua một vé? Hãy chính xác—chỉ ra một phương trình liên quan đến utilities. Bạn có thể giả định tài sản hiện tại là $k$ và $U(S_k)=0$. Bạn cũng có thể giả định rằng
$U(S_{k+{10}}) = {10}\times U(S_{k+1})$, nhưng bạn không thể đưa ra bất kỳ giả định nào về $U(S_{k+1,{000},{000}})$. Các nghiên cứu xã hội học cho thấy những người có thu nhập thấp mua một số lượng vé số không tương xứng. Bạn có nghĩ rằng điều này là do họ là những người ra quyết định tồi tệ hơn hay do họ có hàm utility khác? Hãy xem xét giá trị của việc suy ngẫm về khả năng trúng số so với giá trị của việc suy ngẫm về việc trở thành một anh hùng hành động khi xem một bộ phim phiêu lưu.

---

##### Bài tập 16.11

Đánh giá utility của riêng bạn cho các khoản tiền tăng thêm khác nhau bằng cách chạy một loạt các bài kiểm tra ưu tiên giữa một số tiền xác định $M_1$ và một xổ số $[p,M_2; (1-p), 0]$. Chọn các giá trị khác nhau của $M_1$ và $M_2$, và thay đổi $p$ cho đến khi bạn thờ ơ (indifferent) giữa hai lựa chọn. Vẽ đồ thị hàm utility kết quả.

---

##### Bài tập 16.12

Một micromort đáng giá bao nhiêu đối với bạn? Hãy đưa ra một quy trình để xác định điều này. Đặt câu hỏi dựa trên cả việc trả tiền để tránh rủi ro và được trả tiền để chấp nhận rủi ro.

---

##### Bài tập 16.13

Cho các biến liên tục $X_1,\ldots,X_k$ được phân phối độc lập theo cùng một hàm mật độ xác suất $f(x)$. Chứng minh rằng hàm mật độ cho $\max\{X_1,\ldots,X_k\}$ được cho bởi $kf(x)(F(x))^{k-1}$, trong đó $F$ là phân phối tích lũy (cumulative distribution) cho $f$.

---

##### Bài tập 16.14

Các nhà kinh tế thường sử dụng hàm utility mũ cho tiền tệ:
$U(x) = -e^{-x/R}$, trong đó $R$ là một hằng số dương đại diện cho khả năng chấp nhận rủi ro (risk tolerance) của một cá nhân. Khả năng chấp nhận rủi ro phản ánh mức độ một cá nhân sẵn sàng chấp nhận một xổ số với giá trị tiền tệ kỳ vọng (EMV) nhất định so với một khoản thanh toán chắc chắn. Khi $R$ (được đo bằng cùng đơn vị với $x$) tăng lên, cá nhân đó càng ít ngại rủi ro (less risk-averse).<br>

1. Giả sử Mary có hàm utility mũ với $R = \$500$. Mary được lựa chọn giữa việc nhận \$500 chắc chắn (xác suất 1) hoặc tham gia một xổ số có 60% xác suất thắng \$5000 và 40% xác suất thắng không gì cả. Giả sử Mary hành động hợp lý (rationally), cô ấy sẽ chọn phương án nào? Hãy chỉ ra cách bạn suy ra câu trả lời của mình.<br>

2. Xem xét lựa chọn giữa việc nhận \$100 chắc chắn (xác suất 1) hoặc tham gia một xổ số có 50% xác suất thắng \$500 và 50% xác suất thắng không gì cả. Hãy ước tính giá trị của R (làm tròn đến 3 chữ số có nghĩa) trong hàm utility mũ mà sẽ khiến một cá nhân thờ ơ (indifferent) với hai lựa chọn này. (Bạn có thể thấy hữu ích khi viết một chương trình nhỏ để giúp bạn giải quyết vấn đề này.)

---

##### Bài tập 16.15

Các nhà kinh tế thường sử dụng hàm utility mũ cho tiền tệ:
$U(x) = -e^{-x/R}$, trong đó $R$ là một hằng số dương đại diện cho khả năng chấp nhận rủi ro (risk tolerance) của một cá nhân. Khả năng chấp nhận rủi ro phản ánh mức độ một cá nhân sẵn sàng chấp nhận một xổ số với giá trị tiền tệ kỳ vọng (EMV) nhất định so với một khoản thanh toán chắc chắn. Khi $R$ (được đo bằng cùng đơn vị với $x$) tăng lên, cá nhân đó càng ít ngại rủi ro (less risk-averse).<br>

1. Giả sử Mary có hàm utility mũ với $R = \$400$. Mary được lựa chọn giữa việc nhận \$400 chắc chắn (xác suất 1) hoặc tham gia một xổ số có 60% xác suất thắng \$5000 và 40% xác suất thắng không gì cả. Giả sử Mary hành động hợp lý (rationally), cô ấy sẽ chọn phương án nào? Hãy chỉ ra cách bạn suy ra câu trả lời của mình.<br>

2. Xem xét lựa chọn giữa việc nhận \$100 chắc chắn (xác suất 1) hoặc tham gia một xổ số có 50% xác suất thắng \$500 và 50% xác suất thắng không gì cả. Hãy ước tính giá trị của R (làm tròn đến 3 chữ số có nghĩa) trong hàm utility mũ mà sẽ khiến một cá nhân thờ ơ (indifferent) với hai lựa chọn này. (Bạn có thể thấy hữu ích khi viết một chương trình nhỏ để giúp bạn giải quyết vấn đề này.)

---

##### Bài tập 16.16

Alex được lựa chọn giữa hai trò chơi. Trong Trò chơi 1, một đồng xu công bằng được tung và nếu nó ra mặt ngửa, Alex nhận được \$100. Nếu đồng xu ra mặt sấp, Alex nhận được không gì cả. Trong Trò chơi 2, một đồng xu công bằng được tung hai lần. Mỗi lần đồng xu ra mặt ngửa, Alex nhận được \$50, và Alex nhận được không gì cả cho mỗi lần tung đồng xu ra mặt sấp. Giả sử Alex có một hàm utility tăng đơn điệu (monotonically increasing utility function) cho tiền tệ trong khoảng \[\$0, \$100\], hãy chứng minh bằng toán học rằng nếu Alex ưa thích Trò chơi 2 hơn Trò chơi 1, thì Alex là người ngại rủi ro (risk averse) (ít nhất là đối với phạm vi số tiền này).<br>

Chứng minh rằng nếu $X_1$ và $X_2$ độc lập ưu tiên (preferentially independent) với $X_3$, và $X_2$ và $X_3$ độc lập ưu tiên với $X_1$, thì $X_3$ và $X_1$ độc lập ưu tiên với $X_2$.

---

##### Bài tập 16.17

Lặp lại Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/decision-theory-exercises/ex_21/">airport-id-exercise</a>, sử dụng biểu diễn action-utility được hiển thị trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/airport-au-id-figure.png">airport-au-id-figure</a>.

---

##### Bài tập 16.18

Đối với một trong hai sơ đồ quy hoạch sân bay từ Bài tập
<a class="exerciseRef" href="{{ site.baseurl }}/decision-theory-exercises/ex_21/" >airport-id-exercise</a> và <a class="exerciseRef" href="{{ site.baseurl }}/decision-theory-exercises/ex_17/">airport-au-id-exercise</a>, mục nhập bảng xác suất có điều kiện (conditional probability table entry) nào mà utility nhạy cảm nhất, với bằng chứng có sẵn?

---

##### Bài tập 16.19

Sửa đổi và mở rộng mã mạng Bayes trong kho mã để cung cấp khả năng tạo và đánh giá các mạng quyết định (decision networks) và tính toán giá trị thông tin (information value).

---

##### Bài tập 16.20

Xem xét một sinh viên có lựa chọn mua hoặc không mua một cuốn sách giáo khoa cho một khóa học. Chúng ta sẽ mô hình hóa điều này như một vấn đề quyết định với một nút quyết định Boolean, $B$, cho biết liệu agent có chọn mua sách hay không, và hai nút cơ hội Boolean, $M$, cho biết liệu sinh viên có nắm vững tài liệu trong sách hay không, và $P$, cho biết liệu sinh viên có vượt qua khóa học hay không. Tất nhiên, cũng có một nút utility, $U$. Một sinh viên cụ thể, Sam, có hàm utility cộng tính (additive utility function): 0 nếu không mua sách và -\$100 nếu mua sách; và \$2000 nếu vượt qua khóa học và 0 nếu không vượt qua. Các ước tính xác suất có điều kiện của Sam như sau:
$$\begin{array}{ll}
P(p|b,m) = 0.9              & P(m|b) = 0.9       \\
P(p|b, \lnot m) = 0.5       & P(m|\lnot b) = 0.7 \\
P(p|\lnot b, m) = 0.8       & \\
P(p|\lnot b, \lnot m) = 0.3 & \\
\end{array}$$<br>

Bạn có thể nghĩ rằng $P$ sẽ độc lập với $B$ khi biết $M$. Nhưng khóa học này có bài thi cuối kỳ mở sách—vì vậy có sách sẽ giúp ích.<br>

1. Vẽ mạng quyết định cho vấn đề này.<br>

2. Tính toán expected utility của việc mua sách và không mua sách.<br>
3. Sam nên làm gì?

---

##### Bài tập 16.21

Bài tập này hoàn thành phân tích bài toán quy hoạch sân bay trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/airport-id-figure.png">airport-id-figure</a>.<br>

1. Cung cấp các miền biến, xác suất và utility hợp lý cho mạng, giả sử có ba địa điểm khả thi.<br>

2. Giải quyết vấn đề quyết định.<br>

3. Điều gì xảy ra nếu những thay đổi trong công nghệ có nghĩa là mỗi máy bay tạo ra ít tiếng ồn hơn một nửa?<br>

4. Điều gì xảy ra nếu việc tránh tiếng ồn trở nên quan trọng gấp ba lần?<br>

5. Tính toán VPI (Value of Perfect Information) cho ${AirTraffic}$, ${Litigation}$, và ${Construction}$ trong mô hình của bạn.<br>

---

##### Bài tập 16.22

(Chuyển thể từ Pearl [<a class="paperRef" title="" href="">Pearl:1988</a>].) Một người mua xe đã qua sử dụng có thể quyết định thực hiện các bài kiểm tra khác nhau với các chi phí khác nhau (ví dụ: đá lốp, đưa xe đến thợ cơ khí có trình độ) và sau đó, tùy thuộc vào kết quả của các bài kiểm tra, quyết định mua xe nào. Chúng ta sẽ giả định rằng người mua đang quyết định có mua xe $c_1$ hay không, có thời gian để thực hiện tối đa một bài kiểm tra, và $t_1$ là bài kiểm tra của $c_1$ và có chi phí \$50.<br>

Một chiếc xe có thể ở tình trạng tốt (chất lượng $q^+$) hoặc tình trạng xấu (chất lượng $q^-$), và các bài kiểm tra có thể giúp chỉ ra tình trạng của chiếc xe. Xe $c_1$ có giá \$1.500, và giá trị thị trường của nó là \$2.000 nếu nó ở tình trạng tốt; nếu không, \$700 sửa chữa sẽ cần thiết để đưa nó vào tình trạng tốt. Ước tính của người mua là $c_1$ có 70% cơ hội ở tình trạng tốt.<br>

1. Vẽ mạng quyết định đại diện cho vấn đề này.<br>

2. Tính toán lợi nhuận ròng kỳ vọng (expected net gain) từ việc mua $c_1$, khi không có bài kiểm tra.<br>

3. Các bài kiểm tra có thể được mô tả bằng xác suất mà chiếc xe sẽ vượt qua hoặc trượt bài kiểm tra khi biết rằng chiếc xe ở tình trạng tốt hoặc xấu. Chúng ta có thông tin sau:<br>

$P({pass}(c_1,t_1) | q^+(c_1)) = {0.8}$<br>

$P({pass}(c_1,t_1) | q^-(c_1)) = {0.35}$<br>

Sử dụng định lý Bayes để tính xác suất mà chiếc xe sẽ vượt qua (hoặc trượt) bài kiểm tra của nó và do đó xác suất nó ở tình trạng tốt (hoặc xấu) khi biết mỗi kết quả bài kiểm tra có thể.<br>

4. Tính toán các quyết định tối ưu khi biết kết quả vượt qua hoặc trượt, và utility kỳ vọng của chúng.<br>

5. Tính toán giá trị thông tin (value of information) của bài kiểm tra, và đưa ra một kế hoạch có điều kiện tối ưu cho người mua.<br>

---

##### Bài tập 16.23

Nhớ lại định nghĩa về <i>giá trị thông tin</i> (value of information) trong Mục <a class="sectionRef" title="" class="sectionRef" href="">VPI-section</a>.<br>

1. Chứng minh rằng giá trị thông tin là không âm và độc lập với thứ tự (order independent).<br>

2. Giải thích tại sao một số người lại thích không nhận một số thông tin—ví dụ, không muốn biết giới tính của em bé khi siêu âm.<br>

3. Một hàm $f$ trên các tập hợp là <b>submodular</b> nếu, với mọi phần tử $x$ và mọi tập hợp $A$ và $B$ sao cho $A\subseteq B$, việc thêm $x$ vào $A$ mang lại sự gia tăng lớn hơn cho $f$ so với việc thêm $x$ vào $B$:
$$A\subseteq B \Rightarrow (f(A \cup \{x\}) - f(A)) \geq (f(B\cup \{x\}) - f(B))\ .$$
Submodularity nắm bắt ý niệm trực quan về <i>lợi suất giảm dần</i> (diminishing returns). Giá trị thông tin, được xem như một hàm $f$ trên các tập hợp các quan sát có thể có, có phải là submodular không? Chứng minh điều này hoặc tìm một phản ví dụ.

<!-- tabs:end -->
