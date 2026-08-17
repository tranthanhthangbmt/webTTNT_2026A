# Chapter 23 Reinforcement Learning

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_23_Reinforcement%20Learning/chapter_23_vi.html?v=1" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_23_Reinforcement%20Learning.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

*(Chưa có slide)*



#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter23/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/CYK-Parse.md" target="_blank" data-ignore>CYK-PARSE</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Sentence-Tree.md" target="_blank" data-ignore>SENTENCE-TREE</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/reinforcement_learning.ipynb"  target="_blank" data-ignore>Reinforcement Learning</a>
- <a href="python_runner.html?file=codeAndExercises/aima-python-master/notebooks/reinforcement_learning.py"  target="_blank" data-ignore>Reinforcement Learning (Python File)</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/sarsa.ipynb"  target="_blank" data-ignore>Sarsa</a>
- <a href="python_runner.html?file=codeAndExercises/aima-python-master/notebooks/sarsa.py"  target="_blank" data-ignore>Sarsa (Python File)</a>


#### **Bài tập**


##### Bài tập 23.1

Đọc đoạn văn sau một lần để hiểu, và ghi nhớ càng nhiều càng tốt. Sẽ có một bài kiểm tra sau.<br>

> Thủ tục thực ra khá đơn giản. Đầu tiên bạn sắp xếp mọi thứ thành các nhóm khác nhau. Tất nhiên, một đống có thể đủ tùy thuộc vào khối lượng công việc. Nếu bạn phải đi đến nơi khác do thiếu tiện nghi, đó là bước tiếp theo, nếu không thì bạn đã khá sẵn sàng. Điều quan trọng là không làm quá nhiều việc. Nghĩa là, thà làm quá ít việc cùng một lúc còn hơn làm quá nhiều. Về ngắn hạn, điều này có vẻ không quan trọng nhưng các biến chứng có thể dễ dàng phát sinh. Một sai lầm cũng rất tốn kém. Ban đầu, toàn bộ thủ tục sẽ có vẻ phức tạp. Tuy nhiên, chẳng bao lâu nữa, nó sẽ trở thành một khía cạnh khác của cuộc sống. Rất khó để dự đoán bất kỳ kết thúc nào cho sự cần thiết của nhiệm vụ này trong tương lai gần, nhưng rồi người ta không bao giờ biết được. Sau khi thủ tục hoàn thành, người ta lại sắp xếp tài liệu thành các nhóm khác nhau. Sau đó, chúng có thể được đặt vào đúng vị trí của chúng. Cuối cùng, chúng sẽ được sử dụng một lần nữa và toàn bộ chu kỳ sẽ phải lặp lại. Tuy nhiên, đây là một phần của cuộc sống.


---

##### Bài tập 23.2

Một <i>HMM grammar</i> về cơ bản là một HMM tiêu chuẩn có biến trạng thái là $N$ (nonterminal, với các giá trị như $Det$, $Adjective$, $Noun$ v.v.) và biến bằng chứng là $W$ (word, với các giá trị như $is$, $duck$, v.v.). Mô hình HMM bao gồm một prior ${\textbf{P}}(N_0)$, một mô hình chuyển tiếp ${\textbf{P}}(N_{t+1}|N_t)$, và một mô hình cảm biến ${\textbf{P}}(W_t|N_t)$. Chứng minh rằng mọi HMM grammar có thể được viết dưới dạng PCFG. [Gợi ý: bắt đầu bằng cách suy nghĩ về cách prior của HMM có thể được biểu diễn bằng các quy tắc PCFG cho ký hiệu câu. Bạn có thể thấy hữu ích khi minh họa cho HMM cụ thể với các giá trị $A$, $B$ cho $N$ và các giá trị $x$, $y$ cho $W$.]


---

##### Bài tập 23.3

Xem xét PCFG sau cho các cụm động từ đơn giản:<br>

> 0.1: VP $\rightarrow$ Verb<br>

> 0.2: VP $\rightarrow$ Copula Adjective<br>

> 0.5: VP $\rightarrow$ Verb the Noun<br>

> 0.2: VP $\rightarrow$ VP Adverb<br>

