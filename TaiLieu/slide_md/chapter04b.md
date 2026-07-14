\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Bài toán thỏa mãn ràng buộc (CSP)

## Chương 3, Phần 7 và Chương 4, Phần 4.4

---
## Nội dung

- Các ví dụ về CSP

- Tìm kiếm tổng quát áp dụng cho CSP

- Quay lui (Backtracking)

- Kiểm tra tới (Forward checking)

- Heuristic cho CSP

---
## Bài toán thỏa mãn ràng buộc (CSP)

Bài toán tìm kiếm chuẩn:
  
<u>Trạng thái</u> là một "hộp đen"---một cấu trúc dữ liệu cũ bất kỳ
    
hỗ trợ kiểm tra đích, đánh giá, sinh trạng thái kế tiếp

CSP (Constraint Satisfaction Problems):
  
<u>Trạng thái</u> được định nghĩa bởi các *biến* $V_i$
   có *giá trị* thuộc *miền giá trị* $D_i$
  
\ 
  
<u>Kiểm tra đích</u> là một tập hợp các *ràng buộc* quy định
    
   các tổ hợp giá trị cho phép đối với các tập con của các biến

Ví dụ đơn giản về một *ngôn ngữ biểu diễn hình thức*

Cho phép các thuật toán *đa năng* hữu ích có sức mạnh lớn hơn

các thuật toán tìm kiếm tiêu chuẩn

---
## Ví dụ: Bài toán 4 quân hậu dưới dạng CSP

Giả sử mỗi cột có một quân hậu. Mỗi quân hậu sẽ nằm ở hàng nào?

<u>Các biến</u> $Q_1$, $Q_2$, $Q_3$, $Q_4$ 

<u>Miền giá trị</u> $D_i = \{1,2,3,4\}$

<u>Các ràng buộc</u>
  
$Q_i \neq Q_j$ (không thể ở cùng hàng)
  
$|Q_i - Q_j| \neq |i-j|$ (hoặc cùng đường chéo)

 
in
![Hình ảnh](../TaiLieu/slide_md/figures/4queens.png)

Dịch mỗi ràng buộc thành tập các giá trị cho phép đối với các biến của nó

Ví dụ: các giá trị cho $(Q_1,Q_2)$ là 
$(1,3)\ (1,4)\ (2,4)\ (3,1)\ (4,1)\ (4,2)$

---
## Đồ thị ràng buộc

*CSP nhị phân (Binary CSP)*: mỗi ràng buộc liên kết tối đa hai biến

*Đồ thị ràng buộc*: các nút là các biến, các cung thể hiện các ràng buộc

![Hình ảnh](../TaiLieu/slide_md/figures/4queens-graph.png)

---
## Ví dụ: Số học mật mã (Cryptarithmetic)

<u>Các biến</u>
  
$D\ E\ M\ N\ O\ R\ S\ Y$

<u>Miền giá trị</u>
  
$\{0,1,2,3,4,5,6,7,8,9\}$

 

  S E N D

+ M O R E

\hline
M O N E Y

<u>Các ràng buộc</u>
  
$M\neq 0$, $S\neq 0$ (*ràng buộc một ngôi*)
  
$Y = D+E$ hoặc $Y=D+E-10$, v.v.
  
$D\neq E$, $D\neq M$, $D\neq N$, v.v.

---
## Ví dụ: Tô màu bản đồ

Tô màu một bản đồ sao cho không có hai quốc gia kề nhau nào có cùng màu

<u>Các biến</u>
  
Các quốc gia $C_i$

<u>Miền giá trị</u>
  
$\{Đỏ, Xanh\ dương, Xanh\ lá\}$

<u>Các ràng buộc</u>
  
$C_1 \neq C_2$, $C_1 \neq C_5$, v.v.

 
in
![Hình ảnh](../TaiLieu/slide_md/figures/map-coloring.png)

Đồ thị ràng buộc:

 
in
\raisebox{-2.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/map-coloring-graph.png)}

---
## Các CSP trong thế giới thực

Bài toán phân công
  
    ví dụ: ai dạy lớp nào

