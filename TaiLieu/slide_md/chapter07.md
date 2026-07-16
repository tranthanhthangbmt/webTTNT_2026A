\usepackage{fleqn}
\usepackage{epsf}
\usepackage{color}
\usepackage{aima2e-slides}

# Tác tử logic (Logical agents)

## Chương 7

---
## Phác thảo

- Tác nhân dựa trên tri thức

- Thế giới Wumpus

- Logic nói chung---mô hình và sự kế thừa

- Logic mệnh đề (Boolean)

- Tính tương đương, giá trị, sự thỏa mãn

- Quy tắc suy luận và chứng minh định lý
    
 -- xâu chuỗi về phía trước 
    
 -- xâu chuỗi ngược
    
 -- độ phân giải

---
## Cơ sở kiến thức

![Hình ảnh](../TaiLieu/slide_md/figures/kbs.png)

\defn{Cơ sở kiến thức} = tập hợp \defn{câu} trong ngôn ngữ *trang trọng*

\defn{Cách tiếp cận khai báo} để xây dựng tác nhân (hoặc hệ thống khác):
    
   \defprog{Nói cho nó biết điều nó cần biết

Sau đó, nó có thể tự \defprog{Hỏi} phải làm gì---các câu trả lời sẽ được đưa ra từ KB

Đại lý có thể được xem ở cấp độ kiến ​​thức \defn{} 
    
   tức là, *những gì họ biết*, bất kể được triển khai như thế nào

Hoặc ở cấp độ triển khai \defn{}
    
   tức là cấu trúc dữ liệu trong KB và các thuật toán thao tác chúng

---
## Một tác nhân dựa trên kiến thức đơn giản

```text
function KB-Agent(percept) returns an action
      static: KB, a knowledge base
      static: t, a counter, initially 0, indicating time

    Tell(KB, Make-Percept-Sentence(percept, t))
    action <- Ask(KB, Make-Action-Query(t))
    Tell(KB, Make-Action-Sentence(action, t))
    t <- t + 1
    return action
```

Đại lý phải có khả năng:
  
Đại diện cho các trạng thái, hành động, v.v.
  
Kết hợp các nhận thức mới
  
Cập nhật các biểu diễn nội bộ của thế giới
  
Suy ra những thuộc tính ẩn giấu của thế giới
  
Suy ra những hành động phù hợp

---
## Mô tả Wumpus World PEAS

\note{Thước đo hiệu suất} 
  
  vàng +1000, chết -1000
  
  -1 mỗi bước, -10 khi sử dụng mũi tên

\note{Môi trường}
  
Các ô vuông cạnh wumpus có mùi hôi
  
Ô vuông cạnh hố thoáng mát
  
Vàng lấp lánh nằm trong cùng một ô vuông
  
Bắn giết wumpus nếu bạn đang đối mặt với nó
  
Việc bắn súng sử dụng hết mũi tên duy nhất
  
Nắm lấy vàng nếu ở cùng một ô vuông
  
Thả vàng rơi vào cùng một ô vuông

 

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-world.png)

\note{Thiết bị truyền động} Rẽ trái, Rẽ phải,
    
    Tiến, nắm, thả, bắn

\note{Cảm biến} Gió, Long lanh, Mùi

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? 

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? Không---chỉ nhận thức \note{cục bộ}

<u>Xác định</u>?? 

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? Không---chỉ nhận thức \note{cục bộ}

<u>Xác định</u>?? Có---kết quả được chỉ định chính xác

<u>Tập </u>?? 

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? Không---chỉ nhận thức \note{cục bộ}

<u>Xác định</u>?? Có---kết quả được chỉ định chính xác

<u>Theo từng tập</u>?? Không---tuần tự ở cấp độ hành động

<u>Tĩnh</u>??  

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? Không---chỉ nhận thức \note{cục bộ}

<u>Xác định</u>?? Có---kết quả được chỉ định chính xác

<u>Theo từng tập</u>?? Không---tuần tự ở cấp độ hành động

<u>Tĩnh</u>?? Có---Wumpus và Pits không di chuyển

<u>Rời rạc</u>?? 

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? Không---chỉ nhận thức \note{cục bộ}

<u>Xác định</u>?? Có---kết quả được chỉ định chính xác

<u>Theo từng tập</u>?? Không---tuần tự ở cấp độ hành động

<u>Tĩnh</u>?? Có---Wumpus và Pits không di chuyển

