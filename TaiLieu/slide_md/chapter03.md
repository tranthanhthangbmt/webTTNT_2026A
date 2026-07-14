\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Giải quyết vấn đề và tìm kiếm

## Chương 3, Phần 1--5

---
## Nội dung

- Tác nhân giải quyết vấn đề

- Các loại bài toán

- Khởi tạo bài toán

- Các bài toán ví dụ

- Các thuật toán tìm kiếm cơ bản

---
## Tác nhân giải quyết vấn đề

Một dạng hạn chế của tác nhân tổng quát:

```text
function Simple-Problem-Solving-Agent(p) returns an action
      inputs: p, a percept
      static: s, an action sequence, initially empty
      static: state, some description of the current world state
      static: g, a goal, initially null
      static: problem, a problem formulation

    state <- Update-State(state, p)
    if s is empty then 
          g <- Formulate-Goal(state)
          problem <- Formulate-Problem(state, g)
          s <- Search(problem)
    action <- Recommendation(s, state)
    s <- Remainder(s, state)
    return action
```

Lưu ý: đây là giải quyết vấn đề *ngoại tuyến (offline)*.

Giải quyết vấn đề *trực tuyến (online)* bao gồm việc hành động mà không có
tri thức đầy đủ về bài toán và giải pháp.

---
## Ví dụ: Romania

Đang đi nghỉ ở Romania; hiện đang ở Arad.

Chuyến bay khởi hành vào ngày mai từ Bucharest

<u>Định dạng mục tiêu</u>:
    
có mặt ở Bucharest

<u>Khởi tạo bài toán</u>:
    
*trạng thái*: các thành phố khác nhau
    
*toán tử*: lái xe giữa các thành phố

<u>Tìm giải pháp</u>:
    
chuỗi các thành phố, ví dụ: Arad, Sibiu, Fagaras, Bucharest

---
## Ví dụ: Romania

![Hình ảnh](../TaiLieu/slide_md/figures/romania.png)

---
## Các loại bài toán

<u>Tất định, có thể truy cập</u> $\Longrightarrow$ *bài toán trạng thái đơn (single-state)*

<u>Tất định, không thể truy cập</u> $\Longrightarrow$ *bài toán đa trạng thái (multiple-state)*

<u>Không tất định, không thể truy cập</u> $\Longrightarrow$ *bài toán dự phòng (contingency)*
    
phải sử dụng cảm biến trong quá trình thực thi 
    
giải pháp là một *cây* hoặc *chính sách* 
    
thường *đan xen* giữa tìm kiếm và thực thi

<u>Không gian trạng thái chưa biết</u> $\Longrightarrow$ *bài toán khám phá* ("trực tuyến")

---
## Ví dụ: thế giới máy hút bụi

<u>Trạng thái đơn</u>, bắt đầu ở \#5. <u>Giải pháp</u>?? 

<u>Đa trạng thái</u>, bắt đầu ở $\{1,2,3,4,5,6,7,8\}$

ví dụ: $Phải$ đi đến $\{2,4,6,8\}$. <u>Giải pháp</u>??

<u>Dự phòng</u>, bắt đầu ở \#5

Định luật Murphy: $Hút$ có thể làm bẩn một tấm thảm đang sạch

Cảm biến cục bộ: chỉ biết có bụi và vị trí hiện tại.

<u>Giải pháp</u>??

 

![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-space.png)

---
## Khởi tạo bài toán trạng thái đơn

Một *bài toán* được định nghĩa bởi bốn mục:

<u>*trạng thái ban đầu</u>*  &nbsp;&nbsp;  ví dụ: "ở Arad"

<u>*toán tử</u>* (hoặc *hàm kế tiếp* $S(x)$) 
    
ví dụ: Arad $\rightarrow$ Zerind  &nbsp;&nbsp;&nbsp;&nbsp;  Arad $\rightarrow$ Sibiu  &nbsp;&nbsp;&nbsp;&nbsp;  v.v.

<u>*kiểm tra mục tiêu</u>*, có thể là
    
*tường minh*, ví dụ: $x$ = "ở Bucharest"
    
*ngầm định*, ví dụ: $NoDirt(x)$

<u>*chi phí đường đi</u>* (cộng dồn)
    
ví dụ: tổng khoảng cách, số lượng toán tử đã thực thi, v.v.

Một *giải pháp* là một chuỗi các toán tử

dẫn từ trạng thái ban đầu đến một trạng thái mục tiêu

---
## Chọn lựa một không gian trạng thái

Thế giới thực thì phức tạp một cách vô lý 
    
