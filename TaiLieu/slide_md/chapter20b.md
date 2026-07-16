\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Mạng nơ-ron (Neural networks)

## Chương 20, Phần 5

---
## Phác thảo

- Bộ não

- Mạng lưới thần kinh

- Perceptron

- Perceptron nhiều lớp

- Ứng dụng của mạng nơ-ron

---
## Bộ não

\mat{$10^{11}$} tế bào thần kinh thuộc loại \mat{${}> 20$}, khớp thần kinh \mat{$10^{14}$}, thời gian chu kỳ 1ms--10ms

Tín hiệu ồn ào 'đoàn tàu gai' của điện thế

![Hình ảnh](../TaiLieu/slide_md/figures/neuron.png)

---
## McCulloch--Pitts "đơn vị"

Đầu ra là hàm tuyến tính " bị nén " của các đầu vào:
\mat{\[
a_i \leftarrow g(in_i) = g\left(\mysum_j \w{j}{i} a_j\right)
\]}

[Hình ảnh: \fig{figures/neuron-unit.eps}]

Sự đơn giản hóa quá mức của các nơ-ron thực, nhưng mục đích của nó là

để phát triển sự hiểu biết về những gì mạng lưới các đơn vị đơn giản có thể làm

---
## Chức năng kích hoạt

[Hình ảnh: \fig{figures/activation-fns.eps}]

(a) là hàm bước \defn{} hoặc \defn{hàm ngưỡng }

(b) là hàm \defn{sigmoid} \mat{$1/(1+e^{-x})$}

Thay đổi trọng số thiên vị \mat{$\w{0}{i}$} sẽ di chuyển vị trí ngưỡng

---
## Thực hiện các hàm logic

[Hình ảnh: \fig{figures/nn-logical.eps}]

McCulloch và Pitts: mọi hàm Boolean đều có thể được triển khai

---
## Cấu trúc mạng

\defn{Mạng chuyển tiếp nguồn cấp dữ liệu}:
  
-- \note{perceptron một lớp}
  
-- \note{perceptron nhiều lớp}

Mạng chuyển tiếp nguồn cấp dữ liệu thực hiện các chức năng, không có trạng thái nội bộ

\defn{Mạng định kỳ}:
  
-- \note{Mạng Hopfield} có trọng số đối xứng (\mat{$\w{i}{j} = \w{j}{i}$})
    
   \mat{$g(x)\eq \mbox{sign}(x)$}, \mat{$a_i\eq \pm 1$}; *bộ nhớ kết hợp ba chiều*
  
-- \note{Máy Boltzmann} sử dụng hàm kích hoạt ngẫu nhiên, 
    
   $\approx$ MCMC trong mạng Bayes
  
-- mạng lưới thần kinh tái phát có chu kỳ định hướng với độ trễ
    
  $\implies$ có trạng thái bên trong (như flip-flop), có thể dao động, v.v.

---
## Ví dụ về chuyển tiếp nguồn cấp dữ liệu

![Hình ảnh](../TaiLieu/slide_md/figures/neural-net.png)

Mạng chuyển tiếp nguồn cấp dữ liệu = một họ các hàm phi tuyến được tham số hóa:
\mat{\begin{eqnarray*}
a_5 & = & g(\w{3}{5}\cdot a_3 + \w{4}{5}\cdot a_4) \nonumber 

    & = & g(\w{3}{5}\cdot g(\w{1}{3}\cdot a_1 + \w{2}{3}\cdot a_2) + 
              \w{4}{5}\cdot g(\w{1}{4}\cdot a_1 + \w{2}{4}\cdot a_2)) 
\end{eqnarray*}}
Việc điều chỉnh trọng lượng sẽ thay đổi chức năng: hãy học theo cách này!

---
## Perceptron một lớp

\twofig{figures/perceptron.ps}{graphs/perceptron-model.eps}

Tất cả các đơn vị đầu ra đều hoạt động riêng biệt---không có trọng lượng chung

Việc điều chỉnh trọng lượng sẽ di chuyển vị trí, hướng và độ dốc của vách đá

---
## Tính biểu cảm của perceptron

Hãy xem xét một perceptron có \mat{$g$} = hàm bước (Rosenblatt, 1957, 1960)

Có thể biểu thị AND, OR, NOT, đa số, v.v., nhưng không thể biểu thị XOR

Biểu thị dấu phân cách tuyến tính \defn{} trong không gian đầu vào:
\mat{\[
\mysum_j W_j x_j > 0  &nbsp;&nbsp; \mbox{or} &nbsp;&nbsp;  \mbf{W} \cdot \mbf{x} > 0
\]}

[Hình ảnh: \fig{figures/perceptron-linear.eps}]

Minsky \& Papert (1969) chọc thủng quả bóng mạng lưới thần kinh

---
## Học Perceptron