<u>Rời rạc</u>?? Có

<u>Đại lý đơn lẻ</u>?? 

---
## Đặc điểm thế giới Wumpus

<u>Có thể quan sát được</u>?? Không---chỉ nhận thức \note{cục bộ}

<u>Xác định</u>?? Có---kết quả được chỉ định chính xác

<u>Theo từng tập</u>?? Không---tuần tự ở cấp độ hành động

<u>Tĩnh</u>?? Có---Wumpus và Pits không di chuyển

<u>Rời rạc</u>?? Có

<u>Single-agent</u>?? Có---Wumpus về cơ bản là một tính năng tự nhiên

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq0.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq1.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq2.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq3.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq4.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq5.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq6.png)

---
## Khám phá thế giới wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq7.png)

---
## Các điểm chật khác

in
\raisebox{-0.5in}[2.5in]{![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-bb.png)}
 

Gió vào (1,2) và (2,1)
  
$\implies$ không có hành động an toàn

Giả sử các hố phân bố đồng đều,

(2,2) có điểm thấp với thăm dò 0,86, so với   0,31

     

in
![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-s.png)
 

Mùi trong (1,1) 
  
$\implies$ không thể di chuyển

Có thể sử dụng chiến lược \defn{ép buộc}:
  
  bắn thẳng về phía trước
  
  wumpus đã ở đó $\implies$ đã chết $\implies$ an toàn 
  
  wumpus không có ở đó $\implies$ an toàn
  

---
## Logic nói chung

\defn{Logic} là ngôn ngữ hình thức để biểu diễn thông tin
  
   để có thể rút ra kết luận

\defn{Cú pháp} xác định các câu trong ngôn ngữ

\defn{Ngữ nghĩa} xác định "ý nghĩa" của câu;
  
   tức là xác định \defn{sự thật} của một câu trong một thế giới

Ví dụ, ngôn ngữ của số học

\mat{$x+2 \geq y$} là một câu; \mat{$x2+y>{}$} không phải là một câu

\mat{$x+2 \geq y$} đúng nếu số \mat{$x+2$} không nhỏ hơn
hơn số \mat{$y$}

\mat{$x+2 \geq y$} đúng trong một thế giới nơi \mat{$x\eq 7,\ y\eq 1$}

\mat{$x+2 \geq y$} là sai trong một thế giới nơi \mat{$x\eq 0,\ y\eq 6$}

---
## Yêu cầu

\defn{Entailment} có nghĩa là một thứ *tiếp nối từ* một thứ khác:
\mat{\[KB \models 
  pha\]}

Cơ sở tri thức \mat{$KB$} bao gồm câu \mat{$
  pha$}
    
   nếu và chỉ khi

\mat{$
  pha$} đúng ở mọi thế giới nơi \mat{$KB$} đúng

Ví dụ: KB chứa " the Giants won " và " The Reds won "

đòi hỏi "Hoặc Người khổng lồ thắng hoặc Quỷ đỏ thắng"

Ví dụ: \mat{$x+y\eq 4$} đòi hỏi \mat{$4\eq x+y$}

Yêu cầu là mối quan hệ giữa các câu (tức là *cú pháp*)

dựa trên *ngữ nghĩa*

Lưu ý: bộ não xử lý cú pháp *cú pháp * (thuộc loại nào đó)

---
## Mẫu 

Các nhà logic học thường nghĩ theo các mô hình \defn{}, chính thức là 

thế giới có cấu trúc mà sự thật có thể được đánh giá

Ta nói \mat{$m$} \note{ là mô hình của } một câu \mat{$
  pha$}
nếu \mat{$
  pha$} đúng trong \mat{$m$}

\mat{$M(
  pha)$} là tập hợp tất cả các model của \mat{$
  pha$}

Khi đó \mat{$KB \models 
  pha$} khi và chỉ khi \mat{$M(KB) \subseteq M(
  pha)$}

Ví dụ: \mat{$KB$} = Người khổng lồ thắng và Quỷ đỏ thắng
    
     \mat{$
  pha$} = Người khổng lồ đã thắng

 
in
\raisebox{-2in}[0in]{![Hình ảnh](../TaiLieu/slide_md/figures/model-inclusion.png)}

---
## Sự đòi hỏi trong thế giới wumpus

Tình huống sau khi không phát hiện được gì trong [1,1],

di chuyển sang phải, gió thổi vào [2,1] 

