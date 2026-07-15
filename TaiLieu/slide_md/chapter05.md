\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Bài toán Thỏa mãn Ràng buộc (Constraint Satisfaction Problems)

## Chương 5

---
## Phác thảo

- Ví dụ về CSP

- Tìm kiếm quay lui cho CSP

- Cấu trúc vấn đề và phân rã vấn đề

- Tìm kiếm cục bộ cho CSP

---
## Các vấn đề về sự thỏa mãn ràng buộc (CSP)

Vấn đề tìm kiếm tiêu chuẩn:
  
\note{state} là một "hộp đen"---bất kỳ cấu trúc dữ liệu cũ nào
    
hỗ trợ kiểm tra mục tiêu, đánh giá, kế thừa

CSP:
  
\note{state} được xác định bởi \defn{variables} \mat{$X_i$}
   với \defn{giá trị} từ \defn{miền} \mat{$D_i$}
  
\ 
  
\note{kiểm tra mục tiêu} là một tập hợp các \defn{ràng buộc} chỉ định
    
   sự kết hợp các giá trị được phép cho các tập hợp con của biến

Ví dụ đơn giản về *ngôn ngữ biểu diễn hình thức*

Cho phép các thuật toán *có mục đích chung * hữu ích với nhiều sức mạnh hơn 

hơn các thuật toán tìm kiếm tiêu chuẩn

---
## Ví dụ: Tô màu bản đồ

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/australia.png)

\note{Biến} \mat{$WA$}, \mat{$NT$}, \mat{$Q$}, \mat{$NSW$}, \mat{$V$}, \mat{$SA$}, \mat{$T$} 

\note{Miền} \mat{$D_i = \{red,green,blue\}$}

\note{Ràng buộc}: các vùng liền kề phải có màu khác nhau
  
ví dụ: \mat{$WA\neq NT$} (nếu ngôn ngữ cho phép điều này) hoặc 
  
\mat{$(WA,NT) \in \{(red,green),(red,blue),(green,red),(green,blue),\ldots\}$}

---
## Ví dụ: Tiếp theo tô màu bản đồ.

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/australia-solution.png)

\note{Giải pháp} là các bài tập đáp ứng tất cả các ràng buộc, ví dụ:

\mat{$\{WA\eq red,NT\eq green,Q\eq red,NSW\eq green,V\eq red,SA\eq blue,T\eq green\}$}

---
## Biểu đồ ràng buộc

\defn{CSP nhị phân}: mỗi ràng buộc liên quan đến nhiều nhất hai biến

\defn{Biểu đồ ràng buộc}: các nút là các biến, các cung hiển thị các ràng buộc

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/australia-csp.png)

Các thuật toán CSP có mục đích chung sử dụng cấu trúc biểu đồ

để tăng tốc độ tìm kiếm. Ví dụ: Tasmania là một bài toán con độc lập!

---
## Các loại CSP

Biến rời rạc
  
  miền hữu hạn; kích thước \mat{$d$} $\implies$ \mat{$O(d^n)$} hoàn thành bài tập 
    
    - ví dụ: CSP Boolean, bao gồm Khả năng thỏa mãn Boolean (NP-đầy đủ)
  
  miền vô hạn (số nguyên, chuỗi, v.v.)
    
    - ví dụ: lập kế hoạch công việc, các biến là ngày bắt đầu/kết thúc cho mỗi công việc
    
    - cần ngôn ngữ ràng buộc \defn{}, ví dụ: \mat{$StartJob_1 + 5 \leq StartJob_3$}
    
    - \note{ràng buộc tuyến tính} có thể giải quyết được, \note{phi tuyến tính} không thể giải quyết được

Biến liên tục
  
    - ví dụ: thời gian bắt đầu/kết thúc cho các quan sát bằng Kính viễn vọng Hubble
  
    - ràng buộc tuyến tính có thể giải được trong nhiều thời gian bằng phương pháp LP

---
## Các loại ràng buộc

Các ràng buộc \defn{Unary} liên quan đến một biến duy nhất, 
  
   ví dụ: \mat{$SA\neq green$}

Các ràng buộc \defn{Binary} liên quan đến các cặp biến, 
  
   ví dụ: \mat{$SA\neq WA$}

\defn{Ràng buộc bậc cao hơn} liên quan đến 3 biến trở lên,
  
   ví dụ: các ràng buộc cột mật mã

