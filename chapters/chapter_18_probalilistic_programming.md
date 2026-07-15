# Chapter 18 Probalilistic Programming

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_18_Probalilistic%20Programming/chapter_18_vi.html?v=2" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_18_Probalilistic%20Programming.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{fleqn}
\usepackage{epsf}
\usepackage{aima2e-slides}

# Learning from Observations

## Chapter 18, Sections 1--3

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

,95\textwidth
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

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting1.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting2.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting3.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting4.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

,5\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/curve-fitting5.png)

---
## Phương pháp học quy nạp

Xây dựng/điều chỉnh \mat{$h$} để phù hợp với \mat{$f$} trên tập huấn luyện 

(\mat{$h$} là \defn{nhất quán} nếu nó đồng ý với \mat{$f$} trên tất cả các ví dụ)

Ví dụ: khớp đường cong:

,5\textwidth
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

,8\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/restaurant-tree.png)

---
## Tính biểu cảm

Cây quyết định có thể thể hiện bất kỳ chức năng nào của thuộc tính đầu vào.

Ví dụ: đối với các hàm Boolean, đường dẫn hàng bảng chân lý \mat{$\rightarrow$} đến lá:

,65\textwidth
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

,6\textwidth
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

,6\textwidth
![Hình ảnh](../TaiLieu/slide_md/figures/restaurant-dtl-curve.png)

---
## Tiếp tục đo lường hiệu suất 

Đường cong học tập phụ thuộc vào 
  
 -- \defn{có thể thực hiện được} (có thể biểu thị hàm mục tiêu) so với \defn{không thể thực hiện được}
    
     không thể thực hiện được có thể do thiếu thuộc tính 
    
     hoặc lớp giả thuyết bị hạn chế (ví dụ: hàm tuyến tính có ngưỡng)
  
 -- tính biểu đạt dư thừa (ví dụ: vô số thuộc tính không liên quan)

