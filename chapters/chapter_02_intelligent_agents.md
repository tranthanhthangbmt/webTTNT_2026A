# Chapter 02 Intelligent Agents

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_02/chapter_02_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_02_Intelligent%20Agents.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage[dvips]{color}
\usepackage{aima2e-slides}

# Intelligent Agents

## Chapter 2

---
## Nhắc nhở

*Nhiệm vụ 0 (bồi dưỡng ngọn lửa nói ngọng) hạn chót vào ngày 28/1*

*Hướng dẫn Lisp/emacs/AIMA*: 1-11 hôm nay và thứ Hai, 271 Soda

---
## Phác thảo

- Tác nhân và môi trường

- Tính hợp lý

- PEAS (Đo hiệu suất, Môi trường, Bộ truyền động, Cảm biến)

- Các loại môi trường

- Các loại tác nhân

---
## Tác nhân và môi trường

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/agent-environment.png)

\defn{Đại lý} bao gồm con người, robot, robot mềm, bộ điều nhiệt, v.v.

Hàm tác nhân \defn{} ánh xạ từ lịch sử nhận thức đến hành động:
\[f: {\cal P}^* \rightarrow {\cal A}\]
Chương trình tác nhân \defn{} chạy trên kiến trúc \defn{ vật lý} để tạo ra $f$

---
## Thế giới máy hút bụi

,65\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/vacuum2-environment.png)

Nhận thức: vị trí và nội dung, ví dụ: $[A,Dirty]$

Hành động: $Left$, $Right$, $Suck$, $NoOp$

---
## Chất làm sạch máy hút bụi 

| &nbsp; | &nbsp; |
|---|---|
| Percept sequence | Action |
| $[A,Clean]$ | $Right$ |
| $[A,Dirty]$ | $Suck$ |
| $[B,Clean]$ | $Left$ |
| $[B,Dirty]$ | $Suck$ |
| $[A,Clean]$, $[A,Clean]$ | $Right$ |
| $[A,Clean]$, $[A,Dirty]$ | $Suck$ |
| $\vdots$ | $\vdots$ |

\medskip

