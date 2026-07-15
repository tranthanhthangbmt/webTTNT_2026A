# Chapter 24 Natural Language Processing

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_24_Natural%20Language%20Processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_24_Natural%20Language%20Processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Communication and Language

## Chapter 22

---
## Phác thảo

- Truyền thông

- Ngữ pháp

- Phân tích cú pháp

- Sự cố

---
## Giao tiếp

Chế độ xem "Cổ điển" (trước 1953):
  
   ngôn ngữ bao gồm các câu đúng/sai (cf. logic)

Quan điểm "Hiện đại" (sau 1953):
  
   ngôn ngữ là một hình thức hành động

Wittgenstein (1953) *Điều tra triết học*

Austin (1962) *Cách thực hiện mọi việc bằng từ ngữ*

Searle (1969) *Hành vi lời nói*

Tại sao?

---
## Giao tiếp

Chế độ xem "Cổ điển" (trước 1953):
  
   ngôn ngữ bao gồm các câu đúng/sai (cf. logic)

Quan điểm "Hiện đại" (sau 1953):
  
   ngôn ngữ là một hình thức hành động

Wittgenstein (1953) *Điều tra triết học*

Austin (1962) *Cách thực hiện mọi việc bằng từ ngữ*

Searle (1969) *Hành vi lời nói*

Tại sao? \hspace*{5.5in}in\raisebox{-1.5in[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/lamppost.png)}

---
## Giao tiếp

Chế độ xem "Cổ điển" (trước 1953):
  
   ngôn ngữ bao gồm các câu đúng/sai (cf. logic)

Quan điểm "Hiện đại" (sau 1953):
  
   ngôn ngữ là một hình thức hành động

Wittgenstein (1953) *Điều tra triết học*

Austin (1962) *Cách thực hiện mọi việc bằng từ ngữ*

Searle (1969) *Hành vi lời nói*

Tại sao? \hspace*{5.5in}in\raisebox{-1.5in[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/lamppost+dog.png)}

---
## Giao tiếp

Chế độ xem "Cổ điển" (trước 1953):
  
   ngôn ngữ bao gồm các câu đúng/sai (cf. logic)

Quan điểm "Hiện đại" (sau 1953):
  
   ngôn ngữ là một hình thức hành động

Wittgenstein (1953) *Điều tra triết học*

Austin (1962) *Cách thực hiện mọi việc bằng từ ngữ*

Searle (1969) *Hành vi lời nói*

Tại sao? \hspace*{5.5in}in\raisebox{-1.5in[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/lamppost+dog.png)}

* Để thay đổi hành động của các tác nhân khác*

---
## Hành động lời nói

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/utterance.png)

Hành vi lời nói đạt được mục đích của người nói:
  

| &nbsp; | &nbsp; |
|---|---|
| *Thông báo* | "Có một cái hố trước mặt bạn" |
| *Query* | "Bạn có thấy vàng không?" |
| *Lệnh* | "Nhặt nó lên" |
| *Hứa* | "Tôi sẽ chia vàng với bạn" |
| *Xác nhận* | "OK" |

Lập kế hoạch hành động lời nói đòi hỏi kiến thức về 
  
-- Tình huống 
  
-- Quy ước ngữ nghĩa và cú pháp 
  
-- Mục tiêu, nền tảng kiến thức và tính hợp lý của người nghe

---
## Các giai đoạn trong giao tiếp (thông tin)

| &nbsp; | &nbsp; |
|---|---|
| *Intention* | S muốn thông báo cho H rằng \mat{$P$} |
| *Thế hệ* | S chọn từ \mat{$W$} để diễn đạt \mat{$P$} trong ngữ cảnh \mat{$C$} |
| *Tổng hợp* | S thốt ra từ \mat{$W$} |
|  |  |
| *Nhận thức* | H nhận thức \mat{$W'$} trong ngữ cảnh \mat{$C'$} |
| *Phân tích* | H suy ra những ý nghĩa có thể có \mat{$P_1,\ldots P_n$} |
| *Định hướng* | H suy ra ý nghĩa dự định \mat{$P_i$} |
| * Hợp nhất * | H hợp nhất \mat{$P_i$} vào KB |

Làm thế nào điều này có thể đi sai?  

---
## Các giai đoạn trong giao tiếp (thông tin)

