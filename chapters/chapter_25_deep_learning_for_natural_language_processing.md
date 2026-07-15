# Chapter 25 Deep learning for natural language processing

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_25_Deep%20learning%20for%20natural%20language%20processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_25_Deep%20learning%20for%20natural%20language%20processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Robotics

## Chapter 25

---
## Phác thảo

Robot, Cơ quan tác động và Cảm biến

Bản địa hóa và lập bản đồ

Lập kế hoạch chuyển động

Điều khiển động cơ

---
## Robot di động

 [Hình ảnh: \epsffile{figures/raibert-1leg.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/robocup.eps}] 

 [Hình ảnh: \epsffile{figures/raibert-1leg.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/robocup.eps}] 

---
## Bộ điều khiển 

,7\textwidth
[Hình ảnh: \fig{figures/stanford-arm.eps}]

Cấu hình của robot được xác định bởi 6 số
  
$\implies$ 6 \defn{bậc tự do} (DOF)

6 là số lượng tối thiểu cần thiết để định vị bộ phận tác động cuối một cách tùy ý.

Đối với các hệ thống động lực, hãy thêm vận tốc cho mỗi DOF.

---
## Robot không ba chiều

,4\textwidth
[Hình ảnh: \fig{figures/car-like.eps}]

Một chiếc ô tô có nhiều DOF (3) hơn điều khiển (2), nên \defn{non-holonomic};

nói chung không thể chuyển đổi giữa hai cấu hình cực kỳ gần nhau

---
## Cảm biến

\defn{Công cụ tìm phạm vi}: sonar (trên cạn, dưới nước), công cụ tìm phạm vi laser, radar (máy bay),[Hình ảnh: \epsffile{figures/robot0124bw.eps}]
cảm biến xúc giác, GPS

 [Hình ảnh: \epsffile{figures/sick.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/robot0124bw.eps}] 

\defn{Cảm biến hình ảnh}: camera (hình ảnh, hồng ngoại)

\defn{ Cảm biến bản quyền }: bộ giải mã trục (khớp, bánh xe), cảm biến quán tính, 

cảm biến lực, cảm biến mô-men xoắn

---
## Bản địa hóa---Tôi đang ở đâu?

Tính toán vị trí và hướng hiện tại (\defn{pose}) dựa trên các quan sát:

,7\textwidth
[Hình ảnh: \fig{figures/robotics-ddn.eps}]

---
## Tiếp theo bản địa hóa

\twofig{figures/robotics-pic2.eps}{figures/range-scan-model.eps}

Giả sử nhiễu Gaussian trong dự đoán chuyển động, đo phạm vi cảm biến

---
## Tiếp theo bản địa hóa

Có thể sử dụng tính năng lọc hạt để tạo ra ước tính vị trí gần đúng

\threefig{figures/first.ps}{figures/second.ps}{figures/third.ps}

---
## Tiếp theo bản địa hóa

Cũng có thể sử dụng bộ lọc Kalman mở rộng \defn{} cho các trường hợp đơn giản:

,75\textwidth
[Hình ảnh: \fig{figures/robotics-pic6.eps}]

Giả sử rằng các điểm mốc là *có thể nhận dạng được*---nếu không,
sau là đa phương thức

---
## Ánh xạ

Bản địa hóa: bản đồ đã cho và các mốc quan sát, cập nhật phân bổ tư thế

Lập bản đồ: tư thế đã cho và các mốc quan sát, cập nhật phân bổ bản đồ

SLAM: đưa ra các mốc quan sát, cập nhật tư thế và phân bổ bản đồ

Công thức xác suất của SLAM: 
  
 thêm các vị trí mốc $L_1,\ldots,L_k$ vào vectơ trạng thái,
  
 tiến hành như đối với việc bản địa hóa

---
## Tiếp theo ánh xạ 

 &nbsp;&nbsp;&nbsp;&nbsp; 

\epsfysize=0,37\textheight![Hình ảnh](../TaiLieu/slide_md/figures/arena033.png) &nbsp;&nbsp;&nbsp;&nbsp; \epsfysize=0,37\textheight![Hình ảnh](../TaiLieu/slide_md/figures/arena034.png)
\epsfysize=0,37\textheight![Hình ảnh](../TaiLieu/slide_md/figures/arena033.png) &nbsp;&nbsp;&nbsp;&nbsp; \epsfysize=0,37\textheight![Hình ảnh](../TaiLieu/slide_md/figures/arena034.png)

