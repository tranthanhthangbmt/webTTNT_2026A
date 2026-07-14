\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Tác tử logic (Logical agents)

## Chương 6

---
## Nội dung

- Cơ sở tri thức (Knowledge bases)

- Thế giới Wumpus

- Logic nói chung

- Logic mệnh đề (Logic Boolean)

- Các dạng chuẩn (Normal forms)

- Các quy tắc suy diễn (Inference rules)

---
## Cơ sở tri thức

![Hình ảnh](../TaiLieu/slide_md/figures/kbs.png)

Cơ sở tri thức = tập hợp các <u>câu</u> trong một ngôn ngữ <u>hình thức</u>

Cách tiếp cận <u>Khai báo (Declarative)</u> để xây dựng một tác tử (hoặc hệ thống khác):
    
   **Tell** (Cho biết) những gì nó cần biết

Sau đó nó có thể tự **Ask** (Hỏi) xem cần phải làm gì---câu trả lời phải được suy ra từ KB (cơ sở tri thức)

Các tác tử có thể được xem xét ở <u>cấp độ tri thức</u>
    
   tức là, chúng biết gì, bất kể việc được cài đặt như thế nào

Hoặc ở <u>cấp độ cài đặt</u>
    
   tức là, cấu trúc dữ liệu trong KB và các thuật toán thao tác trên chúng

---
## Một tác tử dựa trên tri thức đơn giản

```text
function KB-Agent(percept) returns một hành động (action)
      static: KB, một cơ sở tri thức (knowledge base)
      static: t, bộ đếm, ban đầu là 0, chỉ báo thời gian

    Tell(KB, Make-Percept-Sentence(percept, t))
    action <- Ask(KB, Make-Action-Query(t))
    Tell(KB, Make-Action-Sentence(action, t))
    t <- t + 1
    return action
```

Tác tử phải có khả năng:
  
Biểu diễn các trạng thái, hành động, v.v.
  
Kết hợp các nhận thức mới
  
Cập nhật các biểu diễn nội bộ của thế giới
  
Suy diễn các thuộc tính ẩn của thế giới
  
Suy diễn các hành động phù hợp

---
## Mô tả PAGE cho Thế giới Wumpus

<u>Nhận thức</u> Gió nhẹ (Breeze), Lấp lánh (Glitter), Mùi (Smell)

<u>Hành động</u> Rẽ trái (Left turn), Rẽ phải (Right turn),
    
    Đi tới (Forward), Lấy (Grab), Thả (Release), Bắn (Shoot)

<u>Đích</u> Mang vàng trở lại điểm xuất phát

mà không rơi vào hố hoặc ô có Wumpus

 

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-world.png)

<u>Môi trường</u>
  
Các ô kề với wumpus có mùi
  
Các ô kề với hố có gió nhẹ
  
Lấp lánh khi và chỉ khi vàng ở trong cùng ô đó
  
Bắn sẽ giết wumpus nếu bạn đang đối mặt với nó
  
Bắn sẽ làm tiêu hao mũi tên duy nhất
  
Lấy sẽ nhặt vàng nếu ở cùng ô đó
  
Thả sẽ đánh rơi vàng trong cùng ô đó

---
## Đặc điểm thế giới Wumpus

<u>Thế giới có tất định không?</u>??

<u>Thế giới có thể truy cập đầy đủ không?</u>??

<u>Thế giới có tĩnh không?</u>??

<u>Thế giới có rời rạc không?</u>??

---
## Đặc điểm thế giới Wumpus

<u>Thế giới có tất định không?</u>?? Có---kết quả được xác định chính xác

<u>Thế giới có thể truy cập đầy đủ không?</u>?? Không---chỉ nhận thức <u>cục bộ</u>

<u>Thế giới có tĩnh không?</u>?? Có---Wumpus và các hố không di chuyển

<u>Thế giới có rời rạc không?</u>?? Có

---
## Khám phá một thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq0.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq1.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq2.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq3.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq4.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq5.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq6.png)

\pheading{}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq7.png)

---
## Các tình huống khó khăn khác

in
\raisebox{-0.5in}[2.5in]{![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-bb.png)}
 

Gió nhẹ ở (1,2) và (2,1)
  
$\Rightarrow$ không có hành động nào an toàn

Giả sử các hố được phân bố đều,

(2,2) có khả năng có hố nhất

     

in
![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-s.png)
 

Mùi ở (1,1) 
  
$\Rightarrow$ không thể di chuyển

Có thể sử dụng chiến lược <u>ép buộc (coercion)</u>:
  
  bắn thẳng về phía trước
  
  nếu có wumpus ở đó $\Rightarrow$ chết $\Rightarrow$ an toàn
  
  nếu wumpus không ở đó $\Rightarrow$ an toàn
  

---
## Logic nói chung