| &nbsp; | &nbsp; |
|---|---|
| *Intention* | S muốn thông báo cho H rằng \mat{$P$} |
| *Thế hệ* | S chọn từ \mat{$W$} để diễn đạt \mat{$P$} trong ngữ cảnh \mat{$C$} |
| *Tổng hợp* | S thốt ra từ \mat{$W$} |
|  |  |
| *Nhận thức* | H nhận thức \mat{$W'$} trong ngữ cảnh \mat{$C'$} |
| *Phân tích* | H suy ra những ý nghĩa có thể có \mat{$P_1,\ldots P_n$} |
| *Định hướng* | H suy ra ý nghĩa dự định \mat{$P_i$} |
| * Hợp nhất * | H hợp nhất \mat{$P_i$} vào KB |

Làm thế nào điều này có thể đi sai?  
  
-- Không thành thật (S không tin \mat{$P$})
  
-- Lỗi đánh lửa do lời nói 
  
-- Lời nói mơ hồ 
  
-- Sự hiểu biết khác nhau về bối cảnh hiện tại (\mat{$C\neq C'$})
  

---
## Ngữ pháp

Khỉ vervet, linh dương, v.v. sử dụng các ký hiệu riêng biệt cho câu
  
\mat{$\implies$} tập hợp các mệnh đề có thể truyền đạt bị hạn chế, không có \defn{khả năng sinh sản}

(Chomsky (1957): *Cấu trúc cú pháp*)

\defn{Ngữ pháp} chỉ định cấu trúc thành phần của các thông báo phức tạp
  
ví dụ: lời nói (tuyến tính), văn bản (tuyến tính), âm nhạc (hai chiều)

Một \defn{ngôn ngữ hình thức} là một tập hợp các \defn{chuỗi} của \defn{ký hiệu đầu cuối}

Mỗi chuỗi trong ngôn ngữ có thể được phân tích/tạo ra bởi ngữ pháp

Ngữ pháp là một tập hợp các quy tắc viết lại \defn{}, ví dụ:
\begin{formula}
 \bnf{S} \bnfeq \bnf{NP} \bl \bnf{VP} 

 \bnf{Bài viết} \bnfeq \bnft{the \bnfor a \bnfor an} \bnfor \ldots
\end{formula}
Ở đây \mat{$\bnf{S}$} là ký hiệu \defn{câu}, \mat{$\bnf{NP}$} và \mat{$\bnf{VP}$} là \defn{nonterminals}

---
## Các loại ngữ pháp

\defn{Thông thường}: \mat{$\bnf{nonterminal} \bnfeq \bnft{terminal} [\bnf{nonterminal}]$}
\begin{formula}
  \bnf{S} \bnfeq \bnft{a}\bnf{S

  \bnf{S} \bnfeq \Lambda
\end{formula}

\defn{Không có ngữ cảnh}: \mat{$\bnf{nonterminal} \bnfeq \bnf{anything} $}
\begin{formula}
  \bnf{S} \bnfeq \bnft{a}\bnf{S}\bnft{b}
\end{formula}

\defn{ Phân biệt ngữ cảnh }: nhiều điểm không kết thúc hơn ở phía bên tay phải
\begin{formula}
  \bnf{A} \bnf{S} \bnf{B} \bnfeq \bnf{A} \bnf{A} \bnft{a} \bnf{B}\bnf{B}
\end{formula}

\defn{Đếm đệ quy}: không có ràng buộc

Liên quan đến hệ thống Post và hệ thống Kleene về quy tắc viết lại

Ngôn ngữ tự nhiên có thể không có ngữ cảnh, có thể phân tích cú pháp trong thời gian thực!

---
## Từ điển Wumpus

\begin{eqnarray*}
\bnf{Noun} & \bnfeq & \bnft{stench \bnfor breeze \bnfor glitter \bnfor nothing} 

        & &\bnfor \bnft{wumpus \bnfor pit \bnfor pits\bnfor gold \bnfor east} \bnfor \ldots 

\bnf{Verb} & \bnfeq & \bnft{is \bnfor see \bnfor smell \bnfor shoot \bnfor feel \bnfor stinks}

        & &\bnfor \bnft{go \bnfor grab \bnfor carry \bnfor kill \bnfor turn} \bnfor \ldots 

\bnf{Adjective} & \bnfeq & \bnft{right \bnfor left \bnfor east \bnfor south \bnfor back \bnfor smelly} \bnfor \ldots 

\bnf{Adverb} & \bnfeq & \bnft{here \bnfor there \bnfor nearby \bnfor ahead} 

        &&\bnfor \bnft{right \bnfor left \bnfor east \bnfor south \bnfor back} \bnfor \ldots 

\bnf{Pronoun} & \bnfeq & \bnft{me \bnfor you \bnfor I \bnfor it} \bnfor \ldots 

\bnf{Name} & \bnfeq & \bnft{John} \bnfor \bnft{Mary} \bnfor \bnft{Boston}
	\bnfor \bnft{UCB} \bnfor \bnft{PAJC} \bnfor \ldots 

\bnf{Article} & \bnfeq & \bnft{the \bnfor a \bnfor an} \bnfor \ldots 

\bnf{Preposition} & \bnfeq & \bnft{to \bnfor in \bnfor on \bnfor near} \bnfor \ldots 

\bnf{Conjunction} & \bnfeq & \bnft{and \bnfor or \bnfor but} \bnfor \ldots 

\bnf{Digit} & \bnfeq & \bnft{0\bnfor 1\bnfor 2\bnfor 3\bnfor 4\bnfor 5\bnfor 6\bnfor 7\bnfor 8\bnfor 9}
\end{eqnarray*}
Được chia thành các lớp \defn{đóng} và \defn{mở}

---
## Từ điển Wumpus

\begin{eqnarray*}
\bnf{Noun} & \bnfeq & \bnft{stench \bnfor breeze \bnfor glitter \bnfor nothing} 

        & &\bnfor \bnft{wumpus \bnfor pit \bnfor pits\bnfor gold \bnfor east} \bnfor \ldots 

\bnf{Verb} & \bnfeq & \bnft{is \bnfor see \bnfor smell \bnfor shoot \bnfor feel \bnfor stinks}

        & &\bnfor \bnft{go \bnfor grab \bnfor carry \bnfor kill \bnfor turn} \bnfor \ldots 

\bnf{Adjective} & \bnfeq & \bnft{right \bnfor left \bnfor east \bnfor south \bnfor back \bnfor smelly} \bnfor \ldots 

\bnf{Adverb} & \bnfeq & \bnft{here \bnfor there \bnfor nearby \bnfor ahead} 

        &&\bnfor \bnft{right \bnfor left \bnfor east \bnfor south \bnfor back} \bnfor \ldots 

\bnf{Pronoun} & \bnfeq & \bnft{me \bnfor you \bnfor I \bnfor it \bnfor \mat{S/HE} \bnfor \mat{Y'ALL}} \ldots 

\bnf{Name} & \bnfeq & \bnft{John} \bnfor \bnft{Mary} \bnfor \bnft{Boston}
	\bnfor \bnft{UCB} \bnfor \bnft{PAJC} \bnfor \ldots 

\bnf{Article} & \bnfeq & \bnft{the \bnfor a \bnfor an} \bnfor \ldots 

\bnf{Preposition} & \bnfeq & \bnft{to \bnfor in \bnfor on \bnfor near} \bnfor \ldots 

\bnf{Conjunction} & \bnfeq & \bnft{and \bnfor or \bnfor but} \bnfor \ldots 

\bnf{Digit} & \bnfeq & \bnft{0\bnfor 1\bnfor 2\bnfor 3\bnfor 4\bnfor 5\bnfor 6\bnfor 7\bnfor 8\bnfor 9}
\end{eqnarray*}
Được chia thành các lớp \defn{đóng} và \defn{mở}

---
## Ngữ pháp Wumpus

\[ \begin{array}{rclcl}
\bnf{S} &\bnfeq& \bnf{NP}  \bl \bnf{VP}             && \mbox{I + feel a breeze }
  
        & \bnfor & \bnf{S} \bl \bnf{Conjunction} \bl \bnf{S} && \mbox{I feel a
breeze + and + I smell a wumpus}
[0.2in]
\bnf{NP} &\bnfeq& \bnf{Pronoun}                 && \mbox{I }

        & \bnfor & \bnf{Noun}                   && \mbox{pits }

        & \bnfor & \bnf{Article} \bl  \bnf{Noun}    && \mbox{the + wumpus }

	& \bnfor & \bnf{Digit}\bl  \bnf{Digit}	&& \mbox{3 4} 

        & \bnfor & \bnf{NP} \bl  \bnf{PP}     && \mbox{the wumpus + to the east}

	& \bnfor & \bnf{NP} \bl \bnf{RelClause} && \mbox{the wumpus + that is smelly} 
[0.2in]
\bnf{VP} & \bnfeq & \bnf{Verb}                   && \mbox{stinks}

        & \bnfor & \bnf{VP} \bl  \bnf{NP}            && \mbox{feel + a breeze}

        & \bnfor & \bnf{VP} \bl  \bnf{Adjective}     && \mbox{is + smelly}

        & \bnfor & \bnf{VP} \bl  \bnf{PP}            && \mbox{turn + to the east}

        & \bnfor & \bnf{VP} \bl  \bnf{Adverb}        && \mbox{go + ahead}
[0.2in]
\bnf{PP} & \bnfeq & \bnf{Preposition}  \bl \bnf{NP}  && \mbox{to + the east}

\rule[-9pt]{0pt}{10pt}\bnf{RelClause} & \bnfeq & \bnft{that} \bl \bnf{VP} &&\mbox{that + is smelly}

\end{array}\]

---
## Đánh giá về mặt ngữ pháp

Ngôn ngữ hình thức \mat{$L_1$} có thể khác với ngôn ngữ tự nhiên \mat{$L_2$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/language-learning.png)

Điều chỉnh \mat{$L_1$} để đồng ý với \mat{$L_2$} là một vấn đề cần học hỏi!

| &nbsp; | &nbsp; |
|---|---|
| \ * | vàng lấy wumpus |
| \ * | Tôi ngửi thấy mùi vàng |
|  | Tôi tặng vàng cho con wumpus |
| \ * | Tôi tặng vàng cho wumpus |

Thỏa thuận liên chủ thể có phần đáng tin cậy, độc lập với ngữ nghĩa!

Ngữ pháp thực sự 10--500 trang, không đủ ngay cả đối với tiếng Anh " chuẩn "

---
## Cây phân tích cú pháp

Trình bày cấu trúc ngữ pháp của câu

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/parse-tree1.png)

---
## Cây phân tích cú pháp

Trình bày cấu trúc ngữ pháp của câu

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/parse-tree2.png)

---
## Cây phân tích cú pháp

Trình bày cấu trúc ngữ pháp của câu

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/parse-tree3.png)

---
## Cây phân tích cú pháp

Trình bày cấu trúc ngữ pháp của câu

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/parse-tree4.png)

---
## Cây phân tích cú pháp

Trình bày cấu trúc ngữ pháp của câu

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/parse-tree5.png)

