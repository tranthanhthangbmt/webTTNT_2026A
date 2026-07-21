\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Quyết định hợp lý (Rational decisions)

## Chương 16

---
## Phác thảo

- Sở thích hợp lý

- Tiện ích

- Tiền

- Tiện ích đa thuộc tính

- Mạng quyết định

- Giá trị của thông tin

---
### Tùy chọn

Đại lý chọn trong số \defn{giải thưởng} (\mat{$A$}, \mat{$B$}, v.v.) và 
\defn{xổ số}, tức là các tình huống có giải thưởng không chắc chắn

Xổ số \mat{$L = [p,A;\ (1-p),B]$}

 

<img src="../TaiLieu/slide_md/figures/lottery.png" style="width:100%; height:auto;">

Ký hiệu:
  
\mat{$A \pref B$}  &nbsp;&nbsp;&nbsp;&nbsp;  \mat{$A$} được ưu tiên hơn \mat{$B$}
  
\mat{$A \indiff B$}  &nbsp;&nbsp;&nbsp;&nbsp;  sự thờ ơ giữa \mat{$A$} và \mat{$B$} 
  
\mat{$A \prefeq B$}  &nbsp;&nbsp;&nbsp;&nbsp;  \mat{$B$} không được ưu tiên hơn \mat{$A$}

---
## Tùy chọn hợp lý

Ý tưởng: sở thích của một tác nhân hợp lý phải tuân theo các ràng buộc.

Sở thích hợp lý \mat{$\implies$} 
    
   hành vi có thể được mô tả là tối đa hóa tiện ích dự kiến

Các ràng buộc:
  
\underline{Khả năng đặt hàng}
    
\mat{$(A \pref B) \lor (B \pref A) \lor (A \indiff B)$}
  
\underline{Độ chuyển tiếp}
    
\mat{$(A \pref B) \land (B \pref C) \implies (A \pref C)$}
  
\underline{Tính liên tục}
    
\mat{$A \pref B \pref C \implies \Exi{p} [p,A;\ 1-p,C] \indiff B$}
  
\underline{Khả năng thay thế}
    
\mat{$A \indiff B \implies [p,A;\ 1-p,C] \indiff [p,B; 1-p,C]$}
  
\underline{Tính đơn điệu}
    
\mat{$A \pref B \implies (p \geq q \lequiv [p,A;\ 1-p,B] \prefeq [q,A;\ 1-q,B])$}

---
### Tiếp theo là sở thích hợp lý.

Vi phạm các ràng buộc dẫn đến sự phi lý hiển nhiên

Ví dụ: một tác nhân có các ưu tiên nội động
có thể bị xúi giục cho đi tất cả số tiền của mình

Nếu \mat{$B \pref C$} thì đại lý có \mat{$C$}
sẽ trả (giả sử) 1 xu để có được \mat{$B$}

Nếu \mat{$A \pref B$} thì đại lý có \mat{$B$}
sẽ trả (giả sử) 1 xu để có được \mat{$A$}

Nếu \mat{$C \pref A$} thì đại lý có \mat{$A$}
sẽ trả (giả sử) 1 xu để có được \mat{$C$}

 

\  &nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;  <img src="../TaiLieu/slide_md/figures/cash-machine.png" style="width:100%; height:auto;">

---
## Tối đa hóa tiện ích mong đợi

*Định lý* (Ramsey, 1931; von Neumann và Morgenstern, 1944):

Đưa ra các ưu tiên thỏa mãn các ràng buộc

tồn tại hàm có giá trị thực \mat{$U$} sao cho 
    
    \mat{$U(A) \geq U(B)\ \lequiv \ A\prefeq B$}
    
    \mat{$U([p_1,S_1;\ \ldots\ ;\ p_n,S_n]) = \mysum_i\ p_i U(S_i)$}

\defn{Nguyên tắc MEU}:
  
Chọn hành động tối đa hóa hữu dụng mong đợi

Lưu ý: một tác nhân có thể hoàn toàn hợp lý (phù hợp với MEU)

mà không bao giờ đại diện hay thao túng các tiện ích và xác suất

Ví dụ: bảng tra cứu tictactoe hoàn hảo

---
### Tiện ích

Tiện ích ánh xạ trạng thái thành số thực. Những con số nào?

Cách tiếp cận tiêu chuẩn để đánh giá tiện ích con người:
  
  so sánh trạng thái nhất định \mat{$A$} với xổ số tiêu chuẩn \defn{} \mat{$L_p$} có 
    
    "giải thưởng tốt nhất có thể" \mat{$\ubest$} với xác suất \mat{$p$}
    
    "thảm họa tồi tệ nhất có thể xảy ra" \mat{$\uworst$} với xác suất \mat{$(1-p)$}
  
  điều chỉnh xác suất xổ số \mat{$p$} cho đến \mat{$A \indiff L_p$}