<u>Các logic</u> là các ngôn ngữ hình thức để biểu diễn thông tin
  
   sao cho có thể rút ra các kết luận

<u>Cú pháp (Syntax)</u> xác định các câu trong ngôn ngữ

<u>Ngữ nghĩa (Semantics)</u> định nghĩa "ý nghĩa" của các câu;
  
   tức là, định nghĩa <u>sự thật (truth)</u> của một câu trong một thế giới

Ví dụ, ngôn ngữ của số học

$x+2 \geq y$ là một câu; $x2+y>{}$ không phải là một câu

$x+2 \geq y$ là đúng khi và chỉ khi số $x+2$ không nhỏ hơn
số $y$

$x+2 \geq y$ là đúng trong một thế giới mà $x\eq 7,\ y\eq 1$

$x+2 \geq y$ là sai trong một thế giới mà $x\eq 0,\ y\eq 6$

---
## Các loại logic

Các logic được đặc trưng bởi những gì chúng cam kết là "nguyên thủy"

Cam kết bản thể học (Ontological commitment): điều gì tồn tại---sự kiện? đối tượng? thời gian? niềm tin?

Cam kết nhận thức học (Epistemological commitment): các trạng thái tri thức là gì?

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| {\tf Ngôn ngữ (Language)} | {\tf Cam kết Bản thể học (Ontological Commitment)} | {\tf Cam kết Nhận thức học (Epistemological Commitment)} |
| Logic mệnh đề (Propositional logic) | sự kiện | đúng/sai/không biết |
| Logic bậc một (First-order logic) | sự kiện, đối tượng, quan hệ | đúng/sai/không biết |
| Logic thời gian (Temporal logic) | sự kiện, đối tượng, quan hệ, thời gian | đúng/sai/không biết |
| Lý thuyết xác suất (Probability theory) | sự kiện | mức độ tin tưởng 0\ldots 1 |
| Logic mờ (Fuzzy logic) | mức độ đúng đắn | mức độ tin tưởng 0\ldots 1 |

---
## Kéo theo (Entailment)

\[KB \models 
  pha\]

Cơ sở tri thức $KB$ <u>kéo theo (entails)</u> câu $
  pha$
    
   khi và chỉ khi

$
  pha$ đúng trong tất cả các thế giới mà $KB$ đúng

Ví dụ, KB chứa "đội Giants thắng" và "đội Reds thắng"

kéo theo "Hoặc đội Giants thắng hoặc đội Reds thắng"

---
## Mô hình (Models)

Các nhà logic học thường suy nghĩ dưới dạng các <u>mô hình (models)</u>, là các thế giới có cấu trúc

hình thức mà theo đó chân lý có thể được đánh giá

Ta nói $m$ là một <u>mô hình</u> của câu $
  pha$
nếu $
  pha$ là đúng trong $m$

$M(
  pha)$ là tập hợp tất cả các mô hình của $
  pha$

Khi đó $KB \models 
  pha$ khi và chỉ khi $M(KB) \subseteq M(
  pha)$

Ví dụ: $KB$ = Giants thắng và Reds thắng
    
     $
  pha$ = Giants thắng

 
in
\raisebox{-2in}[0in]{![Hình ảnh](../TaiLieu/slide_md/figures/model-inclusion.png)}

---
## Suy diễn (Inference)

$KB\vdash_i
  pha$ = câu $
  pha$ có thể được dẫn xuất từ $KB$ bằng thủ tục $i$

<u>Tính đúng đắn (Soundness)</u>: $i$ là đúng đắn nếu
    
bất cứ khi nào $KB\vdash_i
  pha$, thì nó cũng đúng là $KB\models
  pha$

<u>Tính đầy đủ (Completeness)</u>: $i$ là đầy đủ nếu
    
bất cứ khi nào $KB\models
  pha$, thì nó cũng đúng là $KB\vdash_i
  pha$

Xem trước: chúng ta sẽ định nghĩa một logic (logic bậc một) mà đủ
biểu đạt để nói hầu hết những điều quan tâm, và với nó
có tồn tại một thủ tục suy diễn đúng đắn và đầy đủ.

Nghĩa là, thủ tục sẽ trả lời mọi câu hỏi mà câu trả lời có thể được rút ra
từ những gì mà $KB$ đã biết.

---
## Logic mệnh đề: Cú pháp

Logic mệnh đề là logic đơn giản nhất---minh họa các ý tưởng cơ bản

Các ký hiệu mệnh đề $P_1$, $P_2$, v.v. là các câu

Nếu $S$ là một câu, $\lnot S$ là một câu

Nếu $S_1$ và $S_2$ là câu, $S_1 \land S_2$ là một câu

Nếu $S_1$ và $S_2$ là câu, $S_1 \lor S_2$ là một câu

Nếu $S_1$ và $S_2$ là câu, $S_1 \implies S_2$ là một câu

