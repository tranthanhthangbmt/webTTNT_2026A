\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Chơi trò chơi (Game playing)

## Chương 5, Phần 1--5

---
## Nội dung

- Chơi hoàn hảo (Perfect play)

- Giới hạn tài nguyên (Resource limits)

- Tỉa nhánh $
  pha$--$\beta$ ($
  pha$--$\beta$ pruning)

- Trò chơi may rủi (Games of chance)

---
## Trò chơi so với Bài toán tìm kiếm

Đối thủ "không thể đoán trước" $\Rightarrow$ giải pháp là một kế hoạch dự phòng

Giới hạn thời gian $\Rightarrow$ khó có thể tìm thấy đích, phải xấp xỉ

Kế hoạch tấn công:
\begin{itemize}
\item thuật toán chơi hoàn hảo (Von Neumann, 1944)
\item chân trời hữu hạn (finite horizon), đánh giá xấp xỉ (Zuse, 1945; Shannon, 1950; Samuel, 1952--57)
\item tỉa nhánh để giảm chi phí (McCarthy, 1956)
\end{itemize}

---
## Các loại trò chơi

![Hình ảnh](../TaiLieu/slide_md/figures/game-types.png)

---
## Minimax

Chơi hoàn hảo đối với các trò chơi tất định, thông tin hoàn hảo

Ý tưởng: chọn bước đi đến vị trí có *giá trị minimax* cao nhất
    
= phần thưởng đạt được tốt nhất khi chống lại lối chơi tốt nhất của đối thủ

Ví dụ, trò chơi 2 lượt (2-ply):

![Hình ảnh](../TaiLieu/slide_md/figures/minimax.png)

---
## Thuật toán Minimax

```text
function Minimax-Decision(game) returns một toán tử

    for each op in Operators[game] do
          Value[op] <- Minimax-Value(Apply(op, game), game)
    end
    return op có Value[op] cao nhất
\fnsep
function Minimax-Value(state, game) returns một giá trị tiện ích

    if Terminal-Test[game](state) then
          return Utility[game](state)
    else if đến lượt **max** di chuyển trong state then
          return Minimax-Value cao nhất của Successors(state)
    else 
          return Minimax-Value thấp nhất của Successors(state)
```

---
## Thuộc tính của minimax

<u>Đầy đủ (Complete)</u>??

<u>Tối ưu (Optimal)</u>??

<u>Độ phức tạp thời gian (Time complexity)</u>??

<u>Độ phức tạp không gian (Space complexity)</u>??

---
## Thuộc tính của minimax

<u>Đầy đủ</u>?? Có, nếu cây là hữu hạn (cờ vua có các quy tắc cụ thể cho việc này)

<u>Tối ưu</u>?? Có, khi chơi với một đối thủ tối ưu. Nếu không thì sao??

<u>Độ phức tạp thời gian</u>?? $O(b^m)$

<u>Độ phức tạp không gian</u>?? $O(bm)$ (duyệt theo chiều sâu)

Đối với cờ vua, $b\approx 35$, $m \approx 100$ cho các ván cờ "hợp lý"
    
$\Rightarrow$ giải pháp chính xác là hoàn toàn không khả thi

---
## Giới hạn tài nguyên

Giả sử chúng ta có 100 giây, duyệt $10^4$ nút/giây
    
$\Rightarrow$ <u>$10^6$</u> nút mỗi nước đi

Phương pháp tiêu chuẩn:
\begin{itemize}
\item *kiểm tra cắt cụt (cutoff test)*
    
ví dụ, giới hạn độ sâu (có thể thêm *tìm kiếm tĩnh - quiescence search*)
\item *hàm đánh giá (evaluation function)*
    
= mức độ mong muốn ước tính của vị trí
\end{itemize}

---
## Hàm đánh giá

![Hình ảnh](../TaiLieu/slide_md/figures/chess-evaluation-bc.png)

Đối với cờ vua, thông thường là tổng trọng số *tuyến tính* của các <u>đặc trưng</u> (features)
\[
**Eval**(s) = w_1 f_1(s) + w_2 f_2(s) + \ldots + w_n f_n(s)
\]
ví dụ, $w_1 = 9$ với 

