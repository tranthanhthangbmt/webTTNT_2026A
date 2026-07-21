# Chapter 27 Computer Vision

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_27_Computer%20Vision/chapter_27_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_27_Computer%20Vision.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Thị giác máy tính (Vision)

## Chương 24

---
## Phác thảo

- Nhận thức chung

- Sự hình thành hình ảnh

- Tầm nhìn sớm

- 2D \mat{$\rightarrow$} 3D

- Nhận dạng đối tượng

---
## Nhận thức chung

\defn{Kích thích} (nhận thức) \mat{$S$}, Thế giới \mat{$W$}
\mat{\[
  S = g(W)
\]}
Ví dụ: \mat{$g$} = "graphics." Chúng ta có thể thực hiện tầm nhìn như đồ họa nghịch đảo không?
\mat{\[
  W = g^{-1}(S)
\]}

---
### Nhận thức chung

\defn{Kích thích} (nhận thức) \mat{$S$}, Thế giới \mat{$W$}
\mat{\[
  S = g(W)
\]}
Ví dụ: \mat{$g$} = "graphics." Chúng ta có thể thực hiện tầm nhìn như đồ họa nghịch đảo không?
\mat{\[
  W = g^{-1}(S)
\]}
Vấn đề: sự mơ hồ lớn!

<img src="../TaiLieu/slide_md/figures/lecture-scene1.png" style="width:100%; height:auto;">

---
### Nhận thức chung

\defn{Kích thích} (nhận thức) \mat{$S$}, Thế giới \mat{$W$}
\mat{\[
  S = g(W)
\]}
Ví dụ: \mat{$g$} = "graphics." Chúng ta có thể thực hiện tầm nhìn như đồ họa nghịch đảo không?
\mat{\[
  W = g^{-1}(S)
\]}
Vấn đề: sự mơ hồ lớn!

<img src="../TaiLieu/slide_md/figures/lecture-scene2.png" style="width:100%; height:auto;">

---
### Nhận thức chung

\defn{Kích thích} (nhận thức) \mat{$S$}, Thế giới \mat{$W$}
\mat{\[
  S = g(W)
\]}
Ví dụ: \mat{$g$} = "graphics." Chúng ta có thể thực hiện tầm nhìn như đồ họa nghịch đảo không?
\mat{\[
  W = g^{-1}(S)
\]}
Vấn đề: sự mơ hồ lớn!

<img src="../TaiLieu/slide_md/figures/lecture-scene3.png" style="width:100%; height:auto;">

---
## Phương pháp tiếp cận tốt hơn

Suy luận Bayes về cấu hình thế giới:
\mat{\[
  P(W|S) = 
  pha \underbrace{P(S|W)}_{\mbox{"graphics"}} &nbsp;&nbsp;  \underbrace{P(W)}_{\mbox{"prior knowledge"}}
\]}
Vẫn còn tốt hơn: không cần phải khôi phục cảnh chính xác!

Chỉ cần trích xuất thông tin cần thiết cho 
  
 -- \defn{điều hướng}
  
 -- \defn{thao tác}
  
 -- \defn{nhận dạng/nhận dạng}

---
### Vision "hệ thống con"

<img src="../TaiLieu/slide_md/figures/vision-subsystems.png" style="width:100%; height:auto;">

Tầm nhìn đòi hỏi phải kết hợp nhiều tín hiệu

---
### Hình thành hình ảnh

,75\textwidth
<img src="../TaiLieu/slide_md/figures/pinhole.png" style="width:100%; height:auto;">

\mat{$P$} là một điểm trong cảnh, có tọa độ \mat{$ (X,Y,Z)$}

