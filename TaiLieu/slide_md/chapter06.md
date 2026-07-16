\usepackage{fleqn}
\usepackage{epsf}
\usepackage{color}
\usepackage{aima2e-slides}

# Chơi trò chơi (Game playing)

## Chương 6

---
## Phác thảo

- Trò chơi

- Lối chơi hoàn hảo
    
-- quyết định tối đa 
    
-- $
  pha$--$\beta$ cắt tỉa

- Giới hạn tài nguyên và đánh giá gần đúng

- Trò chơi may rủi

- Trò chơi thông tin không hoàn hảo

---
## Trò chơi và  vấn đề tìm kiếm

Giải pháp "Không thể đoán trước" đối thủ $\Rightarrow$ là \note{chiến lược}

chỉ định một nước đi cho mọi câu trả lời có thể có của đối thủ

Giới hạn thời gian $\Rightarrow$ khó có thể tìm được mục tiêu, phải xấp xỉ

Kế hoạch tấn công:
\begin{itemize}
\item Máy tính xem xét các lối chơi có thể có (Babbage, 1846)
\item Thuật toán chơi hoàn hảo (Zermelo, 1912; Von Neumann, 1944)
\item Chân trời hữu hạn, đánh giá gần đúng (Zuse, 1945; Wiener, 1948; 

      Shannon, 1950)
\item Chương trình cờ vua đầu tiên (Turing, 1951)
\item Học máy để nâng cao độ chính xác trong đánh giá (Samuel, 1952--57)
\item Cắt tỉa để cho phép tìm kiếm sâu hơn (McCarthy, 1956)
\end{itemize}

---
## Các loại trò chơi

![Hình ảnh](../TaiLieu/slide_md/figures/game-types.png)

---
## Cây trò chơi (2 người chơi, xác định, lượt)

![Hình ảnh](../TaiLieu/slide_md/figures/tictactoe.png)

---
## Cực tiểu

Chơi hoàn hảo cho các trò chơi xác định, thông tin hoàn hảo

Ý tưởng: chọn di chuyển đến vị trí có giá trị \defn{minimax cao nhất}
    
= phần thưởng tốt nhất có thể đạt được khi chơi tốt nhất

Ví dụ: trò chơi 2 lớp:

![Hình ảnh](../TaiLieu/slide_md/figures/minimax.png)

---
## Thuật toán Minimax

```text
function Minimax-Decision(state) returns an action
      inputs: state, current state in game

    return the a in Actions(state) maximizing Min-Value(Result(a, state))
\fnsep
function Max-Value(state) returns a utility value
    if Terminal-Test(state) then return Utility(state)
    v <- \(-infinity\)
    for a, s in Successors(state) do v <- Max(v, Min-Value(s))
    return v
\fnsep
function Min-Value(state) returns a utility value
    if Terminal-Test(state) then return Utility(state)
    v <- \(infinity\)
    for a, s in Successors(state) do v <- Min(v, Max-Value(s))
    return v
```

---
## Tính chất của minimax

<u>Hoàn thành</u>?? 

---
## Tính chất của minimax

<u>Hoàn thành</u>?? Chỉ khi cây là hữu hạn (cờ vua có các quy tắc cụ thể cho việc này).
    
NB một chiến lược hữu hạn có thể tồn tại ngay cả trong một cây vô hạn!

<u>Tối ưu</u>?? 

---
## Tính chất của minimax

<u>Complete</u>?? Có, nếu cây hữu hạn (cờ vua có các quy tắc cụ thể cho việc này)

<u>Tối ưu</u>?? Có, chống lại đối thủ tối ưu. Nếu không thì??

<u>Độ phức tạp về thời gian</u>?? 

---
## Tính chất của minimax

<u>Complete</u>?? Có, nếu cây hữu hạn (cờ vua có các quy tắc cụ thể cho việc này)

<u>Tối ưu</u>?? Có, chống lại đối thủ tối ưu. Nếu không thì??

<u>Độ phức tạp về thời gian</u>?? \mat{$O(b^m)$}

<u>Độ phức tạp của không gian</u>?? 

---
## Tính chất của minimax

<u>Complete</u>?? Có, nếu cây hữu hạn (cờ vua có các quy tắc cụ thể cho việc này)

<u>Tối ưu</u>?? Có, chống lại đối thủ tối ưu. Nếu không thì??

<u>Độ phức tạp về thời gian</u>?? \mat{$O(b^m)$}

<u>Độ phức tạp của không gian</u>?? \mat{$O(bm)$} (khám phá theo chiều sâu)

Đối với cờ vua, \mat{$b\approx 35$}, \mat{$m \approx 100$} dành cho các trò chơi "hợp lý"
    