---
## Cú pháp trong NLP

Hầu hết đều xem cấu trúc cú pháp là một bước thiết yếu hướng tới ý nghĩa;
  
"Mary đánh John" $\neq$ "John đánh Mary"

“Và vì tôi đã không được thông báo—thực tế là vì tôi đã không
biết rằng có số tiền dư thừa cho đến khi chúng tôi, chính chúng tôi, trong cuộc kiểm tra đó
sau khi toàn bộ sự việc nổ tung, và đó là, nếu bạn còn nhớ, đó là
là sự việc mà bộ trưởng tư pháp đã đến gặp tôi và nói với tôi
rằng anh ấy đã nhìn thấy một bản ghi nhớ cho biết rằng không còn gì nữa
quỹ.”

---
## Cú pháp trong NLP

Hầu hết đều xem cấu trúc cú pháp là một bước thiết yếu hướng tới ý nghĩa;
  
"Mary đánh John" $\neq$ "John đánh Mary"

“Và vì tôi đã không được thông báo—thực tế là vì tôi đã không
biết rằng có số tiền dư thừa cho đến khi chúng tôi, chính chúng tôi, trong cuộc kiểm tra đó
sau khi toàn bộ sự việc nổ tung, và đó là, nếu bạn còn nhớ, đó là
là sự việc mà bộ trưởng tư pháp đã đến gặp tôi và nói với tôi
rằng anh ấy đã nhìn thấy một bản ghi nhớ cho biết rằng không còn gì nữa
quỹ.”