\mat{$P'$} là ảnh của nó trên mặt phẳng ảnh, có tọa độ \mat{$ (x,y,z)$}
\mat{\[x=\frac{-fX}{Z},\ y=\frac{-fY}{Z}  \]}
bằng các tam giác đồng dạng. Tỷ lệ/khoảng cách là không xác định!
  

---
### Hình ảnh

,85\textwidth
<img src="../TaiLieu/slide_md/figures/stapler1+square.png" style="width:100%; height:auto;">

---
## Hình ảnh tiếp theo.

\twofig{figures/pixels-12x12.ps}{figures/pixel-values.ps}

\mat{$I(x,y,t)$} là cường độ tại \mat{$(x,y)$} tại thời điểm \mat{$t$}

Máy ảnh CCD \mat{$\approx$} 1.000.000 pixel; mắt người \mat{$\approx$} 240.000.000 pixel

tức là 0,25 terabit/giây

---
### Tầm nhìn màu sắc

Cường độ thay đổi theo tần số \mat{$\rightarrow$} tín hiệu vô chiều

,65\textwidth
<img src="../TaiLieu/slide_md/figures/color-vision.png" style="width:100%; height:auto;">

Mắt người có ba loại tế bào nhạy cảm với màu sắc;

mỗi tín hiệu tích hợp cường độ vectơ 3 phần tử \mat{$\implies$}

---
### Phát hiện cạnh

,7\textwidth
<img src="../TaiLieu/slide_md/figures/edge-test.png" style="width:100%; height:auto;">

Các cạnh trong ảnh \mat{$\Leftarrow$} sự gián đoạn trong cảnh:
  
1) độ sâu
  
2) hướng bề mặt
  
3) độ phản xạ (dấu hiệu bề mặt)
  
4) chiếu sáng (bóng tối, v.v.)

---
### Tiếp tục phát hiện cạnh

1) Kết hợp hình ảnh với các bộ lọc định hướng không gian (có thể đa tỷ lệ)
\mat{\[
  E_{\theta}(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{\theta}(u,v) I(x+u,y+v)\,du\,dv
\]}

,75\textwidth
<img src="../TaiLieu/slide_md/figures/spatially-oriented-filters.png" style="width:100%; height:auto;">

2) Gắn nhãn các pixel trên ngưỡng với hướng cạnh

3) Suy ra các đoạn đường "sạch" bằng cách kết hợp các pixel cạnh có cùng hướng

,5\textwidth
<img src="../TaiLieu/slide_md/figures/edgels.png" style="width:100%; height:auto;">

  

---
## Tín hiệu từ kiến thức trước đây

