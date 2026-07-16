\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Suy diễn trong mạng Bayes (Inference in Bayesian networks)

## Chương 14.4--5

---
## Phác thảo

- Suy luận chính xác bằng cách liệt kê

- Suy luận chính xác bằng cách loại bỏ biến

- Suy luận gần đúng bằng mô phỏng ngẫu nhiên

- Suy luận gần đúng của chuỗi Markov Monte Carlo

---
## Nhiệm vụ suy luận

\defn{Truy vấn đơn giản}: tính biên sau \mat{$P(X_i|\mbf{E}\eq \e)$}
  
  ví dụ: \mat{$P(NoGas|Gauge\eq empty,Lights\eq on,Starts\eq false)$}

\defn{Truy vấn liên kết}: \mat{$P(X_i,X_j|\mbf{E}\eq \e) = 
    P(X_i|\mbf{E}\eq \e)  P(X_j|X_i,\mbf{E}\eq \e) $}

\defn{Quyết định tối ưu}: mạng quyết định bao gồm thông tin tiện ích;
    
    suy luận xác suất cần thiết cho \mat{$P(outcome|action,evidence)$}

\defn{Giá trị của thông tin}: cần tìm kiếm bằng chứng nào tiếp theo?

\defn{Phân tích độ nhạy}: giá trị xác suất nào là quan trọng nhất?

\defn{Giải thích}: tại sao tôi cần động cơ khởi động mới?

---
## Suy luận bằng phép liệt kê

Cách hơi thông minh để tính tổng các biến từ khớp
mà không thực sự xây dựng sự biểu diễn rõ ràng của nó

Truy vấn đơn giản trên mạng trộm:\hspace*{2.5in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/burglary-small.png)

\mat{$P(B|j,m)$}

\mat{$= P(B,j,m)/P(j,m)$}

\mat{$= 
  pha P(B,j,m)$}

\mat{$= 
  pha \ \mysum_e \ \mysum_a \ P(B,e,a,j,m)$}

Viết lại toàn bộ các mục chung sử dụng tích của các mục CPT:

\mat{$P(B|j,m)$}

\mat{$= 
  pha \ \mysum_e \ \mysum_a \ P(B)P(e)P(a|B,e)P(j|a)P(m|a) $}

\mat{$= 
  pha P(B)\ \mysum_e\ P(e)\ \mysum_a\ P(a|B,e)P(j|a)P(m|a)$}
       
Đệ quy liệt kê theo chiều sâu đầu tiên: \mat{$O(n)$} không gian, \mat{$O(d^n)$} thời gian

---
## Thuật toán liệt kê

```text
function Enumeration-Ask(\v{X), $\e$, \v{bn}}{a distribution over \v{X}}
    \firstinputs{\v{X}} {the query variable}
    \inputs{\v{\e}}{observed values for variables $\E$}
    \inputs{\v{bn}}{a Bayesian network with variables $\{X\} \union \E \union \Y$}

    $Q(\v{X)$}{a distribution over \v{X}, initially empty}
    \k{for each} value \v{$x_i$} of \v{X} \k{do}
          extend \v{$\e$} with value \v{$x_i$} for \v{X}
          $Q(\v{x_i)$}{Enumerate-All(Vars[\v{bn}], \v{$\e$})}
    \k{return} Normalize($Q(\v{X})$)
\fnsep
function Enumerate-All(\v{vars), $\e$}{a real number}
    \k{if} Empty?(\v{vars}) \k{then return} 1.0
    \v{Y}{First(\v{vars})}
    \k{if} \v{Y} has value \v{y} in \v{$\e$}
          \k{then return} $P(\v{y} | Pa(\v{Y})) \times {}$Enumerate-All(Rest(\v{vars}), \v{$\e$})
          \k{else return} $\sum_{\v{y}} P(\v{y} | Pa(\v{Y})) \times {}$Enumerate-All(Rest(\v{vars}), $\v{\e}_{\v{y}}$)
                where $\v{\e}_{\v{y}}$ is $\v{\e}$ extended with $\v{Y}\eq \v{y}$
```

---
## Cây đánh giá

![Hình ảnh](../TaiLieu/slide_md/figures/enumeration-tree.png)