> 0.5: Verb $\rightarrow$ is<br>

> 0.5: Verb $\rightarrow$ shoots<br>

> 0.8: Copula $\rightarrow$ is<br>

> 0.2: Copula $\rightarrow$ seems<br>

> 0.5: Adjective $\rightarrow$ <b>unwell</b><br>

> 0.5: Adjective $\rightarrow$ <b>well</b><br>

> 0.5: Adverb $\rightarrow$ <b>well</b><br>

> 0.5: Adverb $\rightarrow$ <b>badly</b><br>

> 0.6: Noun $\rightarrow$ <b>duck</b><br>

> 0.4: Noun $\rightarrow$ <b>well</b><br>

1.  Trong các câu sau, câu nào có xác suất khác 0 với tư cách là VP? (i)
    shoots the duck well well well(ii) seems the well well(iii) shoots
    the unwell well badly<br>

2.  Xác suất để tạo ra “is well well” là bao nhiêu?<br>

3.  Các loại mơ hồ nào được thể hiện bởi cụm từ trong (b)?<br>

4.  Cho bất kỳ PCFG nào, có thể tính toán xác suất mà PCFG đó tạo ra một chuỗi gồm đúng 10 từ không?<br>


---

##### Bài tập 23.4

Xem xét PCFG đơn giản sau cho các cụm danh từ:<br>

> 0.6: NP $\rightarrow$ Det\ AdjString\ Noun<br>

> 0.4: NP $\rightarrow$ Det\ NounNounCompound<br>

> 0.5: AdjString $\rightarrow$ Adj\ AdjString<br>

> 0.5: AdjString $\rightarrow$ $\Lambda$<br>

> 1.0: NounNounCompound $\rightarrow$ Noun<br>

> 0.8: Det $\rightarrow$ <b>the</b><br>

> 0.2: Det $\rightarrow$ <b>a</b><br>

> 0.5: Adj $\rightarrow$ <b>small</b><br>

> 0.5: Adj $\rightarrow$ <b>green</b><br>

> 0.6: Noun $\rightarrow$ <b>village</b><br>

> 0.4: Noun $\rightarrow$ <b>green</b><br>

trong đó $\Lambda$ biểu thị chuỗi rỗng.<br>

1.  NP dài nhất có thể được tạo ra bởi ngữ pháp này là gì? (i)
    ba từ(ii) bốn từ(iii) vô số từ<br>

2.  Trong các câu sau, câu nào có xác suất khác 0 để được tạo ra dưới dạng NP hoàn chỉnh? (i) a small green village(ii) a green
    green green(iii) a small village green<br>

3.  Xác suất để tạo ra “the green green” là bao nhiêu?<br>

4.  Các loại mơ hồ nào được thể hiện bởi cụm từ trong (c)?<br>

5.  Cho bất kỳ PCFG nào và bất kỳ chuỗi từ hữu hạn nào, có thể tính toán xác suất mà chuỗi đó được tạo ra bởi PCFG không?<br>


---

##### Bài tập 23.5

Phác thảo những khác biệt chính giữa Java (hoặc bất kỳ ngôn ngữ máy tính nào khác mà bạn quen thuộc) và tiếng Anh, bình luận về vấn đề “hiểu” trong mỗi trường hợp. Hãy suy nghĩ về các khía cạnh như ngữ pháp, cú pháp, ngữ nghĩa, ngữ dụng, tính cấu thành, sự phụ thuộc vào ngữ cảnh, sự mơ hồ về từ vựng, sự mơ hồ về cú pháp, tìm kiếm tham chiếu (bao gồm cả đại từ), kiến thức nền và ý nghĩa của việc “hiểu” ngay từ đầu.


---

##### Bài tập 23.6

Bài tập này liên quan đến các ngữ pháp cho các ngôn ngữ rất đơn giản.<br>

1.  Viết một ngữ pháp ngữ cảnh tự do cho ngôn ngữ $a^n b^n$.<br>

2.  Viết một ngữ pháp ngữ cảnh tự do cho ngôn ngữ palindrome: tập hợp tất cả các chuỗi mà nửa sau là đảo ngược của nửa đầu.<br>

