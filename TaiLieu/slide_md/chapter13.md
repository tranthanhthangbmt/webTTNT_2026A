\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Uncertainty

## Chapter 13

---
## Phác thảo

- Sự không chắc chắn

- Xác suất

- Cú pháp và ngữ nghĩa

- Suy luận

- Độc lập và sự cai trị của Bayes

---
## Độ không đảm bảo

Đặt hành động \mat{$A_t$} = rời sân bay \mat{$t$} phút trước chuyến bay 

Liệu \mat{$A_t$} có đưa tôi đến đó đúng giờ không?

Sự cố:
  
1) khả năng quan sát một phần (trạng thái đường, kế hoạch của người lái xe khác, v.v.)
  
2) cảm biến nhiễu (báo cáo lưu lượng KCBS)
  
3) sự không chắc chắn về kết quả hành động (xẹp lốp, v.v.)
  
4) sự phức tạp to lớn của việc lập mô hình và dự đoán lưu lượng truy cập

Do đó, đây là một cách tiếp cận hoàn toàn hợp lý

\phantom{or }1) có nguy cơ nói dối: "\mat{$A_{25}$} sẽ đưa tôi đến đó đúng giờ"

hoặc 2) dẫn đến kết luận quá yếu để đưa ra quyết định:
    
"\mat{$A_{25}$} sẽ đưa tôi đến đó đúng giờ nếu không có tai nạn trên cầu
    
và trời không mưa và lốp xe của tôi vẫn còn nguyên vẹn, v.v."

(\mat{$A_{1440}$} có thể nói một cách hợp lý là sẽ đưa tôi đến đó đúng giờ

nhưng tôi sẽ phải ở lại sân bay qua đêm $\ldots$)

---
## Phương pháp xử lý độ không đảm bảo

Logic \defn{Mặc định} hoặc \defn{không đơn điệu}:
  
  Giả sử xe của tôi không bị xẹp lốp
  
  Giả sử \mat{$A_{25}$} hoạt động trừ khi có bằng chứng mâu thuẫn

Vấn đề: Giả định nào là hợp lý? Làm thế nào để giải quyết mâu thuẫn?

\defn{Quy tắc có hệ số mờ}:
  
\mat{$A_{25} \mapsto_{0.3} AtAirportOnTime$}
  
\mat{$Sprinkler \mapsto_{0.99} WetGrass$}
  
\mat{$WetGrass \mapsto_{0.7} Rain$}

Sự cố: Sự cố với sự kết hợp, ví dụ: \mat{$Sprinkler$} gây ra \mat{$Rain$}??

\defn{Xác suất}
  
  Với những bằng chứng sẵn có,
    
    \mat{$A_{25}$} có khả năng sẽ đưa tôi đến đó đúng giờ \mat{$0.04$}

Lý thuyết cờ bạc của Mahaviracarya (9 C.), Cardamo (1565)

(\defn{Logic mờ} xử lý *mức độ đúng* KHÔNG phải là sự không chắc chắn, ví dụ:
  
  \mat{$WetGrass$} đúng với độ \mat{$0.2$})

---
## Xác suất

Khẳng định xác suất *tóm tắt* tác động của 
  
  \note{sự lười biếng}: không liệt kê các trường hợp ngoại lệ, trình độ chuyên môn, v.v.
  
  \note{sự thiếu hiểu biết}: thiếu các sự kiện liên quan, các điều kiện ban đầu, v.v.

Xác suất \defn{Chủ quan} hoặc \defn{Bayesian}:

Xác suất liên kết các mệnh đề với trạng thái hiểu biết của chính mình
    
ví dụ: \mat{$P(A_{25} | \mbox{no reported accidents}) = 0.06$}

Đây là những tuyên bố *không phải* về một "xác suất
xu hướng" trong tình hình hiện tại

(nhưng có thể rút ra từ kinh nghiệm trong quá khứ về những tình huống tương tự)

Xác suất của mệnh đề thay đổi với bằng chứng mới:
    
ví dụ: \mat{$P(A_{25} | \mbox{no reported accidents},\ \mbox{5 a.m.}) = 0.15$}

(Tương tự với trạng thái kế thừa logic \mat{$KB \models 
  pha$}, không phải sự thật.)