Việc liệt kê không hiệu quả: tính toán lặp đi lặp lại 
  
  ví dụ: tính \mat{$P(j|a)P(m|a)$} cho mỗi giá trị của \mat{$e$}

---
## Suy luận bằng cách loại bỏ biến

Loại bỏ biến: thực hiện tính tổng từ phải sang trái,

lưu trữ kết quả trung gian (\defn{factors}) để tránh tính toán lại

\mat{$P(B|j,m)$}
    
    \mat{$= 
  pha \underbrace{P(B)}_B 
             \mysum_e \underbrace{P(e)}_E
             \mysum_a \underbrace{P(a|B,e)}_A
             \underbrace{P(j|a)}_J
             \underbrace{P(m|a)}_M$}
    
    \mat{$= 
  pha P(B)\mysum_e P(e)\mysum_a P(a|B,e) P(j|a) f_M(a)$}
    
    \mat{$= 
  pha P(B)\mysum_e P(e)\mysum_a P(a|B,e) f_J(a) f_M(a)$}
    
    \mat{$= 
  pha P(B)\mysum_e P(e)\mysum_a f_A(a,b,e) f_J(a) f_M(a)$}
    
    \mat{$= 
  pha P(B)\mysum_e P(e)f_{\bar{A}JM}(b,e) $} (tổng \mat{$A$})
    
    \mat{$= 
  pha P(B)f_{\bar{E}\bar{A}JM}(b)$} (tổng \mat{$E$})
    
    \mat{$= 
  pha f_B(b)\stimes f_{\bar{E}\bar{A}JM}(b)$} 

---
## Loại bỏ biến: Các thao tác cơ bản

\defn{Tính tổng} một biến từ tích của các thừa số: 
  
  di chuyển bất kỳ yếu tố không đổi nào ra ngoài phép tính tổng 
  
  cộng các ma trận con theo tích từng điểm của các thừa số còn lại

\mat{$\mysum_x f_1 \stimes \cdots \stimes f_k =
f_1 \stimes \cdots \stimes f_i\  \mysum_x\; f_{i+1} \stimes \cdots \stimes
f_k = f_1 \stimes \cdots \stimes f_i \stimes f_{\bar{X}}$}

giả sử \mat{$f_1,\ldots,f_i$} không phụ thuộc vào \mat{$X$}

\defn{Tích điểm} của thừa số \mat{$f_1$} và \mat{$f_2$}:
  
  \mat{$f_1(x_1,\ldots,x_j,y_1,\ldots,y_k) \stimes
     f_2(y_1,\ldots,y_k,z_1,\ldots,z_l)$}
    
  = \mat{$f(x_1,\ldots,x_j,y_1,\ldots,y_k,z_1,\ldots,z_l)$}

Ví dụ: \mat{$f_1(a,b) \stimes f_2(b,c) = f(a,b,c)$}

---
## Thuật toán loại bỏ biến 

```text
function Elimination-Ask(\v{X), \e, \v{bn}}{a distribution over \v{X}}
      inputs: X, the query variable
      inputs: \e, evidence specified as an event
      inputs: bn, a belief network specifying joint distribution $P(X_1,\ldots,X_n)$

    \v{factors}{$\emptylist$}; \v{vars}{Reverse(Vars[\v{bn}])}
    \k{for each} \v{var} \k{in} \v{vars} \k{do}
          \v{factors}{$[Make-Factor(\v{var}, \v{\e})|\v{factors}]$}
          \k{if} \v{var} is a hidden variable \k{then} \v{factors}{Sum-Out(\v{var}, \v{factors})}
    \k{return} Normalize(Pointwise-Product(\v{factors}))
```

---
## Các biến không liên quan

Hãy xem xét truy vấn \mat{$P(JohnCalls|Burglary\eq true)$}\hspace*{1.0in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/burglary-small.png)}
\mat{\[
  P(J|b) = 
  pha P(b) \sum_e P(e) \sum_a P(a|b,e) P(J|a) \sum_m P(m|a)
\]}
Tổng trên \mat{$m$} giống hệt 1; \mat{$M$} là *không liên quan* với truy vấn

Thm 1: \mat{$Y$} không liên quan trừ khi \mat{$Y\elt Ancestors(\{X\}\union \E)$}

Đây, \mat{$X\eq JohnCalls$}, \mat{$\E\eq\{Burglary\}$} và 