Tìm hiểu bằng cách điều chỉnh trọng số để giảm \defn{lỗi} trên tập huấn luyện

\defn{lỗi bình phương} trong ví dụ với đầu vào \(\x\) và
đầu ra thực sự \(y\) là 
\mat{\[
  E = \frac{1}{2}\J{Err}^2  \equiv \frac{1}{2}(y-h_{\smbf{W}}(\x))^2\ ,
\]}
Thực hiện tìm kiếm tối ưu hóa bằng cách giảm độ dốc:
\mat{\begin{eqnarray*}
\frac{\partial E}{\partial W_j} 
   &=& \J{Err} \stimes \frac{\partial \J{Err}}{\partial W_j} 
   = \J{Err} \stimes \frac{\partial}{\partial W_j}
           \left(y - g(\mysum_{j\eq 0}^n W_j x_j) \right)

   &=& - \J{Err} \stimes g'(\J{in}) \stimes x_j 
\end{eqnarray*}}
Quy tắc cập nhật trọng lượng đơn giản:
\mat{\[
W_j \leftarrow W_j + 
  pha \stimes \J{Err} \stimes g'(\J{in}) \stimes x_j
\]}
Ví dụ: +ve lỗi \mat{$\implies$} tăng đầu ra mạng 

\mat{$\implies$} tăng trọng số trên đầu vào +ve, giảm trên -ve đầu vào

---
## Tiếp tục học Perceptron.

Quy tắc học Perceptron hội tụ về một hàm nhất quán

*cho mọi tập dữ liệu có thể phân tách tuyến tính *

\twofig{graphs/majority-perceptron+dtl-curve.eps}{graphs/nhà hàng-perceptron+dtl-curve.eps}

Perceptron học hàm đa số dễ dàng, DTL vô vọng

DTL học chức năng nhà hàng dễ dàng, perceptron không thể biểu diễn được

---
## Bộ cảm biến nhiều lớp

Các lớp thường được kết nối đầy đủ;

số lượng \defn{đơn vị ẩn} thường được chọn bằng tay

[Hình ảnh: \fig{figures/restaurant-nn.eps}]

---
## Tính biểu cảm của MLP

Tất cả các chức năng liên tục có 2 lớp, tất cả các chức năng có 3 lớp

\twofig{graphs/nn-ridge.eps}{graphs/nn-bump.eps}

Kết hợp hai hàm ngưỡng đối diện nhau để tạo thành một đường gờ

Kết hợp hai đường gờ vuông góc để tạo thành một vết lồi

Thêm các va chạm có kích thước và vị trí khác nhau để phù hợp với mọi bề mặt

Bằng chứng yêu cầu nhiều đơn vị ẩn theo cấp số nhân (xem bằng chứng DTL)

---
## Học lan truyền ngược

