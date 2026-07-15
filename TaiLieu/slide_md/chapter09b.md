\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Suy diễn quy mô công nghiệp (Industrial-strength inference)

## Chương 9.5--6, Chương 8.1 và 10.2--3

---
## Nội dung

- Tính đầy đủ (Completeness)

- Phân giải (Độ phân giải)

- Lập trình logic (Lập trình logic)

---
##  Tính đầy đủ trong FOL

Thủ tục $i$ là đầy đủ khi và chỉ khi
\[
  KB \vdash_i 
  pha  &nbsp;&nbsp;  \mbox{{\rm mỗi khi}}  &nbsp;&nbsp;  KB \models 
  pha
\]
Suy diễn tiến và lùi là <u>đầy đủ cho KB Horn</u>

Nhưng không đủ logic cho một bậc tổng hợp

Ví dụ, từ
\begin{formula}
  Tiến sĩ(x) \implies Trình độ chuyên môn cao(x) 

  \lkhông phải Tiến sĩ(x) \implies Thu nhập sớm(x)

  Cao(x) \implies Giàu(x)

  Thu nhập sớm(x) \implies Giàu(x)
\end{formula}
lẽ ra phải có thể suy ra $Rich(Me)$, nhưng FC/BC sẽ không làm được điều đó

Có tồn tại một thuật toán đầy đủ không?

---
## Lịch sử sum họp của việc suy luận

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
| 450**TCN** | Stoics | logic mệnh đề, suy diễn (có thể) |
| 322**TCN** | Aristotle | "tam đoạn luận" (quy tắc suy diễn), lượng từ |
| 1565 | Cardano | lý thuyết xác suất (logic mệnh đề + độ bất định) |
| 1847 | Boole | logic mệnh đề (một lần nữa) |
| 1879 | Frege | logic bậc một |
| 1922 | Wittgenstein | chứng minh bằng bảng chân lý |
| 1930 | G\"odel | $\exists$ thuật toán đầy đủ cho FOL |
| 1930 | Herbrand | thuật toán đầy đủ cho FOL (rút gọn về mệnh đề) |
| 1931 | G\"odel | $\lnot\exists$ thuật toán đầy đủ cho số học |
| 1960 | Davis/Putnam | thuật toán "thực tiễn" cho mệnh đề logic |
| 1965 | Robinson | thuật toán "thực tiễn" cho FOL---giải phân tích |

---
## Phân tích (Độ phân giải)

Kéo theo logic bậc một chỉ là <u>nửa quyết định (semicidable)</u>:
  
có thể tìm thấy bằng chứng của $
  pha$ if $KB \models 
  pha$
  
không thể luôn chứng minh rằng $KB \not\models 
  pha$

So sánh với vấn đề dừng (Vấn đề tạm dừng): thủ tục chứng minh có thể sắp xếp dừng
với sự cố hoặc thất bại hoặc có thể diễn ra mãi mãi

Phân tích là một thủ tục <u>bác bỏ (bác bỏ)</u>:
  
để chứng minh $KB \models 
  pha$, chỉ ra rằng $KB\land\lnot
  pha$ là không thỏa mãn được

Phân giải sử dụng $KB$, $\lnot
  pha$ dưới dạng chuẩn hội (CNF) (phép hội của các mệnh đề)

Quy tắc suy diễn phân giải hợp hai mệnh đề để tạo ra một mệnh đề mới:

in
![Hình ảnh](../TaiLieu/slide_md/figures/resolve-clauses.png)

Sự suy diễn tiếp continue cho đến khi một <u>mệnh đề trống (mệnh đề trống)</u> được suy ra (mâu mạnh)

---
## Quy tắc suy diễn phân giải

Phiên bản mệnh đề cơ bản:
\begin{formula}
{\displaystyle
\frac{
  pha \lor \beta,\;\; \lnot \beta \lor \gamma}{
  pha \lor \gamma}
 &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{hoặc tương đương}  &nbsp;&nbsp;&nbsp;&nbsp; 
\frac{\lnot
  pha \implies \beta,\;\; \beta \implies \gamma}{\lkhông 
  pha \implies \gamma}
}
\end{formula}
Phiên bản đầy đủ cấp độ:
\begin{formula}
{\begin{array}{l} p_1\lor \ldots\ p_j\ \ldots \lor p_m,

                   q_1\lor \ldots\ q_k\ \ldots \lor q_n
 \end{array}}
\over
{\begin{array}{l}
(p_1\lor \ldots\ p_{j-1} \lor p_{j+1}\ \ldots p_m \lor 
q_1\ldots\ q_{k-1} \lor q_{k+1}\ \ldots \lor q_n)\sigma
 \end{array}}
\end{formula}
trong đó $p_j\sigma = \lnot q_k \sigma$

Ví dụ:
\begin{formula}
{\begin{array}{l} \lnot Rich(x) \lor Unhappy(x) 

                  Giàu (Tôi)
 \end{array}}
\over
{\begin{array}{l} Không vui(Tôi)
 \end{array}}
\end{formula}
với $\sigma = \{x/Me\}$

---
## Dạng hội chuẩn (Conjunctive Normal Form)

<u>Literal</u> = câu nguyên thủy (có thể được phủ định), ví dụ: $\lnot Rich(Me)$

<u>Mệnh đề (Clause)</u> = phép tuyển các chữ, ví dụ: $\lnot Rich(Me) \lor Unhappy(Me)$

KB được phép của các mệnh đề