Nếu $S_1$ và $S_2$ là câu, $S_1 \lequiv S_2$ là một câu

---
## Logic mệnh đề: Ngữ nghĩa

Mỗi mô hình chỉ định đúng/sai cho từng ký hiệu mệnh đề

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|
| Ví dụ: | $A$ | $B$ | $C$ |
|  | $Đúng$ | $Đúng$ | $Sai$ |

Các quy tắc đánh giá chân lý đối với mô hình $m$:

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|
| $\lnot S$ | đúng khi và chỉ khi | $S$ | sai |  |  |
| $S_1 \land S_2$ | đúng khi và chỉ khi | $S_1$ | đúng <u>và</u> | $S_2$ | đúng |
| $S_1 \lor S_2$ | đúng khi và chỉ khi | $S_1$ | đúng <u>hoặc</u> | $S_2$ | đúng |
| $S_1 \implies S_2$ | đúng khi và chỉ khi | $S_1$ | sai <u>hoặc</u> | $S_2$ | đúng |
|  &nbsp;&nbsp;&nbsp;&nbsp;  tức là, | sai khi và chỉ khi | $S_1$ | đúng <u>và</u> | $S_2$ | sai |
| $S_1 \lequiv S_2$ | đúng khi và chỉ khi | $S_1\implies S_2$ | đúng <u>và</u> | $S_2\implies S_1$ | đúng |

---
## Suy diễn mệnh đề: Phương pháp liệt kê

Cho $
  pha = A \lor B$ và $KB = (A\lor C) \land (B \lor \lnot C)$

Liệu có trường hợp $KB\models
  pha$ không? 

Kiểm tra mọi mô hình có thể---$
  pha$ phải đúng ở mọi nơi mà $KB$ đúng

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|---|
| $A$ | $B$ | $C$ | \ $A\lor C$\ | $B \lor \lnot C$ | \ \ \ $KB$\ \ \ | \ \ \ \ $
  pha$\ \ \ \ |
| $Sai$ | $Sai$ | $Sai$ |  |  |  |  |
| $Sai$ | $Sai$ | $Đúng$ |  |  |  |  |
| $Sai$ | $Đúng$ | $Sai$ |  |  |  |  |
| $Sai$ | $Đúng$ | $Đúng$ |  |  |  |  |
| $Đúng$ | $Sai$ | $Sai$ |  |  |  |  |
| $Đúng$ | $Sai$ | $Đúng$ |  |  |  |  |
| $Đúng$ | $Đúng$ | $Sai$ |  |  |  |  |
| $Đúng$ | $Đúng$ | $Đúng$ |  |  |  |  |

---
## Suy diễn mệnh đề: Giải pháp

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|---|
| $A$ | $B$ | $C$ | \ $A\lor C$\ | $B \lor \lnot C$ | \ \ \ $KB$\ \ \ | \ \ \ \ $
  pha$\ \ \ \ |
| $Sai$ | $Sai$ | $Sai$ | $Sai$ | $Đúng$ | $Sai$ | $Sai$ |
| $Sai$ | $Sai$ | $Đúng$ | $Đúng$ | $Sai$ | $Sai$ | $Sai$ |
| $Sai$ | $Đúng$ | $Sai$ | $Sai$ | $Đúng$ | $Sai$ | $Đúng$ |
| $Sai$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ |
| $Đúng$ | $Sai$ | $Sai$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ |
| $Đúng$ | $Sai$ | $Đúng$ | $Đúng$ | $Sai$ | $Sai$ | $Đúng$ |
| $Đúng$ | $Đúng$ | $Sai$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ |
| $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ | $Đúng$ |

---
## Các dạng chuẩn (Normal forms)

Các phương pháp tiếp cận khác đối với việc suy diễn sử dụng các thao tác cú pháp
trên câu, thường được thể hiện ở dạng chuẩn

<u>Dạng chuẩn hội (Conjunctive Normal Form - CNF)</u> (phổ quát)
    
    *phép hội* của $\underbrace{\mbox{các *phép tuyển* của các *literal*}}$
    
    \phantom{*phép hội* của các *phép t*}*các mệnh đề*
    
    Ví dụ: $(A \lor \lnot B) \land (B \lor \lnot C \lor \lnot D)$

<u>Dạng chuẩn tuyển (Disjunctive Normal Form - DNF)</u> (phổ quát)
    
    *phép tuyển* của $\underbrace{\mbox{các *phép hội* của các *literal*}}$
    
    \phantom{*phép tuyển* của các *phép h*}*các số hạng*
    
    Ví dụ: $(A\land B) \lor (A \land \lnot C) \lor (A \land \lnot D)
           \lor (\lnot B \land \lnot C) \lor (\lnot B \land \lnot D)$