---
## Ví dụ về bản đồ 3D

\twofig{figures/mine-robot.eps}{figures/mine-data.eps}

---
## Lập kế hoạch chuyển động

Ý tưởng: sơ đồ trong không gian cấu hình \defn{} được xác định bởi DOF của robot

[Hình ảnh: \epsffile{figures/armExampleConfSpace.eps}]

 [Hình ảnh: \epsffile{figures/armExampleWorkSpace.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/armExampleConfSpace.eps}] 

Giải là quỹ đạo điểm trong không gian C tự do

---
## Quy hoạch không gian cấu hình

Vấn đề cơ bản: $\infty^d$ khẳng định! Chuyển đổi sang không gian trạng thái *hữu hạn*.

\defn{Phân hủy tế bào}:
  
  chia không gian thành các ô \defn{đơn giản}, 
  
  mỗi trong số đó có thể được duyệt qua một cách “dễ dàng” (ví dụ: lồi)

\defn{ Khung xương }: 
  
  xác định số lượng hữu hạn các điểm/đường được kết nối dễ dàng
  
  tạo thành một biểu đồ sao cho hai điểm bất kỳ được kết nối
  
  bởi một đường dẫn trên đồ thị

---
## Ví dụ về phân hủy ô

 &nbsp;&nbsp;&nbsp;&nbsp; 

 [Hình ảnh: \epsffile{figures/armDPwithoutPotentialWorkspaceCoarse.eps}]  &nbsp;&nbsp;&nbsp;&nbsp;  [Hình ảnh: \epsffile{figures/armDPwithoutPotentialCoarse.eps}] 

Sự cố: có thể không có đường dẫn trong các ô không gian trống thuần túy

Giải pháp: phân rã đệ quy các ô hỗn hợp (tự do + chướng ngại vật)

---
## Skeletonization: Sơ đồ Voronoi

Sơ đồ Voronoi: quỹ tích các điểm cách đều chướng ngại vật

,44\textwidth
[Hình ảnh: \fig{figures/armVoronoi.eps}]

Vấn đề: không mở rộng tốt sang các kích thước cao hơn

---
## Skeletonization: Lộ trình xác suất

Lộ trình xác suất được tạo bằng cách tạo các điểm ngẫu nhiên trong
C-space và giữ chúng trong không gian tự do; tạo biểu đồ bằng cách tham gia
cặp theo đường thẳng

,44\textwidth
[Hình ảnh: \fig{figures/armRoadmap.eps}]

Vấn đề: cần tạo đủ điểm để đảm bảo rằng mọi
cặp điểm bắt đầu/mục tiêu được kết nối thông qua biểu đồ

---
## Điều khiển động cơ

Có thể xem vấn đề điều khiển động cơ dưới dạng vấn đề tìm kiếm

trong không gian trạng thái \note{dynamic} thay vì \note{kinematic}:
  
-- không gian trạng thái được xác định bởi $x_1,x_2,\ldots,\dot{x_1},\dot{x_2},\ldots$
  
-- liên tục, đa chiều (Sarcos hình người: 162 chiều)

Kiểm soát xác định: nhiều vấn đề có thể giải quyết chính xác

đặc biệt nếu tuyến tính, ít chiều, được biết chính xác, có thể quan sát được

Luật điều khiển \defn{đơn giản} có hiệu lực đối với các chuyển động cụ thể

Stochastic \defn{điều khiển tối ưu}: rất ít vấn đề có thể giải được chính xác
  
$\implies$ phương pháp gần đúng/thích ứng

---
## Điều khiển động cơ sinh học

Hệ thống điều khiển động cơ được đặc trưng bởi sự dư thừa lớn

Vô số quỹ đạo đạt được bất kỳ nhiệm vụ nhất định nào

Ví dụ: cánh tay 3 liên kết di chuyển trong mặt phẳng ném vào mục tiêu
    
  bộ điều khiển 12 tham số đơn giản, một bậc tự do tại mục tiêu
    
  Không gian liên tục 11 chiều của bộ điều khiển tối ưu

Ý tưởng: nếu cánh tay ồn ào, chỉ có chính sách tối ưu " một "
giảm thiểu sai sót ở mục tiêu

Tức là, khả năng chịu tiếng ồn có thể giải thích hành vi vận động thực tế

Harris \& Wolpert (*Nature*, 1998): nhiễu phụ thuộc vào tín hiệu