Bài toán xếp thời khóa biểu
  
    ví dụ: lớp nào được cung cấp khi nào và ở đâu?

Cấu hình phần cứng

Bảng tính (Spreadsheets)

Lập lịch vận tải

Lập lịch nhà máy

Thiết kế sơ đồ mặt bằng (Floorplanning)

Lưu ý rằng nhiều bài toán trong thế giới thực liên quan đến các biến có giá trị thực

---
## Áp dụng tìm kiếm tiêu chuẩn

Hãy bắt đầu với một phương pháp đơn giản, ngốc nghếch, sau đó sửa chữa nó

Các trạng thái được xác định bởi các giá trị đã được gán cho đến hiện tại

<u>Trạng thái ban đầu</u>: tất cả các biến đều chưa được gán

<u>Toán tử</u>: gán một giá trị cho một biến chưa được gán

<u>Kiểm tra đích</u>: tất cả các biến đã được gán, không có ràng buộc nào bị vi phạm

Lưu ý rằng điều này giống nhau đối với tất cả các CSP!

---
## Cài đặt

Trạng thái CSP theo dõi các biến nào đã có giá trị cho đến thời điểm hiện tại

Mỗi biến có một miền và một giá trị hiện tại

```text
datatype CSP-State
    components: Unassigned, danh sách các biến chưa được gán
            Assigned, danh sách các biến đã có giá trị

datatype CSP-Var
    components: Name, phục vụ cho mục đích i/o
            Domain, danh sách các giá trị có thể
            Value, giá trị hiện tại (nếu có)
```

Các ràng buộc có thể được biểu diễn
  
<u>rõ ràng</u> dưới dạng tập hợp các giá trị cho phép, hoặc
  
<u>ngầm định</u> bởi một hàm kiểm tra sự thỏa mãn ràng buộc

---
## Tìm kiếm tiêu chuẩn áp dụng cho tô màu bản đồ

![Hình ảnh](../TaiLieu/slide_md/figures/map-coloring-tree.png)

---
## Độ phức tạp của phương pháp ngốc nghếch

<u>Độ sâu tối đa của không gian $m = {</u>??$}

<u>Độ sâu của trạng thái đích $d = {</u>??$}

<u>Thuật toán tìm kiếm sử dụng</u>??

<u>Hệ số phân nhánh $b = {</u>??$}

Điều này có thể được cải thiện đáng kể bằng cách lưu ý những điều sau:

1) Thứ tự gán không quan trọng, do đó nhiều đường đi là tương đương nhau

2) Việc thêm các phép gán không thể khắc phục một ràng buộc đã bị vi phạm

---
## Độ phức tạp của phương pháp ngốc nghếch

<u>Độ sâu tối đa của không gian $m = {</u>??$} $n$ (số lượng biến)

<u>Độ sâu của trạng thái đích $d = {</u>??$} $n$ (tất cả các biến đều được gán)

<u>Thuật toán tìm kiếm sử dụng</u>?? tìm kiếm theo chiều sâu (depth-first)

<u>Hệ số phân nhánh $b = {</u>??$} $\mysum_i |D_i|$ (ở trên cùng của cây)

Điều này có thể được cải thiện đáng kể bằng cách lưu ý những điều sau:

1) Thứ tự gán không quan trọng, do đó nhiều đường đi là tương đương nhau

2) Việc thêm các phép gán không thể khắc phục một ràng buộc đã bị vi phạm

---
## Tìm kiếm quay lui (Backtracking search)

Sử dụng tìm kiếm theo chiều sâu, nhưng
  
1) cố định thứ tự gán, ${} \implies b = |D_i|$
    
   (có thể được thực hiện trong hàm **Successors**)
  
2) kiểm tra sự vi phạm ràng buộc

Kiểm tra vi phạm ràng buộc có thể được thực hiện theo hai cách:
  
1) sửa đổi hàm **Successors** để chỉ gán những giá trị
    
   được phép, với những giá trị đã được gán trước đó
  
hoặc 2) kiểm tra các ràng buộc có được thỏa mãn trước khi phát triển một trạng thái