Xem xét các mô hình có thể có cho ?s

giả sử chỉ có hố 

 

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq1c-alt.png)

3 lựa chọn Boolean $\implies$ 8 mô hình có thể

---
## Mẫu Wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-models1.png)

---
## Mẫu Wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-models2.png)

\mat{$KB$} = quy tắc của thế giới wumpus + quan sát

---
## Mẫu Wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-models3.png)

\mat{$KB$} = quy tắc của thế giới wumpus + quan sát

\mat{$
  pha_1$} = "[1,2] là an toàn", \mat{$KB \models 
  pha_1$}, được chứng minh bằng \defn{kiểm tra mô hình}

---
## Mẫu Wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-models2.png)

\mat{$KB$} = quy tắc của thế giới wumpus + quan sát

---
## Mẫu Wumpus

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-models4.png)

\mat{$KB$} = quy tắc của thế giới wumpus + quan sát

\mat{$
  pha_2$} = "[2,2] an toàn", \mat{$KB  \not\models 
  pha_2$}

---
## Suy luận

\mat{$KB\vdash_i
  pha$} = câu \mat{$
  pha$} có thể được suy ra từ \mat{$KB$} bằng thủ tục \mat{$i$}

Hậu quả của \mat{$KB$} là đống cỏ khô; \mat{$
  pha$} là một cây kim.

Đòi hỏi = kim đáy bể; suy luận = tìm ra nó

\defn{Âm thanh}: \mat{$i$} là âm thanh nếu
    
bất cứ khi nào \mat{$KB\vdash_i
  pha$}, thì cũng đúng là \mat{$KB\models
  pha$}

\defn{Tính đầy đủ}: \mat{$i$} hoàn tất nếu
    
bất cứ khi nào \mat{$KB\models
  pha$}, thì cũng đúng là \mat{$KB\vdash_i
  pha$}

Xem trước: chúng ta sẽ định nghĩa một logic (logic bậc nhất)
đủ biểu cảm để nói lên hầu hết mọi điều đáng quan tâm, và để làm được điều đó
tồn tại một thủ tục suy luận hợp lý và đầy đủ.

Nghĩa là, quy trình sẽ trả lời bất kỳ câu hỏi nào có câu trả lời sau
từ những gì được biết bởi \mat{$KB$}.

---
## Logic mệnh đề: Cú pháp

Logic mệnh đề là logic đơn giản nhất---minh họa những ý tưởng cơ bản

Các ký hiệu mệnh đề \mat{$P_1$}, \mat{$P_2$} v.v. là các câu

Nếu \mat{$S$} là một câu thì \mat{$\lnot S$} là một câu (\defn{phủ định})

Nếu \mat{$S_1$} và \mat{$S_2$} là câu thì \mat{$S_1 \land S_2$} là một câu (\defn{liên từ})
 
Nếu \mat{$S_1$} và \mat{$S_2$} là câu thì \mat{$S_1 \lor S_2$} là câu (\defn{phân cách})

Nếu \mat{$S_1$} và \mat{$S_2$} là câu thì \mat{$S_1 \implies S_2$} là một câu (\defn{ngụ ý})

Nếu \mat{$S_1$} và \mat{$S_2$} là câu thì \mat{$S_1 \lequiv S_2$} là câu (\defn{hai điều kiện})

---
## Logic mệnh đề: Ngữ nghĩa

Mỗi mô hình chỉ định đúng/sai cho từng ký hiệu mệnh đề

| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|
| Ví dụ: | \mat{$P_{1,2}$} | \mat{$P_{2,2}$} | \mat{$P_{3,1}$} |
|  | \mat{$true$} | \mat{$true$} | \mat{$false$} |

(Với những ký hiệu này, 8 mẫu có thể được liệt kê tự động.)

Quy tắc đánh giá sự thật đối với một mô hình \mat{$m$}:

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|
| \mat{$\lnot S$} | đúng iff | \mat{$S$} | sai |  |  |
| \mat{$S_1 \land S_2$} | là đúng iff | \mat{$S_1$} | là đúng *và* | \mat{$S_2$} | là đúng |
| \mat{$S_1 \lor S_2$} | là đúng iff | \mat{$S_1$} | là đúng * hoặc * | \mat{$S_2$} | là đúng |
| \mat{$S_1 \implies S_2$} | là đúng iff | \mat{$S_1$} | là sai * hoặc * | \mat{$S_2$} | là đúng |
|  &nbsp;&nbsp;&nbsp;&nbsp;  tức là | sai iff | \mat{$S_1$} | đúng * và * | \mat{$S_2$} | là sai |
| \mat{$S_1 \lequiv S_2$} | là đúng iff | \mat{$S_1\implies S_2$} | là đúng * và * | \mat{$S_2\implies S_1$} | là đúng |

