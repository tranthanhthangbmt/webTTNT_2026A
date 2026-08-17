# Chapter 22 Deep Learning

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_22_Deep%20Learning/chapter_22_vi.html?v=5" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_22_Deep%20Learning.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter22_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter22/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
<div id="quiz-container" data-chapter="22"></div>

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Passive-ADP-Agent.md" target="_blank">PASSIVE-ADP-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Passive-TD-Agent.md" target="_blank">PASSIVE-TD-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Q-Learning-Agent.md" target="_blank">Q-LEARNING-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Hits.md" target="_blank">HITS</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Neural Nets**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/neural_nets.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/neural_nets.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/neural_nets.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 22.1

Bài tập này khám phá chất lượng của mô hình $n$-gram ngôn ngữ.
Tìm hoặc tạo một corpus đơn ngữ gồm 100.000 từ trở lên. Phân tách nó
thành các từ và tính tần suất của mỗi từ. Có bao nhiêu từ riêng biệt?
Cũng đếm tần suất của bigram (hai từ liên tiếp) và trigram (ba từ liên tiếp).
Bây giờ, sử dụng các tần suất đó để tạo ngôn ngữ: từ các mô hình unigram,
bigram và trigram, lần lượt, tạo một văn bản 100 từ bằng cách đưa ra các lựa chọn ngẫu nhiên
theo số đếm tần suất. So sánh ba văn bản được tạo ra với ngôn ngữ thực tế.
Cuối cùng, tính toán perplexity của mỗi mô hình.


---

##### Bài tập 22.2

Viết một chương trình để thực hiện <b>segmentation</b> từ
mà không có khoảng trắng. Cho một chuỗi, chẳng hạn như URL
“thelongestlistofthelongeststuffatthelongestdomainnameatlonglast.com,”
trả về một danh sách các từ thành phần: [“the,” “longest,” “list,”
$\ldots$]. Nhiệm vụ này hữu ích cho việc phân tích cú pháp URL,
sửa lỗi chính tả khi các từ dính liền nhau và cho các ngôn ngữ như tiếng Trung
không có khoảng trắng giữa các từ. Nó có thể được giải quyết bằng mô hình từ
unigram hoặc bigram và một thuật toán lập trình động tương tự như thuật toán Viterbi.


---

##### Bài tập 22.3

<i>Định luật Zipf</i> về phân phối từ phát biểu như sau:
Lấy một corpus văn bản lớn, đếm tần suất của mọi từ trong corpus,
sau đó xếp hạng các tần suất này theo thứ tự giảm dần. Gọi $f_{I}$ là tần suất lớn thứ $I$ trong danh sách này;
nghĩa là, $f_{1}$ là tần suất của từ phổ biến nhất (thường là “the”), $f_{2}$ là tần suất của từ phổ biến thứ hai, v.v.
Định luật Zipf phát biểu rằng $f_{I}$ xấp xỉ bằng $\alpha / I$ với một hằng số $\alpha$ nào đó.
Định luật có xu hướng rất chính xác ngoại trừ các giá trị rất nhỏ và rất lớn của $I$.


---

##### Bài tập 22.4

Chọn một corpus gồm ít nhất 20.000 từ văn bản trực tuyến và xác minh
Định luật Zipf bằng thực nghiệm. Xác định một thước đo lỗi và tìm giá trị
của $\alpha$ mà Định luật Zipf khớp tốt nhất với dữ liệu thực nghiệm của bạn.
Tạo một biểu đồ log-log vẽ $f_{I}$ so với $I$ và $\alpha/I$ so với $I$.
(Trên biểu đồ log-log, hàm $\alpha/I$ là một đường thẳng.) Khi thực hiện thí nghiệm,
hãy chắc chắn loại bỏ bất kỳ token định dạng nào (ví dụ: thẻ HTML) và chuẩn hóa chữ hoa và chữ thường.


---

##### Bài tập 22.5

(Chuyển thể từ <a class="paperRef" title="" href="">Jurafsky+Martin:2000</a>.) Trong bài tập này, bạn sẽ phát triển một bộ phân loại
cho việc xác định tác giả: cho trước một văn bản, bộ phân loại dự đoán
tác giả nào trong hai tác giả ứng viên đã viết văn bản đó. Thu thập các mẫu văn bản từ hai tác giả khác nhau.
Phân tách chúng thành tập huấn luyện và tập kiểm tra. Bây giờ, huấn luyện một language model trên tập huấn luyện.
Bạn có thể chọn các features để sử dụng; $n$-grams của từ hoặc chữ cái là dễ nhất,
nhưng bạn có thể thêm các features bổ sung mà bạn nghĩ có thể hữu ích.
Sau đó, tính xác suất của văn bản dưới mỗi language model và chọn mô hình có xác suất cao nhất.
Đánh giá độ chính xác của kỹ thuật này. Độ chính xác thay đổi như thế nào khi bạn thay đổi tập hợp các features?
Phân ngành ngôn ngữ học này được gọi là <b>stylometry</b>;
thành công của nó bao gồm việc xác định tác giả của các tác phẩm tranh chấp
<i>Federalist Papers</i> <a class="paperRef" title="" href="">Mosteller+Wallace:1964</a> và một số tác phẩm tranh chấp của Shakespeare
<a class="paperRef" title="" href="">Hope:1994</a>. <a class="paperRef" title="" href="">Khmelev+Tweedie:2001</a> đạt được kết quả tốt với một mô hình bigram chữ cái đơn giản.


