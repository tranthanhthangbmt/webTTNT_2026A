\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Độ bất định (Uncertainty)

## Chương 14

---
## Nội dung

- Default (Uncertainty)

- Xác thực (Xác suất)

- Cú pháp (Cú pháp)

- Ngữ nghĩa (Ngữ nghĩa)

- Các quy tắc suy diễn

---
## Bất định độ 

Cho hành động $A_t$ = trái đi sân bay trước $t$ phút chuyến bay cửa cánh

Liệu $A_t$ có giúp tôi đến đúng giờ không?

Các vấn đề:
  
1) khả năng khảo sát một phần (đường dẫn trạng thái, kế hoạch của tài liệu khác, v.v.)
  
2) cảm biến nhiễu (Báo cáo giao thông thông tin KCBS)
  
3) sự không chắc chắn trong hoạt động kết quả (xịt lốp xe, v.v.)
  
4) sự phức tạp của việc mô hình hóa và giao thông dự kiến

Do đó, một cách tiếp theo logic thuần túy có thể

\phantom{or }1) có nguy cơ sai thật sự: "$A_{25}$ sẽ giúp tôi đến đó đúng giờ"

hoặc 2) dẫn đến các kết luận quá yếu để quyết định:
    
"$A_{25}$ sẽ giúp tôi đến đúng thời điểm nếu không có tai nạn trên cầu
    
và trời không mưa và xe của tôi vẫn còn nguyên v.v. và v.v."

(Có thể nói $A_{1440}$ sẽ giúp tôi đến đúng giờ một cách hợp lý

Nhưng tôi sẽ phải ở lại qua đêm tại sân bay $\ldots$)

---
##  Bất chấp mức độ xử lý phương pháp 

Logic <u>default (Default)</u> hoặc <u>phi đơn điệu (nonmonotonic)</u>:
  
  Giả sử lịch sử của tôi không bị xịt trước
  
  Giả sử $A_{25}$ có tác dụng trừ khi được củng cố bởi bằng chứng 

Vấn đề: Những giả định nào hợp lý? Làm cách nào để xử lý tính nhất quán?

<u> Quy tắc với hệ số fudge (Yếu tố fudge)</u>:
  
$A_{25} \mapsto_{0.3}$ đến đó đúng giờ
  
$Sprinkler \mapsto_{0.99} WetGrass$
  
$WetGrass \mapsto_{0.7} Rain$

Vấn đề: Các mạch rối với sự kết hợp, ví dụ, $Sprinkler$ gây ra $Rain$??

<u>Xác suất (Xác suất)</u>
  
  Dựa trên các bằng chứng có sẵn,
    
    $A_{25}$ sẽ giúp tôi đến đúng thời điểm với xác thực 0.04

Lý thuyết cờ bạc của Mahaviracarya (thế kỷ 9), Cardamo (1565)

(Logic <u>mờ (Fuzzy)</u> xử lý *độ chính xác (mức độ chân lý)* CHỨ KHÔNG PHẢI bất định độ, ví dụ:
  
  $WetGrass$ true ở mức 0,2)

---
## Xác suất (Xác suất)

Các xác nhận hiệu suất ảnh hưởng của 
   *summ Tắt*
  <u> lười biếng (lười biếng)</u>: thất bại trong việc liệt kê các trường hợp ngoại lệ, các điều kiện phụ, v.v.
  
  <u> thiếu hiểu biết (thiếu hiểu biết)</u>: thiếu các sự kiện liên quan, các điều kiện ban đầu, v.v.

Xác thực <u>chủ quan (Subjective)</u> hoặc <u>Bayesian</u>:

Xác thực liên hệ các mệnh đề với trạng thái tri thức của chính một người
    
ví dụ, $P(A_{25} | \mbox{không có tai nạn nào được báo cáo}) = 0.06$

This <u>không</u> phải là các xác nhận về thế giới

Xác minh các mệnh đề thay đổi khi có bằng chứng mới:
    
ví dụ, $P(A_{25} | \mbox{không có tai nạn nào được báo cáo},\ \mbox{5 a.m.}) = 0.15$

(Logic kéo trạng thái tự động $KB \models 
  pha$, chứ không phải sự thật.)

---
## Không quyết định trong điều kiện bất định 

