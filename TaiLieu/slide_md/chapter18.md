\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Học từ các quan sát (Learning from Observations)

## Chương 18, Phần 1--3

---
## Phác thảo

- Tác nhân học tập

- Học quy nạp

- Học cây quyết định

- Đo lường hiệu quả học tập

---
## Học

Học tập là điều cần thiết cho những môi trường chưa biết,

tức là khi nhà thiết kế thiếu sự toàn tri

Học tập hữu ích như một phương pháp xây dựng hệ thống,

tức là, cho tác nhân tiếp xúc với thực tế thay vì cố gắng viết nó ra

Việc học sửa đổi cơ chế quyết định của tác nhân để cải thiện hiệu suất

---
## Tác nhân học tập

![Hình ảnh](../TaiLieu/slide_md/figures/learning-model.png)

---
## Phần tử học tập

Thiết kế thành phần học tập được quyết định bởi
  
- loại phần tử hiệu suất nào được sử dụng
  
- thành phần chức năng nào sẽ được học
  
- cách thể hiện thành phần chức năng đó
  
- có những loại phản hồi nào 

Các tình huống ví dụ:

![Hình ảnh](../TaiLieu/slide_md/figures/learning-elements.png)

\defn{Học có giám sát}: câu trả lời đúng cho từng trường hợp

\defn{Học tăng cường}: phần thưởng không thường xuyên

---
## Học quy nạp (còn gọi là Khoa học)

Hình thức đơn giản nhất: học hàm từ các ví dụ (*tabula rasa*)

   là *hàm đích*

Một \defn{example} là một cặp \mat{$x$}, \mat{$f$}, ví dụ: 
\mat{$\begin{array}{c|c|c}O&O&X 

                     \hline
                      &X&  

                     \hline
                     X& &  \end{array}\ \ ,\ \ +1$}

Bài toán: tìm một(n) \defn{giả thuyết} \mat{$h$}
    
   sao cho \mat{$h \approx f$}
    
   đưa ra một \defn{tập huấn luyện} gồm các ví dụ

(*Đây là mô hình học tập thực tế được đơn giản hóa cao:
  
  -- Bỏ qua kiến thức trước đây
  
  -- Giả sử một "môi trường" xác định, có thể quan sát được 
  
  -- Giả sử các ví dụ được cho là \emph{*
  
  -- Giả sử rằng tác nhân *muốn* tìm hiểu \mat{$f$}---tại sao?})

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting1.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting2.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting3.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting4.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting5.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting5.png)

\defn{Dao cạo Ockham}: tối đa hóa sự kết hợp giữa tính nhất quán và sự đơn giản

---
## Biểu diễn dựa trên thuộc tính

Ví dụ được mô tả bởi các giá trị thuộc tính \defn{} (Boolean, rời rạc, liên tục, v.v.)

Ví dụ: các tình huống mà tôi sẽ/không đợi bàn:

{\em

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
| \raisebox{-6pt}[0pt][0pt]{{\em\tf Example}} | \multicolumn{10}{c||}{\em\tf Attributes} | {\em\tf Target} |
| \cline{2-11} | $Alt$ | $Bar$ | $Fri$ | $Hun$ | $Pat$ | $Price$ | $Rain$ | $Res$ | $Type$ | $Est$ | WillWait |
| $X_1$ | T | F | F | T | Some | \$\$\$ | F | T | French | 0--10 | T |
| $X_2$ | T | F | F | T | Full | \$ | F | F | Thai | 30--60 | F |
| $X_3$ | F | T | F | F | Some | \$ | F | F | Burger | 0--10 | T |
| $X_4$ | T | F | T | T | Full | \$ | F | F | Thai | 10--30 | T |
| $X_5$ | T | F | T | F | Full | \$\$\$ | F | T | French | $>$60 | F |
| $X_6$ | F | T | F | T | Some | \$\$ | T | T | Italian | 0--10 | T |
| $X_7$ | F | T | F | F | None | \$ | T | F | Burger | 0--10 | F |
| $X_8$ | F | F | F | T | Some | \$\$ | T | T | Thai | 0--10 | T |
| $X_9$ | F | T | T | F | Full | \$ | T | F | Burger | $>$60 | F |
| $X_{10}$ | T | T | T | T | Full | \$\$\$ | F | T | Italian | 10--30 | F |
| $X_{11}$ | F | F | F | F | None | \$ | F | F | Thai | 0--10 | F |
| $X_{12}$ | T | T | T | T | Full | \$ | F | F | Burger | 30--60 | T |

}