" Chẳng phải câu 'Tôi muốn đặt một dấu gạch nối giữa các từ Cá
và And và And và Chips trong ký hiệu Fish-And-Chips của tôi' đã rõ ràng hơn
nếu dấu ngoặc kép được đặt trước Cá và giữa Cá và
và, và và và Và và và và và và và và Và và Và và
và, và và Chips, cũng như sau Chips?"

---
## Phân tích cú pháp không ngữ cảnh

Phân tích cú pháp từ dưới lên hoạt động bằng cách thay thế bất kỳ chuỗi con nào khớp với

RHS của một quy tắc với LHS của quy tắc

Các thuật toán hiệu quả (ví dụ: phân tích biểu đồ, Phần 22.3) \mat{$O(n^3)$} cho việc phân tích cú pháp không ngữ cảnh,
chạy với tốc độ vài nghìn từ/giây đối với ngữ pháp thực sự

Phân tích cú pháp không ngữ cảnh \mat{$\equiv$} Phép nhân ma trận Boolean (Lee, 2002)
    
\mat{$\implies$} khó có thể tìm thấy các thuật toán thực tế nhanh hơn 

---
## Ngữ pháp logic

Ký hiệu BNF cho ngữ pháp quá hạn chế:
  
-- khó thêm "điều kiện phụ" (thỏa thuận số, v.v.)
  
