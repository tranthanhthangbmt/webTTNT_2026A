\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Mạng Bayes (Bayesian networks)

## Chương 14.1--3

---
## Phác thảo

- Cú pháp

- Ngữ nghĩa

- Phân phối được tham số hóa

---
## Mạng Bayesian

Một ký hiệu đồ họa đơn giản cho các xác nhận độc lập có điều kiện

và do đó cho đặc điểm kỹ thuật nhỏ gọn của phân phối chung đầy đủ

Cú pháp:
  
  một tập hợp các nút, mỗi nút một biến
  
  một đồ thị có hướng, không theo chu kỳ (liên kết \mat{$\approx$} "ảnh hưởng trực tiếp")
  
  phân phối có điều kiện cho mỗi nút dựa trên cha mẹ của nó:
    
    \mat{$P(X_i|\Parents(X_i))$}

Trong trường hợp đơn giản nhất, phân phối có điều kiện được biểu thị dưới dạng 

một \defn{bảng xác suất có điều kiện} (CPT) đưa ra 

phân phối trên \mat{$X_i$} cho mỗi kết hợp giá trị gốc

---
## Ví dụ

Cấu trúc liên kết của mạng mã hóa các xác nhận độc lập có điều kiện:

![Hình ảnh](../TaiLieu/slide_md/figures/dentist-network.png)

\mat{$Weather$} độc lập với các biến khác

\mat{$Toothache$} và \mat{$Catch$} độc lập có điều kiện với \mat{$Cavity$}

---
## Ví dụ

Tôi đang ở nơi làm việc, người hàng xóm John gọi điện báo rằng chuông báo thức của tôi đang đổ chuông, nhưng
hàng xóm Mary không gọi. Đôi khi nó được đặt ra bởi trẻ vị thành niên
động đất. Có trộm à?

Biến: \mat{$Burglar$}, \mat{$Earthquake$}, \mat{$Alarm$}, \mat{$JohnCalls$}, \mat{$MaryCalls$}

Cấu trúc liên kết mạng phản ánh kiến thức "nhân quả":
  
 -- Một tên trộm có thể tắt báo động
  
 -- Một trận động đất có thể tắt báo động
  
 -- Báo thức có thể khiến Mary gọi 
  
 -- Chuông báo thức có thể khiến John phải gọi

---
## Ví dụ tiếp theo.

![Hình ảnh](../TaiLieu/slide_md/figures/burglary2.png)

---
## Độ nhỏ gọn

CPT cho Boolean \mat{$X_i$} với \mat{$k$} cha mẹ Boolean có\hspace*{1.75in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/burglary-small.png)

\mat{$2^k$} hàng cho sự kết hợp của các giá trị gốc

Mỗi hàng yêu cầu một số \mat{$p$} cho \mat{$X_i\eq true$}

(số của \mat{$X_i\eq false$} chỉ là \mat{$1-p$})

Nếu mỗi biến có không quá \mat{$k$} cha mẹ, 

mạng hoàn chỉnh yêu cầu số \mat{$O(n\cdot 2^k)$}

Tức là, tăng tuyến tính với \mat{$n$}, so với  \mat{$O(2^n)$} để phân phối chung đầy đủ

Đối với mạng trộm, số \mat{$1 + 1 + 4 + 2 + 2 \eq 10$} (so với  \mat{$2^5-1 = 31$})

---
## Ngữ nghĩa toàn cầu

Ngữ nghĩa \defn{Global} xác định phân phối chung đầy đủ\hspace*{1.2in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/burglary-small.png)

là sản phẩm của phân phối có điều kiện cục bộ:
\mat{\[
  P(x_1,\ldots,x_n) = \myprod_{i\eq 1}^n P(x_i|\parents(X_i))
\]}
ví dụ: \mat{$P(j\land m\land a\land \lnot b \land \lnot e)$}
\mat{\[
  =
\]}

---
## Ngữ nghĩa toàn cầu

Ngữ nghĩa "Toàn cầu" xác định phân phối chung đầy đủ\hspace*{1.2in}in\raisebox{-1.5in}[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/burglary-small.png)