<u>Dạng Horn (Horn Form)</u> (bị hạn chế)
    
    *phép hội* của các *mệnh đề Horn* (các mệnh đề có $\leq 1$ literal khẳng định)
    
    Ví dụ: $(A \lor \lnot B) \land (B \lor \lnot C \lor \lnot D)$
    
    Thường được viết dưới dạng tập hợp các phép kéo theo:
    
    $B \implies A$ và $(C \land D) \implies B$

---
## Tính hợp lệ và Tính thỏa mãn được

Một câu là <u>hợp lệ (valid)</u> nếu nó đúng trong <u>tất cả</u> các mô hình
    
ví dụ, $A \lor \lnot A$,  &nbsp;&nbsp;&nbsp;&nbsp;  $A \implies A$,  &nbsp;&nbsp;&nbsp;&nbsp;  
      $(A \land (A \implies B)) \implies B$

Tính hợp lệ được liên kết với suy diễn qua <u>Định lý suy diễn (Deduction Theorem)</u>:
    
      $KB \models 
  pha$ khi và chỉ khi $(KB \implies 
  pha)$ là hợp lệ

Một câu là <u>thỏa mãn được (satisfiable)</u> nếu nó đúng trong <u>một số</u> mô hình
    
ví dụ, $A\lor B$, &nbsp;&nbsp;&nbsp;&nbsp;  $C$

Một câu là <u>không thỏa mãn được (unsatisfiable)</u> nếu nó không đúng trong <u>bất kỳ</u> mô hình nào
    
ví dụ, $A\land \lnot A$

Tính thỏa mãn được liên kết với suy diễn thông qua điều sau:
    
      $KB \models 
  pha$ khi và chỉ khi $(KB \land \lnot 
  pha)$ là không thỏa mãn được

tức là, chứng minh $
  pha$ bằng phương pháp *phản chứng (reductio ad absurdum)*

---
## Các phương pháp chứng minh

Các phương pháp chứng minh chia thành (khoảng) hai loại:
  

<u>Kiểm tra mô hình (Model checking)</u>
  
    liệt kê bảng chân lý (đúng đắn và đầy đủ cho logic mệnh đề)
  
    tìm kiếm heuristic trong không gian mô hình (đúng đắn nhưng không đầy đủ)
    
       ví dụ, thuật toán GSAT (Bài tập 6.15)

<u>Áp dụng các quy tắc suy diễn (Application of inference rules)</u>
  
    Sinh (đúng đắn) hợp pháp các câu mới từ những câu cũ
  
    <u>Chứng minh (Proof)</u> = một chuỗi các ứng dụng quy tắc suy diễn
    
       Có thể sử dụng các quy tắc suy diễn như các toán tử trong một thuật toán tìm kiếm tiêu chuẩn.

---
## Các quy tắc suy diễn cho logic mệnh đề

<u>Hợp giải (Resolution)</u> (đối với dạng CNF): đầy đủ cho logic mệnh đề
\[
\frac{
  pha \lor \beta, &nbsp;&nbsp;&nbsp;&nbsp;  \lnot \beta \lor \gamma}{
  pha \lor \gamma}
\]

<u>Modus Ponens</u> (đối với dạng Horn): đầy đủ cho KB Horn
\[\frac{
  pha_1,\ldots,
  pha_n, &nbsp;&nbsp;&nbsp;&nbsp;  
  pha_1\land \cdots \land 
  pha_n\implies \beta}{\beta} 
\]
Có thể được sử dụng với <u>suy diễn tiến (forward chaining)</u> hoặc <u>suy diễn lùi (backward chaining)</u>

---
## Tóm tắt

Các tác tử logic áp dụng <u>suy diễn (inference)</u> vào <u>cơ sở tri thức (knowledge base)</u>
  
để rút ra thông tin mới và đưa ra quyết định

Các khái niệm cơ bản của logic:
  
-- <u>cú pháp (syntax)</u>: cấu trúc hình thức của <u>các câu</u>
  
-- <u>ngữ nghĩa (semantics)</u>: <u>chân lý</u> của các câu so với <u>mô hình</u>
  
-- <u>kéo theo (entailment)</u>: tính chân lý tất yếu của một câu khi cho trước một câu khác
  
-- <u>suy diễn (inference)</u>: dẫn xuất ra các câu từ các câu khác
  
-- <u>tính đúng đắn (soundness)</u>: các dẫn xuất chỉ tạo ra các câu kéo theo
  
-- <u>tính đầy đủ (completeness)</u>: các dẫn xuất có thể tạo ra tất cả các câu kéo theo

Thế giới wumpus đòi hỏi khả năng biểu diễn thông tin
từng phần và bị phủ định, lập luận theo các trường hợp, v.v.

Logic mệnh đề đủ cho một số nhiệm vụ này

Phương pháp bảng chân lý là đúng đắn và đầy đủ đối với logic mệnh đề