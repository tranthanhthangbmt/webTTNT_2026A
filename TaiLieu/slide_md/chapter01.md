\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Trí tuệ nhân tạo (Artificial Intelligence)

## Chương 1

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