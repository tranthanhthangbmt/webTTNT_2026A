\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Mạng niềm tin (Belief networks)

## Chương 15.1--2

---
## Nội dung

- Độc lập có điều kiện (Conditional independence)

- Mạng Bayes: cú pháp và ngữ nghĩa

- Suy diễn chính xác (Exact inference)

- Suy diễn xấp xỉ (Approximate inference)

---
## Độc lập (Independence)

Hai biến ngẫu nhiên $A$ $B$ <u>độc lập</u> (tuyệt đối) khi và chỉ khi
  
\phantom{hoặc }$P(A|B) = P(A)$
  
hoặc $P(A,B) = P(A|B)P(B) = P(A)P(B)$

ví dụ: $A$ và $B$ là hai lần tung đồng xu

Nếu $n$ biến Boolean độc lập, phân phối đồng thời đầy đủ là
  
  $P(X_1,\ldots,X_n) = \myprod_i P(X_i)$

do đó có thể được chỉ định chỉ bằng $n$ con số

Độc lập tuyệt đối là một yêu cầu rất khắt khe, hiếm khi được đáp ứng

---
## Độc lập có điều kiện

Xem xét bài toán nha sĩ với ba biến ngẫu nhiên:
  
  $Toothache$, $Cavity$, $Catch$ (que thăm dò bằng thép vướng vào răng tôi)

Phân phối đồng thời đầy đủ có $2^3 - 1$ = 7 mục nhập độc lập

Nếu tôi bị sâu răng, xác suất que thăm dò vướng vào đó
không phụ thuộc vào việc tôi có bị đau răng hay không:
  
  (1) $P(Catch|Toothache,Cavity) = P(Catch|Cavity)$
 
nghĩa là, $Catch$ <u>độc lập có điều kiện</u> với $Toothache$ khi biết $Cavity$

Sự độc lập tương tự giữ nguyên nếu tôi không bị sâu răng:
  
  (2) $P(Catch|Toothache,\lnot Cavity) = P(Catch|\lnot Cavity)$

---
## Độc lập có điều kiện (tiếp)

Các phát biểu tương đương với (1) 

(1a) $P(Toothache|Catch,Cavity) = P(Toothache|Cavity)$ <u>Tại sao</u>??

(1b) $P(Toothache,Catch|Cavity) = P(Toothache|Cavity)P(Catch|Cavity)$ <u>Tại sao</u>??

Phân phối đồng thời đầy đủ bây giờ có thể được viết thành
  
  $P(Toothache,Catch,Cavity) = P(Toothache,Catch|Cavity) P(Cavity)$
    
    = $P(Toothache|Cavity)P(Catch|Cavity)P(Cavity)$

nghĩa là, 2 + 2 + 1 = 5 số độc lập (phương trình 1 và 2 loại bỏ đi 2 số)

---
## Độc lập có điều kiện (tiếp)

Các phát biểu tương đương với (1) 

(1a) $P(Toothache|Catch,Cavity) = P(Toothache|Cavity)$ <u>Tại sao</u>??

$P(Toothache|Catch,Cavity)$
  
  = $P(Catch|Toothache,Cavity)P(Toothache|Cavity)/P(Catch|Cavity)$
  
  = $P(Catch|Cavity)P(Toothache|Cavity)/P(Catch|Cavity)$ (từ 1)
  
  = $P(Toothache|Cavity)$

(1b) $P(Toothache,Catch|Cavity) = P(Toothache|Cavity)P(Catch|Cavity)$ <u>Tại sao</u>??

$P(Toothache,Catch|Cavity)$
  
  = $P(Toothache|Catch,Cavity)P(Catch|Cavity)$ (quy tắc nhân)
  
  = $P(Toothache|Cavity)P(Catch|Cavity)$ (từ 1a)

---
## Mạng niềm tin (Belief networks)

Một ký hiệu đồ họa đơn giản cho các khẳng định độc lập có điều kiện

và do đó dùng để biểu diễn một cách nhỏ gọn các phân phối đồng thời đầy đủ

