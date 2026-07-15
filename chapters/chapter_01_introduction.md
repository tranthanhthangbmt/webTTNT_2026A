# Chapter 01 Introduction

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_01/chapter_01_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_01_Introduction.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Artificial Intelligence

## Chapter 1

---
## Phác thảo

- AI là gì?

- Sơ lược lịch sử

- Hiện đại

---
## AI là gì?

 

| &nbsp; | &nbsp; |
|---|---|
| {\bf Systems that think like humans} | {\bf Systems that think rationally} |
| {\bf Systems that act like humans} | {\bf Systems that act rationally} |

 

---
## Hành động con người: Bài kiểm tra Turing

Turing (1950) " Máy tính và trí thông minh ":

- "\txm{Máy móc có thể suy nghĩ}?" $\longrightarrow$ "\txg{Máy móc có thể hoạt động thông minh}?"

- Bài kiểm tra vận hành hành vi thông minh: \defn{Trò chơi bắt chước}

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/turing.png)

- Dự đoán rằng đến năm 2000, một chiếc máy có thể có 30\% khả năng 
  
     lừa gạt một người cư sĩ trong 5 phút

- Dự đoán tất cả các lập luận chính chống lại AI trong 50 năm tới

- Các thành phần chính được đề xuất của AI: kiến thức, lý luận, ngôn ngữ
  
     hiểu biết, học tập
[0,1in]
Sự cố: Kiểm tra Turing không thể tái tạo \emph{}, *mang tính xây dựng* hoặc 

tuân theo *phân tích toán học*

---
## Tư duy con người: Khoa học nhận thức
	

Những năm 1960 "\defn{cuộc cách mạng nhận thức}": tâm lý xử lý thông tin thay thế

tính chính thống thịnh hành của \defn{chủ nghĩa hành vi}

Đòi hỏi những lý thuyết khoa học về hoạt động bên trong của não bộ
  
 -- Mức độ trừu tượng nào? "\note{Kiến thức}" hoặc "\note{mạch}"?
  
 -- Làm thế nào để xác nhận? Yêu cầu 
    
    1) Dự đoán và kiểm tra hành vi của đối tượng con người (từ trên xuống)
    
    hoặc 2) Nhận dạng trực tiếp từ dữ liệu thần kinh (từ dưới lên)

Cả hai cách tiếp cận (đại khái là \txm{Khoa học nhận thức} và \txb{Khoa học thần kinh nhận thức}) 

bây giờ đã khác biệt với AI

Cả hai đều có chung đặc điểm sau với AI:
  
   *các lý thuyết hiện có không giải thích được (hoặc tạo ra)
  
   bất cứ thứ gì giống với trí thông minh chung ở cấp độ con người *

Do đó, cả ba lĩnh vực đều có chung một hướng chính!

---
## Suy nghĩ hợp lý: Quy luật tư duy

\defn{Quy chuẩn} (hoặc \defn{quy định}) thay vì \note{mô tả}

Aristotle: lập luận/quá trình suy nghĩ đúng đắn là gì?

Một số trường học ở Hy Lạp đã phát triển nhiều dạng \defn{logic}:
  
   *ký hiệu* và *quy tắc đạo hàm* cho suy nghĩ;

có thể đã hoặc chưa tiến tới ý tưởng cơ giới hóa

Đường truyền trực tiếp từ toán học và triết học tới AI hiện đại

Sự cố: 

1) Không phải tất cả hành vi thông minh đều được trung gian bởi sự cân nhắc logic

2) \note{Mục đích của việc suy nghĩ} là gì? Tôi nên có những suy nghĩ gì \emph{} 
  
   trong số tất cả những suy nghĩ (hợp lý hay nói cách khác) mà tôi *có thể có*?

---
## Hành động hợp lý

\defn{Hành vi hợp lý}: làm điều đúng đắn

Điều đúng: điều được mong đợi sẽ tối đa hóa thành tích mục tiêu,

dựa trên thông tin có sẵn

Không nhất thiết liên quan đến việc suy nghĩ---ví dụ: phản xạ chớp mắt---nhưng

suy nghĩ nên phục vụ cho hành động hợp lý

Aristotle (Đạo đức học Nicomachean):
  
  *Mọi nghệ thuật và mọi yêu cầu, và tương tự như vậy mọi 
  
       hành động và theo đuổi, được cho là nhằm mục đích tốt đẹp nào đó*

---
## Các tác nhân hợp lý

Một tác nhân \defn{} là một thực thể nhận thức và hành động

Khóa học này nói về thiết kế \defn{các tác nhân hợp lý}

Tóm lại, một tác nhân là một chức năng từ lịch sử nhận thức đến hành động:
\[f: {\cal P}^* \rightarrow {\cal A}\]
Đối với bất kỳ loại môi trường và nhiệm vụ nhất định nào, chúng tôi tìm kiếm 

