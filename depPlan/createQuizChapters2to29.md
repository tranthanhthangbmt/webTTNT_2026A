# Kế hoạch Triển khai Trắc nghiệm (Quiz) cho Các Chương 2 - 29

## Mục tiêu
Dựa trên nền tảng và bộ quy tắc đã thống nhất ở Chương 1, mục tiêu của kế hoạch này là mở rộng (scale) hệ thống bài tập trắc nghiệm cho toàn bộ các chương còn lại (từ Chương 2 đến Chương 29). 
Hệ thống sẽ đảm bảo tính đồng bộ tuyệt đối về giao diện, nguyên tắc sư phạm và trải nghiệm người dùng trên toàn trang web.

## Giải pháp Triển khai (Mở rộng quy mô)

### 1. Kế thừa Interactive Quiz Engine (Tái sử dụng Code)
File `js/quiz_engine.js` được thiết kế cho Chương 1 sẽ được xây dựng theo hướng **Tái sử dụng (Reusable Component)**. 
- Thay vì viết code riêng cho từng chương, engine sẽ tự động nhận diện người dùng đang ở chương nào (thông qua URL hoặc thuộc tính `data-chapter`) và tải file JSON tương ứng.
- **Ví dụ:** Nếu sinh viên đang ở tab Trắc nghiệm của Chương 5, engine sẽ tự động tải file `quizzes/chapter_05.json`.
- Việc này giúp trang web chạy cực kỳ nhẹ, không bị phình to code.

### 2. Quy mô Dữ liệu (Massive Data Generation)
Với 28 chương còn lại (từ 2 đến 29) và mỗi chương yêu cầu đúng 30 câu hỏi, tổng cộng hệ thống cần **840 câu hỏi trắc nghiệm**.
Tất cả các câu hỏi này vẫn tuân thủ 100% các nguyên tắc đã chốt:
- **Nguồn kiến thức:** Trích xuất từ tab **Tiếng Việt** của từng chương tương ứng.
- **Số lượng:** Đúng 30 câu / chương.
- **Mức độ:** Dễ, Trung bình, Khó.
- **Sắp xếp:** Từ dễ đến khó.
- **Độ dài đồng đều:** Cho các đáp án.
- **Đa dạng dạng câu hỏi (6 loại):** 1 lựa chọn, Nhiều lựa chọn, Đúng/Sai, Điền khuyết (từ danh sách), Nối đáp án (Matching), Sắp xếp thứ tự (Ordering).

### 3. Tích hợp Hàng loạt vào Markdown
Sử dụng một kịch bản tự động (Python script) để quét qua tất cả các file từ `chapters/chapter_02_*.md` đến `chapters/chapter_29_*.md` và tự động nhúng thẻ div chứa quiz vào tab "Trắc nghiệm":
```html
<div class="quiz-container" data-chapter="02"></div>
```
*(Thay số 02 bằng số chương tương ứng).*

## Các bước Thực hiện (Execution Workflow)

Vì số lượng câu hỏi lên tới 840 câu, việc triển khai sẽ được chia làm các giai đoạn để đảm bảo chất lượng kiểm duyệt:

- **Giai đoạn 1 (Nền tảng):** Lập trình xong `js/quiz_engine.js` và `quizzes/chapter_01.json` (như kế hoạch Chương 1) để chạy thử nghiệm (Pilot) và đảm bảo giao diện, âm thanh, màu sắc hoạt động trơn tru.
- **Giai đoạn 2 (Sản xuất Dữ liệu):** Trích xuất nội dung và tự động hóa việc tạo hàng loạt file JSON từ `chapter_02.json` đến `chapter_29.json`. (Sẽ cần tiến hành cuốn chiếu từng cụm chương để kiểm tra chất lượng).
- **Giai đoạn 3 (Tích hợp & Khai báo):** Chạy script để nhúng `<div class="quiz-container">` vào tất cả các file Markdown và hoàn thiện toàn bộ khóa học.

> **Lưu ý:** Việc soạn 840 câu hỏi chất lượng cao là một khối lượng công việc lớn. Tôi (AI) sẽ hỗ trợ bạn tự động sinh (generate) các câu hỏi này từ văn bản Tiếng Việt theo đúng cấu trúc JSON đã định. 