---
## Đưa ra quyết định trong điều kiện không chắc chắn

Giả sử tôi tin vào điều sau:
\mat{\begin{eqnarray*}
P(A_{25}\mbox{ gets me there on time} | \ldots) &=& 0.04 

P(A_{90}\mbox{ gets me there on time} | \ldots) &=& 0.70 

P(A_{120}\mbox{ gets me there on time} | \ldots) &=& 0.95 

P(A_{1440}\mbox{ gets me there on time} | \ldots) &=& 0.9999 
\end{eqnarray*}}
Chọn hành động nào?

Tùy thuộc vào \defn{ưu tiên} của tôi đối với việc lỡ chuyến bay và ẩm thực ở sân bay, v.v.

\defn{Lý thuyết hữu ích} được sử dụng để biểu diễn và suy ra các ưu tiên

\defn{Lý thuyết quyết định} = lý thuyết tiện ích + lý thuyết xác suất

---
## Xác suất cơ bản

Bắt đầu với tập \mat{$\Omega$}---không gian mẫu \defn{}
  
ví dụ: có thể có 6 lần tung xúc xắc.
  
\mat{$\omega\in \Omega$} là một \defn{điểm mẫu}/\defn{thế giới có thể}/\defn{sự kiện nguyên tử}

Mô hình xác suất \defn{} hoặc \defn{} là không gian mẫu

với một phép gán \mat{$P(\omega)$} cho mỗi \mat{$\omega\in\Omega$} s.t.
  
  \mat{$0\leq P(\omega) \leq 1$}
  
  \mat{$\mysum_{\omega} P(\omega) = 1$}

ví dụ: \mat{$P(1)\eq P(2)\eq P(3)\eq P(4)\eq P(5)\eq P(6) \eq 1/6$}.

Một \defn{sự kiện} \mat{$A$} là bất kỳ tập hợp con nào của \mat{$\Omega$}
\mat{\[
  P(A) = \mysum_{\{\omega\in A\}} P(\omega)
\]}
Ví dụ: \mat{$P(\mbox{die roll}<4) = P(1) + P(2) + P(3) = 1/6 + 1/6 + 1/6 = 1/2$}

---
## Biến ngẫu nhiên

Biến ngẫu nhiên \defn{} là một hàm từ các điểm mẫu
đến một phạm vi nào đó, ví dụ: số thực hoặc Booleans
  
ví dụ: \mat{$Odd(1)\eq true$}.

\mat{$P$} tạo ra phân phối xác suất \defn{} cho bất kỳ r.v. \mat{$X$}:
\mat{\[
  P(X\eq x_i) = \mysum_{\{\omega: X(\omega)\eq x_i\}} P(\omega)
\]}
ví dụ: \mat{$P(Odd\eq true) = P(1) + P(3) + P(5) = 1/6 + 1/6 + 1/6 = 1/2$}

---
## Dự luật

Hãy coi một mệnh đề như một sự kiện (tập hợp các điểm mẫu)

nơi mệnh đề là đúng

Cho các biến ngẫu nhiên Boolean \mat{$A$} và \mat{$B$}:
  
  sự kiện \mat{$a$} = tập hợp các điểm mẫu trong đó \mat{$A(\omega)\eq true$}
  
  sự kiện \mat{$\lnot a$} = tập hợp các điểm mẫu trong đó \mat{$A(\omega)\eq false$}
  
  sự kiện \mat{$a\land b$} = điểm trong đó \mat{$A(\omega)\eq true$} và \mat{$B(\omega)\eq true$}

Thông thường trong các ứng dụng AI, các điểm mẫu được xác định \emph{}

bởi các giá trị của một tập hợp các biến ngẫu nhiên, tức là 

không gian mẫu là tích Descartes của các phạm vi biến

Với các biến Boolean, điểm mẫu = mô hình logic mệnh đề
    
  ví dụ: \mat{$A\eq true$}, \mat{$B\eq false$} hoặc \mat{$a\land \lnot b$}.

Mệnh đề = sự phân tách các sự kiện nguyên tử trong đó nó đúng
  
ví dụ: \mat{$(a\lor b) \equiv (\lnot a \land b) \lor (a \land \lnot b) \lor (a \land b) $}
  