giải thích hồ sơ vận tốc mắt chớp một cách hoàn hảo

---
## Cài đặt

Giả sử một bộ điều khiển có các tham số điều khiển "dự kiến" $\theta_0$

bị hỏng do nhiễu, tạo ra $\theta$ được rút ra từ $P_{\theta_0}$

Đầu ra (ví dụ: khoảng cách từ mục tiêu) $y = F(\theta)$; 

,7\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/arm-setup.png)

---
## Thuật toán học đơn giản: Độ dốc ngẫu nhiên

Giảm thiểu $E_{\theta}[y^2]$ bằng cách giảm độ dốc:
\begin{eqnarray*}
\nabla_{\theta_0} E_{\theta}[y^2]
  &=&  \nabla_{\theta_0} \int P_{\theta_0}(\theta)F(\theta)^2 d\theta 

  &=&  \int \frac{\nabla_{\theta_0} P_{\theta_0}(\theta)}{P_{\theta_0}(\theta)}
            F(\theta)^2 P_{\theta_0}(\theta)d\theta 

  &=&  E_{\theta}[\frac{\nabla_{\theta_0} P_{\theta_0}(\theta)}
                       {P_{\theta_0}(\theta)}
                  y^2]
\end{eqnarray*}
Cho mẫu $(\theta_j,y_j)$, $j=1,\ldots,N$, ta có
\[
  \hat{\nabla_{\theta_0} E_{\theta}[y^2]} =
  \frac{1}{N}\sum_{j=1}^N
     \frac{\nabla_{\theta_0} P_{\theta_0}(\theta_j)}
                       {P_{\theta_0}(\theta_j)}
                  y_j^2
\]
Đối với nhiễu Gaussian có hiệp phương sai $\Sigma$, tức là
$P_{\theta_0}(\theta) = N(\theta_0,\Sigma)$, chúng tôi thu được
\[
  \hat{\nabla_{\theta_0} E_{\theta}[y^2]} =
  \frac{1}{N}\sum_{j=1}^N \Sigma^{-1}(\theta_j - \theta_0) y_j^2
\]

---
## Thuật toán đang làm gì

,7\maxfigwidth
![Hình ảnh](../TaiLieu/slide_md/figures/control-noise-distort.png)

---
## Kết quả cho bộ điều khiển 2--D

,75\textwidth
 ![Hình ảnh](../TaiLieu/slide_md/figures/progress3-theta.png) 

---
## Kết quả cho bộ điều khiển 2--D

,75\textwidth
 ![Hình ảnh](../TaiLieu/slide_md/figures/progress3-theta-zoom.png) 

---
## Kết quả cho bộ điều khiển 2--D

,75\textwidth
 ![Hình ảnh](../TaiLieu/slide_md/figures/progress3-score.png) 

---
## Tóm tắt

Cao su rơi xuống đường

Robot di động và người thao tác

Bậc tự do xác định cấu hình robot

Bản địa hóa và ánh xạ dưới dạng các vấn đề suy luận xác suất
  
  (yêu cầu mô hình cảm biến và chuyển động tốt)

Lập kế hoạch chuyển động trong không gian cấu hình
  
  yêu cầu một số phương pháp để hoàn thiện



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**

##### Bài tập 25.1

Monte Carlo localization is
<i>biased</i> for any finite sample size—i.e., the expected
value of the location computed by the algorithm differs from the true
expected value—because of the way particle filtering works. In this
question, you are asked to quantify this bias.<br>

To simplify, consider a world with four possible robot locations:
$X=\{x_1,x_2,x_3,x_4\}$. Initially, we
draw $N\geq {{\rm 1}}$ samples uniformly from among those locations. As
usual, it is perfectly acceptable if more than one sample is generated
for any of the locations $X$. Let $Z$ be a Boolean sensor variable
characterized by the following conditional probabilities:<br>


$$\begin{aligned}
P(z | x_1) = 0.8 \qquad\qquad P(z | x_1) = 0.2  \\
P(z | x_2) = 0.4 \qquad\qquad P(z | x_2) = 0.6  \\
P(z | x_3) = 0.1 \qquad\qquad P(z | x_3) = 0.9  \\
P(z | x_4) = 0.1 \qquad\qquad P(z | x_4) = 0.9 
\end{aligned}$$


<br>

