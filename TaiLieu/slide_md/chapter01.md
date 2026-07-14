\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}
\usepackage{epstopdf}
\usepackage{url}

# Trí tuệ nhân tạo

## Chương 1

---
## Nội dung

- Tổng quan khóa học

- Trí tuệ nhân tạo (AI) là gì?

- Lược sử phát triển

- Tình hình hiện tại

---
## Thông tin hành chính

Trang chủ lớp học: \url{http://www-inst.eecs.berkeley.edu/ cs188}

nơi chứa bài giảng, bài tập, đề thi, chấm điểm, giờ giải đáp, v.v.

Bài tập 0 (ôn tập lisp) hạn nộp 8/31

Sách giáo trình: Russell and Norvig <u>Trí tuệ nhân tạo: Cách tiếp cận hiện đại</u>

Đọc Chương 1 và 2 cho tài liệu tuần này

Code: bản cài đặt lisp tích hợp cho các thuật toán AIMA tại

\url{http://www-inst.eecs.berkeley.edu/ cs188/code/}

---
## Tổng quan khóa học

- tác nhân thông minh (intelligent agents)

- tìm kiếm và chơi trò chơi

- các hệ thống logic

- các hệ thống lập kế hoạch

- độ bất định---xác suất và lý thuyết quyết định

- học máy

- ngôn ngữ

- nhận thức

- robot học

- các vấn đề triết học

---
## AI là gì?

| &nbsp; | &nbsp; |
|---|---|
| "[The automation of] activities that we associate with human thinking, activities such as decision-making, problem solving, learning $\ldots$" (Bellman, 1978) | "The study of mental faculties through the use of computational models" (Charniak+McDermott, 1985) |
| "The study of how to make computers do things at which, at the moment, people are better" (Rich+Knight, 1991) | "The branch of computer science that is concerned with the automation of intelligent behavior" (Luger+Stubblefield, 1993) |

Các quan điểm về AI được chia thành bốn loại:

| &nbsp; | &nbsp; |
|---|---|
| Suy nghĩ như người | Suy nghĩ hợp lý |
| Hành động như người | Hành động hợp lý |

Khi xem xét những điều này, chúng ta sẽ nghiêng về hành động hợp lý (ở một mức độ nào đó)
 

---
## Hành động như người: Phép thử Turing

Turing (1950) "Máy tính và trí thông minh":

- "Máy móc có thể suy nghĩ không?" $\longrightarrow$ "Máy móc có thể hành xử thông minh không?"

- Bài kiểm tra thực hành cho hành vi thông minh: Trò chơi bắt chước

![Hình ảnh](../TaiLieu/slide_md/figures/turing.png)

- Dự đoán rằng đến năm 2000, một cỗ máy có 30\% cơ hội
  
     đánh lừa một người bình thường trong 5 phút

- Dự đoán trước tất cả các lập luận chính chống lại AI trong 50 năm tiếp theo

- Đề xuất các thành phần chính của AI: tri thức, lập luận, hiểu
  
     ngôn ngữ, học máy
[0.1in]
Vấn đề: Phép thử Turing không có <u>tính lặp lại</u>, <u>tính kiến thiết</u>, hoặc

phù hợp để <u>phân tích toán học</u>

---
## Suy nghĩ như người: Khoa học nhận thức
	

Thập niên 1960 "cách mạng nhận thức": tâm lý học xử lý thông tin thay thế

cho học thuyết hành vi đang thịnh hành

Yêu cầu các lý thuyết khoa học về các hoạt động bên trong của não bộ
  
 -- Ở mức độ trừu tượng nào? "Tri thức" hay "mạch điện"?
  
 -- Làm thế nào để kiểm chứng? Yêu cầu 
    
    1) Dự đoán và kiểm tra hành vi của con người (từ trên xuống)
    
    hoặc 2) Nhận dạng trực tiếp từ dữ liệu thần kinh (từ dưới lên)

Cả hai cách tiếp cận (nói chung là Khoa học nhận thức và Khoa học thần kinh nhận thức) 

hiện nay đều tách biệt với AI

---
## Suy nghĩ hợp lý: Các định luật của tư duy

<u>Chuẩn tắc</u> (hoặc <u>mô tả quy tắc</u>) hơn là <u>mô tả hiện tượng</u>

Aristotle: thế nào là quá trình lập luận/tư duy đúng đắn?

Một số trường phái Hy Lạp đã phát triển nhiều dạng <u>logic</u>:
  
   <u>ký hiệu</u> và <u>các quy tắc dẫn xuất</u> cho tư duy;

có thể đã hoặc chưa tiến tới ý tưởng cơ giới hóa

Đường lối trực tiếp qua toán học và triết học dẫn đến AI hiện đại

Vấn đề: 

1) Không phải tất cả hành vi thông minh đều được trung gian bởi sự suy ngẫm logic

