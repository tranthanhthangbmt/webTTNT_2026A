# Chapter 04 Searching In Complex Environments

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_04/chapter_04_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_04_Searching%20In%20Complex%20Environments.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}
\def\Astar{A$^*$}

# Informed search algorithms

## Chapter 4, Sections 1--2

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

\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Local search algorithms

## Chapter 4, Sections 3--4

---
## Phác thảo

- Leo đồi

- Ủ mô phỏng

- Thuật toán di truyền (tóm lược)

- Tìm kiếm cục bộ trong không gian liên tục (rất ngắn gọn)

---
## Thuật toán cải tiến lặp lại

Trong nhiều vấn đề tối ưu hóa, *path* không liên quan;

bản thân trạng thái mục tiêu là giải pháp

Khi đó không gian trạng thái = tập hợp các cấu hình "hoàn thành";
    
tìm cấu hình *tối ưu*, ví dụ: TSP
    
hoặc tìm cấu hình thỏa mãn các ràng buộc, ví dụ: thời gian biểu

Trong những trường hợp như vậy, có thể sử dụng thuật toán \defn{cải tiến lặp lại};

giữ một trạng thái “hiện tại” duy nhất, cố gắng cải thiện nó

Không gian cố định, thích hợp cho việc tìm kiếm trực tuyến cũng như ngoại tuyến

---
## Ví dụ: Vấn đề của nhân viên bán hàng khi đi du lịch

Bắt đầu với bất kỳ chuyến tham quan hoàn chỉnh nào, thực hiện trao đổi theo cặp

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/tsp-sequence.png)

Các biến thể của phương pháp này đạt được trong khoảng 1\% mức tối ưu rất nhanh chóng với
hàng ngàn thành phố

---
## Ví dụ: \mat{$n$
-quân hậu}

Đặt quân hậu \mat{$n$} lên bàn \mat{$n \times n$} không có hai quân hậu
trên cùng 

hàng, cột hoặc đường chéo

Di chuyển một nữ hoàng để giảm số lượng xung đột

![Hình ảnh](../TaiLieu/slide_md/figures/4queens-iterative.png)

Hầu như luôn giải quyết được các vấn đề của \mat{$n$}-nữ hoàng gần như ngay lập tức

cho \mat{$n$} rất lớn, ví dụ: \mat{$n\eq 1 million$}

---
## Leo đồi (hoặc lên/xuống dốc)

"Giống như leo Everest trong sương mù dày đặc với chứng mất trí nhớ"

```text
function Hill-Climbing(problem) returns a state that is a local maximum
      inputs: problem, a problem
      local: current, a node
      local: neighbor, a node

    current <- Make-Node(Initial-State[problem])
    loop do
          neighbor <- a highest-valued successor of current
          if Value[neighbor] $\leq$ Value[current] then return State[current]
          current <- neighbor
    end
```

---
## Leo đồi tiếp.

Hữu ích khi xem xét \defn{cảnh quan không gian trạng thái}

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/hill-climbing.png)

\defn{ Leo đồi khởi động lại ngẫu nhiên } vượt qua cực đại cục bộ---hoàn thành tầm thường

\defn{Di chuyển ngang ngẫu nhiên} \smiley thoát khỏi vai \frowny vòng lặp trên cực đại phẳng

---
## Ủ mô phỏng

Ý tưởng: thoát khỏi cực đại địa phương bằng cách cho phép một số chuyển động “xấu”

*nhưng giảm dần kích thước và tần số của chúng*

```text
function Simulated-Annealing(problem, schedule) returns a solution state
      inputs: problem, a problem
      inputs: schedule, a mapping from time to "temperature"
      local: current, a node
      local: next, a node
      local: T, a "temperature" controlling prob. of downward steps

    current <- Make-Node(Initial-State[problem])
    for t 1 to infinity do
          T <- schedule[t]
          if T = 0 then return current
          next <- a randomly selected successor of current
          $\Delta$E <- Value[next] -- Value[current]
          if $\Delta$E $>$ 0 then current <- next
          else current <- next only with probability $e^{\Delta E/T}$
```

---
## Tính chất của quá trình ủ mô phỏng

