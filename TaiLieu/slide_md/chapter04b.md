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