$\Rightarrow$ không gian trạng thái phải được *trừu tượng hóa* để giải quyết bài toán

(Trừu tượng) trạng thái = tập hợp các trạng thái thực

(Trừu tượng) toán tử = kết hợp phức tạp của các hành động thực
    
   ví dụ: "Arad $\rightarrow$ Zerind" đại diện cho một tập hợp phức tạp
      
   các tuyến đường có thể, đường vòng, trạm dừng chân, v.v. 

Để đảm bảo tính khả thi, <u>bất kỳ</u> trạng thái thực nào "ở Arad"
  
đều phải đi được đến *một* trạng thái thực nào đó "ở Zerind"

(Trừu tượng) giải pháp = 
    
   tập hợp các đường đi thực tế là giải pháp trong thế giới thực

Mỗi hành động trừu tượng phải "dễ dàng" hơn bài toán ban đầu!

---
## Ví dụ: Câu đố 8 ô (8-puzzle)

![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>trạng thái</u>??

<u>toán tử</u>??

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường đi</u>??

---
## Ví dụ: Câu đố 8 ô (8-puzzle)

![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>trạng thái</u>??: vị trí nguyên của các ô vuông (bỏ qua các vị trí trung gian)

<u>toán tử</u>??: di chuyển ô trống sang trái, phải, lên, xuống (bỏ qua kẹt v.v.)

<u>kiểm tra mục tiêu</u>??: = trạng thái mục tiêu (được cho trước)

<u>chi phí đường đi</u>??: 1 cho mỗi lần di chuyển

[Lưu ý: giải pháp tối ưu của họ Câu đố $n$-ô là NP-khó]

---
## Ví dụ: đồ thị không gian trạng thái thế giới máy hút bụi

![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>trạng thái</u>??

<u>toán tử</u>??

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường đi</u>??

---
## Ví dụ: đồ thị không gian trạng thái thế giới máy hút bụi

![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>trạng thái</u>??: số nguyên biểu thị vị trí bụi và robot (bỏ qua *lượng* bụi)

<u>toán tử</u>??: $Trái$, $Phải$, $Hút$

<u>kiểm tra mục tiêu</u>??: không còn bụi

<u>chi phí đường đi</u>??: 1 cho mỗi toán tử

---
## Ví dụ: lắp ráp robot

![Hình ảnh](../TaiLieu/slide_md/figures/stanford-arm+blocks.png)

<u>trạng thái</u>??: tọa độ giá trị thực của
    
các khớp robot
    
các bộ phận của vật thể cần lắp ráp

<u>toán tử</u>??: chuyển động liên tục của các khớp robot

<u>kiểm tra mục tiêu</u>??: lắp ráp hoàn chỉnh *không tính robot!*

<u>chi phí đường đi</u>??: thời gian thực thi

---
## Các thuật toán tìm kiếm

Ý tưởng cơ bản:
  
khám phá ngoại tuyến, mô phỏng không gian trạng thái
  
bằng cách sinh ra các trạng thái kế tiếp từ những trạng thái đã khám phá
      
(còn gọi là *khai triển* trạng thái)

```text
function General-Search(problem, strategy) returns a solution, or failure
    initialize the search tree using the initial state of problem
    loop do
          if there are no candidates for expansion then return failure
          choose a leaf node for expansion according to strategy
          if the node contains a goal state then return the corresponding solution
          else expand the node and add the resulting nodes to the search tree
    end
```

---
## Ví dụ tìm kiếm tổng quát

![Hình ảnh](../TaiLieu/slide_md/figures/general-romania1.png)

---
## Ví dụ tìm kiếm tổng quát

![Hình ảnh](../TaiLieu/slide_md/figures/general-romania2.png)

---
## Ví dụ tìm kiếm tổng quát

![Hình ảnh](../TaiLieu/slide_md/figures/general-romania3.png)

---
## Ví dụ tìm kiếm tổng quát

![Hình ảnh](../TaiLieu/slide_md/figures/general-romania4.png)

---
## Cài đặt các thuật toán tìm kiếm

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

---
## Cài đặt (tiếp theo): trạng thái (states) vs. nút (nodes)

Một *trạng thái* là một (biểu diễn của) cấu hình vật lý

Một *nút* là một cấu trúc dữ liệu tạo thành một phần của cây tìm kiếm
    
    bao gồm *nút cha*, *các nút con*, *độ sâu*, *chi phí đường đi* $g(x)$

*Trạng thái* không có nút cha, nút con, độ sâu, hay chi phí đường đi!

![Hình ảnh](../TaiLieu/slide_md/figures/state-vs-node.png)

Hàm **Expand** (Khai triển) tạo ra các nút mới, điền vào các trường
khác nhau và sử dụng **Operators** (Toán tử) (hoặc **SuccessorFn**) của
bài toán để tạo ra các trạng thái tương ứng.

---
## Các chiến lược tìm kiếm

Một chiến lược được xác định bằng cách chọn *thứ tự khai triển nút*

Các chiến lược được đánh giá dựa trên các khía cạnh sau:
    
<u>tính hoàn chỉnh (completeness)</u>---nó có luôn tìm ra giải pháp nếu giải pháp tồn tại không?
    
<u>độ phức tạp thời gian</u>---số lượng nút được tạo/khai triển
    
<u>độ phức tạp không gian</u>---số lượng nút tối đa lưu trong bộ nhớ
    
<u>tính tối ưu (optimality)</u>---nó có luôn tìm ra giải pháp có chi phí thấp nhất không?

Độ phức tạp thời gian và không gian được đo lường thông qua
    
$b$---hệ số rẽ nhánh (branching factor) tối đa của cây tìm kiếm
    
$d$---độ sâu của giải pháp có chi phí thấp nhất
    
$m$---độ sâu tối đa của không gian trạng thái (có thể là $\infty$)

---
## Các chiến lược tìm kiếm mù (Uninformed search)

Chiến lược *tìm kiếm mù* chỉ sử dụng những thông tin có sẵn

trong định nghĩa của bài toán

Tìm kiếm theo chiều rộng (Breadth-first search)

Tìm kiếm chi phí đồng nhất (Uniform-cost search)

Tìm kiếm theo chiều sâu (Depth-first search)

Tìm kiếm sâu hạn chế (Depth-limited search)

Tìm kiếm sâu lặp sâu dần (Iterative deepening search)

---
## Tìm kiếm theo chiều rộng

Khai triển nút chưa khai triển ở độ sâu nông nhất

<u>Cài đặt</u>:
    
**QueueingFn** (Hàm hàng đợi) = đặt các nút kế tiếp vào cuối hàng đợi

![Hình ảnh](../TaiLieu/slide_md/figures/bfs-romania1.png)

---
## Tìm kiếm theo chiều rộng

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/bfs-romania2.png)

---
## Tìm kiếm theo chiều rộng

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/bfs-romania3.png)

---
## Tìm kiếm theo chiều rộng

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/bfs-romania4.png)

---
## Các thuộc tính của tìm kiếm theo chiều rộng

<u>Hoàn chỉnh</u>??

<u>Thời gian</u>??

<u>Không gian</u>??

<u>Tối ưu</u>??

---
## Các thuộc tính của tìm kiếm theo chiều rộng

<u>Hoàn chỉnh</u>?? Có (nếu $b$ là hữu hạn)

<u>Thời gian</u>?? $1+b+b^2+b^3+\ldots +b^d = O(b^d)$, tức là tăng theo hàm mũ của $d$

<u>Không gian</u>?? $O(b^d)$ (lưu giữ mọi nút trong bộ nhớ)

<u>Tối ưu</u>?? Có (nếu chi phí = 1 cho mỗi bước); thông thường thì không tối ưu

*Không gian* là một vấn đề lớn; có thể dễ dàng tạo ra các nút ở mức 1MB/giây
    
do đó 24 giờ = 86GB.

---
## Romania với chi phí bước tính bằng km

![Hình ảnh](../TaiLieu/slide_md/figures/romania2.png)

---
## Tìm kiếm chi phí đồng nhất

Khai triển nút chưa khai triển có chi phí thấp nhất

<u>Cài đặt</u>:
    
**QueueingFn** = chèn theo thứ tự chi phí đường đi tăng dần

![Hình ảnh](../TaiLieu/slide_md/figures/uc-romania1.png)

---
## Tìm kiếm chi phí đồng nhất

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/uc-romania2.png)

