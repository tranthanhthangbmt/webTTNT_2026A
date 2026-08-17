# Chapter 18 Probalilistic Programming

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_18_Probalilistic%20Programming/chapter_18_vi.html?v=2" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_18_Probalilistic%20Programming.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter18_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter18/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/Doubles-Tennis-Problem.md" target="_blank" data-ignore>DOUBLES-TENNIS-PROBLEM</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**


##### Bài tập 18.1

Hãy xem xét vấn đề mà một em bé gặp phải khi học nói và hiểu một ngôn ngữ. Giải thích quá trình này phù hợp với mô hình học tập tổng quát như thế nào. Mô tả các percept và hành động của em bé, cũng như các loại học tập mà em bé phải thực hiện. Mô tả các subfunctions mà em bé đang cố gắng học theo các thuật ngữ về đầu vào và đầu ra, cũng như dữ liệu ví dụ có sẵn.


---

##### Bài tập 18.2

Lặp lại Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/concept-learning-exercises/ex_1/">infant-language-exercise</a> cho trường hợp học chơi quần vợt (hoặc một môn thể thao khác mà bạn quen thuộc). Đây là supervised learning hay reinforcement learning?


---

##### Bài tập 18.3

Vẽ một cây quyết định cho bài toán quyết định có nên di chuyển về phía trước tại một giao lộ đường bộ hay không, với điều kiện là đèn vừa chuyển sang màu xanh.


---

##### Bài tập 18.4

Chúng ta không bao giờ kiểm tra cùng một thuộc tính hai lần trên một đường đi trong cây quyết định. Tại sao không?


---

##### Bài tập 18.5

Giả sử chúng ta tạo một tập huấn luyện từ một cây quyết định và sau đó áp dụng thuật toán học cây quyết định cho tập huấn luyện đó. Liệu thuật toán học có cuối cùng trả về cây chính xác khi kích thước tập huấn luyện tiến tới vô cùng không? Tại sao có hoặc tại sao không?


---

##### Bài tập 18.6

Trong quá trình xây dựng đệ quy các cây quyết định, đôi khi xảy ra trường hợp một tập hợp hỗn hợp các ví dụ tích cực và tiêu cực còn lại tại một nút lá, ngay cả sau khi tất cả các thuộc tính đã được sử dụng. Giả sử chúng ta có $p$ ví dụ tích cực và $n$ ví dụ tiêu cực.<br>

1.  Chứng minh rằng giải pháp được sử dụng bởi DECISION-TREE-LEARNING, chọn phân loại theo đa số, tối thiểu hóa sai số tuyệt đối trên tập hợp các ví dụ tại nút lá.<br>

2.  Chứng minh rằng <b>xác suất lớp</b> $p/(p+n)$ tối thiểu hóa tổng bình phương sai số.


---

##### Bài tập 18.7

Giả sử một thuộc tính chia tập hợp các ví dụ $E$ thành các tập con $E_k$ và mỗi tập con có $p_k$ ví dụ tích cực và $n_k$ ví dụ tiêu cực. Chứng minh rằng thuộc tính có thông tin tăng trưởng (information gain) dương nghiêm ngặt trừ khi tỷ lệ $p_k/(p_k+n_k)$ giống nhau cho tất cả $k$.


---

##### Bài tập 18.8

Xem xét tập dữ liệu sau đây bao gồm ba thuộc tính đầu vào nhị phân ($A_1, A_2$, và $A_3$) và một đầu ra nhị phân:<br>

$$
\begin{array} 
	{|r|r|}\hline \textbf{Ví dụ} & A_1 & A_2 & A_3 & Output\space y \\ 
	\hline \textbf{x}_1 & 1 & 0 & 0 & 0 \\ 
	\textbf{x}_2 & 1 & 0 & 1 & 0 \\ 
	 \textbf{x}_3 & 0 & 1 & 0 & 0 \\ 
	 \textbf{x}_4 & 1 & 1 & 1 & 1 \\ 
	\textbf{x}_5 & 1 & 1 & 0 & 1 \\ 
	\hline  
\end{array}
$$
Sử dụng thuật toán trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/DTL-algorithm.png">DTL-algorithm</a> (trang <a class="pageRef" title="" href="#">DTL-algorithm</a>) để học một cây quyết định cho dữ liệu này. Trình bày các phép tính được thực hiện để xác định thuộc tính để phân tách tại mỗi nút.


