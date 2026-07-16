\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Các quyết định phức tạp (Complex decisions)

## Chương 17, Phần 1--3

---
## Phác thảo

- Vấn đề về quyết định

- Lặp lại giá trị

- Lặp lại chính sách

---
## Các vấn đề về quyết định tuần tự

![Hình ảnh](../TaiLieu/slide_md/figures/decision-problems.png)

---
## Ví dụ MDP

![Hình ảnh](../TaiLieu/slide_md/figures/sequential-decision-world.png)

![Hình ảnh](../TaiLieu/slide_md/figures/sequential-decision-world.png) \hspace*{1in} $M_{ij}^a \equiv P(j|i,a)$

$a$

Mô hình $M_{ij}^a \equiv P(j|i,a)$ = xác suất thực hiện $a$ trong $i$ dẫn đến $j$

Mỗi tiểu bang có một *bonus* $R(i)$
    
   = -0,04 (hình phạt nhỏ) đối với các trạng thái không kết thúc
    
   = $\pm 1$ cho trạng thái đầu cuối

---
## Giải quyết MDP

Trong các bài toán tìm kiếm, mục đích là tìm một chuỗi {\em} tối ưu

Trong MDP, mục đích là tìm ra một *chính sách
     tối ưu
   tức là hành động tốt nhất cho mọi trạng thái có thể
    
   (vì không thể đoán trước được mình sẽ đi về đâu)

Các giá trị trạng thái và chính sách tối ưu cho $R(i)$ đã cho:

{figures/sequential-decision-values.ps}

---
## Tiện ích

Trong các bài toán quyết định *tuần tự*, các ưu tiên được thể hiện

giữa *chuỗi* trạng thái

Thường sử dụng hàm tiện ích *addd*:
    
$U([s_1,s_2,s_3,\ldots,s_n]) = R(s_1) + R(s_2) + R(s_3) + \cdots + R(s_n)$

(xem chi phí đường dẫn trong các vấn đề tìm kiếm)

Tiện ích của một *state* (còn gọi là *value*) của nó) được xác định là 
    
$U(s_i) = {}$ <u>tổng số phần thưởng dự kiến cho đến khi chấm dứt</u>
    
\phantom{$U(s_i) = {}$} <u>giả sử hành động tối ưu</u>

Với những lợi ích của các bang, việc lựa chọn
hành động tốt nhất chỉ là MEU: chọn hành động sao cho
ích lợi mong đợi của những người kế nhiệm trực tiếp là cao nhất.

---
## Phương trình Bellman

Định nghĩa về tính hữu dụng của các trạng thái dẫn đến một mối quan hệ đơn giản giữa
Tiện ích của các nước lân cận:

<u>tổng số phần thưởng dự kiến</u>
  
= <u>phần thưởng hiện tại</u>
    
+ <u>tổng số phần thưởng dự kiến sau khi thực hiện hành động tốt nhất</u>

Phương trình Bellman (1957):
\[ U(i) = R(i) + \max_a \mysum_j U(j) M_{ij}^a\]

$U(1,1) = -0.04$

\tab + $\max\{ 0.8 U(1,2) + 0.1 U(2,1) + 0.1 U(1,1),$*up

\tab \phantom{+ \mbox{$\max\{$*}$0.9 U(1,1) + 0.1 U(1,2) $*left

\tab \phantom{+ \mbox{$\max\{$*}$0.9 U(1,1) + 0.1 U(2,1) $*down

\tab \phantom{+ \mbox{$\max\{$*$0.8 U(2,1) + 0.1 U(1,2) + 0.1 U(1,1) \}$*đúng*

Một phương trình trên mỗi trạng thái = $n$ <u>phi tuyến </u> phương trình trong $n$ ẩn số

---
## Thuật toán lặp giá trị

<u>Idea</u>: Bắt đầu với các giá trị tiện ích tùy ý
    
          Cập nhật để làm cho chúng <u>nhất quán cục bộ</u> với Bellman eqn.
    
          Tối ưu toàn cầu nhất quán cục bộ $\Rightarrow$ ở mọi nơi

lặp lại cho đến khi "không thay đổi"
\[ U(i) \leftarrow R(i) + \max_a \mysum_j U(j) M_{ij}^a  &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{for all } i\]

![Hình ảnh](../TaiLieu/slide_md/figures/4x3-vi-curve.png)

---
##  Lặp lại chính sách (Howard, 1960)

Ý tưởng: tìm kiếm đồng thời các giá trị chính sách và tiện ích tối ưu

Thuật toán:
  
  $\pi \leftarrow {}$ chính sách ban đầu tùy ý
  
  lặp lại cho đến khi không có thay đổi nào trong $\pi$
    
    các tiện ích tính toán được cung cấp $\pi$ 
    
    cập nhật $\pi$ như thể các tiện ích đã chính xác (tức là MEU cục bộ)

Để tính toán các tiện ích đã cho $\pi$ cố định:
\[ U(i) = R(i) + \mysum_j U(j) M_{ij}^{\pi(i)} &nbsp;&nbsp;&nbsp;&nbsp;  \mbox{for all } i \]
tức là, $n$ phương trình <u>tuyến tính</u> đồng thời trong $n$ ẩn số,
giải quyết trong $O(n^3)$

---
## Nếu tôi sống mãi mãi thì sao? (lạc đề)

Sử dụng định nghĩa cộng của tiện ích, $U(i)$ là vô hạn!

Hơn nữa, việc lặp lại giá trị không kết thúc 

Chúng ta nên so sánh hai kiếp sống vô tận như thế nào?

1) Chiết khấu: phần thưởng trong tương lai được chiết khấu theo tỷ lệ $\gamma \leq 1$
\[ U([s_0,\ldots s_{\infty}]) = \mysum_{t=0}^{\infty} \gamma^t R(s_t)\]
Tiện ích tối đa được giới hạn ở trên bởi $R_{{\rm max}}/(1-\gamma)$ 

Đường chân trời ngắn hơn $\gamma \Rightarrow {}$ nhỏ hơn

2) Tối đa hóa <u>lợi ích hệ thống</u> = phần thưởng trung bình mỗi bước thời gian

Định lý: chính sách tối ưu có mức tăng không đổi sau thoáng qua ban đầu

Ví dụ: kế hoạch hàng ngày của tài xế taxi đưa đón hành khách