tác nhân (hoặc lớp tác nhân) có hiệu suất tốt nhất

Hãy cẩn thận: *các hạn chế về tính toán khiến 
    
\ \ tính hợp lý hoàn hảo không thể đạt được*

$\rightarrow$ thiết kế chương trình \note{tốt nhất} cho các tài nguyên máy nhất định

---
## Thời tiền sử AI

| &nbsp; | &nbsp; |
|---|---|
| \defn{Triết học} | logic, phương pháp suy luận |
|  | tâm trí như hệ thống vật chất |
|  | nền tảng học tập, ngôn ngữ, tính hợp lý |
| \defn{Toán học} | biểu diễn và chứng minh hình thức |
|  | thuật toán, tính toán, khả năng quyết định (không), khả năng xử lý (trong) |
|  | xác suất |
| \defn{Tâm lý học} | thích ứng |
|  | hiện tượng nhận thức và điều khiển vận động |
|  | kỹ thuật thử nghiệm (tâm lý học, v.v.) |
| \defn{Kinh tế học} | lý thuyết hình thức về các quyết định hợp lý |
| \defn{Ngôn ngữ học} | biểu diễn tri thức |
|  | ngữ pháp |
| \defn{Khoa học thần kinh} | chất dẻo vật lý cho hoạt động trí óc |
| \defn{Lý thuyết điều khiển} | hệ thống cân bằng nội môi, độ ổn định |
|  | thiết kế đại lý tối ưu đơn giản |

