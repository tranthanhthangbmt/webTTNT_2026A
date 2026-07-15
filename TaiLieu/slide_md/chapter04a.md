\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}
\def\Astar{A$^*$}

# Thuật toán tìm kiếm có thông tin (Informed search algorithms)

## Chương 4, Phần 1--2

---
## Phác thảo

- Tìm kiếm đầu tiên tốt nhất

- tìm kiếm {\Astar}

- Chẩn đoán

---
## Đánh giá: Tìm kiếm cây

```text
function Tree-Search(problem, \var{fringe)}{a solution, or failure}
    fringe <- Insert(Make-Node(Initial-State[problem]), fringe)
    loop do
          if fringe is empty then return failure
          node <- Remove-Front(fringe)
          if Goal-Test[problem] applied to State(node) succeeds return node       
          fringe <- InsertAll(Expand(node, problem), fringe)
```

Chiến lược được xác định bằng cách chọn thứ tự *mở rộng nút*

---
## Tìm kiếm đầu tiên tốt nhất

\note{Idea}: sử dụng hàm đánh giá \defn{} cho mỗi nút
    
-- ước tính về "sự mong muốn"

$\Rightarrow$ Mở rộng nút chưa được mở rộng mong muốn nhất

\note{Triển khai}:

\v{fringe} là hàng đợi được sắp xếp theo thứ tự mong muốn giảm dần

Các trường hợp đặc biệt:
    
tìm kiếm tham lam 
    
tìm kiếm {\Astar}

---
## Romania với chi phí bước tính bằng km

![Hình ảnh](../TaiLieu/slide_md/figures/romania2.png)

---
## Tham lam tìm kiếm

Hàm đánh giá \mat{$h(n)$} (*h*euristic)
    
= ước tính chi phí từ \mat{$n$} đến mục tiêu gần nhất

Ví dụ: \mat{$h_{{\rm SLD}}(n)$} = khoảng cách đường thẳng từ \mat{$n$} đến Bucharest

Tìm kiếm tham lam mở rộng nút *xuất hiện* gần mục tiêu nhất

---
## Ví dụ về tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-progress01.png)

---
## Ví dụ về tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-progress02.png)

---
## Ví dụ về tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-progress03.png)

---
## Ví dụ về tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-progress04.png)

---
## Thuộc tính tìm kiếm tham lam

<u>Hoàn thành</u>??

---
## Thuộc tính tìm kiếm tham lam

<u>Hoàn thành</u>?? Không--có thể bị mắc kẹt trong các vòng lặp, ví dụ: với Oradea làm mục tiêu,
    
Iasi $\rightarrow$ Neamt $\rightarrow$ Iasi $\rightarrow$ Neamt $\rightarrow$

Hoàn thành trong không gian hữu hạn với việc kiểm tra trạng thái lặp lại

<u>Thời gian</u>??

---
## Thuộc tính tìm kiếm tham lam

<u>Hoàn thành</u>?? Không--có thể bị mắc kẹt trong các vòng lặp, ví dụ:
    
Iasi $\rightarrow$ Neamt $\rightarrow$ Iasi $\rightarrow$ Neamt $\rightarrow$

Hoàn thành trong không gian hữu hạn với việc kiểm tra trạng thái lặp lại

<u>Thời gian</u>?? \mat{$O(b^m)$}, nhưng phương pháp phỏng đoán tốt có thể mang lại sự cải thiện đáng kể

<u>Không gian</u>??

---
## Thuộc tính tìm kiếm tham lam

<u>Hoàn thành</u>?? Không--có thể bị mắc kẹt trong các vòng lặp, ví dụ:
    
Iasi $\rightarrow$ Neamt $\rightarrow$ Iasi $\rightarrow$ Neamt $\rightarrow$

Hoàn thành trong không gian hữu hạn với việc kiểm tra trạng thái lặp lại

<u>Thời gian</u>?? \mat{$O(b^m)$}, nhưng phương pháp phỏng đoán tốt có thể mang lại sự cải thiện đáng kể

<u>Space</u>?? \mat{$O(b^m)$}---giữ tất cả các nút trong bộ nhớ

<u>Tối ưu</u>??

---
## Thuộc tính tìm kiếm tham lam

<u>Hoàn thành</u>?? Không--có thể bị mắc kẹt trong các vòng lặp, ví dụ:
    
Iasi $\rightarrow$ Neamt $\rightarrow$ Iasi $\rightarrow$ Neamt $\rightarrow$

Hoàn thành trong không gian hữu hạn với việc kiểm tra trạng thái lặp lại

<u>Thời gian</u>?? \mat{$O(b^m)$}, nhưng phương pháp phỏng đoán tốt có thể mang lại sự cải thiện đáng kể

<u>Space</u>?? \mat{$O(b^m)$}---giữ tất cả các nút trong bộ nhớ

<u>Tối ưu</u>?? Không

---
## {\Astar
 tìm kiếm}

\note{Ý tưởng}: tránh mở rộng những con đường vốn đã tốn kém

Hàm đánh giá \mat{$f(n) = g(n) + h(n)$}

