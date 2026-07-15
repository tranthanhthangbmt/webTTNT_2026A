# Chapter 05 Constraint Satisfaction Problems

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_05/chapter_05_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_05_Constraint%20Satisfaction%20Problems.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Constraint Satisfaction Problems

## Chapter 5

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



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [MINIMAX-SEARCH](codeAndExercises/aima-pseudocode-master/md/Minimax-Decision.md)
- [ALPHA-BETA-SEARCH](codeAndExercises/aima-pseudocode-master/md/Alpha-Beta-Search.md)
- [MONTE-CARLO-TREE-SEARCH](codeAndExercises/aima-pseudocode-master/md/Monte-Carlo-Tree-Search.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Csp](codeAndExercises/aima-python-master/notebooks/csp.ipynb)
- [Csp (Python File)](codeAndExercises/aima-python-master/notebooks/csp.py)
- [Arc Consistency Heuristics](codeAndExercises/aima-python-master/notebooks/arc_consistency_heuristics.ipynb)
- [Arc Consistency Heuristics (Python File)](codeAndExercises/aima-python-master/notebooks/arc_consistency_heuristics.py)


#### **Bài tập**

##### Bài tập 5.1

Suppose you have an oracle, $OM(s)$, that correctly predicts the
opponent’s move in any state. Using this, formulate the definition of a
game as a (single-agent) search problem. Describe an algorithm for
finding the optimal move.


---

##### Bài tập 5.2

Consider the problem of solving two 8-puzzles.<br>

1.  Give a complete problem formulation in the style of
    Chapter <a class="chapterRef" title="" href="{{site.baseurl}}/search-exercises/">search-chapter.</a><br>

2.  How large is the reachable state space? Give an exact
    numerical expression.<br>

3.  Suppose we make the problem adversarial as follows: the two players
    take turns moving; a coin is flipped to determine the puzzle on
    which to make a move in that turn; and the winner is the first to
    solve one puzzle. Which algorithm can be used to choose a move in
    this setting?<br>

4.  Does the game eventually end, given optimal play? Explain.<br>
(a) A map where the cost of every edge is 1. Initially the pursuer $P$ is at
node <b>b</b> and the evader $E$ is at node <b>d</b> <br>(b) A partial game tree for this map.
Each node is labeled with the $P,E$ positions. $P$ moves first. Branches marked "?" have yet to be explored.
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/pursuit-evasion-game.svg" alt="pursuit-evasion-game-figure" id="pursuit-evasion-game-figure" style="width:100%">
  <figcaption><center><b>Pursuit evasion game Figure</b></center></figcaption>
</figure>


---

##### Bài tập 5.3

Imagine that, in Exercise <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_5/">two-friends-exercise</a>, one of
the friends wants to avoid the other. The problem then becomes a
two-player game. We assume now that the players take turns moving. The
game ends only when the players are on the same node; the terminal
payoff to the pursuer is minus the total time taken. (The evader “wins”
by never losing.) An example is shown in Figure.
<a href="#pursuit-evasion-game-figure">pursuit-evasion-game-figure</a><br>


1.  Copy the game tree and mark the values of the terminal nodes.<br>

2.  Next to each internal node, write the strongest fact you can infer
    about its value (a number, one or more inequalities such as
    “$\geq 14$”, or a “?”).<br>

3.  Beneath each question mark, write the name of the node reached by
    that branch.<br>

4.  Explain how a bound on the value of the nodes in (c) can be derived
    from consideration of shortest-path lengths on the map, and derive
    such bounds for these nodes. Remember the cost to get to each leaf
    as well as the cost to solve it.<br>

5.  Now suppose that the tree as given, with the leaf bounds from (d),
    is evaluated from left to right. Circle those “?” nodes that would
    <i>not</i> need to be expanded further, given the bounds
    from part (d), and cross out those that need not be considered
    at all.<br>

6.  Can you prove anything in general about who wins the game on a map
    that is a tree?<br>


---

##### Bài tập 5.4

