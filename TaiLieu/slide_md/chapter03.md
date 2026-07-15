\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Problem solving and search

## Chapter 3

---
## Nhắc nhở

*Bài tập 0 hạn nộp lúc 5 giờ chiều hôm nay*

*Bài tập 1 đã đăng*, hạn nộp ngày 9/2

\note{Phần 105 sẽ chuyển sang 9-10h sáng} bắt đầu từ tuần sau

---
## Phác thảo

- Tác nhân giải quyết vấn đề

- Các loại sự cố

- Xây dựng bài toán

- Các vấn đề mẫu

- Thuật toán tìm kiếm cơ bản

---
## Tác nhân giải quyết vấn đề

Hình thức tổng đại lý bị hạn chế:

```text
function Simple-Problem-Solving-Agent(percept) returns an action
      static: seq, an action sequence, initially empty
      static: state, some description of the current world state
      static: goal, a goal, initially null
      static: problem, a problem formulation

    state <- Update-State(state, percept)
    if seq is empty then 
          goal <- Formulate-Goal(state)
          problem <- Formulate-Problem(state, goal)
          seq <- Search(problem)
    action <- Recommendation(seq, state)
    seq <- Remainder(seq, state)
    return action
```

Lưu ý: đây là cách giải quyết vấn đề \note{ngoại tuyến}; giải pháp được thực thi " nhắm mắt lại."

\note{Trực tuyến} giải quyết vấn đề liên quan đến hành động mà không có kiến thức đầy đủ.

---
## Ví dụ: Romania

Đang đi nghỉ ở Romania; hiện đang ở Arad.

Chuyến bay khởi hành vào ngày mai từ Bucharest

\note{Xây dựng mục tiêu}:
    
ở Bucharest

\note{Xây dựng bài toán}:
    
\note{tiểu bang}: các thành phố khác nhau
    
\note{hành động}: lái xe giữa các thành phố

\note{Tìm giải pháp}:
    
chuỗi các thành phố, ví dụ: Arad, Sibiu, Fagaras, Bucharest

---
## Ví dụ: Romania

![Hình ảnh](../TaiLieu/slide_md/figures/romania-distances.png)

---
## Các loại sự cố

\note{Có tính xác định, hoàn toàn có thể quan sát được} $\Longrightarrow$ \defn{vấn đề một trạng thái}
    
    Đại lý biết chính xác nó sẽ ở trạng thái nào; giải pháp là một chuỗi

\note{Không thể quan sát được} $\Longrightarrow$ \defn{vấn đề về tuân thủ}
    
    Đại lý có thể không biết nó ở đâu; nghiệm (nếu có) là dãy

\note{Không xác định} và/hoặc \note{có thể quan sát được một phần} $\Longrightarrow$ \defn{vấn đề dự phòng}
    
nhận thức cung cấp thông tin *mới* về trạng thái hiện tại
    
giải pháp là \defn{kế hoạch dự phòng} hoặc \defn{chính sách} 
    
thường *xen kẽ* tìm kiếm, thực thi

\note{Không gian trạng thái không xác định} $\Longrightarrow$ \defn{vấn đề khám phá} ("trực tuyến")

---
## Ví dụ: thế giới chân không

\note{Trạng thái đơn}, bắt đầu bằng \#5. <u>Giải pháp</u>?? 

 

,4\maxfigwidth
\raisebox{-0.35\maxfigwidth}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-space.png)}

---
## Ví dụ: thế giới chân không

\hbox{
\note{Trạng thái đơn}, bắt đầu bằng \#5. <u>Giải pháp</u>?? 

\mat{$[Right,Suck]$}

[0,5\baselineskip]
\note{Conformant}, bắt đầu trong \mat{$\{1,2,3,4,5,6,7,8\}$}

ví dụ: \mat{$Right$} chuyển đến \mat{$\{2,4,6,8\}$}. <u>Giải pháp</u>??
}
 

,4\maxfigwidth
\raisebox{-0.35\maxfigwidth}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-space.png)}

---
## Ví dụ: thế giới chân không