\mat{$Ancestors(\{X\}\union \E) = \{Alarm,Earthquake\}$}

vì vậy \mat{$MaryCalls$} không liên quan

(So sánh điều này với chuỗi ngược từ truy vấn trong KB mệnh đề Horn)

---
## Các biến không liên quan tiếp.

Defn: \underline{biểu đồ đạo đức} của Bayes net: kết hôn với tất cả cha mẹ và mũi tên thả

Định nghĩa: \mat{$\A$} được phân tách bằng \underline{m} khỏi \mat{$\B$} bởi \mat{$\C$} nếu được phân tách bằng \mat{$\C$} trong biểu đồ đạo đức

Thm 2: \mat{$Y$} không liên quan nếu m được phân tách khỏi \mat{$X$} bởi \mat{$\E$}\hspace*{1.0in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/burglary-moral.png)}

Đối với \mat{$P(JohnCalls|Alarm\eq true)$}, cả 

\mat{$Burglary$} và \mat{$Earthquake$} không liên quan

---
## Độ phức tạp của suy luận chính xác

\defn{Mạng được kết nối đơn} (hoặc \defn{polytrees}):
  
  -- bất kỳ hai nút nào cũng được kết nối bằng nhiều nhất một đường dẫn (vô hướng)
  
  -- chi phí về thời gian và không gian của việc loại bỏ biến đổi là \mat{$O(d^k n)$}

\defn{Các mạng được kết nối nhiều lần}:
  
  -- có thể giảm 3SAT để suy luận chính xác \mat{$\implies$} NP-hard
  
  -- tương đương với *đếm* kiểu 3SAT \mat{$\implies$} \#P-complete

![Hình ảnh](../TaiLieu/slide_md/figures/bn-3sat.png)

---
## Suy luận bằng mô phỏng ngẫu nhiên

Ý tưởng cơ bản:
  
  1) Vẽ \mat{$N$} mẫu từ phân phối lấy mẫu \mat{$S$}\hspace*{1.5in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/coin-flip.png)
  
  2) Tính xác suất hậu nghiệm gần đúng \mat{$\hat P$}
  
  3) Chứng tỏ điều này hội tụ về xác suất đúng \mat{$P$}

Tóm tắt:
  
  -- Lấy mẫu từ mạng trống
  
  -- Lấy mẫu từ chối: từ chối các mẫu không đồng ý với bằng chứng
  
  -- Trọng số khả năng: sử dụng bằng chứng để cân mẫu
  
  -- Chuỗi Markov Monte Carlo (MCMC): mẫu từ quá trình ngẫu nhiên
    
      có phân bố cố định là phần sau thực sự

---
## Lấy mẫu từ mạng trống

```text
function Prior-Sample(\v{bn)}{an event sampled from \v{bn}}
      inputs: bn, a belief network specifying joint distribution $P(X_1,\ldots,X_n)$

    \v{\x}{an event with $n$ elements}
    \k{for} $i = 1$ \k{to} $n$ \k{do}
          $\v{x_i$}{a random sample from $P(X_i | \parents(X_i))$}
               given the values of $\Parents(X_i)$ in \v{\x}
    \k{return} \v{\x}
```

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample1.png)

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample2.png)

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample3.png)

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample4.png)

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample5.png)

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample6.png)

---
## Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/rain-prior-sample7.png)

---
## Lấy mẫu từ mạng trống tiếp theo.

Xác suất \prog{PriorSample} tạo ra một sự kiện cụ thể
  
  \mat{$S_{PS}(x_1\ldots x_n) = \myprod_{i\eq 1}^n P(x_i | \parents(X_i))
    = P(x_1\ldots x_n)$}

tức là xác suất trước thực sự

Ví dụ: \mat{$S_{PS}(t, f, t, t) = 0.5 \stimes 0.9 \stimes 0.8 \stimes 0.9 = 0.324 = P(t, f, t,t)$}

Gọi \mat{$N_{PS}(x_1\ldots x_n)$} là số lượng mẫu được tạo
cho sự kiện \mat{$x_1,\ldots, x_n$}