Describe and implement state
descriptions, move generators, terminal tests, utility functions, and
evaluation functions for one or more of the following stochastic games:
Monopoly, Scrabble, bridge play with a given contract, or Texas hold’em
poker.
<div id="game-playing-chance-exercise"></div>


---

##### Bài tập 5.5

Describe and implement a <i>real-time</i>,
<i>multiplayer</i> game-playing environment, where time is part
of the environment state and players are given fixed time allocations.


---

##### Bài tập 5.6

Discuss how well the standard approach to game playing would apply to
games such as tennis, pool, and croquet, which take place in a
continuous physical state space.


---

##### Bài tập 5.7

Prove the following assertion: For every
game tree, the utility obtained by max using minimax
decisions against a suboptimal min will never be lower than
the utility obtained playing against an optimal min. Can
you come up with a game tree in which max can do still
better using a <i>suboptimal</i> strategy against a suboptimal
min?
<br>
Player $A$ moves first. The two players take turns moving, and each
player must move his token to an open adjacent space in either
direction.  If the opponent occupies an adjacent space, then a player
may jump over the opponent to the next open space if any. (For
example, if $A$ is on 3 and $B$ is on 2, then $A$ may move back to 1.)
The game ends when one player reaches the opposite end of the board.
If player $A$ reaches space 4 first, then the value of the game to $A$
is $+1$; if player $B$ reaches space 1 first, then the value of the
game to $A$ is $-1$.
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/line-game4.svg" alt="line-game4-figure" id="line-game4-figure" style="width:100%">
  <figcaption><center><b>The starting position of a simple game.</b></center></figcaption>
</figure>


---

##### Bài tập 5.8

Consider the two-player game described in
Figure <a class="insideExerciseFigRef" href="#line-game4-figure">line-game4-figure</a><br>

1.  Draw the complete game tree, using the following conventions:<br>

    -   Write each state as $(s_A,s_B)$, where $s_A$ and $s_B$ denote
        the token locations.<br>

    -   Put each terminal state in a square box and write its game value
        in a circle.<br>

    -   Put <i>loop states</i> (states that already appear on
        the path to the root) in double square boxes. Since their value
        is unclear, annotate each with a “?” in a circle.<br>

2.  Now mark each node with its backed-up minimax value (also in
    a circle). Explain how you handled the “?” values and why.<br>

3.  Explain why the standard minimax algorithm would fail on this game
    tree and briefly sketch how you might fix it, drawing on your answer
    to (b). Does your modified algorithm give optimal decisions for all
    games with loops?<br>

4.  This 4-square game can be generalized to $n$ squares for any
    $n > 2$. Prove that $A$ wins if $n$ is even and loses if $n$ is odd.


---

##### Bài tập 5.9

This problem exercises the basic concepts of game playing, using
tic-tac-toe (noughts and crosses) as an example. We define
$X_n$ as the number of rows, columns, or diagonals with exactly $n$
$X$’s and no $O$’s. Similarly, $O_n$ is the number of rows, columns, or
diagonals with just $n$ $O$’s. The utility function assigns $+1$ to any
position with $X_3=1$ and $-1$ to any position with $O_3 = 1$. All other
terminal positions have utility 0. For nonterminal positions, we use a
linear evaluation function defined as ${Eval}(s) = 3X_2(s) + X_1(s) - (3O_2(s) + O_1(s))$. <br>

1.  Approximately how many possible games of tic-tac-toe are there?<br>

2.  Show the whole game tree starting from an empty board down to depth
    2 (i.e., one $X$ and one $O$ on the board), taking symmetry
    into account.<br>

3.  Mark on your tree the evaluations of all the positions at depth 2.<br>

4.  Using the minimax algorithm, mark on your tree the backed-up values
    for the positions at depths 1 and 0, and use those values to choose
    the best starting move.<br>

5.  Circle the nodes at depth 2 that would <i>not</i> be
    evaluated if alpha–beta pruning were applied, assuming the nodes are
    generated in the optimal order for alpha–beta pruning.<br>


---

##### Bài tập 5.10