$f_1(s)$ = (số lượng quân hậu trắng) -- (số lượng quân hậu đen)

v.v.

---
## Bàn luận: Các giá trị chính xác không quan trọng

![Hình ảnh](../TaiLieu/slide_md/figures/ordinal-utility.png)

Hành vi được bảo toàn dưới bất kỳ phép biến đổi *đơn điệu* (monotonic) nào của
**Eval**

Chỉ có thứ tự là quan trọng:
    
phần thưởng trong các trò chơi tất định hoạt động như một hàm *hữu dụng thứ bậc* (ordinal utility)

---
## Cắt cụt tìm kiếm

**MinimaxCutoff** giống hệt **MinimaxValue** ngoại trừ
    
1. **Terminal?** được thay thế bằng **Cutoff?**
    
2. **Utility** được thay thế bằng **Eval**

Nó có hoạt động trong thực tế không?
\[
b^m = 10^6, &nbsp;&nbsp;  b=35 &nbsp;&nbsp;  \Rightarrow  &nbsp;&nbsp;  m=4
\]
Dự đoán trước 4 lượt (4-ply) là một người chơi cờ vô vọng!

4-ply $\approx$ người mới chơi

8-ply $\approx$ PC điển hình, kiện tướng con người

12-ply $\approx$ Deep Blue, Kasparov

---
## Ví dụ tỉa nhánh $
  pha$--$\beta$

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress1.png)

---
## Ví dụ tỉa nhánh $
  pha$--$\beta$

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress2.png)

---
## Ví dụ tỉa nhánh $
  pha$--$\beta$

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress3.png)

---
## Ví dụ tỉa nhánh $
  pha$--$\beta$

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress4.png)

---
## Ví dụ tỉa nhánh $
  pha$--$\beta$

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress5.png)

---
## Thuộc tính của $
  pha$--$\beta$

Tỉa nhánh *không* ảnh hưởng đến kết quả cuối cùng

Thứ tự nước đi tốt sẽ cải thiện hiệu quả của việc tỉa nhánh

Với "thứ tự hoàn hảo", độ phức tạp thời gian = $O(b^{m/2})$
    
$\Rightarrow$ *tăng gấp đôi* độ sâu tìm kiếm
    
$\Rightarrow$ có thể dễ dàng đạt đến độ sâu 8 và chơi cờ tốt

Một ví dụ đơn giản về giá trị của việc suy luận xem tính toán nào là 
có liên quan (một dạng *siêu suy luận - metareasoning*)

---
## Tại sao nó được gọi là $
  pha$--$\beta$?

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-general.png)

$
  pha$ là giá trị tốt nhất (đối với **max**) được tìm thấy cho đến nay ngoài đường đi hiện tại

Nếu $V$ tệ hơn $
  pha$, **max** sẽ tránh nó
$\Rightarrow$ tỉa bỏ nhánh đó

Định nghĩa $\beta$ tương tự cho **min**

---
## Thuật toán $
  pha$--$\beta$

Về cơ bản là **Minimax** + theo dõi $
  pha$, $\beta$ + tỉa nhánh

```text
function Max-Value(state, game, $
  pha$, $\beta$) returns giá trị minimax của state
      inputs: state, trạng thái hiện tại trong trò chơi
      inputs: game, mô tả trò chơi
      inputs: $
  pha$, điểm tốt nhất cho **max dọc theo đường đi đến state**
      inputs: $\beta$, điểm tốt nhất cho **min dọc theo đường đi đến state**

    if Cutoff-Test(state) then return Eval(state)
    for each s in Successors(state) do
          $
  pha$ <- Max($
  pha$, Min-Value(s, game, $
  pha$, $\beta$))
          if $
  pha \geq \beta$ then return $\beta$ 
    end
    return $
  pha$
\fnsep
function Min-Value(state, game, $
  pha$, $\beta$) returns giá trị minimax của state

    if Cutoff-Test(state) then return Eval(state)
    for each s in Successors(state) do
          $\beta$ <- Min($\beta$, Max-Value(s, game, $
  pha$, $\beta$))
          if $\beta \leq 
  pha$ then return $
  pha$ 
    end
    return $\beta$
```