Ở "nhiệt độ" cố định $T$, xác suất chiếm đóng trạng thái đạt 

phân phối Boltzman
\mat{\[
p(x) = 
  pha e^{\frac{E(x)}{kT}}
\]}
$T$ giảm đủ chậm $\Longrightarrow$ luôn đạt trạng thái tốt nhất \mat{$x^*$}

vì \mat{$e^{\frac{E(x^*)}{kT}} / e^{\frac{E(x)}{kT}} 
= e^{\frac{E(x^*)-E(x)}{kT}} \gg 1$} dành cho \mat{$T$} nhỏ

<u>Đây có phải là một sự đảm bảo thú vị</u>??

Được phát minh bởi Metropolis và cộng sự, 1953, để mô hình hóa quy trình vật lý

Được sử dụng rộng rãi trong bố trí VLSI, lập lịch trình hàng không, v.v.

---
## Tìm kiếm chùm tia cục bộ

\note{Idea}: giữ trạng thái $k$ thay vì 1; chọn top $k$ trong số tất cả những người kế nhiệm của họ

Không giống như các tìm kiếm $k$ chạy song song!

Các tìm kiếm tìm thấy trạng thái tốt tuyển dụng các tìm kiếm khác tham gia cùng họ

\note{Sự cố}: khá thường xuyên, tất cả các trạng thái $k$ đều kết thúc trên cùng một ngọn đồi địa phương

\note{Idea}: chọn ngẫu nhiên $k$ người kế nhiệm, thiên về những người giỏi

Hãy quan sát sự tương tự gần gũi với chọn lọc tự nhiên!

---
## Thuật toán di truyền

= tìm kiếm chùm cục bộ ngẫu nhiên + tạo các trạng thái kế tiếp từ *cặp * trạng thái

![Hình ảnh](../TaiLieu/slide_md/figures/genetic.png)

---
## Thuật toán di truyền tiếp.

GA yêu cầu các trạng thái được mã hóa dưới dạng chuỗi (\defn{GPs} sử dụng \note{programs})

Crossover giúp *iff chuỗi con là các thành phần có ý nghĩa*

![Hình ảnh](../TaiLieu/slide_md/figures/8queens-crossover.png)

Sự tiến hóa của GA $\neq$: ví dụ: gen thực mã hóa bộ máy sao chép!

---
## Không gian trạng thái liên tục

Giả sử chúng tôi muốn xác định ba sân bay ở Romania:
  
-- Không gian trạng thái 6-D được xác định bởi \mat{$(x_1,y_2)$}, \mat{$(x_2,y_2)$}, \mat{$(x_3,y_3)$}
  
-- hàm mục tiêu \mat{$f(x_1,y_2,x_2,y_2,x_3,y_3)$} = 
    
   tổng bình phương khoảng cách từ mỗi thành phố đến sân bay gần nhất

\defn{Phương pháp rời rạc hóa} biến không gian liên tục thành không gian rời rạc,

ví dụ: \defn{gradient theo kinh nghiệm} xem xét sự thay đổi của \mat{$\pm \delta$} trong mỗi tọa độ

Phương pháp tính toán \defn{Gradient} 
\mat{\[
 \nabla f=\left(
  \frac{\partial f}{\partial x_1},\frac{\partial f}{\partial y_1},
  \frac{\partial f}{\partial x_2},\frac{\partial f}{\partial y_2},
  \frac{\partial f}{\partial x_3},\frac{\partial f}{\partial y_3}
 \right)
\]}
để tăng/giảm \mat{$f$}, ví dụ: bằng 
\mat{$\x \leftarrow \x + 
  pha \nabla f(\x)$}

Đôi khi có thể giải chính xác \mat{$\nabla f(\x) = 0$} (ví dụ: với một thành phố).

\defn{Newton--Raphson} (1664, 1690) lặp lại 
\mat{$\x \leftarrow \x - \H^{-1}_f(\x) \nabla f(\x)$}