-- khó kết nối cú pháp với ngữ nghĩa

Ý tưởng: diễn đạt các quy tắc ngữ pháp dưới dạng logic
\[\begin{array}{lcl}
\bnf{X}\bnfeq\bnf{Y}\bnf{Z}        &\mbox{becomes} & \mat{Y(s_1) \land Z(s_2) \implies X(Append(s_1,s_2))} 

\bnf{X}\bnfeq\bnft{word}           &\mbox{becomes} & \mat{X([\mbox{"}\bnft{word}\mbox{"}])} 

\bnf{X}\bnfeq\bnf{Y}\bnfor \bnf{Z} &\mbox{becomes} & \mat{Y(s) \implies X(s) &nbsp;&nbsp;  Z(s) \implies X(s)}
\end{array}\]
Ở đây, \mat{$X(s)$} có nghĩa là chuỗi \mat{$s$} * có thể được hiểu là * là \mat{$X$}

---
## Tiếp theo ngữ pháp logic 

Bây giờ thật dễ dàng để tăng cường các quy tắc
\mat{\begin{eqnarray*}
NP(s_1) &\land &EatsBreakfast(Ref(s_1)) \land VP(s_2) 

        &&      \implies NP(Append(s_1,[\mbox{"}\bnft{who}\mbox{"}],s_2))

        && 

NP(s_1) &\land &Number(s_1,n) \land VP(s_2) \land Number(s_2,n) 

        &&      \implies S(Append(s_1,s_2))
\end{eqnarray*}}
Phân tích cú pháp được giảm xuống thành suy luận logic:
  
  **Hỏi**(\mat{$KB$}, \mat{$S([\mbox{"}\bnft{I}\mbox{" "}\bnft{am}\mbox{" "}\bnft{a}\mbox{" "}\bnft{wumpus}\mbox{"}])$})

(Có thể thêm đối số phụ để trả về cấu trúc phân tích cú pháp, ngữ nghĩa)

Việc tạo chỉ cần một truy vấn với các biến chưa được xác định:
  
  **Hỏi**(\mat{$KB$}, \mat{$S(x)$})

