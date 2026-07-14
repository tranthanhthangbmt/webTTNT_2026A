# Chapter 14 Probabilistic Reasoning over time

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_14_Probabilistic%20Reasoning%20over%20time/chapter_14_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_14_Probabilistic%20Reasoning%20over%20time.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

\usepackage{aima-slides}
\usepackage[utf8]{inputenc}
\usepackage[T5]{fontenc}
\usepackage{lmodern}

# Độ bất định (Uncertainty)

## Chương 14

---
## Nội dung

- Độ bất định (Uncertainty)

- Xác suất (Probability)

- Cú pháp (Syntax)

- Ngữ nghĩa (Semantics)

- Các quy tắc suy diễn (Inference rules)

---
## Độ bất định

Cho hành động $A_t$ = rời đi sân bay trước $t$ phút chuyến bay cất cánh

Liệu $A_t$ có giúp tôi đến đó đúng giờ không?

Các vấn đề:
  
1) khả năng quan sát một phần (tình trạng đường xá, kế hoạch của tài xế khác, v.v.)
  
2) cảm biến bị nhiễu (Báo cáo giao thông KCBS)
  
3) sự không chắc chắn trong kết quả hành động (xịt lốp xe, v.v.)
  
4) sự phức tạp to lớn của việc mô hình hóa và dự đoán giao thông

Do đó, một cách tiếp cận logic thuần túy có thể

\phantom{hoặc }1) có nguy cơ sai sự thật: "$A_{25}$ sẽ giúp tôi đến đó đúng giờ"

hoặc 2) dẫn đến các kết luận quá yếu để ra quyết định:
    
"$A_{25}$ sẽ giúp tôi đến đó đúng giờ nếu không có tai nạn trên cầu
    
và trời không mưa và lốp xe của tôi vẫn nguyên vẹn v.v. và v.v."

(Có thể nói $A_{1440}$ sẽ giúp tôi đến đó đúng giờ một cách hợp lý

nhưng tôi sẽ phải ở lại qua đêm tại sân bay $\ldots$)

---
## Các phương pháp xử lý độ bất định

Logic <u>mặc định (Default)</u> hoặc <u>phi đơn điệu (nonmonotonic)</u>:
  
  Giả sử xe của tôi không bị xịt lốp
  
  Giả sử $A_{25}$ có tác dụng trừ khi bị mâu thuẫn bởi bằng chứng

Vấn đề: Những giả định nào là hợp lý? Làm thế nào để xử lý sự mâu thuẫn?

<u>Các quy tắc với hệ số fudge (Fudge factors)</u>:
  
$A_{25} \mapsto_{0.3}$ đến đó đúng giờ
  
$Sprinkler \mapsto_{0.99} WetGrass$
  
$WetGrass \mapsto_{0.7} Rain$

Vấn đề: Các rắc rối với sự kết hợp, ví dụ, $Sprinkler$ gây ra $Rain$??

<u>Xác suất (Probability)</u>
  
  Dựa trên các bằng chứng có sẵn,
    
    $A_{25}$ sẽ giúp tôi đến đó đúng giờ với xác suất 0.04

Lý thuyết cờ bạc của Mahaviracarya (thế kỷ 9), Cardamo (1565)

(Logic <u>mờ (Fuzzy)</u> xử lý *mức độ đúng đắn (degree of truth)* CHỨ KHÔNG PHẢI độ bất định, ví dụ:
  
  $WetGrass$ đúng ở mức độ 0.2)

---
## Xác suất (Probability)

Các khẳng định xác suất *tóm tắt* ảnh hưởng của
  
  <u>sự lười biếng (laziness)</u>: thất bại trong việc liệt kê các trường hợp ngoại lệ, các điều kiện phụ, v.v.
  
  <u>sự thiếu hiểu biết (ignorance)</u>: thiếu các sự kiện liên quan, các điều kiện ban đầu, v.v.

Xác suất <u>chủ quan (Subjective)</u> hoặc <u>Bayesian</u>:

Xác suất liên hệ các mệnh đề với trạng thái tri thức của chính một người
    
ví dụ, $P(A_{25} | \mbox{không có tai nạn nào được báo cáo}) = 0.06$

Đây <u>không</u> phải là các khẳng định về thế giới

Xác suất của các mệnh đề thay đổi khi có bằng chứng mới:
    
ví dụ, $P(A_{25} | \mbox{không có tai nạn nào được báo cáo},\ \mbox{5 a.m.}) = 0.15$

(Tương tự như trạng thái kéo theo logic $KB \models 
  pha$, chứ không phải là sự thật.)

---
## Đưa ra quyết định trong điều kiện bất định