MCL uses these probabilities to generate particle weights, which are
subsequently normalized and used in the resampling process. For
simplicity, let us assume we generate only one new sample in the
resampling process, regardless of $N$. This sample might correspond to
any of the four locations in $X$. Thus, the sampling process defines a
probability distribution over $X$.<br>

1.  What is the resulting probability distribution over $X$ for this new
    sample? Answer this question separately for
    $N=1,\ldots,10$, and for $N=\infty$.<br>

2.  The difference between two probability distributions $P$ and $Q$ can
    be measured by the KL divergence, which is defined as
    $${KL}(P,Q) = \sum_i P(x_i)\log\frac{P(x_i)}{Q(x_i)}\ .$$ What are
    the KL divergences between the distributions in (a) and the true
    posterior?<br>

3.  What modification of the problem formulation (not the algorithm!)
    would guarantee that the specific estimator above is unbiased even
    for finite values of $N$? Provide at least two such modifications
    (each of which should be sufficient).<br>


---

##### Bài tập 25.2

Implement Monte Carlo localization for a
simulated robot with range sensors. A grid map and range data are
available from the code repository at
<a href="http://aima.cs.berkeley.edu">aima.cs.berkeley.edu</a>. You should demonstrate
successful global localization of the robot.

<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/figRobot2.svg" alt="figRobot2" id="figRobot2" style="width:100%">
  <figcaption><center><b>A Robot manipulator in two of its possible configurations.</b></center></figcaption>
</figure>


---

##### Bài tập 25.3

Consider a robot with two simple manipulators, as
shown in figure <a href="#figRobot2">figRobot2</a>. Manipulator A is a square block of side 2
which can slide back and on a rod that runs along the x-axis from
x=$-$10 to x=10. Manipulator B is a square block of side 2 which can
slide back and on a rod that runs along the y-axis from y=-10 to y=10.
The rods lie outside the plane of manipulation, so the rods do not
interfere with the movement of the blocks. A configuration is then a
pair ${\langle}x,y{\rangle}$ where $x$ is the x-coordinate of the center
of manipulator A and where $y$ is the y-coordinate of the center of
manipulator B. Draw the configuration space for this robot, indicating
the permitted and excluded zones.


---

##### Bài tập 25.4

Suppose that you are working with the robot in
Exercise <a class="exerciseRef" href="{{ site.baseurl }}/nlp-english-exercises/ex_3/">AB-manipulator-ex</a> and you are given the
problem of finding a path from the starting configuration of
figure <a class="insideExercisesFigRef" href="#figRobot2">figRobot2</a> to the ending configuration. Consider a potential
function $$D(A, {Goal})^2 + D(B, {Goal})^2 + \frac{1}{D(A, B)^2}$$
where $D(A,B)$ is the distance between the closest points of A and B.<br>

1.  Show that hill climbing in this potential field will get stuck in a
    local minimum.<br>

2.  Describe a potential field where hill climbing will solve this
    particular problem. You need not work out the exact numerical
    coefficients needed, just the general form of the solution. (Hint:
    Add a term that “rewards" the hill climber for moving A out of B’s
    way, even in a case like this where this does not reduce the
    distance from A to B in the above sense.)<br>


---

##### Bài tập 25.5

Consider the robot arm shown in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/FigArm1.png">FigArm1</a>. Assume that the robot’s base element is
60cm long and that its upper arm and forearm are each 40cm long. As
argued on page <a class="pageRef" title="" href="#">inverse-kinematics-not-unique</a>, the inverse kinematics of a robot is often
not unique. State an explicit closed-form solution of the inverse
kinematics for this arm. Under what exact conditions is the solution
unique?


---

##### Bài tập 25.6

Consider the robot arm shown in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/FigArm1.png">FigArm1</a>. Assume that the robot’s base element is
70cm long and that its upper arm and forearm are each 50cm long. As
argued on page <a class="pageRef" title="" href="#">inverse-kinematics-not-unique</a>, the inverse kinematics of a robot is often
not unique. State an explicit closed-form solution of the inverse
kinematics for this arm. Under what exact conditions is the solution
unique?


---

##### Bài tập 25.7

Implement an algorithm for calculating the Voronoi
diagram of an arbitrary 2D environment, described by an $n\times n$
Boolean array. Illustrate your algorithm by plotting the Voronoi diagram
for 10 interesting maps. What is the complexity of your algorithm?


---

##### Bài tập 25.8

This exercise explores the relationship between
workspace and configuration space using the examples shown in
Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>.