\mat{$g(n)$} = chi phí cho đến nay để đạt được \mat{$n$}

\mat{$h(n)$} = chi phí ước tính cho mục tiêu từ \mat{$n$}

\mat{$f(n)$} = tổng chi phí ước tính của đường đi qua \mat{$n$} tới mục tiêu

Tìm kiếm {\Astar} sử dụng phương pháp phỏng đoán \defn{admissible}

tức là, \mat{$h(n) \leq h^*(n)$} trong đó \mat{$h^*(n)$} là chi phí *true* từ \mat{$n$}.

(Cũng yêu cầu \mat{$h(n)\geq 0$}, vì vậy \mat{$h(G)=0$} cho bất kỳ mục tiêu nào \mat{$G$}.)

Ví dụ: \mat{$h_{{\rm SLD}}(n)$} không bao giờ đánh giá quá cao khoảng cách đường thực tế

\note{Định lý}: tìm kiếm {\Astar} là tối ưu

---
## {\Astar
 ví dụ tìm kiếm}

![Hình ảnh](../TaiLieu/slide_md/figures/astar-progress01.png)

---
## {\Astar
 ví dụ tìm kiếm}

![Hình ảnh](../TaiLieu/slide_md/figures/astar-progress02.png)

---
## {\Astar
 ví dụ tìm kiếm}

![Hình ảnh](../TaiLieu/slide_md/figures/astar-progress03.png)

---
## {\Astar
 ví dụ tìm kiếm}

![Hình ảnh](../TaiLieu/slide_md/figures/astar-progress04.png)

---
## {\Astar
 ví dụ tìm kiếm}

![Hình ảnh](../TaiLieu/slide_md/figures/astar-progress05.png)

---
## {\Astar
 ví dụ tìm kiếm}

![Hình ảnh](../TaiLieu/slide_md/figures/astar-progress06.png)

---
## Tính tối ưu của {\Astar
 (bằng chứng tiêu chuẩn)}

Giả sử một số mục tiêu dưới mức tối ưu \mat{$G_2$} đã được tạo
và đang trong hàng đợi. Đặt \mat{$n$} là một nút chưa được mở rộng
trên con đường ngắn nhất tới mục tiêu tối ưu \mat{$G_1$}.

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/astar-proof.png)

\begin{eqnarray*}
f(G_2) & = &  g(G_2) &nbsp;&nbsp;&nbsp;&nbsp;  {\rm since\ }h(G_2) = 0 

       & > &  g(G_1) &nbsp;&nbsp;&nbsp;&nbsp;  {\rm since\ }G_2 {\rm\ is\ suboptimal} 

      &\geq& f(n)    &nbsp;&nbsp;&nbsp;&nbsp;  {\rm since\ }h {\rm\ is\ admissible} 
\end{eqnarray*}

Vì \mat{$f(G_2) > f(n)$}, {\Astar} sẽ không bao giờ chọn \mat{$G_2$} để mở rộng

---
## Tính tối ưu của {\Astar
 (hữu ích hơn)}

\note{ Bổ đề}: {\Astar} mở rộng các nút theo thứ tự tăng dần giá trị \mat{$f$}$^*$

Dần dần thêm "\mat{$f$}-contours" của các nút (xem thêm các lớp theo chiều rộng đầu tiên)

Đường viền \mat{$i$} có tất cả các nút có \mat{$f=f_i$}, trong đó \mat{$f_i < f_{i+1}$}

,75\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/f-circles.png)

---
## Thuộc tính của {\Astar

<u>Hoàn thành</u>??

---
## Thuộc tính của {\Astar

<u>Hoàn thành</u>?? Có, trừ khi có vô số nút có \mat{$f \leq f(G)$}

<u>Thời gian</u>??

---
## Thuộc tính của {\Astar

<u>Hoàn thành</u>?? Có, trừ khi có vô số nút có \mat{$f \leq f(G)$}

<u>Thời gian</u>?? Hàm mũ theo [lỗi tương đối trong \mat{$h$} $\times$ độ dài của soln.]

<u>Không gian</u>??

---
## Thuộc tính của {\Astar

<u>Hoàn thành</u>?? Có, trừ khi có vô số nút có \mat{$f \leq f(G)$}

<u>Thời gian</u>?? Hàm mũ theo [lỗi tương đối trong \mat{$h$} $\times$ độ dài của soln.]

<u>Space</u>?? Giữ tất cả các nút trong bộ nhớ

<u>Tối ưu</u>??

---
## Thuộc tính của {\Astar

<u>Hoàn thành</u>?? Có, trừ khi có vô số nút có \mat{$f \leq f(G)$}

<u>Thời gian</u>?? Hàm mũ theo [lỗi tương đối trong \mat{$h$} $\times$ độ dài của soln.]

<u>Space</u>?? Giữ tất cả các nút trong bộ nhớ

<u>Tối ưu</u>?? Có---không thể mở rộng \mat{$f_{i+1}$} cho đến khi \mat{$f_i$} kết thúc