Consider the family of generalized tic-tac-toe games, defined as
follows. Each particular game is specified by a set $\mathcal S$ of
<i>squares</i> and a collection $\mathcal W$ of <i>winning
positions.</i> Each winning position is a subset of $\mathcal S$.
For example, in standard tic-tac-toe, $\mathcal S$ is a set of 9 squares
and $\mathcal W$ is a collection of 8 subsets of $\cal W$: the three
rows, the three columns, and the two diagonals. In other respects, the
game is identical to standard tic-tac-toe. Starting from an empty board,
players alternate placing their marks on an empty square. A player who
marks every square in a winning position wins the game. It is a tie if
all squares are marked and neither player has won.<br>

1.  Let $N= |{\mathcal S}|$, the number of squares. Give an upper bound
    on the number of nodes in the complete game tree for generalized
    tic-tac-toe as a function of $N$.<br>

2.  Give a lower bound on the size of the game tree for the worst case,
    where ${\mathcal W} = {\{\,\}}$.<br>

3.  Propose a plausible evaluation function that can be used for any
    instance of generalized tic-tac-toe. The function may depend on
    $\mathcal S$ and $\mathcal W$.<br>

4.  Assume that it is possible to generate a new board and check whether
    it is a winning position in 100$N$ machine instructions and assume a
    2 gigahertz processor. Ignore memory limitations. Using your
    estimate in (a), roughly how large a game tree can be completely
    solved by alpha–beta in a second of CPU time? a minute? an hour?


---

##### Bài tập 5.11

Develop a general game-playing program, capable of playing a variety of
games.<br>

1.  Implement move generators and evaluation functions for one or more
    of the following games: Kalah, Othello, checkers, and chess.<br>

2.  Construct a general alpha–beta game-playing agent.<br>

3.  Compare the effect of increasing search depth, improving move
    ordering, and improving the evaluation function. How close does your
    effective branching factor come to the ideal case of perfect move
    ordering?<br>

4.  Implement a selective search algorithm, such as B\* <a class="paperRef" title="" href="">Berliner:1979</a>,
    conspiracy number search @McAllester:1988, or MGSS\*
    <a class="paperRef" title="" href="">Russell+Wefald:1989</a> and compare its performance to A\*.


---

##### Bài tập 5.12

Describe how the minimax and alpha–beta algorithms change for
two-player, non-zero-sum games in which each player has a distinct
utility function and both utility functions are known to both players.
If there are no constraints on the two terminal utilities, is it
possible for any node to be pruned by alpha–beta? What if the player’s
utility functions on any state differ by at most a constant $k$, making
the game almost cooperative?


---

##### Bài tập 5.13

Describe how the minimax and alpha–beta algorithms change for
two-player, non-zero-sum games in which each player has a distinct
utility function and both utility functions are known to both players.
If there are no constraints on the two terminal utilities, is it
possible for any node to be pruned by alpha–beta? What if the player’s
utility functions on any state sum to a number between constants $-k$
and $k$, making the game almost zero-sum?


---

##### Bài tập 5.14

Develop a formal proof of correctness for alpha–beta pruning. To do
this, consider the situation shown in
Figure <a class="insideExerciseFigRef" href="#alpha-beta-proof-figure">alpha-beta-proof-figure</a>. The question is whether
to prune node $n_j$, which is a max-node and a descendant of node $n_1$.
The basic idea is to prune it if and only if the minimax value of $n_1$
can be shown to be independent of the value of $n_j$.<br>

1.  Mode $n_1$ takes on the minimum value among its children:
    $n_1 = \min(n_2,n_{{21}},\ldots,n_{2b_2})$. Find a similar
    expression for $n_2$ and hence an expression for $n_1$ in terms of
    $n_j$.<br>

2.  Let $l_i$ be the minimum (or maximum) value of the nodes to the
    <i>left</i> of node $n_i$ at depth $i$, whose minimax value
    is already known. Similarly, let $r_i$ be the minimum (or maximum)
    value of the unexplored nodes to the right of $n_i$ at depth $i$.
    Rewrite your expression for $n_1$ in terms of the $l_i$ and
    $r_i$ values.<br>

