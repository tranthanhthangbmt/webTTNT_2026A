\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Suy diễn trong logic bậc một (Inference in first-order logic)

## Chương 9, Phần 1--4

---
## Nội dung

- Các phép chứng minh (Proofs)

- Sự hợp nhất (Unification)

- Modus Ponens tổng quát (Generalized Modus Ponens)

- Suy diễn tiến và lùi (Forward and backward chaining)

---
## Các phép chứng minh

Suy diễn đúng đắn: tìm $
  pha$ sao cho $KB \models 
  pha$.

Quá trình chứng minh là một quá trình <u>tìm kiếm</u>, các toán tử là các quy tắc suy diễn.

Ví dụ, Modus Ponens (MP)
\[\displaystyle
\frac{
  pha, &nbsp;&nbsp;  
  pha\implies\beta}{\beta}  &nbsp;&nbsp;&nbsp;&nbsp; 
\frac{At(Joe,UCB) &nbsp;&nbsp;  At(Joe,UCB)\implies OK(Joe)}{OK(Joe)}
\]

Ví dụ, And-Introduction (AI)
\[\displaystyle
\frac{
  pha  &nbsp;&nbsp;  \beta}{
  pha \land \beta}  &nbsp;&nbsp;&nbsp;&nbsp; 
\frac{OK(Joe) &nbsp;&nbsp;  CSMajor(Joe)}{OK(Joe)\land CSMajor(Joe)}
\]

Ví dụ, Universal Elimination (UE)
\[\displaystyle
\frac{\All{x} 
  pha}{
  pha\{x/\tau\}}  &nbsp;&nbsp;&nbsp;&nbsp; 
\frac{\All{x} At(x,UCB)\implies OK(x)}{At(Pat,UCB)\implies OK(Pat)}
\]
$\tau$ phải là một hạng thức cơ sở (ground term) (tức là, không có biến số)

---
## Ví dụ chứng minh

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| Bob là một con trâu | 1. | $Buffalo(Bob)$ |
| Pat là một con lợn | 2. | $Pig(Pat)$ |
| Trâu chạy nhanh hơn lợn | 3. | $\All{x,y} Buffalo(x) \land Pig(y) \implies Faster(x,y)$ |
| Bob chạy nhanh hơn Pat |  | \phantom{$Buffalo(Bob) \land Pig(Pat) \implies Faster(Bob,Pat)$} |
| \phantom{UE 3, $\{x/Bob,y/Pat\}$} |  |  |

---
## Ví dụ chứng minh

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| \phantom{Bob là một con trâu} |  |  |
| \phantom{UE 3, $\{x/Bob,y/Pat\}$} |  |  |
| \phantom{Trâu chạy nhanh hơn lợn} |  |  |
| \phantom{Bob chạy nhanh hơn Pat} |  | \phantom{$Buffalo(Bob) \land Pig(Pat) \implies Faster(Bob,Pat)$} |
| AI 1 \ | 2 | 4. | $Buffalo(Bob) \land Pig(Pat)$ |

---
## Ví dụ chứng minh

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| \phantom{Bob là một con trâu} |  |  |
| \phantom{Pat là một con lợn} |  |  |
| \phantom{Trâu chạy nhanh hơn lợn} |  |  |
| \phantom{Bob chạy nhanh hơn Pat} |  | \phantom{$Buffalo(Bob) \land Pig(Pat) \implies Faster(Bob,Pat)$} |
| \phantom{AI 1 \ | 2} |  |  |
| UE 3, $\{x/Bob,y/Pat\}$ | 5. | $Buffalo(Bob) \land Pig(Pat) \implies Faster(Bob,Pat)$ |

---
## Ví dụ chứng minh

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| \phantom{Bob là một con trâu} |  |  |
| \phantom{Pat là một con lợn} |  |  |
| \phantom{Trâu chạy nhanh hơn lợn} |  |  |
| \phantom{Bob chạy nhanh hơn Pat} |  | \phantom{$Buffalo(Bob) \land Pig(Pat) \implies Faster(Bob,Pat)$} |
| \phantom{AI 1 \ | 2} |  |  |
| \phantom{UE 3, $\{x/Bob,y/Pat\}$} |  |  |
| MP 6 \ | 7 | 6. | $Faster(Bob,Pat)$ |