---
## Tìm kiếm chi phí đồng nhất

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/uc-romania3.png)

---
## Tìm kiếm chi phí đồng nhất

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/uc-romania4.png)

---
## Các thuộc tính của tìm kiếm chi phí đồng nhất

<u>Hoàn chỉnh</u>?? Có, nếu chi phí mỗi bước $\geq \epsilon$

<u>Thời gian</u>?? Số nút có $g \leq {}$ chi phí của giải pháp tối ưu

<u>Không gian</u>?? Số nút có $g \leq {}$ chi phí của giải pháp tối ưu

<u>Tối ưu</u>?? Có

---
## Tìm kiếm theo chiều sâu

Khai triển nút chưa khai triển ở độ sâu sâu nhất

<u>Cài đặt</u>:
    
**QueueingFn** = chèn các nút kế tiếp vào đầu hàng đợi

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-romania1.png)

---
## Tìm kiếm theo chiều sâu

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-romania2.png)

---
## Tìm kiếm theo chiều sâu

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-romania3.png)

---
## Tìm kiếm theo chiều sâu

.

.

.

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-romania4.png)

Tức là, tìm kiếm theo chiều sâu có thể rơi vào các vòng lặp vô hạn

Cần một không gian tìm kiếm hữu hạn, không có chu trình (hoặc phải kiểm tra trạng thái lặp lại)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary1.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary2.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary3.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary4.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary5.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3 (tiếp)

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary6.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary7.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary8.png)

