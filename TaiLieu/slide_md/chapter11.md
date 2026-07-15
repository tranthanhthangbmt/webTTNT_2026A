\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Lập kế hoạch (Planning)

## Chương 11

---
## Phác thảo

- Tìm kiếm và lập kế hoạch

- Toán tử STRIPS

- Lập kế hoạch theo thứ tự từng phần

---
## Tìm kiếm và lập kế hoạch

Xét nhiệm vụ \txr*lấy sữa, chuối và máy khoan không dây*

Các thuật toán tìm kiếm tiêu chuẩn dường như thất bại thảm hại:

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/supermarket1.png)

Kiểm tra mục tiêu/kinh nghiệm sau thực tế không đầy đủ

---
## Tiếp theo là tìm kiếm và lập kế hoạch.

Hệ thống lập kế hoạch thực hiện những việc sau:
  
1) mở ra hành động và thể hiện mục tiêu để cho phép lựa chọn
  
2) chia để trị bằng cách đặt mục tiêu phụ
  
3) nới lỏng yêu cầu xây dựng giải pháp tuần tự

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
|  | {\bf Tìm kiếm} | {\bf Lập kế hoạch} |
| {\bf Trạng thái} | Cấu trúc dữ liệu Lisp | Câu logic |
| {\bf Hành động} | Mã Lisp | Điều kiện tiên quyết/kết quả |
| {\bf Mục tiêu} | Mã Lisp | Câu logic (liên từ) |
| {\bf Kế hoạch} | Trình tự từ $S_0$ | Ràng buộc về hành động |

---
## Toán tử STRIPS

Mô tả hành động được sắp xếp gọn gàng, ngôn ngữ hạn chế