Quá trình đệ quy đơn giản đánh giá một câu tùy ý, ví dụ:

\mat{$\lnot P_{1,2}\land (P_{2,2}\lor P_{3,1})$} = \mat{$true\land (false \lor true)\eq true\land
true \eq true$}

---
## Bảng chân lý cho liên từ

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|---|
| \(P\) | \(Q\) | \(\lnot P\) | \(P \land Q\) | \(P \lor Q\) | \(P {\Rightarrow} Q\) | \(P {\Leftrightarrow} Q\) |
| \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} |
| \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} |
| \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} |
| \txr{\(\J{true}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} |

 

---
## Câu thế giới Wumpus

Giả sử \mat{$P_{i,j}$} là đúng nếu có một hố trong \mat{$[i,j]$}.

Giả sử \mat{$B_{i,j}$} là đúng nếu có gió trong \mat{$[i,j]$}.
\mat{\begin{eqnarray*}
 \lnot P_{1,1}

 \lnot B_{1,1}

 B_{2,1}
\end{eqnarray*}}
"Hố gây gió ở ô liền kề"

---
## Câu thế giới Wumpus

Giả sử \mat{$P_{i,j}$} là đúng nếu có một hố trong \mat{$[i,j]$}.

Giả sử \mat{$B_{i,j}$} là đúng nếu có gió trong \mat{$[i,j]$}.
\mat{\begin{eqnarray*}
 \lnot P_{1,1}

 \lnot B_{1,1}

 B_{2,1}
\end{eqnarray*}}
"Hố gây gió ở ô liền kề"
\mat{\begin{eqnarray*}
 B_{1,1} &\lequiv& (P_{1,2} \lor P_{2,1})

 B_{2,1} &\lequiv& (P_{1,1} \lor P_{2,2}\lor P_{3,1})
\end{eqnarray*}}
"Một hình vuông sẽ mát mẻ *nếu và chỉ khi* có một cái hố liền kề"

---
## Bảng chân lý cho suy luận

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| \(B_{1,1}\) | \(B_{2,1}\) | \(P_{1,1}\) | \(P_{1,2}\) | \(P_{2,1}\) | \(P_{2,2}\) | \(P_{3,1}\) | \(R_{1}\) | \(R_{2}\) | \(R_{3}\) | \(R_{4}\) | \(R_{5}\) | \(\J{KB}\) |
| \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) | \(\J{false}\) |
| \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) | \(\J{true}\) | \(\J{false}\) | \(\J{false}\) |
| \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) |
| \(\J{false}\) | \(\J{true}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{false}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) |
| \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \mat{\(\underline{\J{true}}\)} |
| \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \mat{\(\underline{\J{true}}\)} |
| \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txg{\(\J{false}\)} | \txr{\(\J{true}\)} | \txr{\(\J{true}\)} | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \mat{\(\underline{\J{true}}\)} |
| \(\J{false}\) | \(\J{true}\) | \(\J{false}\) | \(\J{false}\) | \(\J{true}\) | \(\J{false}\) | \(\J{false}\) | \(\J{true}\) | \(\J{false}\) | \(\J{false}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) |
| \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) | \(\vdots\) |
| \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) | \(\J{true}\) | \(\J{true}\) | \(\J{false}\) | \(\J{true}\) | \(\J{false}\) |

Liệt kê các hàng (các phép gán khác nhau cho các ký hiệu),

nếu \mat{KB} đúng trong hàng, hãy kiểm tra xem \mat{$
  pha$} có đúng không

---
## Suy luận bằng phép liệt kê

Việc liệt kê theo chiều sâu của tất cả các mô hình là hợp lý và đầy đủ 

