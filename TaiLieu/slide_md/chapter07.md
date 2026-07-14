\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Logic bậc một (First-order logic)

## Chương 7

---
## Nội dung

- Cú pháp và ngữ nghĩa của FOL

- Vui với các câu

- Thế giới Wumpus trong FOL

---
## Cú pháp của FOL: Các phần tử cơ bản

| &nbsp; | &nbsp; |
|---|---|
| Hằng số (Constants) | $KingJohn,\ 2,\ UCB,\ldots$ |
| Vị từ (Predicates) | $Brother,\ >,\ldots$ |
| Hàm số (Functions) | $Sqrt,\ LeftLegOf,\ldots$ |
| Biến (Variables) | $x,\ y,\ a,\ b,\ldots$ |
| Ký hiệu nối (Connectives) | $\land\ \lor\ \lnot\ \implies\ \lequiv$ |
| Bằng nhau (Equality) | $=$ |
| Lượng từ (Quantifiers) | $\forall\ \exists$ |

---
## Câu nguyên thủy (Atomic sentences)

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| Câu nguyên thủy | = | $predicate(term_1,\ldots,term_n)$ |
|  |  | hoặc $term_1 = term_2$ |
|  |  |  |
| Hạng thức (Term) | = | $function(term_1,\ldots,term_n)$ |
|  |  | hoặc $constant$ hoặc $variable$ |

| &nbsp; | &nbsp; |
|---|---|
| Ví dụ: | $Brother(KingJohn,RichardTheLionheart)$ |
|  | $>(Length(LeftLegOf(Richard)),Length(LeftLegOf(KingJohn)))$ |

---
## Câu phức hợp (Complex sentences)

Các câu phức hợp được tạo từ các câu nguyên thủy bằng cách sử dụng các ký hiệu nối
\[
\lnot S, &nbsp;&nbsp;  S_1\land S_2, &nbsp;&nbsp;  S_1 \lor S_2, &nbsp;&nbsp;  
S_1 \implies S_2, &nbsp;&nbsp;  S_1 \lequiv S_2
\]

| &nbsp; | &nbsp; |
|---|---|
| Ví dụ: | $Sibling(KingJohn,Richard) \implies Sibling(Richard,KingJohn)$ |
|  | ${>}(1,2) \lor {\leq}(1,2)$ |
|  | ${>}(1,2) \land \lnot {>}(1,2)$ |

---
## Tính chân lý trong logic bậc một

Các câu là đúng đối với một <u>mô hình (model)</u> và một <u>diễn dịch (interpretation)</u>

Mô hình chứa các đối tượng và các quan hệ giữa chúng

Diễn dịch chỉ định các vật sở chỉ (referents) cho
  
*các ký hiệu hằng* $\rightarrow$ <u>các đối tượng</u>
  
*các ký hiệu vị từ* $\rightarrow$ <u>các quan hệ</u>
  
*các ký hiệu hàm* $\rightarrow$ <u>các quan hệ hàm</u>

Một câu nguyên thủy $predicate(term_1,\ldots,term_n)$ là đúng

khi và chỉ khi các <u>đối tượng</u> được chỉ tới bởi $term_1,\ldots,term_n$

nằm trong <u>quan hệ</u> được chỉ tới bởi $predicate$

---
## Các mô hình cho FOL: Ví dụ

![Hình ảnh](../TaiLieu/slide_md/figures/fol-models.png)

---
## Lượng từ phổ dụng (Universal quantification)

$\All{\<variables\>} \<sentence\>$

Mọi người ở Berkeley đều thông minh:

$\All{x} At(x,Berkeley) \implies Smart(x)$

$\All{x} P$ &nbsp;&nbsp;  tương đương với <u>phép hội</u> của các <u>thực thể hóa (instantiations)</u> của $P$
\[
\begin{array}{rl}
     & At(KingJohn,Berkeley) \implies Smart(KingJohn) 

\land& At(Richard,Berkeley) \implies Smart(Richard) 

\land& At(Berkeley,Berkeley) \implies Smart(Berkeley) 

\land& \ldots
\end{array}\]
Thông thường, $\implies$ là ký hiệu nối chính với $\forall$.