<img src="../TaiLieu/slide_md/figures/micromort.png" style="width:100%; height:auto;">

---
## Cân tiện ích

\defn{Tiện ích chuẩn hóa}: \mat{$\ubest = 1.0$}, \mat{$\uworst = 0.0$}

\defn{Micromorts}: khả năng tử vong một phần triệu
  
  hữu ích cho roulette Nga, trả tiền để giảm rủi ro sản phẩm, v.v.

\defn{QALYs}: số năm sống được điều chỉnh theo chất lượng
  
  hữu ích cho các quyết định y tế liên quan đến rủi ro đáng kể

Lưu ý: hành vi là *bất biến* w.r.t. +ve phép biến đổi tuyến tính
\mat{\[
  U'(x) = k_1 U(x) + k_2  &nbsp;&nbsp; \mbox{where } k_1 > 0
\]}
Chỉ với các giải thưởng xác định (không có lựa chọn xổ số), chỉ

\defn{Tiện ích thứ tự} có thể được xác định, tức là tổng thứ tự các giải thưởng

---
### Tiền

Tiền không *không* hoạt động như một chức năng tiện ích

Cho một xổ số \mat{$L$} với giá trị tiền tệ dự kiến \mat{$EMV(L)$},

thường \mat{$U(L) < U(EMV(L))$}, tức là mọi người \defn{không thích rủi ro}

Đường cong hữu dụng: với xác suất \mat{$p$} tôi bàng quan giữa\
giải thưởng \mat{$x$} và xổ số \mat{$[p,{\DollarSign}M;\ (1-p),{\DollarSign}0]$} lớn \mat{$M$}?

Dữ liệu thực nghiệm điển hình, được ngoại suy với hành vi \defn{dễ xảy ra rủi ro}:

<img src="../TaiLieu/slide_md/figures/beard-utility.png" style="width:100%; height:auto;">

---
### Tiện ích nhóm sinh viên

Với mỗi \mat{$x$}, điều chỉnh \mat{$p$} cho đến khi một nửa lớp bỏ phiếu xổ số (M=10.000)

<img src="../TaiLieu/slide_md/figures/student-utility.png" style="width:100%; height:auto;">

---
### Mạng quyết định

Thêm \defn{nút hành động} và \defn{nút tiện ích} vào mạng niềm tin

để cho phép đưa ra quyết định hợp lý

<img src="../TaiLieu/slide_md/figures/airport-id.png" style="width:100%; height:auto;">

Thuật toán:
  
  Đối với mỗi giá trị của nút hành động 
    
    tính toán giá trị kỳ vọng của nút tiện ích cho trước hành động, bằng chứng
  
  Trả lại hành động MEU

---
## Tiện ích đa thuộc tính

Làm cách nào chúng ta có thể xử lý các hàm tiện ích của nhiều biến \mat{$X_1\ldots X_n$}?

Ví dụ: \mat{$U(Deaths,Noise,Cost)$} là gì?

Làm thế nào có thể đánh giá các chức năng tiện ích phức tạp từ 

hành vi ưu tiên?

Ý tưởng 1: xác định các điều kiện theo đó các quyết định có thể được đưa ra mà không cần
nhận dạng đầy đủ của \mat{$U(x_1,\ldots,x_n)$}

Ý tưởng 2: xác định các loại *độc lập* trong preferences

và rút ra các dạng kinh điển cho \mat{$U(x_1,\ldots,x_n)$}

---
### Sự thống trị nghiêm ngặt

Thông thường xác định các thuộc tính sao cho \mat{$U$} là \defn{đơn điệu} trong mỗi thuộc tính

\defn{Sự thống trị nghiêm ngặt}: sự lựa chọn \mat{$B$} sự thống trị nghiêm ngặt sự lựa chọn \mat{$A$} iff
    
\mat{$\All{i} X_i(B) \geq X_i(A)$}  &nbsp;&nbsp;  (và do đó \mat{$U(B) \geq U(A)$})

<img src="../TaiLieu/slide_md/figures/strict-dominance.png" style="width:100%; height:auto;">

Sự thống trị chặt chẽ hiếm khi được áp dụng trong thực tế

---
## Sự thống trị ngẫu nhiên

\twograph{graphs/dominance-density.ps}{graphs/dominance-cumulative.ps}

Phân phối \mat{$p_1$} \defn{chi phối ngẫu nhiên} phân phối \mat{$p_2$} iff
    
  \mat{$\displaystyle\All{t} \int_{-\infty}^t p_1(x)dx \leq \int_{-\infty}^t p_2(t)dt$}

