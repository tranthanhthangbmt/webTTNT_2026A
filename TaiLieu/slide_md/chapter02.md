\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Tác tử thông minh (Intelligent Agents)

## Chương 2

---
## Nhắc nhở

*Nhiệm vụ 0 (bồi dưỡng ngọn lửa nói ngọng) hạn chót vào ngày 28/1*

*Hướng dẫn Lisp/emacs/AIMA*: 1-11 hôm nay và thứ Hai, 271 Soda

---
## Phác thảo

- Tác nhân và môi trường

- Tính hợp lý

- PEAS (Đo hiệu suất, Môi trường, Bộ truyền động, Cảm biến)

- Các loại môi trường

- Các loại tác nhân

---
## Tác nhân và môi trường

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/agent-environment.png)

\defn{Đại lý} bao gồm con người, robot, robot mềm, bộ điều nhiệt, v.v.

Hàm tác nhân \defn{} ánh xạ từ lịch sử nhận thức đến hành động:
\[f: {\cal P}^* \rightarrow {\cal A}\]
Chương trình tác nhân \defn{} chạy trên kiến trúc \defn{ vật lý} để tạo ra $f$

---
## Thế giới máy hút bụi

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-environment.png)

Nhận thức: vị trí và nội dung, ví dụ: $[A,Dirty]$

Hành động: $Left$, $Right$, $Suck$, $NoOp$

---
## Chất làm sạch máy hút bụi 

| &nbsp; | &nbsp; |
|---|---|
| Percept sequence | Action |
| $[A,Clean]$ | $Right$ |
| $[A,Dirty]$ | $Suck$ |
| $[B,Clean]$ | $Left$ |
| $[B,Dirty]$ | $Suck$ |
| $[A,Clean]$, $[A,Clean]$ | $Right$ |
| $[A,Clean]$, $[A,Dirty]$ | $Suck$ |
| $\vdots$ | $\vdots$ |

\medskip

```text
function Reflex-Vacuum-Agent([location,status]) returns an action

    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

Chức năng *right* là gì? 

Nó có thể được thực hiện trong một chương trình đại lý nhỏ không?

---
## Tính hợp lý

Đã sửa lỗi \defn{đo lường hiệu suất} đánh giá trình tự môi trường \note{}
  
-- một điểm trên mỗi ô vuông được dọn sạch kịp thời $T$?
  
-- một điểm cho mỗi ô vuông sạch trong mỗi bước thời gian, trừ một điểm cho mỗi nước đi?
  
-- phạt cho ${}> k$ ô vuông bẩn?

Tác nhân hợp lý \txr{} chọn bất kỳ hành động nào tối đa hóa giá trị \txr{expected} của
thước đo hiệu suất \txr{ đưa ra trình tự nhận thức cho đến nay }

Hợp lý $\neq$ toàn trí 
    
   -- nhận thức có thể không cung cấp tất cả thông tin liên quan

Lý trí $\neq$ thấu thị 
    
   -- kết quả hành động có thể không như mong đợi

Do đó, hợp lý $\neq$ thành công

Hợp lý $\implies$ khám phá, học tập, tự chủ

---
## Đậu Hà Lan

Để thiết kế một tác nhân hợp lý, chúng ta phải chỉ định môi trường tác vụ \txr{}

Ví dụ, hãy xem xét nhiệm vụ thiết kế một chiếc taxi tự động:

<u>Thước đo hiệu suất</u>??

<u>Môi trường</u>??

<u>Bộ truyền động</u>??

<u>Cảm biến</u>??

---
## Đậu Hà Lan

Để thiết kế một tác nhân hợp lý, chúng ta phải chỉ định môi trường tác vụ \txr{}

Ví dụ, hãy xem xét nhiệm vụ thiết kế một chiếc taxi tự động:

<u>Đo lường hiệu quả hoạt động</u>?? an toàn, điểm đến, lợi nhuận, tính hợp pháp, sự thoải mái, $\ldots$

<u>Môi trường</u>?? Đường phố/đường cao tốc ở Hoa Kỳ, giao thông, người đi bộ, thời tiết, $\ldots$

<u>Thiết bị truyền động</u>?? tay lái, chân ga, phanh, còi, loa/màn hình, $\ldots$

<u>Cảm biến</u>?? video, gia tốc kế, đồng hồ đo, cảm biến động cơ, bàn phím, GPS, $\ldots$

---
## Đại lý mua sắm qua Internet

<u>Thước đo hiệu suất</u>??

<u>Môi trường</u>??

<u>Bộ truyền động</u>??

<u>Cảm biến</u>??

---
## Đại lý mua sắm qua Internet

<u>Thước đo hiệu suất</u>?? giá cả, chất lượng, sự phù hợp, hiệu quả

<u>Môi trường</u>?? Các trang web WWW, nhà cung cấp, chủ hàng hiện tại và tương lai

<u>Actuators</u>?? hiển thị cho người dùng, theo dõi URL, điền vào biểu mẫu

<u>Cảm biến</u>?? Trang HTML (văn bản, đồ họa, tập lệnh)

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? |  |  |  |  |
| <u>Xác định</u>?? |  |  |  |  |
| <u>Tập</u>?? |  |  |  |  |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? |  |  |  |  |
| <u>Tập</u>?? |  |  |  |  |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? |  |  |  |  |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán | Bán | Không |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán | Bán | Không |
| <u>Rời rạc</u>?? | Có | Có | Có | Không |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán | Bán | Không |
| <u>Rời rạc</u>?? | Có | Có | Có | Không |
| <u>Một đại lý</u>?? | Có | Không | Có (ngoại trừ đấu giá) | Không |

\bigskip

*Loại môi trường quyết định phần lớn thiết kế tác nhân*

Thế giới thực (tất nhiên) có thể quan sát được một phần, ngẫu nhiên, tuần tự,
năng động, liên tục, đa tác nhân

---
## Các loại tác nhân

Bốn loại cơ bản theo thứ tự tổng quát tăng dần:
  
-- tác nhân phản xạ đơn giản
  
-- tác nhân phản xạ có trạng thái
  
-- tác nhân dựa trên mục tiêu
  
-- đại lý dựa trên tiện ích

Tất cả những thứ này có thể được biến thành tác nhân học tập

---
## Các tác nhân phản xạ đơn giản

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/simple-reflex-agent.png)

---
## Ví dụ

\medskip

```text
function Reflex-Vacuum-Agent([location,status]) returns an action

    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