để giải \mat{$\nabla f(\x) = 0$}, trong đó \mat{$\H_{ij}\eq \partial^2 f/\partial x_i \partial x_j$}



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [HILL-CLIMBING](codeAndExercises/aima-pseudocode-master/md/Hill-Climbing.md)
- [SIMULATED-ANNEALING](codeAndExercises/aima-pseudocode-master/md/Simulated-Annealing.md)
- [GENETIC-ALGORITHM](codeAndExercises/aima-pseudocode-master/md/Genetic-Algorithm.md)
- [AND-OR-GRAPH-SEARCH](codeAndExercises/aima-pseudocode-master/md/And-Or-Graph-Search.md)
- [ONLINE-DFS-AGENT](codeAndExercises/aima-pseudocode-master/md/Online-DFS-Agent.md)
- [LRTA*-AGENT](codeAndExercises/aima-pseudocode-master/md/LRTAStar-Agent.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Search](codeAndExercises/aima-python-master/notebooks/search.ipynb)
- [Search (Python File)](codeAndExercises/aima-python-master/notebooks/search.py)


#### **Bài tập**

##### Bài tập 4.1

Give the name of the algorithm that results from each of the following
special cases:<br>

1.  Local beam search with $k = 1$.<br>

2.  Local beam search with one initial state and no limit on the number
    of states retained.<br>

3.  Simulated annealing with $T = 0$ at all times (and omitting the
    termination test).<br>

4.  Simulated annealing with $T=\infty$ at all times.<br>

5.  Genetic algorithm with population size $N = 1$.<br>


---

##### Bài tập 4.2

Exercise <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_19/">brio-exercise</a> considers the problem of
building railway tracks under the assumption that pieces fit exactly
with no slack. Now consider the real problem, in which pieces don’t fit
exactly but allow for up to 10 degrees of rotation to either side of the
“proper” alignment. Explain how to formulate the problem so it could be
solved by simulated annealing.


---

##### Bài tập 4.3

In this exercise, we explore the use of local search methods to solve
TSPs of the type defined in Exercise <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_38/">tsp-mst-exercise</a><br>