| &nbsp; | &nbsp; |
|---|---|
| {\bf Hình dạng từ\mat{$\ldots$} | {\bf Giả sử} |
| \chuyển động đỉnh và vật rắn, chuyển động liên tục |
| âm thanh nổi | khối liền kề, không lặp lại |
| kết cấu | kết cấu đồng đều |
| bóng và phản xạ đồng đều |
| đường viền | độ cong tối thiểu |

---
### Chuyển động

<img src="../TaiLieu/slide_md/figures/00.png" style="width:100%; height:auto;">

,3\textwidth
 <img src="../TaiLieu/slide_md/figures/00.png" style="width:100%; height:auto;"> 
<img src="../TaiLieu/slide_md/figures/flow.png" style="width:100%; height:auto;">
,3\textwidth
<img src="../TaiLieu/slide_md/figures/19.png" style="width:100%; height:auto;">

,4\textwidth
<img src="../TaiLieu/slide_md/figures/flow.png" style="width:100%; height:auto;">

---
### Âm thanh nổi

,85\textwidth
<img src="../TaiLieu/slide_md/figures/stereo-pyramid.png" style="width:100%; height:auto;">

---
### Độ phân giải độ sâu âm thanh nổi 

<img src="../TaiLieu/slide_md/figures/stereopsis.png" style="width:100%; height:auto;">

Hình học đơn giản: \mat{$\delta Z = Z^2 \delta \theta/(-b)$}

Sinh lý học: \mat{$\delta\theta \geq 2.42\times 10^{-5}$} radian, \mat{$b\eq 6$}cm

\mat{$Z\eq 30$}cm \mat{$\implies \delta Z \approx 0.04$}mm

\mat{$Z\eq 30$}m \mat{$\implies \delta Z \approx 40$}cm

Đường cơ sở lớn \mat{$\implies$} có độ phân giải tốt hơn!

---
### Hoạ tiết

,6\textwidth
<img src="../TaiLieu/slide_md/figures/chem-test.png" style="width:100%; height:auto;">

Ý tưởng: giả sử kết cấu thực tế là đồng nhất, tính toán hình dạng bề mặt sẽ tạo ra sự biến dạng này

Ý tưởng tương tự cũng áp dụng cho việc tạo bóng---giả sử hệ số phản xạ đồng đều, v.v.---*nhưng*

sự giao thoa đưa ra tính toán phi tiêu điểm về cường độ cảm nhận 

\mat{$\implies$} những chỗ trũng có vẻ nông hơn thực tế

---
### Các loại cạnh và đỉnh

,6\textwidth
<img src="../TaiLieu/slide_md/figures/diff-labels.png" style="width:100%; height:auto;">

,6\textwidth
<img src="../TaiLieu/slide_md/figures/trihedral.png" style="width:100%; height:auto;">

Giả sử thế giới của các vật thể đa diện rắn có đỉnh tam diện

---
### Nhãn đỉnh/cạnh

,6\textwidth
<img src="../TaiLieu/slide_md/figures/vertex-a.png" style="width:100%; height:auto;">

,5\textwidth
<img src="../TaiLieu/slide_md/figures/huffman-clowes.png" style="width:100%; height:auto;">

---
## Ví dụ về ghi nhãn đỉnh/cạnh

\twofig{ile{figures}{edge-labelling14.ps}}{figures/huffman-clowes.ps}

CSP: biến = cạnh, ràng buộc = cấu hình nút có thể

---
## Nhận dạng đối tượng

Ý tưởng đơn giản:
  
-- trích xuất hình dạng 3-D từ hình ảnh
  
-- đối chiếu với "thư viện hình dạng"

Sự cố:
  
-- trích xuất các bề mặt cong từ hình ảnh
  
-- thể hiện hình dạng của đối tượng được trích xuất
  
-- biểu diễn hình dạng và tính biến đổi của các lớp đối tượng thư viện
  
-- phân đoạn, tắc nghẽn không đúng
  
-- độ sáng, bóng tối, dấu hiệu, tiếng ồn, độ phức tạp không xác định, v.v.

Phương pháp tiếp cận:
  
-- lập chỉ mục vào thư viện bằng cách đo các thuộc tính bất biến của đối tượng
  
-- căn chỉnh tính năng hình ảnh với tính năng đối tượng thư viện được chiếu 
  
-- khớp hình ảnh với nhiều chế độ xem được lưu trữ (*khía cạnh*) của đối tượng thư viện
  
-- phương pháp học máy dựa trên số liệu thống kê hình ảnh

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

---
## Khớp hình dạng-ngữ cảnh

Ý tưởng cơ bản: chuyển đổi *hình dạng* (khái niệm quan hệ) thành 

một tập hợp cố định các thuộc tính \emph{} sử dụng bối cảnh không gian \defn{}

của mỗi tập hợp điểm cố định trên bề mặt của hình.

\threefig{figures/exampleA3.eps}{figures/exampleA4.eps}{figures/bin_grid.eps}

---
## Tiếp theo là khớp hình dạng-ngữ cảnh.

Mỗi điểm được mô tả bằng biểu đồ ngữ cảnh cục bộ của nó

(số điểm rơi vào mỗi thùng lưới log-cực)

\threefig{figures/exampleA6.eps}{figures/exampleA8.eps}{figures/exampleA7.eps}

---
## Tiếp theo là khớp hình dạng-ngữ cảnh.

Xác định tổng khoảng cách giữa các hình bằng tổng khoảng cách cho
điểm tương ứng dưới sự phù hợp tốt nhất

,3\textwidth
[Hình ảnh: \fig{figures/exampleA5.eps}]

Việc học lân cận gần nhất đơn giản mang lại tỷ lệ lỗi 0,63\% trên dữ liệu chữ số NIST

---
## Tóm tắt

Tầm nhìn khó khăn --- nhiễu, mơ hồ, phức tạp

Kiến thức trước là cần thiết để hạn chế vấn đề

Cần kết hợp nhiều tín hiệu: chuyển động, đường viền, tạo bóng, kết cấu, âm thanh nổi

Biểu diễn đối tượng "Thư viện": hình dạng và các khía cạnh

So khớp hình ảnh/đối tượng: tính năng, đường nét, vùng, v.v.




#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter27/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**

*(Hiện chưa có bài tập cho chương này)*

<!-- tabs:end -->