là sản phẩm của phân phối có điều kiện cục bộ:
\mat{\[
  P(x_1,\ldots,x_n) = \myprod_{i\eq 1}^n P(x_i|\parents(X_i))
\]}
ví dụ: \mat{$P(j\land m\land a\land \lnot b \land \lnot e)$} 
\mat{\begin{eqnarray*}
  &=& P(j|a) P(m|a) P(a|\lnot b, \lnot e) P(\lnot b) P(\lnot e)

  &=& 0.9\stimes 0.7\stimes 0.001\stimes 0.999 \stimes 0.998

  &\approx& 0.00063
\end{eqnarray*}}

---
## Ngữ nghĩa cục bộ

Ngữ nghĩa \defn{Local}: mỗi nút độc lập có điều kiện

của những người không phải là hậu duệ của nó được trao cho cha mẹ của nó

![Hình ảnh](../TaiLieu/slide_md/figures/nondescendants.png)

Định lý: \mat{Local semantics} \mat{$\lequiv$} \mat{global semantics}

---
## Chăn Markov

Mỗi nút độc lập có điều kiện với tất cả các nút khác dựa trên 
 của nó
\defn{Chăn Markov}: cha mẹ + con cái + cha mẹ con cái

![Hình ảnh](../TaiLieu/slide_md/figures/markov-blanket.png)

---
## Xây dựng mạng Bayesian

Cần một phương pháp sao cho một loạt các xác nhận có thể kiểm tra cục bộ của 

tính độc lập có điều kiện đảm bảo ngữ nghĩa toàn cầu cần thiết

1. Chọn thứ tự các biến \mat{$X_1,\ldots,X_n$}

2. Với \mat{$i$} = 1 đến \mat{$n$}
  
  thêm \mat{$X_i$} vào mạng 
  
  chọn cha mẹ từ \mat{$X_1,\ldots,X_{i-1}$} sao cho 
    
    \mat{$ P(X_i|\Parents(X_i)) = P(X_i|X_1,\, \ldots,\, X_{i-1}) $}

Sự lựa chọn này của cha mẹ đảm bảo ngữ nghĩa toàn cầu:
\mat{\begin{eqnarray*}
P(X_1,\ldots,X_n) &=& \myprod_{i\eq 1}^n P(X_i | X_1,\, \ldots,\, X_{i-1})
 &nbsp;&nbsp; \bbox{(chain rule)}

    &=& \myprod_{i\eq 1}^n P(X_i|\Parents(X_i))
 &nbsp;&nbsp; \bbox{(by construction)}
\end{eqnarray*}}

---
## Ví dụ

Giả sử chúng ta chọn thứ tự \mat{$M$}, \mat{$J$}, \mat{$A$}, \mat{$B$}, \mat{$E$}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make1.png)

\mat{$P(J|M) = P(J)$}?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự \mat{$M$}, \mat{$J$}, \mat{$A$}, \mat{$B$}, \mat{$E$}}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make2.png)

\ptext{\mat{$P(J|M) = P(J)$}? &nbsp;&nbsp;  Không

\mat{$P(A|J,M) = P(A|J)$}? \mat{$P(A|J,M) = P(A)$}?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự \mat{$M$}, \mat{$J$}, \mat{$A$}, \mat{$B$}, \mat{$E$}}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make3.png)

\ptext{\mat{$P(J|M) = P(J)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(A|J,M) = P(A|J)$}? \mat{$P(A|J,M) = P(A)$}? &nbsp;&nbsp;  Không

\mat{$P(B|A,J,M) = P(B|A)$}?

\mat{$P(B|A,J,M) = P(B)$}?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự \mat{$M$}, \mat{$J$}, \mat{$A$}, \mat{$B$}, \mat{$E$}}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make4.png)

