# Chapter 21 Learning Probalilistic models

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_21_Learning%20Probalilistic%20models/chapter_21_vi.html?v=3" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_21_Learning%20Probalilistic%20models.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Học thống kê (Statistical learning)

## Chương 20, Phần 1--3

---
## Phác thảo

- Học Bayes

- Tối đa *a posteriori* và khả năng học tập tối đa

- Học mạng Bayes
    
-- Học tham số ML với dữ liệu hoàn chỉnh
    
-- hồi quy tuyến tính

---
## Học Bayesian đầy đủ

Xem việc học dưới dạng cập nhật Bayesian của phân bố xác suất

trên không gian giả thuyết \defn{}

\mat{$H$} là biến giả thuyết, giá trị \mat{$h_1,h_2,\ldots$}, trước \mat{$P(H)$}

\mat{$j$}quan sát thứ \mat{$d_j$} đưa ra kết quả của biến ngẫu nhiên \mat{$D_j$}

dữ liệu huấn luyện \mat{$\d \eq d_1,\ldots,d_{\Ncount}$}

Với dữ liệu cho đến nay, mỗi giả thuyết có xác suất sau:
\mat{\[
  P(h_i|\d) = 
  pha P(\d|h_i) P(h_i)
\]}
trong đó \mat{$P(\d|h_i)$} được gọi là \defn{khả năng}

Các dự đoán sử dụng mức trung bình có trọng số khả năng đối với các giả thuyết:
\mat{\[
  P(X|\d) = \mysum_i\ P(X|\d,h_i) P(h_i|\d) = \mysum_i\ P(X|h_i) P(h_i|\d)
\]}
Không cần phải chọn một giả thuyết dự đoán tốt nhất!

---
## Ví dụ

Giả sử có năm loại túi kẹo:
  
10\% là \mat{$h_1$}: 100\% kẹo anh đào
  
20\% là \mat{$h_2$}: 75\% kẹo anh đào + 25\% kẹo chanh
  
40\% là \mat{$h_3$}: 50\% kẹo anh đào + 50\% kẹo chanh
  
20\% là \mat{$h_4$}: 25\% kẹo anh đào + 75\% kẹo chanh
  
10\% là \mat{$h_5$}: 100\% kẹo chanh

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/candy-kinds.png)

Sau đó, chúng tôi quan sát những viên kẹo được rút ra từ một số túi:  ![Hình ảnh](../TaiLieu/slide_md/figures/candy-obs.png)

Đó là loại túi gì? Kẹo tiếp theo sẽ có hương vị gì?

---
## Xác suất sau của giả thuyết

[Hình ảnh: \fig{graphs/limes-bayes-post.eps}]

---
## Xác suất dự đoán

[Hình ảnh: \fig{graphs/limes-bayes-pred.eps}]

---
## Xấp xỉ MAP

Tổng hợp không gian giả thuyết thường khó thực hiện 

(ví dụ: 18,446,744,073,709,551,616 hàm Boolean của 6 thuộc tính)

\defn{ Học tối đa sau } (MAP): chọn \mat{$h_{{\rm MAP}}$} tối đa hóa \mat{$P(h_i|\d)$}

Tức là tối đa hóa \mat{$P(\d|h_i)P(h_i)$} hoặc \mat{$\log P(\d|h_i) + \log P(h_i)$}

Thuật ngữ nhật ký có thể được xem là (phủ định của)
  
\note{bit để mã hóa dữ liệu cho giả thuyết} + \note{bit để mã hóa giả thuyết} 

Đây là ý tưởng cơ bản của việc học \defn{độ dài mô tả tối thiểu} (MDL)

Đối với các giả thuyết xác định, \mat{$P(\d|h_i)$} là 1 nếu nhất quán, 0 nếu không 
    
$\implies$ MAP = giả thuyết nhất quán đơn giản nhất (cf. science)

---
## Xấp xỉ ML

Đối với các tập dữ liệu lớn, trước trở nên không liên quan

\defn{Khả năng tối đa} (ML): chọn \mat{$h_{{\rm ML}}$} tối đa hóa \mat{$P(\d|h_i)$}

