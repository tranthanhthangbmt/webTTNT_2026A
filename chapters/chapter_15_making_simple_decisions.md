# Chapter 15 Making simple decisions

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_15_Making%20simple%20decisions/chapter_15_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_15_Making%20simple%20decisions.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Temporal probability models

## Chapter 15, Sections 1--5

---
## Phác thảo

- Thời gian và sự bất định

- Suy luận: lọc, dự đoán, làm mịn

- Mô hình Markov ẩn

- Bộ lọc Kalman (đề cập ngắn gọn)

- Mạng Bayes động

- Lọc hạt

---
## Thời gian và độ không đảm bảo

Thế giới thay đổi; chúng ta cần theo dõi và dự đoán nó

Quản lý bệnh tiểu đường và chẩn đoán xe

Ý tưởng cơ bản: sao chép các biến trạng thái và bằng chứng cho từng bước thời gian

\mat{$\X_t$} = tập hợp các biến trạng thái không thể quan sát được tại thời điểm \mat{$t$}
    
    ví dụ: \mat{$BloodSugar_t$}, \mat{$StomachContents_t$}, v.v.

\mat{$\E_t$} = tập hợp các biến bằng chứng có thể quan sát được tại thời điểm \mat{$t$}
  
    ví dụ: \mat{$MeasuredBloodSugar_t$}, \mat{$PulseRate_t$}, \mat{$FoodEaten_t$}

Điều này giả định *thời gian rời rạc*; kích thước bước phụ thuộc vào vấn đề

Ký hiệu: \mat{$\X_{a:b} = \X_a, \X_{a+1},\ldots,\X_{b-1},\X_b$}

---
## Quy trình Markov (chuỗi Markov)

Xây dựng mạng Bayes từ các biến này: cha mẹ?

\defn{Giả định Markov}: \mat{$\X_t$} phụ thuộc vào tập hợp con *bounded* của \mat{$\X_{0:t-1}$}

\defn{Quy trình Markov bậc nhất}: \mat{$P(\X_t|\X_{0:t-1}) = P(\X_t|\X_{t-1})$}

\defn{Quy trình Markov bậc hai}: \mat{$P(\X_t|\X_{0:t-1}) = P(\X_t|\X_{t-2},\X_{t-1})$}

![Hình ảnh](../TaiLieu/slide_md/figures/markov-processes.png)

\defn{Giả định Markov của cảm biến}: \mat{$P(\E_t|\X_{0:t},\E_{0:t-1}) =  P(\E_t|\X_t)$}

\defn{Quy trình cố định}: mô hình chuyển tiếp \mat{$P(\X_t|\X_{t-1})$} và 

mẫu cảm biến \mat{$P(\E_t|\X_t)$} đã được sửa cho tất cả \mat{$t$}

---
## Ví dụ

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella-dbn.png)

Giả định Markov bậc nhất không hoàn toàn đúng trong thế giới thực!

Các bản sửa lỗi có thể có: 
  
 1. *Tăng thứ tự* của quy trình Markov
  
 2. *Trạng thái tăng cường*, ví dụ: thêm \mat{$Temp_t$}, \mat{$Pressure_t$}

Ví dụ: chuyển động của robot. 
  
  Tăng vị trí và vận tốc với \mat{$Battery_t$}

---
## Nhiệm vụ suy luận

\defn{Lọc}: \mat{$P(\X_t|\e_{1:t})$}
  
  \defn{trạng thái niềm tin}---đầu vào cho quá trình quyết định của một tác nhân hợp lý

\defn{Dự đoán}: \mat{$P(\X_{t+k}|\e_{1:t})$} cho \mat{$k>0$}
  
  đánh giá các chuỗi hành động có thể xảy ra;
  
  như lọc mà không có bằng chứng

\defn{Làm mịn}: \mat{$P(\X_k|\e_{1:t})$} cho \mat{$0\leq k < t$}
  
  ước tính tốt hơn về các trạng thái trong quá khứ, cần thiết cho việc học

\defn{Lời giải thích có khả năng nhất}: \mat{$\arg\max_{\sx_{1:t}} P(\x_{1:t}|\e_{1:t})$}
  
  nhận dạng giọng nói, giải mã với kênh ồn ào

---
## Lọc

Mục đích: nghĩ ra thuật toán ước lượng trạng thái *đệ quy*:
\mat{\[
  P(\X_{t+1}|\e_{1:t+1}) = f(\e_{t+1},P(\X_t|\e_{1:t}))
\]}
\mat{\begin{eqnarray*}
\lefteqn{P(\X_{t+1}|\e_{1:t+1}) = P(\X_{t+1}|\e_{1:t},\e_{t+1})} 

&=& 
  pha P(\e_{t+1}|\X_{t+1},\e_{1:t})P(\X_{t+1}|\e_{1:t}) 

&=& 
  pha P(\e_{t+1}|\X_{t+1})P(\X_{t+1}|\e_{1:t})
\end{eqnarray*}}
Tức là, \defn{dự đoán} + \defn{ước tính}. Dự đoán bằng cách tính tổng \mat{$\X_t$}:
\mat{\begin{eqnarray*}
\lefteqn{P(\X_{t+1}|\e_{1:t+1}) = 
   
  pha P(\e_{t+1}|\X_{t+1})
          \mysum_{\sx_t}P(\X_{t+1}|\x_t,\e_{1:t})P(\x_t|\e_{1:t})}

&=& 
  pha P(\e_{t+1}|\X_{t+1})
                \mysum_{\sx_t}P(\X_{t+1}|\x_t)P(\x_t|\e_{1:t})
\end{eqnarray*}}

\mat{$\f_{1:t+1} = \noprog{Forward}(\f_{1:t},\e_{t+1})$} trong đó \mat{$\f_{1:t}\eq P(\X_t|\e_{1:t})$}

Thời gian và không gian *hằng số* (độc lập với \mat{$t$})

---
## Ví dụ về lọc

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella-filter.png)

---
## Làm mịn

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/smoothing-dbn.png)

