\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Lập kế hoạch (Planning)

## Chương 11

---
## Nội dung

- Tìm kiếm so với lập kế hoạch

- Các toán tử STRIPS

- Lập kế hoạch theo thứ tự cục bộ (Partial-order planning)

---
## Tìm kiếm so với lập kế hoạch

Xem xét nhiệm vụ *lấy sữa, chuối và máy khoan không dây*

Các thuật toán tìm kiếm tiêu chuẩn dường như thất bại thảm hại:

![Hình ảnh](../TaiLieu/slide_md/figures/supermarket1.png)

Kiểm tra heuristic/đích sau khi sự việc xảy ra là không thỏa đáng

---
## Tìm kiếm so với lập kế hoạch (tiếp)

Các hệ thống lập kế hoạch thực hiện những việc sau:
  
1) mở rộng biểu diễn hành động và đích để cho phép lựa chọn
  
2) chia để trị bằng cách đặt các mục tiêu con (subgoaling)
  
3) nới lỏng yêu cầu xây dựng các giải pháp tuần tự

| &nbsp; | &nbsp; | &nbsp; |
|---|---|---|
|  | {\bf Tìm kiếm} | {\bf Lập kế hoạch} |
| {\bf Trạng thái} | Cấu trúc dữ liệu Lisp | Các câu logic |
| {\bf Hành động} | Mã Lisp | Tiền điều kiện/kết quả |
| {\bf Đích} | Mã Lisp | Câu logic (phép hội) |
| {\bf Kế hoạch} | Chuỗi từ $S_0$ | Các ràng buộc trên các hành động |

---
## Lập kế hoạch trong phép tính tình huống

$PlanResult(p,s)$ là tình huống kết quả từ việc thực thi $p$ trong $s$
    
  $PlanResult([],s) = s$
    
  $PlanResult([a|p],s) = PlanResult(p,Result(a,s))$

{\bf Trạng thái ban đầu} $At(Home,S_0) \land \lnot Have(Milk,S_0) \land \ldots$

{\bf Hành động} như các tiên đề Trạng thái kế tiếp

  $Have(Milk,Result(a,s)) \lequiv {}$

    $[(a=Buy(Milk) \land At(Supermarket,s))
     \lor (Have(Milk,s) \land a \neq \ldots)]$

{\bf Truy vấn}
  
  $s=PlanResult(p,S_0) \land At(Home,s) \land Have(Milk,s) \land \ldots$

{\bf Giải pháp}
  
  $p = [Go(Supermarket),Buy(Milk),Buy(Bananas),Go(HWS),\ldots]$

Khó khăn chính: phân nhánh không bị ràng buộc, khó áp dụng các heuristic

---
## Các toán tử STRIPS

Mô tả các hành động được sắp xếp gọn gàng, ngôn ngữ bị hạn chế

**Hành động (Action)**: $Buy(x)$

**Tiền điều kiện (Precondition)**: $At(p), Sells(p,x)$

**Hiệu ứng (Effect)**: $Have(x)$

[Lưu ý: điều này trừu tượng hóa nhiều chi tiết quan trọng!]

Ngôn ngữ bị hạn chế $\implies$ thuật toán hiệu quả
    
Tiền điều kiện: phép hội của các literal khẳng định
    
Hiệu ứng: phép hội của các literal

![Hình ảnh](../TaiLieu/slide_md/figures/operator-schema2.png)

---
## Không gian trạng thái so với không gian kế hoạch

Tìm kiếm tiêu chuẩn: nút = trạng thái thế giới cụ thể

Tìm kiếm lập kế hoạch: nút = <u>kế hoạch cục bộ (partial plan)</u>

Định nghĩa: <u>điều kiện mở (open condition)</u> là một tiền điều kiện của một bước chưa được hoàn thành

Các toán tử trên các kế hoạch cục bộ:
    
   <u>thêm một liên kết</u> từ một hành động hiện có đến một điều kiện mở
    
   <u>thêm một bước</u> để hoàn thành một điều kiện mở
    
   <u>sắp xếp</u> một bước so với bước khác

Chuyển dần từ các kế hoạch không đầy đủ/mơ hồ sang các kế hoạch đầy đủ, chính xác

---
## Các kế hoạch được sắp xếp cục bộ

![Hình ảnh](../TaiLieu/slide_md/figures/shoes-socks4.png)

Một kế hoạch là <u>đầy đủ (complete)</u> khi và chỉ khi mọi tiền điều kiện đều đạt được

Một tiền điều kiện <u>đạt được (achieved)</u> khi và chỉ khi nó là hiệu ứng của một bước trước đó

và không có bước <u>có khả năng can thiệp (possibly intervening)</u> nào hủy bỏ nó

---
## Phác thảo thuật toán POP

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

    chọn một bước kế hoạch $S_{need}$ từ Steps(plan)
          với một tiền điều kiện $c$ chưa đạt được
    return $S_{need}, c$
```

---
## Thuật toán POP (tiếp)

```text
\proc{Choose-Operator}{plan, operators, $S_{need$, c}}

    choose chọn một bước $S_{add}$ từ operators hoặc Steps(plan) có hiệu ứng là $c$
    if nếu không có bước như vậy then fail 
    thêm liên kết nhân quả $\cl{S_{add}}{c}{S_{need}}$ vào Links(plan)
    thêm ràng buộc thứ tự $S_{add} \before S_{need}$ vào Orderings(plan)
    if nếu $S_{add}$ là một bước mới được thêm từ operators then
          thêm $S_{add}$ vào Steps(plan)
          thêm $Start \before S_{add} \before Finish$ vào Orderings(plan)
\fnsep
\proc{Resolve-Threats}{plan}

    for each với mỗi $S_{threat}$ đe dọa liên kết $S_i --c--> S_j$ trong Links(plan) do
          choose chọn hoặc
                *Hạ hạng (Demotion):* Thêm $S_{threat}\before S_i$ vào Orderings(plan)
                *Thăng hạng (Promotion):* Thêm $S_j \before S_{threat}$ vào Orderings(plan)
          if not nếu không Consistent(plan) then fail
    end
```

POP là đúng đắn, đầy đủ và <u>có hệ thống</u> (không lặp lại)

Mở rộng cho phép tuyển, lượng từ phổ dụng, phủ định, điều kiện

---
## Đè bẹp (Clobbering) và thăng hạng/hạ hạng (promotion/demotion)

Một <u>clobberer</u> là một bước can thiệp tiềm năng phá hủy
điều kiện đạt được bởi một liên kết nhân quả. Ví dụ, $Go(Home)$ đè bẹp $At(HWS)$:

![Hình ảnh](../TaiLieu/slide_md/figures/clobber.png)
 

<u>Hạ hạng (Demotion)</u>: đặt trước $Go(HWS)$

<u>Thăng hạng (Promotion)</u>: đặt sau $Buy(Drill)$

\ 

---
## Ví dụ: Thế giới khối (Blocks world)

![Hình ảnh](../TaiLieu/slide_md/figures/blocks-world.png)

---
## Ví dụ (tiếp)

![Hình ảnh](../TaiLieu/slide_md/figures/sussman1.png)

---
## Ví dụ (tiếp)

![Hình ảnh](../TaiLieu/slide_md/figures/sussman2.png)

---
## Ví dụ (tiếp)

![Hình ảnh](../TaiLieu/slide_md/figures/sussman3.png)

---
## Ví dụ (tiếp)

![Hình ảnh](../TaiLieu/slide_md/figures/sussman4.png)