Lỗi phổ biến: sử dụng $\land$ làm ký hiệu nối chính với $\forall$:
\[\All{x} At(x,Berkeley) \land Smart(x)\]
có nghĩa là "Tất cả mọi người đều ở Berkeley và tất cả mọi người đều thông minh"

---
## Lượng từ tồn tại (Existential quantification)

$\Exi{\<variables\>} \<sentence\>$

Một ai đó ở Stanford rất thông minh:

$\Exi{x} At(x,Stanford) \land Smart(x)$

$\Exi{x} P$ &nbsp;&nbsp;  tương đương với <u>phép tuyển</u> của các <u>thực thể hóa</u> của $P$
\[
\begin{array}{rl}
     & At(KingJohn,Stanford) \land Smart(KingJohn) 

\lor& At(Richard,Stanford) \land Smart(Richard) 

\lor& At(Stanford,Stanford) \land Smart(Stanford) 

\lor& \ldots
\end{array}\]
Thông thường, $\land$ là ký hiệu nối chính với $\exists$.

Lỗi phổ biến: sử dụng $\implies$ làm ký hiệu nối chính với $\exists$:
\[\Exi{x} At(x,Stanford) \implies Smart(x)\]
là đúng nếu có bất kỳ ai đó \textbf{không} ở Stanford!

---
## Đặc tính của các lượng từ

$\All{x}\All{y}$ giống với $\All{y}\All{x}$ (<u>tại sao?</u>??)

$\Exi{x}\Exi{y}$ giống với $\Exi{y}\Exi{x}$ (<u>tại sao?</u>??)

$\Exi{x}\All{y}$ <u>không</u> giống với $\All{y}\Exi{x}$

$\Exi{x}\All{y} Loves(x,y)$

"Có một người yêu thương mọi người trên thế giới"

$\All{y}\Exi{x} Loves(x,y)$

"Mọi người trên thế giới đều được ít nhất một người yêu thương"

<u>Tính đối ngẫu của lượng từ</u>: mỗi cái có thể được biểu diễn bằng cách sử dụng cái kia

$\All{x} Likes(x,IceCream)$  &nbsp;&nbsp;&nbsp;&nbsp;  $\lnot \Exi{x} \lnot Likes(x,IceCream)$ 

$\Exi{x} Likes(x,Broccoli)$  &nbsp;&nbsp;&nbsp;&nbsp;  $\lnot \All{x} \lnot Likes(x,Broccoli)$ 

---
## Vui với các câu

Anh em trai là anh em ruột (siblings)

.

"Anh em ruột" có tính phản xạ

.

Mẹ của một người là cha mẹ nữ của người đó

.

Anh em họ thứ nhất là con của anh em ruột của cha mẹ

.

---
## Vui với các câu

.

$\All{x,y} Brother(x,y) \lequiv Sibling(x,y)$.

.

$\All{x,y} Sibling(x,y) \lequiv Sibling(y,x)$

.

$\All{x,y} Mother(x,y) \lequiv (Female(x) \land Parent(x,y))$

.

$\All{x,y} FirstCousin(x,y) \lequiv 
\Exi{p,ps} Parent(p,x) \land Sibling(ps,p) \land Parent(ps,y)$

---
## Sự bằng nhau (Equality)

$term_1 = term_2$ là đúng dưới một diễn dịch đã cho

khi và chỉ khi $term_1$ và $term_2$ cùng chỉ một đối tượng

| &nbsp; | &nbsp; |
|---|---|
| Ví dụ: | $1=2$ và $\All{x} {\times}(Sqrt(x),Sqrt(x)) = x$ là thỏa mãn được |
|  | $2=2$ là hợp lệ |

Ví dụ: định nghĩa (đầy đủ) của $Sibling$ (anh em ruột) theo $Parent$ (cha mẹ):
  
$\All{x,y} Sibling(x,y) \lequiv [\lnot(x\eq y) \land \Exi{m,f} \lnot(m\eq f) \land {}$
    
$Parent(m,x) \land Parent(f,x) \land Parent(m,y) \land Parent(f,y)]$