**Hành động**: $Buy(x)$\raisebox{-1.5in[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/operator-schema2.png)

**Điều kiện tiên quyết**: $At(p), Sells(p,x)$

**Effect**: $Have(x)$

[Lưu ý: phần này tóm tắt nhiều chi tiết quan trọng!]

Ngôn ngữ bị hạn chế $\implies$ thuật toán hiệu quả 
    
Điều kiện tiên quyết: sự kết hợp của các chữ tích cực
    
Tác dụng: sự kết hợp của chữ

Một bộ toán tử STRIPS hoàn chỉnh có thể được dịch 

thành một tập tiên đề trạng thái kế tiếp

---
## Các kế hoạch được đặt hàng một phần

\txr*Tập hợp các bước được sắp xếp một phần* với
    
  \txb{$Finish$ step} có mô tả trạng thái ban đầu là hiệu ứng của nó
    
  \txb{$Finish$ step} có mô tả mục tiêu là điều kiện tiên quyết
    
  \txb{liên kết nhân quả} từ kết quả của bước này đến điều kiện tiên quyết của bước khác
    
  \txb{thứ tự thời gian} giữa các cặp bước

\txb{Điều kiện mở} = điều kiện tiên quyết của bước chưa được liên kết nhân quả

Một kế hoạch là \txb{hoàn thành} nếu mọi điều kiện tiên quyết đều đạt được

Một điều kiện tiên quyết đã đạt được \txb{} nếu đó là hiệu quả của bước trước đó

và không có bước \txb{ nào có thể can thiệp } có thể hoàn tác nó

---
## Ví dụ

\centerline{\raisebox{-0.9\textheight[0pt][0pt]{\epsfysize=0.95\textheight![Hình ảnh](../TaiLieu/slide_md/figures/plan-construction1.png)}

---
## Ví dụ

\centerline{\raisebox{-0.9\textheight[0pt][0pt]{\epsfysize=0.95\textheight![Hình ảnh](../TaiLieu/slide_md/figures/plan-construction2.png)}

---
## Ví dụ

\centerline{\raisebox{-0.9\textheight[0pt][0pt]{\epsfysize=0.95\textheight![Hình ảnh](../TaiLieu/slide_md/figures/plan-construction3.png)}

---
## Quy trình lập kế hoạch

Người vận hành trên các gói một phần:
    
   \txb{thêm liên kết} từ hành động hiện có vào điều kiện mở
    
   \txb{thêm một bước} để đáp ứng điều kiện mở
    
   \txb{order} một bước khác để loại bỏ những xung đột có thể xảy ra

Dần dần chuyển từ những kế hoạch chưa đầy đủ/mơ hồ sang những kế hoạch hoàn chỉnh, đúng đắn

Quay lại nếu điều kiện mở không thể đạt được hoặc 

nếu xung đột không thể giải quyết được

---
## Bản phác thảo thuật toán POP

```text
function POP(initial, goal, operators) returns plan

    plan <- Make-Minimal-Plan(initial, goal)
    loop do
          if Solution?(plan) then return plan
          $S_{need, c$}{Select-Subgoal(plan)}
          Choose-Operator(plan, operators, $S_{need}$, c)
          Resolve-Threats(plan)
    end
\fnsep
function Select-Subgoal(plan) returns $S_{need, c$}

    pick a plan step $S_{need}$ from Steps(plan)
          with a precondition $c$ that has not been achieved
    return $S_{need}, c$
```

---
## Tiếp theo thuật toán POP.

```text
\proc{Choose-Operator}{plan, operators, $S_{need$, c}}

    choose a step $S_{add}$ from operators or Steps(plan) that has $c$ as an effect
    if there is no such step then fail 
    add the causal link $\cl{S_{add}}{c}{S_{need}}$ to Links(plan)
    add the ordering constraint $S_{add} \before S_{need}$ to Orderings(plan)
    if $S_{add}$ is a newly added step from operators then
          add $S_{add}$ to Steps(plan)
          add $Start \before S_{add} \before Finish$ to Orderings(plan)
\fnsep
\proc{Resolve-Threats}{plan}

    for each $S_{threat}$ that threatens a link $S_i --c--> S_j$ in Links(plan) do
          choose either
                *Demotion:* Add $S_{threat}\before S_i$ to Orderings(plan)
                *Promotion:* Add $S_j \before S_{threat}$ to Orderings(plan)
          if not Consistent(plan) then fail
    end
```

---
## Tấn công và thăng chức/hạ cấp

\txb{clobberer} là một bước can thiệp có khả năng phá hủy
điều kiện đạt được bởi một liên kết nhân quả. Ví dụ: $Go(Home)$ tắc nghẽn $At(Supermarket)$:

,40\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/clobber.png)
 

\txb{Hạ cấp}: đặt trước $Go(Supermarket)$

\txb{Khuyến mãi}: xếp sau $Buy(Milk)$

\ 

---
## Thuộc tính của POP

Thuật toán không xác định: quay lại tại điểm \txb{lựa chọn} khi thất bại:
  
 -- lựa chọn $S_{add}$ để đạt được $S_{need}$
  
 -- lựa chọn giáng chức hoặc thăng chức cho kẻ phá hoại
  
 -- việc lựa chọn $S_{need}$ là không thể hủy bỏ

POP là âm thanh, hoàn chỉnh và \txb{có hệ thống} (không lặp lại)

Phần mở rộng cho sự phân tách, phổ quát, phủ định, điều kiện

Có thể được thực hiện hiệu quả với các phương pháp phỏng đoán tốt bắt nguồn từ việc mô tả vấn đề

Đặc biệt tốt cho các vấn đề có nhiều mục tiêu phụ có liên quan lỏng lẻo

---
## Ví dụ: Thế giới khối

![Hình ảnh](../TaiLieu/slide_md/figures/blocks-world.png)

---
## Ví dụ tiếp theo.

![Hình ảnh](../TaiLieu/slide_md/figures/sussman1.png)

---
## Ví dụ tiếp theo.

![Hình ảnh](../TaiLieu/slide_md/figures/sussman2.png)

---
## Ví dụ tiếp theo.

![Hình ảnh](../TaiLieu/slide_md/figures/sussman3.png)

---
## Ví dụ tiếp theo.

![Hình ảnh](../TaiLieu/slide_md/figures/sussman4.png)