3.  Viết một ngữ pháp ngữ cảnh cho ngôn ngữ nhân đôi: tập hợp tất cả các chuỗi mà nửa sau giống hệt nửa đầu.<br>


---

##### Bài tập 23.7

Xem xét câu “Someone walked slowly to the supermarket” và một từ điển bao gồm các từ sau:<br>

$Pronoun \rightarrow \textbf{someone} \quad Verb \rightarrow \textbf{walked}$<br>

$Adv \rightarrow \textbf{slowly} \quad Prep \rightarrow \textbf{to}$<br>

$Article \rightarrow \textbf{the} \quad Noun \rightarrow \textbf{supermarket}$<br>

Trong ba ngữ pháp sau, ngữ pháp nào kết hợp với từ điển đã cho sẽ tạo ra câu trên? Trình bày cây phân tích cú pháp tương ứng.<br>

$$
\quad\quad\quad\quad (A):\quad\quad\quad\quad  \quad\quad\quad\quad(B):\quad\quad\quad\quad  \quad\quad\quad\quad(C):\\
\quad\quad\quad\quad S \rightarrow NP \space VP \quad\quad\quad\quad \quad\quad\quad\quad S\rightarrow NP\space VP \quad\quad\quad\quad S\rightarrow NP\space VP\\
\quad\quad\quad\quad NP\rightarrow Pronoun \quad\quad\quad\quad  NP\rightarrow Pronoun \quad\quad\quad\quad  NP\rightarrow Pronoun\\
\quad\quad\quad\quad NP\rightarrow Article\space Noun \quad\quad\quad\quad  NP\rightarrow Noun \quad\quad\quad\quad  NP\rightarrow Article\space NP\\
\quad\quad\quad\quad VP\rightarrow VP\space PP \quad\quad\quad\quad NP\rightarrow Article\space NP \quad\quad\quad\quad  VP\rightarrow Verb\space Adv\\
\quad\quad\quad\quad  VP\rightarrow VP\space Adv\space Adv \quad\quad\quad\quad  VP\rightarrow Verb\space Vmod \quad\quad\quad\quad  Adv\rightarrow Adv\space Adv\\
\quad\quad\quad\quad  VP\rightarrow Verb \quad\quad\quad\quad  Vmod\rightarrow Adv\space Vmod \quad\quad\quad\quad   Adv\rightarrow PP\\
\quad\quad\quad\quad PP\rightarrow Prep\space NP \quad\quad\quad\quad Vmod\rightarrow Adv \quad\quad\quad\quad PP\rightarrow Prep\space NP\\
\quad\quad\quad\quad NP\rightarrow Noun \quad\quad\quad\quad Adv\rightarrow PP \quad\quad\quad\quad NP\rightarrow Noun\\
\quad\quad\quad\quad\quad \quad\quad\quad\quad PP\rightarrow Prep\space NP \quad\quad\quad\quad \quad\quad\quad\quad

$$

Đối với mỗi ngữ pháp trên, hãy viết ba câu tiếng Anh và ba câu không phải tiếng Anh được tạo ra bởi ngữ pháp đó. Mỗi câu phải khác biệt đáng kể, ít nhất sáu từ, và bao gồm một số mục từ vựng mới (mà bạn nên định nghĩa). Đề xuất các cách để cải thiện mỗi ngữ pháp để tránh tạo ra các câu không phải tiếng Anh.


---

##### Bài tập 23.8

Thu thập một số ví dụ về cách diễn đạt thời gian, chẳng hạn như “two o’clock,” “midnight,” và “12:46.” Cũng nghĩ ra một số ví dụ không đúng ngữ pháp, chẳng hạn như “thirteen o’clock” hoặc “half past two fifteen.” Viết một ngữ pháp cho ngôn ngữ thời gian.


---

##### Bài tập 23.9

