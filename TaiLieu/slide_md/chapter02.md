\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Tác nhân thông minh

## Chương 2

---
## Nội dung

- PAGE (Nhận thức, Hành động, Mục tiêu, Môi trường)

- Các loại môi trường

- Hàm tác nhân và chương trình tác nhân

- Các loại tác nhân

- Thế giới máy hút bụi

---
## PAGE

Đầu tiên phải xác định bối cảnh để thiết kế tác nhân thông minh

Xem xét, ví dụ: nhiệm vụ thiết kế một chiếc taxi tự động:

<u>Nhận thức (Percepts)</u>??

<u>Hành động (Actions)</u>??

<u>Mục tiêu (Goals)</u>??

<u>Môi trường (Environment)</u>??

---
## PAGE

Đầu tiên phải xác định bối cảnh để thiết kế tác nhân thông minh

Xem xét, ví dụ: nhiệm vụ thiết kế một chiếc taxi tự động:

<u>Nhận thức (Percepts)</u>?? video, gia tốc kế, đồng hồ đo, cảm biến động cơ, bàn phím, GPS, $\ldots$

<u>Hành động (Actions)</u>?? bẻ lái, tăng tốc, phanh, bấm còi, nói/hiển thị, $\ldots$

<u>Mục tiêu (Goals)</u>?? an toàn, đến đích, tối đa hóa lợi nhuận, tuân thủ luật pháp, sự thoải mái của hành khách, $\ldots$

<u>Môi trường (Environment)</u>?? đường phố Mỹ, đường cao tốc, giao thông, người đi bộ, thời tiết, khách hàng, $\ldots$

---
## Tác nhân mua sắm trên Internet

<u>Nhận thức</u>??

<u>Hành động</u>??

<u>Mục tiêu</u>??

<u>Môi trường</u>??

---
## Tác nhân hợp lý (Rational agents)

Không mất tính tổng quát, "mục tiêu" có thể được xác định bằng <u>độ đo hiệu suất</u>

xác định một giá trị số cho bất kỳ lịch sử môi trường nào

<u>Hành động hợp lý</u>: bất kỳ hành động nào tối đa hóa giá trị kỳ vọng của
độ đo hiệu suất <u>cho trước chuỗi nhận thức cho đến nay</u>

Hợp lý $\neq$ toàn tri (omniscient)

Hợp lý $\neq$ thấu thị (clairvoyant)

Hợp lý $\neq$ thành công (successful)

---
## Các loại môi trường

\resizebox{\textwidth}{!}{

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Xếp bài (Solitaire)} | {Cờ đố (Backgammon)} | {Mua sắm Internet} | {Taxi} |
| <u>Có thể truy cập (Accessible)</u>?? |  |  |  |  |
| <u>Tất định (Deterministic)</u>?? |  |  |  |  |
| <u>Theo giai đoạn (Episodic)</u>?? |  |  |  |  |
| <u>Tĩnh (Static)</u>?? |  |  |  |  |
| <u>Rời rạc (Discrete)</u>?? |  |  |  |  |

}

---
## Các loại môi trường

\resizebox{\textwidth}{!}{

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Xếp bài} | {Cờ đố} | {Mua sắm Internet} | {Taxi} |
| <u>Có thể truy cập</u>?? | Có | Có | Không | Không |
| <u>Tất định</u>?? | Có | Không | Một phần | Không |
| <u>Theo giai đoạn</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán tĩnh | Bán tĩnh | Không |
| <u>Rời rạc</u>?? | Có | Có | Có | Không |

}

Loại môi trường phần lớn quyết định thiết kế của tác nhân

Thế giới thực (tất nhiên) là không thể truy cập, ngẫu nhiên, tuần tự,
động, liên tục

---
## Hàm tác nhân và chương trình

Một tác nhân được xác định hoàn toàn bởi <u>hàm tác nhân</u>

ánh xạ chuỗi nhận thức thành các hành động

(Về nguyên tắc, người ta có thể cung cấp từng chuỗi có thể để xem nó
làm gì. Rõ ràng, một bảng tra cứu thường sẽ rất khổng lồ.)

Một hàm tác nhân (hoặc một lớp tương đương nhỏ) là <u>hợp lý</u>

Mục đích: tìm cách triển khai hàm tác nhân hợp lý một cách ngắn gọn

Một <u>chương trình tác nhân</u> lấy một nhận thức duy nhất làm đầu vào, lưu giữ
trạng thái nội bộ:

```text
function Skeleton-Agent(percept) returns hành\_động
      static: memory, bộ nhớ của tác nhân về thế giới

    memory <- Update-Memory(memory, percept)
    hành\_động <- Choose-Best-Action(memory)
    memory <- Update-Memory(memory, hành\_động)
    return hành\_động
```

---
## Mã nguồn AIMA

Mã nguồn cho mỗi chủ đề được chia thành bốn thư mục:
  
-- `agents`: mã nguồn định nghĩa các loại tác nhân và chương trình
  
-- `algorithms`: mã nguồn cho các phương pháp được sử dụng bởi chương trình tác nhân
  
-- `environments`: mã nguồn định nghĩa các loại môi trường, mô phỏng
  
-- `domains`: các loại bài toán và ví dụ đầu vào cho thuật toán

(Thường chạy các thuật toán trên các miền thay vì các tác nhân trong môi trường.)

{\small

```text
(setq joe (make-agent :name 'joe :body (make-agent-body)
                      :program (make-dumb-agent-program)))

(defun make-dumb-agent-program ()
  (let ((memory nil))
    #'(lambda (percept)
        (push percept memory)
        'no-op)))
```

}

---
## Các loại tác nhân

Bốn loại cơ bản theo thứ tự tính tổng quát tăng dần:
  
-- tác nhân phản xạ đơn giản
  
-- tác nhân phản xạ có trạng thái
  
-- tác nhân dựa trên mục tiêu
  
-- tác nhân dựa trên độ hữu dụng

---
## Tác nhân phản xạ đơn giản

![Hình ảnh](../TaiLieu/slide_md/figures/d-agent.png)

---
## Tác nhân phản xạ có trạng thái

![Hình ảnh](../TaiLieu/slide_md/figures/d+-agent.png)

---
## Tác nhân dựa trên mục tiêu

![Hình ảnh](../TaiLieu/slide_md/figures/goal-based-agent.png)

---
## Tác nhân dựa trên độ hữu dụng

![Hình ảnh](../TaiLieu/slide_md/figures/utility-based-agent.png)

---
## Thế giới máy hút bụi

`code/agents/environments/vacuum.lisp`

<u>Nhận thức</u> `(<bump> <dirt> <home>)`![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2.png)

<u>Hành động</u> `shutoff forward suck (turn left) (turn right)`

<u>Mục tiêu</u> (độ đo hiệu suất trên lịch sử môi trường)
  
-- +100 cho mỗi mảng bụi được dọn sạch
  
-- -1 cho mỗi hành động
  
-- -1000 nếu tắt máy khi xa nhà

<u>Môi trường</u>
  
-- dạng lưới, tường/chướng ngại vật, phân bố và tạo bụi, cơ thể
tác nhân
  
-- các hành động di chuyển hoạt động trừ khi đụng tường
  
-- hành động hút đưa bụi vào cơ thể tác nhân (hoặc không)

Có thể truy cập? Tất định? Theo giai đoạn? Tĩnh? Rời rạc?