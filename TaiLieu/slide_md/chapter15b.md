\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Suy diễn trong mạng niềm tin

## Chương 15.3--4 + bổ sung

---
## Nội dung

- Suy diễn chính xác bằng phép liệt kê (enumeration)

- Suy diễn chính xác bằng cách loại bỏ biến (variable elimination)

- Suy diễn xấp xỉ bằng mô phỏng ngẫu nhiên (stochastic simulation)

- Suy diễn xấp xỉ bằng chuỗi Markov Monte Carlo

---
## Các tác vụ suy diễn (Inference tasks)

<u>Truy vấn đơn giản (Simple queries)</u>: tính biên hậu nghiệm $P(X_i|\mbf{E}\eq \mbf{e})$
  
  ví dụ: $P(NoGas|Gauge\eq empty,Lights\eq on,Starts\eq false)$

<u>Truy vấn hội (Conjunctive queries)</u>: $P(X_i,X_j|\mbf{E}\eq \mbf{e}) = 
    P(X_i|\mbf{E}\eq \mbf{e})  P(X_j|X_i,\mbf{E}\eq \mbf{e}) $

<u>Quyết định tối ưu (Optimal decisions)</u>: mạng quyết định bao gồm thông tin về độ hữu ích;
    
    cần suy diễn xác suất cho $P(K\hat{e}t\ qu\mbox{\`{a}}|h\mbox{\`{a}}nh\ \mbox{\dj}\hat{o}ng,b\mbox{\`{a}}ng\ ch\acute{u}ng)$

<u>Giá trị của thông tin (Value of information)</u>: nên tìm kiếm bằng chứng nào tiếp theo?

<u>Phân tích độ nhạy (Sensitivity analysis)</u>: các giá trị xác suất nào là quan trọng nhất?

<u>Giải thích (Explanation)</u>: tại sao tôi cần một bộ khởi động mới?

---
## Suy diễn bằng cách liệt kê

Một cách thông minh hơn một chút để tính tổng các biến từ phân phối đồng thời
mà không thực sự xây dựng biểu diễn rõ ràng của nó

Truy vấn đơn giản trên mạng trộm (burglary network):

$P(B|J\eq true,M\eq true)$

$= P(B,J\eq true,M\eq true)/P(J\eq true,M\eq true)$

$= 
  pha P(B,J\eq true,M\eq true)$

$= 
  pha \mysum_e \mysum_a P(B,e,a,J\eq true,M\eq true)$

Viết lại các mục nhập đồng thời đầy đủ bằng cách sử dụng tích của các mục nhập CPT:

$P(B\eq true|J\eq true,M\eq true)$

$= 
  pha \mysum_e \mysum_a P(B\eq true)P(e)P(a|B\eq true,e)P(J\eq true|a)P(M\eq true|a) $

$= 
  pha P(B\eq true)\mysum_e P(e)\mysum_a P(a|B\eq true,e)P(J\eq true|a)P(M\eq true|a)$
       

---
## Thuật toán liệt kê

Liệt kê ưu tiên chiều sâu cạn kiệt (Exhaustive depth-first enumeration): độ phức tạp không gian $O(n)$, thời gian $O(d^n)$

```text
EnumerationAsk(\v{X},\mbf{e},\v{bn}) \k{returns} a distribution over \v{X} 
\k{inputs}: \v{X}, {the query variable}
            {\mbf{e}}, {evidence specified as an event}
            \v{bn}, {a belief network specifying joint distribution $P(X_1,\ldots,X_n)$}

    $Q(\v{X)$}{a distribution over \v{X}}
    \k{for each} value $x_i$ of \v{X} \k{do}
          extend \mbf{e} with value $x_i$ for \v{X}
          $Q(x_i)$ <- EnumerateAll(Vars[\v{bn],\mbf{e})}
    \k{return} Normalize($Q(X)$)
\fnsep
EnumerateAll(\v{vars},\mbf{e}) \k{returns} a real number
    \k{if} Empty?(\v{vars}) \k{then return} 1.0
    \k{else do}
          \v{Y}{First(\v{vars})}
          \k{if} \v{Y} has value \v{y} in \mbf{e}
                \k{then return} $P(y | Pa(Y)) \times {}$EnumerateAll(Rest(\v{vars}),\mbf{e})
                \k{else return} $\sum_{y} P(y | Pa(Y)) \times {}$EnumerateAll(Rest(\v{vars}),$\mbf{e}_y$)
                      where $\mbf{e}_y$ is \mbf{e} extended with $Y\eq y$
```

---
## Suy diễn bằng cách loại bỏ biến

Liệt kê không hiệu quả: tính toán lặp lại
  
  ví dụ: tính $P(J\eq true|a)P(M\eq true|a)$ cho mỗi giá trị của $e$

Loại bỏ biến (Variable elimination): thực hiện tính tổng từ phải sang trái,

lưu trữ các kết quả trung gian (<u>các hệ số (factors)</u>) để tránh tính toán lại

$P(B|J\eq true,M\eq true)$
    
    $= 
  pha \underbrace{P(B)}_B 
             \mysum_e \underbrace{P(e)}_E
             \mysum_a \underbrace{P(a|B,e)}_A
             \underbrace{P(J\eq true|a)}_J
             \underbrace{P(M\eq true|a)}_M$
    
    $= 
  pha P(B)\mysum_e P(e)\mysum_a P(a|B,e) P(J\eq true|a) f_M(a)$
    
    $= 
  pha P(B)\mysum_e P(e)\mysum_a P(a|B,e) f_J(a) f_M(a)$
    
    $= 
  pha P(B)\mysum_e P(e)\mysum_a f_A(a,b,e) f_J(a) f_M(a)$
    
    $= 
  pha P(B)\mysum_e P(e)f_{\bar{A}JM}(b,e) $ (tính tổng $A$)
    
    $= 
  pha P(B)f_{\bar{E}\bar{A}JM}(b)$ (tính tổng $E$)
    
    $= 
  pha f_B(b)\stimes f_{\bar{E}\bar{A}JM}(b)$ 

---
## Loại bỏ biến: Các phép toán cơ bản

<u>Tích từng điểm (Pointwise product)</u> của các hệ số $f_1$ và $f_2$:
  
  $f_1(x_1,\ldots,x_j,y_1,\ldots,y_k) \stimes
     f_2(y_1,\ldots,y_k,z_1,\ldots,z_l)$
    
  = $f(x_1,\ldots,x_j,y_1,\ldots,y_k,z_1,\ldots,z_l)$

Ví dụ: $f_1(a,b) \stimes f_2(b,c) = f(a,b,c)$

Lấy tổng một biến ra khỏi tích các hệ số: di chuyển bất kỳ hệ số hằng số nào
ra ngoài phép tổng:

$\mysum_x f_1 \stimes \cdots \stimes f_k =
f_1 \stimes \cdots \stimes f_i\  \mysum_x\; f_{i+1} \stimes \cdots \stimes
f_k = f_1 \stimes \cdots \stimes f_i \stimes f_{\bar{X}}$

giả sử $f_1,\ldots,f_i$ không phụ thuộc vào $X$

---
## Thuật toán loại bỏ biến

```text
function EliminationAsk(\v{X),\mbf{e},\v{bn}}{a distribution over \v{X}}
      inputs: X, the query variable
    \inputs{\mbf{e}}{evidence specified as an event}
      inputs: bn, a belief network specifying joint distribution $P(X_1,\ldots,X_n)$

    if $\v{X}\elt\mbf{e}$ then return observed point distribution for \v{X}
    \v{factors}{$[, ]$}; \v{vars}{Reverse(Vars[\v{bn}])}
    \k{for each} \v{var} \k{in} \v{vars} \k{do}
          \v{factors}{$[MakeFactor(\v{var},\mbf{e})|\v{factors}]$}
          \k{if} \v{var} is a hidden variable \k{then} \v{factors}{SumOut(\v{var},\v{factors})}
    \k{return} Normalize(PointwiseProduct(\v{factors}))
```

---
## Độ phức tạp của suy diễn chính xác

Mạng <u>kết nối đơn (Singly connected)</u> (hoặc <u>đa cây (polytrees)</u>):
  
  -- bất kỳ hai nút nào cũng được kết nối với nhau bởi tối đa một đường dẫn (không có hướng)
  
  -- chi phí thời gian và không gian của việc loại bỏ biến là $O(d^k n)$

Mạng <u>kết nối đa (Multiply connected)</u>:
  
  -- có thể quy giản 3SAT thành suy diễn chính xác $\implies$ NP-khó (NP-hard)
  
  -- tương đương với việc *đếm* các mô hình 3SAT $\implies$ \#P-đầy đủ (\#P-complete)

![Hình ảnh](../TaiLieu/slide_md/figures/bn-3sat.png)

---
## Suy diễn bằng mô phỏng ngẫu nhiên

Ý tưởng cơ bản:
  
  1) Rút ra $N$ mẫu từ một phân phối lấy mẫu $S$
  
  2) Tính xác suất hậu nghiệm xấp xỉ $\hat P$
  
  3) Chỉ ra rằng xác suất này hội tụ về xác suất thực $P$

Phác thảo:
  
  -- Lấy mẫu từ một mạng rỗng (Sampling from an empty network)
  
  -- Lấy mẫu loại bỏ (Rejection sampling): từ chối các mẫu không khớp với bằng chứng
  
  -- Trọng số hợp lý (Likelihood weighting): sử dụng bằng chứng để tính trọng số cho các mẫu
  
  -- MCMC: lấy mẫu từ một quá trình ngẫu nhiên mà phân phối
    
       dừng của nó là phân phối hậu nghiệm thực

---
## Lấy mẫu từ một mạng rỗng

```text
function PriorSample(\v{bn)}{an event sampled from $P(X_1,\ldots,X_n)$ specified by \v{bn}}
    \mbf{x}{an event with $n$ elements}
    \k{for} $i = 1$ \k{to} $n$ \k{do}
          $x_i$ <- a random sample from $P(X_i | Parents(X_i))$
    \k{return} \mbf{x}
```

$P(Cloudy) = \<0.5,0.5\>$
    
    mẫu $\rightarrow$ $true$

$P(Sprinkler|Cloudy) = \<0.1,0.9\>$
    
    mẫu $\rightarrow$ $false$

$P(Rain|Cloudy) = \<0.8,0.2\>$
    
    mẫu $\rightarrow$ $true$

\hbox{$P(WetGrass|\lnot Sprinkler,Rain) = \<0.9,0.1\>$}
    
    mẫu $\rightarrow$ $true$

 

![Hình ảnh](../TaiLieu/slide_md/figures/rain-clustering1.png)

---
## Lấy mẫu từ một mạng rỗng (tiếp)

Xác suất để thuật toán \prog{PriorSample} sinh ra một sự kiện cụ thể
  
  $S_{PS}(x_1\ldots x_n) = \myprod_{i\eq 1}^n P(x_i | Parents(X_i))
    = P(x_1\ldots x_n)$

nghĩa là, xác suất tiên nghiệm thực

Gọi $N_{PS}(\mbf{Y}\eq \mbf{y})$ là số mẫu được tạo ra
trong đó $\mbf{Y}\eq \mbf{y}$, đối với bất kỳ tập biến $\mbf{Y}$ nào.

Khi đó $\hat P(\mbf{Y}\eq \mbf{y}) = N_{PS}(\mbf{Y}\eq \mbf{y})/N$ và
\begin{eqnarray*}
  \lim_{N\to\infty} \hat P(\mbf{Y}\eq \mbf{y}) 
      & = & \mysum_{\smbf{h}} S_{PS}(\mbf{Y}\eq \mbf{y},\mbf{H}\eq \mbf{h})

      & = &  \mysum_{\smbf{h}} P(\mbf{Y}\eq \mbf{y},\mbf{H}\eq \mbf{h})

      & = & P(\mbf{Y}\eq \mbf{y})
\end{eqnarray*}
Nghĩa là, các ước tính thu được từ \prog{PriorSample} là <u>nhất quán (consistent)</u>

---
## Lấy mẫu loại bỏ

$\hat{P}(X|\mbf{e})$ được ước tính từ các mẫu đồng ý với $\mbf{e}$

```text
function RejectionSampling(\v{X),\mbf{e},\v{bn},\v{N}}{an approximation to $P(X|\mbf{e})$}
    \mbf{N[\v{X}]}{a vector of counts over \v{X}, initially zero}
    \k{for} \v{j} = 1 to $N$ \k{do}
          \mbf{x}{PriorSample(\v{bn})}
          \k{if} \mbf{x} is consistent with \mbf{e} \k{then}
              \mbf{N[\v{x}]}{\mbf{N}[\v{x}]+1} where \v{x} is the value of \v{X} in \mbf{x}
    \k{return} Normalize(\mbf{N}[\v{X}])
```

Ví dụ: ước lượng $P(Rain|Sprinkler\eq true)$ bằng cách sử dụng 100 mẫu
  
  27 mẫu có $Sprinkler\eq true$
    
    Trong số này, 8 mẫu có $Rain\eq true$ và 19 mẫu có $Rain\eq false$.
[0.2in]
$\hat{P}(Rain|Sprinkler\eq true) = \noprog{Normalize}(\<8,19\>) =
\<0.296,0.704\>$

Tương tự như một quy trình ước lượng thực nghiệm cơ bản trong thế giới thực

---
## Phân tích lấy mẫu loại bỏ

$\hat{P}(X|\mbf{e}) = 
  pha \mbf{N}_{PS}(X,\mbf{e}) $ 
    &nbsp;&nbsp;&nbsp;&nbsp;  (định nghĩa thuật toán)
  
$= \mbf{N}_{PS}(X,\mbf{e})/N_{PS}(\mbf{e})$ 
    &nbsp;&nbsp;&nbsp;&nbsp;  (được chuẩn hóa bằng $N_{PS}(\mbf{e})$)
  
$\approx P(X,\mbf{e})/P(\mbf{e})$ 
    &nbsp;&nbsp;&nbsp;&nbsp;  (đặc tính của \prog{PriorSample})
  
$= P(X|\mbf{e})$ 
    &nbsp;&nbsp;&nbsp;&nbsp;  (định nghĩa xác suất có điều kiện)

Do đó việc lấy mẫu loại bỏ trả về các ước tính hậu nghiệm nhất quán

Vấn đề: chi phí cực kỳ lớn nếu $P(\mbf{e})$ nhỏ

---
## Trọng số hợp lý (Likelihood weighting)

Ý tưởng: cố định các biến bằng chứng, chỉ lấy mẫu các biến không phải bằng chứng,

và đánh trọng số từng mẫu theo khả năng nó phù hợp với bằng chứng

```text
function WeightedSample(\v{bn),\mbf{e}}{an event and a weight}
    \mbf{x}{an event with $n$ elements}; \v{w}{1}
    \k{for} \v{i} = 1 \k{to} $n$ \k{do}
          \k{if} $X_i$ has a value $x_i$ in \mbf{e}
                \k{then} \v{w}{$\v{w}\times P(X_i\eq x_i | Parents(X_i))$}
                \k{else} $x_i$ <- a random sample from $P(X_i | Parents(X_i))$
    \k{return} \mbf{x}, \v{w}

function LikelihoodWeighting(\v{X),\mbf{e},\v{bn},\v{N}}{an approximation to $P(X|\mbf{e})$}
    $\mbf{W[\v{X}]$}{a vector of weighted counts over \v{X}, initially zero}
    \k{for} \v{j} = 1 to $N$ \k{do}
          \mbf{x,\v{w}}{WeightedSample(\v{bn})}
          $\mbf{W[\v{x}]$}{$\mbf{W}[\v{x}]+\v{w}$} where \v{x} is the value of \v{X} in \mbf{x}
    \k{return} Normalize($\mbf{W}[\v{X}]$)
```

---
## Ví dụ về trọng số hợp lý

Ước lượng $P(Rain|Sprinkler\eq true,WetGrass\eq true)$

![Hình ảnh](../TaiLieu/slide_md/figures/rain-clustering-mcmc.png)

---
## LW example contd.

Sample generation process:

1. $w \leftarrow 1.0$

2. Sample $P(Cloudy) = \<0.5,0.5\>$; say $true$

3. $Sprinkler$ has value $true$, so
  
  $w \leftarrow w \times P(Sprinkler\eq true|Cloudy\eq true) = 0.1$

4. Sample $P(Rain|Cloudy\eq true) = \<0.8,0.2\>$; say $true$ 

5. $WetGrass$ has value $true$, so
  
  $w \leftarrow w \times P(WetGrass\eq true|Sprinkler\eq true,Rain\eq true) = 0.099$

---
## Likelihood weighting analysis

Sampling probability for \prog{WeightedSample} is
  
  $S_{WS}(\mbf{y},\mbf{e}) = \myprod_{i\eq 1}^l P(y_i|Parents(Y_i))$

Note: pays attention to evidence in *ancestors* only
    
    $\implies$ somewhere "in between" prior and posterior distribution

Weight for a given sample $\mbf{y},\mbf{e}$ is
  
  $w(\mbf{y},\mbf{e}) = \myprod_{i\eq 1}^m P(e_i | Parents(E_i))$

Weighted sampling probability is
  
  $S_{WS}(\mbf{y},\mbf{e}) w(\mbf{y},\mbf{e})$
    
    $= \myprod_{i\eq 1}^l P(y_i|Parents(Y_i))\ \ 
       \myprod_{i\eq 1}^m P(e_i|Parents(E_i))$
    
    $= P(\mbf{y},\mbf{e})$ (by standard global semantics of network)

Hence likelihood weighting returns consistent estimates

but performance still degrades with many evidence variables

---
## Approximate inference using MCMC

"State" of network = current assignment to all variables

Generate next state by sampling one variable given Markov blanket

Sample each variable in turn, keeping evidence fixed

```text
function MCMC-Ask(\v{X),\mbf{e},\v{bn},\v{N}}{an approximation to $P(X|\mbf{e})$}
    \firstlocal{$\mbf{N}[\v{X}]$}{a vector of counts over \v{X}, initially zero}
    \local{\mbf{Y}}{the nonevidence variables in \v{bn}}
    \local{\mbf{x}}{the current state of the network, initially copied from \mbf{e}}

    initialize \v{\mbf{x}} with random values for the variables in \v{\mbf{Y}}
    \k{for} \v{j} = 1 to $N$ \k{do}
          $\mbf{N[\v{x}]$}{$\mbf{N}[\v{x}]+1$} where \v{x} is the value of \v{X} in \mbf{x}
          \k{for each} $Y_i$ in \v{\mbf{Y}} \k{do}
                sample the value of $Y_i$ in \mbf{x} from $P(Y_i|MB(Y_i))$ given the values of $MB(Y_i)$ in \mbf{x}
    \k{return} Normalize($\mbf{N}[\v{X}]$)
```

Approaches <u>stationary distribution</u>: long-run fraction of time
spent in each state is exactly proportional to its posterior
probability

---
## MCMC Example

Estimate $P(Rain|Sprinkler\eq true,WetGrass\eq true)$

Sample $Cloudy$ then $Rain$, repeat.

Count number of times $Rain$ is true and false in the samples.

Markov blanket of $Cloudy$ is $Sprinkler$ and $Rain$

Markov blanket of $Rain$ is $Cloudy$, $Sprinkler$, and $WetGrass$

![Hình ảnh](../TaiLieu/slide_md/figures/rain-clustering-mcmc.png)

---
## MCMC example contd.

Random initial state: $Cloudy\eq true$ and $Rain\eq false$

1. $P(Cloudy|MB(Cloudy)) = P(Cloudy|Sprinkler,\lnot Rain)$
    
    sample $\rightarrow$ $false$

2. $P(Rain|MB(Rain)) = P(Rain|\lnot Cloudy,Sprinkler,WetGrass)$
    
    sample $\rightarrow$ $true$

Visit 100 states
  
  31 have $Rain\eq true$, 69 have $Rain\eq false$

$\hat{P}(Rain|Sprinkler\eq true,WetGrass\eq true)$
  
      $= \noprog{Normalize}(\<31,69\>) = \<0.31,0.69\>$

---
## MCMC analysis: Outline

Transition probability $\transition{\mbf{y}}{\mbf{y}'}$

Occupancy probability $\pi_t(\mbf{y})$ at time $t$

Equilibrium condition on $\pi_t$ defines stationary distribution $\pi(\mbf{y})$
    
Note: stationary distribution depends on choice of $\transition{\mbf{y}}{\mbf{y}'}$

Pairwise <u>detailed balance</u> on states guarantees equilibrium

<u>Gibbs sampling</u> transition probability:
    
    sample each variable given current values of all others

$\implies$ detailed balance with the true posterior

For Bayesian networks, Gibbs sampling reduces to

sampling conditioned on each variable's Markov blanket

---
## Stationary distribution

$\pi_t(\mbf{y})$ = probability in state $\mbf{y}$ at time $t$

$\pi_{t+1}(\mbf{y}')$ = probability in state $\mbf{y}'$ at time $t+1$

$\pi_{t+1}$ in terms of $\pi_t$ and $\transition{\mbf{y}}{\mbf{y}'}$
\[
  \pi_{t+1}(\mbf{y}') = \mysum_{\smbf{y}} \pi_t(\mbf{y}) \transition{\mbf{y}}{\mbf{y}'}
\]
Stationary distribution: $\pi_t = \pi_{t+1} = \pi$
\[
  \pi(\mbf{y}') = \mysum_{\smbf{y}} \pi(\mbf{y}) \transition{\mbf{y}}{\mbf{y}'}
       &nbsp;&nbsp;&nbsp;&nbsp; \mbox{for all }\mbf{y}'
\]
If $\pi$ exists, it is unique (specific to $\transition{\mbf{y}}{\mbf{y}'}$)

In equilibrium, expected "outflow" = expected "inflow"
  

---
## Detailed balance

"Outflow" = "inflow" for each pair of states:
\[
  \pi(\mbf{y}) \transition{\mbf{y}}{\mbf{y}'} 
   = \pi(\mbf{y}') \transition{\mbf{y}'}{\mbf{y}}
       &nbsp;&nbsp;&nbsp;&nbsp; \mbox{for all }\mbf{y},\ \mbf{y}'
\]
Detailed balance $\implies$ stationarity:
\begin{eqnarray*}
\mysum_{\smbf{y}} \pi(\mbf{y}) \transition{\mbf{y}}{\mbf{y}'} 
   & = & \mysum_{\smbf{y}} \pi(\mbf{y}') \transition{\mbf{y}'}{\mbf{y}} 

   & = & \pi(\mbf{y}') \mysum_{\smbf{y}} \transition{\mbf{y}'}{\mbf{y}} 

   & = & \pi(\mbf{y}')
\end{eqnarray*}

MCMC algorithms typically constructed by designing a transition

probability $q$ that is in detailed balance with desired $\pi$

---
## Gibbs sampling

Sample each variable in turn, given *all other variables*

Sampling $Y_i$, let $\bar{\mbf{Y}_i}$ be all other nonevidence variables

Current values are $y_i$ and $\bar{\mbf{y}_i}$; $\mbf{e}$ is fixed

Transition probability is given by
\[
\transition{\mbf{y}}{\mbf{y}'} =
  \transition{y_i,\bar{\mbf{y}_i}}{y_i',\bar{\mbf{y}_i}} =
    P(y_i'|\bar{\mbf{y}_i},\mbf{e})
\]
This gives detailed balance with true posterior $P(\mbf{y}|\mbf{e})$:
\begin{eqnarray*}
\pi(\mbf{y}) \transition{\mbf{y}}{\mbf{y}'} 
   &=& P(\mbf{y}|\mbf{e}) P(y_i'|\bar{\mbf{y}_i},\mbf{e}) 
     =  P(y_i,\bar{\mbf{y}_i}|\mbf{e})P(y_i'|\bar{\mbf{y}_i},\mbf{e})  

   &=& P(y_i|\bar{\mbf{y}_i},\mbf{e})P(\bar{\mbf{y}_i}|\mbf{e})
       P(y_i'|\bar{\mbf{y}_i},\mbf{e})  &nbsp;&nbsp; \mbox{(chain rule)} 

   &=& P(y_i|\bar{\mbf{y}_i},\mbf{e})P(y_i',\bar{\mbf{y}_i}|\mbf{e})
       &nbsp;&nbsp;&nbsp;&nbsp; \mbox{(chain rule backwards)} 

   &=& \transition{\mbf{y}'}{\mbf{y}} \pi(\mbf{y}') 
       = \pi(\mbf{y}') \transition{\mbf{y}'}{\mbf{y}} 
\end{eqnarray*}

---
## Markov blanket sampling

A variable is independent of all others given its Markov blanket:
  
  $P(y_i'|\bar{\mbf{y}_i},\mbf{e}) = P(y_i'|MB(Y_i))$

Probability given the Markov blanket is calculated as follows:
  
  $P(y_i'|MB(Y_i)) = P(y_i'|Parents(Y_i)) 
           \myprod_{Z_j\in Children(Y_i)} P(z_j|Parents(Z_j))$

Hence computing the sampling distribution over $Y_i$ for each
flip requires just $cd$ multiplications if $Y_i$ has $c$ children
and $d$ values; can cache it if $c$ not too large.

Main computational problems:
  
  1) Difficult to tell if convergence has been achieved
  
  2) Can be wasteful if Markov blanket is large:
    
    $P(Y_i|MB(Y_i))$ won't change much (law of large numbers)

---
## Performance of approximation algorithms

<u>Absolute approximation</u>: 
  $|P(X|\mbf{e}) - \hat P(X|\mbf{e})| \leq \epsilon$

<u>Relative approximation</u>: 
  $\frac{|P(X|\smbf{e}) - \hat P(X|\smbf{e})|}{P(X|\smbf{e})} \leq \epsilon$

Relative $\implies$ absolute since $0\leq P \leq 1$ (may be $O(2^{-n})$)

Randomized algorithms may fail with probability at most $\delta$

Polytime approximation: $\mbox{poly}(n,\epsilon^{-1},\log \delta^{-1})$

Theorem (Dagum and Luby, 1993): both absolute and relative

approximation for either deterministic or randomized algorithms

are NP-hard for any $\epsilon,\delta<0.5$

(Absolute approximation polytime with no evidence---Chernoff bounds)