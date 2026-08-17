# Chapter 13 Probalilistic Reasoning

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_13_Probalilistic%20Reasoning/chapter_13_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_13_Probalilistic%20Reasoning.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter13_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter13/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/Enumeration-Ask.md" target="_blank" data-ignore>ENUMERATION-ASK</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Elimination-Ask.md" target="_blank" data-ignore>ELIMINATION-ASK</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Prior-Sample.md" target="_blank" data-ignore>PRIOR-SAMPLE</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Rejection-Sampling.md" target="_blank" data-ignore>REJECTION-SAMPLING</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Likelihood-Weighting.md" target="_blank" data-ignore>LIKELIHOOD-WEIGHTING</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Gibbs-Ask.md" target="_blank" data-ignore>GIBBS-ASK</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/probability.ipynb"  target="_blank" data-ignore>Probability</a>
- <a href="python_runner.html?file=codeAndExercises/aima-python-master/notebooks/probability.py"  target="_blank" data-ignore>Probability (Python File)</a>


#### **Bài tập**


##### Bài tập 13.1

Chứng minh từ các nguyên tắc cơ bản rằng $P(a{{\,|\,}}b\land a) = 1$.


---

##### Bài tập 13.2

Sử dụng các tiên đề xác suất, chứng minh rằng mọi phân phối xác suất trên một biến ngẫu nhiên rời rạc phải có tổng bằng 1.


---

##### Bài tập 13.3

Đối với mỗi mệnh đề sau, hãy chứng minh nó đúng hoặc đưa ra một phản ví dụ.<br>

1.  Nếu $P(a {{\,|\,}}b, c) = P(b {{\,|\,}}a, c)$, thì $P(a {{\,|\,}}c) = P(b {{\,|\,}}c)$ <br>

2.  Nếu $P(a {{\,|\,}}b, c) = P(a)$, thì $P(b {{\,|\,}}c) = P(b)$ <br>

3.  Nếu $P(a {{\,|\,}}b) = P(a)$, thì $P(a {{\,|\,}}b, c) = P(a {{\,|\,}}c)$<br>


---

##### Bài tập 13.4

Liệu có hợp lý cho một agent để giữ ba niềm tin $P(A) = 0.4$, $P(B) = 0.3$, và $P(A \lor B) = 0.5$ không? Nếu có, thì khoảng xác suất nào sẽ hợp lý cho agent để giữ cho $A \land B$? Hãy tạo một bảng giống như bảng trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/de-finetti-table.png">de-finetti-table</a>, và cho thấy cách nó hỗ trợ lập luận của bạn về tính hợp lý. Sau đó, vẽ một phiên bản khác của bảng với $P(A \lor B) = 0.7$. Giải thích tại sao việc có xác suất này lại hợp lý, ngay cả khi bảng cho thấy một trường hợp thua lỗ và ba trường hợp hòa vốn. (<i>Gợi ý:</i> Agent 1 cam kết điều gì về xác suất của mỗi trường hợp trong bốn trường hợp, đặc biệt là trường hợp thua lỗ?)


---

##### Bài tập 13.5

Câu hỏi này liên quan đến các thuộc tính của các thế giới khả dĩ, được định nghĩa trên trang <a class="pageRef" title="" href="#">possible-worlds-page</a> là các phép gán cho tất cả các biến ngẫu nhiên. Chúng ta sẽ làm việc với các mệnh đề tương ứng với đúng một thế giới khả dĩ vì chúng xác định các phép gán của tất cả các biến. Trong lý thuyết xác suất, các mệnh đề như vậy được gọi là <b>atomic event</b>. Ví dụ, với các biến Boolean $X_1$, $X_2$, $X_3$, mệnh đề $x_1\land \lnot x_2 \land \lnot x_3$ xác định phép gán của các biến; theo ngôn ngữ logic mệnh đề, chúng ta sẽ nói rằng nó có đúng một mô hình.<br>

1.  Chứng minh, đối với trường hợp $n$ biến Boolean, rằng hai atomic event phân biệt bất kỳ là loại trừ lẫn nhau; nghĩa là, phép hội của chúng tương đương với ${false}$.<br>