3.  Now reformulate the expression to show that in order to affect
    $n_1$, $n_j$ must not exceed a certain bound derived from the
    $l_i$ values.<br>

4.  Repeat the process for the case where $n_j$ is a min-node.<br>
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/alpha-beta-proof.svg" alt="alpha-beta-proof-figure" id="alpha-beta-proof-figure" style="width:100%">
  <figcaption><center><b>Situation when considering whether to prune node $n_j$.</b></center></figcaption>
</figure>


---

##### Bài tập 5.15

Prove that the alpha–beta algorithm takes time $O(b^{m/2})$ with optimal
move ordering, where $m$ is the maximum depth of the game tree.


---

##### Bài tập 5.16

Suppose you have a chess program that can evaluate 5 million nodes per
second. Decide on a compact representation of a game state for storage
in a transposition table. About how many entries can you fit in a
1-gigabyte in-memory table? Will that be enough for the three minutes of
search allocated for one move? How many table lookups can you do in the
time it would take to do one evaluation? Now suppose the transposition
table is stored on disk. About how many evaluations could you do in the
time it takes to do one disk seek with standard disk hardware?


---

##### Bài tập 5.17

Suppose you have a chess program that can evaluate 10 million nodes per
second. Decide on a compact representation of a game state for storage
in a transposition table. About how many entries can you fit in a
2-gigabyte in-memory table? Will that be enough for the three minutes of
search allocated for one move? How many table lookups can you do in the
time it would take to do one evaluation? Now suppose the transposition
table is stored on disk. About how many evaluations could you do in the
time it takes to do one disk seek with standard disk hardware?<br>


<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/pruning.svg" alt="trivial-chance-game-figure" id="trivial-chance-game-figure" style="width:100%">
  <figcaption><center><b>The complete game tree for a trivial game with chance nodes..</b></center></figcaption>
</figure>


---

##### Bài tập 5.18

This question considers pruning in games with chance nodes.
Figure <a class="insideExerciseFigRef" href="#trivial-chance-game-figure">trivial-chance-game-figure</a> shows the complete
game tree for a trivial game. Assume that the leaf nodes are to be
evaluated in left-to-right order, and that before a leaf node is
evaluated, we know nothing about its value—the range of possible values
is $-\infty$ to $\infty$.<br>

1.  Copy the figure, mark the value of all the internal nodes, and
    indicate the best move at the root with an arrow.<br>

2.  Given the values of the first six leaves, do we need to evaluate the
    seventh and eighth leaves? Given the values of the first seven
    leaves, do we need to evaluate the eighth leaf? Explain
    your answers.<br>

3.  Suppose the leaf node values are known to lie between –2 and 2
    inclusive. After the first two leaves are evaluated, what is the
    value range for the left-hand chance node?<br>

4.  Circle all the leaves that need not be evaluated under the
    assumption in (c).<br>


---

##### Bài tập 5.19

Implement the expectiminimax algorithm and the \*-alpha–beta algorithm,
which is described by <a class="paperRef" title="" href="">Ballard:1983</a>, for pruning game trees with chance nodes. Try
them on a game such as backgammon and measure the pruning effectiveness
of \*-alpha–beta.


---

##### Bài tập 5.20

Prove that with a positive linear
transformation of leaf values (i.e., transforming a value $x$ to
$ax + b$ where $a > 0$), the choice of move remains unchanged in a game
tree, even when there are chance nodes.


---

##### Bài tập 5.21

Consider the following procedure
for choosing moves in games with chance nodes:<br>

-   Generate some dice-roll sequences (say, 50) down to a suitable depth
    (say, 8).<br>

-   With known dice rolls, the game tree becomes deterministic. For each
    dice-roll sequence, solve the resulting deterministic game tree
    using alpha–beta.<br>

-   Use the results to estimate the value of each move and to choose
    the best.<br>

Will this procedure work well? Why (or why not)?<br>


---