```text
function TT-Entails?(\v{KB), \(
  pha\)}{\v{true} or \v{false}}
    \firstinputs{\v{KB}}{the knowledge base, a sentence in propositional logic}
      inputs: \(
  pha\), the query, a sentence in propositional logic

    \v{symbols}{a list of the proposition symbols in \v{KB} and \(
  pha\)}
    \k{return} TT-Check-All(\v{KB}, \(
  pha\), \v{symbols}, \([, ]\))
\fnsep
function TT-Check-All(\v{KB), \(
  pha\), \v{symbols}, \v{model}}{\v{true} or \v{false}}
    \k{if} Empty?(\v{symbols}) \k{then}
          \k{if} PL-True?(\v{KB}, \v{model}) \k{then return} PL-True?(\(
  pha\), \v{model})
          \k{else return} \v{true}
    \k{else do}
          \(P\) <- First(\v{symbols)}; \v{rest}{Rest(\v{symbols})}
          \k{return} TT-Check-All(\v{KB}, \(
  pha\), \v{rest}, Extend(\(P, \v{true}, \v{model}\))) \k{and}
                       TT-Check-All(\v{KB}, \(
  pha\), \v{rest}, Extend(\(P, \v{false}, \v{model}\)))
```

\mat{$O(2^n)$} cho ký hiệu \mat{$n$}; vấn đề là *co-NP-complete*

---
## Tương đương logic

Hai câu \defn{tương đương về mặt logic} nếu đúng trong cùng một mô hình:
  
\mat{$
  pha\equiv\beta$} khi và chỉ khi \mat{$
  pha\models\beta$} 
và \mat{$\beta\models
  pha$}

\FigBox{
\[\begin{array}{rcll}
(
  pha\land \beta) &\equiv& (\beta\land 
  pha)  &nbsp;&nbsp; \mbox{commutativity of }\land

(
  pha\lor \beta) &\equiv& (\beta\lor 
  pha)  &nbsp;&nbsp; \mbox{commutativity of }\lor

((
  pha\land \beta)\land \gamma) &\equiv& (
  pha\land (\beta\land \gamma))   &nbsp;&nbsp; \mbox{associativity of }\land

((
  pha\lor \beta)\lor \gamma) &\equiv& (
  pha\lor (\beta\lor \gamma))   &nbsp;&nbsp; \mbox{associativity of }\lor

\lnot(\lnot 
  pha) &\equiv& 
  pha  &nbsp;&nbsp; \mbox{double-negation elimination}

(
  pha\implies \beta) &\equiv& (\lnot \beta \implies \lnot 
  pha)  &nbsp;&nbsp; \mbox{contraposition}

(
  pha\implies \beta) &\equiv& (\lnot 
  pha \lor \beta)  &nbsp;&nbsp; \mbox{implication elimination}

(
  pha\lequiv \beta) &\equiv& ((
  pha\implies \beta)\land (\beta\implies 
  pha))  &nbsp;&nbsp; \mbox{biconditional elimination}

\lnot(
  pha\land \beta) &\equiv& (\lnot 
  pha \lor \lnot \beta)  &nbsp;&nbsp; \mbox{De Morgan}

\lnot(
  pha\lor \beta) &\equiv& (\lnot 
  pha \land \lnot \beta)  &nbsp;&nbsp; \mbox{De Morgan}

(
  pha\land (\beta\lor \gamma)) &\equiv& ((
  pha\land \beta)\lor (
  pha\land \gamma)) &nbsp;&nbsp; \mbox{distributivity of }\land\mbox{ over }\lor

(
  pha\lor (\beta\land \gamma)) &\equiv& ((
  pha\lor \beta)\land (
  pha\lor \gamma))  &nbsp;&nbsp; \mbox{distributivity of }\lor\mbox{ over }\land
\end{array}
\]}

---
## Tính hợp lệ và sự thỏa mãn

Một câu là \defn{valid} nếu nó đúng trong các mô hình *all*,
    
ví dụ: \mat{$True$}, &nbsp;&nbsp;  \mat{$A \lor \lnot A$},  &nbsp;&nbsp;  \mat{$A \implies A$},  &nbsp;&nbsp;  
      \mat{$(A \land (A \implies B)) \implies B$}

Hiệu lực được kết nối với suy luận thông qua \defn{Định lý suy diễn}:
    
      \mat{$KB \models 
  pha$} khi và chỉ khi \mat{$(KB \implies 
  pha)$} hợp lệ

Một câu là \defn{satisfiable} nếu nó đúng trong *some* model
    
ví dụ: \mat{$A\lor B$}, &nbsp;&nbsp;&nbsp;&nbsp;  \mat{$C$}

Một câu là \defn{unsatisfiable} nếu nó đúng trong *no* models
    
ví dụ: \mat{$A\land \lnot A$}