\defn{Preferences} (ràng buộc mềm), ví dụ: \mat{$red$} tốt hơn \mat{$green$}

thường được biểu thị bằng chi phí cho mỗi lần gán biến 
  
$\rightarrow$ các vấn đề tối ưu hóa bị ràng buộc

---
## Ví dụ: Số học mật mã

,85\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/cryptarithmetic.png)

\note{Biến}: \mat{$F\ T\ U\ W\ R\ O\ X_1\ X_2\ X_3$}

\note{Miền}: \mat{$\{0,1,2,3,4,5,6,7,8,9\}$}

\note{Ràng buộc}
  
\mat{$
  ldiff(F,T,U,W,R,O)$}
  
\mat{$O + O = R + 10\cdot X_1$}, v.v.

---
## CSP trong thế giới thực

Vấn đề về bài tập 
  
    ví dụ: ai dạy lớp nào

Vấn đề về thời gian biểu
  
    ví dụ: lớp nào được cung cấp khi nào và ở đâu?

Cấu hình phần cứng

Bảng tính

Lập kế hoạch vận chuyển

Lập kế hoạch nhà máy

quy hoạch sàn

Lưu ý rằng nhiều vấn đề trong thế giới thực liên quan đến các biến có giá trị thực

---
## Công thức tìm kiếm tiêu chuẩn (tăng dần)

Hãy bắt đầu với cách tiếp cận đơn giản, ngu ngốc, sau đó sửa nó

Các trạng thái được xác định bởi các giá trị được gán cho đến nay

- \note{Trạng thái ban đầu}: nhiệm vụ trống, \mat{$\emptyset$}

- \note{Hàm kế tiếp}: gán giá trị cho biến chưa được gán
    
điều đó không xung đột với nhiệm vụ hiện tại.
    
$\implies$ thất bại nếu không có nhiệm vụ pháp lý nào (không thể sửa được!)

- \note{Kiểm tra mục tiêu}: bài tập hiện tại đã hoàn thành

1) Điều này giống nhau đối với tất cả các CSP! \smiley

2) Mọi giải pháp đều xuất hiện ở độ sâu \mat{$n$} với các biến \mat{$n$} 
    
   $\implies$ sử dụng tìm kiếm theo chiều sâu

3) Đường dẫn không liên quan nên cũng có thể sử dụng công thức trạng thái hoàn chỉnh

4) \mat{$b\eq (n-\ell)d$} ở độ sâu \mat{$\ell$}, do đó \mat{$n!d^n$} rời đi!!!! \frowny

---
## Tìm kiếm quay lại

Phép gán biến là \defn{giao hoán}, tức là,
    
 [\mat{$WA\eq red$} rồi \mat{$NT\eq green$}]\ \ giống như \ \ [\mat{$NT\eq green$} rồi \mat{$WA\eq red$}]

Chỉ cần xem xét việc gán cho một biến duy nhất tại mỗi nút
    
   $\implies$ \mat{$b \eq d$} và có \mat{$d^n$} lá
    

Tìm kiếm theo chiều sâu cho CSP với các bài tập một biến 

được gọi là tìm kiếm \defn{quay lại}

Tìm kiếm quay lui là thuật toán cơ bản chưa được hiểu rõ cho CSP

Có thể giải \mat{$n$}-quân hậu cho \mat{$n \approx 25$}

---
## Tìm kiếm quay lại

```text
function Backtracking-Search(csp) returns solution/failure
    return Recursive-Backtracking(\(\{, \}\), csp)

function Recursive-Backtracking(assignment, csp) returns soln/failure
    if assignment is complete then return assignment
    var <- Select-Unassigned-Variable(Variables[csp], assignment, csp)
    for each value in Order-Domain-Values(var, assignment, csp) do
          if value is consistent with assignment given Constraints[csp] then
                add \{var = value\} to assignment
                result <- Recursive-Backtracking(assignment, csp)
                if result \(!=\) failure then return result
                remove \{var = value\} from assignment
    return failure
```

---
## Ví dụ quay lui

,95\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/backtrack-progress1.png)

---
## Ví dụ quay lui

,95\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/backtrack-progress2.png)

---
## Ví dụ quay lui

,95\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/backtrack-progress3.png)

---
## Ví dụ quay lui

,95\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/backtrack-progress4.png)

---
## Cải thiện hiệu quả quay lui