Giả sử tôi tin vào điều sau đây:
\begin{eqnarray*}
P(A_{25}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.04 

P(A_{90}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.70 

P(A_{120}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.95 

P(A_{1440}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.9999 
\end{eqnarray*}
Chọn hành động nào?

Phụ thuộc vào <u> sự ưu tiên (preferences)</u> của tôi đối với việc lỡ chuyến bay so với ẩm thực sân bay, v.v.

<u>Lý thuyết hữu ích (Lý thuyết hữu ích)</u> được sử dụng để biểu diễn và suy diễn các bậc ưu tiên

<u>Lý thuyết quyết định (Lý thuyết quyết định)</u> = lý thuyết hữu ích + lý thuyết xác thực

---
##  Các vật phẩm đầu tiên của màn trình diễn

Với bất kỳ mệnh đề $A$, $B$ nào

1. $0 \leq P(A) \leq 1$

2. $P(True) = 1$ và $P(False) = 0$

3. $P(A \lor B) = P(A) + P(B) - P(A\land B)$

,45\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/axiom3-venn.png)

de Finetti (1931): một tác tử đặt theo phạm vi xác thực
những vấn đề đầu tiên này có thể bị buộc phải đặt số tiền bị mất bất kể kết quả như thế nào.

---
## Cú pháp (Cú pháp)

Tương tự logic mệnh đề: các thế giới có thể được định nghĩa bằng cách phân bổ công việc
giá trị cho các <u> ngẫu nhiên (biến ngẫu nhiên) </u>.

Các biến ngẫu nhiên <u>mệnh đề</u> hoặc <u>Boolean</u>
  
  ví dụ: $Cavity$ (tôi có răng sâu không?)

Bao gồm các biểu thức logic mệnh đề
  
  ví dụ: $\lnot Burglary \lor Earthquake$

Biến ngẫu nhiên <u>nhiều giá trị (Đa giá trị)</u>
  
  ví dụ: $Weather$ is one in $\<sunny,rain,cloudy,snow\>$

Các giá trị phải đầy đủ (đầy đủ) và loại trừ lẫn nhau (loại trừ lẫn nhau)

Mệnh đề được xây dựng bằng cách gán một giá trị:
  
ví dụ: $Weather \eq sunny$; hoặc $Cavity \eq true$ choose clear

---
## Cú pháp (tiếp theo)

Xác thực <u>tiên nghiệm (Prior)</u> hoặc <u>không điều kiện (vô điều kiện)</u> của các mệnh đề
  
  ví dụ: $P(Cavity) = 0.1$ và $P(Weather \eq sunny) = 0.72$

tương ứng với niềm tin trước khi có bất kỳ bằng chứng nào (mới)

<u>Phân phối xác suất (Phân phối xác suất)</u> đưa ra các giá trị cho tất cả các quyền được phân bổ có thể có:
  
  $P(Weather) = \<0.72,0.1,0.08,0.1\>$ (<u>đã chuẩn hóa (chuẩn hóa)</u>,nghĩa là tổng bằng 1)

<u>Phân phối đồng thời (Phân phối xác suất chung)</u> đối với một tập các biến 

các giá trị được phép phân bổ có thể dành cho tất cả các biến
  
  $P(Weather,Cavity)$ = một ma trận giá trị $4 \times 2$:

\[\begin{array}{l|cccc}
\hfil Weather \eq & sunny & rain & cloudy & snow 

\hline
Cavity \eq true & & & & 

Cavity \eq false & & & &
\end{array}\]

<u>Cú pháp (tiếp theo)</u>

Xác thực <u>có điều kiện (Có điều kiện)</u> hoặc <u>hậu nghiệm (sau)</u>
  
  ví dụ: $P(Cavity | Toothache) = 0.8$
  
  nghĩa là, <u>\u{biết rằng $Toothache$ là tất cả những gì tôi biết</u>}

Ký hiệu cho phân phối có điều kiện:
  
  $P(Weather | Earthquake)$ = vector 2 element của vector 4 element

Nếu chúng ta biết nhiều hơn, ví dụ: $Cavity$ cũng được cho trước, thì chúng ta có
  
  $P(Cavity | Toothache,Cavity) = 1$

Lưu ý: niềm tin ít cụ thể hơn *vẫn có giá trị* sau khi có thêm bằng chứng
mới đến, nhưng cũng không phải lúc nào *hữu ích*

Bằng chứng mới có thể không liên quan, cho phép đơn giản hóa, ví dụ:
  
$P(Cavity | Toothache,49ersWin) = P(Cavity | Toothache) = 0.8$

Loại suy diễn này được phê duyệt bởi miền kiến thức là rất quan trọng

---
## Xác suất có điều kiện

Định nghĩa xác thực có điều kiện:
\[
  P(A|B) = \frac{P(A\land B)}{P(B)} \mbox{ nếu } P(B) \neq 0
\]
<u>Quy tắc nhân (Quy tắc sản phẩm)</u> đưa ra một công thức thay thế:
  
  $P(A\land B) = P(A|B)P(B) = P(B|A)P(A)$

Một phiên bản ứng dụng tổng hợp cho toàn bộ phân phối, ví dụ:
  
  $P(Weather,Cavity) = P(Weather|Cavity) P(Cavity)$

(Xem như một tập hợp $4\times 2$ các phương pháp, *không* phải nhân ma trận.)

<u>Quy tắc chuỗi (Quy tắc chuỗi)</u> được suy ra bằng cách áp dụng liên tiếp quy tắc nhân:
  
$P(X_1,\ldots,X_n) = P(X_1,\ldots,X_{n-1})\ 
                        P(X_n | X_1,\ldots,X_{n-1})$
    
                    = $P(X_1,\ldots,X_{n-2})\ 
                        P(X_{n-1} | X_1,\ldots,X_{n-2})\ 
                        P(X_n | X_1,\ldots,X_{n-1})$
    
                  = $\ldots$
    
                  = $\myprod_{i\eq 1}^n P(X_i | X_1,\ldots,X_{i-1})$

---
## Quy tắc Bayes (Quy tắc Bayes)

Quy tắc nhân $P(A\land B) = P(A|B)P(B) = P(B|A)P(A)$
\[
{}\implies \mbox{<u>Quy tắc Bayes </u>}  P(A|B) = \frac{P(B|A)P(A)}{P(B)}
\]
Tại sao điều này lại hữu ích???

Để đánh giá giá xác thực <u>chẩn đoán (chẩn đoán)</u> từ xác thực <u>nhân quả (nhân quả)</u>:
\[
  P(Nguy\hat{e}n\ nh\hat{a}n|K\hat{e}t\ qu\mbox{\`{a}}) = \frac{P(K\hat{e}t\ qu\mbox{\`{a}}|Nguy\hat{e}n\ nh\hat{a}n)P(Nguy\hat{e}n\ nh\hat{a}n)}{P(K\hat{e}t\ qu\mbox{\`{a}})}
\]
Ví dụ, gọi $M$ là viêm loét não, $S$ là cứng cổ:
\[
  P(M|S) = \frac{P(S|M)P(M)}{P(S)} = \frac{0.8 \times 0.0001}{0.1} = 0.0008
\]
Lưu ý:Đặc hậu của bệnh viêm khớp chưa còn rất nhỏ!

---
## Chuẩn hóa (Chuẩn hóa)

Giả sử chúng tôi muốn tính toán hậu quả trên $A$

khi biết $B\eq b$, và giả sử $A$ có thể có các giá trị $a_1 \ldots a_m$

Chúng ta có thể áp dụng quy tắc Bayes cho mỗi giá trị của $A$:
  
  $P(A\eq a_1|B\eq b) = P(B\eq b|A\eq a_1)P(A\eq a_1)/P(B\eq b)$
  
  $\ldots$
  
  $P(A\eq a_m|B\eq b) = P(B\eq b|A\eq a_m)P(A\eq a_m)/P(B\eq b)$

Cộng các giá trị này lại và lưu ý rằng $\mysum_i P(A\eq a_i|B\eq b) = 1$:
\[1/P(B\eq b)  = 1/\mysum_i P(B\eq b|A\eq a_i)P(A\eq a_i)\]
Đây là <u>hệ số chuẩn hóa (hệ số chuẩn hóa)</u>, hằng số theo $i$, được ký hiệu là $
  pha$:
\[
  P(A|B\eq b) = 
  pha P(B\eq b | A)P(A)
\]
Thông thường một phân phối chưa chuẩn hóa, sau đó chuẩn hóa ở cuối
  
  ví dụ: giả sử $P(B\eq b | A)P(A) = \<0.4,0.2,0.2\>$
    
    thì $P(A|B\eq b) = 
  pha \<0.4,0.2,0.2\> 
                        = \frac{\<0.4,0.2,0.2\>}{0.4+0.2+0.2} 
                        = \<0.5,0.25,0.25\>$

---
## Điều kiện hóa (Điều hòa)

Giới thiệu một plugin điều kiện biến thể:
\[
  P(X|Y) = \mysum_z P(X|Y,Z\eq z) P(Z\eq z|Y)
\]
Giác: normal dễ dàng hơn để đánh giá từng trường hợp cụ thể trực quan, ví dụ:

$P(RunOver|Cross)$
  
  = $P(RunOver|Cross,Light\eq green)P(Light\eq green|Cross)$
  
  + $P(RunOver|Cross,Light\eq yellow)P(Light\eq yellow|Cross)$
  
  + $P(RunOver|Cross,Light\eq red)P(Light\eq red|Cross)$

Khi $Y$ vắng mặt, chúng ta có <u> tổng lấy ra (tổng hợp)</u> hoặc <u>lấy biên (marginalization)</u>:
\[
  P(X) = \mysum_z P(X|Z\eq z) P(Z\eq z) = \mysum_z P(X,Z\eq z)
\]
Nói chung, với một phân phối trên một biến, thì
phân phối trên bất kỳ tập tin nào (được gọi là phân phối <u>biên (marginal)</u> vì
lý do lịch sử) có thể được tính toán bằng cách tính tổng các biến khác.

---
## Phân phối đồng thời đầy đủ (Bản phân phối đầy đủ chung)

Một <u>mô tả hoàn thành màn hình xác thực</u>xác định mọi mục nhập trong phân phối
đồng thời cho tất cả các biến $\mbf{X} = X_1,\ldots,X_n$

Nghĩa là, một màn trình diễn cho mỗi thế giới có thể có $X_1\eq x_1,\ldots,X_n\eq x_n$

(So sánh với đầy đủ các lý thuyết trong logic.)

Ví dụ: giả sử $Toothache$ và $Cavity$ là các biến ngẫu nhiên:
\[\begin{array}{l|cc}
 & Toothache\eq true & Toothache\eq false 

\hline
Cavity \eq true  & 0.04 & 0.06 

Cavity \eq false & 0.01 & 0.89
\end{array}\]
Các thế giới có thể được phân loại trừ khi lẫn lộn nhau $\implies$ $P(w_1 \land w_2) = 0$

Các thế giới có thể đủ $\implies$ $w_1 \lor \cdots \lor w_n$ là $True$
    
làm điều đó $\mysum_i P(w_i) = 1$

---
## Phân phối đầy đủ (tiếp theo)

1) Đối với bất kỳ mệnh đề $\phi$ nào được định nghĩa trên các biến ngẫu nhiên
    
   $\phi(w_i)$ là đúng hoặc sai

2) $\phi$ tương đương với việc tuyển dụng $w_i$ khi $\phi(w_i)$ đúng

Làm điều đó $P(\phi) = \mysum_{\{w_i:\ \phi(w_i)\}} P(w_i)$

Nghĩa là, xác thực không điều kiện của bất kỳ mệnh đề nào đều có thể tính được
as a sum of the entry from the full distribution

Xác định điều kiện có thể được tính toán theo một tỷ lệ tương tự:
\[
  P(\phi|\xi) = \frac{P(\phi\land \xi)}{P(\xi)}
\]
Ví dụ: 
\[
  P(Cavity |Toothache) 
   = \frac{P(Cavity \land Toothache)}{P(Toothache)}
   = \frac{0.04}{0.04+0.01} = 0.8
\]

---
## Suy diễn từ các phân phối đồng thời

Thông thường, chúng tôi quan tâm đến 
  
  phân phối hậu kỳ của <u>các truy vấn biến (biến truy vấn)</u> $\mbf{Y}$
  
  cho trước các công cụ giá trị có thể $\mbf{e}$ đối với <u>các biến bằng chứng (biến bằng chứng)</u> $\mbf{E}$

Gọi <u>các biến ẩn (biến ẩn)</u> là $\mbf{H} = \mbf{X} - \mbf{Y} - \mbf{E}$

Khi được phép tính tổng các mục nhập được yêu cầu sẽ được thực hiện bằng cách lấy tổng
ẩn các biến:
\[
P(\mbf{Y}|\mbf{E}\eq \mbf{e}) = 
  pha P(\mbf{Y},\mbf{E}\eq \mbf{e})
= 
  pha \mysum_{\smbf{h}} P(\mbf{Y},\mbf{E}\eq \mbf{e},\mbf{H}\eq \mbf{h})
\]
Tổng số hạng được phép là các mục nhập đồng thời vì $\mbf{Y}$, $\mbf{E}$ và $\mbf{H}$ cùng nhau loại bỏ các biến ngẫu nhiên

Các vấn đề rõ ràng:
  
1) Độ phức tạp thời gian trong trường hợp xấu nhất là $O(d^n)$ trong đó $d$ là số ngôi (arity) lớn nhất
  
2) Độ phức tạp không gian $O(d^n)$ để lưu trữ phân phối đồng thời
  
3) Làm cách nào để tìm các số cho mục $O(d^n)$???