Giả sử tôi tin vào điều sau đây:
\begin{eqnarray*}
P(A_{25}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.04 

P(A_{90}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.70 

P(A_{120}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.95 

P(A_{1440}\mbox{ giúp tôi đến đó đúng giờ} | \ldots) &=& 0.9999 
\end{eqnarray*}
Nên chọn hành động nào?

Phụ thuộc vào <u>sự ưu tiên (preferences)</u> của tôi đối với việc lỡ chuyến bay so với ẩm thực sân bay, v.v.

<u>Lý thuyết hữu ích (Utility theory)</u> được sử dụng để biểu diễn và suy diễn các sự ưu tiên

<u>Lý thuyết quyết định (Decision theory)</u> = lý thuyết hữu ích + lý thuyết xác suất

---
## Các tiên đề của xác suất

Với bất kỳ mệnh đề $A$, $B$ nào

1. $0 \leq P(A) \leq 1$

2. $P(True) = 1$ và $P(False) = 0$

3. $P(A \lor B) = P(A) + P(B) - P(A\land B)$

![Hình ảnh](../TaiLieu/slide_md/figures/axiom3-venn.png)

de Finetti (1931): một tác tử đặt cược theo các xác suất vi phạm
các tiên đề này có thể bị buộc phải đặt cược sao cho mất tiền bất kể kết quả như thế nào.

---
## Cú pháp (Syntax)

Tương tự logic mệnh đề: các thế giới có thể được định nghĩa bằng việc gán
giá trị cho các <u>biến ngẫu nhiên (random variables)</u>.

Các biến ngẫu nhiên <u>mệnh đề</u> hoặc <u>Boolean</u>
  
  ví dụ: $Cavity$ (tôi có bị sâu răng không?)

Bao gồm các biểu thức logic mệnh đề
  
  ví dụ: $\lnot Burglary \lor Earthquake$

Biến ngẫu nhiên <u>nhiều giá trị (Multivalued)</u>
  
  ví dụ: $Weather$ là một trong $\<sunny,rain,cloudy,snow\>$

Các giá trị phải đầy đủ (exhaustive) và loại trừ lẫn nhau (mutually exclusive)

Mệnh đề được xây dựng bằng cách gán một giá trị:
  
ví dụ: $Weather \eq sunny$; hoặc $Cavity \eq true$ cho rõ ràng

---
## Cú pháp (tiếp)

Xác suất <u>tiên nghiệm (Prior)</u> hoặc <u>không điều kiện (unconditional)</u> của các mệnh đề
  
  ví dụ: $P(Cavity) = 0.1$ và $P(Weather \eq sunny) = 0.72$

tương ứng với niềm tin trước khi có bất kỳ bằng chứng (mới) nào

<u>Phân phối xác suất (Probability distribution)</u> đưa ra các giá trị cho tất cả các phép gán có thể có:
  
  $P(Weather) = \<0.72,0.1,0.08,0.1\>$ (<u>đã chuẩn hóa (normalized)</u>, nghĩa là tổng bằng 1)

<u>Phân phối xác suất đồng thời (Joint probability distribution)</u> đối với một tập các biến đưa ra

các giá trị cho từng phép gán có thể có đối với tất cả các biến
  
  $P(Weather,Cavity)$ = một ma trận các giá trị $4 \times 2$:

\[\begin{array}{l|cccc}
\hfil Weather \eq & sunny & rain & cloudy & snow 

\hline
Cavity \eq true & & & & 

Cavity \eq false & & & &
\end{array}\]

---
## Cú pháp (tiếp)

Xác suất <u>có điều kiện (Conditional)</u> hoặc <u>hậu nghiệm (posterior)</u>
  
  ví dụ: $P(Cavity | Toothache) = 0.8$
  
  nghĩa là, <u>\u{biết rằng $Toothache$ là tất cả những gì tôi biết</u>}

Ký hiệu cho phân phối có điều kiện:
  
  $P(Weather | Earthquake)$ = vector 2 phần tử của các vector 4 phần tử

Nếu chúng ta biết nhiều hơn, ví dụ: $Cavity$ cũng được cho trước, thì chúng ta có
  
  $P(Cavity | Toothache,Cavity) = 1$

Lưu ý: niềm tin ít cụ thể hơn *vẫn có giá trị* sau khi có thêm bằng chứng
mới đến, nhưng không phải lúc nào cũng *hữu ích*

Bằng chứng mới có thể không liên quan, cho phép đơn giản hóa, ví dụ:
  
$P(Cavity | Toothache,49ersWin) = P(Cavity | Toothache) = 0.8$

Loại suy diễn này, được phê chuẩn bởi kiến thức miền, là rất quan trọng

---
## Xác suất có điều kiện

Định nghĩa xác suất có điều kiện:
\[
  P(A|B) = \frac{P(A\land B)}{P(B)} \mbox{ nếu } P(B) \neq 0
\]
<u>Quy tắc nhân (Product rule)</u> đưa ra một công thức thay thế:
  
  $P(A\land B) = P(A|B)P(B) = P(B|A)P(A)$

Một phiên bản tổng quát áp dụng cho toàn bộ phân phối, ví dụ:
  
  $P(Weather,Cavity) = P(Weather|Cavity) P(Cavity)$

(Xem như một tập hợp $4\times 2$ các phương trình, *không* phải nhân ma trận.)

<u>Quy tắc chuỗi (Chain rule)</u> được suy ra bằng cách áp dụng liên tiếp quy tắc nhân:
  
$P(X_1,\ldots,X_n) = P(X_1,\ldots,X_{n-1})\ 
                        P(X_n | X_1,\ldots,X_{n-1})$
    
                    = $P(X_1,\ldots,X_{n-2})\ 
                        P(X_{n-1} | X_1,\ldots,X_{n-2})\ 
                        P(X_n | X_1,\ldots,X_{n-1})$
    
                  = $\ldots$
    
                  = $\myprod_{i\eq 1}^n P(X_i | X_1,\ldots,X_{i-1})$

---
## Quy tắc Bayes (Bayes' Rule)

Quy tắc nhân $P(A\land B) = P(A|B)P(B) = P(B|A)P(A)$
\[
{}\implies \mbox{<u>Quy tắc Bayes </u>}  P(A|B) = \frac{P(B|A)P(A)}{P(B)}
\]
Tại sao điều này lại hữu ích???

Để đánh giá xác suất <u>chẩn đoán (diagnostic)</u> từ xác suất <u>nhân quả (causal)</u>:
\[
  P(Nguy\hat{e}n\ nh\hat{a}n|K\hat{e}t\ qu\mbox{\`{a}}) = \frac{P(K\hat{e}t\ qu\mbox{\`{a}}|Nguy\hat{e}n\ nh\hat{a}n)P(Nguy\hat{e}n\ nh\hat{a}n)}{P(K\hat{e}t\ qu\mbox{\`{a}})}
\]
Ví dụ, gọi $M$ là viêm màng não, $S$ là cứng cổ:
\[
  P(M|S) = \frac{P(S|M)P(M)}{P(S)} = \frac{0.8 \times 0.0001}{0.1} = 0.0008
\]
Lưu ý: xác suất hậu nghiệm của bệnh viêm màng não vẫn rất nhỏ!

---
## Chuẩn hóa (Normalization)

Giả sử chúng ta muốn tính phân phối hậu nghiệm trên $A$

khi biết $B\eq b$, và giả sử $A$ có các giá trị có thể có $a_1 \ldots a_m$

Chúng ta có thể áp dụng quy tắc Bayes cho mỗi giá trị của $A$:
  
  $P(A\eq a_1|B\eq b) = P(B\eq b|A\eq a_1)P(A\eq a_1)/P(B\eq b)$
  
  $\ldots$
  
  $P(A\eq a_m|B\eq b) = P(B\eq b|A\eq a_m)P(A\eq a_m)/P(B\eq b)$

Cộng các giá trị này lại, và lưu ý rằng $\mysum_i P(A\eq a_i|B\eq b) = 1$:
\[1/P(B\eq b)  = 1/\mysum_i P(B\eq b|A\eq a_i)P(A\eq a_i)\]
Đây là <u>hệ số chuẩn hóa (normalization factor)</u>, hằng số theo $i$, được ký hiệu là $
  pha$:
\[
  P(A|B\eq b) = 
  pha P(B\eq b | A)P(A)
\]
Thông thường tính một phân phối chưa chuẩn hóa, sau đó chuẩn hóa ở cuối
  
  ví dụ: giả sử $P(B\eq b | A)P(A) = \<0.4,0.2,0.2\>$
    
    thì $P(A|B\eq b) = 
  pha \<0.4,0.2,0.2\> 
                        = \frac{\<0.4,0.2,0.2\>}{0.4+0.2+0.2} 
                        = \<0.5,0.25,0.25\>$

---
## Điều kiện hóa (Conditioning)

Giới thiệu một biến làm điều kiện bổ sung:
\[
  P(X|Y) = \mysum_z P(X|Y,Z\eq z) P(Z\eq z|Y)
\]
Trực giác: thường dễ dàng hơn để đánh giá từng trường hợp cụ thể, ví dụ:

$P(RunOver|Cross)$
  
  = $P(RunOver|Cross,Light\eq green)P(Light\eq green|Cross)$
  
  + $P(RunOver|Cross,Light\eq yellow)P(Light\eq yellow|Cross)$
  
  + $P(RunOver|Cross,Light\eq red)P(Light\eq red|Cross)$

Khi $Y$ vắng mặt, chúng ta có <u>tổng lấy ra (summing out)</u> hoặc <u>lấy biên (marginalization)</u>:
\[
  P(X) = \mysum_z P(X|Z\eq z) P(Z\eq z) = \mysum_z P(X,Z\eq z)
\]
Nói chung, với một phân phối đồng thời trên một tập các biến, thì
phân phối trên bất kỳ tập con nào (được gọi là phân phối <u>biên (marginal)</u> vì
lý do lịch sử) có thể được tính bằng cách tính tổng các biến khác.

---
## Phân phối đồng thời đầy đủ (Full joint distributions)

Một <u>mô hình xác suất hoàn chỉnh</u> xác định mọi mục nhập trong phân phối
đồng thời cho tất cả các biến $\mbf{X} = X_1,\ldots,X_n$

Nghĩa là, một xác suất cho mỗi thế giới có thể có $X_1\eq x_1,\ldots,X_n\eq x_n$

(So sánh với các lý thuyết đầy đủ trong logic.)

Ví dụ: giả sử $Toothache$ và $Cavity$ là các biến ngẫu nhiên:
\[\begin{array}{l|cc}
 & Toothache\eq true & Toothache\eq false 

\hline
Cavity \eq true  & 0.04 & 0.06 

Cavity \eq false & 0.01 & 0.89
\end{array}\]
Các thế giới có thể có loại trừ lẫn nhau $\implies$ $P(w_1 \land w_2) = 0$

Các thế giới có thể có là đầy đủ $\implies$ $w_1 \lor \cdots \lor w_n$ là $True$
    
do đó $\mysum_i P(w_i) = 1$

---
## Phân phối đồng thời đầy đủ (tiếp)

1) Đối với bất kỳ mệnh đề $\phi$ nào được định nghĩa trên các biến ngẫu nhiên
    
   $\phi(w_i)$ là đúng hoặc sai

2) $\phi$ tương đương với phép tuyển của các $w_i$ khi $\phi(w_i)$ đúng

Do đó $P(\phi) = \mysum_{\{w_i:\ \phi(w_i)\}} P(w_i)$

Nghĩa là, xác suất không điều kiện của bất kỳ mệnh đề nào đều có thể tính được
như là tổng của các mục nhập từ phân phối đồng thời đầy đủ

Xác suất có điều kiện có thể được tính theo cùng một cách như một tỷ lệ:
\[
  P(\phi|\xi) = \frac{P(\phi\land \xi)}{P(\xi)}
\]
Ví dụ: 
\[
  P(Cavity |Toothache) 
   = \frac{P(Cavity \land Toothache)}{P(Toothache)}
   = \frac{0.04}{0.04+0.01} = 0.8
\]

---
## Suy diễn từ các phân phối đồng thời

Thông thường, chúng ta quan tâm đến 
  
  phân phối đồng thời hậu nghiệm của <u>các biến truy vấn (query variables)</u> $\mbf{Y}$
  
  cho trước các giá trị cụ thể $\mbf{e}$ đối với <u>các biến bằng chứng (evidence variables)</u> $\mbf{E}$

Gọi <u>các biến ẩn (hidden variables)</u> là $\mbf{H} = \mbf{X} - \mbf{Y} - \mbf{E}$

Khi đó phép tính tổng các mục nhập đồng thời được yêu cầu sẽ được thực hiện bằng cách lấy tổng
các biến ẩn:
\[
P(\mbf{Y}|\mbf{E}\eq \mbf{e}) = 
  pha P(\mbf{Y},\mbf{E}\eq \mbf{e})
= 
  pha \mysum_{\smbf{h}} P(\mbf{Y},\mbf{E}\eq \mbf{e},\mbf{H}\eq \mbf{h})
\]
Các số hạng trong phép tổng là các mục nhập đồng thời vì $\mbf{Y}$, $\mbf{E}$, và $\mbf{H}$ cùng nhau vét cạn tập các biến ngẫu nhiên

Các vấn đề rõ ràng:
  
1) Độ phức tạp thời gian trong trường hợp xấu nhất là $O(d^n)$ trong đó $d$ là số ngôi (arity) lớn nhất
  
2) Độ phức tạp không gian $O(d^n)$ để lưu trữ phân phối đồng thời
  
3) Làm thế nào để tìm ra các con số cho $O(d^n)$ mục nhập???



#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- [FORWARD-BACKWARD](codeAndExercises/aima-pseudocode-master/md/Forward-Backward.md)
- [FIXED-LAG-SMOOTHING](codeAndExercises/aima-pseudocode-master/md/Fixed-Lag-Smoothing.md)
- [PARTICLE-FILTERING](codeAndExercises/aima-pseudocode-master/md/Particle-Filtering.md)

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Probability](codeAndExercises/aima-python-master/notebooks/probability.ipynb)
- [Probability (Python File)](codeAndExercises/aima-python-master/notebooks/probability.py)
- [Kalman Filter](codeAndExercises/aima-python-master/notebooks/kalman_filter.ipynb)
- [Kalman Filter (Python File)](codeAndExercises/aima-python-master/notebooks/kalman_filter.py)
- [Viterbi Algorithm](codeAndExercises/aima-python-master/notebooks/viterbi_algorithm.ipynb)
- [Viterbi Algorithm (Python File)](codeAndExercises/aima-python-master/notebooks/viterbi_algorithm.py)
- [Expectation Maximization](codeAndExercises/aima-python-master/notebooks/expectation_maximization.ipynb)
- [Expectation Maximization (Python File)](codeAndExercises/aima-python-master/notebooks/expectation_maximization.py)


#### **Bài tập**

##### Bài tập 14.1

We have a bag of three biased coins $a$, $b$, and $c$ with probabilities
of coming up heads of 20%, 60%, and 80%, respectively. One coin is drawn
randomly from the bag (with equal likelihood of drawing each of the
three coins), and then the coin is flipped three times to generate the
outcomes $X_1$, $X_2$, and $X_3$.<br>

1.  Draw the Bayesian network corresponding to this setup and define the
    necessary CPTs.<br>

2.  Calculate which coin was most likely to have been drawn from the bag
    if the observed flips come out heads twice and tails once.


---

##### Bài tập 14.2

We have a bag of three biased coins $a$, $b$, and $c$ with probabilities
of coming up heads of 30%, 60%, and 75%, respectively. One coin is drawn
randomly from the bag (with equal likelihood of drawing each of the
three coins), and then the coin is flipped three times to generate the
outcomes $X_1$, $X_2$, and $X_3$.<br>

1.  Draw the Bayesian network corresponding to this setup and define the
    necessary CPTs.<br>

2.  Calculate which coin was most likely to have been drawn from the bag
    if the observed flips come out heads twice and tails once.<br>


---

##### Bài tập 14.3

Equation (<a href="#">parameter-joint-repn-equation</a> on
page <a class="pageRef" title="" href="#">parameter-joint-repn-equation</a> defines the joint distribution represented by a
Bayesian network in terms of the parameters
$\theta(X_i{{\,|\,}}{Parents}(X_i))$. This exercise asks you to derive
the equivalence between the parameters and the conditional probabilities
${\textbf{ P}}(X_i{{\,|\,}}{Parents}(X_i))$ from this definition.<br>

1.  Consider a simple network $X\rightarrow Y\rightarrow Z$ with three
    Boolean variables. Use
    Equations (<a class="equationRef" title="" href="#">conditional-probability-equation</a> and (<a class="pageRef" title="" href="#">marginalization-equation</a>
    (pages <a href="#">conditional-probability-equation</a> and <a href="#">marginalization-equation</a>)
    to express the conditional probability $P(z{{\,|\,}}y)$ as the ratio of two sums, each over entries in the
    joint distribution ${\textbf{P}}(X,Y,Z)$.<br>

2.  Now use Equation (<a class="equationRef" title="" href="#">parameter-joint-repn-equation</a> to
    write this expression in terms of the network parameters
    $\theta(X)$, $\theta(Y{{\,|\,}}X)$, and $\theta(Z{{\,|\,}}Y)$.<br>

3.  Next, expand out the summations in your expression from part (b),
    writing out explicitly the terms for the true and false values of
    each summed variable. Assuming that all network parameters satisfy
    the constraint
    $\sum_{x_i} \theta(x_i{{\,|\,}}{parents}(X_i)){{\,=\,}}1$, show
    that the resulting expression reduces to $\theta(z{{\,|\,}}y)$.<br>

4.  Generalize this derivation to show that
    $\theta(X_i{{\,|\,}}{Parents}(X_i)) = {\textbf{P}}(X_i{{\,|\,}}{Parents}(X_i))$
    for any Bayesian network.<br>


---

##### Bài tập 14.4

The <b>arc reversal</b> operation of in a Bayesian network allows us to change the direction
of an arc $X\rightarrow Y$ while preserving the joint probability
distribution that the network represents <a class="paperRef" title="" href="">Shachter:1986</a>. Arc reversal
may require introducing new arcs: all the parents of $X$ also become
parents of $Y$, and all parents of $Y$ also become parents of $X$.<br>

1.  Assume that $X$ and $Y$ start with $m$ and $n$ parents,
    respectively, and that all variables have $k$ values. By calculating
    the change in size for the CPTs of $X$ and $Y$, show that the total
    number of parameters in the network cannot decrease during
    arc reversal. (<i>Hint</i>: the parents of $X$ and $Y$ need
    not be disjoint.)<br>

2.  Under what circumstances can the total number remain constant?<br>

3.  Let the parents of $X$ be $\textbf{U} \cup \textbf{V}$ and the parents of $Y$ be
    $\textbf{V} \cup \textbf{W}$, where $\textbf{U}$ and $\textbf{W}$ are disjoint. The formulas for the
    new CPTs after arc reversal are as follows: $$\begin{aligned}
    {\textbf{P}}(Y | \textbf{U},\textbf{V},\textbf{W}) &=& \sum_x {\textbf{P}}(Y | \textbf{V},\textbf{W}, x) {\textbf{P}}(x | \textbf{U}, \textbf{V}) \\
    {\textbf{P}}(X | \textbf{U},\textbf{V},\textbf{W}, Y) &=& {\textbf{P}}(Y | X, \textbf{V}, \textbf{W}) {\textbf{P}}(X | \textbf{U}, \textbf{V}) / {\textbf{P}}(Y | \textbf{U},\textbf{V},\textbf{W})\ .\end{aligned}$$
    Prove that the new network expresses the same joint distribution
    over all variables as the original network.


---

##### Bài tập 14.5

Consider the Bayesian network in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/burglary-figure.png">burglary-figure.</a><br>

1.  If no evidence is observed, are ${Burglary}$ and ${Earthquake}$
    independent? Prove this from the numerical semantics and from the
    topological semantics.<br>

2.  If we observe ${Alarm}{{\,=\,}}{true}$, are ${Burglary}$ and
    ${Earthquake}$ independent? Justify your answer by calculating
    whether the probabilities involved satisfy the definition of
    conditional independence.


---

##### Bài tập 14.6

Suppose that in a Bayesian network containing an unobserved variable
$Y$, all the variables in the Markov blanket ${MB}(Y)$ have been
observed.<br>

1.  Prove that removing the node $Y$ from the network will not affect
    the posterior distribution for any other unobserved variable in
    the network.<br>

2.  Discuss whether we can remove $Y$ if we are planning to use (i)
    rejection sampling and (ii) likelihood weighting.<br>


    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/handedness1.svg" alt="handedness-figure" id="handedness-figure" style="width:100%">
      <figcaption><center><b>Three possible structures for a Bayesian network describing genetic inheritance of handedness.</b></center></figcaption>
    </figure>


---

##### Bài tập 14.7

Let $H_x$ be a random variable denoting the
handedness of an individual $x$, with possible values $l$ or $r$. A
common hypothesis is that left- or right-handedness is inherited by a
simple mechanism; that is, perhaps there is a gene $G_x$, also with
values $l$ or $r$, and perhaps actual handedness turns out mostly the
same (with some probability $s$) as the gene an individual possesses.
Furthermore, perhaps the gene itself is equally likely to be inherited
from either of an individual’s parents, with a small nonzero probability
$m$ of a random mutation flipping the handedness.<br>

1.  Which of the three networks in
    Figure <a class="insideExercisesFigRef" href="#handedness-figure">handedness-figure</a> claim that
    $ {\textbf{P}}(G_{father},G_{mother},G_{child}) = {\textbf{P}}(G_{father}){\textbf{P}}(G_{mother}){\textbf{P}}(G_{child})$?<br>

2.  Which of the three networks make independence claims that are
    consistent with the hypothesis about the inheritance of handedness?<br>

3.  Which of the three networks is the best description of the
    hypothesis?<br>

4.  Write down the CPT for the $G_{child}$ node in network (a), in
    terms of $s$ and $m$.<br>

5.  Suppose that
    $P(G_{father}{{\,=\,}}l)=P(G_{mother}{{\,=\,}}l)=q$. In
    network (a), derive an expression for $P(G_{child}{{\,=\,}}l)$
    in terms of $m$ and $q$ only, by conditioning on its parent nodes.<br>

6.  Under conditions of genetic equilibrium, we expect the distribution
    of genes to be the same across generations. Use this to calculate
    the value of $q$, and, given what you know about handedness in
    humans, explain why the hypothesis described at the beginning of
    this question must be wrong.<br>


---

##### Bài tập 14.8

The <b>Markov
blanket</b> of a variable is defined on page <a href="#">markov-blanket-page</a>.
Prove that a variable is independent of all other variables in the
network, given its Markov blanket and derive
Equation (<a class="equationRef" title="" href="#">markov-blanket-equation</a>)
(page <a class="pageRef" title="" href="#">markov-blanket-equation</a>).
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/car-starts.svg" alt="car-starts-figure" id="car-starts-figure" style="width:100%">
    <figcaption><center><b>A Bayesian network describing some features of a car's electrical system and engine. Each variable is Boolean, and the <i>true</i> value indicates that the corresponding aspect of the vehicle is in working order.</b></center></figcaption>
</figure>


---

##### Bài tập 14.9

Consider the network for car diagnosis shown in
Figure <a class="insideExercisesFigRef" href="#car-starts-figure">car-starts-figure</a><br>.

1.  Extend the network with the Boolean variables ${IcyWeather}$ and
    ${StarterMotor}$.<br>

2.  Give reasonable conditional probability tables for all the nodes.<br>

3.  How many independent values are contained in the joint probability
    distribution for eight Boolean nodes, assuming that no conditional
    independence relations are known to hold among them?<br>

4.  How many independent probability values do your network tables
    contain?<br>

5.  The conditional distribution for ${Starts}$ could be described as
    a <b>noisy-AND</b> distribution. Define this
    family in general and relate it to the noisy-OR distribution.


---

##### Bài tập 14.10

Consider a simple Bayesian network with root variables ${Cold}$,
${Flu}$, and ${Malaria}$ and child variable ${Fever}$, with a
noisy-OR conditional distribution for ${Fever}$ as described in
Section <a class="sectionRef" title="" href="#">canonical-distribution-section</a>. By adding
appropriate auxiliary variables for inhibition events and fever-inducing
events, construct an equivalent Bayesian network whose CPTs (except for
root variables) are deterministic. Define the CPTs and prove
equivalence.


---

##### Bài tập 14.11

Consider the family of linear Gaussian networks, as
defined on page <a class="pageRef" title="" href="#">LG-network-page</a><br>.

1.  In a two-variable network, let $X_1$ be the parent of $X_2$, let
    $X_1$ have a Gaussian prior, and let
    ${\textbf{P}}(X_2{{\,|\,}}X_1)$ be a linear
    Gaussian distribution. Show that the joint distribution $P(X_1,X_2)$
    is a multivariate Gaussian, and calculate its covariance matrix.<br>

2.  Prove by induction that the joint distribution for a general linear
    Gaussian network on $X_1,\ldots,X_n$ is also a
    multivariate Gaussian.<br>


---

##### Bài tập 14.12

The probit distribution defined on
page <a class="pageRef" title="" href="#">probit-page</a> describes the probability distribution for a Boolean
child, given a single continuous parent.<br>

1.  How might the definition be extended to cover multiple continuous
    parents?<br>

2.  How might it be extended to handle a <i>multivalued</i>
    child variable? Consider both cases where the child’s values are
    ordered (as in selecting a gear while driving, depending on speed,
    slope, desired acceleration, etc.) and cases where they are
    unordered (as in selecting bus, train, or car to get to work).
    (<i>Hint</i>: Consider ways to divide the possible values
    into two sets, to mimic a Boolean variable.)


---

##### Bài tập 14.13

In your local nuclear power station, there is an alarm that senses when
a temperature gauge exceeds a given threshold. The gauge measures the
temperature of the core. Consider the Boolean variables $A$ (alarm
sounds), $F_A$ (alarm is faulty), and $F_G$ (gauge is faulty) and the
multivalued nodes $G$ (gauge reading) and $T$ (actual core temperature).<br>

1.  Draw a Bayesian network for this domain, given that the gauge is
    more likely to fail when the core temperature gets too high.<br>

2.  Is your network a polytree? Why or why not?<br>

3.  Suppose there are just two possible actual and measured
    temperatures, normal and high; the probability that the gauge gives
    the correct temperature is $x$ when it is working, but $y$ when it
    is faulty. Give the conditional probability table associated with
    $G$.<br>

4.  Suppose the alarm works correctly unless it is faulty, in which case
    it never sounds. Give the conditional probability table associated
    with $A$.<br>

5.  Suppose the alarm and gauge are working and the alarm sounds.
    Calculate an expression for the probability that the temperature of
    the core is too high, in terms of the various conditional
    probabilities in the network.<br>


---

##### Bài tập 14.14

Two astronomers in different parts of the world
make measurements $M_1$ and $M_2$ of the number of stars $N$ in some
small region of the sky, using their telescopes. Normally, there is a
small possibility $e$ of error by up to one star in each direction. Each
telescope can also (with a much smaller probability $f$) be badly out of
focus (events $F_1$ and $F_2$), in which case the scientist will
undercount by three or more stars (or if $N$ is less than 3, fail to
detect any stars at all). Consider the three networks shown in
Figure <a class="insideExercisesFigRef"  href="#telescope-nets-figure">telescope-nets-figure</a>.<br>

1.  Which of these Bayesian networks are correct (but not
    necessarily efficient) representations of the preceding information?<br>

2.  Which is the best network? Explain.<br>

3.  Write out a conditional distribution for
    ${\textbf{P}}(M_1{{\,|\,}}N)$, for the case where
    $N{{\,\in\\,}}\{1,2,3\}$ and $M_1{{\,\in\\,}}\{0,1,2,3,4\}$. Each
    entry in the conditional distribution should be expressed as a
    function of the parameters $e$ and/or $f$.<br>

4.  Suppose $M_1{{\,=\,}}1$ and $M_2{{\,=\,}}3$. What are the
    <i>possible</i> numbers of stars if you assume no prior
    constraint on the values of $N$?<br>

5.  What is the <i>most likely</i> number of stars, given these
    observations? Explain how to compute this, or if it is not possible
    to compute, explain what additional information is needed and how it
    would affect the result.<br>


---

##### Bài tập 14.15

Consider the network shown in
Figure <a class="insideExercisesFigRef" href="#telescope-nets-figure">telescope-nets-figure</a>(ii), and assume that the
two telescopes work identically. $N{{\,\in\\,}}\{1,2,3\}$ and
$M_1,M_2{{\,\in\\,}}\{0,1,2,3,4\}$, with the symbolic CPTs as described
in Exercise <a class="exerciseRef" href="{{ site.baseurl }}/bayes-nets-exercises/ex_14/">telescope-exercise</a>. Using the enumeration
algorithm (Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/enumeration-algorithm.png">enumeration-algorithm</a> on
page <a class="pageRef" id="pageref" title="" href="#">enumeration-algorithm</a>), calculate the probability distribution
${\textbf{P}}(N{{\,|\,}}M_1{{\,=\,}}2,M_2{{\,=\,}}2)$.<br>


<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/telescope-nets.svg" alt="telescope-nets-figure" id="telescope-nets-figure" style="width:100%">
  <figcaption><center><b>Three possible networks for the telescope problem.</b></center></figcaption>
</figure>


---

##### Bài tập 14.16

Consider the Bayes net shown in Figure <a class="insideExercisesFigRef" href="#politics-figure">politics-figure</a><br>.

1.  Which of the following are asserted by the network
    <i>structure</i>?<br>

    1.  ${\textbf{P}}(B,I,M) = {\textbf{P}}(B){\textbf{P}}(I){\textbf{P}}(M)$.<br>

    2.  ${\textbf{P}}(J|G) = {\textbf{P}}(J|G,I)$.<br>

    3.  ${\textbf{P}}(M|G,B,I) = {\textbf{P}}(M|G,B,I,J)$.<br>

2.  Calculate the value of $P(b,i,\lnot m,g,j)$.<br>

3.  Calculate the probability that someone goes to jail given that they
    broke the law, have been indicted, and face a politically
    motivated prosecutor.<br>

4.  A <b>context-specific independence</b> (see
    page <a class="pageRef" title="" href="#">CSI-page</a>) allows a variable to be independent of some of
    its parents given certain values of others. In addition to the usual
    conditional independences given by the graph structure, what
    context-specific independences exist in the Bayes net in
    Figure <a class="insideExercisesFigRef" href="#politics-figure">politics-figure</a>?<br>

5.  Suppose we want to add the variable
    $P={PresidentialPardon}$ to the network; draw the new
    network and briefly explain any links you add.<br>
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/politics.svg" alt="politics-figure" id="politics-figure" style="width:100%">
  <figcaption><center><b>A simple Bayes net with
  Boolean variables B = {BrokeElectionLaw}, I = {Indicted}, M = {PoliticallyMotivatedProsecutor}, G= {FoundGuilty}, J = {Jailed}.</b></center></figcaption>
</figure>


---

##### Bài tập 14.17

Consider the Bayes net shown in Figure <a class="insideExercisesFigRef" href="#politics-figure">politics-figure</a><br>.

1.  Which of the following are asserted by the network
    <i>structure</i>?<br>

    1.  ${\textbf{P}}(B,I,M) = {\textbf{P}}(B){\textbf{P}}(I){\textbf{P}}(M)$.<br>

    2.  ${\textbf{P}}(J|G) = {\textbf{P}}(J|G,I)$.<br>

    3.  ${\textbf{P}}(M|G,B,I) = {\textbf{P}}(M|G,B,I,J)$.<br>

2.  Calculate the value of $P(b,i,\lnot m,g,j)$.<br>

3.  Calculate the probability that someone goes to jail given that they
    broke the law, have been indicted, and face a politically
    motivated prosecutor.<br>

4.  A <b>context-specific independence</b> (see
    page <a class="pageRef" id="pageref" title="" href="#">CSI-page</a>) allows a variable to be independent of some of
    its parents given certain values of others. In addition to the usual
    conditional independences given by the graph structure, what
    context-specific independences exist in the Bayes net in
    Figure <a class="insideExercisesFigRef" id="insideexercisesfigref" href="#politics-figure">politics-figure</a>?<br>

5.  Suppose we want to add the variable
    $P={PresidentialPardon}$ to the network; draw the new
    network and briefly explain any links you add.<br>


---

##### Bài tập 14.18

Consider the variable elimination algorithm in
Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/elimination-ask-algorithm.png">elimination-ask-algorithm</a> (page <a class="pageRef" title="" href="#">elimination-ask-algorithm</a>).<br>

1.  Section <a class="sectionRef" title="" href="#">exact-inference-section</a> applies variable
    elimination to the query
    $${\textbf{P}}({Burglary}{{\,|\,}}{JohnCalls}{{\,=\,}}{true},{MaryCalls}{{\,=\,}}{true})\ .$$
    Perform the calculations indicated and check that the answer
    is correct.<br>

2.  Count the number of arithmetic operations performed, and compare it
    with the number performed by the enumeration algorithm.<br>

3.  Suppose a network has the form of a <i>chain</i>: a sequence
    of Boolean variables $X_1,\ldots, X_n$ where
    ${Parents}(X_i){{\,=\,}}\{X_{i-1}\}$ for $i{{\,=\,}}2,\ldots,n$.
    What is the complexity of computing
    ${\textbf{P}}(X_1{{\,|\,}}X_n{{\,=\,}}{true})$ using
    enumeration? Using variable elimination?<br>

4.  Prove that the complexity of running variable elimination on a
    polytree network is linear in the size of the tree for any variable
    ordering consistent with the network structure.<br>


---

##### Bài tập 14.19

Investigate the complexity of exact inference
in general Bayesian networks:<br>

1.  Prove that any 3-SAT problem can be reduced to exact inference in a
    Bayesian network constructed to represent the particular problem and
    hence that exact inference is NP-hard. (<i>Hint</i>:
    Consider a network with one variable for each proposition symbol,
    one for each clause, and one for the conjunction of clauses.)<br>

2.  The problem of counting the number of satisfying assignments for a
    3-SAT problem is \#P-complete. Show that exact inference is at least
    as hard as this.<br>


---

##### Bài tập 14.20

Consider the problem of generating a
random sample from a specified distribution on a single variable. Assume
you have a random number generator that returns a random number
uniformly distributed between 0 and 1.<br>

1.  Let $X$ be a discrete variable with
    $P(X{{\,=\,}}x_i){{\,=\,}}p_i$ for
    $i{{\,\in\\,}}\{1,\ldots,k\}$. The <b>cumulative distribution</b> of $X$ gives the probability
    that $X{{\,\in\\,}}\{x_1,\ldots,x_j\}$ for each possible $j$. (See
    also Appendix [math-appendix].) Explain how to
    calculate the cumulative distribution in $O(k)$ time and how to
    generate a single sample of $X$ from it. Can the latter be done in
    less than $O(k)$ time?<br>

2.  Now suppose we want to generate $N$ samples of $X$, where $N\gg k$.
    Explain how to do this with an expected run time per sample that is
    <i>constant</i> (i.e., independent of $k$).<br>

3.  Now consider a continuous-valued variable with a parameterized
    distribution (e.g., Gaussian). How can samples be generated from
    such a distribution?<br>

4.  Suppose you want to query a continuous-valued variable and you are
    using a sampling algorithm such as LIKELIHOODWEIGHTING to do the inference. How would
    you have to modify the query-answering process?


---

##### Bài tập 14.21

Consider the query
${\textbf{P}}({Rain}{{\,|\,}}{Sprinkler}{{\,=\,}}{true},{WetGrass}{{\,=\,}}{true})$
in Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/rain-clustering-figure.png">rain-clustering-figure</a>(a)
(page <a class="pageRef" title="" href="#">rain-clustering-figure</a>) and how Gibbs sampling can answer it.<br>

1.  How many states does the Markov chain have?<br>

2.  Calculate the <b>transition matrix</b>
    ${\textbf{Q}}$ containing
    $q({\textbf{y}}$ $\rightarrow$ ${\textbf{y}}')$
    for all ${\textbf{y}}$, ${\textbf{y}}'$.<br>

3.  What does ${\textbf{ Q}}^2$, the square of the
    transition matrix, represent?<br>

4.  What about ${\textbf{Q}}^n$ as $n\to \infty$?<br>

5.  Explain how to do probabilistic inference in Bayesian networks,
    assuming that ${\textbf{Q}}^n$ is available. Is this a
    practical way to do inference?


---

##### Bài tập 14.22

This exercise explores the stationary
distribution for Gibbs sampling methods.<br>

1.  The convex composition $[\alpha, q_1; 1-\alpha, q_2]$ of $q_1$ and
    $q_2$ is a transition probability distribution that first chooses
    one of $q_1$ and $q_2$ with probabilities $\alpha$ and $1-\alpha$,
    respectively, and then applies whichever is chosen. Prove that if
    $q_1$ and $q_2$ are in detailed balance with $\pi$, then their
    convex composition is also in detailed balance with $\pi$.
    (<i>Note</i>: this result justifies a variant of GIBBS-ASK in which
    variables are chosen at random rather than sampled in a
    fixed sequence.)<br>

2.  Prove that if each of $q_1$ and $q_2$ has $\pi$ as its stationary
    distribution, then the sequential composition
    $q {{\,=\,}}q_1 \circ q_2$ also has $\pi$ as its
    stationary distribution.<br>


---

##### Bài tập 14.23

The <b>Metropolis--Hastings</b> algorithm is a member of the MCMC family; as such,
it is designed to generate samples $\textbf{x}$ (eventually) according to target
probabilities $\pi(\textbf{x})$. (Typically we are interested in sampling from
$\pi(\textbf{x}){{\,=\,}}P(\textbf{x}{{\,|\,}}\textbf{e})$.) Like simulated annealing,
Metropolis–Hastings operates in two stages. First, it samples a new
state $\textbf{x'}$ from a <b>proposal distribution</b> $q(\textbf{x'}{{\,|\,}}\textbf{x})$, given the current state $\textbf{x}$.
Then, it probabilistically accepts or rejects $\textbf{x'}$ according to the <b>acceptance probability</b>
$$\alpha(\textbf{x'}{{\,|\,}}\textbf{x}) = \min\ \left(1,\frac{\pi(\textbf{x'})q(\textbf{x}{{\,|\,}}\textbf{x'})}{\pi(\textbf{x})q(\textbf{x'}{{\,|\,}}\textbf{x})}  \right)\ .$$
If the proposal is rejected, the state remains at $\textbf{x}$.<br>

1.  Consider an ordinary Gibbs sampling step for a specific variable
    $X_i$. Show that this step, considered as a proposal, is guaranteed
    to be accepted by Metropolis–Hastings. (Hence, Gibbs sampling is a
    special case of Metropolis–Hastings.)<br>

2.  Show that the two-step process above, viewed as a transition
    probability distribution, is in detailed balance with $\pi$.<br>


---

##### Bài tập 14.24

Three soccer teams $A$, $B$, and $C$, play each
other once. Each match is between two teams, and can be won, drawn, or
lost. Each team has a fixed, unknown degree of quality—an integer
ranging from 0 to 3—and the outcome of a match depends probabilistically
on the difference in quality between the two teams.<br>

1.  Construct a relational probability model to describe this domain,
    and suggest numerical values for all the necessary
    probability distributions.<br>

2.  Construct the equivalent Bayesian network for the three matches.<br>

3.  Suppose that in the first two matches $A$ beats $B$ and draws with
    $C$. Using an exact inference algorithm of your choice, compute the
    posterior distribution for the outcome of the third match.<br>

4.  Suppose there are $n$ teams in the league and we have the results
    for all but the last match. How does the complexity of predicting
    the last game vary with $n$?<br>

5.  Investigate the application of MCMC to this problem. How quickly
    does it converge in practice and how well does it scale?<br>


---


<!-- tabs:end -->