Các phương pháp *Mục đích chung* có thể mang lại tốc độ rất lớn:
\begin{enumerate}
\item Biến nào sẽ được gán tiếp theo?
\item Nên thử các giá trị của nó theo thứ tự nào?
\item Liệu chúng ta có thể phát hiện sớm những thất bại không thể tránh khỏi được không?
\item Chúng ta có thể tận dụng được cấu trúc bài toán không?
\end{enumerate}

---
## Giá trị còn lại tối thiểu

Giá trị còn lại tối thiểu (MRV):
  
   chọn biến có giá trị pháp lý nhỏ nhất

![Hình ảnh](../TaiLieu/slide_md/figures/australia-most-constrained-variable.png)

---
## Bậc heuristic

Sự ràng buộc giữa các biến MRV

Heuristic độ: 
  
   chọn biến có nhiều ràng buộc nhất đối với các biến còn lại

![Hình ảnh](../TaiLieu/slide_md/figures/australia-most-constraining-variable.png)

---
## Giá trị ràng buộc nhỏ nhất

Cho một biến, chọn giá trị ít ràng buộc nhất:
  
   cái loại trừ ít giá trị nhất trong các biến còn lại

![Hình ảnh](../TaiLieu/slide_md/figures/australia-least-constraining-value.png)

Việc kết hợp các phương pháp phỏng đoán này làm cho 1000 quân hậu trở nên khả thi

---
## Kiểm tra chuyển tiếp

\note{Idea}: Theo dõi các giá trị pháp lý còn lại cho các biến chưa được gán

\phantom{\note{Idea}: }Chấm dứt tìm kiếm khi bất kỳ biến nào không có giá trị pháp lý

![Hình ảnh](../TaiLieu/slide_md/figures/forward-checking-progress1.png)

---
## Kiểm tra chuyển tiếp

\note{Idea}: Theo dõi các giá trị pháp lý còn lại cho các biến chưa được gán

\phantom{\note{Idea}: }Chấm dứt tìm kiếm khi bất kỳ biến nào không có giá trị pháp lý

![Hình ảnh](../TaiLieu/slide_md/figures/forward-checking-progress2.png)

---
## Kiểm tra chuyển tiếp

\note{Idea}: Theo dõi các giá trị pháp lý còn lại cho các biến chưa được gán

\phantom{\note{Idea}: }Chấm dứt tìm kiếm khi bất kỳ biến nào không có giá trị pháp lý

![Hình ảnh](../TaiLieu/slide_md/figures/forward-checking-progress3.png)

---
## Kiểm tra chuyển tiếp

\note{Idea}: Theo dõi các giá trị pháp lý còn lại cho các biến chưa được gán

\phantom{\note{Idea}: }Chấm dứt tìm kiếm khi bất kỳ biến nào không có giá trị pháp lý

![Hình ảnh](../TaiLieu/slide_md/figures/forward-checking-progress4.png)

---
## Truyền bá ràng buộc

Kiểm tra chuyển tiếp truyền thông tin từ các biến được gán đến các biến chưa được gán,
nhưng không cung cấp khả năng phát hiện sớm mọi lỗi:

![Hình ảnh](../TaiLieu/slide_md/figures/forward-checking-progress3.png)

\mat{$NT$} và \mat{$SA$} không thể cùng có màu xanh lam!

\defn{Truyền bá ràng buộc} liên tục thực thi các ràng buộc cục bộ

---
## Tính nhất quán của hồ quang 

Dạng truyền lan đơn giản nhất làm cho mỗi cung \defn{nhất quán}

\mat{$X\rightarrow Y$} nhất quán iff
  
  đối với *mọi* giá trị \mat{$x$} của \mat{$X$} thì có *some* được phép \mat{$y$}

![Hình ảnh](../TaiLieu/slide_md/figures/ac-example1.png)

---
## Tính nhất quán của hồ quang 

Dạng truyền lan đơn giản nhất làm cho mỗi cung \defn{nhất quán}

\mat{$X\rightarrow Y$} nhất quán iff
  
  đối với *mọi* giá trị \mat{$x$} của \mat{$X$} thì có *some* được phép \mat{$y$}

![Hình ảnh](../TaiLieu/slide_md/figures/ac-example2.png)

---
## Tính nhất quán của hồ quang 

Dạng truyền lan đơn giản nhất làm cho mỗi cung \defn{nhất quán}