Chia bằng chứng \mat{$\e_{1:t}$} thành \mat{$\e_{1:k}$}, \mat{$\e_{k+1:t}$}:
\mat{\begin{eqnarray*}
P(\X_k|\e_{1:t}) & = & P(\X_k|\e_{1:k},\e_{k+1:t})\nonumber

   & = & 
  pha P(\X_k|\e_{1:k}) P(\e_{k+1:t}|\X_k,\e_{1:k}) 

   & = & 
  pha P(\X_k|\e_{1:k}) P(\e_{k+1:t}|\X_k) 

   & = & 
  pha \f_{1:k} \b_{k+1:t} 
\end{eqnarray*}}
Thông báo ngược được tính bằng đệ quy ngược:
\mat{\begin{eqnarray*}
P(\e_{k+1:t}|\X_k) 
   & = & \mysum_{\sx_{k+1}}P(\e_{k+1:t}|\X_k,\x_{k+1})P(\x_{k+1}|\X_k)  

   & = & \mysum_{\sx_{k+1}}P(\e_{k+1:t}|\x_{k+1})P(\x_{k+1}|\X_k)  

   & = & \mysum_{\sx_{k+1}}
           P(\e_{k+1}|\x_{k+1})P(\e_{k+2:t}|\x_{k+1})P(\x_{k+1}|\X_k)
\end{eqnarray*}}

---
## Ví dụ làm mịn

,72\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella-smooth.png)

Thuật toán \defn{Chuyển tiếp--lùi lại}: lưu các tin nhắn chuyển tiếp vào bộ đệm trong quá trình thực hiện 

Tuyến tính thời gian trong \mat{$t$} (suy luận polytree), không gian \mat{$O(t|\f|)$}

---
## Lời giải thích hợp lý nhất

Trình tự có khả năng xảy ra nhất \mat{$\neq$} trình tự của các trạng thái có khả năng xảy ra nhất!!!!

Đường dẫn có nhiều khả năng nhất đến từng \mat{$\x_{t+1}$} 
  
  = đường dẫn có khả năng xảy ra nhất tới *some* \mat{$\x_t$} cộng thêm một bước nữa
\mat{\begin{eqnarray*}
\lefteqn{\max_{\sx_1\ldots\sx_t} P(\x_1,\ldots,\x_t,\X_{t+1} | \e_{1:t+1})} 

   & = &  P(\e_{t+1} | \X_{t+1})
        \max_{\sx_t}\left( 
            P(\X_{t+1} | \x_t) 
            \max_{\sx_1\ldots\sx_{t-1}} P(\x_1,\ldots,\x_{t-1},\x_t | \e_{1:t})
        \right)
\end{eqnarray*}}
Giống hệt với bộ lọc, ngoại trừ \mat{$\f_{1:t}$} được thay thế bằng
\mat{\[ 
  \m_{1:t} = \max_{\sx_1\ldots\sx_{t-1}} P(\x_1,\ldots,\x_{t-1},\X_t | \e_{1:t}),
\]}
Tức là, \mat{$\m_{1:t}(i)$} đưa ra xác suất của đường dẫn có khả năng xảy ra nhất đến trạng thái \mat{$i$}.

Cập nhật có tổng được thay thế bằng max, tạo ra \defn{Thuật toán Viterbi}:
\mat{\[
  \m_{1:t+1} = P(\e_{t+1} | \X_{t+1})  \max_{\sx_t}\left(
            P(\X_{t+1} | \x_t) \m_{1:t}\right)
\]}

---
## Ví dụ về Viterbi

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella-paths.png)

---
## Mô hình Markov ẩn 

\mat{$\X_t$} là một biến riêng biệt (thường là \mat{$\E_t$})

Tên miền của \mat{$X_t$} là \mat{$\{1,\ldots,S\}$}

\defn{Ma trận chuyển tiếp} \mat{$\T_{ij} = P(X_t\eq j|X_{t-1}\eq i)$}, ví dụ: \mat{$\left(\begin{array}{cc}0.7 & 0.3 
 
                                                 0.3 & 0.7 \end{array}\right)$}

\defn{Ma trận cảm biến} \mat{$\O_t$} cho từng bước thời gian, các phần tử đường chéo \mat{$P(e_t|X_t\eq i)$}

ví dụ: với \mat{$U_1\eq true$}, \mat{$\O_1 = \left(\begin{array}{cc}0.9 & 0 
 0 & 0.2\end{array}\right)$}

Tin nhắn chuyển tiếp và lùi lại dưới dạng vectơ cột:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \b_{k+1:t} &=& \T \O_{k+1} \b_{k+2:t}
\end{eqnarray*}}
Thuật toán tiến lùi cần thời gian \mat{$O(S^2t)$} và không gian \mat{$O(St)$}

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance01.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance02.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance03.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance04.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance05.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance06.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance07.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance08.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance09.png)

---
## Thuật toán múa đồng quê

Có thể tránh lưu trữ tất cả các tin nhắn chuyển tiếp trong quá trình làm mịn bằng cách chạy 

thuật toán tiến lùi:
\mat{\begin{eqnarray*}
  \f_{1:t+1} &=& 
  pha \O_{t+1} \T\transpose \f_{1:t} 

  \O_{t+1}^{-1} \f_{1:t+1} &=& 
  pha \T\transpose \f_{1:t} 

  
  pha' (\T\transpose)^{-1} \O_{t+1}^{-1} \f_{1:t+1} &=&  \f_{1:t} 
\end{eqnarray*}}
Thuật toán: chuyền tiến tính \mat{$\f_t$}, chuyền lùi tính \mat{$\f_i$}, \mat{$\b_i$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/country-dance10.png)

---
## Bộ lọc Kalman

Hệ thống mô hình hóa được mô tả bởi một tập hợp các biến liên tục,
  
ví dụ: theo dõi một con chim đang bay---\mat{$\X_t\eq X, Y, Z, \dot X,\dot Y,\dot Z$}.
  
Máy bay, robot, hệ sinh thái, nền kinh tế, nhà máy hóa chất, hành tinh, \mat{$\ldots$}

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/kalman-network.png)

Gaussian trước, mô hình chuyển tiếp Gaussian tuyến tính và mô hình cảm biến

---
## Cập nhật phân phối Gaussian

