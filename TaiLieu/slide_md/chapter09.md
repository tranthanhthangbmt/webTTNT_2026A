\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Suy diễn trong logic bậc một (Inference in first-order logic)

## Chương 9

---
## Phác thảo

- Rút gọn suy luận bậc nhất thành suy luận mệnh đề

- Thống nhất

- Các mô thức tổng quát

- Chuỗi tiến và lùi

- Lập trình logic

- Độ phân giải

---
## Lược sử lý luận

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| \note{450**b.c.** | \txr{ Stoics } | logic mệnh đề, suy luận (có thể) |
| \note{322**b.c.** } | \txr{ Aristotle } | "syllogisms" (quy tắc suy luận), định lượng |
| \note{1565 } | \txr{ Cardano } | lý thuyết xác suất (logic mệnh đề + độ không chắc chắn) |
| \note{1847 } | \txr{ Boole } | logic mệnh đề (lại) |
| \note{1879 } | \txr{ Frege } | logic bậc nhất |
| \note{1922 } | \txr{ Wittgenstein} | bằng chứng bằng bảng chân lý |
| \note{1930 } | \txr{ G\"odel } | $\exists$ thuật toán hoàn chỉnh cho FOL |
| \note{1930 } | \txr{ Herbrand } | thuật toán hoàn chỉnh cho FOL (rút gọn về mệnh đề) |
| \note{1931 } | \txr{ G\"odel } | $\lnot\exists$ thuật toán hoàn chỉnh cho số học |
| \note{1960 } | \txr{ Davis/Putnam} | thuật toán "thực tế" cho logic mệnh đề |
| \note{1965 } | \txr{ Robinson } | thuật toán "thực tế" cho FOL---độ phân giải |

---
##  Khởi tạo phổ quát (UI) 

Mọi sự thể hiện của một câu được định lượng phổ quát đều được nó kéo theo:
\mat{\[\frac{\All{v} 
  pha}{\noprog{Subst}(\{v/g\},
  pha)}\]}
cho bất kỳ biến nào \mat{$v$} và thuật ngữ cơ bản \mat{$g$}

Ví dụ: \mat{$\All{x} King(x) \land Greedy(x) \implies Evil(x)$} mang lại
\mat{\begin{formula}
   King(John) \land Greedy(John)  \implies Evil(John)

   King(Richard) \land Greedy(Richard)  \implies Evil(Richard)

   King(Father(John)) \land Greedy(Father(John))  \implies Evil(Father(John))

    &nbsp;&nbsp; \vdots
\end{formula}}

---
##  Khởi tạo hiện sinh (EI)

Đối với bất kỳ câu \mat{$
  pha$}, biến \mat{$v$} và ký hiệu hằng \mat{$k$} 

*không xuất hiện ở nơi khác trong cơ sở kiến thức*:
\mat{\[\frac{\Exi{v} 
  pha}{\noprog{Subst}(\{v/k\},
  pha)}\]}

Ví dụ: \mat{$\Exi{x} Crown(x) \land OnHead(x,John)$} mang lại
\mat{\[
Crown(C_1) \land OnHead(C_1,John)
\]}
với điều kiện \mat{$C_1$} là ký hiệu hằng số mới, được gọi là \defn{Hằng số Skolem}

Một ví dụ khác: từ \mat{$\Exi{x} {{d(x^y)}/{dy}} \eq  x^y$} chúng ta có được
\mat{\[
{{d(e^y)}/{dy}} \eq  e^y
\]}
với điều kiện \mat{$e$} là ký hiệu hằng số mới

---
##  Tiếp tục khởi tạo hiện sinh.

Giao diện người dùng có thể được áp dụng nhiều lần để *thêm* câu mới;

KB mới về mặt logic tương đương với KB cũ

EI có thể được áp dụng một lần để *thay thế* câu hiện sinh;

KB mới là *không * tương đương với cái cũ,

nhưng có thể đáp ứng được nếu KB cũ có thể đáp ứng được

---
## Giảm suy luận mệnh đề

Giả sử KB chỉ chứa những thứ sau:
\mat{\begin{formula}
   \All{x} King(x) \land Greedy(x) \implies Evil(x)

   King(John)

   Greedy(John)

   Brother(Richard,John)
\end{formula}}
Khởi tạo câu phổ quát theo *tất cả các cách có thể*, chúng ta có
\mat{\begin{formula}
   King(John) \land Greedy(John) \implies Evil(John)

   King(Richard) \land Greedy(Richard) \implies Evil(Richard)

   King(John)

   Greedy(John)

   Brother(Richard,John)
\end{formula}}
KB mới được \defn{được đề xuất}: các ký hiệu mệnh đề là
\mat{\[
  King(John),\ Greedy(John),\ Evil(John), King(Richard)\, \bbox{etc.}
\]}

---
## Tiếp theo mức giảm 

Khiếu nại: một câu cơ bản\mat{$^*$} được đưa ra bởi KB mới nếu được KB ban đầu kéo theo

Yêu cầu: mọi KB FOL đều có thể được đề xuất hóa để duy trì quyền thừa kế

Ý tưởng: đề xuất KB và truy vấn, áp dụng độ phân giải, trả về kết quả

Vấn đề: với các ký hiệu hàm số, có vô số thuật ngữ cơ bản,
  
  ví dụ: \mat{$Father(Father(Father(John)))$}

Định lý: Herbrand (1930). Nếu một câu \mat{$
  pha$} được bao gồm bởi FOL KB,
    
  nó được kéo theo một tập con *hữu hạn* của mệnh đề KB

Ý tưởng: Với \mat{$n$} = \mat{$0$} đến \mat{$\infty$} do
    
    tạo một KB mệnh đề bằng cách khởi tạo với các thuật ngữ độ sâu-\mat{$n$}
    
    xem liệu \mat{$
  pha$} có được KB này yêu cầu không

Sự cố: hoạt động nếu \mat{$
  pha$} được yêu cầu, lặp lại nếu \mat{$
  pha$} không được yêu cầu

Định lý: Turing (1936), Church (1936), sự kéo theo trong FOL là \defn{semicidable}

---
## Các vấn đề về mệnh đề hóa

Sự đề xuất dường như tạo ra rất nhiều câu không liên quan.

Ví dụ: từ 
\mat{\begin{formula}
   \All{x} King(x) \land Greedy(x) \implies Evil(x)

   King(John)

   \All{y} Greedy(y)

   Brother(Richard,John)
\end{formula}}
điều đó có vẻ hiển nhiên \mat{$Evil(John)$}, nhưng việc mệnh đề hóa tạo ra
rất nhiều sự thật như \mat{$Greedy(Richard)$} không liên quan

Với các biến vị ngữ \mat{$p$} \mat{$k$} và hằng số \mat{$n$}, có các phiên bản \mat{$p\cdot n^k$}

Với các ký hiệu chức năng, mọi chuyện còn tệ hơn nhiều!

---
## Hợp nhất

Chúng ta có thể suy luận ngay lập tức nếu tìm được sự thay thế \mat{$\theta$}

sao cho \mat{$King(x)$} và \mat{$Greedy(x)$} khớp với \mat{$King(John)$} và \mat{$Greedy(y)$}

\mat{$\theta = \{x/John,y/John\}$} hoạt động

\mat{\noprog{Unify}}\mat{$(
  pha,\beta) = \theta$} nếu \mat{$
  pha\theta\eq \beta\theta$}

\mat{\[\begin{array}{l|l|l}
p & q & \theta 

\hline
Knows(John,x) & Knows(John,Jane) & 

Knows(John,x) & Knows(y,OJ)      & 

Knows(John,x) & Knows(y,Mother(y))& \phantom{\{y/John,x/Mother(John)\}}

Knows(John,x) & Knows(x,OJ)
\end{array}\]}

---
## Hợp nhất

Chúng ta có thể suy luận ngay lập tức nếu tìm được sự thay thế \mat{$\theta$}

sao cho \mat{$King(x)$} và \mat{$Greedy(x)$} khớp với \mat{$King(John)$} và \mat{$Greedy(y)$}

\mat{$\theta = \{x/John,y/John\}$} hoạt động

\mat{\noprog{Unify}}\mat{$(
  pha,\beta) = \theta$} nếu \mat{$
  pha\theta\eq \beta\theta$}

\mat{\[\begin{array}{l|l|l}
p & q & \theta 

\hline
Knows(John,x) & Knows(John,Jane) & \hbox{\note{$\{x/Jane\}$}}

Knows(John,x) & Knows(y,OJ)      & 

Knows(John,x) & Knows(y,Mother(y))& \phantom{\{y/John,x/Mother(John)\}}

Knows(John,x) & Knows(x,OJ)
\end{array}\]}

---
## Hợp nhất

Chúng ta có thể suy luận ngay lập tức nếu tìm được sự thay thế \mat{$\theta$}

sao cho \mat{$King(x)$} và \mat{$Greedy(x)$} khớp với \mat{$King(John)$} và \mat{$Greedy(y)$}

\mat{$\theta = \{x/John,y/John\}$} hoạt động

\mat{\noprog{Unify}}\mat{$(
  pha,\beta) = \theta$} nếu \mat{$
  pha\theta\eq \beta\theta$}

\mat{\[\begin{array}{l|l|l}
p & q & \theta 

\hline
Knows(John,x) & Knows(John,Jane) & \hbox{\note{$\{x/Jane\}$}}

Knows(John,x) & Knows(y,OJ)      & \hbox{\note{$\{x/OJ,y/John\}$}}

Knows(John,x) & Knows(y,Mother(y))& \phantom{\{y/John,x/Mother(John)\}}

Knows(John,x) & Knows(x,OJ)
\end{array}\]}

---
## Hợp nhất

Chúng ta có thể suy luận ngay lập tức nếu tìm được sự thay thế \mat{$\theta$}

sao cho \mat{$King(x)$} và \mat{$Greedy(x)$} khớp với \mat{$King(John)$} và \mat{$Greedy(y)$}

\mat{$\theta = \{x/John,y/John\}$} hoạt động

\mat{\noprog{Unify}}\mat{$(
  pha,\beta) = \theta$} nếu \mat{$
  pha\theta\eq \beta\theta$}

\mat{\[\begin{array}{l|l|l}
p & q & \theta 

\hline
Knows(John,x) & Knows(John,Jane) & \hbox{\note{$\{x/Jane\}$}}

Knows(John,x) & Knows(y,OJ)      & \hbox{\note{$\{x/OJ,y/John\}$}}

Knows(John,x) & Knows(y,Mother(y))& \hbox{\note{$\{y/John,x/Mother(John)\}$}}

Knows(John,x) & Knows(x,OJ)
\end{array}\]}

---
## Hợp nhất

Chúng ta có thể suy luận ngay lập tức nếu tìm được sự thay thế \mat{$\theta$}

sao cho \mat{$King(x)$} và \mat{$Greedy(x)$} khớp với \mat{$King(John)$} và \mat{$Greedy(y)$}

\mat{$\theta = \{x/John,y/John\}$} hoạt động

\mat{\noprog{Unify}}\mat{$(
  pha,\beta) = \theta$} nếu \mat{$
  pha\theta\eq \beta\theta$}

\mat{\[\begin{array}{l|l|l}
p & q & \theta 

\hline
Knows(John,x) & Knows(John,Jane) & \hbox{\note{$\{x/Jane\}$}}

Knows(John,x) & Knows(y,OJ)      & \hbox{\note{$\{x/OJ,y/John\}$}}

Knows(John,x) & Knows(y,Mother(y))& \hbox{\note{$\{y/John,x/Mother(John)\}$}}

Knows(John,x) & Knows(x,OJ) & \note{$fail$}
\end{array}\]}
\defn{Tiêu chuẩn hóa riêng biệt} loại bỏ sự chồng chéo của các biến, ví dụ: \mat{$Knows(z_{17},OJ)$}

---
## Phương thức tổng quát (GMP)

\mat{\[\frac{{p_1}', \;\; {p_2}', \; \ldots, \; {p_n}', \;\;
( p_1 \land p_2 \land \ldots \land p_n \Rightarrow q)}{q\theta}
 &nbsp;&nbsp;&nbsp;&nbsp;  \bbox{where }{p_i}'\theta \eq p_i\theta\bbox{ for all } i
\]}
\mat{\begin{formula}
{p_1}'  \bbox{ is }  King(John)  & p_1 \bbox{ is }  King(x) 

{p_2}' \bbox{ is }  Greedy(y)  & p_2  \bbox{ is }  Greedy(x) 

\theta  \bbox{ is }  \{x/John,y/John\} & q \bbox{ is } Evil(x) 

q\theta \bbox{ is } Evil(John)
\end{formula}}

GMP được sử dụng với KB của \defn{mệnh đề xác định} (*chính xác* một chữ dương)

Tất cả các biến giả định được định lượng phổ quát

---
## Tính hợp lý của GMP

Cần phải chứng tỏ điều đó 
\mat{\[{p_1}', \; \ldots, \; {p_n}', \;\;
( p_1 \land \ldots \land p_n \Rightarrow q) \models q\theta\]}
với điều kiện là \mat{${p_i}'\theta \eq p_i\theta$} cho tất cả \mat{$i$}

Bổ đề: Với mọi mệnh đề xác định \mat{$p$}, ta có \mat{$p \models p\theta$} theo UI

1. \mat{$( p_1 \land \ldots \land p_n \Rightarrow q) \models 
    ( p_1 \land \ldots \land p_n \Rightarrow q)\theta \eq
    ( p_1\theta \land \ldots \land p_n\theta \Rightarrow q\theta)$}

2. \mat{$ {p_1}', \; \ldots, \; {p_n}' \models
     {p_1}' \land \ldots \land {p_n}' \models
     {p_1}'\theta \land \ldots \land {p_n}'\theta $}

3. Từ 1 và 2, \mat{$q\theta$} tiếp theo là Modus Ponens thông thường

---
## Cơ sở kiến thức mẫu

Luật pháp quy định rằng việc người Mỹ bán vũ khí cho
các quốc gia thù địch.  Đất nước Nono\index{Nono}, kẻ thù của Mỹ,
có một số tên lửa và tất cả tên lửa của nó đã được Đại tá bán cho nó
Tây, người Mỹ.

Chứng minh rằng Col. West là tội phạm

---
## Ví dụ cơ sở kiến thức tiếp theo.

$\ldots$ việc một người Mỹ bán vũ khí cho các quốc gia thù địch là một tội ác:

---
## Ví dụ cơ sở kiến thức tiếp theo.

$\ldots$ việc một người Mỹ bán vũ khí cho các quốc gia thù địch là tội ác:
  
  \mat{$American(x) \land  Weapon(y)\land Sells(x,y,z) \land  Hostile(z) \implies Criminal(x)$}

Nono $\ldots$ có một số tên lửa

---
## Ví dụ cơ sở kiến thức tiếp theo.

$\ldots$ việc một người Mỹ bán vũ khí cho các quốc gia thù địch là tội ác:
  
  \mat{$American(x) \land  Weapon(y)\land Sells(x,y,z) \land  Hostile(z) \implies Criminal(x)$}

Nono $\ldots$ có một số tên lửa, tức là $\exists\,x\ Owns(Nono,x)\land Missile(x)$:
  
  \mat{$Owns(Nono,M_1)$} và \mat{$Missile(M_1)$}

$\ldots$ tất cả tên lửa của nó đã được Đại tá West bán cho nó

---
## Ví dụ cơ sở kiến thức tiếp theo.

$\ldots$ việc một người Mỹ bán vũ khí cho các quốc gia thù địch là tội ác:
  
  \mat{$American(x) \land  Weapon(y)\land Sells(x,y,z) \land  Hostile(z) \implies Criminal(x)$}

Nono $\ldots$ có một số tên lửa, tức là $\exists\,x\ Owns(Nono,x)\land Missile(x)$:
  
  \mat{$Owns(Nono,M_1)$} và \mat{$Missile(M_1)$}

$\ldots$ tất cả tên lửa của nó đã được Đại tá West bán cho nó
  
  \mat{$\All{x} Missile(x) \land Owns(Nono,x) \implies Sells(West,x,Nono)$}

Tên lửa là vũ khí:

---
## Ví dụ cơ sở kiến thức tiếp theo.

$\ldots$ việc một người Mỹ bán vũ khí cho các quốc gia thù địch là tội ác:
  
  \mat{$American(x) \land  Weapon(y)\land Sells(x,y,z) \land  Hostile(z) \implies Criminal(x)$}

Nono $\ldots$ có một số tên lửa, tức là $\exists\,x\ Owns(Nono,x)\land Missile(x)$:
  
  \mat{$Owns(Nono,M_1)$} và \mat{$Missile(M_1)$}

$\ldots$ tất cả tên lửa của nó đã được Đại tá West bán cho nó
  
  \mat{$\All{x} Missile(x) \land Owns(Nono,x) \implies Sells(West,x,Nono)$}

Tên lửa là vũ khí:
  
  \mat{$Missile(x)\Rightarrow Weapon(x)$}

Kẻ thù của Mỹ bị coi là “thù địch”:

---
## Ví dụ cơ sở kiến thức tiếp theo.

$\ldots$ việc một người Mỹ bán vũ khí cho các quốc gia thù địch là tội ác:
  
  \mat{$American(x) \land  Weapon(y)\land Sells(x,y,z) \land  Hostile(z) \implies Criminal(x)$}

Nono $\ldots$ có một số tên lửa, tức là $\exists\,x\ Owns(Nono,x)\land Missile(x)$:
  
  \mat{$Owns(Nono,M_1)$} và \mat{$Missile(M_1)$}

$\ldots$ tất cả tên lửa của nó đã được Đại tá West bán cho nó
  
  \mat{$\All{x} Missile(x) \land Owns(Nono,x) \implies Sells(West,x,Nono)$}

Tên lửa là vũ khí:
  
  \mat{$Missile(x)\Rightarrow Weapon(x)$}

Kẻ thù của Mỹ bị coi là "thù địch":
  
  \mat{$Enemy(x,America)\implies Hostile(x)$}

Tây, người Mỹ $\ldots$ 
  
  \mat{$American(West)$}

Đất nước Nono, kẻ thù của Mỹ $\ldots$
  
  \mat{$Enemy(Nono,America)$}

---
## Thuật toán chuỗi chuyển tiếp

```text
function FOL-FC-Ask(\v{KB), $
  pha$}{a substitution or \v{false}}

    repeat until \v{new} is empty
          \v{new}{$\emptyset$}
          for each sentence \v{r} in \v{KB} do 
                $(\v{p_1\land\ldots\land \v{p}_n\implies \v{q})$}{Standardize-Apart(\v{r})} 
                for each $\theta$ such that $(\v{p}_1 \land \ldots \land \v{p}_n)\theta = (\v{p}'_1 \land \ldots \land \v{p}'_n)\theta$
                                  for some $\v{p}'_1,\ldots,\v{p}'_n$ in \v{KB}
                      $\v{q'$}{Subst($\theta$, $\v{q}$)}
                      if $\v{q}'$ is not a renaming of a sentence already in \v{KB} or \v{new} then do
                            add $\v{q}'$ to \v{new}
                            $\phi$ <- Unify($\v{q'$, $
  pha$)}
                            \k{if} $\phi$ is not \v{fail} then return $\phi$
          add \v{new} to \v{KB}
    return \v{false}
```

---
## Chứng minh xích chuyển tiếp

![Hình ảnh](../TaiLieu/slide_md/figures/crime-fc1c.png)

---
## Chứng minh xích chuyển tiếp

![Hình ảnh](../TaiLieu/slide_md/figures/crime-fc2c.png)

---
## Chứng minh xích chuyển tiếp

![Hình ảnh](../TaiLieu/slide_md/figures/crime-fc3c.png)

---
##  Thuộc tính của chuỗi thuận 

Âm thanh và đầy đủ cho các mệnh đề xác định bậc một

(chứng minh tương tự chứng minh mệnh đề)

\defn{Datalog} = mệnh đề xác định thứ tự đầu tiên + *không có chức năng* (ví dụ: KB tội phạm)

FC chấm dứt Datalog trong nhiều lần lặp: tối đa \mat{$p\cdot n^k$} bằng chữ

Nói chung có thể không chấm dứt nếu không có \mat{$
  pha$}

Điều này là không thể tránh khỏi: việc đưa ra các mệnh đề xác định là có thể bán được

---
## Hiệu quả của chuỗi chuyển tiếp 

Quan sát đơn giản: không cần khớp quy tắc lặp \mat{$k$}

nếu tiền đề không được thêm vào trong lần lặp \mat{$k-1$}
    
$\implies$ khớp với từng quy tắc có tiền đề chứa nghĩa đen mới được thêm vào

Bản thân sự phù hợp có thể tốn kém

\defn{Lập chỉ mục cơ sở dữ liệu} cho phép \mat{$O(1)$} truy xuất các sự kiện đã biết
  
ví dụ: truy vấn \mat{$Missile(x)$} truy xuất \mat{$Missile(M_1)$}

Việc kết hợp các tiền đề liên kết với các sự kiện đã biết là NP-hard

Chuỗi chuyển tiếp được sử dụng rộng rãi trong cơ sở dữ liệu suy diễn \defn{}

---
## Ví dụ về khớp cứng

,4\maxfigwidth
 ![Hình ảnh](../TaiLieu/slide_md/figures/australia-csp.png) 

\hđiền

 
\tab\mat{$\Diff(wa,nt)\land \Diff(wa,sa)\land{}$}

[4pt]
\tab\tab\tab\mat{$\Diff(nt,q) \Diff(nt,sa)\land {}$}

[4pt]
\tab\tab\tab\mat{$\Diff(q,nsw)\land \Diff(q,sa)\land {}$}

[4pt]
\tab\tab\tab\mat{$\Diff(nsw,v)\land \Diff(nsw,sa)\land {}$}

[4pt]
\tab\tab\tab\mat{$\Diff(v,sa) \implies Colorable()$}

[8 điểm]
\tab\mat{$\Diff(Red,Blue)  &nbsp;&nbsp;  \Diff(Red,Green)$}

[4pt]
\tab\mat{$\Diff(Green,Red) &nbsp;&nbsp;  \Diff(Green,Blue)$}

[4pt]
\tab\mat{$\Diff(Blue,Red)  &nbsp;&nbsp;  \Diff(Blue,Green)$}

\mat{$Colorable()$} được suy ra nếu CSP có giải pháp 

CSP bao gồm 3SAT như một trường hợp đặc biệt, do đó việc so khớp là NP-hard

---
## Thuật toán xâu chuỗi ngược

```text
function FOL-BC-Ask(KB, goals, \(\theta\)) returns a set of substitutions
      inputs: KB, a knowledge base
      inputs: goals, a list of conjuncts forming a query (\(\theta\) already applied)
      inputs: \(\theta\), the current substitution, initially the empty substitution \(\emptyset\)
      local: answers, a set of substitutions, initially empty

    if goals is empty then return \(\{\theta\}\)
    \(q'\) <- Subst(\(\theta\), First(goals))
    for each sentence r in KB 
                where Standardize-Apart(r) = \((p_1 \land \ldots \land p_n \Rightarrow q)\)
                and \(\theta'\) <- Unify(q, \(q'\)) succeeds
          new\_goals <- \([p_1,\ldots,p_n|\)Rest(goals)\(]\)
          answers <- \mbox{FOL-BC-Ask(KB, new\_goals, Compose(\(\theta'\), \(\theta\))) \(\cup\) answers}
    return answers
```

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc01c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc02c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc03c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc04c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc05c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc06c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/crime-bc07c.png)

---
##  Thuộc tính của chuỗi ngược 

Tìm kiếm bằng chứng đệ quy theo chiều sâu: không gian có kích thước tuyến tính của bằng chứng

Chưa hoàn thành do vòng lặp vô hạn
  
$\implies$ khắc phục bằng cách kiểm tra mục tiêu hiện tại với mọi mục tiêu trên ngăn xếp

Không hiệu quả do các mục tiêu phụ lặp đi lặp lại (cả thành công và thất bại)
  
$\implies$ sửa lỗi sử dụng bộ nhớ đệm của các kết quả trước đó (thêm dung lượng!)

Được sử dụng rộng rãi (không có cải tiến!) cho \defn{lập trình logic}

---
## Lập trình logic

Âm thanh cắn: tính toán như suy luận trên KB logic

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
|  | \note{Lập trình logic} | \note{Lập trình thông thường} |
| 1. | Xác định vấn đề | Xác định vấn đề |
| 2. | Tập hợp thông tin | Tập hợp thông tin |
| 3. | Tea break | Tìm giải pháp |
| 4. | Mã hóa thông tin trong KB | Giải pháp chương trình |
| 5. | Mã hóa trường hợp vấn đề dưới dạng dữ kiện | Mã hóa trường hợp vấn đề dưới dạng dữ liệu |
| 6. | Đặt câu hỏi | Áp dụng chương trình vào dữ liệu |
| 7. | Tìm thông tin sai | Gỡ lỗi thủ tục |

Sẽ dễ gỡ lỗi \mat{$Capital(NewYork,US)$} hơn \mat{$x:= x+2$}!

---
## Hệ thống Prolog

Cơ sở: xâu chuỗi ngược với mệnh đề Horn + chuông \& còi

Được sử dụng rộng rãi ở Châu Âu, Nhật Bản (cơ sở của dự án Thế hệ thứ 5)

Kỹ thuật tổng hợp $\Rightarrow$ tiếp cận một tỷ LIPS

Chương trình = tập hợp các mệnh đề = `head :- Literal$_1$, $\ldots$ Literal$_n$`

```text
criminal(X) :- american(X), weapon(Y), sells(X,Y,Z), hostile(Z).
```

Hợp nhất hiệu quả bằng \defn{mã hóa mở}

Truy xuất hiệu quả các mệnh đề phù hợp bằng cách liên kết trực tiếp

Chuỗi lùi theo chiều sâu, từ trái sang phải

Các vị từ tích hợp sẵn cho số học, v.v., ví dụ: `X is Y*Z+3`

Giả định thế giới đóng ("phủ định là thất bại")
  
   ví dụ: cho `còn sống(X) :- chưa chết(X).
  
   {\tt live(joe)` thành công nếu `dead(joe)` thất bại

---
## Ví dụ về Prolog

Tìm kiếm theo chiều sâu từ trạng thái bắt đầu `X`:

```text
dfs(X) :- goal(X).
dfs(X) :- successor(X,S),dfs(S).
```

Không cần lặp lại `S`: `kế thừa` thành công cho mỗi

Nối hai danh sách để tạo ra danh sách thứ ba:

```text
append([],Y,Y).                         
append([X|L],Y,[X|Z]) :- append(L,Y,Z). 
                                        
query:   append(A,B,[1,2]) ?            
answers: A=[]    B=[1,2]
         A=[1]   B=[2]
         A=[1,2] B=[]
```

---
## Giải pháp: tóm tắt ngắn gọn

Phiên bản đặt hàng đầu tiên đầy đủ:
\mat{\[\frac {\ell_1 \lor \cdots\lor \ell_k, &nbsp;&nbsp;&nbsp;&nbsp;  m_1 \lor \cdots\lor m_n}
        {(\ell_1 \lor \cdots\lor \ell_{i-1}\lor \ell_{i+1}\lor\cdots\lor \ell_k
        \lor m_1 \lor \cdots \lor m_{j-1}\lor m_{j+1}\lor\cdots\lor m_n)\theta}
\]}
ở đâu \mat{$\noprog{Unify}(\ell_i,\lnot m_j) \eq \theta$}.

Ví dụ,
\mat{\begin{formula}
{\begin{array}{l} \lnot Rich(x) \lor Unhappy(x) 

                  Rich(Ken)
 \end{array}}
\over
{\begin{array}{l} Unhappy(Ken)
 \end{array}}
\end{formula}}
với \mat{$\theta = \{x/Ken\}$}

Áp dụng các bước giải quyết cho \mat{$CNF(KB\land \lnot 
  pha)$}; hoàn thành cho FOL

---
## Chuyển đổi sang CNF

Ai yêu thương mọi loài vật thì sẽ có người yêu thương:
   
  \mat{$\All{x} [\All{y} Animal(y) \implies Loves(x,y)] \implies [\Exi{y} Loves(y,x)]$}

1. Loại bỏ các câu điều kiện và hàm ý
\mat{\[
 \All{x} [\lnot \All{y} \lnot Animal(y) \lor Loves(x,y)] \lor [\Exi{y} Loves(y,x)]
\]}
2. Di chuyển \mat{$\lnot$} vào trong: \mat{$\lnot \All{x,p} \equiv \Exi{x} \lnot p$}, &nbsp;&nbsp; 
                         \mat{$\lnot \Exi{x,p} \equiv \All{x} \lnot p$}:
\mat{\begin{formula}
 \All{x} [\Exi{y} \lnot(\lnot Animal(y) \lor Loves(x,y))] \lor [\Exi{y} Loves(y,x)] 

 \All{x} [\Exi{y} \lnot\lnot Animal(y) \land \lnot Loves(x,y)] \lor [\Exi{y} Loves(y,x)] 

 \All{x} [\Exi{y} Animal(y) \land \lnot Loves(x,y)] \lor [\Exi{y} Loves(y,x)] 
\end{formula}}

---
## Chuyển đổi sang CNF tiếp.

3. Chuẩn hóa các biến: mỗi bộ định lượng nên sử dụng một biến định lượng khác nhau
\mat{\[
 \All{x} [\Exi{y} Animal(y) \land \lnot Loves(x,y)] \lor [\Exi{z} Loves(z,x)] 
\]}
4. Skolemize: một hình thức tổng quát hơn của sự khởi tạo hiện sinh.
    
   Mỗi biến tồn tại được thay thế bằng hàm \defn{Skolem}
    
   của các biến định lượng phổ quát kèm theo:
\mat{\[
 \All{x} [Animal(F(x)) \land \lnot Loves(x,F(x))] \lor Loves(G(x),x)
\]}
5. Bỏ các bộ định lượng phổ quát:
\mat{\[
 [Animal(F(x)) \land \lnot Loves(x,F(x))] \lor Loves(G(x),x)
\]}
6. Phân phối \mat{$\land$} trên \mat{$\lor$}:
\mat{\[
 [Animal(F(x)) \lor Loves(G(x),x)] \land [\lnot Loves(x,F(x)) \lor Loves(G(x),x)]
\]}

---
##  Chứng minh độ phân giải: mệnh đề xác định 

![Hình ảnh](../TaiLieu/slide_md/figures/crime-resolution.png)