Tức là, chỉ cần lấy dữ liệu phù hợp nhất; giống hệt với MAP cho đồng phục trước

(điều này hợp lý nếu tất cả các giả thuyết đều có cùng độ phức tạp)

ML là phương pháp học thống kê "chuẩn" (không phải Bayesian)

---
## Học tham số ML trong mạng Bayes

Túi từ nhà sản xuất mới; phần \mat{$\theta$} của kẹo anh đào?in\raisebox{-1.25in[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/ml-network1.png)} 

Bất kỳ \mat{$\theta$} nào cũng có thể xảy ra: sự liên tục của các giả thuyết \mat{$h_{\theta}$} 

\mat{$\theta$} là tham số \defn{} cho dòng mô hình đơn giản (\note{binomial}) này 

Giả sử chúng ta mở gói \(\Ncount\) kẹo, \(c\) quả anh đào và \(\ell\eq \Ncount-c\) chanh

Đây là các quan sát \defn{i.i.d.} (độc lập, phân bố giống hệt nhau), vì vậy
\mat{\[
  P(\data |h_{\theta}) = \prod_{j\eq 1}^{\Ncount} P(\datum_j|h_{\theta}) =
  \theta^c\cdot (1-\theta)^{\ell}
\]}
Tối đa hóa w.r.t. \mat{$\theta$}---điều này dễ dàng hơn đối với \defn{log-likelihood}:
\mat{\begin{eqnarray*}
  L(\data |h_{\theta}) &=& \log P(\data |h_{\theta}) = \sum_{j\eq 1}^{\Ncount} \log P(\datum_j|h_{\theta}) =
  c\log\theta +  \ell\log(1-\theta) 

  \frac{dL(\data |h_{\theta})}{d\theta} &=& \frac{c}{\theta} -
  \frac{\ell}{1-\theta} = 0  &nbsp;&nbsp;&nbsp;&nbsp;  \implies  &nbsp;&nbsp;  \theta =
  \frac{c}{c+\ell} = \frac{c}{\Ncount}
\end{eqnarray*}}
Có vẻ hợp lý nhưng gây ra vấn đề với số 0!

---
## Nhiều tham số