Cú pháp:
  
  một tập hợp các nút, mỗi nút cho một biến
  
  một đồ thị có hướng, không chu trình (liên kết $\approx$ "ảnh hưởng trực tiếp")
  
  một phân phối có điều kiện cho mỗi nút khi biết các nút cha của nó:
    
    $P(X_i|Parents(X_i))$

Trong trường hợp đơn giản nhất, phân phối có điều kiện được biểu diễn bằng

một <u>bảng xác suất có điều kiện (conditional probability table - CPT)</u>

---
## Ví dụ

Tôi đang ở chỗ làm, người hàng xóm John gọi điện báo chuông báo động nhà tôi đang reo, nhưng
người hàng xóm Mary không gọi. Đôi khi nó bị kích hoạt bởi các
trận động đất nhỏ. Có kẻ trộm không?

Các biến: $Burglar$, $Earthquake$, $Alarm$, $JohnCalls$, $MaryCalls$

Cấu trúc mạng phản ánh kiến thức "nhân quả":

![Hình ảnh](../TaiLieu/slide_md/figures/burglary2.png)

Lưu ý: $\leq k$ nút cha ${} \implies O(d^k n)$ số so với $O(d^n)$

---
## Ngữ nghĩa (Semantics)

Ngữ nghĩa "toàn cục (Global)" định nghĩa phân phối đồng thời đầy đủ là

tích của các phân phối có điều kiện cục bộ:
\[
  P(X_1,\ldots,X_n) = \myprod_{i\eq 1}^n P(X_i|Parents(X_i))
\]
ví dụ: $P(J\land M\land A\land \lnot B \land \lnot E)$ <u>được cho bởi</u>??
  
  =

---
## Ngữ nghĩa

Ngữ nghĩa "toàn cục" định nghĩa phân phối đồng thời đầy đủ là

tích của các phân phối có điều kiện cục bộ:
\[
  P(X_1,\ldots,X_n) = \myprod_{i\eq 1}^n P(X_i|Parents(X_i))
\]
ví dụ: $P(J\land M\land A\land \lnot B \land \lnot E)$ <u>được cho bởi</u>??
  
  = $P(\lnot B)P(\lnot E)P(A|\lnot B \land \lnot E)P(J|A)P(M|A)$

Ngữ nghĩa "cục bộ (Local)": mỗi nút độc lập có điều kiện

với các nút không phải hậu duệ (nondescendants) của nó khi biết các nút cha của nó

Định lý: Ngữ nghĩa cục bộ $\lequiv$ ngữ nghĩa toàn cục

---
## Bao đóng Markov (Markov blanket)

Mỗi nút độc lập có điều kiện với tất cả các nút khác khi biết

<u>Bao đóng Markov</u> của nó: các cha + các con + các cha của các con

![Hình ảnh](../TaiLieu/slide_md/figures/markov-blanket.png)

---
## Xây dựng mạng niềm tin

Cần một phương pháp sao cho một loạt các khẳng định độc lập có điều kiện

có thể kiểm tra cục bộ đảm bảo được ngữ nghĩa toàn cục yêu cầu

1. Chọn một thứ tự của các biến $X_1,\ldots,X_n$

2. Với $i$ = 1 đến $n$
  
  thêm $X_i$ vào mạng
  
  chọn các cha từ $X_1,\ldots,X_{i-1}$ sao cho
    
    $ P(X_i|Parents(X_i)) = P(X_i|X_1,\, \ldots,\, X_{i-1}) $

Việc lựa chọn các nút cha này đảm bảo ngữ nghĩa toàn cục:
  
  $P(X_1,\ldots,X_n) = \myprod_{i\eq 1}^n P(X_i | X_1,\, \ldots,\, X_{i-1})$ (quy tắc chuỗi)
    
    = $\myprod_{i\eq 1}^n P(X_i|Parents(X_i))$ theo cách xây dựng

---
## Ví dụ

Giả sử chúng ta chọn thứ tự $M$, $J$, $A$, $B$, $E$

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make1.png)

$P(J|M) = P(J)$?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự $M$, $J$, $A$, $B$, $E$}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make2.png)

\ptext{$P(J|M) = P(J)$?} &nbsp;&nbsp;  Không

$P(A|J,M) = P(A|J)$? $P(A|J,M) = P(A)$?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự $M$, $J$, $A$, $B$, $E$}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make3.png)

