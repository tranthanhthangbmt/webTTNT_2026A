\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Các thuật toán tìm kiếm có thông tin (Informed search)

## Chương 4, Phần 1--2, 4

---
## Nội dung

- Tìm kiếm tốt nhất đầu tiên (Best-first search)

- Tìm kiếm A$^*$

- Hàm Heuristic

- Leo đồi (Hill-climbing)

- Luyện kim mô phỏng (Simulated annealing)

---
## Ôn tập: Tìm kiếm tổng quát

```text
function General-Search(problem, Queuing-Fn){một giải pháp, hoặc thất bại}

    nodes <- Make-Queue(Make-Node(Initial-State[problem]))
    loop do
          if nodes trống then return thất bại
          node <- Remove-Front(nodes)
          if Goal-Test[problem] áp dụng cho State(node) thành công then return node
          nodes <- Queuing-Fn(nodes, Expand(node, Operators[problem]))
    end
```

Một chiến lược được xác định bằng cách chọn *thứ tự phát triển nút*

---
## Tìm kiếm tốt nhất đầu tiên (Best-first search)

Ý tưởng: sử dụng một *hàm đánh giá* cho mỗi nút
    
-- ước tính mức độ "đáng mong muốn"

$\Rightarrow$ Phát triển nút chưa được phát triển có mức độ mong muốn cao nhất

<u>Cài đặt</u>:

**QueueingFn** = chèn các trạng thái kế tiếp theo thứ tự giảm dần của mức độ mong muốn

Các trường hợp đặc biệt:
    
tìm kiếm tham lam (greedy search)
    
tìm kiếm A$^*$

---
## Bản đồ Romania với chi phí bước tính bằng km

![Hình ảnh](../TaiLieu/slide_md/figures/romania2.png)

---
## Tìm kiếm tham lam (Greedy search)

Hàm đánh giá $h(n)$ (hàm k<u>h</u>ám phá - <u>h</u>euristic)
    
= ước lượng chi phí từ $n$ đến *đích* ($goal$)

Ví dụ, $h_{{\rm SLD}}(n)$ = khoảng cách đường chim bay từ $n$ đến Bucharest

Tìm kiếm tham lam phát triển nút *có vẻ* gần đích nhất

---
## Ví dụ tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-romania1.png)

---
## Ví dụ tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-romania2.png)

---
## Ví dụ tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-romania3.png)

---
## Ví dụ tìm kiếm tham lam

![Hình ảnh](../TaiLieu/slide_md/figures/greedy-romania4.png)

---
## Thuộc tính của tìm kiếm tham lam

<u>Đầy đủ (Complete)</u>??

<u>Thời gian (Time)</u>??

<u>Không gian bộ nhớ (Space)</u>??

<u>Tối ưu (Optimal)</u>??

---
## Thuộc tính của tìm kiếm tham lam

<u>Đầy đủ</u>?? Không -- có thể bị mắc kẹt trong các vòng lặp, ví dụ:
    
Iasi $\rightarrow$ Neamt $\rightarrow$ Iasi $\rightarrow$ Neamt $\rightarrow$

Sẽ đầy đủ trong không gian hữu hạn nếu có kiểm tra trạng thái lặp

<u>Thời gian</u>?? $O(b^m)$, nhưng một heuristic tốt có thể cải thiện đáng kể

<u>Không gian</u>?? $O(b^m)$ --- giữ tất cả các nút trong bộ nhớ

<u>Tối ưu</u>?? Không

---
## Tìm kiếm A$^*$

Ý tưởng: tránh phát triển các đường đi đã tốn kém

Hàm đánh giá $f(n) = g(n) + h(n)$

$g(n)$ = chi phí tính đến hiện tại để đạt đến $n$

$h(n)$ = chi phí ước tính đến đích từ $n$

$f(n)$ = tổng chi phí ước tính của đường đi qua $n$ đến đích

Tìm kiếm A$^*$ sử dụng một heuristic *chấp nhận được* (admissible)

nghĩa là, $h(n) \leq h^*(n)$ trong đó $h^*(n)$ là chi phí *thực tế* từ $n$.

Ví dụ, $h_{{\rm SLD}}(n)$ không bao giờ đánh giá quá cao khoảng cách đường bộ thực tế

<u>Định lý</u>: Tìm kiếm A$^*$ là tối ưu

---
## Ví dụ tìm kiếm A$^*$

![Hình ảnh](../TaiLieu/slide_md/figures/astar-romania1.png)

---
## Ví dụ tìm kiếm A$^*$

![Hình ảnh](../TaiLieu/slide_md/figures/astar-romania2.png)

---
## Ví dụ tìm kiếm A$^*$

![Hình ảnh](../TaiLieu/slide_md/figures/astar-romania3.png)