\mat{$\implies P(a\lor b) = P(\lnot a \land b) + P(a \land \lnot b) + P(a \land b) $}

---
## Tại sao sử dụng xác suất?

Các định nghĩa ngụ ý rằng các sự kiện nhất định có liên quan về mặt logic
phải có xác suất liên quan

Ví dụ: \mat{$P(a \lor b) = P(a) + P(b) - P(a\land b)$}

,45\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/axiom3-venn.png)

de Finetti (1931): một đại lý đặt cược theo xác suất vi phạm
những tiên đề này có thể bị buộc phải đặt cược để mất tiền bất kể kết quả ra sao.

---
## Cú pháp mệnh đề

\defn{Các biến ngẫu nhiên đề xuất} hoặc \defn{Boolean}
  
  ví dụ: \mat{$Cavity$} (tôi có bị sâu răng không?)
  
  \mat{$Cavity\eq true$} là một mệnh đề, cũng được viết là \mat{$cavity$}

\defn{Rời rạc} biến ngẫu nhiên (\note{hữu hạn} hoặc \note{vô hạn}) 
  
  ví dụ: \mat{$Weather$} là một trong \mat{$\<sunny,rain,cloudy,snow\>$}
  
  \mat{$Weather\eq rain$} là một mệnh đề
  
Các giá trị phải đầy đủ và loại trừ lẫn nhau

\defn{Liên tục} biến ngẫu nhiên (\note{bounded} hoặc \note{unbounded})
  
  ví dụ: \mat{$Temp\eq 21.6$}; cũng cho phép, ví dụ: \mat{$Temp<22.0$}.

Sự kết hợp Boolean tùy ý của các mệnh đề cơ bản

---
## Xác suất trước

\defn{Trước} hoặc \defn{xác suất vô điều kiện} của mệnh đề
  
  ví dụ: \mat{$P(Cavity\eq true) = 0.1$} và \mat{$P(Weather \eq sunny) = 0.72$}

tương ứng với niềm tin trước khi có bất kỳ bằng chứng (mới) nào

\defn{Phân bố xác suất} đưa ra các giá trị cho tất cả các phép gán có thể có:
  
  \mat{$P(Weather) = \<0.72,0.1,0.08,0.1\>$} (\note{chuẩn hóa}, tức là 
       tổng thành \mat{$1$})

\defn{Phân bố xác suất chung} cho một tập hợp r.v.s mang lại 

xác suất của mọi sự kiện nguyên tử trên các r.v.s đó (tức là mọi điểm mẫu)
  
  \mat{$P(Weather,Cavity)$} = ma trận các giá trị \mat{$4 \times 2$}:

\mat{\[\begin{array}{l|llll}
\hfil Weather \eq & sunny & rain & cloudy & snow 

\hline
Cavity \eq true &0.144 &0.02 &0.016 & 0.02

Cavity \eq false&0.576 &0.08 &0.064 & 0.08
\end{array}\]}
*Mọi thắc mắc về miền đều có thể được giải đáp chung

phân phối vì mọi sự kiện là tổng của các điểm mẫu*

---
## Xác suất cho các biến liên tục

Phân phối nhanh dưới dạng hàm tham số của giá trị:
  
\mat{$P(X\eq x) = U[18,26](x)$} = mật độ đồng đều giữa \mat{$18$} và \mat{$26$}

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/uniform-density.png)

Ở đây \mat{$P$} là \defn{mật độ}; tích phân thành 1.

\mat{$P(X\eq 20.5)=0.125$} thực sự có nghĩa là
\mat{\[
  \lim_{dx \to 0} P(20.5 \leq X \leq 20.5+dx)/dx = 0.125
\]}

---
## Mật độ Gaussian

\mat{$P(x) = \frac{1}{\sqrt{2\pi} \sigma} e^{-(x-\mu)^2/2\sigma^2}$}

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/gaussian-density.png)

---
## Xác suất có điều kiện

\defn{Có điều kiện} hoặc \defn{xác suất sau}
  
  ví dụ: \mat{$P(cavity | toothache) = 0.8$}
  
  tức là, *cho rằng* \mat{$toothache$} *là tất cả những gì tôi biết*
  
  *NOT* "nếu \mat{$toothache$} thì 80\% cơ hội có \mat{$cavity$}"