Tìm kiếm quay lui là thuật toán không có thông tin cơ bản cho các CSP

Có thể giải bài toán $n$-quân hậu với $n \approx 15$

---
## Kiểm tra tới (Forward checking)

<u>Ý tưởng</u>: Theo dõi các giá trị hợp lệ còn lại cho các biến chưa được gán

\phantom{<u>Ý tưởng</u>: }Dừng tìm kiếm khi bất kỳ biến nào không còn giá trị hợp lệ nào

Ví dụ tô màu bản đồ được đơn giản hóa:

\hline
   **đỏ**   **xanh\ dương**   **xanh\ lá** 

\hline
$C_1$          

\hline
$C_2$          

\hline
$C_3$          

\hline
$C_4$          

\hline
$C_5$          

\hline

&
in
\raisebox{-1in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/map-coloring2.png)}

Có thể giải bài toán $n$-quân hậu lên đến $n \approx 30$

\pheading{}

.

.

.

\hline
   \phantom{**đỏ**}   \phantom{**xanh\ dương**}   \phantom{**xanh\ lá**} 

\hline
\phantom{$C_1$}   \tick        

\hline
\phantom{$C_2$}   \cross       

\hline
\phantom{$C_3$}          

\hline
\phantom{$C_4$}   \cross       

\hline
\phantom{$C_5$}   \cross       

\hline

&

\pheading{}

.

.

.

\hline
   \phantom{**đỏ**}   \phantom{**xanh\ dương**}   \phantom{**xanh\ lá**} 

\hline
\phantom{$C_1$}          

\hline
\phantom{$C_2$}      \tick    

\hline
\phantom{$C_3$}      \cross    

\hline
\phantom{$C_4$}      \cross    

\hline
\phantom{$C_5$}      \cross    

\hline

&

\pheading{}

.

.

.

\hline
   \phantom{**đỏ**}   \phantom{**xanh\ dương**}   \phantom{**xanh\ lá**} 

\hline
\phantom{$C_1$}          

\hline
\phantom{$C_2$}          

\hline
\phantom{$C_3$}         \tick 

\hline
\phantom{$C_4$}          

\hline
\phantom{$C_5$}         \cross 

\hline

&

---
## Heuristic cho CSP

Các quyết định thông minh hơn về việc
  
chọn giá trị nào cho mỗi biến
  
biến nào sẽ được gán tiếp theo

<u>Cho $C_1 \eq Đỏ$, $C_2 \eq Xanh\ lá$, chọn $C_3 \eq$</u>??
  
.

<u>Cho $C_1 \eq Đỏ$, $C_2 \eq Xanh\ lá$, tiếp theo chọn biến nào</u>??
  
.

 
in
![Hình ảnh](../TaiLieu/slide_md/figures/map-coloring.png)

Có thể giải bài toán $n$-quân hậu cho $n \approx 1000$

---
## Heuristic cho CSP

Các quyết định thông minh hơn về việc
  
chọn giá trị nào cho mỗi biến
  
biến nào sẽ được gán tiếp theo

<u>Cho $C_1 \eq Đỏ$, $C_2 \eq Xanh\ lá$, chọn $C_3 \eq$</u>??
  
$C_3 \eq Xanh\ lá$: *giá-trị-ràng-buộc-ít-nhất (least-constraining-value)*

<u>Cho $C_1 \eq Đỏ$, $C_2 \eq Xanh\ lá$, tiếp theo chọn biến nào</u>??
  
$C_5$: *biến-bị-ràng-buộc-nhiều-nhất (most-constrained-variable)*

 
in
![Hình ảnh](../TaiLieu/slide_md/figures/map-coloring.png)

Có thể giải bài toán $n$-quân hậu cho $n \approx 1000$

---
## Thuật toán lặp cho CSP

Leo đồi, luyện kim mô phỏng thường hoạt động với

các trạng thái "đầy đủ", tức là tất cả các biến đã được gán

Để áp dụng cho CSP:
  
cho phép các trạng thái với các ràng buộc không được thỏa mãn
  
toán tử *gán lại* (reassign) các giá trị của biến