Sau đó chúng tôi có
\mat{\begin{eqnarray*}
  \lim_{N\to\infty} \hat P(x_1,\ldots, x_n) 
      & = & \lim_{N\to\infty} N_{PS}(x_1,\ldots, x_n)/N 

      & = & S_{PS}(x_1,\ldots,x_n) 

      & = & P(x_1\ldots x_n)
\end{eqnarray*}}
Nghĩa là, các ước tính bắt nguồn từ \prog{PriorSample} là \defn{nhất quán}

Viết tắt: \mat{$\hat P(x_1,\ldots, x_n) \approx P(x_1\ldots x_n)$}

---
## Lấy mẫu loại bỏ

\mat{$\hat{P}(X|\e)$} được ước tính từ các mẫu phù hợp với \mat{$\e$}

```text
function Rejection-Sampling(\v{X), \v{\e}, \v{bn}, \v{N}}{an estimate of $P(\v{X}|\v{\e})$}
    \firstlocal{\mbf{N}}{a vector of counts over \v{X}, initially zero}

    \k{for} \v{j} = 1 to \v{N} \k{do}
          \v{\x}{Prior-Sample(\v{bn})}
          \k{if} \v{\x} is consistent with \v{\e} \k{then}
              \mbf{N[\v{x}]}{\mbf{N}[\v{x}]+1} where \v{x} is the value of \v{X} in \v{\x}
    \k{return} Normalize(\mbf{N}[\v{X}])
```

Ví dụ: ước tính \mat{$P(Rain|Sprinkler\eq true)$} sử dụng 100 mẫu 
  
  27 mẫu có \mat{$Sprinkler\eq true$}
    
    Trong số này, 8 có \mat{$Rain\eq true$} và 19 có \mat{$Rain\eq false$}.
[0.2in]
\mat{$\hat{P}(Rain|Sprinkler\eq true) = \noprog{Normalize}(\<8,19\>) =
\<0.296,0.704\>$}

Tương tự như quy trình ước lượng thực nghiệm cơ bản trong thế giới thực

---
## Phân tích lấy mẫu từ chối

\mat{$\hat{P}(X|\e) = 
  pha \mbf{N}_{PS}(X,\e) $} 
    &nbsp;&nbsp;&nbsp;&nbsp;  (định nghĩa thuật toán)
  
\mat{$= \mbf{N}_{PS}(X,\e)/N_{PS}(\e)$} 
    &nbsp;&nbsp;&nbsp;&nbsp;  (chuẩn hóa bởi \mat{$N_{PS}(\e)$})
  
\mat{$\approx P(X,\e)/P(\e)$} 
    &nbsp;&nbsp;&nbsp;&nbsp;  (thuộc tính của \prog{PriorSample})
  
\mat{$= P(X|\e)$} 
    &nbsp;&nbsp;&nbsp;&nbsp;  (định nghĩa về xác suất có điều kiện)

Do đó việc lấy mẫu từ chối trả về các ước tính sau nhất quán

Vấn đề: cực kỳ tốn kém nếu \mat{$P(\e)$} nhỏ

\mat{$P(\e)$} giảm theo cấp số nhân với số lượng biến bằng chứng!

---
## Trọng số khả năng

Ý tưởng: sửa các biến bằng chứng, chỉ lấy mẫu các biến không có bằng chứng,

và cân nhắc từng mẫu theo khả năng nó phù hợp với bằng chứng

```text
function Likelihood-Weighting(\v{X), \v{\e}, \v{bn}, \v{N}}{an estimate of $P(\v{X}|\v{\e})$}
    \firstlocal{\v{\mbf{W}}}{a vector of weighted counts over \v{X}, initially zero}

    \k{for} \v{j} = 1 to \v{N} \k{do}
          \v{\x, \v{w}}{Weighted-Sample(\v{bn})}
          $\v{\mbf{W}[\v{x}]$}{$\v{\mbf{W}}[\v{x}]+\v{w}$} where \v{x} is the value of \v{X} in \v{\x}
    \k{return} Normalize($\v{\mbf{W}}[\v{X}]$)
\fnsep
function Weighted-Sample(\v{bn), \v{\e}}{an event and a weight}

    \v{\x}{an event with $n$ elements}; \v{w}{1}
    \k{for} \v{i} = 1 \k{to} $n$ \k{do}
          \k{if} $\v{X_i}$ has a value $\v{x_i}$ in \v{\e}
                \k{then} \v{w}{$\v{w}\times P(\v{X_i}\eq \v{x_i} | \parents(\v{X_i}))$}
                \k{else} $\v{x_i$}{a random sample from $P(\v{X_i} | \parents(\v{X_i}))$}
    \k{return} \v{\x}, \v{w}
```

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample1.png)