\ptext{$P(J|M) = P(J)$? &nbsp;&nbsp;  Không}

\ptext{$P(A|J,M) = P(A|J)$? $P(A|J,M) = P(A)$?} &nbsp;&nbsp;  Không

$P(B|A,J,M) = P(B|A)$?

$P(B|A,J,M) = P(B)$?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự $M$, $J$, $A$, $B$, $E$}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make4.png)

\ptext{$P(J|M) = P(J)$? &nbsp;&nbsp;  Không}

\ptext{$P(A|J,M) = P(A|J)$? $P(A|J,M) = P(A)$? &nbsp;&nbsp;  Không}

\ptext{$P(B|A,J,M) = P(B|A)$?} &nbsp;&nbsp;  Có

\ptext{$P(B|A,J,M) = P(B)$?} &nbsp;&nbsp;  Không

$P(E|B,A,J,M) = P(E|A)$?

$P(E|B,A,J,M) = P(E|A,B)$?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự $M$, $J$, $A$, $B$, $E$}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make5.png)

\ptext{$P(J|M) = P(J)$? &nbsp;&nbsp;  Không}

\ptext{$P(A|J,M) = P(A|J)$? $P(A|J,M) = P(A)$? &nbsp;&nbsp;  Không}

\ptext{$P(B|A,J,M) = P(B|A)$? &nbsp;&nbsp;  Có}

\ptext{$P(B|A,J,M) = P(B)$? &nbsp;&nbsp;  Không}

\ptext{$P(E|B,A,J,M) = P(E|A)$?} &nbsp;&nbsp;  Không

\ptext{$P(E|B,A,J,M) = P(E|A,B)$?} &nbsp;&nbsp;  Có

---
## Ví dụ: Chẩn đoán xe (Car diagnosis)

Bằng chứng ban đầu: động cơ không nổ

Các biến có thể kiểm tra (hình bầu dục mỏng), các biến chẩn đoán (hình bầu dục dày)

Các biến ẩn (bị tô đậm) đảm bảo cấu trúc thưa thớt, giảm các tham số

![Hình ảnh](../TaiLieu/slide_md/figures/car-net.png)

---
## Ví dụ: Bảo hiểm xe ô tô (Car insurance)

Dự đoán chi phí yêu cầu bồi thường (y tế, trách nhiệm pháp lý, tài sản)

dựa trên dữ liệu từ đơn đăng ký (các nút không được tô sáng khác)

![Hình ảnh](../TaiLieu/slide_md/figures/insurance-net.png)

---
## Phân phối có điều kiện nhỏ gọn

Bảng CPT tăng theo cấp số nhân theo số lượng các nút cha

Bảng CPT trở thành vô hạn khi nút cha hoặc con mang giá trị liên tục

Giải pháp: Các phân phối <u>chính tắc (canonical)</u> được định nghĩa một cách nhỏ gọn

Các nút <u>tất định (Deterministic)</u> là trường hợp đơn giản nhất:
  
   $X = f(Parents(X))$ đối với một hàm số $f$ nào đó

Ví dụ: Các hàm Boolean
  
  $NorthAmerican \lequiv Canadian \lor US \lor Mexican$

Ví dụ: Mối quan hệ số học giữa các biến liên tục
\[
  \frac{\partial Level}{\partial t} = \mbox{ inflow + precipation 
                                            - outflow - evaporation}
\]

---
## Phân phối có điều kiện nhỏ gọn (tiếp)