2.  Chứng minh rằng phép tuyển của tất cả các atomic event khả dĩ là tương đương logic với ${true}$.<br>

3.  Chứng minh rằng mọi mệnh đề là tương đương logic với phép tuyển của các atomic event mà kéo theo tính đúng đắn của nó.<br>


---

##### Bài tập 13.6

Chứng minh Phương trình (<a class="equationRef" title="" href="#">kolmogorov-disjunction-equation</a>) từ Phương trình (<a class="equationRef" title="" href="#">basic-probability-axiom-equation</a>) và (<a class="equationRef" title="" href="#">proposition-probability-equation</a>).


---

##### Bài tập 13.7

Xem xét tập hợp tất cả các bộ bài poker năm lá được chia công bằng từ một bộ bài tiêu chuẩn năm mươi hai lá.<br>

1.  Có bao nhiêu atomic event trong phân phối xác suất chung (tức là, có bao nhiêu bộ bài năm lá)?<br>

2.  Xác suất của mỗi atomic event là bao nhiêu?<br>

3.  Xác suất để được chia một bộ sảnh thùng phá sảnh (royal straight flush)? Bốn lá giống nhau (four of a kind)?


---

##### Bài tập 13.8

Cho phân phối xác suất chung đầy đủ được hiển thị trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/dentist-joint-table.png">dentist-joint-table</a>, hãy tính toán các giá trị sau:<br>

1.  $\textbf{P}({toothache})$.<br>

2.  $\textbf{P}({Cavity})$.<br>

3.  $\textbf{P}({Toothache}{{\,|\,}}{cavity})$.<br>

4.  $\textbf{P}({Cavity}{{\,|\,}}{toothache}\lor {catch})$.


---

##### Bài tập 13.9

Cho phân phối xác suất chung đầy đủ được hiển thị trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/dentist-joint-table.png">dentist-joint-table</a>, hãy tính toán các giá trị sau:<br>

1.  $\textbf{P}({toothache})$.<br>

2.  $\textbf{P}({Catch})$.<br>

3.  $\textbf{P}({Cavity}{{\,|\,}}{catch})$.<br>

4.  $\textbf{P}({Cavity}{{\,|\,}}{toothache}\lor {catch})$.<br>


---

##### Bài tập 13.10

Trong lá thư ngày 24 tháng 8 năm 1654, Pascal đã cố gắng chỉ ra cách phân bổ một khoản tiền khi một trò chơi cờ bạc phải kết thúc sớm. Hãy tưởng tượng một trò chơi mà mỗi lượt bao gồm việc tung một con xúc xắc, người chơi <i>E</i> nhận được một điểm khi xúc xắc là số chẵn, và người chơi <i>O</i> nhận được một điểm khi xúc xắc là số lẻ. Người chơi đầu tiên đạt được 7 điểm sẽ thắng pot. Giả sử trò chơi bị gián đoạn với tỷ số <i>E</i> dẫn trước 4–2. Làm thế nào để chia tiền một cách công bằng trong trường hợp này? Công thức tổng quát là gì? (Fermat và Pascal đã mắc một số lỗi trước khi giải quyết vấn đề, nhưng bạn nên giải quyết đúng ngay từ lần đầu.)


---

##### Bài tập 13.11

Quyết định sử dụng lý thuyết xác suất một cách hiệu quả, chúng ta gặp một máy đánh bạc với ba bánh xe độc lập, mỗi bánh xe tạo ra một trong bốn ký hiệu bar, bell, lemon, hoặc cherry với xác suất bằng nhau. Máy đánh bạc có sơ đồ trả thưởng sau cho một lần đặt cược 1 xu (trong đó "?" biểu thị rằng chúng ta không quan tâm đến kết quả của bánh xe đó): <br>

> bar/bar/bar trả 20 xu<br>

> bell/bell/bell trả 15 xu<br>

> lemon/lemon/lemon trả 5 xu<br>

> cherry/cherry/cherry trả 3 xu<br>

> cherry/cherry/? trả 2 xu<br>