---
## Tìm kiếm theo chiều sâu trên cây nhị phân độ sâu 3

![Hình ảnh](../TaiLieu/slide_md/figures/dfs-binary9.png)

---
## Các thuộc tính của tìm kiếm theo chiều sâu

<u>Hoàn chỉnh</u>??

<u>Thời gian</u>??

<u>Không gian</u>??

<u>Tối ưu</u>??

---
## Các thuộc tính của tìm kiếm theo chiều sâu

<u>Hoàn chỉnh</u>?? Không: thất bại trong không gian có độ sâu vô hạn, không gian có chu trình
    
Sửa đổi để tránh lặp lại các trạng thái trên đường đi
      
$\Rightarrow$ hoàn chỉnh trong các không gian hữu hạn

<u>Thời gian</u>?? $O(b^m)$: rất tệ nếu $m$ lớn hơn nhiều so với $d$
    
        nhưng nếu các giải pháp dày đặc, có thể nhanh hơn nhiều so với tìm kiếm theo chiều rộng

<u>Không gian</u>?? $O(bm)$, tức là không gian tuyến tính!

<u>Tối ưu</u>?? Không

---
## Tìm kiếm sâu hạn chế (Depth-limited search)

= tìm kiếm theo chiều sâu với giới hạn độ sâu là $l$

<u>Cài đặt</u>:
    
Các nút ở độ sâu $l$ không có nút con kế tiếp

---
## Tìm kiếm sâu lặp sâu dần (Iterative deepening search)

```text
function Iterative-Deepening-Search(problem) returns a solution sequence
        inputs: problem, a problem

      for depth 0 to infinity do
          result <- Depth-Limited-Search(problem, depth)
          if result != cutoff then return result
      end
```

---
## Tìm kiếm sâu lặp sâu dần $l=0$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania1.png)

---
## Tìm kiếm sâu lặp sâu dần $l=1$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania1.png)

---
## Tìm kiếm sâu lặp sâu dần $l=1$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania2.png)

---
## Tìm kiếm sâu lặp sâu dần $l=2$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania1.png)

---
## Tìm kiếm sâu lặp sâu dần $l=2$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania2.png)

---
## Tìm kiếm sâu lặp sâu dần $l=2$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania3.png)

---
## Tìm kiếm sâu lặp sâu dần $l=2$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania4.png)

---
## Tìm kiếm sâu lặp sâu dần $l=2$

![Hình ảnh](../TaiLieu/slide_md/figures/ids-romania5.png)

---
## Các thuộc tính của tìm kiếm sâu lặp sâu dần

<u>Hoàn chỉnh</u>??

<u>Thời gian</u>??

<u>Không gian</u>??

<u>Tối ưu</u>??

---
## Các thuộc tính của tìm kiếm sâu lặp sâu dần

<u>Hoàn chỉnh</u>?? Có

<u>Thời gian</u>?? $(d+1)b^0 + d b^1 + (d-1)b^2 + \ldots + b^d = O(b^d)$

<u>Không gian</u>?? $O(bd)$

<u>Tối ưu</u>?? Có, nếu chi phí bước = 1
    
Có thể sửa đổi để khám phá trên cây chi phí đồng nhất

---
## Tóm tắt

Khởi tạo bài toán thường yêu cầu trừu tượng hóa các chi tiết của thế giới thực
để định nghĩa một không gian trạng thái có thể khả thi để khám phá

Nhiều chiến lược tìm kiếm mù khác nhau

Tìm kiếm sâu lặp sâu dần chỉ sử dụng không gian tuyến tính

và không tốn nhiều thời gian hơn các thuật toán tìm kiếm mù khác