\hbox{
\note{Trạng thái đơn}, bắt đầu bằng \#5. <u>Giải pháp</u>?? 

\mat{$[Right,Suck]$}

[0,5\baselineskip]
\note{Conformant}, bắt đầu trong \mat{$\{1,2,3,4,5,6,7,8\}$}

ví dụ: \mat{$Right$} chuyển đến \mat{$\{2,4,6,8\}$}. <u>Giải pháp</u>??

\mat{$[Right,Suck,Left,Suck]$}

[0,5\baselineskip]
\note{Dự phòng}, bắt đầu trong \#5

Định luật Murphy: \mat{$Suck$} có thể làm bẩn một tấm thảm sạch

Cảm biến cục bộ: bụi bẩn, chỉ vị trí.

<u>Giải pháp</u>??
}
 

,4\maxfigwidth
\raisebox{-0.35\maxfigwidth}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-space.png)}

---
## Ví dụ: thế giới chân không

\hbox{
\note{Trạng thái đơn}, bắt đầu bằng \#5. <u>Giải pháp</u>?? 

\mat{$[Right,Suck]$}

[0,5\baselineskip]
\note{Conformant}, bắt đầu trong \mat{$\{1,2,3,4,5,6,7,8\}$}

ví dụ: \mat{$Right$} chuyển đến \mat{$\{2,4,6,8\}$}. <u>Giải pháp</u>??

\mat{$[Right,Suck,Left,Suck]$}

[0,5\baselineskip]
\note{Dự phòng}, bắt đầu trong \#5

Định luật Murphy: \mat{$Suck$} có thể làm bẩn một tấm thảm sạch

Cảm biến cục bộ: bụi bẩn, chỉ vị trí.

<u>Giải pháp</u>??

\mat{$[Right,\k{if}\ dirt\ \k{then}\ Suck]$}
}
 

,4\maxfigwidth
\raisebox{-0.35\maxfigwidth}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-space.png)}

---
## Xây dựng bài toán trạng thái đơn

Sự cố \defn{} được xác định bởi bốn mục:

\defn{trạng thái ban đầu}  &nbsp;&nbsp;  ví dụ: "tại Arad"

\defn{hàm kế tiếp} \mat{$S(x)$} = tập hợp các cặp hành động--trạng thái 
    
ví dụ: \mat{$S(Arad) = \{\<Arad\rightarrow Zerind, Zerind\>, \ldots \}$}

\defn{kiểm tra mục tiêu}, có thể là
    
\note{rõ ràng}, ví dụ: \mat{$x$} = "tại Bucharest"
    
\note{ẩn}, ví dụ: \mat{$NoDirt(x)$}

\defn{chi phí đường dẫn} (phụ gia)
    
ví dụ: tổng khoảng cách, số hành động được thực hiện, v.v.
    
\mat{$c(x,a,y)$} là \defn{chi phí bước}, giả định là \mat{$\geq 0$}

Giải pháp \defn{} là một chuỗi hành động

dẫn từ trạng thái ban đầu đến trạng thái mục tiêu

---
## Chọn không gian trạng thái

Thế giới thực phức tạp đến mức ngớ ngẩn 
    
Không gian trạng thái $\Rightarrow$ phải được *trừu tượng* để giải quyết vấn đề

(Tóm tắt) trạng thái = tập hợp các trạng thái thực

(Tóm tắt) hành động = sự kết hợp phức tạp của các hành động thực tế
    
   ví dụ: "Arad $\rightarrow$ Zerind" đại diện cho một tập hợp phức tạp
      
   về các tuyến đường có thể, đường vòng, điểm dừng nghỉ, v.v. 

Để đảm bảo khả năng thực hiện được, *bất kỳ* trạng thái thực " ở Arad"
  
phải đến \note{some} trạng thái thực " ở Zerind "

(Tóm tắt) giải pháp = 
    
   tập hợp các đường dẫn thực sự là giải pháp trong thế giới thực

Mỗi hành động trừu tượng phải "dễ dàng hơn" so với vấn đề ban đầu!

---
##  Ví dụ: đồ thị không gian trạng thái thế giới chân không 

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>trạng thái</u>??

<u>hành động</u>??

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường đi</u>??

---
##  Ví dụ: đồ thị không gian trạng thái thế giới chân không 

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>state</u>??: số nguyên bụi bẩn và vị trí robot (bỏ qua bụi bẩn \note{số lượng}, v.v.)