\ptext{\mat{$P(J|M) = P(J)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(A|J,M) = P(A|J)$}? \mat{$P(A|J,M) = P(A)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(B|A,J,M) = P(B|A)$}? &nbsp;&nbsp;  Có

\ptext{\mat{$P(B|A,J,M) = P(B)$}? &nbsp;&nbsp;  Không

\mat{$P(E|B,A,J,M) = P(E|A)$}?

\mat{$P(E|B,A,J,M) = P(E|A,B)$}?

---
## Ví dụ

\ptext{Giả sử chúng ta chọn thứ tự \mat{$M$}, \mat{$J$}, \mat{$A$}, \mat{$B$}, \mat{$E$}}

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make5.png)

\ptext{\mat{$P(J|M) = P(J)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(A|J,M) = P(A|J)$}? \mat{$P(A|J,M) = P(A)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(B|A,J,M) = P(B|A)$}? &nbsp;&nbsp;  Có

\ptext{\mat{$P(B|A,J,M) = P(B)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(E|B,A,J,M) = P(E|A)$}? &nbsp;&nbsp;  Không

\ptext{\mat{$P(E|B,A,J,M) = P(E|A,B)$}? &nbsp;&nbsp;  Có

---
## Ví dụ tiếp theo.

![Hình ảnh](../TaiLieu/slide_md/figures/burglary-make5.png)

Quyết định tính độc lập có điều kiện là khó theo hướng phi nhân quả

(Các mô hình nhân quả và sự độc lập có điều kiện dường như đã được lập trình sẵn cho con người!)

Đánh giá xác suất có điều kiện là khó theo hướng phi nhân quả

Mạng kém gọn hơn: cần có số \mat{$1 + 2 + 4 + 2 + 4 \eq 13$}

---
## Ví dụ: Chẩn đoán ô tô

Bằng chứng ban đầu: xe không nổ máy

Các biến có thể kiểm tra (màu xanh lá cây), các biến " bị hỏng, vì vậy hãy sửa nó " (màu cam) 

Biến ẩn (màu xám) đảm bảo cấu trúc thưa thớt, giảm tham số

![Hình ảnh](../TaiLieu/slide_md/figures/car-net.png)

---
## Ví dụ: Bảo hiểm ô tô

![Hình ảnh](../TaiLieu/slide_md/figures/insurance-net.png)

---
## Phân phối có điều kiện nhỏ gọn

CPT tăng theo cấp số nhân với số lượng cha mẹ

CPT trở nên vô hạn với cha hoặc con có giá trị liên tục

Giải pháp: Phân phối \defn{canonical} được xác định nhỏ gọn

Các nút \defn{Xác định} là trường hợp đơn giản nhất:
  
   \mat{$X = f(Parents(X))$} cho một số chức năng \mat{$f$}

Ví dụ: hàm Boolean
  
  \mat{$NorthAmerican \lequiv Canadian \lor US \lor Mexican$}

Ví dụ: mối quan hệ số giữa các biến liên tục
\mat{\[
  \frac{\partial Level}{\partial t} = \mbox{ inflow + precipitation 
                                            - outflow - evaporation}
\]}

---
## Phân phối có điều kiện thu gọn tiếp.

\defn{Noisy-OR} mô hình phân phối có nhiều nguyên nhân không tương tác
  
  1) Cha mẹ \mat{$U_1\ldots U_k$} bao gồm tất cả các nguyên nhân (có thể thêm \defn{nút rò rỉ})
  
  2) Xác suất hư hỏng độc lập \mat{$q_i$} cho riêng từng nguyên nhân 
    
    \mat{${} \implies 
     P(X|U_1\ldots U_j,\lnot U_{j+1}\ldots \lnot U_k)
     = 1 - \myprod_{i\eq 1}^j q_i$}

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
| \makebox[72pt]{\mat{$Cold$}} | \makebox[72pt]{\mat{$Flu$}} | \makebox[72pt]{\mat{$Malaria$}} | \mat{$P(Fever)$} | \mat{$P(\lnot Fever)$} |
| F | F | F | \mat{$\mbf{0.0}$} | \mat{$1.0$} |
| F | F | T | \mat{$0.9$} | \mat{$\mbf{0.1}$} |
| F | T | F | \mat{$0.8$} | \mat{$\mbf{0.2}$} |
| F | T | T | \mat{$0.98$} | \mat{$0.02 = 0.2 \times 0.1$} |
| T | F | F | \mat{$0.4$} | \mat{$\mbf{0.6}$} |
| T | F | T | \mat{$0.94$} | \mat{$0.06 = 0.6 \times 0.1$} |
| T | T | F | \mat{$0.88$} | \mat{$0.12 = 0.6 \times 0.2$} |
| T | T | T | \mat{$0.988$} | \mat{$0.012 = 0.6 \times 0.2 \times 0.1$} |

Số tham số *tuyến tính* trong số cha mẹ

---
## Mạng lai (rời rạc+liên tục)

Rời rạc (\mat{$Subsidy?$} và \mat{$Buys?$});  liên tục (\mat{$Harvest$} và \mat{$Cost$})

![Hình ảnh](../TaiLieu/slide_md/figures/continuous-net.png)

Tùy chọn 1: rời rạc---có thể có lỗi lớn, CPT lớn

Tùy chọn 2: họ chính tắc được tham số hóa hữu hạn

1) Biến liên tục, cha mẹ rời rạc+liên tục (ví dụ: \mat{$Cost$})

2) Biến rời rạc, cha mẹ liên tục (ví dụ: \mat{$Buys?$})