Một số nhà ngôn ngữ học đã lập luận như sau:<br>
<br>
 Trẻ em học ngôn ngữ chỉ nghe các <i>ví dụ tích cực</i> về ngôn ngữ và không có <i>ví dụ tiêu cực</i>. Do đó, giả thuyết rằng “mọi câu có thể có đều thuộc về ngôn ngữ” là nhất quán với tất cả các ví dụ đã quan sát được. Hơn nữa, đây là giả thuyết nhất quán đơn giản nhất. Hơn nữa, tất cả các ngữ pháp cho các ngôn ngữ là tập hợp cha của ngôn ngữ thực sự cũng nhất quán với dữ liệu đã quan sát được. Tuy nhiên, trẻ em suy luận (ít nhiều) ngữ pháp đúng. Do đó, chúng bắt đầu với các ràng buộc ngữ pháp bẩm sinh rất mạnh mẽ loại trừ tất cả các giả thuyết tổng quát hơn này <i>a priori</i>.<br>

Bình luận về điểm yếu trong lập luận này từ quan điểm học thống kê.


---

##### Bài tập 23.10

Trong bài tập này, bạn sẽ chuyển đổi $\large \varepsilon_0$ sang dạng chuẩn Chomsky (CNF). Có năm bước: (a) Thêm một ký hiệu bắt đầu mới, (b) Loại bỏ các quy tắc $\epsilon$, (c) Loại bỏ nhiều từ ở vế phải, (d) Loại bỏ các quy tắc có dạng (${\it X} \rightarrow{{\;}}$${\it Y}$), (e) Chuyển đổi các vế phải dài thành các quy tắc nhị phân.<br>

1.  Ký hiệu bắt đầu, $S$, chỉ có thể xuất hiện ở vế trái trong CNF. Thay thế ${\it S}$ ở mọi nơi bằng một ký hiệu mới ${\it S'}$ và thêm một quy tắc có dạng ${\it S}$ ${{\;}}\rightarrow{{\;}}$${\it S'}$.<br>

2.  Chuỗi rỗng, $\epsilon$, không thể xuất hiện ở vế phải trong CNF. $\large \varepsilon_0$ không có quy tắc nào có $\epsilon$, vì vậy đây không phải là vấn đề.<br>