Nếu \mat{$U$} đơn điệu trong \mat{$x$} thì \mat{$A_1$} với phân phối kết quả \mat{$p_1$}

chiếm ưu thế một cách ngẫu nhiên \mat{$A_2$} với phân phối kết quả \mat{$p_2$}:
    
  \mat{$\displaystyle\int_{-\infty}^{\infty} p_1(x) U(x)dx \geq \int_{-\infty}^{\infty} p_2(x) U(x)dx $}

Trường hợp đa thuộc tính: sự thống trị ngẫu nhiên trên tất cả các thuộc tính \mat{$\implies$} tối ưu

---
## Tiếp theo sự thống trị ngẫu nhiên.

Sự thống trị ngẫu nhiên thường có thể được xác định mà không cần 

phân phối chính xác bằng cách sử dụng lý luận *định tính*

Ví dụ: chi phí xây dựng tăng theo khoảng cách từ thành phố
    
      \mat{$S_1$} gần thành phố hơn \mat{$S_2$}
  
  \mat{$\implies$} \mat{$S_1$} chiếm ưu thế một cách ngẫu nhiên \mat{$S_2$} về chi phí

Ví dụ: thương tích tăng theo tốc độ va chạm

Có thể chú thích mạng lưới niềm tin với thông tin thống trị ngẫu nhiên:
  
  \mat{$X \qplus Y$} (\mat{$X$} ảnh hưởng tích cực đến \mat{$Y$}) có nghĩa là 
  
  Đối với mọi giá trị \mat{$\mbf{z}$} của cha mẹ khác của \mat{$Y$} \mat{$\mbf{Z}$} 
    
    \mat{$\All{x_1,x_2} x_1 \geq x_2 \implies
      P(Y|x_1,\mbf{z})$} chiếm ưu thế ngẫu nhiên \mat{$ P(Y|x_2,\mbf{z})$}

---
### Gán nhãn các cung + hoặc --

<img src="../TaiLieu/slide_md/figures/insurance-qpn01.png" style="width:100%; height:auto;">

---
### Gán nhãn các cung + hoặc --

<img src="../TaiLieu/slide_md/figures/insurance-qpn02.png" style="width:100%; height:auto;">

---
### Gán nhãn các cung + hoặc --

<img src="../TaiLieu/slide_md/figures/insurance-qpn03.png" style="width:100%; height:auto;">

---
### Gán nhãn các cung + hoặc --

<img src="../TaiLieu/slide_md/figures/insurance-qpn04.png" style="width:100%; height:auto;">

---
### Gán nhãn các cung + hoặc --

<img src="../TaiLieu/slide_md/figures/insurance-qpn05.png" style="width:100%; height:auto;">

---
### Gán nhãn các cung + hoặc --

<img src="../TaiLieu/slide_md/figures/insurance-qpn06.png" style="width:100%; height:auto;">

---
## Cấu trúc ưu tiên: Xác định

\mat{$X_1$} và \mat{$X_2$} \defn{tốt nhất là độc lập} của \mat{$X_3$} iff
  
  ưu tiên giữa \mat{$\< x_1,x_2,x_3 \>$} và \mat{$\< x_1',x_2',x_3 \>$}
  
  không phụ thuộc vào \mat{$x_3$}

Ví dụ: \mat{$\<Noise,Cost,Safety\>$}:
  
  \mat{$\<$}20.000 người bị ảnh hưởng, {\DollarSign}4,6 tỷ, 0,06 người chết/mpm\mat{$\>$} so với
  
  \mat{$\<$}70.000 người bị ảnh hưởng, {\DollarSign}4,2 tỷ, 0,06 người chết/mpm\mat{$\>$}

*Định lý* (Leontief, 1947): nếu mọi cặp thuộc tính là P.I. phần bổ sung của nó,
thì mọi tập hợp con của các thuộc tính là P.I của phần bù của nó: \defn{P.I tương hỗ }.

*Định lý* (Debreu, 1960): P.I. Hàm giá trị \mat{$\implies$} \mat{$\exists$} \defn{additive}:
\mat{\[
  V(S) = \mysum_i V_i(X_i(S))
\]}
Do đó đánh giá các hàm thuộc tính đơn \mat{$n$}; thường là một xấp xỉ tốt

---
## Cấu trúc ưu tiên: Stochastic

Cần cân nhắc ưu tiên so với xổ số:

\mat{$\mbf{X}$} là \defn{không phụ thuộc vào tiện ích} của \mat{$\mbf{Y}$} iff
  
  sở thích về xổ số trong \mat{$\mbf{X}$} không phụ thuộc vào \mat{$\mbf{y}$}