---

##### Bài tập 18.9

Xây dựng một tập dữ liệu (tập hợp các ví dụ với các thuộc tính và phân loại) sẽ khiến thuật toán học cây quyết định tìm thấy một cây có kích thước không tối thiểu. Trình bày cây được thuật toán xây dựng và cây có kích thước tối thiểu mà bạn có thể tạo bằng tay.


---

##### Bài tập 18.10

Một đồ thị quyết định (decision graph) là một sự tổng quát hóa của cây quyết định, cho phép các nút (tức là, các thuộc tính được sử dụng để phân tách) có nhiều nút cha, thay vì chỉ một nút cha duy nhất. Đồ thị kết quả vẫn phải là đồ thị không có chu trình. Bây giờ, hãy xem xét hàm XOR của *ba* thuộc tính đầu vào nhị phân, hàm này cho ra giá trị 1 khi và chỉ khi một số lẻ trong ba thuộc tính đầu vào có giá trị 1.<br>

1.  Vẽ một cây quyết định có kích thước tối thiểu cho hàm XOR ba đầu vào.<br>

2.  Vẽ một đồ thị quyết định có kích thước tối thiểu cho hàm XOR ba đầu vào.<br>


---

##### Bài tập 18.11

Bài tập này xem xét việc cắt tỉa $\chi^2$ (pruning) các cây quyết định (Mục <a class="sectionRef" title="" href="#">chi-squared-section</a><br>.

1.  Tạo một tập dữ liệu với hai thuộc tính đầu vào, sao cho thông tin tăng trưởng (information gain) tại gốc cây cho cả hai thuộc tính bằng 0, nhưng có một cây quyết định có độ sâu 2 nhất quán với tất cả dữ liệu. Việc cắt tỉa $\chi^2$ sẽ làm gì trên tập dữ liệu này nếu được áp dụng từ dưới lên? Nếu được áp dụng từ trên xuống?<br>

2.  Sửa đổi DECISION-TREE-LEARNING để bao gồm việc cắt tỉa $\chi^2$. Bạn có thể tham khảo Quinlan [<a class="paperRef" title="" href="">Quinlan:1986</a>] hoặc [<a class="paperRef" title="" href="">Kearns+Mansour:1998</a>] để biết chi tiết.<br>


---

##### Bài tập 18.12

Thuật toán DECISION-TREE-LEARNING tiêu chuẩn được mô tả trong chương không xử lý các trường hợp mà một số ví dụ có giá trị thuộc tính bị thiếu.<br>

1.  Đầu tiên, chúng ta cần tìm một cách để phân loại các ví dụ như vậy, với một cây quyết định bao gồm các kiểm tra trên các thuộc tính mà giá trị có thể bị thiếu. Giả sử một ví dụ $\textbf{x}$ có giá trị bị thiếu cho thuộc tính $A$ và cây quyết định kiểm tra $A$ tại một nút mà $\textbf{x}$ đến. Một cách để xử lý trường hợp này là giả vờ rằng ví dụ có *tất cả* các giá trị có thể có cho thuộc tính đó, nhưng gán trọng số cho mỗi giá trị theo tần suất của nó trong tất cả các ví dụ đến nút đó trong cây quyết định. Thuật toán phân loại nên đi theo tất cả các nhánh tại bất kỳ nút nào mà giá trị bị thiếu và nên nhân các trọng số dọc theo mỗi đường đi. Viết một thuật toán phân loại sửa đổi cho cây quyết định có hành vi này.<br>

2.  Bây giờ, sửa đổi phép tính thông tin tăng trưởng (information gain) sao cho trong bất kỳ tập hợp ví dụ $C$ nào tại một nút nhất định trong cây trong quá trình xây dựng, các ví dụ có giá trị bị thiếu cho bất kỳ thuộc tính còn lại nào sẽ được gán các giá trị "như thể" theo tần suất của các giá trị đó trong tập $C$.<br>


---

##### Bài tập 18.13

Trong Mục <a class="sectionRef" title="" href="#">broadening-decision-tree-section</a>, chúng ta đã lưu ý rằng các thuộc tính có nhiều giá trị khác nhau có thể gây ra vấn đề với thước đo gain. Các thuộc tính như vậy có xu hướng chia các ví dụ thành nhiều lớp nhỏ hoặc thậm chí các lớp đơn lẻ, do đó có vẻ rất liên quan theo thước đo gain. Tiêu chí <b>gain-ratio</b> chọn các thuộc tính theo tỷ lệ giữa gain của chúng và nội dung thông tin nội tại của chúng—tức là, lượng thông tin chứa trong câu trả lời cho câu hỏi, "Giá trị của thuộc tính này là gì?" Do đó, tiêu chí gain-ratio cố gắng đo lường mức độ hiệu quả mà một thuộc tính cung cấp thông tin về phân loại chính xác của một ví dụ. Viết một biểu thức toán học cho nội dung thông tin của một thuộc tính và triển khai tiêu chí gain ratio trong DECISION-TREE-LEARNING.


---

##### Bài tập 18.14

Giả sử bạn đang chạy một thí nghiệm học tập trên một thuật toán mới cho phân loại Boolean. Bạn có một tập dữ liệu bao gồm 100 ví dụ tích cực và 100 ví dụ tiêu cực. Bạn dự định sử dụng cross-validation bỏ sót một phần tử (leave-one-out) và so sánh thuật toán của bạn với một hàm cơ sở, một bộ phân loại đa số đơn giản. (Một bộ phân loại đa số nhận một tập dữ liệu huấn luyện và sau đó luôn xuất ra lớp chiếm đa số trong tập dữ liệu huấn luyện, bất kể đầu vào.) Bạn mong đợi bộ phân loại đa số sẽ đạt khoảng 50% trên cross-validation bỏ sót một phần tử, nhưng bạn ngạc nhiên khi nó luôn đạt điểm 0. Bạn có thể giải thích tại sao không?


---

##### Bài tập 18.15

Giả sử một thuật toán học đang cố gắng tìm một giả thuyết nhất quán khi phân loại các ví dụ thực sự là ngẫu nhiên. Có $n$ thuộc tính Boolean, và các ví dụ được rút ra đồng nhất từ tập hợp $2^n$ ví dụ có thể có. Tính số lượng ví dụ cần thiết trước khi xác suất tìm thấy mâu thuẫn trong dữ liệu đạt 0.5.


---

##### Bài tập 18.16

Xây dựng một danh sách quyết định (decision list) để phân loại dữ liệu dưới đây. Chọn các kiểm tra nhỏ nhất có thể (về số lượng thuộc tính), phá vỡ các ràng buộc giữa các kiểm tra có cùng số lượng thuộc tính bằng cách chọn kiểm tra phân loại đúng số lượng ví dụ lớn nhất. Nếu nhiều kiểm tra có cùng số lượng thuộc tính và phân loại cùng số lượng ví dụ, thì phá vỡ ràng buộc bằng cách sử dụng các thuộc tính có chỉ số thấp hơn (ví dụ: chọn $A_1$ thay vì $A_2$).<br>

$$
\begin{array} 
	{|r|r|}\hline \textbf{Ví dụ} & A_1 & A_2 & A_3 & A_4 & y \\ 
	\hline \textbf{x}_1 & 1 & 0 & 0 & 0 & 1 \\ 
	\textbf{x}_2 & 1 & 0 & 1 & 1 & 1 \\ 
	 \textbf{x}_3 & 0 & 1 & 0 & 0 & 1 \\ 
	 \textbf{x}_4 & 0 & 1 & 1 & 0 & 0 \\ 
	 \textbf{x}_5 & 1 & 1 & 0 & 1 & 1 \\ 
	 \textbf{x}_6 & 0 & 1 & 0 & 1 & 0 \\ 
	 \textbf{x}_7 & 0 & 0 & 1 & 1 & 1 \\ 
	 \textbf{x}_8 & 0 & 0 & 1 & 0 & 0 \\ 
	\hline  
\end{array}
$$


---

##### Bài tập 18.17

Chứng minh rằng một danh sách quyết định có thể biểu diễn cùng một hàm như một cây quyết định trong khi sử dụng tối đa số quy tắc bằng số lá trong cây quyết định cho hàm đó. Đưa ra một ví dụ về hàm được biểu diễn bởi một danh sách quyết định sử dụng ít quy tắc hơn nghiêm ngặt so với số lá trong cây quyết định có kích thước tối thiểu cho cùng hàm đó.


---

##### Bài tập 18.18

Bài tập này liên quan đến khả năng biểu đạt của danh sách quyết định (Mục <a class="sectionRef" title="" href="#">learning-theory-section</a>).<br>

1.  Chứng minh rằng danh sách quyết định có thể biểu diễn bất kỳ hàm Boolean nào, nếu kích thước của các kiểm tra không bị giới hạn.<br>

2.  Chứng minh rằng nếu các kiểm tra có thể chứa tối đa $k$ literal mỗi loại, thì danh sách quyết định có thể biểu diễn bất kỳ hàm nào có thể được biểu diễn bởi một cây quyết định có độ sâu $k$.


---

##### Bài tập 18.19

Giả sử một search $7$-nearest-neighbors regression trả về $ \{7, 6, 8, 4, 7, 11, 100\} $ là 7 giá trị $y$ gần nhất cho một giá trị $x$ nhất định. Giá trị $\hat{y}$ nào tối thiểu hóa hàm mất mát $L_1$ trên dữ liệu này? Có một tên gọi phổ biến trong thống kê cho giá trị này như một hàm của các giá trị $y$; đó là gì? Trả lời hai câu hỏi tương tự cho hàm mất mát $L_2$.


---

##### Bài tập 18.20

Giả sử một search $7$-nearest-neighbors regression trả về $ \{4, 2, 8, 4, 9, 11, 100\} $ là 7 giá trị $y$ gần nhất cho một giá trị $x$ nhất định. Giá trị $\hat{y}$ nào tối thiểu hóa hàm mất mát $L_1$ trên dữ liệu này? Có một tên gọi phổ biến trong thống kê cho giá trị này như một hàm của các giá trị $y$; đó là gì? Trả lời hai câu hỏi tương tự cho hàm mất mát $L_2$.


---

##### Bài tập 18.21

Hình <a href="#">kernel-machine-figure</a> đã cho thấy làm thế nào một đường tròn tại gốc tọa độ có thể được phân tách tuyến tính bằng cách ánh xạ từ các đặc trưng $(x_1, x_2)$ sang hai chiều $(x_1^2, x_2^2)$. Nhưng nếu đường tròn không nằm tại gốc tọa độ thì sao? Nếu đó là một hình elip, không phải là một đường tròn thì sao? Phương trình tổng quát cho một đường tròn (và do đó là biên quyết định) là $(x_1-a)^2 + (x_2-b)^2 - r^2{{\,=\,}}0$, và phương trình tổng quát cho một hình elip là $c(x_1-a)^2 + d(x_2-b)^2 - 1 {{\,=\,}}0$.
<br>
1.  Khai triển phương trình cho đường tròn và cho thấy các trọng số $w_i$ sẽ là gì cho biên quyết định trong không gian đặc trưng bốn chiều $(x_1, x_2, x_1^2, x_2^2)$. Giải thích tại sao điều này có nghĩa là bất kỳ đường tròn nào cũng có thể được phân tách tuyến tính trong không gian này.<br>

2.  Thực hiện tương tự cho các hình elip trong không gian đặc trưng năm chiều $(x_1, x_2, x_1^2, x_2^2, x_1 x_2)$.


---

##### Bài tập 18.22

Xây dựng một support vector machine tính toán hàm xor. Sử dụng các giá trị +1 và –1 (thay vì 1 và 0) cho cả đầu vào và đầu ra, sao cho một ví dụ trông giống như $([-1, 1], 1)$ hoặc $([-1, -1], -1)$. Ánh xạ đầu vào $[x_1,x_2]$ vào một không gian bao gồm $x_1$ và $x_1\,x_2$. Vẽ bốn điểm đầu vào trong không gian này và đường phân tách biên độ tối đa. Biên độ là bao nhiêu? Sau đó, vẽ đường phân tách trở lại không gian đầu vào Euclidean ban đầu.


---

##### Bài tập 18.23

Xem xét một thuật toán học tập hợp sử dụng bỏ phiếu đa số đơn giản giữa $K$ giả thuyết đã học. Giả sử mỗi giả thuyết có sai số $\epsilon$ và các sai số được thực hiện bởi mỗi giả thuyết là độc lập với nhau. Tính toán công thức cho sai số của thuật toán học tập hợp theo $K$ và $\epsilon$, và đánh giá nó cho các trường hợp $K=5$, 10, và 20 và $\epsilon={0.1}$, 0.2, và 0.4. Nếu giả định độc lập bị loại bỏ, liệu sai số của tập hợp có thể tệ hơn $\epsilon$ không?


---

##### Bài tập 18.24

Tự tay xây dựng một mạng nơ-ron tính toán hàm xor của hai đầu vào. Đảm bảo chỉ định loại đơn vị bạn đang sử dụng.


---

##### Bài tập 18.25

Một perceptron đơn giản không thể biểu diễn xor (hoặc nói chung là hàm parity của các đầu vào của nó). Mô tả điều gì xảy ra với các trọng số của một perceptron có bốn đầu vào, ngưỡng cứng, bắt đầu với tất cả các trọng số được đặt thành 0.1, khi các ví dụ về hàm parity đến.


---

##### Bài tập 18.26

Nhớ lại từ Chương <a class="chapterRef" href="{{site.baseurl}}/concept-learning-exercises/">concept-learning-chapter</a> rằng có $2^{2^n}$ hàm Boolean riêng biệt của $n$ đầu vào. Có bao nhiêu trong số đó có thể được biểu diễn bởi một perceptron ngưỡng?


---

##### Bài tập 18.27

Xem xét tập hợp các ví dụ sau đây, mỗi ví dụ có sáu đầu vào và một đầu ra mục tiêu:<br>

$$
\begin{array} 
	{|r|r|}\hline \textbf{Ví dụ} & A_1 & A_2 & A_3 & A_4 & A_5 & A_6 & A_7 & A_8 & A_9 & A_{10} & A_{11} & A_{12} & A_{13} & A_{14} \\ 
	\hline 
	\textbf{x}_1  & 1 & 1  & 1  & 1 & 1 & 1 & 1  & 0  & 0 & 0 & 0 & 0  & 0  & 0 \\
	\textbf{x}_2  & 0 & 0  & 0  & 1 & 1 & 0 & 0  & 1  & 1 & 0 & 1 & 0  & 1  & 1 \\
	\textbf{x}_3  & 1 & 1  & 1  & 0 & 1 & 0 & 0  & 1  & 1 & 0 & 0 & 0  & 1  & 1 \\
	\textbf{x}_4  & 0 & 1  & 0  & 0 & 1 & 0 & 0  & 1  & 0 & 1 & 1 & 1  & 0  & 1 \\
	\textbf{x}_5  & 0 & 0  & 1  & 1 & 0 & 1 & 1  & 0  & 1 & 1 & 0 & 0  & 1  & 0 \\
	\textbf{x}_6  & 0 & 0  & 0  & 1 & 0 & 1 & 0  & 1  & 1 & 0 & 1 & 1  & 1  & 0 \\
	\textbf{T}   & 1 & 1  & 1  & 1 & 1 & 1 & 0  & 1  & 0 & 0 & 0 & 0  & 0  & 0 \\
	\hline  
\end{array}
$$



1.  Chạy quy tắc học perceptron trên dữ liệu này và hiển thị các trọng số cuối cùng.<br>

2.  Chạy quy tắc học cây quyết định và hiển thị cây quyết định kết quả.<br>

3.  Nhận xét về kết quả của bạn.<br>


---

##### Bài tập 18.28

Mục <a class="sectionRef" title="" href="#">logistic-regression-section</a> (trang <a class="pageRef" title="" href="#">logistic-regression-section</a>) đã lưu ý rằng đầu ra của hàm logistic có thể được diễn giải là một *xác suất* $p$ mà mô hình gán cho mệnh đề $f(\textbf{x}){{\,=\,}}1$; do đó, xác suất $f(\textbf{x}){{\,=\,}}0$ là $1-p$. Viết xác suất $p$ dưới dạng hàm của $\textbf{x}$ và tính đạo hàm của $\log p$ theo từng trọng số $w_i$. Lặp lại quy trình cho $\log (1-p)$. Các phép tính này cung cấp một quy tắc học để tối thiểu hóa hàm mất mát negative-log-likelihood cho một giả thuyết xác suất. Nhận xét về bất kỳ sự tương đồng nào với các quy tắc học khác trong chương.


---

##### Bài tập 18.29

Giả sử bạn có một mạng nơ-ron với các hàm kích hoạt tuyến tính. Nghĩa là, đối với mỗi đơn vị, đầu ra là một hằng số $c$ nhân với tổng trọng số của các đầu vào.<br>

1.  Giả sử mạng có một lớp ẩn. Với một phép gán trọng số $\textbf{w}$ nhất định, hãy viết các phương trình cho giá trị của các đơn vị trong lớp đầu ra dưới dạng hàm của $\textbf{w}$ và lớp đầu vào $\textbf{x}$, mà không đề cập rõ ràng đến đầu ra của lớp ẩn. Chứng minh rằng có một mạng không có đơn vị ẩn nào tính toán cùng một hàm.<br>

2.  Lặp lại phép tính trong phần (a), nhưng lần này thực hiện cho mạng có bất kỳ số lượng lớp ẩn nào.<br>

3.  Giả sử một mạng có một lớp ẩn và các hàm kích hoạt tuyến tính có $n$ nút đầu vào và đầu ra và $h$ nút ẩn. Phép biến đổi trong phần (a) sang một mạng không có lớp ẩn có tác động gì đến tổng số trọng số? Thảo luận đặc biệt về trường hợp $h \ll n$.


---

##### Bài tập 18.30

Triển khai một cấu trúc dữ liệu cho các mạng nơ-ron phân lớp, truyền thẳng, ghi nhớ cung cấp thông tin cần thiết cho cả đánh giá tiến và lan truyền ngược. Sử dụng cấu trúc dữ liệu này, viết một hàm NEURAL-NETWORK-OUTPUT nhận một ví dụ và một mạng và tính toán các giá trị đầu ra thích hợp.


---

##### Bài tập 18.31

Giả sử một tập huấn luyện chỉ chứa một ví dụ duy nhất, lặp lại 100 lần. Trong 80 trong số 100 trường hợp, giá trị đầu ra duy nhất là 1; trong 20 trường hợp còn lại, nó là 0. Mạng back-propagation sẽ dự đoán gì cho ví dụ này, giả sử nó đã được huấn luyện và đạt đến một điểm tối ưu toàn cục? (<i>Gợi ý:</i> để tìm điểm tối ưu toàn cục, hãy lấy đạo hàm của hàm lỗi và đặt nó bằng 0.)


---

##### Bài tập 18.32

Mạng nơ-ron có hiệu suất học tập được đo lường trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/restaurant-back-prop-figure.png">restaurant-back-prop-figure</a> có bốn nút ẩn. Số lượng này được chọn một cách tùy ý. Sử dụng phương pháp cross-validation để tìm số lượng nút ẩn tốt nhất.


---

##### Bài tập 18.33

Xem xét bài toán phân tách $N$ điểm dữ liệu thành các ví dụ tích cực và tiêu cực bằng một bộ phân tách tuyến tính. Rõ ràng, điều này luôn có thể thực hiện được đối với $N{{\,=\,}}2$ điểm trên một đường thẳng có chiều $d{{\,=\,}}1$, bất kể các điểm được gán nhãn như thế nào hoặc chúng nằm ở đâu (trừ khi các điểm ở cùng một vị trí).<br>

1.  Chứng minh rằng điều này luôn có thể thực hiện được đối với $N{{\,=\,}}3$ điểm trên một mặt phẳng có chiều $d{{\,=\,}}2$, trừ khi chúng thẳng hàng.<br>

2.  Chứng minh rằng điều này không phải lúc nào cũng có thể thực hiện được đối với $N{{\,=\,}}4$ điểm trên một mặt phẳng có chiều $d{{\,=\,}}2$.<br>

3.  Chứng minh rằng điều này luôn có thể thực hiện được đối với $N{{\,=\,}}4$ điểm trong một không gian có chiều $d{{\,=\,}}3$, trừ khi chúng đồng phẳng.<br>

4.  Chứng minh rằng điều này không phải lúc nào cũng có thể thực hiện được đối với $N{{\,=\,}}5$ điểm trong một không gian có chiều $d{{\,=\,}}3$.<br>

5.  Học sinh tham vọng có thể muốn chứng minh rằng $N$ điểm ở vị trí tổng quát (nhưng không phải $N+1$) có thể được phân tách tuyến tính trong một không gian có chiều $N-1$.<br>


---

<!-- tabs:end -->