Lớp đầu ra: giống như perceptron một lớp,
\mat{\[
  \w{j}{i} \leftarrow \w{j}{i} + 
  pha \times a_j \times \Delta_i
\]}
ở đâu \mat{$\Delta_i \eq \J{Err}{}_i \times g'(\J{in}{}_i)$}

Lớp ẩn: *truyền ngược* lỗi từ lớp đầu ra:
\mat{\[
   \Delta_j = g'(\J{in}{}_j) \sum_i \w{j}{i} \Delta_i\ .
\]}
Cập nhật quy tắc cho trọng số trong lớp ẩn:
\mat{\[ \w{k}{j} \leftarrow \w{k}{j} +
 
  pha \times a_k \times \Delta_j\ .
\]}
(Hầu hết các nhà thần kinh học đều phủ nhận rằng hiện tượng lan truyền ngược xảy ra trong não)

---
## Đạo hàm lan truyền ngược

Lỗi bình phương trên một ví dụ được định nghĩa là
\mat{\[ E = \frac{1}{2} \sum_i (y_i - a_i)^2\ , \]}
trong đó tổng bằng các nút trong lớp đầu ra.
\mat{\begin{eqnarray*}
\frac{\partial E}{\partial \w{j}{i}} 
  & = & - (y_i - a_i) \frac{\partial a_i}{\partial \w{j}{i}} 
      = - (y_i - a_i) \frac{\partial g(\J{in}{}_i)}{\partial \w{j}{i}} 

  & = & - (y_i - a_i) g'(\J{in}{}_i)\frac{\partial \J{in}{}_i}{\partial \w{j}{i}}
      = - (y_i - a_i) g'(\J{in}{}_i)\frac{\partial}{\partial\w{j}{i}}\left(\sum_j\w{j}{i} a_j \right) 

  & = & - (y_i - a_i) g'(\J{in}{}_i) a_j = - a_j \Delta_i
\end{eqnarray*}}

---
## Đạo hàm lan truyền ngược tiếp theo.

\mat{\begin{eqnarray*}
\frac{\partial E}{\partial \w{k}{j}} 
  & = & - \sum_i (y_i - a_i) \frac{\partial a_i}{\partial \w{k}{j}} 
      = - \sum_i (y_i - a_i) \frac{\partial g(\J{in}{}_i)}{\partial \w{k}{j}} 

  & = & - \sum_i (y_i - a_i) g'(\J{in}{}_i)\frac{\partial \J{in}{}_i}{\partial \w{k}{j}}
      = - \sum_i \Delta_i\frac{\partial}{\partial\w{k}{j}}\left(\sum_j\w{j}{i} a_j \right) 

  & = & - \sum_i \Delta_i \w{j}{i} \frac{\partial a_j}{\partial\w{k}{j}}
      = - \sum_i \Delta_i \w{j}{i} \frac{\partial g(\J{in}{}_j)}{\partial\w{k}{j}} 

  & = & - \sum_i \Delta_i \w{j}{i} g'(\J{in}{}_j)\frac{\partial \J{in}{}_j}{\partial \w{k}{j}}

  & = & - \sum_i \Delta_i \w{j}{i} g'(\J{in}{}_j)\frac{\partial}{\partial \w{k}{j}}\left(\sum_k\w{k}{j} a_k \right) 

  & = & - \sum_i \Delta_i \w{j}{i} g'(\J{in}{}_j) a_k = - a_k \Delta_j
\end{eqnarray*}}

---
## Tiếp tục học lan truyền ngược

Tại mỗi \defn{epoch}, tính tổng các cập nhật gradient cho tất cả các mẫu và áp dụng

\defn{Đường cong đào tạo} cho 100 ví dụ về nhà hàng: tìm thấy sự phù hợp chính xác

[Hình ảnh: \fig{graphs/restaurant-back-prop-error.eps}]

Các vấn đề điển hình: hội tụ chậm, cực tiểu cục bộ

---
## Tiếp tục học lan truyền ngược

Đường cong học tập cho MLP với 4 đơn vị ẩn:

[Hình ảnh: \fig{graphs/restaurant-back-prop+dtl-curve.eps}]

MLP khá tốt cho các nhiệm vụ nhận dạng mẫu phức tạp,

nhưng các giả thuyết dẫn đến không thể được hiểu một cách dễ dàng

---
## Nhận dạng chữ số viết tay

\framebox[\textwidth]{
{figures/easy21c.eps}}
\framebox{\epsfflex{0.095}{figures/easy23c.eps}}
\framebox{\epsfflex{0.095}{figures/easy16c.eps}}
\framebox{\epsfflex{0.095}{figures/easy12c.eps}}
\framebox{\epsfflex{0.095}{figures/easy20c.eps}}
\framebox{\epsfflex{0.095}{figures/easy35c.eps}}
\framebox{\epsfflex{0.095}{figures/easy13c.eps}}
\framebox{\epsfflex{0.095}{figures/easy29c.eps}}
\framebox{\epsfflex{0.095}{figures/easy17c.eps}}
\framebox{\epsfflex{0.095}{figures/easy19c.eps}
[6pt]
\framebox{\epsfflex{0.095}{figures/hard53c.eps}}
\framebox{\epsfflex{0.095}{figures/hard04c.eps}}
\framebox{\epsfflex{0.095}{figures/hard20c.eps}}
\framebox{\epsfflex{0.095}{figures/hard13c.eps}}
\framebox{\epsfflex{0.095}{figures/hard01c.eps}}
\framebox{\epsfflex{0.095}{figures/hard10c.eps}}
\framebox{\epsfflex{0.095}{figures/hard34c.eps}}
\framebox{\epsfflex{0.095}{figures/hard52c.eps}}
\framebox{\epsfflex{0.095}{figures/hard05c.eps}}
\framebox{\epsfflex{0.095}{figures/hard14c.eps}}}
}

3-hàng xóm gần nhất = lỗi 2,4\% 

400--300--10 đơn vị MLP = lỗi 1,6\%

LeNet: 768--192--30--10 đơn vị MLP = lỗi 0,9\%

Tốt nhất hiện nay (máy hạt nhân, thuật toán thị giác) $\approx$ lỗi 0,6\%

---
## Tóm tắt

Hầu hết bộ não đều có rất nhiều tế bào thần kinh; mỗi nơron $\approx$ đơn vị ngưỡng tuyến tính (?)

Perceptron (mạng một lớp) không đủ biểu cảm

Mạng nhiều lớp có đủ biểu cảm; có thể được đào tạo bởi 
giảm độ dốc, tức là lan truyền ngược lỗi

Nhiều ứng dụng: nói, lái xe, viết tay, phát hiện gian lận, v.v.

Kỹ thuật, mô hình nhận thức và mô hình hệ thống thần kinh

các trường con phần lớn đã chuyển hướng