##### Bài tập 5.22

In the following, a “max” tree consists only of max nodes, whereas an
“expectimax” tree consists of a max node at the root with alternating
layers of chance and max nodes. At chance nodes, all outcome
probabilities are nonzero. The goal is to <i>find the value of the
root</i> with a bounded-depth search. For each of (a)–(f), either
give an example or explain why this is impossible.<br>

1.  Assuming that leaf values are finite but unbounded, is pruning (as
    in alpha–beta) ever possible in a max tree?<br>

2.  Is pruning ever possible in an expectimax tree under the same
    conditions?<br>

3.  If leaf values are all nonnegative, is pruning ever possible in a
    max tree? Give an example, or explain why not.<br>

4.  If leaf values are all nonnegative, is pruning ever possible in an
    expectimax tree? Give an example, or explain why not.<br>

5.  If leaf values are all in the range $[0,1]$, is pruning ever
    possible in a max tree? Give an example, or explain why not.<br>

6.  If leaf values are all in the range $[0,1]$, is pruning ever
    possible in an expectimax tree?1<br>

7.  Consider the outcomes of a chance node in an expectimax tree. Which
    of the following evaluation orders is most likely to yield pruning
    opportunities?<br>

    i.  Lowest probability first<br>

    ii.  Highest probability first<br>

    iii.  Doesn’t make any difference<br>


---

##### Bài tập 5.23

In the following, a “max” tree consists only of max nodes, whereas an
“expectimax” tree consists of a max node at the root with alternating
layers of chance and max nodes. At chance nodes, all outcome
probabilities are nonzero. The goal is to <i>find the value of the
root</i> with a bounded-depth search.<br>

1.  Assuming that leaf values are finite but unbounded, is pruning (as
    in alpha–beta) ever possible in a max tree? Give an example, or
    explain why not.<br>

2.  Is pruning ever possible in an expectimax tree under the same
    conditions? Give an example, or explain why not.<br>

3.  If leaf values are constrained to be in the range $[0,1]$, is
    pruning ever possible in a max tree? Give an example, or explain
    why not.<br>

4.  If leaf values are constrained to be in the range $[0,1]$, is
    pruning ever possible in an expectimax tree? Give an example
    (qualitatively different from your example in (e), if any), or
    explain why not.<br>

5.  If leaf values are constrained to be nonnegative, is pruning ever
    possible in a max tree? Give an example, or explain why not.<br>

6.  If leaf values are constrained to be nonnegative, is pruning ever
    possible in an expectimax tree? Give an example, or explain why not.<br>

7.  Consider the outcomes of a chance node in an expectimax tree. Which
    of the following evaluation orders is most likely to yield pruning
    opportunities: (i) Lowest probability first; (ii) Highest
    probability first; (iii) Doesn’t make any difference?


---

##### Bài tập 5.24

Which of the following are true and which are false? Give brief
explanations.<br>

1.  In a fully observable, turn-taking, zero-sum game between two
    perfectly rational players, it does not help the first player to
    know what strategy the second player is using—that is, what move the
    second player will make, given the first player’s move.<br>

2.  In a partially observable, turn-taking, zero-sum game between two
    perfectly rational players, it does not help the first player to
    know what move the second player will make, given the first
    player’s move.<br>

3.  A perfectly rational backgammon agent never loses.<br>


---

##### Bài tập 5.25

Consider carefully the interplay of chance events and partial
information in each of the games in
Exercise <a class="exerciseRef" href="{{ site.baseurl }}/game-playing-exercises/ex_4/">game-playing-chance-exercise</a>.<br>

1.  For which is the standard expectiminimax model appropriate?
    Implement the algorithm and run it in your game-playing agent, with
    appropriate modifications to the game-playing environment.<br>

2.  For which would the scheme described in
    Exercise <a href="#ex5.21">game-playing-monte-carlo-exercise</a> be
    appropriate?<br>

3.  Discuss how you might deal with the fact that in some of the games,
    the players do not have the same knowledge of the current state.<br>


---


<!-- tabs:end -->