Bước dự đoán: nếu \mat{$P(\X_t|\e_{1:t})$} là Gaussian thì dự đoán
\mat{\[
   P(\X_{t+1}|\e_{1:t}) =
  \int_{\sx_t}P(\X_{t+1}|\x_t)P(\x_t|\e_{1:t}) \,d\x_t
\]}
là Gaussian. Nếu \mat{$P(\X_{t+1}|\e_{1:t})$} là Gaussian thì phân phối được cập nhật
\mat{\[
  P(\X_{t+1}|\e_{1:t+1}) =
  
  pha P(\e_{t+1}|\X_{t+1}) P(\X_{t+1}|\e_{1:t})
\]}
là Gaussian

Do đó \mat{$P(\X_t|\e_{1:t})$} là Gaussian đa biến \mat{$N(\mean_t,\covariance_t)$} cho tất cả \mat{$t$}

Quy trình chung (phi tuyến tính, phi Gaussian):
mô tả phần sau phát triển *không giới hạn* như \mat{$t\rightarrow\infty$}

---
## Ví dụ 1-D đơn giản

Bước đi ngẫu nhiên Gaussian trên \mat{$X$}--axis, s.d. \mat{$\sigma_x$}, cảm biến s.d. \mat{$\sigma_z$}
\mat{\[
\mu_{t+1} = \frac{(\sigma_t^2+\sigma_x^2)z_{t+1} + \sigma_z^2\mu_t}
                   {\sigma_t^2+\sigma_x^2+\sigma_z^2}
 &nbsp;&nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;&nbsp;  
\sigma_{t+1}^2 = \frac{(\sigma_t^2+\sigma_x^2)\sigma_z^2}
                        {\sigma_t^2+\sigma_x^2+\sigma_z^2}
\]}

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/kalman-one-step.png)

---
## Cập nhật chung Kalman

Mô hình chuyển tiếp và cảm biến:
\mat{\[
\begin{array}{rcl}
  P(\x_{t+1}|\x_t) & = & N(\kftm \x_t,\kftv)(\x_{t+1}) 

  P(\z_t|\x_t) & = & N(\kfsm \x_t,\kfsv)(\z_t) 
\end{array}
\]}
\mat{$\kftm$} là ma trận chuyển tiếp; \mat{$\kftv$} hiệp phương sai nhiễu chuyển tiếp 

\mat{$\kfsm$} là ma trận cho các cảm biến; \mat{$\kfsv$} hiệp phương sai nhiễu cảm biến

Bộ lọc tính toán bản cập nhật sau:
\mat{\[
\begin{array}{rcl}
\mean_{t+1} &=& \kftm\mean_t + \kfgm_{t+1}(\z_{t+1} - \kfsm\kftm\mean_t)

\covariance_{t+1} &=& (\I-\kfgm_{t+1})(\kftm\covariance_t\kftm\transpose+\kftv)
\end{array}
\]}
trong đó \mat{$\kfgm_{t+1}\eq (\kftm\covariance_t\kftm\transpose+\kftv)
\kfsm\transpose(\kfsm(\kftm\covariance_t\kftm\transpose+\kftv)\kfsm\transpose+\kfsv)^{-1}$}

là \defn{ma trận khuếch đại Kalman}

\mat{$\covariance_t$} và \mat{$\kfgm_t$} độc lập với chuỗi quan sát, vì vậy hãy tính toán ngoại tuyến

---
## Ví dụ về theo dõi 2-D: lọc

![Hình ảnh](../TaiLieu/slide_md/figures/kalman-filtering.png)

---
## Ví dụ theo dõi 2-D: làm mịn

![Hình ảnh](../TaiLieu/slide_md/figures/kalman-smoothing.png)

---
## Nơi nó bị hỏng

Không thể áp dụng nếu mô hình chuyển đổi là phi tuyến

\defn{Bộ lọc Kalman mở rộng} chuyển đổi mô hình thành *tuyến tính cục bộ* xung quanh \mat{$\x_t\eq \mean_t$}

Không thành công nếu hệ thống cục bộ không mượt mà

\twofig{figures/kalman-bird1.ps}{figures/kalman-bird2.ps}

---
## Mạng Bayesian động

\mat{$\X_t$}, \mat{$\E_t$} chứa nhiều biến tùy ý trong mạng Bayes được sao chép

\twofig{figures/umbrella-1slice.ps}{figures/robot-dbn1.ps}

---
## DBN so với HMM

Mỗi HMM là một DBN một biến; mọi DBN rời rạc đều là HMM

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/dbn-vs-hmm.png)

Các phần phụ thuộc thưa thớt \mat{$\Rightarrow$} có ít tham số hơn theo cấp số nhân;
  
ví dụ: 20 biến trạng thái, mỗi biến có ba trạng thái cha 
  
DBN có tham số \mat{$20\stimes2^3\eq 160$}, HMM có \mat{$2^{20}\stimes 2^{20}\approx 10^{12}$}

---
##  Bộ lọc DBN so với Kalman 

Mọi mô hình bộ lọc Kalman đều là DBN, nhưng rất ít DBN là KF;

thế giới thực yêu cầu hậu nghiệm không phải Gaussian

Ví dụ: bin Laden và chìa khóa của tôi ở đâu? Sạc pin là gì?

\twofig{figures/robot-full-dbn.ps}{graphs/pin8.ps}

---
## Suy luận chính xác trong DBN

Phương pháp ngây thơ: \defn{ hủy đăng ký } mạng và chạy bất kỳ thuật toán chính xác nào

![Hình ảnh](../TaiLieu/slide_md/figures/dbn-unrolling.png)

Sự cố: chi phí suy luận cho mỗi bản cập nhật tăng theo \mat{$t$}

\defn{Lọc tổng hợp}: thêm lát \mat{$t+1$}, lát "tổng hợp" \mat{$t$} bằng cách sử dụng loại bỏ biến

Hệ số lớn nhất là \mat{$O(d^{n+1})$}, chi phí cập nhật \mat{$O(d^{n+2})$} 

(xem chi phí cập nhật HMM \mat{$O(d^{2n})$})

---
## Trọng số khả năng cho DBN

Tập hợp các mẫu có trọng số gần đúng với trạng thái niềm tin

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella5.png)