Nếu chúng ta thêm các đối số vào các ký hiệu không kết thúc để xây dựng ngữ nghĩa của câu,
Việc tạo NLP có thể được thực hiện từ một câu logic nhất định:
  
  **Hỏi**(\mat{$KB$}, \mat{$S(x,At(Robot,[1,1])$})

---
## Ngôn ngữ thực

Ngôn ngữ thực sự của con người cung cấp nhiều vấn đề cho NLP:

- \defn{mơ hồ}

- \defn{anaphora}

- \defn{tính chỉ số}

- \defn{sự mơ hồ}

- \defn{cấu trúc bài giảng}

- \defn{ẩn dụ}

- \defn{ẩn dụ}

- \defn{tính không thành phần}

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

| &nbsp; |
|---|
| Tôi đã ăn spaghetti với thịt viên |

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

| &nbsp; |
|---|
| Tôi đã ăn spaghetti với thịt viên |
|  | salad |

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

| &nbsp; |
|---|
| Tôi đã ăn spaghetti với thịt viên |
|  | xà lách |
|  | từ bỏ |

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

| &nbsp; |
|---|
| Tôi đã ăn spaghetti với thịt viên |
|  | xà lách |
|  | từ bỏ |
|  | một cái nĩa |

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

| &nbsp; |
|---|
| Tôi đã ăn spaghetti với thịt viên |
|  | xà lách |
|  | từ bỏ |
|  | một cái nĩa |
|  | một người bạn |

---
## Sự mơ hồ

Biệt đội giúp đỡ nạn nhân bị chó cắn 

Máy bay trực thăng chạy bằng ruồi người

Người Mỹ đẩy chai lên người Đức

| &nbsp; |
|---|
| Tôi đã ăn spaghetti với thịt viên |
|  | xà lách |
|  | từ bỏ |
|  | một cái nĩa |
|  | một người bạn |

Sự mơ hồ có thể là từ vựng (đa nghĩa), cú pháp, ngữ nghĩa, tham chiếu

---
## Anaphora

Sử dụng đại từ để chỉ lại các thực thể đã được giới thiệu trong văn bản

Sau khi Mary cầu hôn John, *họ* đã tìm được một nhà truyền giáo và kết hôn.

---
## Anaphora

Sử dụng đại từ để chỉ lại các thực thể đã được giới thiệu trong văn bản

Sau khi Mary cầu hôn John, *họ* đã tìm được một nhà truyền giáo và kết hôn.

Trong tuần trăng mật, *họ* đi Hawaii

---
## Anaphora

Sử dụng đại từ để chỉ lại các thực thể đã được giới thiệu trong văn bản

Sau khi Mary cầu hôn John, *họ* đã tìm được một nhà truyền giáo và kết hôn.

Trong tuần trăng mật, *họ* đi Hawaii

Mary nhìn thấy một chiếc nhẫn qua cửa sổ và hỏi John *it*

---
## Anaphora

Sử dụng đại từ để chỉ lại các thực thể đã được giới thiệu trong văn bản

Sau khi Mary cầu hôn John, *họ* đã tìm được một nhà truyền giáo và kết hôn.

Trong tuần trăng mật, *họ* đi Hawaii

Mary nhìn thấy một chiếc nhẫn qua cửa sổ và hỏi John *it*

Mary ném một hòn đá vào cửa sổ và làm vỡ *it*

---
## Tính chỉ mục

Câu mệnh đề đề cập đến tình huống phát ngôn (địa điểm, thời gian, S/H, v.v.)

*I* *am* qua *đây*

Tại sao *bạn* lại làm *điều đó*?

---
## Ẩn dụ

Dùng một cụm danh từ để thay thế cho một cụm danh từ khác

Tôi đã đọc *Shakespeare*

*Chrysler* công bố lợi nhuận kỷ lục

Chiếc bánh sandwich giăm bông \emph{} ở Bảng 4 muốn một cốc bia khác

---
## Ẩn dụ

Cách sử dụng từ và cụm từ “không theo nghĩa đen”, thường có tính hệ thống:

Tôi đã thử giết quá trình nhưng nó không chết. Cha mẹ của nó giữ cho nó sống.

---
## Tính không thành phần

giày bóng rổ

---
## Tính không thành phần

giày bóng rổ

giày em bé

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

mặt trăng nhỏ

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

trăng nhỏ

phân tử lớn

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

trăng nhỏ

phân tử lớn 

đứa trẻ đơn thuần

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

trăng nhỏ

phân tử lớn 

đứa trẻ đơn thuần

bị cáo buộc sát nhân

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

trăng nhỏ

phân tử lớn 

đứa trẻ đơn thuần

bị cáo buộc là kẻ sát nhân

da thật

---
## Tính không thành phần

giày bóng rổ

giày em bé

giày cá sấu 

giày thiết kế 

giày phanh

sổ đỏ

bút đỏ

tóc đỏ

cá trích đỏ

trăng nhỏ

phân tử lớn 

đứa trẻ đơn thuần

bị cáo buộc là kẻ sát nhân

da thật

cỏ nhân tạo



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Nlp](codeAndExercises/aima-python-master/notebooks/nlp.ipynb)
- [Nlp (Python File)](codeAndExercises/aima-python-master/notebooks/nlp.py)
- [Nlp Apps](codeAndExercises/aima-python-master/notebooks/nlp_apps.ipynb)
- [Nlp Apps (Python File)](codeAndExercises/aima-python-master/notebooks/nlp_apps.py)
- [Text](codeAndExercises/aima-python-master/notebooks/text.ipynb)
- [Text (Python File)](codeAndExercises/aima-python-master/notebooks/text.py)