> cherry/?/? trả 1 xu<br>

1.  Tính toán tỷ lệ "hoàn tiền" dự kiến của máy. Nói cách khác, với mỗi xu được chơi, lợi tức dự kiến bằng xu là bao nhiêu?<br>

2.  Tính xác suất để chơi máy đánh bạc một lần sẽ dẫn đến chiến thắng.<br>

3.  Ước tính số lần chơi trung bình và trung vị mà bạn có thể mong đợi cho đến khi bạn hết tiền, nếu bạn bắt đầu với 10 xu. Bạn có thể chạy một mô phỏng để ước tính điều này, thay vì cố gắng tính toán một câu trả lời chính xác.<br>


---

##### Bài tập 13.12

Quyết định sử dụng lý thuyết xác suất một cách hiệu quả, chúng ta gặp một máy đánh bạc với ba bánh xe độc lập, mỗi bánh xe tạo ra một trong bốn ký hiệu bar, bell, lemon, hoặc cherry với xác suất bằng nhau. Máy đánh bạc có sơ đồ trả thưởng sau cho một lần đặt cược 1 xu (trong đó "?" biểu thị rằng chúng ta không quan tâm đến kết quả của bánh xe đó): <br>

> bar/bar/bar trả 20 xu<br>

> bell/bell/bell trả 15 xu<br>

> lemon/lemon/lemon trả 5 xu<br>

> cherry/cherry/cherry trả 3 xu<br>

> cherry/cherry/? trả 2 xu<br>

> cherry/?/? trả 1 xu<br>

1.  Tính toán tỷ lệ "hoàn tiền" dự kiến của máy. Nói cách khác, với mỗi xu được chơi, lợi tức dự kiến bằng xu là bao nhiêu?<br>

2.  Tính xác suất để chơi máy đánh bạc một lần sẽ dẫn đến chiến thắng.<br>

3.  Ước tính số lần chơi trung bình và trung vị mà bạn có thể mong đợi cho đến khi bạn hết tiền, nếu bạn bắt đầu với 10 xu. Bạn có thể chạy một mô phỏng để ước tính điều này, thay vì cố gắng tính toán một câu trả lời chính xác.<br>


---

##### Bài tập 13.13

Chúng ta muốn truyền một thông điệp $n$ bit đến một agent nhận. Các bit trong thông điệp bị hỏng (lật) một cách độc lập trong quá trình truyền với xác suất $\epsilon$ cho mỗi bit. Với một bit kiểm tra chẵn lẻ bổ sung được gửi cùng với thông tin ban đầu, một thông điệp có thể được sửa bởi người nhận nếu có tối đa một bit trong toàn bộ thông điệp (bao gồm cả bit kiểm tra chẵn lẻ) bị hỏng. Giả sử chúng ta muốn đảm bảo rằng thông điệp chính xác được nhận với xác suất ít nhất $1-\delta$. Giá trị $n$ khả thi tối đa là bao nhiêu? Tính giá trị này cho trường hợp $\epsilon = 0.001$, $\delta = 0.01$.


---

##### Bài tập 13.14

Chúng ta muốn truyền một thông điệp $n$ bit đến một agent nhận. Các bit trong thông điệp bị hỏng (lật) một cách độc lập trong quá trình truyền với xác suất $\epsilon$ cho mỗi bit. Với một bit kiểm tra chẵn lẻ bổ sung được gửi cùng với thông tin ban đầu, một thông điệp có thể được sửa bởi người nhận nếu có tối đa một bit trong toàn bộ thông điệp (bao gồm cả bit kiểm tra chẵn lẻ) bị hỏng. Giả sử chúng ta muốn đảm bảo rằng thông điệp chính xác được nhận với xác suất ít nhất $1-\delta$. Giá trị $n$ khả thi tối đa là bao nhiêu? Tính giá trị này cho trường hợp $\epsilon{{\,=\,}}0.002$, $\delta{{\,=\,}}0.01$.


---

##### Bài tập 13.15

Chứng minh rằng ba dạng độc lập trong Phương trình (<a class="equationRef" title="" href="#">independence-equation</a>) là tương đương.