\mat{$w = 1.0$}

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample2.png)

\mat{$w = 1.0$}

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample3.png)

\mat{$w = 1.0$}

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample3.png)

\mat{$w = 1.0 \stimes 0.1$}

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample4.png)

\mat{$w = 1.0 \stimes 0.1$}

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample5.png)

\mat{$w = 1.0 \stimes 0.1$}

---
## Ví dụ về trọng số khả năng

![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw-sample5.png)

\mat{$w = 1.0 \stimes 0.1 \stimes 0.99 = 0.099$}

---
## Phân tích trọng số khả năng

Xác suất lấy mẫu cho \prog{WeightedSample} là
  
  \mat{$S_{WS}(\mbf{z},\e) = \myprod_{i\eq 1}^l P(z_i|\parents(Z_i))$}

Lưu ý: chỉ chú ý đến bằng chứng trong *tổ tiên*\hspace*{0.3in}in\raisebox{-1.3in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw2.png)
    
    \mat{$\implies$} đâu đó "ở giữa" trước và
    
    phân bố sau

Trọng lượng của một mẫu nhất định \mat{$\mbf{z},\e$} là 
  
  \mat{$w(\mbf{z},\e) = \myprod_{i\eq 1}^m P(e_i | \parents(E_i))$}

Xác suất lấy mẫu có trọng số là 
  
  \mat{$S_{WS}(\mbf{z},\e) w(\mbf{z},\e)$}
    
    \mat{$= \myprod_{i\eq 1}^l P(z_i|\parents(Z_i))\ \ 
       \myprod_{i\eq 1}^m P(e_i|\parents(E_i))$}
    
    \mat{$= P(\mbf{z},\e)$} (theo ngữ nghĩa toàn cầu tiêu chuẩn của mạng)

Do đó, trọng số khả năng trả về ước tính nhất quán

nhưng hiệu suất vẫn suy giảm với nhiều biến số bằng chứng

vì một số mẫu có gần như toàn bộ trọng lượng

---
## Suy luận gần đúng sử dụng MCMC

"Trạng thái" của mạng = sự gán hiện tại cho tất cả các biến.

Tạo trạng thái tiếp theo bằng cách lấy mẫu một biến cho chăn Markov 

Lấy mẫu lần lượt từng biến, giữ bằng chứng cố định

```text
function MCMC-Ask(\v{X), \v{\e}, \v{bn}, \v{N}}{an estimate of $P(\v{X}|\v{\e})$}
    \firstlocal{$\v{\mbf{N}}[\v{X}]$}{a vector of counts over \v{X}, initially zero}
    \local{\mbf{Z}}{the nonevidence variables in \v{bn}}
    \local{\v{\x}}{the current state of the network, initially copied from \v{\e}}

    initialize \v{\x} with random values for the variables in \v{\mbf{Y}}
    \k{for} \v{j} = 1 to \v{N} \k{do}
          \k{for each} $\v{Z_i}$ in \v{\mbf{Z}} \k{do}
                sample the value of $\v{Z_i}$ in \v{\x} from $P(\v{Z_i}|\markovBlanket(\v{Z_i}))$ 
                      given the values of $\MarkovBlanket(\v{Z_i})$ in \v{\x}
                $\v{\mbf{N}[\v{x}]$}{$\v{\mbf{N}}[\v{x}]+1$} where \v{x} is the value of \v{X} in \v{\x}
    \k{return} Normalize($\v{\mbf{N}}[\v{X}]$)
```

Cũng có thể chọn một biến để lấy mẫu ngẫu nhiên mỗi lần

---
## Chuỗi Markov

Với \mat{$Sprinkler\eq true,WetGrass\eq true$}, có bốn trạng thái:

![Hình ảnh](../TaiLieu/slide_md/figures/rain-chain.png)

Đi loanh quanh một lúc, tính trung bình những gì bạn nhìn thấy

---
## Ví dụ MCMC tiếp theo.

Ước tính \mat{$P(Rain|Sprinkler\eq true,WetGrass\eq true)$}