<u>hành động</u>??

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường dẫn</u>??

---
##  Ví dụ: đồ thị không gian trạng thái thế giới chân không 

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>state</u>??: số nguyên bụi bẩn và vị trí robot (bỏ qua bụi bẩn \note{số lượng}, v.v.)

<u>hành động</u>??: \mat{$Left$}, \mat{$Right$}, \mat{$Suck$}, \mat{$NoOp$}

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường dẫn</u>??

---
##  Ví dụ: đồ thị không gian trạng thái thế giới chân không 

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>state</u>??: số nguyên bụi bẩn và vị trí robot (bỏ qua bụi bẩn \note{số lượng}, v.v.)

<u>hành động</u>??: \mat{$Left$}, \mat{$Right$}, \mat{$Suck$}, \mat{$NoOp$}

<u>kiểm tra mục tiêu</u>??: không có bụi bẩn

<u>chi phí đường dẫn</u>??

---
##  Ví dụ: đồ thị không gian trạng thái thế giới chân không 

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-paths.png)

<u>state</u>??: số nguyên bụi bẩn và vị trí robot (bỏ qua bụi bẩn \note{số lượng}, v.v.)

<u>hành động</u>??: \mat{$Left$}, \mat{$Right$}, \mat{$Suck$}, \mat{$NoOp$}

<u>kiểm tra mục tiêu</u>??: không có bụi bẩn

<u>chi phí đường dẫn</u>??: 1 cho mỗi hành động (0 cho \mat{$NoOp$})

---
## Ví dụ: Câu đố 8 ô

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>trạng thái</u>??

<u>hành động</u>??

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường đi</u>??

---
## Ví dụ: Câu đố 8 ô

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>state</u>??: vị trí số nguyên của các ô (bỏ qua các vị trí trung gian)

<u>hành động</u>??

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường đi</u>??

---
## Ví dụ: Câu đố 8 ô

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>state</u>??: vị trí số nguyên của các ô (bỏ qua các vị trí trung gian)

<u>actions</u>??: di chuyển trống sang trái, phải, lên, xuống (bỏ qua việc gỡ nhiễu, v.v.)

<u>kiểm tra mục tiêu</u>??

<u>chi phí đường đi</u>??

---
## Ví dụ: Câu đố 8 ô

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>state</u>??: vị trí số nguyên của các ô (bỏ qua các vị trí trung gian)

<u>actions</u>??: di chuyển trống sang trái, phải, lên, xuống (bỏ qua việc gỡ nhiễu, v.v.)

<u>kiểm tra mục tiêu</u>??: = trạng thái mục tiêu (đã cho)

<u>chi phí đường đi</u>??

---
## Ví dụ: Câu đố 8 ô

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/8puzzle.png)

<u>state</u>??: vị trí số nguyên của các ô (bỏ qua các vị trí trung gian)

<u>actions</u>??: di chuyển trống sang trái, phải, lên, xuống (bỏ qua việc gỡ nhiễu, v.v.)

<u>kiểm tra mục tiêu</u>??: = trạng thái mục tiêu (đã cho)

<u>chi phí đường dẫn</u>??: 1 mỗi lần di chuyển

[Lưu ý: giải pháp tối ưu của $n$-Puzzle là NP-hard]

---
## Ví dụ: lắp ráp robot

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/stanford-arm+blocks.png)

<u>state</u>??: tọa độ có giá trị thực của các góc khớp robot
    
các bộ phận của đối tượng được lắp ráp

<u>hành động</u>??: chuyển động liên tục của các khớp robot

<u>kiểm tra mục tiêu</u>??: lắp ráp hoàn chỉnh *không bao gồm robot!*

<u>chi phí đường dẫn</u>??: thời gian thực hiện

---
## Thuật toán tìm kiếm cây

Ý tưởng cơ bản:
  
ngoại tuyến, mô phỏng khám phá không gian trạng thái
  
bằng cách tạo ra những trạng thái kế thừa đã được khám phá
      
(còn gọi là trạng thái  \defn{mở rộng })

```text
function Tree-Search(problem, strategy) returns a solution, or failure
    initialize the search tree using the initial state of problem
    loop do
          if there are no candidates for expansion then return failure
          choose a leaf node for expansion according to strategy
          if the node contains a goal state then return the corresponding solution
          else expand the node and add the resulting nodes to the search tree
    end
```

