# Kế hoạch Tạo Tab Trắc nghiệm (Quiz) cho Chương 1

## Mục tiêu
Thiết kế và tích hợp hệ thống bài tập trắc nghiệm tương tác cho Chapter 01. Hệ thống cần đa dạng (nhiều loại câu hỏi), bám sát nội dung từ **tab Tiếng Việt**, và tuân thủ chặt chẽ nguyên tắc sư phạm: **"độ dài của lựa chọn đúng phải tương đương với các lựa chọn sai để tránh sinh viên đoán mò."**

## Giải pháp Đề xuất

### 1. Nguồn Kiến Thức (Source of Knowledge)
Toàn bộ nội dung câu hỏi và câu trả lời sẽ được trích xuất trực tiếp từ bản dịch Tiếng Việt của sách (được hiển thị trong tab **Tiếng Việt**). Điều này đảm bảo tính nhất quán giữa lý thuyết sinh viên đọc và bài tập sinh viên làm.

### 2. Đa Dạng Loại Hình Trắc Nghiệm (Multiple Quiz Types)
Giống như trang tham khảo, hệ thống trắc nghiệm sẽ hỗ trợ nhiều định dạng câu hỏi để tránh nhàm chán và kiểm tra kiến thức đa chiều. Cấu trúc dữ liệu (`quizzes/chapter_01.json`) sẽ định nghĩa từng `type`:
1. **Single Choice (Một lựa chọn đúng):** 4 đáp án A, B, C, D.
2. **Multiple Select (Nhiều lựa chọn đúng):** Chọn tất cả các đáp án đúng bằng Checkbox.
3. **True/False (Đúng/Sai):** Đánh giá một nhận định.
4. **Fill in the Blank (Điền khuyết từ danh sách):** Chọn từ khóa chính xác từ một danh sách thả xuống (dropdown) để điền vào ô trống.
5. **Matching (Nối đáp án):** Nối khái niệm ở cột trái với giải nghĩa tương ứng ở cột phải thông qua Dropdown.
6. **Ordering (Sắp xếp thứ tự):** Di chuyển các mục lên/xuống để sắp xếp đúng trình tự bằng các nút điều khiển.

### 3. Thành phần Giao diện (Interactive Quiz Engine)
Tôi sẽ viết một file Javascript (`js/quiz_engine.js`) để tự động tải file JSON và sinh giao diện:
- Giao diện linh hoạt thay đổi theo từng loại câu hỏi (Radio, Checkbox, Dropdown cho điền khuyết).
- **Tương tác thời gian thực (Instant Feedback):** 
  - Khi người dùng chọn một đáp án sai, lựa chọn đó sẽ **đổi màu đỏ** và người dùng vẫn được phép chọn tiếp các đáp án khác.
  - Khi người dùng chọn đúng, lựa chọn đó sẽ **đổi màu xanh** và hệ thống lập tức hiển thị đoạn văn giải thích lý do tại sao lựa chọn đó đúng (dựa trên lý thuyết của tab Tiếng Việt).
- **Thanh điều khiển (Control Bar):** Dưới mỗi câu hỏi sẽ có thanh điều hướng gồm:
  - Nút **"< Câu trước"** (quay lại câu trước).
  - Nút **"Kiểm tra"** (ở giữa): Dành riêng cho các câu hỏi không phải là Một lựa chọn đúng (như Điền khuyết, Nhiều lựa chọn đúng). Người dùng chọn xong sẽ bấm nút này để xem phản hồi đúng/sai.
  - Nút **"Câu sau >"** (chuyển sang câu tiếp theo).
- Màn hình **Tổng kết** sẽ tự động hiển thị ở câu cuối cùng để báo cáo điểm số.

### 4. Nguyên tắc Soạn thảo Câu hỏi
- **Số lượng câu hỏi:** Đảm bảo mỗi chương có chính xác **30 câu hỏi**.
- **Phân loại & Sắp xếp độ khó:** Mỗi câu hỏi phải được gắn nhãn mức độ rõ ràng (`Dễ`, `Trung bình`, `Khó`) và toàn bộ 30 câu hỏi phải được sắp xếp xuất hiện từ dễ đến khó.
- **Độ dài đồng đều:** Đối với dạng trắc nghiệm, các đáp án (đặc biệt là đáp án đúng) phải có độ dài từ ngữ tương đương nhau.
- **Tránh từ tuyệt đối:** Hạn chế "luôn luôn", "không bao giờ" ở đáp án sai.

## Ví dụ cấu trúc câu hỏi (Draft)

**Câu 1 (Một lựa chọn đúng):** Theo định nghĩa trong giáo trình, cách tiếp cận "Acting Humanly" (Hành động như con người) yêu cầu máy tính phải có khả năng nào sau đây?
- [ ] A. Khả năng giải quyết các phương trình toán học phức tạp cực kỳ nhanh.
- [ ] B. Khả năng giao tiếp bằng ngôn ngữ tự nhiên để đánh lừa người kiểm tra.
- [ ] C. Khả năng mô phỏng chính xác các phản ứng sinh học của não bộ.
- [ ] D. Khả năng tự động tìm kiếm mọi dữ liệu trên Internet mà không cần hỏi.
*(Lưu ý: Độ dài các đáp án tương đương nhau).*

**Câu 2 (Nhiều lựa chọn đúng):** Để vượt qua bài kiểm tra Turing (Turing Test), một máy tính cần sở hữu những năng lực cốt lõi nào? *(Chọn tất cả đáp án đúng)*
- [ ] Xử lý ngôn ngữ tự nhiên (Natural language processing)
- [ ] Tầm nhìn máy tính (Computer vision) - *(Yêu cầu cho Total Turing Test)*
- [ ] Suy luận tự động (Automated reasoning)
- [ ] Cơ cấu sinh học nhân tạo (Artificial biological organs)

**Câu 3 (Đúng / Sai):** Thuật ngữ "Trí tuệ nhân tạo" (Artificial Intelligence) lần đầu tiên được giới thiệu bởi Alan Turing vào năm 1950.
- [ ] Đúng
- [ ] Sai *(Giải thích: Được giới thiệu bởi John McCarthy vào năm 1956 tại hội thảo Dartmouth).*

**Câu 4 (Điền khuyết từ danh sách):**
Cách tiếp cận "Suy nghĩ hợp lý" (Thinking rationally) trong AI chủ yếu dựa trên nền tảng của môn học [ ▼ Chọn từ... ].
*(Danh sách thả xuống gồm: Tâm lý học, Triết học, Toán học, Logic học. Đáp án đúng: Logic học)*

## Các bước Thực hiện (Execution Steps)
1. Tạo thư mục `quizzes` và file `quizzes/chapter_01.json` với dữ liệu đa dạng các dạng câu hỏi dựa trên nội dung tab Tiếng Việt (Chương 1).
2. Viết mã Javascript (`js/quiz_engine.js`) để xử lý các loại câu hỏi khác nhau và logic chấm điểm.
3. Nhúng hệ thống vào file `chapters/chapter_01_introduction.md` trong tab "Trắc nghiệm".
4. Khai báo script `quiz_engine.js` và CSS tương ứng (nếu cần) vào `index.html`.