---
## Lịch sử chậu cây AI

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| \note{1943} | McCulloch \ | Pitts: Mô hình mạch Boolean của não |
| \note{1950} | "Máy tính và trí thông minh" của Turing |
| \note{1952--69} | Nhìn này, Mẹ, không có tay! |
| \note{Những năm 1950} | Các chương trình AI thời kỳ đầu, bao gồm chương trình cờ đam của Samuel, |
|  | Newell \ | Nhà lý thuyết logic của Simon, Công cụ hình học của Gelernter |
| \note{1956} | Cuộc họp ở Dartmouth: "Trí tuệ nhân tạo" được thông qua |
| \note{1965} | Thuật toán hoàn chỉnh của Robinson cho suy luận logic |
| \note{1966--74} | AI phát hiện ra độ phức tạp tính toán |
|  | Nghiên cứu mạng lưới thần kinh gần như biến mất |
| \note{1969--79} | Phát triển ban đầu các hệ thống dựa trên tri thức |
| \note{1980--88} | Sự bùng nổ của ngành hệ thống chuyên gia |
| \note{1988--93} | Sự phá sản của ngành hệ thống chuyên gia: "AI Winter" |
| \note{1985--95} | Mạng lưới thần kinh trở lại phổ biến |
| \note{1988}-- | Sự trỗi dậy của xác suất; tăng chung về chiều sâu kỹ thuật |
|  | "Nouvelle AI": ALife, GA, điện toán mềm |
| \note{1995}-- | Đại lý, đại lý, khắp mọi nơi $\ldots$ |
| \note{2003}-- | AI cấp độ con người trở lại chương trình nghị sự |

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- {Chơi một ván bóng bàn tử tế} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- {Lái xe an toàn trên đường núi quanh co} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- {Lái xe an toàn dọc theo Đại lộ Telegraph} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- {Mua hàng tạp hóa trị giá một tuần trên web} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- {Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- {Chơi trò chơi cầu đàng hoàng} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- {Khám phá và chứng minh một định lý toán học mới} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- {Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- {Viết một câu chuyện có chủ đích hài hước} 

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- \txr{Viết truyện hài hước có chủ ý} 

- {Tư vấn pháp luật có thẩm quyền trong lĩnh vực pháp luật chuyên ngành}

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- \txr{Viết truyện hài hước có chủ ý} 

- \txg{Tư vấn pháp luật có thẩm quyền trong lĩnh vực luật chuyên ngành}

- {Dịch nói tiếng Anh sang tiếng Thụy Điển trong thời gian thực}

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- \txr{Viết truyện hài hước có chủ ý} 

- \txg{Tư vấn pháp luật có thẩm quyền trong lĩnh vực luật chuyên ngành}

- \txg{Dịch giọng nói tiếng Anh sang tiếng Thụy Điển nói trong thời gian thực}

- {Trò chuyện thành công với người khác trong một giờ}

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- \txr{Viết truyện hài hước có chủ ý} 

- \txg{Tư vấn pháp luật có thẩm quyền trong lĩnh vực luật chuyên ngành}

- \txg{Dịch giọng nói tiếng Anh sang tiếng Thụy Điển nói trong thời gian thực}

- \txr{Trò chuyện thành công với người khác trong một giờ}

- {Thực hiện một ca phẫu thuật phức tạp}

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- \txr{Viết truyện hài hước có chủ ý} 

- \txg{Tư vấn pháp luật có thẩm quyền trong lĩnh vực luật chuyên ngành}

- \txg{Dịch giọng nói tiếng Anh sang tiếng Thụy Điển nói trong thời gian thực}

- \txr{Trò chuyện thành công với người khác trong một giờ}

- \txm{Thực hiện một ca phẫu thuật phức tạp}

- {Dỡ bất kỳ máy rửa chén nào và cất mọi thứ đi}

---
## Hiện đại

Hiện tại, điều nào sau đây có thể được thực hiện?

- \txg{Chơi một ván bóng bàn tử tế} 

- \txg{Lái xe an toàn dọc theo con đường núi quanh co} 

- \txr{Lái xe an toàn dọc theo Đại lộ Telegraph} 

- \txg{Mua hàng tạp hóa trị giá một tuần trên web} 

- \txr{Mua hàng tạp hóa trị giá một tuần tại Berkeley Bowl} 

- \txg{Chơi bài bridge đàng hoàng} 

- \txm{Khám phá và chứng minh một định lý toán học mới} 

- \txm{Thiết kế và thực hiện chương trình nghiên cứu về sinh học phân tử}

- \txr{Viết truyện hài hước có chủ ý} 

- \txg{Tư vấn pháp luật có thẩm quyền trong lĩnh vực luật chuyên ngành}

- \txg{Dịch giọng nói tiếng Anh sang tiếng Thụy Điển nói trong thời gian thực}

- \txr{Trò chuyện thành công với người khác trong một giờ}

- \txm{Thực hiện một ca phẫu thuật phức tạp}

- \txr{Dỡ bất kỳ máy rửa bát nào ra và cất mọi thứ đi}

---
## Những câu chuyện vô tình hài hước

Một ngày nọ, Joe Bear đói. Anh ấy hỏi người bạn Irving Bird của mình xem một số
mật ong đã. Irving nói với anh rằng có một tổ ong trên cây sồi. Joe đe dọa
để đánh Irving nếu anh ta không nói cho anh ta biết mật ong ở đâu. Sự kết thúc.

Henry Squirrel khát nước. Anh bước tới bờ sông nơi anh
người bạn tốt Bill Bird đang ngồi. Henry trượt chân và ngã trong
sông. Trọng lực bị nhấn chìm. Sự kết thúc.

Ngày xửa ngày xưa có một con cáo gian dối và một con quạ kiêu ngạo. Một ngày nọ
con quạ đang ngồi trên cây, ngậm một miếng pho mát trong miệng. Anh ấy
nhận thấy rằng anh ta đang cầm miếng pho mát. Anh ấy trở nên đói và
nuốt miếng phô mai. Con cáo bước tới chỗ con quạ. Sự kết thúc.

---
## Những câu chuyện vô tình hài hước

Joe Bear đang đói. Anh ấy hỏi Irving Bird mật ong ở đâu. Irving
từ chối nói cho anh ta biết nên Joe đề nghị mang cho anh ta một con sâu nếu anh ta kể.
anh ta có một ít mật ong ở đâu.  Irving đồng ý. Nhưng Joe không biết ở đâu
có con sâu nào không, vì vậy anh ấy hỏi Irving, người từ chối nói. Thế là Joe đề nghị
mang cho anh ta một con sâu nếu anh ta nói cho anh ta biết con sâu ở đâu.  Irving
đồng ý. Nhưng Joe không biết sâu ở đâu nên anh ấy hỏi Irving,
người từ chối nói. Vì vậy Joe đề nghị mang cho anh ta một con sâu nếu anh ta nói
anh ta có một con sâu $\ldots$



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**

##### Bài tập 1.1

Define in your own words: (a) intelligence, (b) artificial intelligence,
(c) agent, (d) rationality, (e) logical reasoning.


---

##### Bài tập 1.2

Read Turing’s original paper on AI <a class="paperRef" title="" href="">Turing:1950 </a>.In the paper, he discusses several objections to his proposed enterprise and his test for
intelligence. Which objections still carry weight? Are his refutations
valid? Can you think of new objections arising from developments since
he wrote the paper? In the paper, he predicts that, by the year 2000, a
computer will have a 30% chance of passing a five-minute Turing Test
with an unskilled interrogator. What chance do you think a computer
would have today? In another 50 years?


---

##### Bài tập 1.3

Every year the Loebner Prize is awarded to the program that comes
closest to passing a version of the <a href="https://en.wikipedia.org/wiki/Turing_test">Turing Test</a>. Research and report on
the latest winner of the Loebner prize. What techniques does it use? How
does it advance the state of the art in AI?


---

##### Bài tập 1.4

Are reflex actions (such as flinching from a hot stove) rational? Are
they intelligent?


---

##### Bài tập 1.5

There are well-known classes of problems that are intractably difficult
for computers, and other classes that are provably undecidable. Does
this mean that AI is impossible?


---

##### Bài tập 1.6

Suppose we extend Evans’s <i>SYSTEM</i> program so that it can score 200 on a standard
IQ test. Would we then have a program more intelligent than a human?
Explain.


---

##### Bài tập 1.7

The neural structure of the sea slug <i>Aplysis</i> has been
widely studied (first by Nobel Laureate Eric Kandel) because it has only
about 20,000 neurons, most of them large and easily manipulated.
Assuming that the cycle time for an <i>Aplysis</i> neuron is
roughly the same as for a human neuron, how does the computational
power, in terms of memory updates per second, compare with the high-end
computer described in (Figure <a class ="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/computer-brain-table.png">computer-brain-table</a>)?


---

##### Bài tập 1.8

How could introspection—reporting on one’s inner thoughts—be inaccurate?
Could I be wrong about what I’m thinking? Discuss.


---

##### Bài tập 1.9

To what extent are the following computer systems instances of
artificial intelligence:<br>

-   Supermarket bar code scanners.<br>

-   Web search engines.<br>

-   Voice-activated telephone menus.<br>

-   Internet routing algorithms that respond dynamically to the state of
    the network.


---

##### Bài tập 1.10

To what extent are the following computer systems instances of
artificial intelligence:<br>

- Supermarket bar code scanners.<br>

- Voice-activated telephone menus.<br>

- Spelling and grammar correction features in Microsoft Word.<br>

- Internet routing algorithms that respond dynamically to the state of the network.<br>


---

##### Bài tập 1.11

Many of the computational models of cognitive activities that have been
proposed involve quite complex mathematical operations, such as
convolving an image with a Gaussian or finding a minimum of the entropy
function. Most humans (and certainly all animals) never learn this kind
of mathematics at all, almost no one learns it before college, and
almost no one can compute the convolution of a function with a Gaussian
in their head. What sense does it make to say that the “vision system”
is doing this kind of mathematics, whereas the actual person has no idea
how to do it?


---

##### Bài tập 1.12

Some authors have claimed that perception and motor skills are the most
important part of intelligence, and that “higher level” capacities are
necessarily parasitic—simple add-ons to these underlying facilities.
Certainly, most of evolution and a large part of the brain have been
devoted to perception and motor skills, whereas AI has found tasks such
as game playing and logical inference to be easier, in many ways, than
perceiving and acting in the real world. Do you think that AI’s
traditional focus on higher-level cognitive abilities is misplaced?


---

##### Bài tập 1.13

Why would evolution tend to result in systems that act rationally? What
goals are such systems designed to achieve?


---

##### Bài tập 1.14

Is AI a science, or is it engineering? Or neither or both? Explain.


---

##### Bài tập 1.15

“Surely computers cannot be intelligent—they can do only what their
programmers tell them.” Is the latter statement true, and does it imply
the former?


---

##### Bài tập 1.16

“Surely animals cannot be intelligent—they can do only what their genes
tell them.” Is the latter statement true, and does it imply the former?


---

##### Bài tập 1.17

“Surely animals, humans, and computers cannot be intelligent—they can do
only what their constituent atoms are told to do by the laws of
physics.” Is the latter statement true, and does it imply the former?


---

##### Bài tập 1.18

Examine the AI literature to discover whether the following tasks can
currently be solved by computers:

- Playing a decent game of table tennis (Ping-Pong).
- Driving in the center of Cairo, Egypt.
- Driving in Victorville, California.
- Buying a week’s worth of groceries at the market.
- Buying a week’s worth of groceries on the Web.
- Playing a decent game of bridge at a competitive level.
- Discovering and proving new mathematical theorems.
- Writing an intentionally funny story.
- Giving competent legal advice in a specialized area of law.
- Translating spoken English into spoken Swedish in real time.
- Performing a complex surgical operation.


---

##### Bài tập 1.19

For the currently infeasible tasks, try to find out what the
difficulties are and predict when, if ever, they will be overcome.


---

##### Bài tập 1.20

Various subfields of AI have held contests by defining a standard task
and inviting researchers to do their best. Examples include the DARPA
Grand Challenge for robotic cars, the International Planning
Competition, the Robocup robotic soccer league, the TREC information
retrieval event, and contests in machine translation and speech
recognition. Investigate five of these contests and describe the
progress made over the years. To what degree have the contests advanced
the state of the art in AI? To what degree do they hurt the field by
drawing energy away from new ideas?


---


<!-- tabs:end -->