1.  Consider the robot configurations shown in
    Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(a) through (c), ignoring the obstacle
    shown in each of the diagrams. Draw the corresponding arm
    configurations in configuration space. (<i>Hint:</i> Each
    arm configuration maps to a single point in configuration space, as
    illustrated in Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigArm1</a>(b).)<br>

2.  Draw the configuration space for each of the workspace diagrams in
    Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(a)–(c). (<i>Hint:</i> The
    configuration spaces share with the one shown in
    Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(a) the region that corresponds to
    self-collision, but differences arise from the lack of enclosing
    obstacles and the different locations of the obstacles in these
    individual figures.)<br>

3.  For each of the black dots in Figure <a href="#">FigEx2</a>(e)–(f),
    draw the corresponding configurations of the robot arm in workspace.
    Please ignore the shaded regions in this exercise.<br>

4.  The configuration spaces shown in
    Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(e)–(f) have all been generated by a
    single workspace obstacle (dark shading), plus the constraints
    arising from the self-collision constraint (light shading). Draw,
    for each diagram, the workspace obstacle that corresponds to the
    darkly shaded area.<br>

5.  Figure <a class="insideExercisesFigRef"  href="#FigEx2">FigEx2</a>(d) illustrates that a single planar
    obstacle can decompose the workspace into two disconnected regions.
    What is the maximum number of disconnected regions that can be
    created by inserting a planar obstacle into an obstacle-free,
    connected workspace, for a 2DOF robot? Give an example, and argue
    why no larger number of disconnected regions can be created. How
    about a non-planar obstacle?<br>

    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseRobot1.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(a)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseRobot3.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(b)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseRobot6.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(c)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseConf2.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(d)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseConf4.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(e)</b></center></figcaption>
    </figure>
    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/exerciseConf5.svg" alt="FigEx2" id="FigEx2" style="width:100%">
      <figcaption><center><b>(f)</b></center></figcaption>
    </figure>


---

##### Bài tập 25.9

Consider a mobile robot moving on a horizontal surface. Suppose that the
robot can execute two kinds of motions:<br>

-   Rolling forward a specified distance.<br>

-   Rotating in place through a specified angle.<br>

The state of such a robot can be characterized in terms of three
parameters ${\langle}x,y,\phi$, the x-coordinate and y-coordinate of the
robot (more precisely, of its center of rotation) and the robot’s
orientation expressed as the angle from the positive x direction. The
action “$Roll(D)$” has the effect of changing state ${\langle}x,y,\phi$
to ${\langle}x+D \cos(\phi), y+D \sin(\phi), \phi {\rangle}$, and the
action $Rotate(\theta)$ has the effect of changing state<br>
${\langle}x,y,\phi {\rangle}$ to
${\langle}x,y, \phi + \theta {\rangle}$.

1.  Suppose that the robot is initially at ${\langle}0,0,0 {\rangle}$
    and then executes the actions $Rotate(60^{\circ})$, $Roll(1)$,
    $Rotate(25^{\circ})$, $Roll(2)$. What is the final state of the
    robot?<br>

2.  Now suppose that the robot has imperfect control of its own
    rotation, and that, if it attempts to rotate by $\theta$, it may
    actually rotate by any angle between $\theta-10^{\circ}$ and
    $\theta+10^{\circ}$. In that case, if the robot attempts to carry
    out the sequence of actions in (A), there is a range of possible
    ending states. What are the minimal and maximal values of the
    x-coordinate, the y-coordinate and the orientation in the final
    state?<br>

3.  Let us modify the model in (B) to a probabilistic model in which,
    when the robot attempts to rotate by $\theta$, its actual angle of
    rotation follows a Gaussian distribution with mean $\theta$ and
    standard deviation $10^{\circ}$. Suppose that the robot executes the
    actions $Rotate(90^{\circ})$, $Roll(1)$. Give a simple argument
    that (a) the expected value of the location at the end is not equal
    to the result of rotating exactly $90^{\circ}$ and then rolling
    forward 1 unit, and (b) that the distribution of locations at the
    end does not follow a Gaussian. (Do not attempt to calculate the
    true mean or the true distribution.)<br>

    The point of this exercise is that rotational uncertainty quickly
    gives rise to a lot of positional uncertainty and that dealing with
    rotational uncertainty is painful, whether uncertainty is treated in
    terms of hard intervals or probabilistically, due to the fact that
    the relation between orientation and position is both non-linear
    and non-monotonic.<br>