Sự thỏa mãn được kết nối với suy luận thông qua:
    
      \mat{$KB \models 
  pha$} khi và chỉ nếu \mat{$(KB \land \lnot 
  pha)$} không thỏa mãn

tức là chứng minh \mat{$
  pha$} bằng \note{{\it reductio ad vô lý}

---
## Phương pháp chứng minh

Các phương pháp chứng minh chia thành (đại khái) hai loại:
  

\note{Ứng dụng quy tắc suy luận}
  
    -- Tạo câu mới (âm thanh) hợp pháp từ câu cũ
  
    -- \defn{Proof} = một chuỗi các ứng dụng quy tắc suy luận
    
       Có thể sử dụng các quy tắc suy luận làm toán tử trong một thuật toán tìm kiếm tiêu chuẩn.
  
    -- Thông thường yêu cầu dịch câu sang dạng \defn{dạng thông thường}

\note{Kiểm tra mô hình}
  
    liệt kê bảng chân lý (luôn theo cấp số nhân trong \mat{$n$})
  
    việc quay lui được cải tiến, ví dụ: Davis--Putnam--Logemann--Loveland
  
    tìm kiếm heuristic trong không gian mô hình (âm thanh nhưng không đầy đủ)
    
       ví dụ: thuật toán leo đồi giống như xung đột tối thiểu

---
## Xích tiến và lùi

\defn{Dạng sừng} (bị hạn chế)
    
    KB = *liên từ* của *Mệnh đề Horn*
  
    Mệnh đề Horn = 
    
     - ký hiệu mệnh đề;  hoặc 
    
     - (kết hợp các ký hiệu) \mat{$\implies$} ký hiệu
  
    Ví dụ: \mat{$C \land (B \implies A) \land (C \land D \implies B)$}

\defn{Modus Ponens} (dành cho dạng Horn): hoàn thành cho KB Horn
\mat{\[\frac{
  pha_1,\ldots,
  pha_n, &nbsp;&nbsp;&nbsp;&nbsp;  
  pha_1\land \cdots \land 
  pha_n\implies \beta}{\beta} 
\]}
Có thể được sử dụng với \defn{xâu chuỗi thuận} hoặc \defn{xâu chuỗi lùi}.

Các thuật toán này rất tự nhiên và chạy trong thời gian *tuyến tính*

---
## Chuyển tiếp 

Ý tưởng: kích hoạt bất kỳ quy tắc nào có tiền đề được thỏa mãn trong \mat{$KB$},
    
   thêm kết luận của nó vào \mat{$KB$}, cho đến khi tìm thấy truy vấn

 
\tab\tab\tab\tab\tab\tab$P\implies Q$
[4pt]
\tab\tab\tab\tab\tab\tab$L\land M \implies P$
[4pt]
\tab\tab\tab\tab\tab\tab$B \land L \implies M$
[4pt]
\tab\tab\tab\tab\tab\tab$A \land P\implies L$
[4pt]
\tab\tab\tab\tab\tab\tab$A \land B\implies L$
[4pt]
\tab\tab\tab\tab\tab\tab$A$
[4pt]
\tab\tab\tab\tab\tab\tab$B$

 ![Hình ảnh](../TaiLieu/slide_md/figures/pl-horn-example.png) 

---
## Thuật toán chuỗi chuyển tiếp

```text
function PL-FC-Entails?(\v{KB), \v{q}}{\v{true} or \v{false}}
    \firstinputs{\v{KB}}{the knowledge base, a set of propositional Horn clauses}
    \inputs{\v{q}}{the query, a proposition symbol}
    \firstlocal{\v{count}}{a table, indexed by clause, initially the number of premises}
    \local{\v{inferred}}{a table, indexed by symbol, each entry initially \v{false}}
    \local{\v{agenda}}{a list of symbols, initially the symbols known in \v{KB}}

    \k{while} \v{agenda} is not empty \k{do}
          \v{p}{Pop(\v{agenda})}
          \k{unless} \v{inferred}[\v{p}] \k{do}
                \v{inferred[\v{p}]}{\v{true}}
                \k{for each} Horn clause \v{c} in whose premise \v{p} appears \k{do}
                      decrement \v{count}[\v{c}]
                      \k{if} \v{count}[\v{c}] = 0 \k{then do} 
                            \k{if} Head[\v{c}] = \v{q} \k{then return} \v{true}
                            Push(Head[\v{c}], \v{agenda})
    \k{return} \v{false}
```

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example01c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example02c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example03c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example04c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example05c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example06c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example07c.png)