---

##### Bài tập 13.16

Xem xét hai xét nghiệm y tế, A và B, cho một loại virus. Xét nghiệm A có hiệu quả 95% trong việc phát hiện virus khi nó có mặt, nhưng có tỷ lệ dương tính giả là 10% (cho thấy virus có mặt, trong khi thực tế không có). Xét nghiệm B có hiệu quả 90% trong việc phát hiện virus, nhưng có tỷ lệ dương tính giả là 5%. Hai xét nghiệm sử dụng các phương pháp độc lập để xác định virus. Virus lây nhiễm cho 1% dân số. Giả sử một người được xét nghiệm virus chỉ bằng một trong hai xét nghiệm, và xét nghiệm đó cho kết quả dương tính với việc mang virus. Xét nghiệm nào cho kết quả dương tính có ý nghĩa hơn về việc một người thực sự mang virus? Biện minh câu trả lời của bạn bằng toán học.


---

##### Bài tập 13.17

Giả sử bạn được cho một đồng xu có xác suất ra mặt ${heads}$ là $x$ và xác suất ra mặt ${tails}$ là $1 - x$. Các kết quả của các lần tung đồng xu liên tiếp có độc lập với nhau khi bạn biết giá trị của $x$ không? Các kết quả của các lần tung đồng xu liên tiếp có độc lập với nhau nếu bạn *không* biết giá trị của $x$ không? Biện minh câu trả lời của bạn.


---

##### Bài tập 13.18

Sau lần kiểm tra sức khỏe hàng năm, bác sĩ có tin xấu và tin tốt. Tin xấu là bạn đã xét nghiệm dương tính với một căn bệnh nghiêm trọng và xét nghiệm này có độ chính xác 99% (tức là, xác suất xét nghiệm dương tính khi bạn mắc bệnh là 0.99, cũng như xác suất xét nghiệm âm tính khi bạn không mắc bệnh). Tin tốt là căn bệnh này hiếm gặp, chỉ ảnh hưởng đến 1 trên 10.000 người ở độ tuổi của bạn. Tại sao việc căn bệnh hiếm gặp lại là tin tốt? Cơ hội bạn thực sự mắc bệnh là bao nhiêu?


---

##### Bài tập 13.19

Sau lần kiểm tra sức khỏe hàng năm, bác sĩ có tin xấu và tin tốt. Tin xấu là bạn đã xét nghiệm dương tính với một căn bệnh nghiêm trọng và xét nghiệm này có độ chính xác 99% (tức là, xác suất xét nghiệm dương tính khi bạn mắc bệnh là 0.99, cũng như xác suất xét nghiệm âm tính khi bạn không mắc bệnh). Tin tốt là căn bệnh này hiếm gặp, chỉ ảnh hưởng đến 1 trên 100.000 người ở độ tuổi của bạn. Tại sao việc căn bệnh hiếm gặp lại là tin tốt? Cơ hội bạn thực sự mắc bệnh là bao nhiêu?


---

##### Bài tập 13.20

Thông thường, rất hữu ích khi xem xét ảnh hưởng của một số mệnh đề cụ thể trong bối cảnh của một bằng chứng nền chung được giữ cố định, thay vì trong sự vắng mặt hoàn toàn của thông tin. Các câu hỏi sau đây yêu cầu bạn chứng minh các phiên bản tổng quát hơn của quy tắc nhân và quy tắc Bayes, liên quan đến một bằng chứng nền $\textbf{e}$: <br>

1.  Chứng minh phiên bản có điều kiện của quy tắc nhân tổng quát:
    $${\textbf{P}}(X,Y {{\,|\,}}\textbf{e}) = {\textbf{P}}(X{{\,|\,}}Y,\textbf{e}) {\textbf{P}}(Y{{\,|\,}}\textbf{e})\ .$$ <br>

2.  Chứng minh phiên bản có điều kiện của quy tắc Bayes trong Phương trình (<a class="equationRef" title="" href="#">conditional-bayes-equation</a>). <br>


---

##### Bài tập 13.21