---
## Ví dụ tìm kiếm cây

![Hình ảnh](../TaiLieu/slide_md/figures/search-map1.png)

---
## Ví dụ tìm kiếm cây

![Hình ảnh](../TaiLieu/slide_md/figures/search-map2.png)

---
## Ví dụ tìm kiếm cây

![Hình ảnh](../TaiLieu/slide_md/figures/search-map3.png)

---
## Triển khai: trạng thái so với. nút

Trạng thái \defn{} là (biểu thị của) cấu hình vật lý

Nút \defn{} là cấu trúc dữ liệu cấu thành một phần của cây tìm kiếm
    
    bao gồm \note{parent}, \note{children}, \note{deep}, \note{path cost} \mat{$g(x)$}

Hoa không có cha mẹ, con cái, độ sâu, hoặc chi phí đường đi!

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/state-vs-node.png)

Hàm **Expand** tạo các nút mới, điền vào các nút khác nhau
các trường và sử dụng {\s SuccessorFn} của
bài toán để tạo ra các trạng thái tương ứng.

---
## Thực hiện: tìm kiếm cây tổng quát

```text
function Tree-Search(problem, \var{fringe)}{a solution, or failure}
    fringe <- Insert(Make-Node(Initial-State[problem]), fringe)
    loop do
          if fringe is empty then return failure
          node <- Remove-Front(fringe)
          if Goal-Test(problem, State(node)) then return node       
          fringe <- InsertAll(Expand(node, problem), fringe)

\fnsep
function Expand(node, \var{problem)}{a set of nodes}
    successors <- the empty set
    for each action, result in Successor-Fn(problem, State[node]) do
          s <- a new Node
          Parent-Node[s] <- node;  Action[s] <- action;  State[s] <- result
          Path-Cost[s] <- Path-Cost[node] + Step-Cost(State[node], action, result)
          Depth[s] <- Depth[node] + 1
          add s to successors
    return successors
```

---
## Chiến lược tìm kiếm

Chiến lược được xác định bằng cách chọn thứ tự *mở rộng nút*

Các chiến lược được đánh giá theo các khía cạnh sau:
    
\defn{tính đầy đủ}---nó có luôn tìm ra giải pháp nếu có không?
    
\defn{độ phức tạp về thời gian}---số lượng nút được tạo/mở rộng
    
\defn{Độ phức tạp của không gian}---số lượng nút tối đa trong bộ nhớ
    
\defn{optimality}---nó có luôn tìm ra giải pháp có chi phí thấp nhất không?

Độ phức tạp về thời gian và không gian được đo bằng 
    
\mat{$b$}---hệ số phân nhánh tối đa của cây tìm kiếm
    
\mat{$d$}---độ sâu của giải pháp chi phí thấp nhất
    
\mat{$m$}---độ sâu tối đa của không gian trạng thái (có thể là \mat{$\infty$})

---
## Chiến lược tìm kiếm không chính xác

Chiến lược \defn{Uninformed} chỉ sử dụng thông tin có sẵn

trong định nghĩa vấn đề

Tìm kiếm theo chiều rộng

Tìm kiếm chi phí thống nhất

Tìm kiếm theo chiều sâu

Tìm kiếm giới hạn độ sâu

Tìm kiếm sâu hơn lặp đi lặp lại

---
## Tìm kiếm theo chiều rộng

Mở rộng nút nông nhất chưa được mở rộng

*Triển khai*:
    
\v{fringe} là một hàng đợi FIFO, tức là những người kế nhiệm mới sẽ ở cuối

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/bfs-progress1.png)

---
## Tìm kiếm theo chiều rộng

Mở rộng nút nông nhất chưa được mở rộng

*Triển khai*:
    
\v{fringe} là một hàng đợi FIFO, tức là những người kế nhiệm mới sẽ ở cuối

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/bfs-progress2.png)

---
## Tìm kiếm theo chiều rộng

Mở rộng nút nông nhất chưa được mở rộng

*Triển khai*:
    
\v{fringe} là một hàng đợi FIFO, tức là những người kế nhiệm mới sẽ ở cuối

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/bfs-progress3.png)