---
## Ví dụ tìm kiếm A$^*$

![Hình ảnh](../TaiLieu/slide_md/figures/astar-romania4.png)

---
## Ví dụ tìm kiếm A$^*$

![Hình ảnh](../TaiLieu/slide_md/figures/astar-romania5.png)

---
## Ví dụ tìm kiếm A$^*$

![Hình ảnh](../TaiLieu/slide_md/figures/astar-romania6.png)

---
## Tính tối ưu của A$^*$ (chứng minh tiêu chuẩn)

Giả sử một nút đích không tối ưu $G_2$ đã được sinh ra
và đang ở trong hàng đợi. Gọi $n$ là một nút chưa được phát triển
nằm trên đường đi ngắn nhất đến đích tối ưu $G_1$.

![Hình ảnh](../TaiLieu/slide_md/figures/astar-proof.png)

\begin{eqnarray*}
f(G_2) & = &  g(G_2) &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{vì } h(G_2) = 0 

       & > &  g(G_1) &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{vì } G_2 \mbox{ là không tối ưu} 

      &\geq& f(n)    &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{vì } h \mbox{ là chấp nhận được} 
\end{eqnarray*}

Vì $f(G_2) > f(n)$, A$^*$ sẽ không bao giờ chọn $G_2$ để phát triển

---
## Tính tối ưu của A$^*$ (hữu ích hơn)

<u>Bổ đề</u>: A$^*$ phát triển các nút theo thứ tự giá trị $f$ tăng dần

Từ từ thêm các "đường đồng mức $f$" của các nút (so sánh với tìm kiếm chiều rộng thêm các lớp)

Đường đồng mức $i$ chứa tất cả các nút có $f=f_i$, trong đó $f_i < f_{i+1}$

![Hình ảnh](../TaiLieu/slide_md/figures/f-circles.png)

---
## Thuộc tính của A$^*$

<u>Đầy đủ</u>?? Có, trừ khi có vô số nút với $f \leq f(G)$

<u>Thời gian</u>?? Hàm mũ theo [sai số tương đối của $h$ $\times$ chiều dài của giải pháp]

<u>Không gian</u>?? Giữ tất cả các nút trong bộ nhớ

<u>Tối ưu</u>?? Có --- không thể phát triển $f_{i+1}$ cho đến khi $f_i$ hoàn tất

---
## Chứng minh bổ đề: Pathmax

Đối với một số heuristic chấp nhận được, $f$ có thể *giảm* dọc theo một đường đi

Ví dụ, giả sử $n'$ là một nút kế tiếp của $n$

![Hình ảnh](../TaiLieu/slide_md/figures/pathmax-example.png)

Nhưng điều này ném bỏ thông tin!

$f(n)=9 \Rightarrow$ chi phí thực sự của đường đi qua $n$ là $\geq 9$

Do đó chi phí thực sự của đường đi qua $n'$ cũng $\geq 9$

Điều chỉnh Pathmax cho A$^*$:

Thay vì $f(n') = g(n') + h(n')$, sử dụng $f(n') = max(g(n') + h(n'), f(n))$

Với pathmax, $f$ luôn không giảm dọc theo bất kỳ đường đi nào

---
## Các heuristic chấp nhận được

Ví dụ, cho bài toán 8-puzzle (trò chơi xếp số 8 ô):

$h_1(n)$ = số ô đặt sai vị trí

$h_2(n)$ = tổng khoảng cách <u>Manhattan</u>
    
(tức là tổng số ô vuông từ vị trí hiện tại đến vị trí mong muốn của mỗi ô)