#### **Bài tập**

##### Bài tập 24.1

In the shadow of a tree with a dense, leafy canopy, one sees a number of
light spots. Surprisingly, they all appear to be circular. Why? After
all, the gaps between the leaves through which the sun shines are not
likely to be circular.


---

##### Bài tập 24.2

Consider a picture of a white sphere floating in front of a black
backdrop. The image curve separating white pixels from black pixels is
sometimes called the “outline” of the sphere. Show that the outline of a
sphere, viewed in a perspective camera, can be an ellipse. Why do
spheres not look like ellipses to you?


---

##### Bài tập 24.3

Consider an infinitely long cylinder of radius $r$ oriented with its
axis along the $y$-axis. The cylinder has a Lambertian surface and is
viewed by a camera along the positive $z$-axis. What will you expect to
see in the image if the cylinder is illuminated by a point source at
infinity located on the positive $x$-axis? Draw the contours of constant
brightness in the projected image. Are the contours of equal brightness
uniformly spaced?


---

##### Bài tập 24.4

Edges in an image can correspond to a variety of events in a scene.
Consider Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/illuminationfigure.png">illuminationfigure</a>
(page <a class="pageRef" title="" href="#">illuminationfigure</a>, and assume that it is a picture of a real
three-dimensional scene. Identify ten different brightness edges in the
image, and for each, state whether it corresponds to a discontinuity in
(a) depth, (b) surface orientation, (c) reflectance, or (d)
illumination.


---

##### Bài tập 24.5

A stereoscopic system is being contemplated for terrain mapping. It will
consist of two CCD cameras, each having ${512}\times {512}$ pixels on a
10 cm $\times$ 10 cm square sensor. The lenses to be used have a focal
length of 16 cm, with the focus fixed at infinity. For corresponding
points ($u_1,v_1$) in the left image and ($u_2,v_2$) in the right image,
$v_1=v_2$ because the $x$-axes in the two image planes are parallel to
the epipolar lines—the lines from the object to the camera. The optical
axes of the two cameras are parallel. The baseline between the cameras
is 1 meter.<br>

1.  If the nearest distance to be measured is 16 meters, what is the
    largest disparity that will occur (in pixels)?<br>

2.  What is the distance resolution at 16 meters, due to the pixel
    spacing?<br>

3.  What distance corresponds to a disparity of one pixel?<br>


---

##### Bài tập 24.6

Which of the following are true, and which are false?<br>

1.  Finding corresponding points in stereo images is the easiest phase
    of the stereo depth-finding process.<br>

2.  Shape-from-texture can be done by projecting a grid of light-stripes
    onto the scene.<br>

3.  Lines with equal lengths in the scene always project to equal
    lengths in the image.<br>

4.  Straight lines in the image necessarily correspond to straight lines
    in the scene.


---

##### Bài tập 24.7

Which of the following are true, and which are false?<br>

1.  Finding corresponding points in stereo images is the easiest phase
    of the stereo depth-finding process.<br>

2.  In stereo views of the same scene, greater accuracy is obtained in
    the depth calculations if the two camera positions are
    farther apart.<br>

3.  Lines with equal lengths in the scene always project to equal
    lengths in the image.<br>

4.  Straight lines in the image necessarily correspond to straight lines
    in the scene.<br>



    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/bottle-stereo.svg" alt="bottle-figure" id="bottle-figure" style="width:100%">
      <figcaption><center><b>Top view of
      a two-camera vision system observing a bottle with a wall behind it.</b></center></figcaption>
    </figure>


---

##### Bài tập 24.8

(Courtesy of Pietro Perona.) Figure <a class="insideExercisesFigRef"  href="#bottle-figure">bottle-figure</a> shows
two cameras at X and Y observing a scene. Draw the image seen at each
camera, assuming that all named points are in the same horizontal plane.
What can be concluded from these two images about the relative distances
of points A, B, C, D, and E from the camera baseline, and on what basis?


---


<!-- tabs:end -->