<figure>
  <img src="http://aimacode.github.io/aima-exercises/figures/robotics-pic7.svg" alt="FigEx3" id="FigEx3" style="width:100%">
    <figcaption><center><b>Simplified robot in a maze. See Exercise <a href="#">robot-exploration-exercise</a></b></center></figcaption>
</figure>


---

##### Bài tập 25.10

Consider the simplified robot shown in
Figure <a class="insideExercisesFigRef"  href="#FigEx3">FigEx3</a>. Suppose the robot’s Cartesian
coordinates are known at all times, as are those of its goal location.
However, the locations of the obstacles are unknown. The robot can sense
obstacles in its immediate proximity, as illustrated in this figure. For
simplicity, let us assume the robot’s motion is noise-free, and the
state space is discrete. Figure <a class="insideExercisesFigRef"  href="#FigEx3">FigEx3</a> is only one
example; in this exercise you are required to address all possible grid
worlds with a valid path from the start to the goal location.<br>

1.  Design a deliberate controller that guarantees that the robot always
    reaches its goal location if at all possible. The deliberate
    controller can memorize measurements in the form of a map that is
    being acquired as the robot moves. Between individual moves, it may
    spend arbitrary time deliberating.<br>

2.  Now design a <i>reactive</i> controller for the same task.
    This controller may not memorize past sensor measurements. (It may
    not build a map!) Instead, it has to make all decisions based on the
    current measurement, which includes knowledge of its own location
    and that of the goal. The time to make a decision must be
    independent of the environment size or the number of past
    time steps. What is the maximum number of steps that it may take for
    your robot to arrive at the goal?<br>

3.  How will your controllers from (a) and (b) perform if any of the
    following six conditions apply: continuous state space, noise in
    perception, noise in motion, noise in both perception and motion,
    unknown location of the goal (the goal can be detected only when
    within sensor range), or moving obstacles. For each condition and
    each controller, give an example of a situation where the robot
    fails (or explain why it cannot fail).<br>


---

##### Bài tập 25.11

In Figure <a class="insideExercisesFigRef" href="#">Fig5</a>(b) on
page <a class="pageRef" title="" href="#">Fig5</a>, we encountered an augmented finite state machine for
the control of a single leg of a hexapod robot. In this exercise, the
aim is to design an AFSM that, when combined with six copies of the
individual leg controllers, results in efficient, stable locomotion. For
this purpose, you have to augment the individual leg controller to pass
messages to your new AFSM and to wait until other messages arrive. Argue
why your controller is efficient, in that it does not unnecessarily
waste energy (e.g., by sliding legs), and in that it propels the robot
at reasonably high speeds. Prove that your controller satisfies the
dynamic stability condition given on page <a href="#">polygon-stability-condition-page</a>.


---

##### Bài tập 25.12

(This exercise was first devised by Michael
Genesereth and Nils Nilsson. It works for first graders through graduate
students.) Humans are so adept at basic household tasks that they often
forget how complex these tasks are. In this exercise you will discover
the complexity and recapitulate the last 30 years of developments in
robotics. Consider the task of building an arch out of three blocks.
Simulate a robot with four humans as follows:<br>

<b>Brain.</b> The Brain direct the hands in the execution of a
plan to achieve the goal. The Brain receives input from the Eyes, but
<i>cannot see the scene directly</i>. The brain is the only one
who knows what the goal is.<br>

<b>Eyes.</b> The Eyes report a brief description of the scene
to the Brain: “There is a red box standing on top of a green box, which
is on its side” Eyes can also answer questions from the Brain such as,
“Is there a gap between the Left Hand and the red box?” If you have a
video camera, point it at the scene and allow the eyes to look at the
viewfinder of the video camera, but not directly at the scene.<br>

<b>Left hand</b> and <b>right hand.</b> One person
plays each Hand. The two Hands stand next to each other, each wearing an
oven mitt on one hand, Hands execute only simple commands from the
Brain—for example, “Left Hand, move two inches forward.” They cannot
execute commands other than motions; for example, they cannot be
commanded to “Pick up the box.” The Hands must be
<i>blindfolded</i>. The only sensory capability they have is the
ability to tell when their path is blocked by an immovable obstacle such
as a table or the other Hand. In such cases, they can beep to inform the
Brain of the difficulty.


---


<!-- tabs:end -->