Bất kỳ KB FOL nào cũng có thể được chuyển đổi thành CNF như sau:

1. Thay thế $P{\implies}Q$ bằng ${\lnot}P{\lor}Q$

2. Chuyển $\lnot$ vào trong, ví dụ: 
      $\lnot \forall x\,P$ trở thành $\exists x\,\lnot P$

3. Chuẩn hóa các biến đổi, ví dụ: 
  $\forall x\,P \lor \exists x\,Q$ trở thành $\forall x\,P \lor \exists y\,Q$

4. Chuyển lượng từ sang trái theo thứ tự, ví dụ:
  $\forall x\,P \lor \exists x\,Q$ trở thành $\forall x\exists y\,P \lor Q$

5. Loại bỏ $\exists$ bằng phương pháp Skolemization (slide tiếp theo)

6. Bỏ các từ phổ dụng

7. Phân phối $\land$ qua $\lor$, ví dụ:
    $(P \land Q) \lor R$ trở thành $(P\lor Q) \land (P\lor R)$

---
## Phương pháp Skolemization

$\exists x\,Rich(x)$ trở thành $Rich(G1)$ trong đó $G1$ là một "<u>hằng số Skolem</u>" mới

$\Exi{k} \frac{d}{dy}(k^y) \eq k^y$ trở thành $\frac{d}{dy}(e^y) \eq e^y$

Khó hơn khi $\exists$ nằm bên trong $\forall$

Ví dụ: "Mọi người đều có một trái tim"
  
   $\All{x} Person(x) \implies \Exi{y} Heart(y) \land Has(x,y)$

<u>Sai</u>:
  
   $\All{x} Person(x) \implies Heart(H1) \land Has(x,H1)$

<u> Đúng</u>:
  
   $\All{x} Person(x) \implies Heart(H(x)) \land Has(x,H(x))$

trong đó $H$ là một ký hiệu mới ("hàm Skolem")

Các đối số của hàm Skolem: Tất cả các biến số từ phổ dụng <u>bao quanh</u>

---
## Chứng minh phân giải 

Để chứng minh $
  pha$:
  
-- định nghĩa nó
  
-- chuyển đổi sang CNF
  
-- thêm vào CNF KB
  
-- suy diễn ra ổn định

Ví dụ: để chứng minh $Rich(me)$, thêm $\lnot Rich(me)$ vào CNF KB
\begin{formula}
  \lkhông phải Tiến sĩ(x) \lor Có trình độ cao(x) 

  Tiến sĩ(x) \lor Thu nhập sớm(x)

  \lkhông đủ tiêu chuẩn cao(x) \lor Rich(x)

  \lkhông phải Thu nhập sớm(x) \lor Rich(x)
\end{formula}

---
## Chứng minh phân giải 

![Hình ảnh](../TaiLieu/slide_md/figures/rich-proof.png)

---
## Logic trình nhập

Khẩu hiệu: tính toán là suy diễn trên logic KB

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
|  | <u>Lập trình logic</u> | <u>Lập trình thông thường</u> |
| 1. | Xác định vấn đề | Xác định vấn đề |
| 2. | Thu thập thông tin | Thu thập thông tin |
| 3. | Nghỉ giải lao | Tìm ra giải pháp |
| 4. | Mã hóa thông tin vào KB | Giải pháp lập trình |
| 5. | Mã hóa ví dụ vấn đề thành sự kiện | Mã hóa ví dụ vấn đề thành dữ liệu |
| 6. | Hỏi các truy vấn | Áp dụng chương trình vào dữ liệu |
| 7. | Tìm các lỗi sự kiện | Loại bỏ các lỗi thủ tục |

Tránh dễ dàng gỡ lỗi $Capital(NewYork,US)$ hơn $x:= x+2$ !

---
##  Hệ thống Prolog

Cơ sở: suy diễn ngược với các mệnh đề Horn + các tính năng bổ sung (chuông \& còi)

Được sử dụng rộng rãi ở Châu Âu, Nhật Bản (cơ sở của dự án Thế hệ thứ 5)

Kỹ thuật biên dịch $\Rightarrow$ 10 triệu LIPS

Chương trình = tập các mệnh đề = `head :- Literal$_1$, $\ldots$ Liter$_n$.

Hợp chất hiệu quả nhất bằng <u>mã hóa mở (opencoding)`

Truy xuất hiệu quả các mệnh đề phù hợp bằng liên kết trực tiếp

Suy diễn lùi từ trái sang phải, độ sâu ưu tiên

Các từ tích hợp cho số học v.v., ví dụ: `X is Y*Z+3Ni1012]
Giả định thế giới đóng ("phủ định như thất bại")
  
   ví dụ: {\tt not PhD(X)` thành công nếu `PhD(X)` thất bại

---
## Ví dụ Prolog</u>

Tìm kiếm độ sâu ưu tiên từ trạng thái bắt đầu `X`:

```text
dfs(X) :- goal(X).
dfs(X) :- successor(X,S),dfs(S).
```

Không cần lặp qua `S`: `next` thành công với mỗi trường hợp

Nối hai danh sách để tạo ra danh sách thứ ba:

```text
append([],Y,Y).                         
append([X|L],Y,[X|Z]) :- append(L,Y,Z). 
                                        
query:   append(A,B,[1,2]) ?            
answers: A=[]    B=[1,2]
         A=[1]   B=[2]
         A=[1,2] B=[]
```

\end{huge