\defn{Phân loại} của các ví dụ là \defn{dương} (T) hoặc \defn{âm tính} (F)

---
## Cây quyết định

Một đại diện khả dĩ cho các giả thuyết

Ví dụ: đây là cây "true" để quyết định có nên đợi hay không:

![Hình ảnh](../TaiLieu/slide_md/figures/restaurant-tree.png)

---
## Tính biểu cảm

Cây quyết định có thể thể hiện bất kỳ chức năng nào của thuộc tính đầu vào.

Ví dụ: đối với các hàm Boolean, đường dẫn hàng bảng chân lý \mat{$\rightarrow$} đến lá:

![Hình ảnh](../TaiLieu/slide_md/figures/xor-decision-tree.png)

Điều đáng chú ý là có một cây quyết định nhất quán cho bất kỳ tập huấn luyện nào

w/ một đường dẫn đến lá cho mỗi ví dụ (trừ khi \mat{$f$} không xác định trong \mat{$x$})

nhưng có lẽ nó sẽ không khái quát hóa được các ví dụ mới

Muốn tìm thêm cây quyết định *compact*

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$n$</u>??}

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$n$</u>??}

= số lượng hàm Boolean

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$n$</u>??}

= số lượng hàm Boolean

= số bảng chân lý riêng biệt có hàng \mat{$2^n$}

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$n$</u>??}

= số lượng hàm Boolean

= số bảng chân lý riêng biệt có \mat{$2^n$} hàng = \mat{$2^{2^n}$}

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$n$</u>??}

= số lượng hàm Boolean

= số bảng chân lý riêng biệt có \mat{$2^n$} hàng = \mat{$2^{2^n}$}

Ví dụ: với 6 thuộc tính Boolean, có 18.446.744.073.709.551.616 cây

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$Hungry\land\lnot Rain$</u>??}

= số lượng hàm Boolean

= số bảng chân lý riêng biệt có \mat{$2^n$} hàng = \mat{$2^{2^n}$}

Ví dụ: với 6 thuộc tính Boolean, có 18.446.744.073.709.551.616 cây

<u>Có bao nhiêu giả thuyết liên kết thuần túy (ví dụ: \mat{$Hungry\land\lnot Rain$</u>??)}

---
## Không gian giả thuyết

<u>Có bao nhiêu cây quyết định riêng biệt với thuộc tính Boolean \mat{$Hungry\land\lnot Rain$</u>??}

= số lượng hàm Boolean

= số bảng chân lý riêng biệt có \mat{$2^n$} hàng = \mat{$2^{2^n}$}

Ví dụ: với 6 thuộc tính Boolean, có 18.446.744.073.709.551.616 cây

<u>Có bao nhiêu giả thuyết liên kết thuần túy (ví dụ: \mat{$Hungry\land\lnot Rain$</u>??)}

Mỗi thuộc tính có thể ở (dương), in (âm) hoặc out
    
\mat{$\implies$} \mat{$3^n$} giả thuyết liên kết khác biệt

Không gian giả thuyết biểu cảm hơn
  
 -- tăng khả năng hàm mục tiêu có thể được biểu thị  &nbsp;&nbsp; \smiley
  
 -- tăng số lượng giả thuyết phù hợp với tập huấn luyện
    
    \mat{$\implies$} có thể nhận được dự đoán tồi tệ hơn &nbsp;&nbsp; \frowny

---
## Học cây quyết định

Mục tiêu: tìm một cây nhỏ phù hợp với các ví dụ đào tạo

Ý tưởng: (đệ quy) chọn thuộc tính "quan trọng nhất" làm gốc của cây (phụ)

```text
function DTL(examples, attributes, default) returns a decision tree

    if examples is empty then return default
    else if all examples have the same classification then return the classification
    else if attributes is empty then return Mode(examples)
    else 
          best <- Choose-Attribute(attributes, examples)
          tree <- a new decision tree with root test best
          for each value v$_i$ of best do
                examples$_i$ <- $\{$elements of examples with $best = v_i\$}
                \v{subtree}{}DTL(examples$_i, $attributes$, -, $best, Mode(examples))
                add a branch to tree with label v$_i$ and subtree subtree
          return tree
```

---
## Chọn thuộc tính

Ý tưởng: một thuộc tính tốt sẽ chia các ví dụ thành các tập con
(lý tưởng) "tất cả đều tích cực" hoặc "tất cả tiêu cực"

![Hình ảnh](../TaiLieu/slide_md/figures/restaurant-roots.png)