Chứng minh rằng phát biểu về sự độc lập có điều kiện
$${\textbf{P}}(X,Y  | Z) = {\textbf{P}}(X | Z) {\textbf{P}}(Y | Z)$$
tương đương với mỗi phát biểu
$${\textbf{P}}(X | Y,Z) = {\textbf{P}}(X | Z) \quad\mbox{và}\quad {\textbf{P}}(Y | X,Z) = {\textbf{P}}(Y | Z)\ .$$


---

##### Bài tập 13.22

Giả sử bạn được cho một túi chứa $n$ đồng xu không thiên vị. Bạn được cho biết rằng $n-1$ trong số các đồng xu này là bình thường, một mặt là mặt ngửa và mặt kia là mặt sấp, trong khi một đồng xu là giả, có hai mặt ngửa. <br>

1.  Giả sử bạn thò tay vào túi, chọn ngẫu nhiên một đồng xu, tung nó và được mặt ngửa. Xác suất (có điều kiện) mà đồng xu bạn chọn là đồng xu giả là bao nhiêu? <br>

2.  Giả sử bạn tiếp tục tung đồng xu đó tổng cộng $k$ lần sau khi chọn nó và thấy $k$ lần mặt ngửa. Bây giờ xác suất có điều kiện mà bạn đã chọn đồng xu giả là bao nhiêu? <br>

3.  Giả sử bạn muốn quyết định xem đồng xu được chọn là giả hay không bằng cách tung nó $k$ lần. Thủ tục quyết định trả về ${fake}$ nếu tất cả $k$ lần tung đều ra mặt ngửa; nếu không, nó trả về ${normal}$. Xác suất (không có điều kiện) mà thủ tục này mắc lỗi là bao nhiêu?


---

##### Bài tập 13.23

Trong bài tập này, bạn sẽ hoàn thành phép tính chuẩn hóa cho ví dụ về viêm màng não. Đầu tiên, hãy đưa ra một giá trị phù hợp cho $P(s{{\,|\,}}\lnot m)$, và sử dụng nó để tính toán các giá trị chưa chuẩn hóa cho $P(m{{\,|\,}}s)$ và $P(\lnot m {{\,|\,}}s)$ (tức là, bỏ qua số hạng $P(s)$ trong biểu thức quy tắc Bayes, Phương trình (<a class="equationRef" title="" href="#">meningitis-bayes-equation</a>)). Bây giờ hãy chuẩn hóa các giá trị này sao cho chúng cộng lại bằng 1.


---

##### Bài tập 13.24

Bài tập này điều tra cách các mối quan hệ độc lập có điều kiện ảnh hưởng đến lượng thông tin cần thiết cho các phép tính xác suất.<br>

1.  Giả sử chúng ta muốn tính $P(h{{\,|\,}}e_1,e_2)$ và chúng ta không có thông tin độc lập có điều kiện. Những tập hợp số nào sau đây là đủ cho phép tính?<br>

    1.  ${\textbf{P}}(E_1,E_2)$, ${\textbf{P}}(H)$,
        ${\textbf{P}}(E_1{{\,|\,}}H)$,
        ${\textbf{P}}(E_2{{\,|\,}}H)$

    2.  ${\textbf{P}}(E_1,E_2)$, ${\textbf{P}}(H)$,
        ${\textbf{P}}(E_1,E_2{{\,|\,}}H)$<br>

    3.  ${\textbf{P}}(H)$,
        ${\textbf{P}}(E_1{{\,|\,}}H)$,
        ${\textbf{P}}(E_2{{\,|\,}}H)$<br>

2.  Giả sử chúng ta biết rằng
    ${\textbf{P}}(E_1{{\,|\,}}H,E_2)={\textbf{P}}(E_1{{\,|\,}}H)$
    cho tất cả các giá trị của $H$, $E_1$, $E_2$. Bây giờ tập hợp nào là đủ?


---

##### Bài tập 13.25