---
## Tìm kiếm theo chiều rộng

Mở rộng nút nông nhất chưa được mở rộng

*Triển khai*:
    
\v{fringe} là một hàng đợi FIFO, tức là những người kế nhiệm mới sẽ ở cuối

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/bfs-progress4.png)

---
## Thuộc tính tìm kiếm theo chiều rộng

<u>Hoàn thành</u>?? 

---
## Thuộc tính tìm kiếm theo chiều rộng

<u>Hoàn thành</u>?? Có (nếu \mat{$b$} là hữu hạn)

<u>Thời gian</u>?? 

---
## Thuộc tính tìm kiếm theo chiều rộng

<u>Hoàn thành</u>?? Có (nếu \mat{$b$} là hữu hạn)

<u>Thời gian</u>?? \mat{$1+b+b^2+b^3+\ldots +b^d + b(b^d-1)= O(b^{d+1})$}, tức là exp. in \mat{$d$}

<u>Không gian</u>?? 

---
## Thuộc tính tìm kiếm theo chiều rộng

<u>Hoàn thành</u>?? Có (nếu \mat{$b$} là hữu hạn)

<u>Thời gian</u>?? \mat{$1+b+b^2+b^3+\ldots +b^d + b(b^d-1)= O(b^{d+1})$}, tức là exp. in \mat{$d$}

<u>Space</u>?? \mat{$O(b^{d+1})$} (giữ mọi nút trong bộ nhớ)

<u>Tối ưu</u>?? 

---
## Thuộc tính tìm kiếm theo chiều rộng

<u>Hoàn thành</u>?? Có (nếu \mat{$b$} là hữu hạn)

<u>Thời gian</u>?? \mat{$1+b+b^2+b^3+\ldots +b^d + b(b^d-1)= O(b^{d+1})$}, tức là exp. in \mat{$d$}

<u>Space</u>?? \mat{$O(b^{d+1})$} (giữ mọi nút trong bộ nhớ)

<u>Tối ưu</u>?? Có (nếu chi phí = 1 mỗi bước); nói chung là không tối ưu

*Không gian* là vấn đề lớn; có thể dễ dàng tạo các nút ở tốc độ 100MB/giây
    
vậy 24 giờ = 8640GB.

---
## Tìm kiếm chi phí thống nhất

Mở rộng nút chưa được mở rộng với chi phí thấp nhất

*Triển khai*:
    
\v{fringe} = hàng đợi được sắp xếp theo chi phí đường dẫn, thấp nhất trước

Tương đương với chiều rộng đầu tiên nếu chi phí bước đều bằng nhau

<u>Hoàn thành</u>?? Có, nếu chi phí bước \mat{$\geq \epsilon$}

<u>Thời gian</u>?? \# nút có \mat{$g \leq {}$} chi phí cho giải pháp tối ưu, \mat{$O(b^{\ceiling{C^*/\epsilon}})$}
  
trong đó \mat{$C^*$} là chi phí của giải pháp tối ưu

<u>Không gian</u>?? \# nút có \mat{$g \leq {}$} chi phí của giải pháp tối ưu, \mat{$O(b^{\ceiling{C^*/\epsilon}})$}

<u>Tối ưu</u>?? Có---các nút được mở rộng theo thứ tự tăng dần \mat{$g(n)$}

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress01.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress02.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress03.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress04.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress05.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress06.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress07.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress08.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress09.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress10.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress11.png)

---
## Tìm kiếm theo chiều sâu

Mở rộng nút chưa được mở rộng sâu nhất

*Triển khai*:
    
\v{fringe} = Hàng đợi LIFO, tức là đặt những người kế nhiệm lên hàng đầu

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dfs-progress12.png)

---
## Thuộc tính tìm kiếm theo chiều sâu

<u>Hoàn thành</u>?? 

---
## Thuộc tính tìm kiếm theo chiều sâu

<u>Hoàn thành</u>?? Không: thất bại trong không gian có độ sâu vô hạn, không gian có vòng lặp
    
Sửa đổi để tránh các trạng thái lặp lại dọc theo đường dẫn 
      
$\Rightarrow$ hoàn thành trong không gian hữu hạn