Lựa chọn biến: chọn ngẫu nhiên bất kỳ biến nào đang có xung đột

<u>Heuristic *xung-đột-nhỏ-nhất</u> (min-conflicts)*:
  
chọn giá trị vi phạm ít ràng buộc nhất
  
tức là leo đồi với $h(n)$ = tổng số ràng buộc bị vi phạm

---
## Ví dụ: Bài toán 4 quân hậu

<u>Trạng thái</u>: 4 quân hậu trong 4 cột (có $4^4 = 256$ trạng thái)

<u>Toán tử</u>: di chuyển quân hậu trong cột

<u>Kiểm tra đích</u>: không có sự tấn công nào

<u>Đánh giá</u>: $h(n)$ = số lượng các cuộc tấn công

![Hình ảnh](../TaiLieu/slide_md/figures/4queens-iterative.png)

---
## Hiệu suất của min-conflicts

Với trạng thái khởi tạo ngẫu nhiên, có thể giải bài toán $n$-quân hậu trong thời gian
gần như hằng số đối với bất kỳ $n$ nào với xác suất cao (ví dụ: $n$ = 10,000,000)

Điều tương tự có vẻ cũng đúng cho bất kỳ CSP được sinh ngẫu nhiên nào

<u>ngoại trừ</u> trong một phạm vi hẹp của tỷ lệ
\[
R = \frac{\mbox{số lượng ràng buộc}}{\mbox{số lượng biến}}
\]

![Hình ảnh](../TaiLieu/slide_md/figures/random-csp-runtime.png)

---
## CSP có cấu trúc cây (Tree-structured CSPs)

![Hình ảnh](../TaiLieu/slide_md/figures/abcdef-graph.png)

<u>Định lý</u>: nếu đồ thị ràng buộc không có vòng lặp (loop), CSP có thể được giải trong 
thời gian $O(n|D|^2)$

So sánh với các CSP tổng quát, nơi thời gian xấu nhất là $O(|D|^n)$

Thuộc tính này cũng áp dụng cho suy luận logic và xác suất:

một ví dụ quan trọng về mối quan hệ giữa
những hạn chế về cú pháp và độ phức tạp của suy luận.

---
## Thuật toán cho các CSP có cấu trúc cây

Bước cơ bản được gọi là *lọc (filtering)*:

$**Filter**(V_i,\, V_j)$
  
loại bỏ các giá trị của $V_i$ không nhất quán với TẤT CẢ các giá trị của $V_j$

Ví dụ về lọc:

![Hình ảnh](../TaiLieu/slide_md/figures/csp-filter.png)

---
## Thuật toán (tiếp)

![Hình ảnh](../TaiLieu/slide_md/figures/abcdef-graph.png)

1) Sắp xếp các nút theo chiều rộng (breadth-first) bắt đầu từ bất kỳ nút lá nào:

![Hình ảnh](../TaiLieu/slide_md/figures/abcdef-ordered.png)

2) Đối với $j = n$ giảm xuống $1$, áp dụng $**Filter**(V_i,\, V_j)$
trong đó $V_i$ là nút cha của $V_j$

3) Đối với $j = 1$ tăng lên $n$, chọn giá trị hợp lệ cho $V_j$ với giá trị của nút cha đã cho

---
## Tóm tắt

CSP là một loại bài toán đặc biệt:
  
trạng thái được xác định bằng các giá trị của một tập hợp các biến cố định
  
kiểm tra đích được xác định bởi các *ràng buộc* trên giá trị của các biến

Quay lui (Backtracking) = tìm kiếm theo chiều sâu với
  
1) thứ tự biến cố định
  
2) chỉ có các trạng thái kế tiếp hợp lệ

Kiểm tra tới (Forward checking) ngăn chặn các phép gán chắc chắn dẫn đến thất bại sau này

Heuristic để chọn thứ tự biến và chọn giá trị giúp ích đáng kể

Cải tiến lặp min-conflicts <u>thường</u> có hiệu quả trong thực tế

Các CSP có cấu trúc cây <u>luôn luôn</u> có thể được giải quyết rất hiệu quả