Mẫu \mat{$Cloudy$} hoặc \mat{$Rain$} được cung cấp chăn Markov, lặp lại.

Đếm số lần \mat{$Rain$} đúng và sai trong các mẫu.

Ví dụ: truy cập 100 tiểu bang
  
  31 có \mat{$Rain\eq true$}, 69 có \mat{$Rain\eq false$}

\mat{$\hat{P}(Rain|Sprinkler\eq true,WetGrass\eq true)$}
  
      \mat{$= \noprog{Normalize}(\<31,69\>) = \<0.31,0.69\>$}

Định lý: phương pháp tiếp cận chuỗi \defn{phân phối cố định}: 
  
Phần thời gian dài hạn dành cho mỗi trạng thái chính xác là 
  
tỷ lệ thuận với xác suất sau của nó

---
## Lấy mẫu chăn Markov

Chăn Markov của \mat{$Cloudy$} là\hspace*{2.3in}in\raisebox{-1.3in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/rain-lw1.png)
    
    \mat{$Sprinkler$} và \mat{$Rain$}

Chăn Markov của \mat{$Rain$} là 
    
    \mat{$Cloudy$}, \mat{$Sprinkler$} và \mat{$WetGrass$}

Xác suất cho chăn Markov được tính như sau:
  
  \mat{$P(x_i'|\markovBlanket(X_i)) = P(x_i'|\parents(X_i)) 
           \myprod_{Z_j\in Children(X_i)} P(z_j|\parents(Z_j))$}

Dễ dàng triển khai trong các hệ thống song song truyền thông điệp, bộ não

Các vấn đề tính toán chính:
  
  1) Khó biết liệu đã đạt được sự hội tụ hay chưa
  
  2) Có thể lãng phí nếu chăn Markov lớn:
    
    \mat{$P(X_i|\markovBlanket(X_i))$} sẽ không thay đổi nhiều (luật số lớn)

---
## Tóm tắt

Suy luận chính xác bằng cách loại bỏ biến: 
  
 -- polytime trên polytrees, NP-hard trên đồ thị chung
  
 -- không gian = thời gian, rất nhạy cảm với cấu trúc liên kết

Suy luận gần đúng của LW, MCMC:
  
 -- LW hoạt động kém khi có nhiều bằng chứng (hạ lưu)
  
 -- LW, MCMC thường không nhạy cảm với cấu trúc liên kết
  
 -- Sự hội tụ có thể rất chậm với xác suất gần bằng 1 hoặc 0
  
 -- Có thể xử lý sự kết hợp tùy ý của các biến rời rạc và liên tục

 

---
## Phân tích MCMC: Đề cương