\bigskip

```text
(setq joe (make-agent :name 'joe :body (make-agent-body)
                      :program (make-reflex-vacuum-agent-program)))

(defun make-reflex-vacuum-agent-program ()
  #'(lambda (percept)
      (let ((location (first percept)) (status (second percept)))
        (cond ((eq status 'dirty) 'Suck)
              ((eq location 'A) 'Right)
              ((eq location 'B) 'Left)))))
```

---
## Tác nhân phản xạ có trạng thái 

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/reflex+state-agent.png)

---
## Ví dụ

\medskip

```text
function Reflex-Vacuum-Agent([location,status]) returns an action
  static: last\_A,\ last\_B, numbers, initially infinity

    if status = Dirty then $\ldots$
```

\bigskip

```text
(defun make-reflex-vacuum-agent-with-state-program ()
  (let ((last-A infinity) (last-B infinity))
  #'(lambda (percept)
      (let ((location (first percept)) (status (second percept)))
        (incf last-A) (incf last-B)
        (cond 
         ((eq status 'dirty) 
          (if (eq location 'A) (setq last-A 0) (setq last-B 0))
          'Suck)
         ((eq location 'A) (if (> last-B 3) 'Right 'NoOp))
         ((eq location 'B) (if (> last-A 3) 'Left 'NoOp)))))))
```

---
## Tác nhân dựa trên mục tiêu

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/goal-based-agent.png)

---
## Tác nhân dựa trên tiện ích

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/utility-based-agent.png)

---
## Tác nhân học tập

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/learning-agent.png)

---
## Tóm tắt

\defn{Tác nhân} tương tác với \defn{môi trường} thông qua
\defn{bộ truyền động} và cảm biến \defn{}

Hàm tác nhân \defn{} mô tả những gì tác nhân thực hiện trong mọi trường hợp

Thước đo hiệu suất \defn{} đánh giá trình tự môi trường

Tác nhân \defn{hoàn toàn hợp lý} tối đa hóa hiệu suất mong đợi 

\defn{Chương trình tác nhân} triển khai (một số) chức năng của tác nhân

Mô tả \defn{PEAS} xác định môi trường tác vụ

Môi trường được phân loại theo nhiều chiều:
    
  \defn{có thể quan sát được}? \defn{ xác định }? \defn{tập}? \defn{tĩnh}? 
  \defn{rời rạc}? \defn{đại lý đơn lẻ}?

Một số kiến trúc tác nhân cơ bản tồn tại:
    
  \defn{phản xạ}, \defn{phản xạ với trạng thái}, \defn{dựa trên mục tiêu}, 
  \defn{dựa trên tiện ích}