\mat{$X\rightarrow Y$} nhất quán iff
  
  đối với *mọi* giá trị \mat{$x$} của \mat{$X$} thì có *some* được phép \mat{$y$}

![Hình ảnh](../TaiLieu/slide_md/figures/ac-example3.png)

Nếu \mat{$X$} mất giá trị, các hàng xóm của \mat{$X$} cần được kiểm tra lại

---
## Tính nhất quán của hồ quang 

Dạng truyền lan đơn giản nhất làm cho mỗi cung \defn{nhất quán}

\mat{$X\rightarrow Y$} nhất quán iff
  
  đối với *mọi* giá trị \mat{$x$} của \mat{$X$} thì có *some* được phép \mat{$y$}

![Hình ảnh](../TaiLieu/slide_md/figures/ac-example4.png)

Nếu \mat{$X$} mất giá trị, các hàng xóm của \mat{$X$} cần được kiểm tra lại

Tính nhất quán của hồ quang phát hiện lỗi sớm hơn việc kiểm tra chuyển tiếp

Có thể chạy như một bộ tiền xử lý hoặc sau mỗi lần gán

---
## Thuật toán nhất quán Arc

```text
function AC-3(csp) returns the CSP, possibly with reduced domains
      inputs: csp, a binary CSP with variables \(\{X_{1, X_{2}, \ldots, X_{n}\}\)}
      local: queue, a queue of arcs, initially all the arcs in csp

    while queue is not empty do
        \((X_{i, X_{j})\)}{Remove-First(queue)}
        if Remove-Inconsistent-Values(\(X_{i}, X_{j}\)) then 
            for each \(X_{k}\) in Neighbors[\(X_{i}\)] do
                add (\(X_{k}, X_{i}\)) to queue
\fnsep
function Remove-Inconsistent-Values(\(X_{i), X_{j}\)}{true iff succeeds}
    removed <- false
    for each x in Domain[\(X_{i}\)] do
        if no value \(y\) in Domain[\(X_{j}\)] allows (x,y) to satisfy the constraint \(X_i \leftrightarrow X_j\)
            then delete x from Domain[\(X_{i}\)];  removed <- true
    return removed
```

\mat{$O(n^2d^3)$}, có thể giảm xuống \mat{$O(n^2d^2)$}
(nhưng việc phát hiện *all* là NP-hard)

---
## Cấu trúc bài toán

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/australia-csp.png)

Tasmania và đất liền là \defn{bài toán con độc lập}

Có thể xác định là \defn{các thành phần được kết nối} của biểu đồ ràng buộc

---
## Cấu trúc bài toán tiếp theo.

Giả sử mỗi bài toán con có các biến \mat{$c$} trên tổng số \mat{$n$}

Chi phí giải pháp trong trường hợp xấu nhất là \mat{$n/c \cdot d^c$}, *tuyến tính* trong \mat{$n$}

Ví dụ: \mat{$n\eq 80$}, \mat{$d\eq 2$}, \mat{$c\eq 20$}
  
  \mat{$2^{80}$} = 4 tỷ năm với tốc độ 10 triệu nút/giây
  
  \mat{$4\cdot 2^{20}$} = 0,4 giây ở 10 triệu nút/giây

---
## CSP có cấu trúc cây

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/tree-csp1.png)

\note{Định lý}: nếu đồ thị ràng buộc không có vòng lặp, thì CSP có thể được giải theo 
\mat{$O(n\,d^2)$} thời gian

So sánh với các CSP chung, trong đó thời gian trong trường hợp xấu nhất là \mat{$O(d^n)$}

Thuộc tính này cũng áp dụng cho lý luận logic và xác suất:

một ví dụ quan trọng về mối quan hệ giữa các hạn chế cú pháp

và sự phức tạp của lý luận.

---
## Thuật toán cho CSP có cấu trúc cây

1. Chọn biến làm gốc, sắp xếp biến từ gốc đến lá

sao cho mọi nút cha của nút đều đứng trước nó theo thứ tự 

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/tree-csp2.png)