```text
function Reflex-Vacuum-Agent([location,status]) returns an action

    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

Chức năng *right* là gì? 

Nó có thể được thực hiện trong một chương trình đại lý nhỏ không?

---
## Tính hợp lý

Đã sửa lỗi \defn{đo lường hiệu suất} đánh giá trình tự môi trường \note{}
  
-- một điểm trên mỗi ô vuông được dọn sạch kịp thời $T$?
  
-- một điểm cho mỗi ô vuông sạch trong mỗi bước thời gian, trừ một điểm cho mỗi nước đi?
  
-- phạt cho ${}> k$ ô vuông bẩn?

Tác nhân hợp lý \txr{} chọn bất kỳ hành động nào tối đa hóa giá trị \txr{expected} của
thước đo hiệu suất \txr{ đưa ra trình tự nhận thức cho đến nay }

Hợp lý $\neq$ toàn trí 
    
   -- nhận thức có thể không cung cấp tất cả thông tin liên quan

Lý trí $\neq$ thấu thị 
    
   -- kết quả hành động có thể không như mong đợi

Do đó, hợp lý $\neq$ thành công

Hợp lý $\implies$ khám phá, học tập, tự chủ

---
## Đậu Hà Lan

Để thiết kế một tác nhân hợp lý, chúng ta phải chỉ định môi trường tác vụ \txr{}

Ví dụ, hãy xem xét nhiệm vụ thiết kế một chiếc taxi tự động:

<u>Thước đo hiệu suất</u>??

<u>Môi trường</u>??

<u>Bộ truyền động</u>??

<u>Cảm biến</u>??

---
## Đậu Hà Lan

Để thiết kế một tác nhân hợp lý, chúng ta phải chỉ định môi trường tác vụ \txr{}

Ví dụ, hãy xem xét nhiệm vụ thiết kế một chiếc taxi tự động:

<u>Đo lường hiệu quả hoạt động</u>?? an toàn, điểm đến, lợi nhuận, tính hợp pháp, sự thoải mái, $\ldots$

<u>Môi trường</u>?? Đường phố/đường cao tốc ở Hoa Kỳ, giao thông, người đi bộ, thời tiết, $\ldots$

<u>Thiết bị truyền động</u>?? tay lái, chân ga, phanh, còi, loa/màn hình, $\ldots$

<u>Cảm biến</u>?? video, gia tốc kế, đồng hồ đo, cảm biến động cơ, bàn phím, GPS, $\ldots$

---
## Đại lý mua sắm qua Internet

<u>Thước đo hiệu suất</u>??

<u>Môi trường</u>??

<u>Bộ truyền động</u>??

<u>Cảm biến</u>??

---
## Đại lý mua sắm qua Internet

<u>Thước đo hiệu suất</u>?? giá cả, chất lượng, sự phù hợp, hiệu quả

<u>Môi trường</u>?? Các trang web WWW, nhà cung cấp, chủ hàng hiện tại và tương lai

<u>Actuators</u>?? hiển thị cho người dùng, theo dõi URL, điền vào biểu mẫu

<u>Cảm biến</u>?? Trang HTML (văn bản, đồ họa, tập lệnh)

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? |  |  |  |  |
| <u>Xác định</u>?? |  |  |  |  |
| <u>Tập</u>?? |  |  |  |  |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? |  |  |  |  |
| <u>Tập</u>?? |  |  |  |  |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? |  |  |  |  |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? |  |  |  |  |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán | Bán | Không |
| <u>Rời rạc</u>?? |  |  |  |  |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán | Bán | Không |
| <u>Rời rạc</u>?? | Có | Có | Có | Không |
| <u>Đại lý đơn lẻ</u>?? |  |  |  |  |

---
## Loại môi trường

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|---|---|---|---|---|
|  | {Solitaire} | {Backgammon} | {Mua sắm trên Internet} | {Taxi} |
| <u>Có thể quan sát được</u>?? | Có | Có | Không | Không |
| <u>Xác định</u>?? | Có | Không | Một phần | Không |
| <u>Tập</u>?? | Không | Không | Không | Không |
| <u>Tĩnh</u>?? | Có | Bán | Bán | Không |
| <u>Rời rạc</u>?? | Có | Có | Có | Không |
| <u>Một đại lý</u>?? | Có | Không | Có (ngoại trừ đấu giá) | Không |

\bigskip

*Loại môi trường quyết định phần lớn thiết kế tác nhân*

Thế giới thực (tất nhiên) có thể quan sát được một phần, ngẫu nhiên, tuần tự,
năng động, liên tục, đa tác nhân

---
## Các loại tác nhân

Bốn loại cơ bản theo thứ tự tổng quát tăng dần:
  
-- tác nhân phản xạ đơn giản
  
-- tác nhân phản xạ có trạng thái
  
-- tác nhân dựa trên mục tiêu
  
-- đại lý dựa trên tiện ích

Tất cả những thứ này có thể được biến thành tác nhân học tập

---
## Các tác nhân phản xạ đơn giản

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/simple-reflex-agent.png)

---
## Ví dụ

\medskip

```text
function Reflex-Vacuum-Agent([location,status]) returns an action

    if status = Dirty then return Suck
    else if location = A then return Right
    else if location = B then return Left
```

\bigskip

```text
(setq joe (make-agent :name 'joe :body (make-agent-body)
                      :program (make-reflex-vacuum-agent-program)))