---
## Tương tác với KB của FOL

Giả sử một tác tử thế giới wumpus đang sử dụng một KB của FOL

và nhận thấy một mùi và một luồng gió (nhưng không lấp lánh) tại $t=5$:

$**Tell**(KB,Percept([Smell,Breeze,None],5))$

$**Ask**(KB,\Exi{a} Action(a,5))$

Nghĩa là, liệu KB có kéo theo bất kỳ hành động cụ thể nào tại $t=5$ không?

Trả lời: $Có,\ \{a/Shoot\}$ &nbsp;&nbsp;&nbsp;&nbsp;  $\leftarrow$ <u>phép thế (substitution)</u> (danh sách ràng buộc)

Cho một câu $S$ và một phép thế $\sigma$,

$S\sigma$ biểu thị kết quả của việc áp dụng $\sigma$ vào $S$; ví dụ:

$S = Smarter(x,y)$

$\sigma = \{x/Hillary,y/Bill\}$

$S\sigma = Smarter(Hillary,Bill)$

$**Ask(KB,S)**$ trả về một số/tất cả $\sigma$ sao cho $KB \models S\sigma$

---
## Cơ sở tri thức cho thế giới wumpus

<u>"Nhận thức (Perception)"</u>

$\All{b,g,t} Percept([Smell,b,g],t) \implies Smelt(t)$

$\All{s,b,t} Percept([s,b,Glitter],t) \implies AtGold(t)$

<u>Phản xạ (Reflex)</u>: $\All{t} AtGold(t) \implies Action(Grab,t)$

<u>Phản xạ với trạng thái nội bộ (Reflex with internal state)</u>: chúng ta đã có vàng chưa?

$\All{t} AtGold(t) \land \lnot Holding(Gold,t) \implies Action(Grab,t)$

$Holding(Gold,t)$ không thể quan sát được
    
$\Rightarrow$ việc theo dõi sự thay đổi là cần thiết

---
## Suy diễn các thuộc tính ẩn

Các thuộc tính của vị trí:

$\All{l,t} At(Agent,l,t) \land Smelt(t) \implies Smelly(l)$

$\All{l,t} At(Agent,l,t) \land Breeze(t) \implies Breezy(l)$

Các ô gần hố thì có gió nhẹ:

<u>Quy tắc chẩn đoán (Diagnostic rule)</u>---suy diễn nguyên nhân từ kết quả
    
      $\All{y} Breezy(y) \implies \Exi{x} Pit(x) \land Adjacent(x,y)$

<u>Quy tắc nhân quả (Causal rule)</u>---suy diễn kết quả từ nguyên nhân
    
      $\All{x,y} Pit(x) \land Adjacent(x,y) \implies Breezy(y)$

Không có quy tắc nào trong số này là đầy đủ---ví dụ, quy tắc nhân quả không nói
rằng liệu các ô ở xa hố có gió nhẹ hay không

<u>Định nghĩa (Definition)</u> cho vị từ $Breezy$:
    
      $\All{y}  Breezy(y)  \lequiv [\Exi{x} Pit(x) \land Adjacent(x,y)]$

---
## Theo dõi sự thay đổi

Các sự kiện (Facts) diễn ra trong các <u>tình huống (situations)</u>, thay vì vĩnh viễn

Ví dụ, $Holding(Gold,Now)$ thay vì chỉ $Holding(Gold)$

<u>Phép tính tình huống (Situation calculus)</u> là một cách để biểu diễn sự thay đổi trong FOL:
    
   Thêm một đối số tình huống vào mỗi vị từ không vĩnh viễn
    
   Ví dụ, $Now$ trong $Holding(Gold,Now)$ biểu thị một tình huống

Các tình huống được kết nối bởi hàm $Result$

$Result(a,s)$ là tình huống sinh ra từ việc thực hiện $a$ trong $s$

![Hình ảnh](../TaiLieu/slide_md/figures/situations2.png)

---
## Mô tả các hành động I