Các mẫu LW không chú ý đến bằng chứng!
    
   \mat{$\Rightarrow$} phân số "đồng ý" giảm theo cấp số nhân với \mat{$t$}
    
   \mat{$\Rightarrow$} số lượng mẫu cần thiết tăng theo cấp số nhân với \mat{$t$}

,4\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella-lw.png)

---
## Lọc hạt

Ý tưởng cơ bản: đảm bảo rằng quần thể mẫu (" hạt ")

theo dõi các vùng có khả năng xảy ra cao trong không gian trạng thái

Tái tạo các hạt tỷ lệ thuận với khả năng xảy ra đối với \mat{$\e_t$}

,7\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella-particle.png)

Được sử dụng rộng rãi để theo dõi các hệ thống phi tuyến, đặc biệt. trong tầm nhìn

Cũng được sử dụng để bản địa hóa và lập bản đồ đồng thời trong robot di động
  
 \mat{$10^5$} không gian trạng thái hai chiều

---
## Tiếp theo lọc hạt

Giả sử nhất quán tại thời điểm \mat{$t$}: \mat{$N(\x_t|\e_{1:t})/N = P(\x_t|\e_{1:t})$}

Tuyên truyền về phía trước: quần thể của \mat{$\x_{t+1}$} là
\mat{\[
  N(\x_{t+1}|\e_{1:t}) = \mysum_{\sx_t} P(\x_{t+1}|\x_t) N(\x_t|\e_{1:t})   
\]}
Trọng số mẫu theo khả năng của chúng đối với \mat{$\e_{t+1}$}:
\mat{\[
  W(\x_{t+1}|\e_{1:t+1}) = P(\e_{t+1}|\x_{t+1}) N(\x_{t+1}|\e_{1:t}) 
\]}
Lấy mẫu lại để thu được các quần thể tỷ lệ với \mat{$W$}:
\mat{\begin{eqnarray*}
  N(\x_{t+1}|\e_{1:t+1})/N 
    &=&  
  pha W(\x_{t+1}|\e_{1:t+1}) = 
  pha P(\e_{t+1}|\x_{t+1}) N(\x_{t+1}|\e_{1:t}) 

    &=&  
  pha P(\e_{t+1}|\x_{t+1}) 
            \mysum_{\sx_t} P(\x_{t+1}|\x_t) N(\x_t|\e_{1:t})

    &=&  
  pha' P(\e_{t+1}|\x_{t+1}) 
            \mysum_{\sx_t} P(\x_{t+1}|\x_t) P(\x_t|\e_{1:t}) 

    &=&  P(\x_{t+1}|\e_{1:t+1})
\end{eqnarray*}}

---
## Hiệu suất lọc hạt 

Lỗi gần đúng của quá trình lọc hạt vẫn bị giới hạn theo thời gian,

ít nhất là về mặt thực nghiệm---phân tích lý thuyết rất khó

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/comparison-lw-ersof.png)

---
## Tóm tắt

Các mô hình tạm thời sử dụng các biến trạng thái và cảm biến được sao chép theo thời gian

Giả định Markov và giả định về tính dừng, vì vậy chúng ta cần
  
 -- mô hình chuyển tiếp\mat{$P(\X_t|\X_{t-1})$}
  
 -- mẫu cảm biến \mat{$P(\E_t|\X_t)$}

Nhiệm vụ là lọc, dự đoán, làm mịn, trình tự rất có thể;

*tất cả được thực hiện đệ quy với chi phí không đổi trên mỗi bước thời gian*

Các mô hình Markov ẩn có một biến trạng thái riêng biệt; đã sử dụng 

để nhận dạng giọng nói

Bộ lọc Kalman cho phép các biến trạng thái \mat{$n$}, Gaussian tuyến tính, cập nhật \mat{$O(n^3)$}

Lưới Dynamic Bayes bao gồm các bộ lọc HMM, Kalman; cập nhật chính xác khó hiểu

Lọc hạt là một thuật toán lọc gần đúng tốt cho DBN

 

---
## Thuật toán đảo

Ý tưởng: chạy lưu trữ tiến-lùi \mat{$\f_t$}, \mat{$\b_t$} chỉ tại \mat{$k-1$} điểm 

Gọi đệ quy (theo chiều sâu) trên các nhiệm vụ con \mat{$k$}

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/island.png)

\mat{$O(k|\f|\log_k t)$} không gian, \mat{$O(k\log_k t)$} thêm thời gian 

---
## Làm mượt độ trễ cố định trực tuyến

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/fixed-lag-smoothing.png)

Phương pháp rõ ràng là chạy tiến--lùi cho các bước \mat{$d$} mỗi lần

Tính toán đệ quy \mat{$\f_{1:t-d+1},\ \b_{t-d+2:t+1}$} từ \mat{$\f_{1:t-d},\ \b_{t-d+1:t}$}?

Chuyển tiếp tin nhắn OK, tin nhắn ngược không thể nhận được trực tiếp

---
## Tiếp tục làm mịn độ trễ cố định trực tuyến.

Xác định \mat{$\B_{j:k} = \myprod_{i\eq j}^k \T \O_i$}, vì vậy 
\mat{\begin{eqnarray*}
  \b_{t-d+1:t} &=&  \B_{t-d+1:t} \ones

  \b_{t-d+2:t+1} &=&  \B_{t-d+2:t+1} \ones
\end{eqnarray*}}
Bây giờ chúng tôi có thể nhận được bản cập nhật đệ quy cho \mat{$\B$}:
\mat{\[
  \B_{t-d+2:t+1} = \O_{t-d+1}^{-1} \T^{-1} \B_{t-d+1:t} \T\O_{t+1}
\]}
Do đó chi phí cập nhật không đổi, không phụ thuộc vào độ trễ \mat{$d$}

---
## Suy luận gần đúng trong DBN

Lọc hạt (Gordon, 1994; Kanazawa, Koller và Russell, 1995; Blake và Isard, 1996)

Xấp xỉ nhân tố (Boyen và Koller, 1999)

Tuyên truyền vòng lặp (Pearl, 1988; Yedidia, Freeman và Weiss, 2000)

Xấp xỉ biến phân (Ghahramani và Jordan, 1997)

MCMC suy tàn (chưa được xuất bản)

---
## Đảo ngược bằng chứng

