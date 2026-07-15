\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Các mô hình xác suất theo thời gian (Temporal probability models)

## Chương 15, Phần 1--5

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