Tiên đề "Kết quả (Effect)"---mô tả các thay đổi do hành động

$\All{s} AtGold(s) \implies Holding(Gold,Result(Grab,s))$

Tiên đề "Khung (Frame)"---mô tả <u>không thay đổi</u> do hành động

$\All{s} HaveArrow(s) \implies HaveArrow(Result(Grab,s))$

<u>Vấn đề khung (Frame problem)</u>: tìm một cách thanh lịch để xử lý sự không thay đổi
    
   (a) biểu diễn---tránh các tiên đề khung
    
   (b) suy diễn---tránh "sao chép qua (copy-overs)" liên tục để theo dõi trạng thái

<u>Vấn đề ngoại lệ (Qualification problem)</u>: mô tả đúng về các hành động thực tế đòi hỏi vô số các ngoại lệ---điều gì xảy ra nếu vàng bị trơn trượt hoặc bị đóng đinh hoặc $\ldots$

<u>Vấn đề hệ quả (Ramification problem)</u>: các hành động thực tế có nhiều hệ quả phụ---thế còn bụi trên vàng, hao mòn trên găng tay, $\ldots$

---
## Mô tả các hành động II

<u>Các tiên đề trạng thái kế tiếp (Successor-state axioms)</u> giải quyết vấn đề khung biểu diễn

Mỗi tiên đề nói "về" một <u>vị từ</u> (không phải bản thân một hành động):
\begin{eqnarray*}
\mbox{P đúng sau đó}&\lequiv& [\mbox{một hành động làm P đúng}

                      &\lor   & \mbox{P đã đúng và không có hành động nào
                                  làm P sai}]
\end{eqnarray*}

Để cầm được vàng:
  
   $\All{a,s} Holding(Gold,Result(a,s)) \lequiv {}$
    
      $[(a\eq Grab \land AtGold(s))$
    
      ${}\lor (Holding(Gold,s) \land a\neq Release)]$

---
## Lập kế hoạch

Điều kiện ban đầu trong KB:
    
   $At(Agent,[1,1],S_0)$
    
   $At(Gold,[1,2],S_0)$

Truy vấn: $**Ask**(KB,\Exi{s} Holding(Gold,s))$
    
   nghĩa là, trong tình huống nào tôi sẽ cầm vàng?

Trả lời: $\{s/Result(Grab,Result(Forward,S_0))\}$
    
   nghĩa là, đi tới và sau đó nhặt vàng

Điều này giả định rằng tác tử quan tâm đến các kế hoạch bắt đầu tại $S_0$
và rằng $S_0$ là tình huống duy nhất được mô tả trong KB

---
## Lập kế hoạch: Một cách tốt hơn

Biểu diễn <u>các kế hoạch (plans)</u> dưới dạng các chuỗi hành động $[a_1,a_2,\ldots,a_n]$

$PlanResult(p,s)$ là kết quả của việc thực thi $p$ trong $s$

Sau đó truy vấn $**Ask**(KB,\Exi{p} Holding(Gold,PlanResult(p,S_0)))$

có giải pháp là $\{p/[Forward,Grab]\}$

Định nghĩa của $PlanResult$ theo $Result$:
  
   $\All{s} PlanResult([],s) = s$
  
   $\All{a,p,s} PlanResult([a|p],s) = PlanResult(p,Result(a,s))$

<u>Hệ thống lập kế hoạch (Planning systems)</u> là các công cụ suy diễn có mục đích đặc biệt được thiết kế để thực hiện
loại suy diễn này hiệu quả hơn công cụ suy diễn mục đích chung

---
## Tóm tắt

Logic bậc một: 
  
-- các đối tượng và quan hệ là các nguyên thủy ngữ nghĩa
  
-- cú pháp: hằng số, hàm số, vị từ, bằng nhau, lượng từ

Tăng sức mạnh biểu đạt: đủ để định nghĩa thế giới wumpus

Phép tính tình huống:
  
-- các quy ước để mô tả các hành động và thay đổi trong FOL
  
-- có thể diễn đạt việc lập kế hoạch như sự suy diễn trên một KB phép tính tình huống