Phân phối <u>Noisy-OR</u> mô hình hóa nhiều nguyên nhân không tương tác
  
  1) Các nút cha $U_1\ldots U_k$ bao gồm tất cả các nguyên nhân (có thể thêm <u>nút rò rỉ (leak node)</u>)
  
  2) Xác suất hỏng độc lập $q_i$ cho riêng từng nguyên nhân
    
    ${} \implies 
     P(X|U_1\ldots U_j,\lnot U_{j+1}\ldots \lnot U_k)
     = 1 - \myprod_{i\eq 1}^j q_i$

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
| \makebox[72pt]{$Cold$} | \makebox[72pt]{$Flu$} | \makebox[72pt]{$Malaria$} | $P(Fever)$ | $P(\lnot Fever)$ |
| F | F | F | $\mbf{0.0}$ | $1.0$ |
| F | F | T | $0.9$ | $\mbf{0.1}$ |
| F | T | F | $0.8$ | $\mbf{0.2}$ |
| F | T | T | $0.98$ | $0.02 = 0.2 \times 0.1$ |
| T | F | F | $0.4$ | $\mbf{0.6}$ |
| T | F | T | $0.94$ | $0.06 = 0.6 \times 0.1$ |
| T | T | F | $0.88$ | $0.12 = 0.6 \times 0.2$ |
| T | T | T | $0.988$ | $0.012 = 0.6 \times 0.2 \times 0.1$ |

Số lượng tham số tuyến tính với số lượng nút cha

---
## Mạng lai (Hybrid networks) (rời rạc+liên tục)

Biến rời rạc ($Subsidy?$ và $Buys?$);  biến liên tục ($Harvest$ và $Cost$)

![Hình ảnh](../TaiLieu/slide_md/figures/continuous-net.png)

Lựa chọn 1: rời rạc hóa---có thể có lỗi lớn, bảng CPT lớn

Lựa chọn 2: các họ chính tắc được tham số hóa hữu hạn

1) Biến liên tục, cha rời rạc+liên tục (ví dụ: $Cost$)

2) Biến rời rạc, cha liên tục (ví dụ: $Buys?$)

---
## Biến con liên tục

Cần một hàm <u>mật độ có điều kiện</u> cho biến con khi biết các
nút cha liên tục, cho mỗi phép gán có thể có đối với các cha rời rạc

Phổ biến nhất là mô hình <u>Gaussian tuyến tính</u>, ví dụ:
\begin{eqnarray*}
\lefteqn{P(Cost\eq c|Harvest\eq h,Subsidy?\eq true)}

 & = & N(a_t h + b_t, \sigma_t)(c)

 &=& \frac{1}{\sigma_t \sqrt{2\pi}}
 exp\left(-\frac{1}{2} 
          \left(\frac{c-(a_t h + b_t)}{\sigma_t}\right)^2
    \right)
\end{eqnarray*}

Giá trị trung bình $Cost$ thay đổi tuyến tính với $Harvest$, phương sai cố định

Biến thiên tuyến tính là vô lý trên toàn dải
  
  nhưng có thể chấp nhận được nếu phạm vi <u>khả dĩ</u> của $Harvest$ hẹp

---
## Biến con liên tục

\threegraph{graphs/linear-gaussian-true.ps}{graphs/linear-gaussian-false.ps}{graphs/linear-gaussian-average.ps}

Mạng toàn liên tục với các phân phối LG
  
  $\implies$ phân phối đồng thời đầy đủ là một Gaussian đa biến
  

Mạng LG rời rạc+liên tục là một mạng <u>Gaussian có điều kiện</u>
nghĩa là, một Gaussian đa biến trên tất cả các biến liên tục
cho mỗi tổ hợp các giá trị biến rời rạc

---
## Biến rời rạc có các cha liên tục

Xác suất $Buys?$ khi biết $Cost$ nên là một ngưỡng "mềm":

![Hình ảnh](../TaiLieu/slide_md/figures/probit.png)

Phân phối <u>Probit</u> sử dụng tích phân của Gaussian:
  
  $\Phi(x) = \int_{-\infty}{^x} N(0,1)(x) dx$
  
  $P(Buys?\eq true \given Cost \eq c) = \Phi((-c + \mu)/\sigma)$

Có thể xem là ngưỡng cứng có vị trí bị nhiễu

---
## Biến rời rạc (tiếp)

Phân phối <u>Sigmoid</u> (hoặc <u>logit</u>) cũng được sử dụng trong mạng nơ-ron:
\[
P(Buys?\eq true \given Cost \eq c) = \frac{1}{1+exp(-2\frac{-c+\mu}{\sigma})}
\]
Sigmoid có dạng tương tự probit nhưng đuôi dài hơn nhiều:

![Hình ảnh](../TaiLieu/slide_md/figures/logit.png)