2) Mục đích của suy nghĩ là gì? Tôi nên có những suy nghĩ nào?

---
## Hành động hợp lý

Hành vi <u>hợp lý</u>: làm điều đúng đắn

Điều đúng đắn: điều được kỳ vọng sẽ tối đa hóa việc đạt được mục tiêu,

dựa trên thông tin có sẵn

Không nhất thiết liên quan đến suy nghĩ---ví dụ: phản xạ chớp mắt---nhưng

suy nghĩ nên phục vụ cho hành động hợp lý

Aristotle (Đạo đức học Nicomachean):
  
  *Mọi nghệ thuật và mọi sự tìm tòi, cũng như mọi hành động 
  
       và theo đuổi, đều được cho là hướng tới một điều tốt đẹp nào đó*

---
## Tác nhân hợp lý

Một <u>tác nhân</u> là một thực thể cảm nhận và hành động

Khóa học này xoay quanh việc thiết kế các tác nhân hợp lý

Một cách trừu tượng, một tác nhân là một hàm từ lịch sử nhận thức đến các hành động:
\[f: {\cal P}^* \rightarrow {\cal A}\]
Đối với bất kỳ lớp môi trường và tác vụ nào, chúng ta tìm kiếm

tác nhân (hoặc lớp tác nhân) có hiệu suất tốt nhất

Lưu ý: những hạn chế về tính toán khiến cho sự hợp lý hoàn hảo không thể đạt được

$\rightarrow$ thiết kế <u>chương trình</u> tốt nhất cho các tài nguyên máy móc nhất định

---
## Tiền sử của AI

\resizebox{\textwidth}{!}{

| &nbsp; | &nbsp; |
|---|---|
| Triết học | logic, các phương pháp lập luận |
|  | tâm trí như một hệ thống vật lý |
|  | nền tảng của học máy, ngôn ngữ, tính hợp lý |
| Toán học | biểu diễn và chứng minh hình thức |
|  | thuật toán |
|  | tính toán, tính (không) quyết định được, tính (không) giải được |
|  | xác suất |
| Tâm lý học | sự thích nghi |
|  | các hiện tượng nhận thức và kiểm soát vận động |
|  | các kỹ thuật thực nghiệm (tâm lý vật lý học, v.v.) |
| Ngôn ngữ học | biểu diễn tri thức |
|  | ngữ pháp |
| Khoa học thần kinh | cơ sở vật chất cho hoạt động tâm trí |
| Lý thuyết điều khiển | các hệ thống cân bằng nội môi, tính ổn định |
|  | các thiết kế tác nhân tối ưu đơn giản |

}

---
## Tóm tắt lịch sử AI

\resizebox{\textwidth}{!}{

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| 1943 | McCulloch \ | Pitts: Mô hình mạch Boolean của não bộ |
| 1950 | "Máy tính và trí thông minh" của Turing |
| 1952--69 | Hãy nhìn này, không cần dùng tay! |
| 1950s | Các chương trình AI sơ khai, bao gồm chương trình cờ đam của Samuel, |
|  | Logic Theorist của Newell \ | Simon, Geometry Engine của Gelernter |
| 1956 | Hội nghị Dartmouth: Thuật ngữ "Trí tuệ nhân tạo" được chấp nhận |
| 1965 | Thuật toán hoàn chỉnh của Robinson cho lập luận logic |
| 1966--74 | AI khám phá ra độ phức tạp tính toán |
|  | Nghiên cứu mạng nơ-ron gần như biến mất |
| 1969--79 | Sự phát triển ban đầu của các hệ chuyên gia |
| 1980--88 | Ngành công nghiệp hệ chuyên gia bùng nổ |
| 1988--93 | Ngành công nghiệp hệ chuyên gia phá sản: "Mùa đông AI" |
| 1985--95 | Mạng nơ-ron trở lại phổ biến |
| 1988-- | Sự trỗi dậy của các phương pháp xác suất và lý thuyết quyết định |
|  | Sự gia tăng nhanh chóng về chiều sâu kỹ thuật của AI chính thống |
|  | "Nouvelle AI": ALife, Thuật toán di truyền (GAs), tính toán mềm |

}

---
## Tình hình hiện tại

Những điều nào sau đây có thể thực hiện được ở hiện tại?

- Chơi bóng bàn ở mức độ khá 

- Lái xe trên một con đường núi quanh co 

- Lái xe ở trung tâm Cairo 

- Chơi bài bridge ở mức độ khá 

- Khám phá và chứng minh một định lý toán học mới 

- Cố tình viết một câu chuyện hài hước 

- Đưa ra lời khuyên pháp lý có năng lực trong một lĩnh vực chuyên ngành

- Dịch tiếng Anh nói sang tiếng Thụy Điển nói theo thời gian thực