<u>Thời gian</u>?? 

---
## Thuộc tính tìm kiếm theo chiều sâu

<u>Hoàn thành</u>?? Không: thất bại trong không gian có độ sâu vô hạn, không gian có vòng lặp
    
Sửa đổi để tránh các trạng thái lặp lại dọc theo đường dẫn 
      
$\Rightarrow$ hoàn thành trong không gian hữu hạn

<u>Thời gian</u>?? \mat{$O(b^m)$}: khủng khiếp nếu \mat{$m$} lớn hơn nhiều so với \mat{$d$}
    
        nhưng nếu các giải pháp dày đặc, có thể nhanh hơn nhiều so với chiều rộng đầu tiên

<u>Không gian</u>??

---
## Thuộc tính tìm kiếm theo chiều sâu

<u>Hoàn thành</u>?? Không: thất bại trong không gian có độ sâu vô hạn, không gian có vòng lặp
    
Sửa đổi để tránh các trạng thái lặp lại dọc theo đường dẫn 
      
$\Rightarrow$ hoàn thành trong không gian hữu hạn

<u>Thời gian</u>?? \mat{$O(b^m)$}: khủng khiếp nếu \mat{$m$} lớn hơn nhiều so với \mat{$d$}
    
        nhưng nếu các giải pháp dày đặc, có thể nhanh hơn nhiều so với chiều rộng đầu tiên

<u>Không gian</u>?? \mat{$O(bm)$}, tức là không gian tuyến tính!

<u>Tối ưu</u>?? 

---
## Thuộc tính tìm kiếm theo chiều sâu

<u>Hoàn thành</u>?? Không: thất bại trong không gian có độ sâu vô hạn, không gian có vòng lặp
    
Sửa đổi để tránh các trạng thái lặp lại dọc theo đường dẫn 
      
$\Rightarrow$ hoàn thành trong không gian hữu hạn

<u>Thời gian</u>?? \mat{$O(b^m)$}: khủng khiếp nếu \mat{$m$} lớn hơn nhiều so với \mat{$d$}
    
        nhưng nếu các giải pháp dày đặc, có thể nhanh hơn nhiều so với chiều rộng đầu tiên

<u>Không gian</u>?? \mat{$O(bm)$}, tức là không gian tuyến tính!

<u>Tối ưu</u>?? Không

---
## Tìm kiếm giới hạn độ sâu

= tìm kiếm theo chiều sâu với giới hạn độ sâu \mat{$l$},

tức là các nút ở độ sâu \mat{$l$} không có nút kế thừa

*Triển khai đệ quy*: 

```text
function Depth-Limited-Search(problem, limit) returns soln/fail/cutoff
    Recursive-DLS(Make-Node(Initial-State[problem]), problem, limit)

function Recursive-DLS(node, problem, limit) returns soln/fail/cutoff
    cutoff-occurred? <- false
    if Goal-Test(problem, State[node]) then return node
    else if Depth[node] = limit then return cutoff
    else for each successor in Expand(node, problem) do
          result <- Recursive-DLS(successor, problem, limit)
          if result = cutoff then cutoff-occurred? <- true
          else if result != failure then return result
    if cutoff-occurred? then return cutoff else return failure
```

---
## Tìm kiếm chuyên sâu lặp lại

```text
function Iterative-Deepening-Search(problem) returns a solution
        inputs: problem, a problem

      for depth 0 to infinity do
          result <- Depth-Limited-Search(problem, depth)
          if result != cutoff then return result
      end
```

---
## Tìm kiếm sâu lặp đi lặp lại \mat{$l=0$
}

![Hình ảnh](../TaiLieu/slide_md/figures/ids-progress1.png)

---
## Tìm kiếm sâu lặp đi lặp lại \mat{$l=1$
}

![Hình ảnh](../TaiLieu/slide_md/figures/ids-progress2.png)

---
## Tìm kiếm sâu lặp đi lặp lại \mat{$l=2$
}

![Hình ảnh](../TaiLieu/slide_md/figures/ids-progress3.png)

---
## Tìm kiếm sâu lặp đi lặp lại \mat{$l=3$
}

![Hình ảnh](../TaiLieu/slide_md/figures/ids-progress4.png)