---
## Các trò chơi tất định trong thực tế

Cờ đam (Checkers): Chinook đã chấm dứt sự thống trị 40 năm của nhà vô địch thế giới con người Marion
Tinsley vào năm 1994. Đã sử dụng một cơ sở dữ liệu tàn cuộc xác định lối chơi hoàn hảo cho
tất cả các vị trí có từ 8 quân cờ trở xuống trên bàn, tổng cộng
443.748.401.247 vị trí.

Cờ vua (Chess): Deep Blue đã đánh bại nhà vô địch thế giới con người Gary Kasparov
trong một trận đấu sáu ván vào năm 1997. Deep Blue tìm kiếm 200 triệu vị trí
mỗi giây, sử dụng đánh giá rất tinh vi và các phương pháp không được tiết lộ để
mở rộng một số nhánh tìm kiếm lên đến 40 lượt (40 ply).

Othello: các nhà vô địch con người từ chối thi đấu với máy tính, vì chúng
quá giỏi.

Cờ vây (Go): các nhà vô địch con người từ chối thi đấu với máy tính, vì chúng quá
tệ. Trong cờ vây, $b > 300$, vì vậy hầu hết các chương trình sử dụng cơ sở tri thức mẫu (pattern) để
đề xuất các nước đi hợp lý.

---
## Các trò chơi không tất định (Nondeterministic games)

Ví dụ, trong cờ sáu trong (backgammon), việc tung xúc xắc quyết định các nước đi hợp lệ

Ví dụ đơn giản hóa với việc tung đồng xu thay vì tung xúc xắc:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-simple.png)

---
## Thuật toán cho các trò chơi không tất định

**Expectiminimax** đưa ra lối chơi hoàn hảo

Giống hệt như **Minimax**, ngoại trừ việc chúng ta cũng phải xử lý các nút cơ hội (chance nodes):

$\ldots$

\key{if} \var{state} là một nút cơ hội \key{then}
    
   \key{return} trung bình của **ExpectiMinimax-Value** của **Successors**(\var{state})

$\ldots$

Một phiên bản tỉa nhánh $
  pha$--$\beta$ là có thể

nhưng chỉ khi các giá trị ở nút lá bị giới hạn. <u>Tại sao?</u>??

---
## Các trò chơi không tất định trong thực tế

Việc tung xúc xắc làm tăng $b$: có 21 kết quả có thể xảy ra khi tung 2 xúc xắc

Cờ sáu trong (Backgammon) $\approx$ 20 nước đi hợp lệ (có thể lên tới 6.000 với kết quả tung là 1-1)
\[
\mbox{độ sâu}\ 4 = 20 \times (21 \times 20)^3 \approx 1.2\times 10^9
\]

Khi độ sâu tăng lên, xác suất đạt tới một nút cụ thể sẽ co lại
    
$\Rightarrow$ giá trị của việc dự đoán trước (lookahead) bị giảm đi

Tỉa nhánh $
  pha$--$\beta$ ít hiệu quả hơn nhiều

**TDGammon** sử dụng tìm kiếm ở độ sâu 2 + **Eval** rất tốt
    
$\approx$ ở mức độ vô địch thế giới

---
## Bàn luận: Các giá trị chính xác CÓ quan trọng

![Hình ảnh](../TaiLieu/slide_md/figures/chance-evaluation.png)

Hành vi chỉ được bảo toàn qua phép biến đổi *tuyến tính dương* của
**Eval**

Do đó, **Eval** nên tỷ lệ thuận với phần thưởng kỳ vọng (expected payoff)

---
## Tóm tắt

Các trò chơi rất thú vị để nghiên cứu! (và nguy hiểm)

Chúng minh họa một số điểm quan trọng về AI

- sự hoàn hảo là không thể đạt được $\Rightarrow$ phải xấp xỉ

- một ý tưởng hay là nghĩ về việc cần suy nghĩ về điều gì

- sự không chắc chắn ràng buộc việc gán các giá trị cho các trạng thái

Trò chơi đối với AI cũng giống như đua xe grand prix đối với thiết kế ô tô