\mat{$Patrons?$} là lựa chọn tốt hơn---cung cấp *thông tin* về phân loại

---
## Thông tin

Thông tin trả lời câu hỏi

Tôi càng không biết gì về câu trả lời ban đầu thì càng
thông tin có trong câu trả lời

Tỷ lệ: 1 bit = câu trả lời cho câu hỏi Boolean có \mat{$\<0.5,0.5\>$} trước

Thông tin trong câu trả lời có trước \mat{$\<P_1,\ldots,P_n\>$} là
\mat{\[
  H(\<P_1,\ldots,P_n\>) = \mysum_{i\eq 1}^n - P_i \log_2 P_i
\]}
(còn gọi là \defn{entropy} trước đó)

---
## Thông tin tiếp theo.

Giả sử chúng ta có \mat{$p$} ví dụ dương và \mat{$n$} âm ở gốc
    
\mat{$\implies$} \mat{$H(\<p/(p+n),n/(p+n)\>)$} bit cần thiết để phân loại một ví dụ mới 

Ví dụ: đối với 12 ví dụ về nhà hàng, \mat{$p\eq n\eq 6$} vì vậy chúng tôi cần 1 bit

Một thuộc tính chia các ví dụ \mat{$E$} thành các tập con \mat{$E_i$}, mỗi tập con đó
(chúng tôi hy vọng) cần ít thông tin hơn để hoàn thành việc phân loại

Đặt \mat{$E_i$} có \mat{$p_i$} ví dụ dương và \mat{$n_i$} âm 
  
\mat{$\implies$} \mat{$H(\<p_i/(p_i+n_i),n_i/(p_i+n_i)\>)$} bit cần thiết để phân loại một ví dụ mới 
  
\mat{$\implies$} *số bit mong đợi* trên mỗi ví dụ trên tất cả các nhánh là
\mat{\[
  \mysum_i \ \ \frac{p_i+n_i}{p+n} \ H(\<p_i/(p_i+n_i),n_i/(p_i+n_i)\>)
\]}
Đối với \mat{$Patrons?$}, đây là 0,459 bit, đối với \mat{$Type$} thì đây là (vẫn) 1 bit

\mat{$\implies$} chọn thuộc tính giảm thiểu thông tin còn lại cần thiết

---
## Ví dụ tiếp theo.

Cây quyết định học được từ 12 ví dụ:

![Hình ảnh](../TaiLieu/slide_md/figures/induced-restaurant-tree.png)

Đơn giản hơn nhiều so với cây “đúng”---một giả thuyết phức tạp hơn
không được chứng minh bằng lượng nhỏ dữ liệu

---
## Đo hiệu suất

Làm sao chúng ta biết được điều đó \mat{$h\approx f$}? (Bài toán cảm ứng * của Hume *)

1) Sử dụng các định lý của lý thuyết học tính toán/thống kê

2) Thử \mat{$h$} trên \defn{bộ thử nghiệm} mới gồm các ví dụ 
  
  (sử dụng *cùng phân phối trên không gian mẫu* làm tập huấn luyện)

\defn{Đường cong học tập} = \% đúng trên tập kiểm tra dưới dạng hàm của kích thước tập huấn luyện

![Hình ảnh](../TaiLieu/slide_md/figures/restaurant-dtl-curve.png)

---
## Tiếp tục đo lường hiệu suất 

Đường cong học tập phụ thuộc vào 
  
 -- \defn{có thể thực hiện được} (có thể biểu thị hàm mục tiêu) so với \defn{không thể thực hiện được}
    
     không thể thực hiện được có thể do thiếu thuộc tính 
    
     hoặc lớp giả thuyết bị hạn chế (ví dụ: hàm tuyến tính có ngưỡng)
  
 -- tính biểu đạt dư thừa (ví dụ: vô số thuộc tính không liên quan)

![Hình ảnh](../TaiLieu/slide_md/figures/learning-curves.png)

---
## Tóm tắt

Cần học tập cho môi trường chưa rõ, nhà thiết kế lười biếng

Tác nhân học tập = yếu tố hiệu suất + yếu tố học tập

Phương pháp học phụ thuộc vào loại yếu tố hiệu suất, có sẵn

phản hồi, loại thành phần cần được cải thiện và cách trình bày của nó

Đối với việc học có giám sát, mục đích là tìm ra một giả thuyết đơn giản

điều đó gần như phù hợp với các ví dụ huấn luyện

Học cây quyết định bằng cách sử dụng thông tin đạt được 

Hiệu suất học tập = độ chính xác dự đoán được đo trên bộ kiểm tra