(Ký hiệu cho phân bố có điều kiện:
  
  \mat{$P(Cavity |Toothache)$} = vectơ 2 phần tử của vectơ 2 phần tử)

Nếu chúng ta biết nhiều hơn, ví dụ: \mat{$cavity$} cũng được cho, thì chúng ta có
  
  \mat{$P(cavity | toothache,cavity) = 1$}

Lưu ý: niềm tin ít cụ thể hơn * vẫn có giá trị * sau khi có thêm bằng chứng 
đến, nhưng không phải lúc nào cũng *hữu ích*

Bằng chứng mới có thể không liên quan, cho phép đơn giản hóa, ví dụ:
  
\mat{$P(cavity | toothache,49ersWin) = P(cavity | toothache) = 0.8$}

Loại suy luận này, được thừa nhận bởi kiến thức lĩnh vực, là rất quan trọng

---
## Xác suất có điều kiện

Định nghĩa xác suất có điều kiện:
\mat{\[
  P(a|b) = \frac{P(a\land b)}{P(b)} \mbox{ if } P(b) \neq 0
\]}
\defn{Quy tắc tích số} đưa ra công thức thay thế:
  
  \mat{$P(a\land b) = P(a|b)P(b) = P(b|a)P(a)$}

Phiên bản chung áp dụng cho toàn bộ bản phân phối, ví dụ:
  
  \mat{$P(Weather,Cavity) = P(Weather|Cavity) P(Cavity)$}

(Xem dưới dạng tập hợp các phương trình \mat{$4\times 2$}, *không phải * ma trận đa.)

\defn{Quy tắc chuỗi} được rút ra bằng cách áp dụng liên tiếp quy tắc sản phẩm:
  
\mat{$P(X_1,\ldots,X_n) = P(X_1,\ldots,X_{n-1})\ 
                        P(X_n | X_1,\ldots,X_{n-1})$}
    
                    = \mat{$P(X_1,\ldots,X_{n-2})\ 
                        P(X_{n-1} | X_1,\ldots,X_{n-2})\ 
                        P(X_n | X_1,\ldots,X_{n-1})$}
    
                  = \mat{$\ldots$}
    
                  = \mat{$\myprod_{i\eq 1}^n P(X_i | X_1,\ldots,X_{i-1})$}

 

---
## Suy luận bằng phép liệt kê

Bắt đầu với việc phân phối chung:

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dentist-joint.png)

Đối với bất kỳ mệnh đề nào \mat{$\phi$}, hãy tính tổng các sự kiện nguyên tử trong đó nó đúng:
  
 \mat{$P(\phi) = \mysum_{\omega: \omega \models \phi} P(\omega)$}

---
## Suy luận bằng phép liệt kê

Bắt đầu với việc phân phối chung:

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dentist-joint1.png)

Đối với bất kỳ mệnh đề nào \mat{$\phi$}, hãy tính tổng các sự kiện nguyên tử trong đó nó đúng:
  
 \mat{$P(\phi) = \mysum_{\omega: \omega \models \phi} P(\omega)$}

\mat{$P(toothache) = 0.108 + 0.012 + 0.016 + 0.064 = 0.2$}

---
## Suy luận bằng phép liệt kê

Bắt đầu với việc phân phối chung:

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dentist-joint2.png)

Đối với bất kỳ mệnh đề nào \mat{$\phi$}, hãy tính tổng các sự kiện nguyên tử trong đó nó đúng:
  
 \mat{$P(\phi) = \mysum_{\omega: \omega \models \phi} P(\omega)$}

\mat{$P(cavity \lor toothache) = 0.108 + 0.012 + 0.072 + 0.008 + 0.016 + 0.064 
                         = 0.28$}

---
## Suy luận bằng phép liệt kê

Bắt đầu với việc phân phối chung:

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dentist-joint3.png)

Cũng có thể tính xác suất có điều kiện:
\mat{\begin{eqnarray*}
P(\lnot cavity|toothache) 
     &=& \frac{P(\lnot cavity \land toothache)}{P(toothache)}

     &=& \frac{0.016+0.064}{0.108 + 0.012 + 0.016 + 0.064} = 0.4
\end{eqnarray*}}

---
## Chuẩn hóa

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dentist-joint4.png)