---
## Biến con liên tục

Cần một hàm mật độ điều kiện \defn{} cho biến con đã cho
cha mẹ liên tục, cho mỗi nhiệm vụ có thể có cho cha mẹ riêng biệt

Phổ biến nhất là mô hình Gaussian tuyến tính \defn{}, ví dụ:
\begin{eqnarray*}
\lefteqn{P(Cost\eq c|Harvest\eq h,Subsidy?\eq true)}

 & = & N(a_t h + b_t, \sigma_t)(c)

 &=& \frac{1}{\sigma_t \sqrt{2\pi}}
 exp\left(-\frac{1}{2} 
          \left(\frac{c-(a_t h + b_t)}{\sigma_t}\right)^2
    \right)
\end{eqnarray*}

Giá trị trung bình \mat{$Cost$} thay đổi tuyến tính với \mat{$Harvest$}, phương sai được cố định

Sự thay đổi tuyến tính là không hợp lý trên toàn bộ phạm vi 
  
  nhưng hoạt động tốt nếu phạm vi *có khả năng* của \mat{$Harvest$} hẹp

---
## Biến con liên tục

![Hình ảnh](../TaiLieu/slide_md/figures/linear-gaussian-true.png)

Mạng liên tục với các bản phân phối của LG
  
  \mat{$\implies$} phân phối chung đầy đủ là Gaussian đa biến 
  

Mạng LG rời rạc+liên tục là mạng Gaussian có điều kiện \defn{}
tức là, một Gaussian đa biến trên tất cả các biến liên tục
cho mỗi sự kết hợp của các giá trị biến rời rạc

---
## Biến rời rạc với cha mẹ liên tục

Xác suất của \mat{$Buys?$} cho trước \mat{$Cost$} phải là ngưỡng "mềm":

![Hình ảnh](../TaiLieu/slide_md/figures/probit.png)

Phân phối \defn{Probit} sử dụng tích phân của Gaussian:
  
  \mat{$\Phi(x) = \int_{-\infty}^{x} N(0,1)(x) dx$}
  
  \mat{$P(Buys?\eq true \given Cost \eq c) = \Phi((-c + \mu)/\sigma)$}

---
## Tại sao lại là probit?

1. Nó có hình dạng phù hợp

2. Có thể xem là ngưỡng cứng có vị trí bị nhiễu

![Hình ảnh](../TaiLieu/slide_md/figures/noisy-threshold.png)

---
## Biến rời rạc tiếp theo.

Phân phối \defn{Sigmoid} (hoặc \defn{logit}) cũng được sử dụng trong mạng thần kinh:
\mat{\[
P(Buys?\eq true \given Cost \eq c) = \frac{1}{1+exp(-2\frac{-c+\mu}{\sigma})}
\]}
Sigmoid có hình dạng tương tự probit nhưng đuôi dài hơn nhiều:

![Hình ảnh](../TaiLieu/slide_md/figures/logit.png)

---
## Tóm tắt

Lưới Bayes cung cấp một biểu diễn tự nhiên cho (do nguyên nhân gây ra)

độc lập có điều kiện

Cấu trúc liên kết + CPT = biểu diễn nhỏ gọn của phân phối chung

Nói chung là dễ dàng đối với các chuyên gia (không phải) chuyên gia để xây dựng

Phân phối chuẩn (ví dụ: noise-OR) = biểu diễn nhỏ gọn của CPT

Các biến liên tục $\implies$ phân phối được tham số hóa (ví dụ: tuyến tính
Gaussian)