Giấy gói màu đỏ/xanh phụ thuộc xác suất vào hương vị: \hspace*{0.75in}in\raisebox{-2.5in[0pt][0pt]{![Hình ảnh](../TaiLieu/slide_md/figures/ml-network2.png)} 

Ví dụ: khả năng xảy ra với kẹo anh đào trong giấy gói màu xanh lá cây:
\mat{\begin{eqnarray*}
\lefteqn{P(\J{F}\eq \J{cherry},\J{W}\eq \J{green}|h_{\theta,\theta_1,\theta_2})}

 & = & P(\J{F}\eq \J{cherry}|h_{\theta,\theta_1,\theta_2})P(\J{W}\eq
 \J{green}|\J{F}\eq \J{cherry},h_{\theta,\theta_1,\theta_2}) 

 & = & \theta \cdot (1-\theta_1)
\end{eqnarray*}}
\(\Ncount\) kẹo, \(r_c\) kẹo anh đào bọc đỏ, v.v.:
\mat{\begin{eqnarray*}
 P(\data|h_{\theta,\theta_1,\theta_2}) &=&
  \theta^c (1-\theta)^{\ell} \cdot \theta_1^{r_c}(1-\theta_1)^{g_c}
  \cdot \theta_2^{r_{\ell}}(1-\theta_2)^{g_{\ell}}
\end{eqnarray*}}
\mat{\begin{eqnarray*}
L &=&  [c\log \theta + \ell\log (1-\theta) ]  

  &+&   [r_c\log \theta_1 + g_c\log(1-\theta_1) ]  

  &+&   [r_{\ell}\log \theta_2 + g_{\ell}\log(1-\theta_2) ]
\end{eqnarray*}}

---
## Tiếp theo nhiều tham số.

Đạo hàm của \mat{$L$} chỉ chứa tham số liên quan:
\mat{\[\begin{array}{rclcl}
\displaystyle \frac{\partial L}{\partial\theta} &=& \displaystyle \frac{c}{\theta} - \displaystyle\frac{\ell}{1-\theta} = 0                  &  &nbsp;&nbsp;&nbsp;&nbsp;  \implies & \theta = \displaystyle \frac{c}{c+\ell} 
\end{array}\]}
\mat{\[\begin{array}{rclcl}
\displaystyle \frac{\partial L}{\partial\theta_1} &=& \displaystyle\frac{r_c}{\theta_1} - \displaystyle\frac{g_c}{1-\theta_1} = 0           &  &nbsp;&nbsp;&nbsp;&nbsp;  \implies & \theta_1 = \displaystyle\frac{r_c}{r_c+g_c} 
\end{array}\]}
\mat{\[\begin{array}{rclcl}
\displaystyle \frac{\partial L}{\partial\theta_2} &=& \displaystyle\frac{r_{\ell}}{\theta_2} - \displaystyle\frac{g_{\ell}}{1-\theta_2} = 0 &  &nbsp;&nbsp;&nbsp;&nbsp;  \implies & \theta_2 = \displaystyle\frac{r_{\ell}}{r_{\ell}+g_{\ell}}
\end{array}\]}
Với \defn{dữ liệu đầy đủ}, các tham số * có thể được học riêng *

---
## Ví dụ: mô hình Gaussian tuyến tính

\twofig{graphs/regression-model.eps}{graphs/regression-sample.eps}

Tối đa hóa \mat{$\displaystyle P(y|x) = \frac{1}{\sqrt{2 \pi} \sigma} e^{-\frac{(y-(\theta_1 x+\theta_2))^2}{2\sigma^2}}$} w.r.t. \mat{$\theta_1$}, \mat{$\theta_2$}

= giảm thiểu \mat{$\displaystyle E = \sum_{j\eq 1}^{\Ncount} (y_j-(\theta_1 x_j+\theta_2))^2$}

Nghĩa là, giảm thiểu tổng sai số bình phương sẽ mang lại giải pháp ML

để phù hợp tuyến tính *giả sử nhiễu Gaussian có phương sai cố định *

---
## Tóm tắt

Học tập Bayesian đầy đủ đưa ra dự đoán tốt nhất có thể nhưng khó thực hiện

Học MAP cân bằng độ phức tạp với độ chính xác trên dữ liệu đào tạo 

Khả năng tối đa giả định thống nhất trước đó, OK đối với các tập dữ liệu lớn

1. Chọn một nhóm mô hình được tham số hóa để mô tả dữ liệu

\note{*yêu cầu cái nhìn sâu sắc đáng kể và đôi khi là các mô hình mới*

2. Viết ra khả năng xảy ra của dữ liệu dưới dạng hàm của các tham số

\note{*có thể yêu cầu tính tổng các biến ẩn, tức là suy luận*

3. Viết đạo hàm của log khả năng w.r.t. mỗi tham số

4. Tìm các giá trị tham số sao cho đạo hàm bằng 0

\note{*có thể khó/không thể; trợ giúp về kỹ thuật tối ưu hóa hiện đại*



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**

##### Bài tập 21.1

Implement a passive learning agent in a simple environment, such as the
$4\times 3$ world. For the case of an initially unknown environment
model, compare the learning performance of the direct utility
estimation, TD, and ADP algorithms. Do the comparison for the optimal
policy and for several random policies. For which do the utility
estimates converge faster? What happens when the size of the environment
is increased? (Try environments with and without obstacles.)


---

##### Bài tập 21.2

Chapter <a class="chapterRef" href="{{site.baseurl}}/concept-decisions-exercise/">complex-decisions-chapter</a> defined a
<b>proper policy</b> for an MDP as one that is
guaranteed to reach a terminal state. Show that it is possible for a
passive ADP agent to learn a transition model for which its policy $\pi$
is improper even if $\pi$ is proper for the true MDP; with such models,
the POLICY-EVALUATION step may fail if $\gamma{{\,=\,}}1$. Show that this problem cannot
arise if POLICY-EVALUATION is applied to the learned model only at the end of a trial.


---

##### Bài tập 21.3

Starting with the passive ADP agent,
modify it to use an approximate ADP algorithm as discussed in the text.
Do this in two steps:<br>

1.  Implement a priority queue for adjustments to the utility estimates.
    Whenever a state is adjusted, all of its predecessors also become
    candidates for adjustment and should be added to the queue. The
    queue is initialized with the state from which the most recent
    transition took place. Allow only a fixed number of adjustments.<br>

2.  Experiment with various heuristics for ordering the priority queue,
    examining their effect on learning rates and computation time.


---

##### Bài tập 21.4

The direct utility estimation method in
Section <a class="sectionRef" title="" href="#">passive-rl-section</a> uses distinguished terminal
states to indicate the end of a trial. How could it be modified for
environments with discounted rewards and no terminal states?


---

##### Bài tập 21.5

Write out the parameter update equations for TD learning with
$$\hat{U}(x,y) = \theta_0 + \theta_1 x + \theta_2 y + \theta_3\,\sqrt{(x-x_g)^2 + (y-y_g)^2}\ .$$


---

##### Bài tập 21.6

Adapt the vacuum world (Chapter <a class="chapterRef" href="{{site.baseurl}}/agents-exercises/">agents-chapter</a> for
reinforcement learning by including rewards for squares being clean.
Make the world observable by providing suitable percepts. Now experiment
with different reinforcement learning agents. Is function approximation
necessary for success? What sort of approximator works for this
application?


---

##### Bài tập 21.7

Implement an exploring reinforcement learning
agent that uses direct utility estimation. Make two versions—one with a
tabular representation and one using the function approximator in
Equation (<a class="equationRef" title="" href="#">4x3-linear-approx-equation</a>). Compare their
performance in three environments:<br>

1.  The $4\times 3$ world described in the chapter.<br>

2.  A ${10}\times {10}$ world with no obstacles and a +1 reward
    at (10,10).<br>

3.  A ${10}\times {10}$ world with no obstacles and a +1 reward
    at (5,5).


---

##### Bài tập 21.8

Devise suitable features for reinforcement learning in stochastic grid
worlds (generalizations of the $4\times 3$ world) that contain multiple
obstacles and multiple terminal states with rewards of $+1$ or $-1$.


---

##### Bài tập 21.9

Extend the standard game-playing environment
(Chapter <a class="chapterRef" href="{{site.baseurl}}/game-playing-exercises/">game-playing-chapter</a>) to incorporate a reward
signal. Put two reinforcement learning agents into the environment (they
may, of course, share the agent program) and have them play against each
other. Apply the generalized TD update rule
(Equation (<a class="equationRef" title="" href="#">generalized-td-equation</a>)) to update the
evaluation function. You might wish to start with a simple linear
weighted evaluation function and a simple game, such as tic-tac-toe.


---

##### Bài tập 21.10

Compute the true utility function and the best linear
approximation in $x$ and $y$ (as in
Equation (<a class="equationRef" title="" href="#">4x3-linear-approx-equation</a>)) for the
following environments:<br>

1.  A ${10}\times {10}$ world with a single $+1$ terminal state
    at (10,10).<br>

2.  As in (a), but add a $-1$ terminal state at (10,1).<br>

3.  As in (b), but add obstacles in 10 randomly selected squares.<br>

4.  As in (b), but place a wall stretching from (5,2) to (5,9).<br>

5.  As in (a), but with the terminal state at (5,5).<br>

The actions are deterministic moves in the four directions. In each
case, compare the results using three-dimensional plots. For each
environment, propose additional features (besides $x$ and $y$) that
would improve the approximation and show the results.


---

##### Bài tập 21.11

Implement the REINFORCE and PEGASUS algorithms and apply them to the $4\times 3$ world,
using a policy family of your own choosing. Comment on the results.


---

##### Bài tập 21.12

Investigate the application of reinforcement learning ideas to the
modeling of human and animal behavior.


---

##### Bài tập 21.13

Is reinforcement learning an appropriate abstract model for evolution?
What connection exists, if any, between hardwired reward signals and
evolutionary fitness?


---


<!-- tabs:end -->
