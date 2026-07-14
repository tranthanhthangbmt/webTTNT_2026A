\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Lập kế hoạch và Hành động (Planning and Acting)

## Chương 13

---
## Nội dung

- Thế giới thực

- Lập kế hoạch có điều kiện

- Giám sát và Lập lại kế hoạch

---
## Thế giới thực

![Hình ảnh](../TaiLieu/slide_md/figures/flat-tire-picture.png)

![Hình ảnh](../TaiLieu/slide_md/figures/flat-tire-model.png)

---
## Những điều có thể sai lệch

<u>Thông tin không đầy đủ (Incomplete information)</u>
  
  Chưa biết các tiền điều kiện, ví dụ: $Intact(Spare)$?
  
  Hiệu ứng tuyển, ví dụ: $Inflate(x)$ gây ra
    
    $Inflated(x) \lor SlowHiss(x) \lor Burst(x) \lor BrokenPump \lor \ldots$

<u>Thông tin không chính xác (Incorrect information)</u>
  
  Trạng thái hiện tại không chính xác, ví dụ: lốp dự phòng KHÔNG nguyên vẹn
  
  Thiếu/sai các hậu điều kiện trong các toán tử

Vấn đề chất lượng (Qualification problem):
    
   không bao giờ có thể liệt kê xong tất cả các tiền điều kiện bắt buộc và
    
   các kết quả có điều kiện có thể xảy ra của các hành động

---
## Các giải pháp

<u>Lập kế hoạch có điều kiện (Conditional planning)</u>
    
    Lập kế hoạch để thu thập thông tin ({\bf các hành động quan sát})
    
    Kế hoạch con cho từng tình huống ngẫu nhiên, ví dụ:
    
    $[Check(Tire1),\mbf{If}(Intact(Tire1),[Inflate(Tire1)],[CallAAA])]$

Tốn kém vì nó lập kế hoạch cho nhiều trường hợp khó xảy ra

<u>Giám sát/Lập lại kế hoạch (Monitoring/Replanning)</u>
    
    Giả định các trạng thái bình thường, kết quả bình thường
    
    Kiểm tra tiến độ *trong quá trình thực thi*, lập lại kế hoạch nếu cần thiết

Kết quả không lường trước có thể dẫn đến thất bại (ví dụ: không có thẻ AAA)

Nhìn chung, một số giám sát là không thể tránh khỏi
       

---
## Lập kế hoạch có điều kiện

$[\ldots,\mbf{If}(p,[then\,plan],[else\,plan]),\ldots]$

Thực thi: kiểm tra $p$ dựa trên KB hiện tại, thực thi nhánh "then" hoặc "else"

Lập kế hoạch có điều kiện: giống như \prog{POP} ngoại trừ
  
  nếu một điều kiện mở có thể được thiết lập bởi hành động <u>quan sát</u>
    
    thêm hành động đó vào kế hoạch
    
    hoàn thành kế hoạch cho từng kết quả quan sát có thể xảy ra
    
    chèn bước điều kiện với các kế hoạch con này

![Hình ảnh](../TaiLieu/slide_md/figures/observation-schema.png)

---
## Ví dụ lập kế hoạch có điều kiện

![Hình ảnh](../TaiLieu/slide_md/figures/flat1.png)

---
## Ví dụ lập kế hoạch có điều kiện

![Hình ảnh](../TaiLieu/slide_md/figures/flat2.png)

---
## Ví dụ lập kế hoạch có điều kiện

![Hình ảnh](../TaiLieu/slide_md/figures/flat3.png)

---
## Ví dụ lập kế hoạch có điều kiện

![Hình ảnh](../TaiLieu/slide_md/figures/flat4.png)

---
## Ví dụ lập kế hoạch có điều kiện

![Hình ảnh](../TaiLieu/slide_md/figures/flat5.png)

---
## Ví dụ lập kế hoạch có điều kiện

![Hình ảnh](../TaiLieu/slide_md/figures/flat6.png)

---
## Giám sát (Monitoring)

{\bf Giám sát thực thi (Execution monitoring)}
  
  "thất bại" = tiền điều kiện của *kế hoạch còn lại* không được đáp ứng
  
  tiền điều kiện = <u>các liên kết nhân quả tại thời điểm hiện tại</u>

{\bf Giám sát hành động (Action monitoring)}
  
    "thất bại" = tiền điều kiện của *hành động tiếp theo* không được đáp ứng
    
       (hoặc bản thân hành động thất bại, ví dụ: cảm biến va chạm của robot)

Trong cả hai trường hợp, đều cần phải *lập lại kế hoạch (replan)*

---
## Các tiền điều kiện cho kế hoạch còn lại

\epsfysize=0.8\textheight
![Hình ảnh](../TaiLieu/slide_md/figures/plan-preconditions.png)

---
## Lập lại kế hoạch (Replanning)

Đơn giản nhất: khi thất bại, lập lại kế hoạch từ đầu

Tốt hơn: lập kế hoạch để quay trở lại đúng hướng bằng cách kết nối lại với phần tiếp theo tốt nhất

Tạo ra hành vi "lặp cho đến khi xong" mà không có vòng lặp rõ ràng

![Hình ảnh](../TaiLieu/slide_md/figures/replanning-generic.png)

![Hình ảnh](../TaiLieu/slide_md/figures/replanning-paint.png)