---
## Thuộc tính của tìm kiếm sâu lặp đi lặp lại

<u>Hoàn thành</u>?? 

---
## Thuộc tính của tìm kiếm sâu lặp đi lặp lại

<u>Hoàn thành</u>?? Có

<u>Thời gian</u>?? 

---
## Thuộc tính của tìm kiếm sâu lặp đi lặp lại

<u>Hoàn thành</u>?? Có

<u>Thời gian</u>?? \mat{$(d+1)b^0 + d b^1 + (d-1)b^2 + \ldots + b^d = O(b^d)$}

<u>Không gian</u>?? 

---
## Thuộc tính của tìm kiếm sâu lặp đi lặp lại

<u>Hoàn thành</u>?? Có

<u>Thời gian</u>?? \mat{$(d+1)b^0 + d b^1 + (d-1)b^2 + \ldots + b^d = O(b^d)$}

<u>Không gian</u>?? \mat{$O(bd)$}

<u>Tối ưu</u>?? 

---
## Thuộc tính của tìm kiếm sâu lặp đi lặp lại

<u>Hoàn thành</u>?? Có

<u>Thời gian</u>?? \mat{$(d+1)b^0 + d b^1 + (d-1)b^2 + \ldots + b^d = O(b^d)$}

<u>Không gian</u>?? \mat{$O(bd)$}

<u>Tối ưu</u>?? Có, nếu chi phí bước = 1
    
Có thể được sửa đổi để khám phá cây chi phí thống nhất

So sánh số cho \mat{$b=10$} và \mat{$d=5$}, giải pháp ở lá ngoài cùng bên phải:
\mat{\begin{eqnarray*}
N(\mbox{IDS}) &=& 50 + 400 + 3,000 + 20,000 + 100,000 = 123,450 

N(\mbox{BFS}) &=& 10 + 100 + 1,000 + 10,000 + 100,000 + 999,990 = 1,111,100
\end{eqnarray*}}

IDS hoạt động tốt hơn vì các nút khác ở độ sâu \mat{$d$} không được mở rộng

BFS có thể được sửa đổi để áp dụng kiểm tra mục tiêu khi một nút được tạo \emph{}

---
## Tóm tắt thuật toán

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|
| \raisebox{-0.5\baselineskip}[0pt][0pt]{Criterion} | Breadth- | Uniform- | Depth- | Depth- | Iterative |
|  | First | Cost | First | Limited | Deepening |
| \rule{0pt}{3ex}Complete? | Yes$^*$ | Yes$^*$ | No | Yes, if $l \ge d$ | Yes |
| Time | $b^{d+1}$ | $b^{\ceiling{C^*/\epsilon}}$ | $b^m$ | $b^l$ | $b^d$ |
| Space | $b^{d+1}$ | $b^{\ceiling{C^*/\epsilon}}$ | $bm$ | $bl$ | $bd$ |
| Optimal? | Yes$^*$ | Yes | No | No | Yes$^*$ |

---
## Trạng thái lặp lại

Việc không phát hiện được các trạng thái lặp lại có thể biến một bài toán tuyến tính thành một bài toán
số mũ!

,7\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/ribbon-space.png)

---
## Tìm kiếm đồ thị

```text
function Graph-Search(problem, \var{fringe)}{a solution, or failure}

    closed <- an empty set
    fringe <- Insert(Make-Node(Initial-State[problem]), fringe)
    loop do
          if fringe is empty then return failure
          node <- Remove-Front(fringe)
          if Goal-Test(problem, State[node]) then return node       
          if State[node] is not in closed then
                add State[node] to closed
                fringe <- InsertAll(Expand(node, problem), fringe)
    end
```

---
## Tóm tắt

Việc xây dựng vấn đề thường yêu cầu trừu tượng hóa các chi tiết trong thế giới thực
để xác định một không gian trạng thái có thể được khám phá

Sự đa dạng của các chiến lược tìm kiếm không chính xác

Tìm kiếm sâu hơn lặp lại chỉ sử dụng không gian tuyến tính

và không mất nhiều thời gian hơn các thuật toán chưa hiểu rõ khác

Tìm kiếm đồ thị có thể hiệu quả hơn theo cấp số nhân so với tìm kiếm cây