Tốt hơn nên đề xuất các mẫu mới dựa trên bằng chứng mới

Giảm thiểu phương sai của các ước tính hậu nghiệm (Kong \& Liu, 1996)

,75\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/umbrella5-er.png)

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/step-all-25.png)

---
## Ví dụ: DBN để nhận dạng giọng nói

![Hình ảnh](../TaiLieu/slide_md/figures/speech-dbn.png)

Cũng dễ dàng thêm các biến cho, ví dụ: giới tính, giọng nói, tốc độ.

Zweig và Russell (1998) cho thấy mức giảm lỗi tới 40

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Speech recognition (briefly)

## Chapter 15, Section 6

---
## Phác thảo

- Lời nói dưới dạng suy luận xác suất

- Âm thanh lời nói

- Phát âm từ

- Chuỗi từ

---
## Bài phát biểu dưới dạng suy luận xác suất

*Không dễ để phá hủy một bãi biển đẹp*

Tín hiệu giọng nói ồn ào, thay đổi, mơ hồ

Chuỗi từ *có khả năng nhất*, cho tín hiệu giọng nói là gì?
  
Tức là chọn \mat{$Words$} để tối đa hóa \mat{$P(Words|signal)$}

Sử dụng quy tắc Bayes:
\mat{\[
P(Words|signal) = 
  pha P(signal|Words) P(Words)
\]}
Tức là phân rã thành \defn{mô hình âm thanh} + \defn{mô hình ngôn ngữ}

\mat{$Words$} là chuỗi trạng thái ẩn, \mat{$signal$} là chuỗi quan sát

---
## Điện thoại

Tất cả lời nói của con người được tạo thành từ 40-50 \defn{điện thoại}, được xác định bởi 

cấu hình của \defn{khớp nối } (môi, răng, lưỡi, dây thanh âm, luồng không khí)

Hình thành mức độ trung gian của trạng thái ẩn giữa các từ và tín hiệu
    
  \mat{$\Rightarrow$} mô hình âm thanh = mô hình phát âm + mô hình điện thoại

ARPAbet được thiết kế cho tiếng Anh Mỹ