2. Đối với \mat{$j$} từ \mat{$n$} xuống \mat{$2$}, hãy áp dụng \prog{RemoveInconsistent\mat{\mat{$(Parent(X_j),X_j)$}}

3. Đối với \mat{$j$} từ \mat{$1$} đến \mat{$n$}, gán \mat{$X_j$} nhất quán với \mat{$Parent(X_j)$}

---
## CSP gần như có cấu trúc cây

\defn{Điều hòa}: khởi tạo một biến, cắt tỉa các miền của hàng xóm của nó

,75\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/australia-cutset.png)

\defn{Điều hòa cutset}: khởi tạo (theo mọi cách) một tập hợp các biến
 
sao cho đồ thị ràng buộc còn lại là một cây

Kích thước cutset \mat{$c$} $\implies$ thời gian chạy \mat{$O(d^c\cdot (n-c)d^2)$}, rất nhanh đối với \mat{$c$} nhỏ

---
## Thuật toán lặp cho CSP

Leo đồi, ủ mô phỏng thường hoạt động với 

trạng thái "hoàn thành", tức là, tất cả các biến được gán

Để đăng ký CSP:
  
cho phép các trạng thái có ràng buộc không thỏa mãn
  
toán tử *gán lại giá trị biến *

Lựa chọn biến: chọn ngẫu nhiên bất kỳ biến xung đột nào

Lựa chọn giá trị theo \defn{min-conflicts} heuristic:
  
chọn giá trị vi phạm ít ràng buộc nhất 
  
tức là leo dốc với \mat{$h(n)$} = tổng số ràng buộc bị vi phạm

---
## Ví dụ: 4-Queens

\note{Các bang}: 4 quân hậu trong 4 cột (các bang \mat{$4^4 = 256$})

\note{Toán tử}: di chuyển quân hậu trong cột

\note{Kiểm tra mục tiêu}: không tấn công

\note{Đánh giá}: \mat{$h(n)$} = số lần tấn công

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/4queens-iterative.png)

---
## Hiệu suất xung đột tối thiểu

Cho trạng thái ban đầu ngẫu nhiên, có thể giải \mat{$n$}-nữ hoàng trong thời gian gần như không đổi cho
tùy ý \mat{$n$} với xác suất cao (ví dụ: \mat{$n$} = 10.000.000)

Điều tương tự cũng có vẻ đúng đối với mọi CSP được tạo ngẫu nhiên 

*ngoại trừ* trong phạm vi tỷ lệ hẹp
\[
R = \frac{\mbox{number of constraints}}{\mbox{number of variables}}
\]

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/random-csp-runtime.png)

---
## Tóm tắt

CSP là một loại vấn đề đặc biệt:
  
các trạng thái được xác định bởi các giá trị của một tập hợp biến cố định
  
kiểm tra mục tiêu được xác định bởi \defn{ràng buộc} trên các giá trị biến

Quay lui = tìm kiếm theo chiều sâu với một biến được gán cho mỗi nút

Phương pháp phỏng đoán lựa chọn giá trị và thứ tự biến giúp ích đáng kể

Kiểm tra chuyển tiếp ngăn chặn các nhiệm vụ đảm bảo thất bại sau này

Việc truyền bá ràng buộc (ví dụ: tính nhất quán của cung) thực hiện công việc bổ sung

để hạn chế các giá trị và phát hiện sự không nhất quán

Biểu diễn CSP cho phép phân tích cấu trúc vấn đề

CSP có cấu trúc cây có thể được giải quyết trong thời gian tuyến tính

Những xung đột nhỏ lặp đi lặp lại thường có hiệu quả trong thực tế

---
## Ví dụ: 4-Queen làm CSP

Giả sử có một quân hậu ở mỗi cột. Mỗi người đi vào hàng nào?

\hbox{
\note{Biến} \mat{$Q_1$}, \mat{$Q_2$}, \mat{$Q_3$}, \mat{$Q_4$} 

\note{Miền} \mat{$D_i = \{1,2,3,4\}$}

\note{Ràng buộc}
  
\mat{$Q_i \neq Q_j$} (không thể ở cùng một hàng)
  
\mat{$|Q_i - Q_j| \neq |i-j|$} (hoặc cùng đường chéo)

}
 
,3in
![Hình ảnh](../TaiLieu/slide_md/figures/4queens.png)

Chuyển từng ràng buộc thành tập hợp các giá trị cho phép cho các biến của nó

Ví dụ: các giá trị cho \mat{$(Q_1,Q_2)$} là 
\mat{$(1,3)\ (1,4)\ (2,4)\ (3,1)\ (4,1)\ (4,2)$}