Mẫu số có thể được xem dưới dạng hằng số chuẩn hóa \note{} \mat{$
  pha$}
\mat{\begin{eqnarray*}
 \lefteqn{P(Cavity|toothache) = 
  pha\, P(Cavity,toothache)} 

  &=& 
  pha\, [P(Cavity,toothache,catch)+P(Cavity,toothache,\lnot catch)]

  &=& 
  pha\, [\<0.108,0.016\> + \<0.012,0.064\>] 

  &=& 
  pha\, \<0.12,0.08\> = \<0.6,0.4\>
\end{eqnarray*}}
Ý tưởng chung: tính toán phân phối trên biến truy vấn

bằng cách sửa \defn{các biến bằng chứng} và tính tổng trên \defn{các biến ẩn}

---
## Suy luận bằng cách liệt kê, tiếp theo.

Đặt \mat{$\mbf{X}$} là tất cả các biến. Thông thường, chúng tôi muốn 
  
  phân bố khớp sau của các biến truy vấn \defn{} \mat{$\mbf{Y}$}
  
  các giá trị cụ thể \mat{$\mbf{e}$} cho các biến bằng chứng \defn{} \mat{$\mbf{E}$}

Đặt \defn{biến ẩn} là \mat{$\mbf{H} = \mbf{X} - \mbf{Y} - \mbf{E}$}

Sau đó, việc tổng hợp các mục chung được yêu cầu được thực hiện bằng cách \note{tổng kết}
các biến ẩn:
\mat{\[
P(\mbf{Y}|\mbf{E}\eq \mbf{e}) = 
  pha P(\mbf{Y},\mbf{E}\eq \mbf{e})
= 
  pha \mysum_{\smbf{h}} P(\mbf{Y},\mbf{E}\eq \mbf{e},\mbf{H}\eq \mbf{h})
\]}
Các số hạng trong phép tính tổng là các mục chung vì \mat{$\mbf{Y}$}, \mat{$\mbf{E}$} và \mat{$\mbf{H}$} cùng nhau làm cạn kiệt tập hợp các biến ngẫu nhiên

Vấn đề rõ ràng:
  
1) Độ phức tạp về thời gian trong trường hợp xấu nhất \mat{$O(d^n)$} trong đó \mat{$d$} là giá trị lớn nhất
  
2) Độ phức tạp của không gian \mat{$O(d^n)$} để lưu trữ phân phối chung
  
3) Làm cách nào để tìm số cho mục \mat{$O(d^n)$}???

---
## Độc lập

\mat{$A$} và \mat{$B$} là \defn{độc lập} iff

\mat{$P(A|B) \eq P(A)$}  &nbsp;&nbsp;  hoặc  &nbsp;&nbsp;  \mat{$P(B|A) \eq P(B)$}  &nbsp;&nbsp;  hoặc  &nbsp;&nbsp;  \mat{$P(A, B) \eq P(A)P(B)$}

,75\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/weather-independence.png)

\mat{$P(Toothache,Catch,Cavity,Weather)$}
    
\mat{${} = P(Toothache,Catch,Cavity)P(Weather)$}

32 mục giảm xuống còn 12; cho \mat{$n$} đồng tiền thiên vị độc lập, \mat{$2^n \rightarrow n$}

Độc lập tuyệt đối mạnh mẽ nhưng hiếm có

Nha khoa là một lĩnh vực rộng lớn với hàng trăm biến số,

không ai trong số đó là độc lập. Phải làm gì?

---
## Độc lập có điều kiện

\mat{$P(Toothache,Cavity,Catch)$} có \mat{$2^3 - 1$} = 7 mục độc lập

Nếu tôi có một khoang, xác suất để đầu dò lọt vào đó
không phụ thuộc vào việc tôi có bị đau răng hay không:
  
  (1) \mat{$P(catch|toothache,cavity) = P(catch|cavity)$}

Tính độc lập tương tự cũng được giữ nếu tôi không có khoang:
  
  (2) \mat{$P(catch|toothache,\lnot cavity) = P(catch|\lnot cavity)$}

\mat{$Catch$} là \defn{độc lập có điều kiện} của \mat{$Toothache$} cho \mat{$Cavity$}:
  
  \mat{$P(Catch|Toothache,Cavity) = P(Catch|Cavity)$}