{\Astar} mở rộng tất cả các nút bằng \mat{$f(n) < C^*$}

{\Astar} mở rộng một số nút bằng \mat{$f(n) = C^*$}

{\Astar} không mở rộng nút nào với \mat{$f(n) > C^*$}

---
## Chứng minh bổ đề: Tính nhất quán

Một phương pháp phỏng đoán là \defn{nhất quán} nếu \raisebox{-0.35\textwidth[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/consistency.png)}
\[
  h(n) \leq c(n,a,n') + h(n')
\]
Nếu \mat{$h$} nhất quán, chúng ta có\
\mat{\begin{eqnarray*}
f(n') &=& g(n') + h(n') 

      &=& g(n) + c(n,a,n') + h(n') 

      &\geq& g(n) + h(n) 

      &=& f(n)
\end{eqnarray*}}
Tức là, \mat{$f(n)$} không giảm dọc theo bất kỳ đường dẫn nào.

---
## Các phương pháp phỏng đoán được chấp nhận

Ví dụ: đối với câu đố 8:

\mat{$h_1(n)$} = số ô bị đặt sai vị trí

\mat{$h_2(n)$} = tổng khoảng cách \defn{Manhattan} 
    
(tức là số ô vuông từ vị trí mong muốn của mỗi ô)

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>$h_2(S)$ =</u>?? 

<u>$h_2(S)$ =</u>?? 

---
## Các phương pháp phỏng đoán được chấp nhận

Ví dụ: đối với câu đố 8:

\mat{$h_1(n)$} = số ô bị đặt sai vị trí

\mat{$h_2(n)$} = tổng khoảng cách \defn{Manhattan} 
    
(tức là số ô vuông từ vị trí mong muốn của mỗi ô)

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>$h_2(S)$ =</u>?? 6

<u>$h_2(S)$ =</u>?? 4+0+3+3+1+0+2+1 = {14}

---
## Sự thống trị

Nếu \mat{$h_2(n) \geq h_1(n)$} cho tất cả \mat{$n$} (cả hai đều được chấp nhận)

thì \mat{$h_2$} \defn{chiếm ưu thế} \mat{$h_1$} và tốt hơn cho tìm kiếm

Chi phí tìm kiếm điển hình:

| &nbsp; | &nbsp; |
|---|---|
| $d=14$ | IDS = 3.473.941 nút |
|  | A$^*(h_1)$ = 539 nút |
|  | A$^*(h_2)$ = 113 nút |
| $d=24$ | IDS $\approx$ 54.000.000.000 nút |
|  | A$^*(h_1)$ = 39.135 nút |
|  | A$^*(h_2)$ = 1.641 nút |

Với bất kỳ phương pháp phỏng đoán được chấp nhận nào \mat{$h_a$}, \mat{$h_b$},
\mat{\[
  h(n) = \max(h_a(n),h_b(n))
\]}
cũng được chấp nhận và chiếm ưu thế \mat{$h_a$}, \mat{$h_b$}

---
## Các vấn đề đã được giải quyết

Các phương pháp phỏng đoán được chấp nhận có thể được rút ra từ *chính xác*

chi phí giải pháp của phiên bản *thoải mái* của vấn đề

Nếu các quy tắc của câu đố 8 được nới lỏng để một viên gạch có thể di chuyển
*bất cứ nơi nào*, sau đó \mat{$h_1(n)$} đưa ra giải pháp ngắn nhất

Nếu các quy tắc được nới lỏng để một ô có thể di chuyển tới *bất kỳ ô liền kề nào
Square*, sau đó \mat{$h_2(n)$} cho lời giải ngắn nhất

Điểm mấu chốt: chi phí giải pháp tối ưu của một vấn đề thoải mái 

không lớn hơn chi phí giải pháp tối ưu của bài toán thực

---
## Các vấn đề đã được giải quyết tiếp.

Ví dụ nổi tiếng: \defn{vấn đề của nhân viên bán hàng du lịch} (TSP)

Tìm chuyến đi ngắn nhất đến thăm tất cả các thành phố đúng một lần

,75\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/tsp-mst.png)

\defn{ Cây bao trùm tối thiểu } có thể được tính trong \mat{$O(n^2)$} 

và là giới hạn dưới của hành trình (mở) ngắn nhất

---
## Tóm tắt

Hàm heuristic ước tính chi phí của các đường đi ngắn nhất

Phương pháp phỏng đoán tốt có thể giảm đáng kể chi phí tìm kiếm 

Tìm kiếm đầu tiên tốt nhất tham lam mở rộng thấp nhất \mat{$h$} 
  
  -- không đầy đủ và không phải lúc nào cũng tối ưu

Tìm kiếm {\Astar} mở rộng ở mức thấp nhất \mat{$g+h$}
  
  -- đầy đủ và tối ưu
  
  -- cũng có hiệu quả tối ưu (tối đa các điểm ngắt, để tìm kiếm chuyển tiếp)

Các phương pháp phỏng đoán có thể chấp nhận được có thể được rút ra từ lời giải chính xác của các bài toán thoải mái