---
##  Ví dụ về chuỗi chuyển tiếp 

![Hình ảnh](../TaiLieu/slide_md/figures/fc-horn-example08c.png)

---
## Bằng chứng về tính đầy đủ

FC rút ra mọi câu nguyên tử được yêu cầu bởi \mat{$KB$}

1. FC đạt đến \defn{điểm cố định} nơi không có câu nguyên tử mới nào được dẫn xuất

2. Xem trạng thái cuối cùng dưới dạng mô hình \mat{$m$}, gán đúng/sai cho các ký hiệu

3. Mọi mệnh đề trong bản gốc \mat{$KB$} đều đúng trong \mat{$m$}
  
   *Bằng chứng*: Giả sử mệnh đề \mat{$a_1\land\ldots\land a_k\textimplies b$} sai trong \mat{$m$}
  
   Khi đó \mat{$a_1\land\ldots\land a_k$} đúng trong \mat{$m$} và \mat{$b$} sai trong \mat{$m$}
  
   Do đó thuật toán chưa đạt đến điểm cố định!

4. Do đó \mat{$m$} là mô hình của \mat{$KB$}

5. Nếu \mat{$KB\models q$}, \mat{$q$} đúng trong *mọi mẫu * của \mat{$KB$}, bao gồm \mat{$m$}

\note{Ý tưởng chung}: xây dựng bất kỳ mô hình nào của \mat{$KB$} bằng suy luận âm thanh, kiểm tra \mat{$
  pha$}

---
## Xích ngược

Ý tưởng: làm ngược lại từ truy vấn \mat{$q$}:
  
   để chứng minh \mat{$q$} bởi BC,
    
      kiểm tra xem \mat{$q$} đã được biết chưa, hoặc 
    
      chứng minh bằng BC tất cả các tiền đề của một số quy tắc kết luận \mat{$q$}

Tránh vòng lặp: kiểm tra xem mục tiêu phụ mới đã có trong ngăn xếp mục tiêu chưa

Tránh làm việc lặp lại: kiểm tra xem mục tiêu phụ mới 
  
  1) đã được chứng minh là đúng, hoặc
  
  2) đã thất bại

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example01c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example02c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example03c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example04c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example03c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example05c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example06c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example07c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example08c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example09c.png)

---
## Ví dụ về chuỗi ngược

![Hình ảnh](../TaiLieu/slide_md/figures/bc-horn-example10c.png)

---
## Xâu chuỗi tiến và  lùi 

FC là \defn{dựa trên dữ liệu}, cf. xử lý tự động, vô thức,
    
ví dụ: nhận dạng đối tượng, các quyết định thông thường

Có thể làm nhiều việc không liên quan đến mục tiêu

BC là \defn{định hướng theo mục tiêu}, thích hợp để giải quyết vấn đề,
    
ví dụ: Chìa khóa của tôi đâu? Làm thế nào để tôi vào được chương trình tiến sĩ?

Độ phức tạp của BC có thể *nhỏ hơn nhiều* so với kích thước tuyến tính của KB

---
## Độ phân giải

\defn{Dạng liên hợp thông thường} (CNF---phổ thông)
    
    *liên hợp* của $\underbrace{\mbox{*disjunctions* of *literals*}}$
    
    \phantom{*liên từ* của *disjuncti**mệnh đề*
    
    Ví dụ: \mat{$(A \lor \lnot B) \land (B \lor \lnot C \lor \lnot D)$}

\defn{Quy tắc suy luận Độ phân giải} (dành cho CNF): hoàn thành cho logic mệnh đề
\mat{\[\frac {\ell_1 \lor \cdots\lor \ell_k, &nbsp;&nbsp;&nbsp;&nbsp;  m_1 \lor \cdots\lor m_n}
        {\ell_1 \lor \cdots\lor \ell_{i-1}\lor \ell_{i+1}\lor\cdots\lor \ell_k
        \lor m_1 \lor \cdots \lor m_{j-1}\lor m_{j+1}\lor\cdots\lor m_n}
\]}
trong đó \mat{$\ell_i$} và \mat{$m_j$} là các chữ bổ sung. Ví dụ:in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-seq5c.png)}
\mat{\[
   \frac{P_{1,3} \lor P_{2,2}, &nbsp;&nbsp;&nbsp;&nbsp; \lnot P_{2,2}}
       {P_{1,3}}
\]}
Độ phân giải hợp lý và đầy đủ cho logic mệnh đề