,95\textwidth
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



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [DOUBLES-TENNIS-PROBLEM](codeAndExercises/aima-pseudocode-master/md/Doubles-Tennis-Problem.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
*(Không có Jupyter Notebook/Python code cho chương này)*

#### **Bài tập**

##### Bài tập 18.1

Consider the problem faced by an infant
learning to speak and understand a language. Explain how this process
fits into the general learning model. Describe the percepts and actions
of the infant, and the types of learning the infant must do. Describe
the subfunctions the infant is trying to learn in terms of inputs and
outputs, and available example data.


---

##### Bài tập 18.2

Repeat Exercise <a class="exerciseRef" href="{{ site.baseurl }}/concept-learning-exercises/ex_1/">infant-language-exercise</a> for the case
of learning to play tennis (or some other sport with which you are
familiar). Is this supervised learning or reinforcement learning?


---

##### Bài tập 18.3

Draw a decision tree for the problem of deciding whether to move forward
at a road intersection, given that the light has just turned green.


---

##### Bài tập 18.4

We never test the same attribute twice along one path in a decision
tree. Why not?


---

##### Bài tập 18.5

Suppose we generate a training set from a decision tree and then apply
decision-tree learning to that training set. Is it the case that the
learning algorithm will eventually return the correct tree as the
training-set size goes to infinity? Why or why not?


---

##### Bài tập 18.6

In the recursive construction of
decision trees, it sometimes happens that a mixed set of positive and
negative examples remains at a leaf node, even after all the attributes
have been used. Suppose that we have $p$ positive examples and $n$
negative examples.<br>

1.  Show that the solution used by DECISION-TREE-LEARNING, which picks the majority
    classification, minimizes the absolute error over the set of
    examples at the leaf.<br>

2.  Show that the <b>class probability</b> $p/(p+n)$ minimizes the sum of squared errors.


---

##### Bài tập 18.7

Suppose that an attribute splits the set of
examples $E$ into subsets $E_k$ and that each subset has $p_k$
positive examples and $n_k$ negative examples. Show that the
attribute has strictly positive information gain unless the ratio
$p_k/(p_k+n_k)$ is the same for all $k$.


---

##### Bài tập 18.8

Consider the following data set comprised of three binary input
attributes ($A_1, A_2$, and $A_3$) and one binary output:<br>

$$
\begin{array} 
	{|r|r|}\hline \textbf{Example} & A_1 & A_2 & A_3 & Output\space y \\ 
	\hline \textbf{x}_1 & 1 & 0 & 0 & 0 \\ 
	\textbf{x}_2 & 1 & 0 & 1 & 0 \\ 
	 \textbf{x}_3 & 0 & 1 & 0 & 0 \\ 
	 \textbf{x}_4 & 1 & 1 & 1 & 1 \\ 
	 \textbf{x}_5 & 1 & 1 & 0 & 1 \\ 
	\hline  
\end{array}
$$
Use the algorithm in Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/DTL-algorithm.png">DTL-algorithm</a>
(page <a class="pageRef" title="" href="#">DTL-algorithm</a>) to learn a decision tree for these data. Show the
computations made to determine the attribute to split at each node.


---

##### Bài tập 18.9

Construct a data set (set of examples with attributes and
classifications) that would cause the decision-tree learning algorithm
to find a non-minimal-sized tree. Show the tree constructed by the
algorithm and the minimal-sized tree that you can generate by hand.


---

##### Bài tập 18.10

A decision <i>graph</i> is a generalization of a decision tree
that allows nodes (i.e., attributes used for splits) to have multiple
parents, rather than just a single parent. The resulting graph must
still be acyclic. Now, consider the XOR function of <i>three</i>
binary input attributes, which produces the value 1 if and only if an
odd number of the three input attributes has value 1.<br>

1.  Draw a minimal-sized decision <i>tree</i> for the
    three-input XOR function.<br>

2.  Draw a minimal-sized decision <i>graph</i> for the
    three-input XOR function.<br>


---

##### Bài tập 18.11

This exercise considers $\chi^2$ pruning of
decision trees (Section <a class="sectionRef" title="" href="#">chi-squared-section</a><br>.

1.  Create a data set with two input attributes, such that the
    information gain at the root of the tree for both attributes is
    zero, but there is a decision tree of depth 2 that is consistent
    with all the data. What would $\chi^2$ pruning do on this data set
    if applied bottom up? If applied top down?<br>

2.  Modify DECISION-TREE-LEARNING to include $\chi^2$-pruning. You might wish to consult
    Quinlan [<a class="paperRef" title="" href="">Quinlan:1986</a>] or [<a class="paperRef" title="" href="">Kearns+Mansour:1998</a>] for details.<br>


---

##### Bài tập 18.12

The standard DECISION-TREE-LEARNING algorithm described in the
chapter does not handle cases in which some examples have missing
attribute values.<br>

1.  First, we need to find a way to classify such examples, given a
    decision tree that includes tests on the attributes for which values
    can be missing. Suppose that an example $\textbf{x}$ has a missing value for
    attribute $A$ and that the decision tree tests for $A$ at a node
    that $\textbf{x}$ reaches. One way to handle this case is to pretend that
    the example has <i>all</i> possible values for the
    attribute, but to weight each value according to its frequency among
    all of the examples that reach that node in the decision tree. The
    classification algorithm should follow all branches at any node for
    which a value is missing and should multiply the weights along each
    path. Write a modified classification algorithm for decision trees
    that has this behavior.<br>

2.  Now modify the information-gain calculation so that in any given
    collection of examples $C$ at a given node in the tree during the
    construction process, the examples with missing values for any of
    the remaining attributes are given “as-if” values according to the
    frequencies of those values in the set $C$.<br>


---

##### Bài tập 18.13

In
Section <a class="sectionRef" title="" href="#">broadening-decision-tree-section</a>, we noted that
attributes with many different possible values can cause problems with
the gain measure. Such attributes tend to split the examples into
numerous small classes or even singleton classes, thereby appearing to
be highly relevant according to the gain measure. The
<b>gain-ratio</b> criterion selects attributes
according to the ratio between their gain and their intrinsic
information content—that is, the amount of information contained in the
answer to the question, “What is the value of this attribute?” The
gain-ratio criterion therefore tries to measure how efficiently an
attribute provides information on the correct classification of an
example. Write a mathematical expression for the information content of
an attribute, and implement the gain ratio criterion in DECISION-TREE-LEARNING.


---

##### Bài tập 18.14

Suppose you are running a learning experiment on a new algorithm for
Boolean classification. You have a data set consisting of 100 positive
and 100 negative examples. You plan to use leave-one-out
cross-validation and compare your algorithm to a baseline function, a
simple majority classifier. (A majority classifier is given a set of
training data and then always outputs the class that is in the majority
in the training set, regardless of the input.) You expect the majority
classifier to score about 50% on leave-one-out cross-validation, but to
your surprise, it scores zero every time. Can you explain why?


---

##### Bài tập 18.15

Suppose that a learning algorithm is trying to find a consistent
hypothesis when the classifications of examples are actually random.
There are $n$ Boolean attributes, and examples are drawn uniformly from
the set of $2^n$ possible examples. Calculate the number of examples
required before the probability of finding a contradiction in the data
reaches 0.5.


---

##### Bài tập 18.16

Construct a <i>decision list</i> to classify the data below.
Select tests to be as small as possible (in terms of attributes),
breaking ties among tests with the same number of attributes by
selecting the one that classifies the greatest number of examples
correctly. If multiple tests have the same number of attributes and
classify the same number of examples, then break the tie using
attributes with lower index numbers (e.g., select $A_1$ over $A_2$).<br>

$$
\begin{array} 
	{|r|r|}\hline \textbf{Example} & A_1 & A_2 & A_3 & A_4 & y \\ 
	\hline \textbf{x}_1 & 1 & 0 & 0 & 0 & 1 \\ 
	\textbf{x}_2 & 1 & 0 & 1 & 1 & 1 \\ 
	 \textbf{x}_3 & 0 & 1 & 0 & 0 & 1 \\ 
	 \textbf{x}_4 & 0 & 1 & 1 & 0 & 0 \\ 
	 \textbf{x}_5 & 1 & 1 & 0 & 1 & 1 \\ 
	 \textbf{x}_6 & 0 & 1 & 0 & 1 & 0 \\ 
	 \textbf{x}_7 & 0 & 0 & 1 & 1 & 1 \\ 
	 \textbf{x}_8 & 0 & 0 & 1 & 0 & 0 \\ 
	\hline  
\end{array}
$$


---

##### Bài tập 18.17

Prove that a decision list can represent the same function as a decision
tree while using at most as many rules as there are leaves in the
decision tree for that function. Give an example of a function
represented by a decision list using strictly fewer rules than the
number of leaves in a minimal-sized decision tree for that same
function.


---

##### Bài tập 18.18

This exercise concerns the expressiveness of
decision lists (Section <a class="sectionRef" title="" href="#">learning-theory-section</a>).<br>

1.  Show that decision lists can represent any Boolean function, if the
    size of the tests is not limited.<br>

2.  Show that if the tests can contain at most $k$ literals each, then
    decision lists can represent any function that can be represented by
    a decision tree of depth $k$.


---

##### Bài tập 18.19

Suppose a $7$-nearest-neighbors regression search
returns $ \{7, 6, 8, 4, 7, 11, 100\} $ as the 7 nearest $y$ values for a
given $x$ value. What is the value of $\hat{y}$ that minimizes the $L_1$
loss function on this data? There is a common name in statistics for
this value as a function of the $y$ values; what is it? Answer the same
two questions for the $L_2$ loss function.


---

##### Bài tập 18.20

Suppose a $7$-nearest-neighbors regression search
returns $ \{4, 2, 8, 4, 9, 11, 100\} $ as the 7 nearest $y$ values for a
given $x$ value. What is the value of $\hat{y}$ that minimizes the $L_1$
loss function on this data? There is a common name in statistics for
this value as a function of the $y$ values; what is it? Answer the same
two questions for the $L_2$ loss function.


---

##### Bài tập 18.21

Figure <a href="#">kernel-machine-figure</a>
showed how a circle at the origin can be linearly separated by mapping
from the features $(x_1, x_2)$ to the two dimensions $(x_1^2, x_2^2)$.
But what if the circle is not located at the origin? What if it is an
ellipse, not a circle? The general equation for a circle (and hence the
decision boundary) is $(x_1-a)^2 + (x_2-b)^2 - r^2{{\,=\,}}0$, and the general equation for an ellipse is
$c(x_1-a)^2 + d(x_2-b)^2 - 1 {{\,=\,}}0$.
<br>
1.  Expand out the equation for the circle and show what the weights
    $w_i$ would be for the decision boundary in the four-dimensional
    feature space $(x_1, x_2, x_1^2, x_2^2)$. Explain why this means
    that any circle is linearly separable in this space.<br>

2.  Do the same for ellipses in the five-dimensional feature space
    $(x_1, x_2, x_1^2, x_2^2, x_1 x_2)$.


---

##### Bài tập 18.22

Construct a support vector machine that computes the
xor function. Use values of +1 and –1 (instead of 1 and 0)
for both inputs and outputs, so that an example looks like $([-1, 1], 1)$ or $([-1, -1], -1)$. Map the input $[x_1,x_2]$ into a space
consisting of $x_1$ and $x_1\,x_2$. Draw the four input points in this
space, and the maximal margin separator. What is the margin? Now draw
the separating line back in the original Euclidean input space.


---

##### Bài tập 18.23

Consider an ensemble learning algorithm that
uses simple majority voting among $K$ learned hypotheses.
Suppose that each hypothesis has error $\epsilon$ and that the errors
made by each hypothesis are independent of the others’. Calculate a
formula for the error of the ensemble algorithm in terms of $K$
and $\epsilon$, and evaluate it for the cases where
$K=5$, 10, and 20 and $\epsilon={0.1}$, 0.2,
and 0.4. If the independence assumption is removed, is it possible for
the ensemble error to be <i>worse</i> than $\epsilon$?


---

##### Bài tập 18.24

Construct by hand a neural network that computes the xor
function of two inputs. Make sure to specify what sort of units you are
using.


---

##### Bài tập 18.25

A simple perceptron cannot represent xor (or, generally,
the parity function of its inputs). Describe what happens to the weights
of a four-input, hard-threshold perceptron, beginning with all weights
set to 0.1, as examples of the parity function arrive.


---

##### Bài tập 18.26

Recall from
Chapter <a class="chapterRef" href="{{site.baseurl}}/concept-learning-exercises/">concept-learning-chapter</a> that there are
$2^{2^n}$ distinct Boolean functions of $n$ inputs. How many of
these are representable by a threshold perceptron?


---

##### Bài tập 18.27

Consider the following set of examples, each with six inputs and one
target output:<br>



$$
\begin{array} 
	{|r|r|}\hline \textbf{Example} & A_1 & A_2 & A_3 & A_4 & A_5 & A_6 & A_7 & A_8 & A_9 & A_{10} & A_{11} & A_{12} & A_{13} & A_{14} \\ 
	\hline 
	\textbf{x}_1  & 1 & 1  & 1  & 1 & 1 & 1 & 1  & 0  & 0 & 0 & 0 & 0  & 0  & 0 \\
	\textbf{x}_2  & 0 & 0  & 0  & 1 & 1 & 0 & 0  & 1  & 1 & 0 & 1 & 0  & 1  & 1 \\
	\textbf{x}_3  & 1 & 1  & 1  & 0 & 1 & 0 & 0  & 1  & 1 & 0 & 0 & 0  & 1  & 1 \\
	\textbf{x}_4  & 0 & 1  & 0  & 0 & 1 & 0 & 0  & 1  & 0 & 1 & 1 & 1  & 0  & 1 \\
	\textbf{x}_5  & 0 & 0  & 1  & 1 & 0 & 1 & 1  & 0  & 1 & 1 & 0 & 0  & 1  & 0 \\
	\textbf{x}_6  & 0 & 0  & 0  & 1 & 0 & 1 & 0  & 1  & 1 & 0 & 1 & 1  & 1  & 0 \\
	\textbf{T}   & 1 & 1  & 1  & 1 & 1 & 1 & 0  & 1  & 0 & 0 & 0 & 0  & 0  & 0 \\
	\hline  
\end{array}
$$



1.  Run the perceptron learning rule on these data and show the
    final weights.<br>

2.  Run the decision tree learning rule, and show the resulting
    decision tree.<br>

3.  Comment on your results.<br>


---

##### Bài tập 18.28

Section <a class="sectionRef" title="" href="#">logistic-regression-section</a>
(page <a class="pageRef" title="" href="#">logistic-regression-section</a>) noted that the output of the logistic function
could be interpreted as a <i>probability</i> $p$ assigned by the
model to the proposition that $f(\textbf{x}){{\,=\,}}1$; the probability that
$f(\textbf{x}){{\,=\,}}0$ is therefore $1-p$. Write down the probability $p$
as a function of $\textbf{x}$ and calculate the derivative of $\log p$ with
respect to each weight $w_i$. Repeat the process for $\log (1-p)$. These
calculations give a learning rule for minimizing the
negative-log-likelihood loss function for a probabilistic hypothesis.
Comment on any resemblance to other learning rules in the chapter.


---

##### Bài tập 18.29

Suppose you had a neural network with linear
activation functions. That is, for each unit the output is some constant
$c$ times the weighted sum of the inputs.<br>

1.  Assume that the network has one hidden layer. For a given assignment
    to the weights $\textbf{w}$, write down equations for the value of the
    units in the output layer as a function of $\textbf{w}$ and the input layer
    $\textbf{x}$, without any explicit mention of the output of the
    hidden layer. Show that there is a network with no hidden units that
    computes the same function.<br>

2.  Repeat the calculation in part (a), but this time do it for a
    network with any number of hidden layers.<br>

3.  Suppose a network with one hidden layer and linear activation
    functions has $n$ input and output nodes and $h$ hidden nodes. What
    effect does the transformation in part (a) to a network with no
    hidden layers have on the total number of weights? Discuss in
    particular the case $h \ll n$.


---

##### Bài tập 18.30

Implement a data structure for layered, feed-forward neural networks,
remembering to provide the information needed for both forward
evaluation and backward propagation. Using this data structure, write a
function NEURAL-NETWORK-OUTPUT that takes an example and a network and computes the
appropriate output values.


---

##### Bài tập 18.31

Suppose that a training set contains only a single example, repeated 100
times. In 80 of the 100 cases, the single output value is 1; in the
other 20, it is 0. What will a back-propagation network predict for this
example, assuming that it has been trained and reaches a global optimum?
(<i>Hint:</i> to find the global optimum, differentiate the
error function and set it to zero.)


---

##### Bài tập 18.32

The neural network whose learning performance is measured in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/restaurant-back-prop-figure.png">restaurant-back-prop-figure</a> has four hidden
nodes. This number was chosen somewhat arbitrarily. Use a
cross-validation method to find the best number of hidden nodes.


---

##### Bài tập 18.33

Consider the problem of separating
$N$ data points into positive and negative examples using a linear
separator. Clearly, this can always be done for $N{{\,=\,}}2$ points
on a line of dimension $d{{\,=\,}}1$, regardless of how the points are
labeled or where they are located (unless the points are in the same
place).<br>

1.  Show that it can always be done for $N{{\,=\,}}3$ points on a
    plane of dimension $d{{\,=\,}}2$, unless they are collinear.<br>

2.  Show that it cannot always be done for $N{{\,=\,}}4$ points on a
    plane of dimension $d{{\,=\,}}2$.<br>

3.  Show that it can always be done for $N{{\,=\,}}4$ points in a
    space of dimension $d{{\,=\,}}3$, unless they are coplanar.<br>

4.  Show that it cannot always be done for $N{{\,=\,}}5$ points in a
    space of dimension $d{{\,=\,}}3$.<br>

5.  The ambitious student may wish to prove that $N$ points in general
    position (but not $N+1$) are linearly separable in a space of
    dimension $N-1$.<br>


---


<!-- tabs:end -->