Xác suất chuyển tiếp \mat{$\transition{\x}{\x'}$}

Xác suất chiếm dụng \mat{$\pi_t(\x)$} tại thời điểm \mat{$t$}

Điều kiện cân bằng trên \mat{$\pi_t$} xác định phân bố cố định \mat{$\pi(\x)$}
    
Lưu ý: phân phối cố định phụ thuộc vào sự lựa chọn \mat{$\transition{\x}{\x'}$}

Theo cặp \defn{cân bằng chi tiết} ở các trạng thái đảm bảo trạng thái cân bằng

\defn{Xác suất chuyển tiếp lấy mẫu Gibbs}:
    
    lấy mẫu từng biến cho các giá trị hiện tại của tất cả các biến khác

\mat{$\implies$} cân bằng chi tiết với mặt sau thật

Đối với mạng Bayesian, việc lấy mẫu Gibbs giảm xuống còn 

lấy mẫu có điều kiện trên chăn Markov của mỗi biến

---
## Phân phối cố định

\mat{$\pi_t(\x)$} = xác suất ở trạng thái \mat{$\x$} tại thời điểm \mat{$t$}

\mat{$\pi_{t+1}(\x')$} = xác suất ở trạng thái \mat{$\x'$} tại thời điểm \mat{$t+1$}

\mat{$\pi_{t+1}$} xét về \mat{$\pi_t$} và \mat{$\transition{\x}{\x'}$}
\mat{\[
  \pi_{t+1}(\x') = \mysum_{\smbf{x}} \pi_t(\x) \transition{\x}{\x'}
\]}
Phân bố cố định: \mat{$\pi_t = \pi_{t+1} = \pi$}
\mat{\[
  \pi(\x') = \mysum_{\smbf{x}} \pi(\x) \transition{\x}{\x'}
       &nbsp;&nbsp;&nbsp;&nbsp; \mbox{for all }\x'
\]}
Nếu \mat{$\pi$} tồn tại thì nó là duy nhất (cụ thể cho \mat{$\transition{\x}{\x'}$})

Ở trạng thái cân bằng, "dòng ra" dự kiến = "dòng vào" dự kiến
  

---
## Số dư chi tiết

"Outflow" = "inflow" cho mỗi cặp trạng thái:
\mat{\[
  \pi(\x) \transition{\x}{\x'} 
   = \pi(\x') \transition{\x'}{\x}
       &nbsp;&nbsp;&nbsp;&nbsp; \mbox{for all }\x,\ \x'
\]}
Cân bằng chi tiết \mat{$\implies$} tính ổn định:
\mat{\begin{eqnarray*}
\mysum_{\smbf{x}} \pi(\x) \transition{\x}{\x'} 
   & = & \mysum_{\smbf{x}} \pi(\x') \transition{\x'}{\x} 

   & = & \pi(\x') \mysum_{\smbf{x}} \transition{\x'}{\x} 

   & = & \pi(\x')
\end{eqnarray*}}

Các thuật toán MCMC thường được xây dựng bằng cách thiết kế một quá trình chuyển đổi

xác suất \mat{$q$} cân bằng chi tiết với \mat{$\pi$} mong muốn

---
##  Lấy mẫu Gibbs 

Lấy mẫu lần lượt từng biến, cho trước *tất cả các biến khác*

Lấy mẫu \mat{$X_i$}, đặt \mat{$\bar{\X_i}$} là tất cả các biến không có bằng chứng khác

Giá trị hiện tại là \mat{$x_i$} và \mat{$\bar{\x_i}$}; \mat{$\e$} đã được sửa 

Xác suất chuyển tiếp được đưa ra bởi
\mat{\[
\transition{\x}{\x'} =
  \transition{x_i,\bar{\x_i}}{x_i',\bar{\x_i}} =
    P(x_i'|\bar{\x_i},\e)
\]}
Điều này mang lại sự cân bằng chi tiết với phần sau thực sự \mat{$P(\x|\e)$}:
\mat{\begin{eqnarray*}
\pi(\x) \transition{\x}{\x'} 
   &=& P(\x|\e) P(x_i'|\bar{\x_i},\e) 
     =  P(x_i,\bar{\x_i}|\e)P(x_i'|\bar{\x_i},\e)  

   &=& P(x_i|\bar{\x_i},\e)P(\bar{\x_i}|\e)
       P(x_i'|\bar{\x_i},\e)  &nbsp;&nbsp; \mbox{(chain rule)} 

   &=& P(x_i|\bar{\x_i},\e)P(x_i',\bar{\x_i}|\e)
       &nbsp;&nbsp;&nbsp;&nbsp; \mbox{(chain rule backwards)} 

   &=& \transition{\x'}{\x} \pi(\x') 
       = \pi(\x') \transition{\x'}{\x} 
\end{eqnarray*}}

---
## Hiệu suất của thuật toán xấp xỉ

\defn{Xấp xỉ tuyệt đối}: 
  \mat{$|P(X|\e) - \hat P(X|\e)| \leq \epsilon$}

\defn{Xấp xỉ tương đối}: 
  \mat{$\frac{|P(X|\smbf{e}) - \hat P(X|\smbf{e})|}{P(X|\smbf{e})} \leq \epsilon$}

Tương đối \mat{$\implies$} tuyệt đối kể từ \mat{$0\leq P \leq 1$} (có thể là \mat{$O(2^{-n})$})

Các thuật toán ngẫu nhiên có thể thất bại với xác suất tối đa \mat{$\delta$}

Xấp xỉ đa thời gian: \mat{$\mbox{poly}(n,\epsilon^{-1},\log \delta^{-1})$}

Định lý (Dagum và Luby, 1993): cả tuyệt đối và tương đối

xấp xỉ cho các thuật toán xác định hoặc ngẫu nhiên

là NP-hard cho mọi \mat{$\epsilon,\delta<0.5$}

(Polytime gần đúng tuyệt đối không có bằng chứng---giới hạn Chernoff)