1.  Implement and test a hill-climbing method to solve TSPs. Compare the
    results with optimal solutions obtained from the A* algorithm with
    the MST heuristic (Exercise <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_38/">tsp-mst-exercise</a>)<br>

2.  Repeat part (a) using a genetic algorithm instead of hill climbing.
    You may want to consult @Larranaga+al:1999 for some suggestions for representations.


---

##### Bài tập 4.4

Generate a large number of 8-puzzle and
8-queens instances and solve them (where possible) by hill climbing
(steepest-ascent and first-choice variants), hill climbing with random
restart, and simulated annealing. Measure the search cost and percentage
of solved problems and graph these against the optimal solution cost.
Comment on your results.


---

##### Bài tập 4.5

The <b>And-Or-Graph-Search</b> algorithm in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/and-or-graph-search-algorithm.png">and-or-graph-search-algorithm</a> checks for
repeated states only on the path from the root to the current state.
Suppose that, in addition, the algorithm were to store
<i>every</i> visited state and check against that list. (See in
Figure <a class="insideBookFigRef" href="#">breadth-first-search-algorithm</a> for an example.)
Determine the information that should be stored and how the algorithm
should use that information when a repeated state is found.
(*Hint*: You will need to distinguish at least between
states for which a successful subplan was constructed previously and
states for which no subplan could be found.) Explain how to use labels,
as defined in Section <a class="sectionRef" title="" href="#">cyclic-plan-section</a>, to avoid
having multiple copies of subplans.


---

##### Bài tập 4.6

Explain precisely how to modify the <b>And-Or-Graph-Search</b> algorithm to
generate a cyclic plan if no acyclic plan exists. You will need to deal
with three issues: labeling the plan steps so that a cyclic plan can
point back to an earlier part of the plan, modifying <b>Or-Search</b> so that it
continues to look for acyclic plans after finding a cyclic plan, and
augmenting the plan representation to indicate whether a plan is cyclic.
Show how your algorithm works on (a) the slippery vacuum world, and (b)
the slippery, erratic vacuum world. You might wish to use a computer
implementation to check your results.


---

##### Bài tập 4.7

In Section <a class="sectionRef" title="" href="#">conformant-section</a> we introduced belief
states to solve sensorless search problems. A sequence of actions solves
a sensorless problem if it maps every physical state in the initial
belief state $b$ to a goal state. Suppose the agent knows $h^\*(s)$, the
true optimal cost of solving the physical state $s$ in the fully
observable problem, for every state $s$ in $b$. Find an admissible
heuristic $h(b)$ for the sensorless problem in terms of these costs, and
prove its admissibilty. Comment on the accuracy of this heuristic on the
sensorless vacuum problem of
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum2-sets-figure.png">vacuum2-sets-figure</a>. How well does A* perform?


---

##### Bài tập 4.8

This exercise explores
subset–superset relations between belief states in sensorless or
partially observable environments.<br>

1.  Prove that if an action sequence is a solution for a belief state
    $b$, it is also a solution for any subset of $b$. Can anything be
    said about supersets of $b$?<br>

2.  Explain in detail how to modify graph search for sensorless problems
    to take advantage of your answers in (a).<br>

3.  Explain in detail how to modify and–or search for
    partially observable problems, beyond the modifications you describe
    in (b).<br>


---

##### Bài tập 4.9

On page <a class="pageRef" title="" href="#">multivalued-sensorless-page</a> it was assumed
that a given action would have the same cost when executed in any
physical state within a given belief state. (This leads to a
belief-state search problem with well-defined step costs.) Now consider
what happens when the assumption does not hold. Does the notion of
optimality still make sense in this context, or does it require
modification? Consider also various possible definitions of the “cost”
of executing an action in a belief state; for example, we could use the
<i>minimum</i> of the physical costs; or the
<i>maximum</i>; or a cost <i>interval</i> with the lower
bound being the minimum cost and the upper bound being the maximum; or
just keep the set of all possible costs for that action. For each of
these, explore whether A* (with modifications if necessary) can return
optimal solutions.


---

##### Bài tập 4.10

Consider the sensorless version of the
erratic vacuum world. Draw the belief-state space reachable from the
initial belief state $\{1,2,3,4,5,6,7,8\}$, and explain why the
problem is unsolvable.


---

##### Bài tập 4.11

Consider the sensorless version of the
erratic vacuum world. Draw the belief-state space reachable from the
initial belief state $\{ 1,3,5,7 \}$, and explain why the problem
is unsolvable.


---

##### Bài tập 4.12

We can turn the navigation problem in
Exercise <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_9/">path-planning-exercise</a> into an environment as
follows:<br>

-   The percept will be a list of the positions, <i>relative to the
    agent</i>, of the visible vertices. The percept does
    <i>not</i> include the position of the robot! The robot must
    learn its own position from the map; for now, you can assume that
    each location has a different “view.”<br>

-   Each action will be a vector describing a straight-line path
    to follow. If the path is unobstructed, the action succeeds;
    otherwise, the robot stops at the point where its path first
    intersects an obstacle. If the agent returns a zero motion vector
    and is at the goal (which is fixed and known), then the environment
    teleports the agent to a <i>random location</i> (not inside
    an obstacle).<br>

-   The performance measure charges the agent 1 point for each unit of
    distance traversed and awards 1000 points each time the goal
    is reached.<br>

1.  Implement this environment and a problem-solving agent for it. After
    each teleportation, the agent will need to formulate a new problem,
    which will involve discovering its current location.<br>

2.  Document your agent’s performance (by having the agent generate
    suitable commentary as it moves around) and report its performance
    over 100 episodes.<br>

3.  Modify the environment so that 30% of the time the agent ends up at
    an unintended destination (chosen randomly from the other visible
    vertices if any; otherwise, no move at all). This is a crude model
    of the motion errors of a real robot. Modify the agent so that when
    such an error is detected, it finds out where it is and then
    constructs a plan to get back to where it was and resume the
    old plan. Remember that sometimes getting back to where it was might
    also fail! Show an example of the agent successfully overcoming two
    successive motion errors and still reaching the goal.<br>

4.  Now try two different recovery schemes after an error: (1) head for
    the closest vertex on the original route; and (2) replan a route to
    the goal from the new location. Compare the performance of the three
    recovery schemes. Would the inclusion of search costs affect the
    comparison?<br>

5.  Now suppose that there are locations from which the view
    is identical. (For example, suppose the world is a grid with
    square obstacles.) What kind of problem does the agent now face?
    What do solutions look like?


---

##### Bài tập 4.13

Suppose that an agent is in a $3 \times 3$
maze environment like the one shown in
Figure <a class="insideBookFigRef"  target="_blank" href="https://aimacode.github.io/aima-exercises/figures/maze-3x3-figure.png">maze-3x3-figure</a>. The agent knows that its
initial location is (1,1), that the goal is at (3,3), and that the
actions <i>Up</i>, <i>Down</i>, <i>Left</i>, <i>Right</i> have their usual
effects unless blocked by a wall. The agent does <i>not</i> know
where the internal walls are. In any given state, the agent perceives
the set of legal actions; it can also tell whether the state is one it
has visited before.<br>

1.  Explain how this online search problem can be viewed as an offline
    search in belief-state space, where the initial belief state
    includes all possible environment configurations. How large is the
    initial belief state? How large is the space of belief states?<br>

2.  How many distinct percepts are possible in the initial state?<br>

3.  Describe the first few branches of a contingency plan for this
    problem. How large (roughly) is the complete plan?<br>

Notice that this contingency plan is a solution for <i>every
possible environment</i> fitting the given description. Therefore,
interleaving of search and execution is not strictly necessary even in
unknown environments.


---

##### Bài tập 4.14

Suppose that an agent is in a $3 \times 3$
maze environment like the one shown in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/maze-3x3-figure.png">maze-3x3-figure</a>. The agent knows that its
initial location is (3,3), that the goal is at (1,1), and that the four
actions *Up*, *Down*, *Left*, *Right* have their usual
effects unless blocked by a wall. The agent does *not* know
where the internal walls are. In any given state, the agent perceives
the set of legal actions; it can also tell whether the state is one it
has visited before or is a new state.<br>

1.  Explain how this online search problem can be viewed as an offline
    search in belief-state space, where the initial belief state
    includes all possible environment configurations. How large is the
    initial belief state? How large is the space of belief states?<br>

2.  How many distinct percepts are possible in the initial state?<br>

3.  Describe the first few branches of a contingency plan for this
    problem. How large (roughly) is the complete plan?<br>

Notice that this contingency plan is a solution for *every
possible environment* fitting the given description. Therefore,
interleaving of search and execution is not strictly necessary even in
unknown environments.


---

##### Bài tập 4.15

In this exercise, we examine hill climbing
in the context of robot navigation, using the environment in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/geometric-scene-figure.png">geometric-scene-figure</a> as an example.<br>

1.  Repeat Exercise <a class="exerciseRef" href="{{ site.baseurl }}/advanced-search-exercises/ex_11/">path-planning-agent-exercise</a> using
    hill climbing. Does your agent ever get stuck in a local minimum? Is
    it *possible* for it to get stuck with convex
    obstacles?<br>

2.  Construct a nonconvex polygonal environment in which the agent
    gets stuck.<br>

3.  Modify the hill-climbing algorithm so that, instead of doing a
    depth-1 search to decide where to go next, it does a
    depth-$k$ search. It should find the best $k$-step path and do one
    step along it, and then repeat the process.<br>

4.  Is there some $k$ for which the new algorithm is guaranteed to
    escape from local minima?<br>

5.  Explain how LRTA enables the agent to escape from local minima in
    this case.<br>


---

##### Bài tập 4.16

Like DFS, online DFS is incomplete for reversible state spaces with
infinite paths. For example, suppose that states are points on the
infinite two-dimensional grid and actions are unit vectors $(1,0)$,
$(0,1)$, $(-1,0)$, $(0,-1)$, tried in that order. Show that online DFS
starting at $(0,0)$ will not reach $(1,-1)$. Suppose the agent can
observe, in addition to its current state, all successor states and the
actions that would lead to them. Write an algorithm that is complete
even for bidirected state spaces with infinite paths. What states does
it visit in reaching $(1,-1)$?


---

##### Bài tập 4.17

Relate the time complexity of LRTA* to its space complexity.


---


<!-- tabs:end -->