$\Rightarrow$ giải pháp chính xác hoàn toàn không khả thi

Nhưng chúng ta có cần khám phá mọi con đường không?

---
## $
  pha$--$\beta$ ví dụ về cắt tỉa

$\beta$

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress1.png)

---
## $
  pha$--$\beta$ ví dụ về cắt tỉa

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress2.png)

---
## $
  pha$--$\beta$ ví dụ về cắt tỉa

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress3.png)

---
## $
  pha$--$\beta$ ví dụ về cắt tỉa

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress4.png)

---
## $
  pha$--$\beta$ ví dụ về cắt tỉa

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-progress5.png)

---
## Tại sao lại gọi là $
  pha$--

![Hình ảnh](../TaiLieu/slide_md/figures/alpha-beta-general.png)

\mat{$
  pha$} là giá trị tốt nhất (đến **max**) được tìm thấy ở xa đường dẫn hiện tại

Nếu \mat{$V$} tệ hơn \mat{$
  pha$}, **max** sẽ tránh được
$\Rightarrow$ Tỉa cành đó đi

Xác định \mat{$\beta$} tương tự cho **min**

---
## Thuật toán $
  pha$--

```text
function Alpha-Beta-Decision(state) returns an action
    return the a in Actions(state) maximizing Min-Value(Result(a, state))
\fnsep
function Max-Value(state, \(
  pha\), \(\beta\)) returns a utility value
      inputs: state, current state in game
      inputs: \(
  pha\), the value of the best alternative for **max along the path to state**
      inputs: \(\beta\), the value of the best alternative for **min along the path to state**

    if Terminal-Test(state) then return Utility(state)
    v <- \(-infinity\)
    for a, s in Successors(state) do
        v <- Max(v, Min-Value(s, \(
  pha\), \(\beta\)))
        if \(v \ge \beta\) then return v
        \(
  pha\) <- Max(\(
  pha\), v)
    return v
\fnsep
function Min-Value(state, \(
  pha\), \(\beta\)) returns a utility value
    same as Max-Value but with roles of \(
  pha\), \(\beta\) reversed
```

---
## Thuộc tính của $
  pha$--$\beta$

Cắt tỉa *không * ảnh hưởng đến kết quả cuối cùng

Thứ tự di chuyển tốt sẽ nâng cao hiệu quả của việc cắt tỉa

Với "thứ tự hoàn hảo", độ phức tạp về thời gian = \mat{$O(b^{m/2})$}
    
$\Rightarrow$ *tăng gấp đôi* độ sâu có thể giải được

Một ví dụ đơn giản về giá trị của lý luận về điều gì 
các tính toán có liên quan (một dạng \note{siêu lý luận})

Thật không may, \mat{$35^{50}$} vẫn không thể thực hiện được!

---
## Giới hạn tài nguyên

Cách tiếp cận tiêu chuẩn:
\begin{itemize}
\item Sử dụng **Cutoff-Test** thay vì **Terminal-Test
    