\newcommand{\bU}[1]{{\bf\underline{#1}}}

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|---|
| {[iy]} | b\bU{ea}t | [b] | \bU{b}et | [p] | \bU{p}et |
| {[ih]} | b\bU{i}t | [ch] | \bU{Ch}et | [r] | \bU{r}at |
| {[ey]} | b\bU{e}t | [d] | \bU{d}ebt | [s] | \bU{s}et |
| {[ao]} | b\bU{ough}t | [hh] | \bU{h}at | [th] | \bU{th}ick |
| {[ow]} | b\bU{oa}t | [hv] | \bU{h}igh | [dh] | \bU{th}at |
| {[er]} | B\bU{er}t | [l] | \bU{l}et | [w] | \bU{w}et |
| {[ix]} | ros\bU{e}s | [ng] | si\bU{ng} | [en] | butt\bU{on} |
| $\ \ \vdots$ | $\ \ \vdots$ | $\ \ \vdots$ | $\ \ \vdots$ | $\ \ \vdots$ | $\ \ \vdots$ |

Ví dụ: " trần " là [s iy l ih ng] / [s iy l ix ng] / [s iy l en]

---
## Âm thanh lời nói

Tín hiệu thô là độ dịch chuyển của micrô theo hàm thời gian;

được xử lý thành các khung hình 30ms \defn{} chồng chéo, mỗi khung được mô tả bởi \defn{features}

![Hình ảnh](../TaiLieu/slide_md/figures/sr-acoustic-frames.png)

Các tính năng của khung thường là \defn{formants} --- các đỉnh trong phổ công suất

---
## Mẫu điện thoại

Các tính năng của khung trong \mat{$P(features|phone)$} được tóm tắt bởi 
  
  -- một số nguyên trong \mat{$[0\ldots 255]$} (sử dụng lượng tử hóa vectơ \defn{}); hoặc 
  
  -- các tham số của hỗn hợp Gaussian

\defn{Điện thoại ba trạng thái}: mỗi điện thoại có ba giai đoạn (Khởi động, Giữa, Kết thúc)
  
 Ví dụ: [t] có Khởi phát im lặng, Mid bùng nổ, Kết thúc rít lên 
  
 $\Rightarrow$ \mat{$P(features|phone,phase)$}

\defn{Triphone context}: mỗi điện thoại trở thành \mat{$n^2$} điện thoại riêng biệt,
tùy thuộc vào điện thoại ở bên trái và bên phải
  
  Ví dụ: [t] trong "star" được viết là [t(s,aa)] (khác với "tar"!)

Triphones hữu ích để xử lý hiệu ứng \defn{coarticulation}: bộ phát âm
có quán tính và không thể chuyển đổi tức thời giữa các vị trí
  
Ví dụ: [t] trong "thứ tám" có lưỡi chạm vào răng cửa

---
## Ví dụ về mẫu điện thoại

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/sr-hmm.png)

---
## Mô hình phát âm từ

Mỗi từ được mô tả như một sự phân bố qua các chuỗi điện thoại

Phân phối được biểu diễn dưới dạng mô hình chuyển tiếp HMM

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/sr-tomato-b.png)

\mat{\begin{formula}
P([towmeytow]|\mbox{"tomato"}) = P([towmaatow]|\mbox{"tomato"}) = 0.1 

P([tahmeytow]|\mbox{"tomato"}) = P([tahmaatow]|\mbox{"tomato"}) = 0.4
\end{formula}}

Cấu trúc được tạo thủ công, xác suất chuyển tiếp được học từ dữ liệu

---
## Từ riêng biệt

Khả năng sửa lỗi kiểu điện thoại + kiểu từ \mat{$P(e_{1:t}|word)$} cho \defn{từ cô lập}
\mat{\[
P(word|e_{1:t}) = 
  pha P(e_{1:t}|word) P(word)
\]}
Xác suất trước \mat{$P(word)$} thu được đơn giản bằng cách đếm tần số từ

\mat{$P(e_{1:t}|word)$} có thể được tính toán đệ quy: xác định
\mat{\[
  \bell_{1:t}\eq P(\X_t,\e_{1:t})
\]}
và sử dụng bản cập nhật đệ quy
\mat{\[
  \bell_{1:t+1} = \noprog{Forward}(\ell_{1:t},\e_{t+1})
\]}
và sau đó \mat{$P(e_{1:t}|word) = \mysum_{\sx_t} \bell_{1:t}(\x_t)$}

Hệ thống đọc chính tả từng từ được đào tạo đạt độ chính xác 95--99\%

---
## Nói liên tục

Không chỉ là một chuỗi các vấn đề nhận dạng từ đơn lẻ!
  
-- Các từ liền kề có mối tương quan cao 
  
-- Chuỗi các từ có khả năng nhất $\neq$ Chuỗi các từ có khả năng nhất 
  
-- Phân đoạn: có rất ít khoảng trống trong lời nói
  
-- Kết hợp từ ngữ---ví dụ: "điều tiếp theo"

Hệ thống giọng nói liên tục quản lý độ chính xác 60--80\% vào một ngày đẹp trời

---
## Mô hình ngôn ngữ

Xác suất trước của một chuỗi từ được đưa ra theo quy tắc dây chuyền:
\mat{\[
P(w_{1}\cdots w_{n}) = \prod_{i=1}^{n} P(w_i|w_{1}\cdots w_{i-1})
\]}
\defn{Mô hình Bigram }:
\mat{\[
   P(w_i|w_{1}\cdots w_{i-1}) \approx P(w_i|w_{i-1})
\]}
Huấn luyện bằng cách đếm tất cả các cặp từ trong kho văn bản lớn

Các mô hình phức tạp hơn (bát quái, ngữ pháp, v.v.) sẽ giúp ích được đôi chút

---
## HMM kết hợp

Các trạng thái của kiểu ngôn ngữ+từ+điện thoại kết hợp được gắn nhãn bởi

từ chúng ta đang ở + số điện thoại trong từ đó + trạng thái điện thoại trong số điện thoại đó

Thuật toán Viterbi tìm chuỗi *trạng thái điện thoại* có khả năng nhất

Thực hiện phân đoạn bằng cách xem xét tất cả các chuỗi từ và ranh giới có thể có

Không phải lúc nào cũng đưa ra chuỗi từ có khả năng nhất vì

mỗi chuỗi từ là tổng của nhiều chuỗi trạng thái

Jelinek đã phát minh ra A$^*$ vào năm 1969 một cách để tìm chuỗi từ có khả năng xảy ra nhất
  
   trong đó " chi phí bước " là \mat{$-\log P(w_i|w_{i-1})$}

---
## DBN để nhận dạng giọng nói

![Hình ảnh](../TaiLieu/slide_md/figures/speech-dbn.png)

Cũng dễ dàng thêm các biến cho, ví dụ: giới tính, giọng nói, tốc độ.

Zweig và Russell (1998) cho thấy mức giảm lỗi tới 40

---
## Tóm tắt

Từ giữa những năm 1970, nhận dạng giọng nói đã được xây dựng dưới dạng suy luận xác suất

Bằng chứng = tín hiệu giọng nói, biến ẩn = chuỗi từ và âm thanh

Các hiệu ứng "Context" (coarticulation, v.v.) được xử lý bằng cách tăng cường trạng thái

Sự thay đổi trong lời nói của con người (tốc độ, âm sắc, v.v.) và tiếng ồn xung quanh

làm cho nhận dạng giọng nói liên tục trong cài đặt thực tế trở thành một vấn đề mở



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [OUPM](codeAndExercises/aima-pseudocode-master/md/oupm.md)
- [NET-VISA](codeAndExercises/aima-pseudocode-master/md/net-visa.md)
- [RADAR](codeAndExercises/aima-pseudocode-master/md/radar.md)
- [GENERATE-IMAGE](codeAndExercises/aima-pseudocode-master/md/generate-image.md)
- [GENERATE-MARKOV-LETTERS](codeAndExercises/aima-pseudocode-master/md/generate-markov-letters.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Dynamic Decision Network](codeAndExercises/aima-python-master/notebooks/dynamic_decision_network.ipynb)
- [Dynamic Decision Network (Python File)](codeAndExercises/aima-python-master/notebooks/dynamic_decision_network.py)


#### **Bài tập**

##### Bài tập 15.1

Show that any second-order Markov
process can be rewritten as a first-order Markov process with an
augmented set of state variables. Can this always be done
<i>parsimoniously</i>, i.e., without increasing the number of
parameters needed to specify the transition model?


---

##### Bài tập 15.2

In this exercise, we examine what
happens to the probabilities in the umbrella world in the limit of long
time sequences.<br>

1.  Suppose we observe an unending sequence of days on which the
    umbrella appears. Show that, as the days go by, the probability of
    rain on the current day increases monotonically toward a
    fixed point. Calculate this fixed point.<br>

2.  Now consider <i>forecasting</i> further and further into the
    future, given just the first two umbrella observations. First,
    compute the probability $P(r_{2+k}|u_1,u_2)$ for
    $k=1 \ldots 20$ and plot the results. You should see that
    the probability converges towards a fixed point. Prove that the
    exact value of this fixed point is 0.5.


---

##### Bài tập 15.3

This exercise develops a space-efficient variant of
the forward–backward algorithm described in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/forward-backward-algorithm.png">forward-backward-algorithm</a> (page <a class="pageRef" title="" href="#">forward-backward-algorithm</a>).
We wish to compute $\textbf{P} (\textbf{X}_k|\textbf{e}_{1:t})$ for
$k=1,\ldots ,t$. This will be done with a divide-and-conquer
approach.<br>

1.  Suppose, for simplicity, that $t$ is odd, and let the halfway point
    be $h=(t+1)/2$. Show that $\textbf{P} (\textbf{X}_k|\textbf{e}_{1:t}) $
     can be computed for
    $k=1,\ldots ,h$ given just the initial forward message
    $\textbf{f}_{1:0}$, the backward message $\textbf{b}_{h+1:t}$, and the evidence
    $\textbf{e}_{1:h}$.<br>

2.  Show a similar result for the second half of the sequence.<br>

3.  Given the results of (a) and (b), a recursive divide-and-conquer
    algorithm can be constructed by first running forward along the
    sequence and then backward from the end, storing just the required
    messages at the middle and the ends. Then the algorithm is called on
    each half. Write out the algorithm in detail.<br>

4.  Compute the time and space complexity of the algorithm as a function
    of $t$, the length of the sequence. How does this change if we
    divide the input into more than two pieces?<br>


---

##### Bài tập 15.4

On page <a class="pageRef" title="" href="#">flawed-viterbi-page</a>, we outlined a flawed
procedure for finding the most likely state sequence, given an
observation sequence. The procedure involves finding the most likely
state at each time step, using smoothing, and returning the sequence
composed of these states. Show that, for some temporal probability
models and observation sequences, this procedure returns an impossible
state sequence (i.e., the posterior probability of the sequence is
zero).


---

##### Bài tập 15.5

Equation (<a class="equationRef" title="" href="#">matrix-filtering-equation</a>) describes the
filtering process for the matrix formulation of HMMs. Give a similar
equation for the calculation of likelihoods, which was described
generically in Equation (<a class="equationRef" title="" href="#">forward-likelihood-equation</a>).


---

##### Bài tập 15.6

Consider the vacuum worlds of
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-maze-ch4-figure.png">vacuum-maze-ch4-figure</a> (perfect sensing) and
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-maze-hmm2-figure.png">vacuum-maze-hmm2-figure</a> (noisy sensing). Suppose
that the robot receives an observation sequence such that, with perfect
sensing, there is exactly one possible location it could be in. Is this
location necessarily the most probable location under noisy sensing for
sufficiently small noise probability $\epsilon$? Prove your claim or
find a counterexample.


---

##### Bài tập 15.7

In Section <a class="sectionRef" title="" href="#">hmm-localization-section</a>, the prior
distribution over locations is uniform and the transition model assumes
an equal probability of moving to any neighboring square. What if those
assumptions are wrong? Suppose that the initial location is actually
chosen uniformly from the northwest quadrant of the room and the action
actually tends to move southeast. Keeping
the HMM model fixed, explore the effect on localization and path
accuracy as the southeasterly tendency increases, for different values
of $\epsilon$.


---

##### Bài tập 15.8

Consider a version of the vacuum robot
(page <a class="pageRef" title="" href="#">vacuum-maze-hmm2-figure</a>) that has the policy of going straight for as long
as it can; only when it encounters an obstacle does it change to a new
(randomly selected) heading. To model this robot, each state in the
model consists of a <i>(location, heading)</i> pair. Implement
this model and see how well the Viterbi algorithm can track a robot with
this model. The robot’s policy is more constrained than the random-walk
robot; does that mean that predictions of the most likely path are more
accurate?


---

##### Bài tập 15.9

We have described three policies for the vacuum robot: (1) a uniform
random walk, (2) a bias for wandering southeast, as described in
Exercise <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_7/">hmm-robust-exercise</a>, and (3) the policy
described in Exercise <a href="#">roomba-viterbi-exercise</a>. Suppose
an observer is given the observation sequence from a vacuum robot, but
is not sure which of the three policies the robot is following. What
approach should the observer use to find the most likely path, given the
observations? Implement the approach and test it. How much does the
localization accuracy suffer, compared to the case in which the observer
knows which policy the robot is following?


---

##### Bài tập 15.10

This exercise is concerned with filtering in an environment with no
landmarks. Consider a vacuum robot in an empty room, represented by an
$n \times m$ rectangular grid. The robot’s location is hidden; the only
evidence available to the observer is a noisy location sensor that gives
an approximation to the robot’s location. If the robot is at location
$(x, y)$ then with probability .1 the sensor gives the correct location,
with probability .05 each it reports one of the 8 locations immediately
surrounding $(x, y)$, with probability .025 each it reports one of the
16 locations that surround those 8, and with the remaining probability
of .1 it reports “no reading.” The robot’s policy is to pick a direction
and follow it with probability .8 on each step; the robot switches to a
randomly selected new heading with probability .2 (or with probability 1
if it encounters a wall). Implement this as an HMM and do filtering to
track the robot. How accurately can we track the robot’s path?


---

##### Bài tập 15.11

This exercise is concerned with filtering in an environment with no
landmarks. Consider a vacuum robot in an empty room, represented by an
$n \times m$ rectangular grid. The robot’s location is hidden; the only
evidence available to the observer is a noisy location sensor that gives
an approximation to the robot’s location. If the robot is at location
$(x, y)$ then with probability .1 the sensor gives the correct location,
with probability .05 each it reports one of the 8 locations immediately
surrounding $(x, y)$, with probability .025 each it reports one of the
16 locations that surround those 8, and with the remaining probability
of .1 it reports “no reading.” The robot’s policy is to pick a direction
and follow it with probability .7 on each step; the robot switches to a
randomly selected new heading with probability .3 (or with probability 1
if it encounters a wall). Implement this as an HMM and do filtering to
track the robot. How accurately can we track the robot’s path?

<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/switching-kf.svg" alt="switching-kf-figure" id="switching-kf-figure" style="width:100%">
  <figcaption><center><b>A Bayesian network representation of a switching Kalman filter. The switching variable $S_t$ is a discrete state variable whose value determines
  the transition model for the continuous state variables $\textbf{X}_t$.
  For any discrete state $\textit{i}$, the transition model
  $\textbf{P}(\textbf{X}_{t+1}|\textbf{X}_t,S_t= i)$ is a linear Gaussian model, just as in a
  regular Kalman filter. The transition model for the discrete state,
  $\textbf{P}(S_{t+1}|S_t)$, can be thought of as a matrix, as in a hidden
  Markov model.</b></center></figcaption>
</figure>


---

##### Bài tập 15.12

Often, we wish to monitor a continuous-state
system whose behavior switches unpredictably among a set of $k$ distinct
“modes.” For example, an aircraft trying to evade a missile can execute
a series of distinct maneuvers that the missile may attempt to track. A
Bayesian network representation of such a <b>switching Kalman
filter</b> model is shown in
Figure <a class="insideExercisesFigRef"  href="#switching-kf-figure">switching-kf-figure</a>.<br><br>

1.  Suppose that the discrete state $S_t$ has $k$ possible values and
    that the prior continuous state estimate
    ${\textbf{P}}(\textbf{X}_0)$ is a multivariate
    Gaussian distribution. Show that the prediction
    ${\textbf{P}}(\textbf{X}_1)$ is a <b>mixture of
    Gaussians</b>—that is, a weighted sum of Gaussians such
    that the weights sum to 1.<br><br>

2.  Show that if the current continuous state estimate
    ${\textbf{P}}(\textbf{X}_t|\textbf{e}_{1:t})$ is a mixture of $m$ Gaussians,
    then in the general case the updated state estimate
    ${\textbf{P}}(\textbf{X}_{t+1}|\textbf{e}_{1:t+1})$ will be a mixture of
    $km$ Gaussians.<br><br>

3.  What aspect of the temporal process do the weights in the Gaussian
    mixture represent?<br><br>

The results in (a) and (b) show that the representation of the posterior
grows without limit even for switching Kalman filters, which are among
the simplest hybrid dynamic models.


---

##### Bài tập 15.13

Complete the missing step in the derivation
of Equation (<a class="equationRef" title="" href="#">kalman-one-step-equation</a>) on
page <a class="pageRef" title="" href="#">kalman-one-step-equation</a>, the first update step for the one-dimensional Kalman
filter.


---

##### Bài tập 15.14

Let us examine the behavior of the variance
update in Equation (<a class="equationRef" title="" href="#">kalman-univariate-equation</a>)
(page <a class="pageRef" title="" href="#">kalman-univariate-equation</a>).<br>

1.  Plot the value of $\sigma_t^2$ as a function of $t$, given various
    values for $\sigma_x^2$ and $\sigma_z^2$.<br>

2.  Show that the update has a fixed point $\sigma^2$ such that
    $\sigma_t^2 \rightarrow \sigma^2$ as $t \rightarrow \infty$, and
    calculate the value of $\sigma^2$.<br>

3.  Give a qualitative explanation for what happens as
    $\sigma_x^2\rightarrow 0$ and as $\sigma_z^2\rightarrow 0$.


---

##### Bài tập 15.15

A professor wants to know if students are getting
enough sleep. Each day, the professor observes whether the students
sleep in class, and whether they have red eyes. The professor has the
following domain theory:<br>

-   The prior probability of getting enough sleep, with no observations,
    is 0.7.<br>

-   The probability of getting enough sleep on night $t$ is 0.8 given
    that the student got enough sleep the previous night, and 0.3
    if not.<br>

-   The probability of having red eyes is 0.2 if the student got enough
    sleep, and 0.7 if not.<br>

-   The probability of sleeping in class is 0.1 if the student got
    enough sleep, and 0.3 if not.<br>

Formulate this information as a dynamic Bayesian network that the
professor could use to filter or predict from a sequence of
observations. Then reformulate it as a hidden Markov model that has only
a single observation variable. Give the complete probability tables for
the model.<br>


---

##### Bài tập 15.16

A professor wants to know if students are getting
enough sleep. Each day, the professor observes whether the students
sleep in class, and whether they have red eyes. The professor has the
following domain theory:<br>

-   The prior probability of getting enough sleep, with no observations,
    is 0.7.<br>

-   The probability of getting enough sleep on night $t$ is 0.8 given
    that the student got enough sleep the previous night, and 0.3
    if not.<br>

-   The probability of having red eyes is 0.2 if the student got enough
    sleep, and 0.7 if not.<br>

-   The probability of sleeping in class is 0.1 if the student got
    enough sleep, and 0.3 if not.<br>

Formulate this information as a dynamic Bayesian network that the
professor could use to filter or predict from a sequence of
observations. Then reformulate it as a hidden Markov model that has only
a single observation variable. Give the complete probability tables for
the model.<br>


---

##### Bài tập 15.17

For the DBN specified in Exercise <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_15/">sleep1-exercise</a> and
for the evidence values<br>

$\textbf{e}_1 = not\space red\space eyes,\space not\space sleeping\space in\space class$<br>
$\textbf{e}_2 = red\space eyes,\space not\space sleeping\space in\space class$<br>
$\textbf{e}_3 = red\space eyes,\space sleeping\space in\space class$<br>

perform the following computations:<br>

1.  State estimation: Compute $P({EnoughSleep}_t | \textbf{e}_{1:t})$ for each
    of $t = 1,2,3$.<br>

2.  Smoothing: Compute $P({EnoughSleep}_t | \textbf{e}_{1:3})$ for each of
    $t = 1,2,3$.<br>

3.  Compare the filtered and smoothed probabilities for $t=1$ and $t=2$.<br>


---

##### Bài tập 15.18

Suppose that a particular student shows up with red eyes and sleeps in
class every day. Given the model described in
Exercise <a class="exerciseRef" href="{{ site.baseurl }}/dbn-exercises/ex_15/">sleep1-exercise</a>, explain why the probability
that the student had enough sleep the previous night converges to a
fixed point rather than continuing to go down as we gather more days of
evidence. What is the fixed point? Answer this both numerically (by
computation) and analytically.


---

##### Bài tập 15.19

This exercise analyzes in more detail the
persistent-failure model for the battery sensor in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/battery-persistence-figure.png">battery-persistence-figure</a>(a)
(page <a class="pageRef" title="" href="#">battery-persistence-figure</a>).<br>

1.  Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/battery-persistence-figure.png">battery-persistence-figure</a>(b) stops at
    $t=32$. Describe qualitatively what should happen as
    $t\to\infty$ if the sensor continues to read 0.<br>

2.  Suppose that the external temperature affects the battery sensor in
    such a way that transient failures become more likely as
    temperature increases. Show how to augment the DBN structure in
    Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/battery-persistence-figure.png">battery-persistence-figure</a>(a), and explain
    any required changes to the CPTs.<br>

3.  Given the new network structure, can battery readings be used by the
    robot to infer the current temperature?<br>


---

##### Bài tập 15.20

Consider applying the variable elimination
algorithm to the umbrella DBN unrolled for three slices, where the query
is ${\textbf{P}}(R_3|u_1,u_2,u_3)$. Show that the space
complexity of the algorithm—the size of the largest factor—is the same,
regardless of whether the rain variables are eliminated in forward or
backward order.


---


<!-- tabs:end -->
