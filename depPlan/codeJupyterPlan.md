# Tích hợp Trình Xem & Chạy Code Python Trực Tiếp Trên Web

Để có thể xem và **chạy trực tiếp** mã nguồn Python (`.py`) ngay trên nền web (mà không cần cài đặt Python hay chạy server backend), giải pháp tối ưu nhất cho một trang web tĩnh (như Docsify của bạn) là sử dụng **WebAssembly** với thư viện **Pyodide** hoặc **PyScript**. 

Dưới đây là kế hoạch chi tiết để hiện thực hóa tính năng này.

## Open Questions
- Thư mục dự án này (`webTTNT_2026`) sau này sẽ được đưa lên Github/Hosting công khai hay chỉ chạy local (máy tính cá nhân)? (Điều này ảnh hưởng đến cách cấu hình đường dẫn tới các file code).
- Với file `.ipynb`, bạn có muốn tôi tự động tạo link mở thẳng bằng **Google Colab** (nếu web được up lên Github) không, hay cứ giữ nguyên tải về để bạn tự upload lên Colab như hiện tại?

## Đề Xuất Kế Hoạch (Proposed Changes)

### 1. Tạo Trang IDE Thu Nhỏ (`python_runner.html`)

Tôi sẽ tạo một trang web độc lập đóng vai trò như một môi trường lập trình (IDE) thu nhỏ, bao gồm:
- **Trình soạn thảo mã nguồn (Code Editor):** Sử dụng thư viện `CodeMirror` hoặc `Ace Editor` để hiển thị code Python với đầy đủ màu sắc (syntax highlighting), đánh số dòng. Người dùng có thể đọc hoặc thậm chí chỉnh sửa code trực tiếp trên web.
- **Trình thực thi Python (Pyodide):** Tích hợp thư viện `Pyodide` (Python chạy trực tiếp trên trình duyệt qua WebAssembly).
- **Cửa sổ Output (Console):** Nơi hiển thị kết quả (các lệnh `print`, lỗi syntax, v.v.) khi người dùng nhấn nút **"Chạy Code"**.

Trang này sẽ nhận tên file qua URL (ví dụ: `python_runner.html?file=codeAndExercises/.../agents.py`), tự động đọc nội dung file `.py` đó và đưa vào trình soạn thảo.

### 2. Cập Nhật Các Link Code Python

Tôi sẽ viết lại script `fix_code_links.py` để thay đổi cách hoạt động của các link trong tab **Python**:

- **Với file `.py`:** Thay vì mở file raw gốc, link sẽ được đổi thành:
  `<a href="python_runner.html?file=codeAndExercises/.../agents.py" target="_blank" data-ignore>Agents (Python File)</a>`
  Khi sinh viên click vào, một tab mới với giao diện IDE sẽ mở ra, load sẵn code của bài đó và có thể bấm "Run" để chạy luôn.
  
- **Với file `.ipynb`:**
  - Nếu web có Github: Có thể đổi thành link `https://colab.research.google.com/github/TênUser/TênRepo/blob/main/codeAndExercises/...` để mở thẳng Colab.
  - Tạm thời vẫn sẽ giữ nguyên link tải file như hiện tại để dùng cho môi trường Local.

### 3. Tùy Chỉnh Giao Diện Gắn Kết

Đảm bảo trang `python_runner.html` có giao diện (màu sắc, font chữ) đồng nhất với giao diện xanh/trắng hiện tại của Docsify (đã được tinh chỉnh từ trước).

---
> [!TIP]
> Việc dùng **Pyodide** vô cùng an toàn và thông minh vì mã Python được biên dịch và chạy 100% bên trong trình duyệt của sinh viên (client-side), hoàn toàn không tiêu tốn tài nguyên máy chủ và không yêu cầu sinh viên phải cài đặt bất kỳ thứ gì.

**Vui lòng bấm 'Proceed' nếu bạn đồng ý với kế hoạch này, hoặc cho tôi biết nếu bạn muốn điều chỉnh gì nhé!**