---
## Chuyển đổi sang CNF

\mat{$B_{1,1} \textlequiv (P_{1,2} \lor P_{2,1})$}

1. Loại bỏ \mat{$\lequivsymbol$}, thay thế \mat{$
  pha\textlequiv \beta$} bằng \mat{$(
  pha\implies
\beta)\land (\beta\implies 
  pha)$}.
\mat{\[
   (B_{1,1} \implies (P_{1,2} \lor P_{2,1})) \land 
   ((P_{1,2} \lor P_{2,1})\implies B_{1,1})
\]}
2. Loại bỏ \mat{$\impliessymbol$}, thay thế \mat{$
  pha\textimplies \beta$} bằng \mat{$\lnot

  pha\lor \beta$}.
\mat{\[
   (\lnot B_{1,1} \lor P_{1,2} \lor P_{2,1}) \land 
   (\lnot(P_{1,2} \lor P_{2,1})\lor B_{1,1})
\]}
3. Di chuyển \mat{$\lnot$} vào trong bằng cách sử dụng quy tắc de Morgan và phủ định kép:
\mat{\[
   (\lnot B_{1,1} \lor P_{1,2} \lor P_{2,1}) \land 
   ((\lnot P_{1,2} \land \lnot P_{2,1})\lor B_{1,1})
\]}
4. Áp dụng luật phân phối (\mat{${\lor}$} trên \mat{${\land}$}) và làm phẳng:
\mat{\[
   (\lnot B_{1,1} \lor P_{1,2} \lor P_{2,1}) \land 
   (\lnot P_{1,2} \lor B_{1,1}) \land (\lnot P_{2,1} \lor B_{1,1})
\]}

---
## Thuật toán độ phân giải

Chứng minh bằng phản chứng, tức là chỉ ra \mat{$KB\land\lnot
  pha$} không thỏa mãn

```text
function PL-Resolution(\v{KB), \(
  pha\)}{\v{true} or \v{false}}
    \firstinputs{\v{KB}}{the knowledge base, a sentence in propositional logic}
      inputs: \(
  pha\), the query, a sentence in propositional logic

    \v{clauses}{the set of clauses in the CNF representation of \(\v{KB}\land\lnot
  pha\)}
    \v{new}{\(\{, \}\)}
    \k{loop do}
          \k{for each} \(C_i\), \(C_j\) \k{in} \v{clauses} \k{do}
                \v{resolvents}{PL-Resolve(\(C_i\), \(C_j\))}
                \k{if} \v{resolvents} contains the empty clause \k{then return} \v{true}
                \v{new}{\(\v{new}\union \v{resolvents}\)}
          \k{if} \(\v{new}\subseteq\v{clauses}\) \k{then return} \v{false}
          \v{clauses}{\(\v{clauses}\union\v{new}\)}
```

---
## Ví dụ về độ phân giải

\mat{$KB = (B_{1,1} \lequiv (P_{1,2} \lor P_{2,1})) \land \lnot B_{1,1}$}
\mat{$
  pha = \lnot P_{1,2}$}

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-resolution.png)

---
## Tóm tắt

Các tác nhân logic áp dụng \defn{suy luận} cho cơ sở tri thức \defn{}
  
để thu thập thông tin mới và đưa ra quyết định

Các khái niệm cơ bản về logic:
  
-- \defn{cú pháp}: cấu trúc hình thức của \defn{câu}
  
-- \defn{ngữ nghĩa}: \defn{sự thật} của câu wrt \defn{models}
  
-- \defn{đòi hỏi}: sự thật cần thiết của câu này cho câu khác
  
-- \defn{suy luận}: suy ra câu từ các câu khác
  
-- \defn{soundess}: dẫn xuất chỉ tạo ra các câu kéo theo
  
-- \defn{tính đầy đủ}: dẫn xuất có thể tạo ra tất cả các câu kéo theo

Thế giới Wumpus đòi hỏi khả năng thể hiện một phần
và thông tin phủ định, lý do theo trường hợp, v.v.

Chuỗi tiến, lùi là thời gian tuyến tính, hoàn chỉnh cho mệnh đề Horn

Độ phân giải hoàn tất cho logic mệnh đề

Logic mệnh đề thiếu sức mạnh diễn đạt