(defun make-reflex-vacuum-agent-program ()
  #'(lambda (percept)
      (let ((location (first percept)) (status (second percept)))
        (cond ((eq status 'dirty) 'Suck)
              ((eq location 'A) 'Right)
              ((eq location 'B) 'Left)))))
```

---
## Tác nhân phản xạ có trạng thái 

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/reflex+state-agent.png)

---
## Ví dụ

\medskip

```text
function Reflex-Vacuum-Agent([location,status]) returns an action
  static: last\_A,\ last\_B, numbers, initially infinity

    if status = Dirty then $\ldots$
```

\bigskip

```text
(defun make-reflex-vacuum-agent-with-state-program ()
  (let ((last-A infinity) (last-B infinity))
  #'(lambda (percept)
      (let ((location (first percept)) (status (second percept)))
        (incf last-A) (incf last-B)
        (cond 
         ((eq status 'dirty) 
          (if (eq location 'A) (setq last-A 0) (setq last-B 0))
          'Suck)
         ((eq location 'A) (if (> last-B 3) 'Right 'NoOp))
         ((eq location 'B) (if (> last-A 3) 'Left 'NoOp)))))))
```

---
## Tác nhân dựa trên mục tiêu

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/goal-based-agent.png)

---
## Tác nhân dựa trên tiện ích

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/utility-based-agent.png)

---
## Tác nhân học tập

,95\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/learning-agent.png)

---
## Tóm tắt

\defn{Tác nhân} tương tác với \defn{môi trường} thông qua
\defn{bộ truyền động} và cảm biến \defn{}

Hàm tác nhân \defn{} mô tả những gì tác nhân thực hiện trong mọi trường hợp

Thước đo hiệu suất \defn{} đánh giá trình tự môi trường

Tác nhân \defn{hoàn toàn hợp lý} tối đa hóa hiệu suất mong đợi 

\defn{Chương trình tác nhân} triển khai (một số) chức năng của tác nhân

Mô tả \defn{PEAS} xác định môi trường tác vụ

Môi trường được phân loại theo nhiều chiều:
    
  \defn{có thể quan sát được}? \defn{ xác định }? \defn{tập}? \defn{tĩnh}? 
  \defn{rời rạc}? \defn{đại lý đơn lẻ}?

Một số kiến trúc tác nhân cơ bản tồn tại:
    
  \defn{phản xạ}, \defn{phản xạ với trạng thái}, \defn{dựa trên mục tiêu}, 
  \defn{dựa trên tiện ích}



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [TABLE-DRIVEN-AGENT](codeAndExercises/aima-pseudocode-master/md/Table-Driven-Agent.md)
- [REFLEX-VACUUM-AGENT](codeAndExercises/aima-pseudocode-master/md/Reflex-Vacuum-Agent.md)
- [SIMPLE-REFLEX-AGENT](codeAndExercises/aima-pseudocode-master/md/Simple-Reflex-Agent.md)
- [MODEL-BASED-REFLEX-AGENT](codeAndExercises/aima-pseudocode-master/md/Model-Based-Reflex-Agent.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Agents](codeAndExercises/aima-python-master/notebooks/agents.ipynb)
- [Agents (Python File)](codeAndExercises/aima-python-master/notebooks/agents.py)
- [Vacuum World](codeAndExercises/aima-python-master/notebooks/vacuum_world.ipynb)
- [Vacuum World (Python File)](codeAndExercises/aima-python-master/notebooks/vacuum_world.py)


#### **Bài tập**

##### Bài tập 2.1

Suppose that the performance measure is concerned with just the first
$T$ time steps of the environment and ignores everything thereafter.
Show that a rational agent’s action may depend not just on the state of
the environment but also on the time step it has reached.


---

##### Bài tập 2.2

Let us examine the rationality of various
vacuum-cleaner agent functions.<br>
1.  Show that the simple vacuum-cleaner agent function described in
    Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-agent-function-table.png">vacuum-agent-function-table</a> is indeed
    rational under the assumptions listed on page <a class="pageRef" title="" href="#">vacuum-rationality-page</a><br>

2.  Describe a rational agent function for the case in which each
    movement costs one point. Does the corresponding agent program
    require internal state?<br>

3.  Discuss possible agent designs for the cases in which clean squares
    can become dirty and the geography of the environment is unknown.
    Does it make sense for the agent to learn from its experience in
    these cases? If so, what should it learn? If not, why not?<br>


---

##### Bài tập 2.3

Write an essay on the relationship between evolution and one or more of
autonomy, intelligence, and learning.


---

##### Bài tập 2.4

For each of the following assertions, say whether it is true or false
and support your answer with examples or counterexamples where
appropriate.<br>

1.  An agent that senses only partial information about the state cannot
    be perfectly rational.<br>

2.  There exist task environments in which no pure reflex agent can
    behave rationally.<br>

3.  There exists a task environment in which every agent is rational.<br>

4.  The input to an agent program is the same as the input to the
    agent function.<br>

5.  Every agent function is implementable by some
    program/machine combination.<br>

6.  Suppose an agent selects its action uniformly at random from the set
    of possible actions. There exists a deterministic task environment
    in which this agent is rational.<br>

7.  It is possible for a given agent to be perfectly rational in two
    distinct task environments.<br>

8.  Every agent is rational in an unobservable environment.<br>

9.  A perfectly rational poker-playing agent never loses.<br>


---

##### Bài tập 2.5

For each of the following activities, give a PEAS
description of the task environment and characterize it in terms of the
properties listed in Section <a class="sectionRef" title="" href="#">env-properties-subsection</a><br>

-   Playing soccer.<br>

-   Exploring the subsurface oceans of Titan.<br>

-   Shopping for used AI books on the Internet.<br>

-   Playing a tennis match.<br>

-   Practicing tennis against a wall.<br>

-   Performing a high jump.<br>

-   Knitting a sweater.<br>

-   Bidding on an item at an auction.<br>


---

##### Bài tập 2.6

For each of the following activities, give a PEAS
description of the task environment and characterize it in terms of the
properties listed in Section <a class="sectionRef" title="" href="#">env-properties-subsection</a><br>

-   Performing a gymnastics floor routine.<br>

-   Exploring the subsurface oceans of Titan.<br>

-   Playing soccer.<br>

-   Shopping for used AI books on the Internet.<br>

-   Practicing tennis against a wall.<br>

-   Performing a high jump.<br>

-   Bidding on an item at an auction.<br>


---

##### Bài tập 2.7

Define in your own words the following terms: agent, agent function,
agent program, rationality, autonomy, reflex agent, model-based agent,
goal-based agent, utility-based agent, learning agent.


---

##### Bài tập 2.8

This exercise explores the differences between
agent functions and agent programs.<br>

1.  Can there be more than one agent program that implements a given
    agent function? Give an example, or show why one is not possible.<br>

2.  Are there agent functions that cannot be implemented by any agent
    program?<br>

3.  Given a fixed machine architecture, does each agent program
    implement exactly one agent function?<br>

4.  Given an architecture with $n$ bits of storage, how many different
    possible agent programs are there?<br>

5.  Suppose we keep the agent program fixed but speed up the machine by
    a factor of two. Does that change the agent function?<br>


---

##### Bài tập 2.9

Write pseudocode agent programs for the goal-based and utility-based
agents.


---

##### Bài tập 2.10

Consider a simple thermostat that turns on a furnace when the
temperature is at least 3 degrees below the setting, and turns off a
furnace when the temperature is at least 3 degrees above the setting. Is
a thermostat an instance of a simple reflex agent, a model-based reflex
agent, or a goal-based agent?


---

##### Bài tập 2.11

Implement a performance-measuring environment
simulator for the vacuum-cleaner world depicted in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum-world-figure.png">vacuum-world-figure</a> and specified on
page <a class="pageRef" title="" href="#">vacuum-rationality-page</a>. Your implementation should be modular so that the
sensors, actuators, and environment characteristics (size, shape, dirt
placement, etc.) can be changed easily. (Note: for some
choices of programming language and operating system there are already
implementations in the online code repository.)


---

##### Bài tập 2.12

Implement a simple reflex agent for the vacuum environment in
Exercise <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_10/">vacuum-start-exercise</a>. Run the environment
with this agent for all possible initial dirt configurations and agent
locations. Record the performance score for each configuration and the
overall average score.


---

##### Bài tập 2.13

Consider a modified version of the
vacuum environment in Exercise <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_10/">vacuum-start-exercise</a>,
in which the agent is penalized one point for each movement.<br>

1.  Can a simple reflex agent be perfectly rational for this
    environment? Explain.<br>

2.  What about a reflex agent with state? Design such an agent.<br>

3.  How do your answers to 1 and 2
    change if the agent’s percepts give it the clean/dirty status of
    every square in the environment?


---

##### Bài tập 2.14

Consider a modified version of the
vacuum environment in Exercise <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_10/">vacuum-start-exercise</a>,
in which the geography of the environment—its extent, boundaries, and
obstacles—is unknown, as is the initial dirt configuration. (The agent
can go Up and Down as well as Left and Right.)<br>

1.  Can a simple reflex agent be perfectly rational for this
    environment? Explain.<br>

2.  Can a simple reflex agent with a randomized agent
    function outperform a simple reflex agent? Design such an agent and
    measure its performance on several environments.<br>

3.  Can you design an environment in which your randomized agent will
    perform poorly? Show your results.<br>

4.  Can a reflex agent with state outperform a simple reflex agent?
    Design such an agent and measure its performance on several
    environments. Can you design a rational agent of this type?


---

##### Bài tập 2.15

Repeat Exercise <a class="exerciseRef" href="{{ site.baseurl }}/agents-exercises/ex_13/">vacuum-unknown-geog-exercise</a> for the case in
which the location sensor is replaced with a “bump” sensor that detects
the agent’s attempts to move into an obstacle or to cross the boundaries
of the environment. Suppose the bump sensor stops working; how should
the agent behave?


---

##### Bài tập 2.16

The vacuum environments in the preceding
exercises have all been deterministic. Discuss possible agent programs
for each of the following stochastic versions:<br>

1.  Murphy’s law: twenty-five percent of the time, the Suck action
    fails to clean the floor if it is dirty and deposits dirt onto the
    floor if the floor is clean. How is your agent program affected if
    the dirt sensor gives the wrong answer 10% of the time?<br>

2.  Small children: At each time step, each clean square has a 10%
    chance of becoming dirty. Can you come up with a rational agent
    design for this case?


---


<!-- tabs:end -->