Giao diện người dùng tương hỗ: mỗi tập hợp con là giao diện người dùng của phần bổ sung của nó

\mat{$\implies$} \mat{$\exists$} \defn{hàm tiện ích nhân }: 
  
\mat{$U  =  k_1U_1 + k_2U_2 + k_3U_3$}
    
 + \mat{$k_1k_2U_1U_2 + k_2k_3U_2U_3 + k_3k_1U_3U_1$}
    
 + \mat{$k_1k_2k_3U_1U_2U_3$}

Các thủ tục thông thường và gói phần mềm để tạo ưu tiên
kiểm tra để xác định các họ chức năng tiện ích chính tắc khác nhau

---
## Giá trị của thông tin

Ý tưởng: tính toán giá trị của việc thu thập từng bằng chứng có thể có 

Có thể được thực hiện *trực tiếp từ mạng quyết định*

Ví dụ: mua quyền khoan dầu
  
  Hai khối \mat{$A$} và \mat{$B$}, đúng một khối có dầu, trị giá \mat{$k$}
  
  Xác suất trước 0,5 mỗi xác suất, loại trừ lẫn nhau
  
  Giá hiện tại mỗi block là \mat{$k/2$}
  
  "Tư vấn" đưa ra khảo sát chính xác về \mat{$A$}. Giá hợp lý?

Giải pháp: tính giá trị dự kiến của thông tin
  
  = giá trị mong đợi của hành động tốt nhất dựa trên thông tin
    
    trừ giá trị mong đợi của hành động tốt nhất không có thông tin

Khảo sát có thể cho biết " dầu ở A " hoặc " không có dầu ở A ", *vấn đề. 0,5 mỗi cái* (đã cho!)
  
  = [\mat{$0.5 \times {}$} giá trị của "mua A" cho "dầu ở A"
    
    + \mat{$0.5 \times {}$} giá trị "mua B" cho "không có dầu ở A"]
    
    -- 0
  
  = \mat{$(0.5 \times k/2) + (0.5 \times k/2) - 0 = k/2$}

---
## Công thức tổng quát

Bằng chứng hiện tại \mat{$E$}, hành động tốt nhất hiện tại \mat{$
  pha$} 

Kết quả hành động có thể xảy ra \mat{$S_i$}, bằng chứng mới tiềm năng \mat{$E_j$}
\mat{\[
  EU(
  pha|E) = \max_{a} \mysum_i\ U(S_i)\;P(S_i|E,a)
\]}
Giả sử chúng ta biết \mat{$E_j \eq e_{jk}$} thì chúng ta sẽ chọn \mat{$
  pha_{e_{jk}}$} s.t.
\mat{\[
  EU(
  pha_{e_{jk}}|E,E_j \eq e_{jk}) = \max_a \mysum_i\ U(S_i)\;P(S_i|E,a,E_j \eq e_{jk})
\]}
\mat{$E_j$} là một biến ngẫu nhiên có giá trị là {\it now} known

\mat{$\implies$} phải tính toán mức tăng dự kiến trên tất cả các giá trị có thể có:
\mat{\[
VPI_{E}(E_j) = \left(\mysum_k\ P(E_j \eq e_{jk}|E)
EU(
  pha_{e_{jk}}|E,E_j \eq e_{jk})\right) - EU(
  pha|E) 
\]}
(VPI = giá trị thông tin hoàn hảo)

---
## Tính chất của VPI

*Không âm*---trong *kỳ vọng*, không phải *post hoc*
\mat{\[
\All{j,E} VPI_{E}(E_j)\geq 0\
\]}
*Không phụ gia*---xem xét, ví dụ: nhận được \mat{$E_j$} hai lần
\mat{\[
VPI_{E}(E_j,E_k) \not= VPI_{E}(E_j) + VPI_{E}(E_k)
\]}
*Không phụ thuộc vào đơn hàng*
\mat{\[
VPI_{E}(E_j,E_k) = VPI_{E}(E_j) + VPI_{E,E_j}(E_k)
                   = VPI_{E}(E_k) + VPI_{E,E_k}(E_j) 
\]}
Lưu ý: khi có thể thu thập được nhiều bằng chứng,

tối đa hóa VPI cho mỗi người chọn một không phải lúc nào cũng tối ưu

\mat{$\implies$} thu thập bằng chứng trở thành vấn đề quyết định *tuần tự*

---
### Hành vi định tính

a) Sự lựa chọn là hiển nhiên, thông tin có giá trị rất ít

b) Sự lựa chọn là không rõ ràng, thông tin có giá trị rất nhiều

c) Sự lựa chọn không rõ ràng, thông tin ít có giá trị

 

<img src="../TaiLieu/slide_md/figures/3cases.png" style="width:100%; height:auto;">