ví dụ: giới hạn độ sâu (có thể thêm \defn{tìm kiếm tĩnh **)
\item Sử dụng **Eval** thay vì **Utility
    
tức là, \defn{hàm đánh giá ** ước tính mức độ mong muốn của vị trí
\end{itemize}

Giả sử chúng ta có \mat{$100$} giây, hãy khám phá \mat{$10^4$} nút/giây
    
$\Rightarrow$ \mat{$10^6$} nút mỗi lần di chuyển $\approx$ \mat{$35^{8/2}$}
    
$\Rightarrow$ $
  pha$--$\beta$ đạt độ sâu 8 $\Rightarrow$ chương trình cờ vua khá hay

---
## Chức năng đánh giá

![Hình ảnh](../TaiLieu/slide_md/figures/chess-evaluation-bc.png)

Đối với cờ vua, thường là tổng trọng số \note{tuyến tính} của \defn{features}
\mat{\[
**Eval**(s) = w_1 f_1(s) + w_2 f_2(s) + \ldots + w_n f_n(s)
\]}
ví dụ: \mat{$w_1 = 9$} với 

\mat{$f_1(s)$} = (số quân hậu trắng) -- (số quân hậu đen),\ \ v.v.

---
## Lạc đề: Giá trị chính xác không quan trọng

![Hình ảnh](../TaiLieu/slide_md/figures/ordinal-utility.png)

Hành vi được bảo toàn dưới bất kỳ phép biến đổi *đơn điệu* nào của
**Đánh giá**

Chỉ có thứ tự là quan trọng:
    
phần thưởng trong trò chơi xác định đóng vai trò như một hàm \defn{tiện ích thứ tự}

---
## Trò chơi xác định trong thực tế

Cờ đam: Chinook chấm dứt 40 năm thống trị của nhà vô địch thế giới loài người Marion
Tinsley vào năm 1994. Đã sử dụng cơ sở dữ liệu tàn cuộc để xác định cách chơi hoàn hảo cho
tất cả các vị trí liên quan đến 8 quân cờ trở xuống trên bàn cờ, tổng cộng
443.748.401.247 vị trí.

Cờ vua: Deep Blue đánh bại nhà vô địch thế giới loài người Gary Kasparov
trong một trận đấu sáu ván vào năm 1997. Deep Blue tìm kiếm 200 triệu vị trí
mỗi giây, sử dụng sự đánh giá rất phức tạp và các phương pháp chưa được tiết lộ để
mở rộng một số dòng tìm kiếm lên tới 40 lớp.

Othello: những nhà vô địch của con người từ chối cạnh tranh với máy tính, những kẻ
quá tốt.

Đi: những nhà vô địch của con người từ chối cạnh tranh với máy tính, những người cũng vậy
tệ. Trong go, $b > 300$, vì vậy hầu hết các chương trình đều sử dụng cơ sở kiến thức mẫu để
đề xuất những động thái hợp lý.

---
## Trò chơi không xác định: cờ thỏ cáo

![Hình ảnh](../TaiLieu/slide_md/figures/backgammon-position.png)

---
## Trò chơi không xác định nói chung

Trong các trò chơi không xác định, cơ hội được tạo ra bởi xúc xắc, xáo bài

Ví dụ đơn giản hóa với việc lật đồng xu:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-simple.png)

---
## Thuật toán cho trò chơi không xác định

**Expectiminimax** chơi hoàn hảo

Giống như **Minimax**, ngoại trừ việc chúng ta cũng phải xử lý các nút ngẫu nhiên:

$\ldots$

\key{if} \var{state} là một nút **Max** \key{then
    
   \key{return} **ExpectiMinimax-Value** cao nhất trong số **Successors**(\var{state})

\key{if} \var{state} là một nút **Min** \key{then
    
   \key{return} **ExpectiMinimax-Value** thấp nhất của **Successors**(\var{state})

\key{if} \var{state} là một nút cơ hội \key{then
    
   \key{return} trung bình của **ExpectiMinimax-Value** của **Successors**(\var{state})

$\ldots$

---
## Trò chơi bất định trong thực tế

Tăng xúc xắc $b$: 21 lần tung xúc xắc có thể có 2 xúc xắc

Backgammon $\approx$ 20 nước đi hợp pháp (có thể là 6.000 với 1-1 lần tung)
\[
{\rm depth}\ 4 = 20 \times (21 \times 20)^3 \approx 1.2\times 10^9
\]

Khi độ sâu tăng lên, xác suất tiếp cận một nút nhất định sẽ giảm 
    
$\Rightarrow$ giá trị của lookahead bị giảm đi

$
  pha$--$\beta$ việc cắt tỉa kém hiệu quả hơn nhiều

**TDGammon** sử dụng tìm kiếm theo độ sâu 2 + rất tốt **Eval
    
$\approx$ cấp độ vô địch thế giới

---
## Lạc đề: Giá trị chính xác DO quan trọng**

 của
**Đánh giá**

Do đó **Eval** phải tỷ lệ thuận với mức hoàn trả dự kiến

---
## Trò chơi thông tin không hoàn hảo

Ví dụ: trò chơi bài, trong đó quân bài đầu tiên của đối thủ không xác định được

Thông thường chúng ta có thể tính toán xác suất cho mỗi giao dịch có thể xảy ra

Có vẻ giống như có một lần tung xúc xắc lớn vào đầu trò chơi\mat{$^*$}

\note{Idea}: tính giá trị tối thiểu của từng hành động trong mỗi giao dịch,
    
   sau đó chọn hành động có giá trị mong đợi cao nhất trong tất cả các giao dịch\mat{$^*$}

Trường hợp đặc biệt: nếu một hành động là tối ưu cho tất cả các giao dịch thì đó là hành động tối ưu.\mat{$^*$}

GIB, chương trình cầu nối tốt nhất hiện nay, gần đúng với ý tưởng này bằng 
  
1) tạo 100 giao dịch phù hợp với thông tin đấu thầu
  
2) chọn hành động thắng trung bình hầu hết các thủ thuật 

---
## Ví dụ

Bài bốn lá bài/tay bài huýt sáo/trái tim, **Max** chơi trước

![Hình ảnh](../TaiLieu/slide_md/figures/card-tree1.png)

---
## Ví dụ

Bài bốn lá bài/tay bài huýt sáo/trái tim, **Max** chơi trước

![Hình ảnh](../TaiLieu/slide_md/figures/card-tree2.png)

---
## Ví dụ

Bài bốn lá bài/tay bài huýt sáo/trái tim, **Max** chơi trước

![Hình ảnh](../TaiLieu/slide_md/figures/card-tree3.png)

---
## Ví dụ thông thường

Đường A dẫn tới một đống vàng nhỏ

Đường B dẫn tới một ngã ba:
    
   rẽ trái và bạn sẽ tìm thấy một đống đá quý;
    
   rẽ phải và bạn sẽ bị xe buýt cán qua.

---
## Ví dụ thông thường

Đường A dẫn tới một đống vàng nhỏ

Đường B dẫn tới một ngã ba:
    
   rẽ trái và bạn sẽ tìm thấy một đống đá quý;
    
   rẽ phải và bạn sẽ bị xe buýt cán qua.

Đường A dẫn tới một đống vàng nhỏ

Đường B dẫn tới một ngã ba:
    
   rẽ trái và bạn sẽ bị xe buýt cán qua;
    
   lấy cái nĩa bên phải và bạn sẽ tìm thấy một đống đồ trang sức.

---
## Ví dụ thông thường

Đường A dẫn tới một đống vàng nhỏ

Đường B dẫn tới một ngã ba:
    
   rẽ trái và bạn sẽ tìm thấy một đống đá quý;
    
   rẽ phải và bạn sẽ bị xe buýt cán qua.

Đường A dẫn tới một đống vàng nhỏ

Đường B dẫn tới một ngã ba:
    
   rẽ trái và bạn sẽ bị xe buýt cán qua;
    
   lấy cái nĩa bên phải và bạn sẽ tìm thấy một đống đồ trang sức.

Đường A dẫn tới một đống vàng nhỏ

Đường B dẫn tới một ngã ba:
    
   đoán đúng và bạn sẽ tìm thấy một đống ngọc;
    
   đoán sai và bạn sẽ bị xe buýt cán qua.

---
## Phân tích thích hợp

\mat{*} Trực giác rằng giá trị của một hành động là trung bình của các giá trị của nó

ở tất cả các trạng thái thực tế là *WRONG*

Với khả năng quan sát một phần, giá trị của một hành động phụ thuộc vào 

\defn{trạng thái thông tin} hoặc \defn{trạng thái niềm tin} tác nhân đang ở

Có thể tạo và tìm kiếm một cây trạng thái thông tin

Dẫn đến những hành vi hợp lý như 
  
- Hành động để lấy thông tin
  
- Ra hiệu cho đồng đội
  
- Hành động ngẫu nhiên để giảm thiểu tiết lộ thông tin

---
## Tóm tắt

Trò chơi rất thú vị để làm việc! (và nguy hiểm)

Chúng minh họa một số điểm quan trọng về AI

- sự hoàn hảo là không thể đạt được $\Rightarrow$ phải gần đúng

- suy nghĩ về điều cần suy nghĩ là một ý tưởng hay

- sự không chắc chắn hạn chế việc gán giá trị cho các trạng thái

- quyết định tối ưu phụ thuộc vào trạng thái thông tin, không phải trạng thái thực

Trò chơi dành cho AI cũng như giải đua xe lớn dành cho thiết kế ô tô

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning1.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning2.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning3.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning4.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning5.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning6.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning7.png)

---
## Cắt tỉa cây trò chơi không xác định

Có thể sử dụng phiên bản cắt tỉa $
  pha$-$\beta$:

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-pruning8.png)

---
## Tiếp tục cắt tỉa

Việc cắt tỉa xảy ra nhiều hơn nếu chúng ta có thể ràng buộc các giá trị lá

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-bounded1.png)

---
## Tiếp tục cắt tỉa

Việc cắt tỉa xảy ra nhiều hơn nếu chúng ta có thể ràng buộc các giá trị lá

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-bounded2.png)

---
## Tiếp tục cắt tỉa

Việc cắt tỉa xảy ra nhiều hơn nếu chúng ta có thể ràng buộc các giá trị lá

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-bounded3.png)

---
## Tiếp tục cắt tỉa

Việc cắt tỉa xảy ra nhiều hơn nếu chúng ta có thể ràng buộc các giá trị lá

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-bounded4.png)

---
## Tiếp tục cắt tỉa

Việc cắt tỉa xảy ra nhiều hơn nếu chúng ta có thể ràng buộc các giá trị lá

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-bounded5.png)

---
## Tiếp tục cắt tỉa

Việc cắt tỉa xảy ra nhiều hơn nếu chúng ta có thể ràng buộc các giá trị lá

![Hình ảnh](../TaiLieu/slide_md/figures/expectiminimax-bounded6.png)