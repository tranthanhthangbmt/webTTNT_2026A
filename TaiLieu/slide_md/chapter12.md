\usepackage{fleqn}
\usepackage{epsf}
\usepackage{color}
\usepackage{aima2e-slides}

\newcommand{\condstep}[3]{\mbf{if} #1 \mbf{then} #2 \mbf{else} #3}
\newcommand{\whilestep}[2]{\mbf{while} #1 \mbf{do} #2}
\newcommand{\noplan}{\emptylist}

# Lập kế hoạch và Hành động (Planning and Acting)

## Chương 12

---
## Phác thảo

- Thế giới thực

- Lập kế hoạch có điều kiện

- Giám sát và lập kế hoạch lại

---
### Thế giới thực

<img src="../TaiLieu/slide_md/figures/flat-tire-picture.png" style="width:100%; height:auto;">

<img src="../TaiLieu/slide_md/figures/flat-tire-model.png" style="width:100%; height:auto;">

---
## Có vấn đề xảy ra

\txr*Thông tin chưa đầy đủ*
  
  Điều kiện tiên quyết không xác định, ví dụ: $Intact(Spare)$?
  
  Các hiệu ứng phân biệt, ví dụ: $Inflate(x)$ gây ra
    
    $Inflated(x) \lor SlowHiss(x) \lor Burst(x) \lor BrokenPump \lor \ldots$

\txr*Thông tin không chính xác*
  
  Trạng thái hiện tại không chính xác, ví dụ: dự phòng KHÔNG nguyên vẹn
  
  Hậu điều kiện bị thiếu/không chính xác trong toán tử

\txb{Vấn đề về trình độ chuyên môn}:
    
   không bao giờ có thể liệt kê xong tất cả các điều kiện tiên quyết bắt buộc và
    
   kết quả có điều kiện có thể có của hành động

---
## Giải pháp

\txb{Conformant} hoặc \txb{quy hoạch không có cảm biến}
    
   Đưa ra một kế hoạch có hiệu quả bất kể trạng thái hay kết quả

\txr*Những kế hoạch như vậy có thể không tồn tại*

\txb{Lập kế hoạch có điều kiện}
    
    Lập kế hoạch thu thập thông tin ({\bf hành động quan sát})
    
    Kế hoạch con cho từng trường hợp dự phòng, ví dụ:
    
    $[Check(Tire1),\condstep{Intact(Tire1)}{Inflate(Tire1)}{CallAAA}$

\txr*Đắt vì nó lên kế hoạch cho nhiều trường hợp khó xảy ra*

\txb{Giám sát/Lập kế hoạch lại}
    
    Giả sử trạng thái bình thường, kết quả
    
    Kiểm tra tiến trình \txr*trong khi thực hiện*, lập kế hoạch lại nếu cần thiết

\txr*Kết quả không lường trước được có thể dẫn đến thất bại (ví dụ: không có thẻ AAA)*

(Thực sự cần sự kết hợp; lên kế hoạch cho những tình huống có thể xảy ra/nghiêm trọng,

đối phó với người khác khi họ phát sinh, vì cuối cùng họ phải làm vậy)

       

---
### Lập kế hoạch phù hợp

Tìm kiếm trong không gian của \txb{trạng thái niềm tin} (tập hợp các trạng thái thực tế có thể có)

<img src="../TaiLieu/slide_md/figures/vacuum2-sets.png" style="width:100%; height:auto;">

---
### Lập kế hoạch có điều kiện

Nếu thế giới không xác định hoặc có thể quan sát được một phần
  
  thì các nhận thức thường \txr*cung cấp thông tin*, 
  
  tức là, \txr*chia tách * trạng thái niềm tin

<img src="../TaiLieu/slide_md/figures/contingent-percepts.png" style="width:100%; height:auto;">

---
## Lập kế hoạch có điều kiện tiếp theo.

Kiểm tra kế hoạch có điều kiện (bất kỳ hậu quả nào của KB +) nhận thức

$[\ldots,\condstep{C}{Plan_A}{Plan_B},\ldots]$

Thực thi: kiểm tra $C$ so với KB hiện tại, thực thi " sau đó " hoặc " khác "

Cần \txr*một số * kế hoạch cho \txr*mọi * nhận thức có thể

(Cf. chơi trò chơi: \txr*một số * phản hồi cho \txr*mỗi * nước đi của đối thủ)

(Cf. xâu chuỗi ngược: \txr*some* quy tắc sao cho \txr*mọi tiền đề * đều thỏa mãn

AND--OR tìm kiếm cây (rất giống với thuật toán xâu chuỗi ngược)

---
### Ví dụ

Double Murphy: hút hoặc đến có thể làm bẩn một hình vuông sạch sẽ

<img src="../TaiLieu/slide_md/figures/vacuum-cond-plan.png" style="width:100%; height:auto;">

---
### Ví dụ

Triple Murphy: đôi khi cũng đứng yên thay vì di chuyển

<img src="../TaiLieu/slide_md/figures/vacuum-loop-plan.png" style="width:100%; height:auto;">

$[L_1:\ Left, \condstep{AtR}{L_1}{[\condstep{CleanL}{\noplan}{Suck}]}]$

hoặc $[\whilestep{AtR}{[Left]}, \condstep{CleanL}{\noplan}{Suck}]$

"Vòng lặp vô hạn" nhưng cuối cùng sẽ hoạt động trừ khi hành động luôn thất bại

---
## Giám sát thực thi

"Thất bại" = các điều kiện tiên quyết của \txr*kế hoạch còn lại* không được đáp ứng

Điều kiện tiên quyết của kế hoạch còn lại
    
= tất cả các điều kiện tiên quyết của các bước còn lại không đạt được bằng các bước còn lại
    
= tất cả các liên kết nhân quả \txr*băng qua * thời điểm hiện tại

Khi thất bại, hãy tiếp tục POP để đạt được các điều kiện mở từ trạng thái hiện tại

IPEM (Lập kế hoạch, thực thi và giám sát tích hợp):
    
  tiếp tục cập nhật $Start$ để phù hợp với trạng thái hiện tại 
    
  liên kết từ các hành động được thay thế bằng liên kết từ $Start$ khi hoàn tất

---
### Ví dụ

\centerline{\raisebox{-0.9\textheight}[0pt][0pt]{\epsfysize=0.95\textheight<img src="../TaiLieu/slide_md/figures/plan-preconditions1.png" style="width:100%; height:auto;">}

---
### Ví dụ

\centerline{\raisebox{-0.9\textheight}[0pt][0pt]{\epsfysize=0.95\textheight<img src="../TaiLieu/slide_md/figures/plan-preconditions2.png" style="width:100%; height:auto;">}

---
### Ví dụ

\centerline{\raisebox{-0.9\textheight}[0pt][0pt]{\epsfysize=0.95\textheight<img src="../TaiLieu/slide_md/figures/plan-preconditions3.png" style="width:100%; height:auto;">}

---
### Ví dụ

\centerline{\raisebox{-0.9\textheight}[0pt][0pt]{\epsfysize=0.95\textheight<img src="../TaiLieu/slide_md/figures/plan-preconditions4.png" style="width:100%; height:auto;">}

---
### Ví dụ

\centerline{\raisebox{-0.9\textheight}[0pt][0pt]{\epsfysize=0.95\textheight<img src="../TaiLieu/slide_md/figures/plan-preconditions5.png" style="width:100%; height:auto;">}

---
### Ví dụ

\centerline{\raisebox{-0.9\textheight}[0pt][0pt]{\epsfysize=0.95\textheight<img src="../TaiLieu/slide_md/figures/plan-preconditions6.png" style="width:100%; height:auto;">}

---
### Hành vi mới nổi 

<img src="../TaiLieu/slide_md/figures/replanning-paint2.png" style="width:100%; height:auto;">

---
### Hành vi mới nổi 

<img src="../TaiLieu/slide_md/figures/replanning-paint3.png" style="width:100%; height:auto;">

---
### Hành vi mới nổi 

<img src="../TaiLieu/slide_md/figures/replanning-paint3.png" style="width:100%; height:auto;">

Hành vi "Lặp lại cho đến khi thành công" \txr*xuất hiện* từ sự tương tác giữa 
giám sát/lập kế hoạch lại thiết kế đại lý và môi trường không hợp tác