Báo cáo tương đương:
  
   \mat{$P(Toothache|Catch,Cavity) = P(Toothache|Cavity)$}
  
   \mat{$P(Toothache,Catch|Cavity) = P(Toothache|Cavity)P(Catch|Cavity)$}

---
## Độc lập có điều kiện tiếp theo.

Viết phân phối chung đầy đủ bằng cách sử dụng quy tắc chuỗi:\mat{$n$}
  \mat{$P(Toothache,Catch,Cavity)$}
  
  \mat{${} = P(Toothache|Catch,Cavity) P(Catch,Cavity)$}
  
  \mat{${} = P(Toothache|Catch,Cavity) P(Catch|Cavity)P(Cavity)$}
  
  \mat{${} = P(Toothache|Cavity) P(Catch|Cavity)P(Cavity)$}

Tức là 2 + 2 + 1 = 5 số độc lập (phương trình 1 và 2 loại bỏ 2)

\note{Trong hầu hết các trường hợp, việc sử dụng tính độc lập có điều kiện làm giảm quy mô của
biểu diễn phân phối chung từ hàm mũ trong 

tuyến tính trong \mat{$n$}.}

*Sự độc lập có điều kiện là cơ bản và mạnh mẽ nhất của chúng tôi 

dạng kiến thức về môi trường không chắc chắn.*

---
## Quy tắc Bayes

Quy tắc sản phẩm \mat{$P(a\land b) = P(a|b)P(b) = P(b|a)P(a)$}
\mat{\[
{}\implies \mbox{\defn{Bayes' rule }}  P(a|b) = \frac{P(b|a)P(a)}{P(b)}
\]}
hoặc ở dạng phân phối 
\mat{\[
P(Y|X) = \frac{P(X|Y)P(Y)}{P(X)} = 
  pha P(X|Y)P(Y)
\]}
Hữu ích để đánh giá xác suất \defn{chẩn đoán} từ xác suất \defn{nhân quả}:
\mat{\[
  P(Cause|Effect) = \frac{P(Effect|Cause)P(Cause)}{P(Effect)}
\]}
Ví dụ: đặt \mat{$M$} là viêm màng não, \mat{$S$} là cứng cổ:
\mat{\[
  P(m|s) = \frac{P(s|m)P(m)}{P(s)} = \frac{0.8 \times 0.0001}{0.1} = 0.0008
\]}
Lưu ý: khả năng mắc bệnh viêm màng não sau này vẫn rất nhỏ!

---
## Quy tắc Bayes và tính độc lập có điều kiện

\mat{\begin{eqnarray*}
\lefteqn{P(Cavity|toothache \land catch)}

   & = & 
  pha\, P(toothache\land catch|Cavity) P(Cavity) 

   & = & 
  pha\, P(toothache|Cavity)P(catch|Cavity) P(Cavity) 
\end{eqnarray*}}
Đây là ví dụ về mô hình \defn{naive Bayes}:
\mat{\[
  P(Cause,Effect_1,\ldots,Effect_n) =
       P(Cause)\myprod_i P(Effect_i|Cause)
\]}

,75\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/naive-bayes.png)

Tổng số tham số là *tuyến tính* trong \mat{$n$}

---
## Thế giới Wumpus

,35\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-stuck.png)

\mat{$P_{ij}\eq true$} iff [\mat{$i,j$}] chứa một cái hố

\mat{$B_{ij}\eq true$} nếu [\mat{$i,j$}] trời mát mẻ

Chỉ bao gồm \mat{$B_{1,1},B_{1,2},B_{2,1}$} trong mô hình xác suất

---
## Chỉ định mô hình xác suất

Phân phối chung đầy đủ là \mat{$P(P_{1,1},\ldots,P_{4,4},B_{1,1},B_{1,2},B_{2,1})$}

Áp dụng quy tắc sản phẩm: \mat{$P(B_{1,1},B_{1,2},B_{2,1}\,|\,P_{1,1},\ldots,P_{4,4}) P(P_{1,1},\ldots,P_{4,4})$}

(Làm theo cách này để lấy \mat{$P(Effect|Cause)$}.)