---

##### Bài tập 22.6

Bài tập này liên quan đến việc phân loại email spam.
Tạo một corpus email spam và một corpus email không phải spam.
Kiểm tra từng corpus và quyết định những features nào có vẻ hữu ích cho việc phân loại:
từ unigram? bigram? độ dài tin nhắn, người gửi, thời gian nhận?
Sau đó, huấn luyện một thuật toán phân loại (cây quyết định, naive Bayes, SVM,
hồi quy logistic, hoặc một thuật toán khác bạn chọn) trên một tập huấn luyện và báo cáo độ chính xác của nó trên một tập kiểm tra.


---

##### Bài tập 22.7

Tạo một tập kiểm tra gồm mười truy vấn và gửi chúng đến ba công cụ tìm kiếm Web chính.
Đánh giá từng công cụ về precision ở 1, 3 và 10 tài liệu. Bạn có thể giải thích sự khác biệt giữa các công cụ không?


---

##### Bài tập 22.8

Thử xác định xem công cụ tìm kiếm nào từ bài tập trước đang sử dụng
case folding, stemming, từ đồng nghĩa và sửa lỗi chính tả.


---

##### Bài tập 22.9

Ước tính lượng không gian lưu trữ cần thiết cho index của một corpus
100 tỷ trang web. Trình bày các giả định bạn đã đưa ra.


---

##### Bài tập 22.10

Viết một biểu thức chính quy hoặc một chương trình ngắn để trích xuất tên công ty.
Kiểm tra nó trên một corpus các bài báo kinh doanh. Báo cáo recall và precision của bạn.


---

##### Bài tập 22.11

Xem xét bài toán cố gắng đánh giá chất lượng của một hệ thống IR
trả về một danh sách kết quả được xếp hạng (như hầu hết các công cụ tìm kiếm Web).
Thước đo chất lượng phù hợp phụ thuộc vào mô hình giả định về những gì người tìm kiếm
đang cố gắng đạt được và chiến lược cô ấy sử dụng. Đối với mỗi mô hình sau đây,
đề xuất một thước đo số tương ứng.<br>

1.  Người tìm kiếm sẽ xem xét hai mươi kết quả đầu tiên được trả về, với
    mục tiêu thu thập càng nhiều thông tin liên quan càng tốt.<br>

2.  Người tìm kiếm chỉ cần một tài liệu liên quan và sẽ đi xuống danh sách
    cho đến khi cô ấy tìm thấy tài liệu đầu tiên.<br>

3.  Người tìm kiếm có một truy vấn khá hẹp và có thể xem xét tất cả
    các kết quả được truy xuất. Cô ấy muốn chắc chắn rằng mình đã xem
    thấy mọi thứ trong bộ sưu tập tài liệu có liên quan đến truy vấn của mình.
    (Ví dụ: một luật sư muốn chắc chắn rằng cô ấy đã tìm thấy
    <i>tất cả</i> các tiền lệ liên quan và sẵn sàng chi một khoản
    chi phí đáng kể cho việc đó.)<br>

4.  Người tìm kiếm chỉ cần một tài liệu liên quan đến truy vấn và có thể
    chi trả cho một trợ lý nghiên cứu làm việc một giờ để xem xét
    kết quả. Trợ lý có thể xem xét 100 tài liệu được truy xuất trong một giờ.
    Trợ lý sẽ tính phí người tìm kiếm cho toàn bộ giờ làm việc bất kể
    việc tìm thấy ngay lập tức hay vào cuối giờ.<br>

5.  Người tìm kiếm sẽ xem xét tất cả các kết quả. Việc xem xét một tài liệu
    có chi phí \$ A; tìm thấy một tài liệu liên quan có giá trị \$ B;
    không tìm thấy một tài liệu liên quan có chi phí \$ C cho mỗi tài liệu liên quan
    không tìm thấy.<br>

6.  Người tìm kiếm muốn thu thập càng nhiều tài liệu liên quan càng tốt,
    nhưng cần sự khuyến khích đều đặn. Cô ấy xem xét các tài liệu theo thứ tự.
    Nếu các tài liệu cô ấy đã xem cho đến nay chủ yếu là tốt, cô ấy sẽ tiếp tục;
    nếu không, cô ấy sẽ dừng lại.


---

<!-- tabs:end -->