Cho $X$, $Y$, $Z$ là các biến ngẫu nhiên Boolean. Gán nhãn tám mục trong phân phối chung ${\textbf{P}}(X,Y,Z)$ là $a$ đến $h$. Biểu diễn phát biểu rằng $X$ và $Y$ độc lập có điều kiện khi biết $Z$, dưới dạng một tập hợp các phương trình liên hệ $a$ đến $h$. Có bao nhiêu phương trình *không dư thừa*?


---

##### Bài tập 13.26

(Chuyển thể từ Pearl [<a class="paperRef" title="" href="">Pearl:1988</a>].) Giả sử bạn là nhân chứng của một vụ tai nạn bỏ chạy ban đêm liên quan đến một chiếc taxi ở Athens. Tất cả taxi ở Athens đều màu xanh lam hoặc xanh lục. Bạn thề, dưới lời thề, rằng chiếc taxi màu xanh lam. Các thử nghiệm rộng rãi cho thấy rằng, trong điều kiện ánh sáng yếu, việc phân biệt giữa màu xanh lam và xanh lục có độ tin cậy 75%. <br>

1.  Có thể tính toán màu sắc có khả năng xảy ra nhất cho chiếc taxi không? (*Gợi ý:* phân biệt cẩn thận giữa mệnh đề rằng chiếc taxi *là* màu xanh lam và mệnh đề rằng nó *có vẻ* màu xanh lam.) <br>

2.  Điều gì sẽ xảy ra nếu bạn biết rằng 9 trên 10 taxi ở Athens là màu xanh lục?<br>


---

##### Bài tập 13.27

Viết ra một thuật toán tổng quát để trả lời các truy vấn có dạng ${\textbf{P}}({Cause}{{\,|\,}}\textbf{e})$, sử dụng một phân phối naive Bayes. Giả sử rằng bằng chứng $\textbf{e}$ có thể gán giá trị cho *bất kỳ tập con* nào của các biến hiệu ứng.


---

##### Bài tập 13.28

Phân loại văn bản là nhiệm vụ gán một tài liệu cho trước vào một trong một tập hợp các danh mục cố định dựa trên văn bản mà nó chứa. Các mô hình Naive Bayes thường được sử dụng cho nhiệm vụ này. Trong các mô hình này, biến truy vấn là danh mục tài liệu, và các biến "hiệu ứng" là sự hiện diện hoặc vắng mặt của mỗi từ trong ngôn ngữ; giả định là các từ xuất hiện độc lập trong các tài liệu, với tần suất được xác định bởi danh mục tài liệu.<br>

1.  Giải thích chính xác cách một mô hình như vậy có thể được xây dựng, với dữ liệu "huấn luyện" là một tập hợp các tài liệu đã được gán vào các danh mục.<br>

2.  Giải thích chính xác cách phân loại một tài liệu mới.<br>

3.  Giả thuyết độc lập có điều kiện có hợp lý không? Thảo luận.<br>


---

##### Bài tập 13.29

Trong phân tích của chúng ta về thế giới wumpus, chúng ta đã sử dụng thực tế là mỗi ô chứa một cái hố với xác suất 0.2, độc lập với nội dung của các ô khác. Thay vào đó, giả sử rằng chính xác $N/5$ cái hố được rải ngẫu nhiên trong số $N$ ô khác với [1,1]. Các biến $P_{i,j}$ và $P_{k,l}$ có còn độc lập không? Phân phối chung ${\textbf{P}}(P_{1,1},\ldots,P_{4,4})$ bây giờ là gì? Thực hiện lại phép tính cho xác suất của các hố ở [1,3] và [2,2].


---

##### Bài tập 13.30

Thực hiện lại phép tính xác suất cho các hố ở [1,3] và [2,2], giả sử rằng mỗi ô chứa một cái hố với xác suất 0.01, độc lập với các ô khác. Bạn có thể nói gì về hiệu suất tương đối của một agent logic so với một agent xác suất trong trường hợp này?


---

##### Bài tập 13.31

Triển khai một agent xác suất lai cho thế giới wumpus, dựa trên agent lai trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/hybrid-wumpus-agent-algorithm.png">hybrid-wumpus-agent-algorithm</a> và quy trình suy luận xác suất được phác thảo trong chương này.


---

<!-- tabs:end -->