![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>$h_1(S)$ =</u>?? 

<u>$h_2(S)$ =</u>?? 

---
## Các heuristic chấp nhận được

Ví dụ, cho bài toán 8-puzzle:

$h_1(n)$ = số ô đặt sai vị trí

$h_2(n)$ = tổng khoảng cách <u>Manhattan</u>
    
(tức là tổng số ô vuông từ vị trí hiện tại đến vị trí mong muốn của mỗi ô)

![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>$h_1(S)$ =</u>?? 7

<u>$h_2(S)$ =</u>?? 2+3+3+2+4+2+0+2 = 18

---
## Sự vượt trội (Dominance)

Nếu $h_2(n) \geq h_1(n)$ với mọi $n$ (cả hai đều chấp nhận được)

thì $h_2$ *vượt trội* $h_1$ và tốt hơn cho quá trình tìm kiếm

Chi phí tìm kiếm điển hình:

| &nbsp; | &nbsp; |
|---|---|
| $d=14$ | IDS = 3,473,941 nút |
|  | A$^*(h_1)$ = 539 nút |
|  | A$^*(h_2)$ = 113 nút |
| $d=14$ | IDS = quá nhiều nút |
|  | A$^*(h_1)$ = 39,135 nút |
|  | A$^*(h_2)$ = 1,641 nút |

---
## Bài toán nới lỏng (Relaxed problems)

Các heuristic chấp nhận được có thể được suy ra từ chi phí giải pháp

*chính xác* của phiên bản *nới lỏng* của bài toán

Nếu các quy tắc của bài toán 8-puzzle được nới lỏng để một ô có thể di chuyển
*bất cứ nơi đâu*, thì $h_1(n)$ cho ta giải pháp ngắn nhất

Nếu các quy tắc được nới lỏng để một ô có thể di chuyển đến *bất kỳ ô
kề cạnh nào*, thì $h_2(n)$ cho ta giải pháp ngắn nhất

Đối với bài toán Người giao hàng (TSP): gọi đường đi là *bất kỳ* cấu trúc nào nối tất cả các thành phố
    
$\Longrightarrow$ heuristic là cây khung nhỏ nhất (minimum spanning tree)

---
## Thuật toán cải tiến lặp (Iterative improvement algorithms)

Trong nhiều bài toán tối ưu hóa, *đường đi* không quan trọng;

bản thân trạng thái đích chính là giải pháp

Khi đó, không gian trạng thái = tập các cấu hình "đầy đủ";
    
tìm cấu hình *tối ưu*, ví dụ TSP
    
hoặc tìm cấu hình thỏa mãn ràng buộc, ví dụ n-quân hậu

Trong những trường hợp này, có thể sử dụng các thuật toán *cải tiến lặp*;

giữ một trạng thái "hiện tại" duy nhất, và cố gắng cải thiện nó

Không gian bộ nhớ không đổi, thích hợp cho cả tìm kiếm trực tuyến và ngoại tuyến

---
## Ví dụ: Bài toán Người giao hàng (TSP)

Tìm hành trình ngắn nhất đi qua mỗi thành phố đúng một lần

![Hình ảnh](../TaiLieu/slide_md/figures/tsp-sequence.png)

---
## Ví dụ: Bài toán $n$-quân hậu

Đặt $n$ quân hậu trên bàn cờ $n \times n$ sao cho không có hai quân hậu nào nằm
trên cùng một

hàng, cột, hoặc đường chéo

![Hình ảnh](../TaiLieu/slide_md/figures/4queens-sequence.png)

---
## Leo đồi (Hill-climbing / gradient ascent / descent)

"Giống như leo đỉnh Everest trong màn sương mù dày đặc với chứng mất trí nhớ"

```text
function Hill-Climbing(problem) returns một trạng thái giải pháp
      inputs: problem, một bài toán
      local: current, một nút
      local: next, một nút

    current <- Make-Node(Initial-State[problem])
    loop do
          next <- một nút kế tiếp có giá trị cao nhất của current
          if Value[next] $<$ Value[current] then return current
          current <- next
    end
```

---
## Leo đồi (tiếp)

Vấn đề: tùy thuộc vào trạng thái ban đầu, có thể bị mắc kẹt ở cực đại cục bộ (local maxima)

![Hình ảnh](../TaiLieu/slide_md/figures/hill-climbing-maxima.png)

---
## Luyện kim mô phỏng (Simulated annealing)

Ý tưởng: thoát khỏi cực đại cục bộ bằng cách cho phép một số bước đi "tồi"

*nhưng giảm dần kích thước và tần suất của chúng*

```text
function Simulated-Annealing(problem, schedule) returns một trạng thái giải pháp
      inputs: problem, một bài toán
      inputs: schedule, một ánh xạ từ thời gian sang "nhiệt độ"
      local: current, một nút
      local: next, một nút
      local: T, một "nhiệt độ" kiểm soát xác suất của các bước đi xuống

    current <- Make-Node(Initial-State[problem])
    for t 1 to infinity do
          T <- schedule[t]
          if T=0 then return current
          next <- một nút kế tiếp được chọn ngẫu nhiên của current
          $\Delta$E <- Value[next] -- Value[current]
          if $\Delta$E $>$ 0 then current <- next
          else current <- next chỉ với xác suất $e^{\DeltaE/T}$
```

---
## Thuộc tính của luyện kim mô phỏng

Ở một "nhiệt độ" cố định $T$, xác suất chiếm hữu trạng thái đạt đến

phân bố Boltzman
\[
p(x) = 
  pha e^{\frac{E(x)}{kT}}
\]
$T$ giảm đủ chậm $\Longrightarrow$ luôn đạt được trạng thái tốt nhất

<u>Đây có nhất thiết là một sự đảm bảo thú vị không?</u>??

Được phát triển bởi Metropolis và cộng sự vào năm 1953, dùng cho mô phỏng quá trình vật lý

Được sử dụng rộng rãi trong thiết kế bố trí VLSI, lập lịch hàng không, v.v.