---
## Tìm kiếm với các quy tắc suy diễn nguyên thủy

Các toán tử là các quy tắc suy diễn

Các trạng thái là các tập hợp các câu

Kiểm tra đích kiểm tra trạng thái để xem nó có chứa câu truy vấn hay không

![Hình ảnh](../TaiLieu/slide_md/figures/naive-proof-tree.png)
 

AI, UE, MP là một mẫu suy diễn phổ biến

<u>Vấn đề</u>: hệ số phân nhánh khổng lồ, đặc biệt đối với UE

<u>Ý tưởng</u>: tìm một phép thế làm cho tiền đề của quy tắc khớp với một số
sự kiện đã biết
  
$\Rightarrow$ một quy tắc suy diễn duy nhất, mạnh mẽ hơn

---
## Sự hợp nhất (Unification)

Một phép thế $\sigma$ hợp nhất các câu nguyên thủy $p$ và $q$ nếu
<u>\u{$p\sigma = q\sigma$</u>}
\[\begin{array}{l|l|l}
p & q & \sigma 

\hline
Knows(John,x) & Knows(John,Jane) & 

Knows(John,x) & Knows(y,OJ)      & 

Knows(John,x) & Knows(y,Mother(y)& \phantom{\{y/John,x/Mother(John)\}}

\end{array}\]

---
## Sự hợp nhất

.
\[\begin{array}{l|l|l}
 &  &  

\hline
\phantom{Knows(John,x)} & \phantom{Knows(John,Jane)} & \{x/Jane\}

\phantom{Knows(John,x)} & \phantom{Knows(y,OJ)}      & \{x/John,y/OJ\}

\phantom{Knows(John,x)} & \phantom{Knows(y,Mother(y)}& \{y/John,x/Mother(John)\}

\end{array}\]
<u>Ý tưởng</u>: Hợp nhất các tiền đề quy tắc với các sự kiện đã biết, áp dụng phép hợp nhất cho kết luận

| &nbsp; | &nbsp; |
|---|---|
| Ví dụ, nếu chúng ta biết $q$ và | $Knows(John,x) \implies Likes(John,x)$ |
| thì chúng ta kết luận | $Likes(John,Jane)$ |
|  | $Likes(John,OJ)$ |
|  | $Likes(John,Mother(John))$ |

---
## Modus Ponens tổng quát (Generalized Modus Ponens - GMP)

\[\frac{{p_1}', \;\; {p_2}', \; \ldots, \; {p_n}', \;\;
( p_1 \land p_2 \land \ldots \land p_n \Rightarrow q)}{q\sigma}
 &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{trong đó }{p_i}'\sigma \eq p_i\sigma\mbox{ với mọi } i
\]

| &nbsp; | &nbsp; |
|---|---|
| Ví dụ ${p_1}'\eq$ | Faster(Bob,Pat) |
| ${p_2}'\eq$ | Faster(Pat,Steve) |
| $p_1 \land p_2 \implies q\ \eq$ | $Faster(x,y) \land Faster(y,z) \implies Faster(x,z)$ |
| $\sigma\eq$ | $\{x/Bob,y/Pat,z/Steve\}$ |
| $q\sigma\eq$ | $Faster(Bob,Steve)$ |

GMP được sử dụng với KB của <u>các mệnh đề xác định (definite clauses)</u> (*chính xác* một literal khẳng định):

hoặc là một câu nguyên thủy đơn hoặc
    
(phép hội của các câu nguyên thủy) $\Rightarrow$ (câu nguyên thủy)

Tất cả các biến được giả định là có lượng từ phổ dụng

---
## Tính đúng đắn của GMP

Cần phải chỉ ra rằng 
\[{p_1}', \; \ldots, \; {p_n}', \;\;
( p_1 \land \ldots \land p_n \Rightarrow q) \models q\sigma\]
với điều kiện là ${p_i}'\sigma \eq p_i\sigma$ với mọi $i$

Bổ đề: Đối với bất kỳ mệnh đề xác định $p$ nào, ta có $p \models p\sigma$ bằng UE

1. $( p_1 \land \ldots \land p_n \Rightarrow q) \models 
    ( p_1 \land \ldots \land p_n \Rightarrow q)\sigma \eq
    ( p_1\sigma \land \ldots \land p_n\sigma \Rightarrow q\sigma)$

2. $ {p_1}', \; \ldots, \; {p_n}' \models
     {p_1}' \land \ldots \land {p_n}' \models
     {p_1}'\sigma \land \ldots \land {p_n}'\sigma $

3. Từ 1 và 2, $q\sigma$ được rút ra bằng MP đơn giản

---
## Suy diễn tiến (Forward chaining)

Khi một sự kiện mới $p$ được thêm vào KB
  
   với mỗi quy tắc sao cho $p$ hợp nhất với một tiền đề
    
      nếu các tiền đề khác <u>đã biết</u>
    
      thì thêm kết luận vào KB và tiếp tục suy diễn (chaining)

Suy diễn tiến <u>được thúc đẩy bởi dữ liệu (data-driven)</u>
    
ví dụ, suy diễn các thuộc tính và loại từ các nhận thức

---
## Ví dụ suy diễn tiến

Lần lượt thêm các sự kiện 1, 2, 3, 4, 5, 7.

Số trong [] = literal hợp nhất; \tick\ chỉ ra quy tắc được kích hoạt

<u>1.</u> $Buffalo(x) \land Pig(y) \implies Faster(x,y)$

<u>2.</u> $Pig(y) \land Slug(z) \implies Faster(y,z)$

<u>3.</u> $Faster(x,y) \land Faster(y,z) \implies Faster(x,z)$

<u>4.</u> $Buffalo(Bob)$ <u>[1a,\cross]</u>

<u>5.</u> $Pig(Pat)$ <u>[1b,\tick]</u> $\rightarrow$ <u>6.</u> $Faster(Bob,Pat)$ <u>[3a,\cross]</u>, <u>[3b,\cross]</u>

\phantom{<u>5.</u> $Pig(Pat)$} <u>[2a,\cross]</u>

<u>7.</u> $Slug(Steve)$ <u>[2b,\tick]</u>
  
$\rightarrow$<u>8.</u> $Faster(Pat,Steve)$ <u>[3a,\cross]</u>, <u>[3b,\tick]</u>
    
$\rightarrow$<u>9.</u> $Faster(Bob,Steve)$ <u>[3a,\cross]</u>, <u>[3b,\cross]</u>

---
## Suy diễn lùi (Backward chaining)

Khi một truy vấn $q$ được hỏi
  
   nếu một sự kiện khớp $q'$ đã được biết, trả về bộ hợp nhất
  
   với mỗi quy tắc mà hệ quả $q'$ của nó khớp với $q$
    
      cố gắng chứng minh từng tiền đề của quy tắc bằng suy diễn lùi

(Có một số phức tạp được thêm vào trong việc theo dõi các bộ hợp nhất)

(Nhiều phức tạp hơn giúp tránh các vòng lặp vô hạn)

Hai phiên bản: tìm <u>bất kỳ</u> giải pháp nào, tìm <u>tất cả</u> các giải pháp

Suy diễn lùi là cơ sở cho <u>lập trình logic (logic programming)</u>, ví dụ: Prolog

---
## Ví dụ suy diễn lùi

<u>1.</u> $Pig(y) \land Slug(z) \implies Faster(y,z)$

<u>2.</u> $Slimy(z) \land Creeps(z) \implies Slug(z)$

<u>3.</u> $Pig(Pat)$  &nbsp;&nbsp;&nbsp;&nbsp;  <u>4.</u> $Slimy(Steve)$  &nbsp;&nbsp;&nbsp;&nbsp;  <u>5.</u> $Creeps(Steve)$

![Hình ảnh](../TaiLieu/slide_md/figures/slug-bc.png)