3.  Một từ có thể xuất hiện ở vế phải trong một quy tắc chỉ có dạng (${\it X}$ ${{\;}}\rightarrow{{\;}}$<i>word</i>). Thay thế mỗi quy tắc có dạng (${\it X}$ ${{\;}}\rightarrow{{\;}}$…<i>word</i> …) bằng (${\it X}$ ${{\;}}\rightarrow{{\;}}$…${\it W'}$ …) và (${\it W'}$ ${{\;}}\rightarrow{{\;}}$<i>word</i>), sử dụng một ký hiệu mới ${\it W'}$.<br>

4.  Quy tắc (${\it X}$ ${{\;}}\rightarrow{{\;}}$${\it Y}$) không được phép trong CNF; nó phải là (${\it X}$ ${{\;}}\rightarrow{{\;}}$${\it Y}$ ${\it Z}$) hoặc (${\it X}$ ${{\;}}\rightarrow{{\;}}$<i>word</i>). Thay thế mỗi quy tắc có dạng (${\it X}$ ${{\;}}\rightarrow{{\;}}$${\it Y}$) bằng một tập hợp các quy tắc có dạng (${\it X}$ ${{\;}}\rightarrow{{\;}}$…), một cho mỗi quy tắc (${\it Y}$ ${{\;}}\rightarrow{{\;}}$…), trong đó (…) biểu thị một hoặc nhiều ký hiệu.<br>

5.  Thay thế mỗi quy tắc có dạng (${\it X}$ ${{\;}}\rightarrow{{\;}}$${\it Y}$ ${\it Z}$ …) bằng hai quy tắc, (${\it X}$ ${{\;}}\rightarrow{{\;}}$${\it Y}$ ${\it Z'}$) và (${\it Z'}$ ${{\;}}\rightarrow{{\;}}$${\it Z}$ …), trong đó ${\it Z'}$ là một ký hiệu mới.<br>

Trình bày từng bước của quy trình và tập hợp các quy tắc cuối cùng.<br>


---

##### Bài tập 23.11

Xem xét ngữ pháp đồ chơi sau:<br>

> $S \rightarrow NP\space VP$<br>

> $NP \rightarrow Noun$<br>

> $NP \rightarrow NP\space and\space NP$<br>

> $NP \rightarrow NP\space PP$<br>

> $VP \rightarrow Verb$<br>

> $VP \rightarrow VP\space and \space VP$<br>

> $VP \rightarrow VP\space PP$<br>

> $PP \rightarrow Prep\space NP$<br>

> $Noun \rightarrow Sally\space; pools\space; streams\space; swims$<br>

> $Prep \rightarrow in$<br>

> $Verb \rightarrow pools\space; streams\space; swims$<br>

1.  Trình bày tất cả các cây phân tích cú pháp trong ngữ pháp này cho câu “Sally swims in streams and pools.”<br>

2.  Trình bày tất cả các mục bảng sẽ được tạo ra bởi một trình phân tích cú pháp CYK (không xác suất) trên câu này.<br>


---

##### Bài tập 23.12

Sử dụng ký hiệu DCG, viết một ngữ pháp cho một ngôn ngữ giống hệt $\large \varepsilon_1$, ngoại trừ việc nó thực thi sự hòa hợp giữa chủ ngữ và động từ của một câu và do đó không tạo ra các câu không đúng ngữ pháp như “I smells the wumpus.”


---

##### Bài tập 23.13

Xem xét PCFG sau:<br>

> $S \rightarrow NP \space VP[1.0] $<br>

> $NP \rightarrow \textit{Noun}[0.6] \space|\space \textit{Pronoun}[0.4] $<br>

> $VP \rightarrow \textit{Verb} \space NP[0.8] \space|\space \textit{Modal}\space \textit{Verb}[0.2]$<br>

> $\textit{Noun} \rightarrow \textbf{can}[0.1] \space|\space \textbf{fish}[0.3] \space|\space ...$<br>

> $\textit{Pronoun} \rightarrow \textbf{I}[0.4] \space|\space ...$<br>

> $\textit{Verb} \rightarrow \textbf{can}[0.01] \space|\space \textbf{fish}[0.1] \space|\space ...$<br>

> $\textit{Modal} \rightarrow \textbf{can}[0.3] \space|\space ...$<br>

Câu “I can fish” có hai cây phân tích cú pháp với ngữ pháp này. Trình bày hai cây, xác suất tiên nghiệm của chúng và xác suất có điều kiện của chúng, cho trước câu đó.


---

##### Bài tập 23.14

Một ngữ pháp ngữ cảnh tự do tăng cường có thể biểu diễn các ngôn ngữ mà ngữ pháp ngữ cảnh tự do thông thường không thể. Trình bày một ngữ pháp ngữ cảnh tự do tăng cường cho ngôn ngữ $a^nb^nc^n$. Các giá trị cho phép cho các biến tăng cường là 1 và $SUCCESSOR(n)$, trong đó $n$ là một giá trị. Quy tắc cho một câu trong ngôn ngữ này là<br>
$$S(n) \rightarrow A(n) B(n) C(n) \ .$$
Trình bày quy tắc(các quy tắc) cho mỗi ${\it A}$, ${\it B}$, và ${\it C}$.


---

##### Bài tập 23.15

Tăng cường ngữ pháp $\large \varepsilon_1$ để nó xử lý sự hòa hợp giữa mạo từ và danh từ. Nghĩa là, đảm bảo rằng “agents” và “an agent” là các NP, nhưng “agent” và “an agents” thì không.


---

##### Bài tập 23.16

Xem xét câu sau (từ <i>The New York Times,</i> ngày 28 tháng 7 năm 2008):<br>

> Banks struggling to recover from multibillion-dollar loans on real
> estate are curtailing loans to American businesses, depriving even
> healthy companies of money for expansion and hiring.

1.  Những từ nào trong câu này bị mơ hồ về mặt từ vựng?<br>

2.  Tìm hai trường hợp mơ hồ về cú pháp trong câu này (có nhiều hơn hai.)<br>

3.  Đưa ra một ví dụ về phép ẩn dụ trong câu này.<br>

4.  Bạn có thể tìm thấy sự mơ hồ về ngữ nghĩa không?<br>


---

##### Bài tập 23.17

Không nhìn lại Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/nlp-english-exercises/ex_1/">washing-clothes-exercise</a>, trả lời các câu hỏi sau:<br>

1.  Bốn bước được đề cập là gì?<br>

2.  Bước nào bị bỏ sót?<br>

3.  “Tài liệu” được đề cập trong văn bản là gì?<br>

4.  Loại sai lầm nào sẽ tốn kém?<br>

5.  Thà làm quá ít việc hay quá nhiều việc? Tại sao?<br>


---

##### Bài tập 23.18

Chọn năm câu và gửi chúng đến một dịch vụ dịch thuật trực tuyến. Dịch chúng từ tiếng Anh sang một ngôn ngữ khác và quay lại tiếng Anh. Đánh giá các câu kết quả về tính ngữ pháp và sự bảo toàn ý nghĩa. Lặp lại quy trình; vòng lặp thứ hai cho kết quả tệ hơn hay giống nhau? Việc lựa chọn ngôn ngữ trung gian có tạo ra sự khác biệt về chất lượng kết quả không? Nếu bạn biết một ngoại ngữ, hãy xem bản dịch của một đoạn văn sang ngôn ngữ đó. Đếm và mô tả các lỗi đã mắc phải, và suy đoán lý do tại sao những lỗi đó lại xảy ra.


---

##### Bài tập 23.19

Các giá trị $D_i$ cho câu trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/mt-alignment-figure.png">mt-alignment-figure</a> có tổng bằng 0. Điều này có đúng với mọi cặp dịch không? Chứng minh hoặc đưa ra một phản ví dụ.


---

##### Bài tập 23.20

(Chuyển thể từ [<a class="paperRef" title="" href="">Knight:1999</a>].) Mô hình dịch của chúng tôi giả định rằng, sau khi mô hình dịch cụm chọn các cụm và mô hình biến dạng sắp xếp lại chúng, mô hình ngôn ngữ có thể sắp xếp lại sự sắp xếp đó. Bài tập này điều tra mức độ hợp lý của giả định đó. Hãy thử sắp xếp lại các danh sách cụm được đề xuất sau đây theo đúng thứ tự:<br>

1.  have, programming, a, seen, never, I, language, better<br>

2.  loves, john, mary<br>

3.  is the, communication, exchange of, intentional, information
    brought, by, about, the production, perception of, and signs, from,
    drawn, a, of, system, signs, conventional, shared<br>

4.  created, that, we hold these, to be, all men, truths, are, equal,
    self-evident<br>

Bạn có thể làm được những câu nào? Bạn đã sử dụng loại kiến thức nào? Huấn luyện một mô hình bigram từ một tập dữ liệu huấn luyện và sử dụng nó để tìm hoán vị có xác suất cao nhất của một số câu từ một tập dữ liệu kiểm tra. Báo cáo về độ chính xác của mô hình này.


---

##### Bài tập 23.21

Tính toán đường đi có xác suất cao nhất qua HMM trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/sr-hmm-figure.png">sr-hmm-figure</a> cho chuỗi đầu ra $[C_1,C_2,C_3,C_4,C_4,C_6,C_7]$. Cũng đưa ra xác suất của nó.


---

##### Bài tập 23.22

Chúng tôi quên đề cập rằng văn bản trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/nlp-english-exercises/ex_1/">washing-clothes-exercise</a> có tiêu đề “Washing Clothes.” Đọc lại văn bản và trả lời các câu hỏi trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/nlp-english-exercises/ex_17/">washing-clothes2-exercise</a>. Lần này bạn làm tốt hơn chứ? Bransford và Johnson [<a class="paperRef" title="" href="">Bransford+Johnson:1973</a>] đã sử dụng văn bản này trong một thí nghiệm có kiểm soát và nhận thấy rằng tiêu đề đã giúp ích đáng kể. Điều này cho bạn biết gì về cách ngôn ngữ và trí nhớ hoạt động?


---

<!-- tabs:end -->