Thuật ngữ đầu tiên: 1 nếu hố tiếp giáp với gió, 0 nếu không

Thuật ngữ thứ hai: các hố được đặt ngẫu nhiên, xác suất 0,2 trên mỗi ô vuông:
\mat{\[
   P(P_{1,1},\ldots,P_{4,4}) = \myprod_{i,j\eq 1,1}^{4,4} P(P_{i,j}) = 0.2^n \stimes 0.8^{16-n}
\]}
cho hố \mat{$n$}.

---
## Quan sát và truy vấn

Chúng tôi biết các sự kiện sau:
  
\mat{$b = \lnot b_{1,1} \land b_{1,2} \land b_{2,1}$}
  
\mat{$known = \lnot p_{1,1} \land \lnot p_{1,2}\land \lnot p_{2,1}$}

Truy vấn là \mat{$P(P_{1,3}|known,b)$}

Xác định \mat{$Unknown$} = \mat{$P_{ij}$}s khác với \mat{$P_{1,3}$} và \mat{$Known$}

Để suy luận bằng cách liệt kê, chúng ta có
\mat{\[
  P(P_{1,3}|known,b) = 
  pha \mysum_{unknown}P(P_{1,3},unknown,known,b)  
\]}
Phát triển theo cấp số nhân với số lượng hình vuông!

---
## Sử dụng tính độc lập có điều kiện

Cái nhìn sâu sắc cơ bản: các quan sát độc lập có điều kiện với
các ô vuông ẩn khác cho các ô vuông ẩn lân cận

,35\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-variables.png)

Xác định \mat{$Unknown = Fringe \cup Other$}

\mat{$P(b|P_{1,3},Known,Unknown) = P(b|P_{1,3},Known,Fringe)$}

Thao tác truy vấn thành một biểu mẫu mà chúng ta có thể sử dụng điều này!

---
## Sử dụng tính độc lập có điều kiện tiếp.

\mat{\begin{eqnarray*}
  \lefteqn{P(P_{1,3}|known,b) = 
  pha \sum_{unknown}P(P_{1,3},unknown,known,b)}

  &=& 
  pha \sum_{unknown}P(b|P_{1,3},known,unknown)P(P_{1,3},known,unknown)

  &=& 
  pha \sum_{fringe}\sum_{other} P(b|known,P_{1,3},fringe,other)P(P_{1,3},known,fringe,other)

  &=& 
  pha \sum_{fringe}\sum_{other} P(b|known,P_{1,3},fringe)P(P_{1,3},known,fringe,other)

  &=& 
  pha \!\sum_{fringe} \!P(b|known,P_{1,3},fringe) \sum_{other}\! P(P_{1,3},known,fringe,other)

  &=&  
  pha \sum_{fringe} P(b|known,P_{1,3},fringe)
       \sum_{other} P(P_{1,3}) P(known)P(fringe)P(other)

  &=&  
  pha\, P(known) P(P_{1,3}) \sum_{fringe}
       P(b|known,P_{1,3},fringe) P(fringe) \sum_{other} P(other)

  &=&  
  pha'\, P(P_{1,3}) \sum_{fringe} P(b|known,P_{1,3},fringe) P(fringe)
\end{eqnarray*}}

---
## Sử dụng tính độc lập có điều kiện tiếp.

![Hình ảnh](../TaiLieu/slide_md/figures/wumpus-fringe-models.png)

\mat{\begin{eqnarray*}
P(P_{1,3}|known,b) 
   &=&  
  pha'\, \< 0.2(0.04 + 0.16 + 0.16),\ 0.8(0.04 + 0.16) \> 

   &\approx& \<0.31,0.69\>

   &&

P(P_{2,2}|known,b)  &\approx&  \<0.86,0.14\>
\end{eqnarray*}}

---
## Tóm tắt

Xác suất là một hình thức luận chặt chẽ đối với tri thức không chắc chắn

\defn{Phân phối xác suất chung} chỉ định xác suất của mọi \defn{sự kiện nguyên tử}

Các truy vấn có thể được trả lời bằng cách tổng hợp các sự kiện nguyên tử

Đối với các miền không cần thiết, chúng ta phải tìm cách giảm kích thước khớp

\defn{Độc lập} và \defn{Độc lập có điều kiện} cung cấp các công cụ