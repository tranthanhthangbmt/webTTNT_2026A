# Chapter 05 Constraint Satisfaction Problems

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_05/chapter_05_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_05_Constraint%20Satisfaction%20Problems.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter05_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter05/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
- <a href="codeAndExercises/aima-pseudocode-master/md/Minimax-Decision.md" target="_blank" data-ignore>MINIMAX-SEARCH</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Alpha-Beta-Search.md" target="_blank" data-ignore>ALPHA-BETA-SEARCH</a>
- <a href="codeAndExercises/aima-pseudocode-master/md/Monte-Carlo-Tree-Search.md" target="_blank" data-ignore>MONTE-CARLO-TREE-SEARCH</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/csp.ipynb"  target="_blank" data-ignore>Csp</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/csp.ipynb"   target="_blank" data-ignore>Csp (Python File)</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/arc_consistency_heuristics.ipynb"  target="_blank" data-ignore>Arc Consistency Heuristics</a>
- <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/arc_consistency_heuristics.ipynb"   target="_blank" data-ignore>Arc Consistency Heuristics (Python File)</a>


#### **Bài tập**


Tuyệt vời! Dưới đây là bản dịch các bài tập sang tiếng Việt, tuân thủ nghiêm ngặt các quy tắc bạn đã đặt ra:

##### Bài tập 5.1

Giả sử bạn có một oracle, $OM(s)$, có thể dự đoán chính xác nước đi của đối thủ trong bất kỳ state nào. Sử dụng oracle này, hãy định nghĩa một game như một bài toán search (single-agent). Mô tả một thuật toán để tìm nước đi tối ưu.


---

###### Bài tập 5.2

Xem xét bài toán giải hai bàn cờ 8-puzzle.<br>

1.  Đưa ra một formulation bài toán hoàn chỉnh theo phong cách của Chương <a class="chapterRef" title="" href="{{site.baseurl}}/search-exercises/">search-chapter.</a><br>

2.  Không gian state có thể đạt được lớn đến mức nào? Đưa ra một biểu thức số chính xác.<br>

3.  Giả sử chúng ta làm cho bài toán trở nên đối kháng như sau: hai người chơi lần lượt di chuyển; một đồng xu được tung để xác định bàn cờ sẽ thực hiện nước đi trong lượt đó; và người chiến thắng là người đầu tiên giải được một bàn cờ. Thuật toán nào có thể được sử dụng để chọn nước đi trong cài đặt này?<br>

4.  Trò chơi có kết thúc cuối cùng hay không, với lối chơi tối ưu? Giải thích.<br>(a) Một bản đồ với chi phí của mỗi cạnh là 1. Ban đầu, người truy đuổi $P$ ở node <b>b</b> và người chạy trốn $E$ ở node <b>d</b> <br>(b) Một cây game một phần cho bản đồ này. Mỗi node được gán nhãn với vị trí $P,E$. $P$ đi trước. Các nhánh được đánh dấu "?" chưa được khám phá.
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/pursuit-evasion-game.svg" alt="pursuit-evasion-game-figure" id="pursuit-evasion-game-figure" style="width:100%">
  <figcaption><center><b>Hình ảnh trò chơi truy đuổi - chạy trốn</b></center></figcaption>
</figure>


---

##### Bài tập 5.3

Hãy tưởng tượng rằng, trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_5/">two-friends-exercise</a>, một trong hai người bạn muốn tránh người kia. Bài toán sau đó trở thành một trò chơi hai người chơi. Chúng ta giả định bây giờ người chơi lần lượt di chuyển. Trò chơi chỉ kết thúc khi người chơi ở cùng một node; phần thưởng cuối cùng cho người truy đuổi là trừ đi tổng thời gian đã thực hiện. (Người chạy trốn "thắng" bằng cách không bao giờ thua.) Một ví dụ được hiển thị trong Hình.
<a href="#pursuit-evasion-game-figure">pursuit-evasion-game-figure</a><br>


1.  Sao chép cây game và đánh dấu giá trị của các node cuối. <br>

2.  Bên cạnh mỗi node nội bộ, hãy viết sự kiện mạnh nhất mà bạn có thể suy luận về giá trị của nó (một số, một hoặc nhiều bất đẳng thức như “$\geq 14$”, hoặc một “?”).<br>

3.  Bên dưới mỗi dấu hỏi, hãy viết tên của node được đạt tới bởi nhánh đó.<br>

4.  Giải thích làm thế nào một giới hạn về giá trị của các node trong (c) có thể được suy ra từ việc xem xét độ dài đường đi ngắn nhất trên bản đồ, và suy ra các giới hạn như vậy cho các node này. Hãy nhớ chi phí để đến mỗi lá cũng như chi phí để giải nó.<br>

5.  Bây giờ giả sử cây như đã cho, với các giới hạn lá từ (d), được đánh giá từ trái sang phải. Khoanh tròn những node “?” sẽ *không* cần được mở rộng thêm, dựa trên các giới hạn từ phần (d), và gạch chéo những node không cần xem xét.<br>

6.  Bạn có thể chứng minh điều gì nói chung về việc ai thắng trò chơi trên một bản đồ là một cây không?<br>


---

##### Bài tập 5.4

Mô tả và triển khai các mô tả state, bộ tạo nước đi (move generators), kiểm tra cuối cùng (terminal tests), hàm tiện ích (utility functions), và hàm đánh giá (evaluation functions) cho một hoặc nhiều trò chơi ngẫu nhiên sau: Monopoly, Scrabble, chơi bridge với một hợp đồng đã cho, hoặc poker Texas hold’em.
<div id="game-playing-chance-exercise"></div>


---

##### Bài tập 5.5

Mô tả và triển khai một môi trường chơi game *thời gian thực*, *nhiều người chơi*, nơi thời gian là một phần của state môi trường và người chơi được phân bổ thời gian cố định.


---

##### Bài tập 5.6

Thảo luận về mức độ phù hợp của cách tiếp cận tiêu chuẩn để chơi game đối với các trò chơi như tennis, pool và croquet, diễn ra trong một không gian state vật lý liên tục.


---

###### Bài tập 5.7

Chứng minh khẳng định sau: Đối với mọi cây game, utility mà max thu được bằng cách sử dụng các quyết định minimax khi đối đầu với một min không tối ưu sẽ không bao giờ thấp hơn utility thu được khi chơi với một min tối ưu. Bạn có thể đưa ra một cây game mà max có thể làm tốt hơn nữa bằng cách sử dụng một chiến lược *không tối ưu* khi đối đầu với một min không tối ưu không?
<br>
Người chơi $A$ đi trước. Hai người chơi lần lượt di chuyển, và mỗi người chơi phải di chuyển token của mình đến một ô trống liền kề theo bất kỳ hướng nào. Nếu đối thủ chiếm một ô liền kề, thì người chơi có thể nhảy qua đối thủ đến ô trống tiếp theo nếu có. (Ví dụ, nếu $A$ ở ô 3 và $B$ ở ô 2, thì $A$ có thể lùi về ô 1.) Trò chơi kết thúc khi một người chơi đạt đến đầu đối diện của bàn cờ. Nếu người chơi $A$ đạt đến ô 4 trước, thì giá trị của trò chơi đối với $A$ là $+1$; nếu người chơi $B$ đạt đến ô 1 trước, thì giá trị của trò chơi đối với $A$ là $-1$.
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/line-game4.svg" alt="line-game4-figure" id="line-game4-figure" style="width:100%">
  <figcaption><center><b>Vị trí bắt đầu của một trò chơi đơn giản.</b></center></figcaption>
</figure>


---

##### Bài tập 5.8

Xem xét trò chơi hai người chơi được mô tả trong Hình <a class="insideExerciseFigRef" href="#line-game4-figure">line-game4-figure</a><br>

1.  Vẽ cây game hoàn chỉnh, sử dụng các quy ước sau:<br>

    -   Viết mỗi state dưới dạng $(s_A,s_B)$, trong đó $s_A$ và $s_B$ biểu thị vị trí của token.<br>

    -   Đặt mỗi state cuối cùng trong một ô vuông và viết giá trị game của nó trong một vòng tròn.<br>

    -   Đặt các *state lặp* (các state đã xuất hiện trên đường đi đến gốc) trong các ô vuông đôi. Vì giá trị của chúng không rõ ràng, hãy chú thích mỗi ô bằng một dấu “?” trong một vòng tròn.<br>

2.  Bây giờ hãy đánh dấu mỗi node bằng giá trị minimax được sao lưu của nó (cũng trong một vòng tròn). Giải thích cách bạn xử lý các giá trị “?” và tại sao.<br>

3.  Giải thích tại sao thuật toán minimax tiêu chuẩn sẽ thất bại trên cây game này và phác thảo ngắn gọn cách bạn có thể sửa nó, dựa trên câu trả lời của bạn cho (b). Thuật toán đã sửa đổi của bạn có đưa ra các quyết định tối ưu cho tất cả các trò chơi có vòng lặp không?<br>

4.  Trò chơi 4 ô vuông này có thể được tổng quát hóa thành $n$ ô vuông cho bất kỳ $n > 2$ nào. Chứng minh rằng $A$ thắng nếu $n$ chẵn và thua nếu $n$ lẻ.


---

##### Bài tập 5.9

Bài toán này kiểm tra các khái niệm cơ bản về chơi game, sử dụng tic-tac-toe (cờ ca-rô) làm ví dụ. Chúng ta định nghĩa $X_n$ là số hàng, cột hoặc đường chéo có chính xác $n$ ký hiệu $X$ và không có ký hiệu $O$. Tương tự, $O_n$ là số hàng, cột hoặc đường chéo chỉ có $n$ ký hiệu $O$. Hàm tiện ích gán $+1$ cho bất kỳ vị trí nào có $X_3=1$ và $-1$ cho bất kỳ vị trí nào có $O_3 = 1$. Tất cả các vị trí cuối cùng khác có utility 0. Đối với các vị trí không cuối cùng, chúng ta sử dụng hàm đánh giá tuyến tính được định nghĩa là ${Eval}(s) = 3X_2(s) + X_1(s) - (3O_2(s) + O_1(s))$. <br>

1.  Ước tính có khoảng bao nhiêu trò chơi tic-tac-toe có thể có?<br>

2.  Hiển thị toàn bộ cây game bắt đầu từ một bàn cờ trống cho đến độ sâu 2 (tức là, một $X$ và một $O$ trên bàn cờ), có tính đến tính đối xứng.<br>

3.  Đánh dấu trên cây của bạn các giá trị đánh giá của tất cả các vị trí ở độ sâu 2.<br>

4.  Sử dụng thuật toán minimax, đánh dấu trên cây của bạn các giá trị sao lưu cho các vị trí ở độ sâu 1 và 0, và sử dụng các giá trị đó để chọn nước đi bắt đầu tốt nhất.<br>

5.  Khoanh tròn các node ở độ sâu 2 sẽ *không* được đánh giá nếu áp dụng alpha–beta pruning, giả sử các node được tạo ra theo thứ tự tối ưu cho alpha–beta pruning.<br>


---

##### Bài tập 5.10

Xem xét họ các trò chơi tic-tac-toe tổng quát, được định nghĩa như sau. Mỗi trò chơi cụ thể được chỉ định bởi một tập hợp $\mathcal S$ các *ô* và một tập hợp $\mathcal W$ các *vị trí thắng*. Mỗi vị trí thắng là một tập con của $\mathcal S$. Ví dụ, trong tic-tac-toe tiêu chuẩn, $\mathcal S$ là một tập hợp gồm 9 ô và $\mathcal W$ là một tập hợp gồm 8 tập con của $\mathcal W$: ba hàng, ba cột và hai đường chéo. Theo các khía cạnh khác, trò chơi giống hệt tic-tac-toe tiêu chuẩn. Bắt đầu từ một bàn cờ trống, người chơi lần lượt đặt dấu của họ vào một ô trống. Người chơi nào đánh dấu mọi ô trong một vị trí thắng thì thắng trò chơi. Đó là một trận hòa nếu tất cả các ô đều được đánh dấu và không người chơi nào thắng.<br>

1.  Đặt $N= |{\mathcal S}|$, số lượng ô. Đưa ra một giới hạn trên về số lượng node trong cây game hoàn chỉnh cho tic-tac-toe tổng quát như một hàm của $N$.<br>

2.  Đưa ra một giới hạn dưới về kích thước của cây game cho trường hợp xấu nhất, trong đó ${\mathcal W} = {\{\,\}}$.<br>

3.  Đề xuất một hàm đánh giá hợp lý có thể được sử dụng cho bất kỳ trường hợp nào của tic-tac-toe tổng quát. Hàm có thể phụ thuộc vào $\mathcal S$ và $\mathcal W$.<br>

4.  Giả sử rằng có thể tạo ra một bàn cờ mới và kiểm tra xem nó có phải là một vị trí thắng hay không trong 100$N$ lệnh máy và giả sử bộ xử lý 2 gigahertz. Bỏ qua giới hạn bộ nhớ. Sử dụng ước tính của bạn trong (a), ước tính có thể giải quyết hoàn toàn bao nhiêu cây game bằng alpha–beta trong một giây thời gian CPU? một phút? một giờ?<br>


---

##### Bài tập 5.11

Phát triển một chương trình chơi game tổng quát, có khả năng chơi nhiều trò chơi khác nhau.<br>

1.  Triển khai các bộ tạo nước đi (move generators) và hàm đánh giá cho một hoặc nhiều trò chơi sau: Kalah, Othello, checkers và chess.<br>

2.  Xây dựng một agent chơi game alpha–beta tổng quát.<br>

3.  So sánh tác động của việc tăng độ sâu tìm kiếm, cải thiện thứ tự nước đi (move ordering), và cải thiện hàm đánh giá. Hệ số phân nhánh hiệu quả của bạn gần với trường hợp lý tưởng của thứ tự nước đi hoàn hảo đến mức nào?<br>

4.  Triển khai một thuật toán tìm kiếm có chọn lọc, chẳng hạn như B\* <a class="paperRef" title="" href="">Berliner:1979</a>, conspiracy number search @McAllester:1988, hoặc MGSS\* <a class="paperRef" title="" href="">Russell+Wefald:1989</a> và so sánh hiệu suất của nó với A\*.<br>


---

##### Bài tập 5.12

Mô tả cách các thuật toán minimax và alpha–beta thay đổi đối với các trò chơi hai người chơi, không phải tổng bằng không (non-zero-sum) trong đó mỗi người chơi có một hàm tiện ích riêng biệt và cả hai hàm tiện ích đều được cả hai người chơi biết. Nếu không có ràng buộc nào đối với hai tiện ích cuối cùng, liệu có thể có bất kỳ node nào bị cắt tỉa bởi alpha–beta không? Điều gì xảy ra nếu hàm tiện ích của người chơi trên bất kỳ state nào khác nhau tối đa là một hằng số $k$, làm cho trò chơi gần như hợp tác?<br>


---

##### Bài tập 5.13

Mô tả cách các thuật toán minimax và alpha–beta thay đổi đối với các trò chơi hai người chơi, không phải tổng bằng không (non-zero-sum) trong đó mỗi người chơi có một hàm tiện ích riêng biệt và cả hai hàm tiện ích đều được cả hai người chơi biết. Nếu không có ràng buộc nào đối với hai tiện ích cuối cùng, liệu có thể có bất kỳ node nào bị cắt tỉa bởi alpha–beta không? Điều gì xảy ra nếu tổng các hàm tiện ích của người chơi trên bất kỳ state nào nằm trong khoảng giữa các hằng số $-k$ và $k$, làm cho trò chơi gần như tổng bằng không?<br>


---

###### Bài tập 5.14

Phát triển một chứng minh chính thức về tính đúng đắn của alpha–beta pruning. Để làm điều này, hãy xem xét tình huống được hiển thị trong Hình <a class="insideExerciseFigRef" href="#alpha-beta-proof-figure">alpha-beta-proof-figure</a>. Câu hỏi là liệu có nên cắt tỉa node $n_j$ hay không, đây là một max-node và là hậu duệ của node $n_1$. Ý tưởng cơ bản là cắt tỉa nó khi và chỉ khi giá trị minimax của $n_1$ có thể được chứng minh là độc lập với giá trị của $n_j$.<br>

1.  Node $n_1$ nhận giá trị nhỏ nhất trong số các con của nó: $n_1 = \min(n_2,n_{{21}},\ldots,n_{2b_2})$. Tìm một biểu thức tương tự cho $n_2$ và do đó một biểu thức cho $n_1$ theo $n_j$.<br>

2.  Đặt $l_i$ là giá trị nhỏ nhất (hoặc lớn nhất) của các node ở *bên trái* node $n_i$ ở độ sâu $i$, có giá trị minimax đã biết. Tương tự, đặt $r_i$ là giá trị nhỏ nhất (hoặc lớn nhất) của các node chưa được khám phá ở bên phải $n_i$ ở độ sâu $i$. Viết lại biểu thức của bạn cho $n_1$ theo các giá trị $l_i$ và $r_i$.<br>

3.  Bây giờ hãy diễn đạt lại biểu thức để cho thấy rằng để ảnh hưởng đến $n_1$, $n_j$ phải không vượt quá một giới hạn nhất định được suy ra từ các giá trị $l_i$.<br>

4.  Lặp lại quy trình cho trường hợp $n_j$ là một min-node.<br>
<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/alpha-beta-proof.svg" alt="alpha-beta-proof-figure" id="alpha-beta-proof-figure" style="width:100%">
  <figcaption><center><b>Tình huống khi xem xét liệu có nên cắt tỉa node $n_j$ hay không.</b></center></figcaption>
</figure>


---

##### Bài tập 5.15

Chứng minh rằng thuật toán alpha–beta mất thời gian $O(b^{m/2})$ với thứ tự nước đi tối ưu, trong đó $m$ là độ sâu tối đa của cây game.


---

##### Bài tập 5.16

Giả sử bạn có một chương trình cờ vua có thể đánh giá 5 triệu node mỗi giây. Quyết định một biểu diễn nhỏ gọn của một state game để lưu trữ trong một bảng chuyển vị (transposition table). Khoảng bao nhiêu mục nhập bạn có thể đặt vừa vào một bảng 1 gigabyte trong bộ nhớ? Số lượng đó có đủ cho ba phút tìm kiếm được phân bổ cho một nước đi không? Bạn có thể thực hiện bao nhiêu lần tra cứu bảng trong thời gian cần thiết để thực hiện một lần đánh giá? Bây giờ giả sử bảng chuyển vị được lưu trữ trên đĩa. Khoảng bao nhiêu lần đánh giá bạn có thể thực hiện trong thời gian cần thiết để thực hiện một lần tìm kiếm đĩa với phần cứng đĩa tiêu chuẩn?<br>


---

###### Bài tập 5.17

Giả sử bạn có một chương trình cờ vua có thể đánh giá 10 triệu node mỗi giây. Quyết định một biểu diễn nhỏ gọn của một state game để lưu trữ trong một bảng chuyển vị (transposition table). Khoảng bao nhiêu mục nhập bạn có thể đặt vừa vào một bảng 2 gigabyte trong bộ nhớ? Số lượng đó có đủ cho ba phút tìm kiếm được phân bổ cho một nước đi không? Bạn có thể thực hiện bao nhiêu lần tra cứu bảng trong thời gian cần thiết để thực hiện một lần đánh giá? Bây giờ giả sử bảng chuyển vị được lưu trữ trên đĩa. Khoảng bao nhiêu lần đánh giá bạn có thể thực hiện trong thời gian cần thiết để thực hiện một lần tìm kiếm đĩa với phần cứng đĩa tiêu chuẩn?<br>


<figure>
  <img src="https://aimacode.github.io/aima-exercises/figures/pruning.svg" alt="trivial-chance-game-figure" id="trivial-chance-game-figure" style="width:100%">
  <figcaption><center><b>Cây game hoàn chỉnh cho một trò chơi đơn giản với các node cơ hội.</b></center></figcaption>
</figure>


---

##### Bài tập 5.18

Câu hỏi này xem xét việc cắt tỉa trong các trò chơi có node cơ hội. Hình <a class="insideExerciseFigRef" href="#trivial-chance-game-figure">trivial-chance-game-figure</a> hiển thị cây game hoàn chỉnh cho một trò chơi đơn giản. Giả sử các node lá được đánh giá theo thứ tự từ trái sang phải, và trước khi một node lá được đánh giá, chúng ta không biết gì về giá trị của nó—phạm vi các giá trị có thể có là $-\infty$ đến $\infty$.<br>

1.  Sao chép hình, đánh dấu giá trị của tất cả các node nội bộ, và chỉ ra nước đi tốt nhất tại gốc bằng một mũi tên.<br>

2.  Với các giá trị của sáu lá đầu tiên, chúng ta có cần đánh giá lá thứ bảy và thứ tám không? Với các giá trị của bảy lá đầu tiên, chúng ta có cần đánh giá lá thứ tám không? Giải thích câu trả lời của bạn.<br>

3.  Giả sử giá trị của các node lá được biết là nằm trong khoảng từ –2 đến 2 bao gồm. Sau khi hai lá đầu tiên được đánh giá, phạm vi giá trị cho node cơ hội bên trái là gì?<br>

4.  Khoanh tròn tất cả các lá không cần phải đánh giá theo giả định trong (c).<br>


---

##### Bài tập 5.19

Triển khai thuật toán expectiminimax và thuật toán \*-alpha–beta, được mô tả bởi <a class="paperRef" title="" href="">Ballard:1983</a>, để cắt tỉa các cây game có node cơ hội. Hãy thử chúng trên một trò chơi như backgammon và đo lường hiệu quả cắt tỉa của \*-alpha–beta.<br>


---

##### Bài tập 5.20

Chứng minh rằng với một phép biến đổi tuyến tính dương của các giá trị lá (tức là, biến đổi giá trị $x$ thành $ax + b$ với $a > 0$), lựa chọn nước đi không thay đổi trong một cây game, ngay cả khi có các node cơ hội.<br>


---

##### Bài tập 5.21

Xem xét quy trình sau để chọn nước đi trong các trò chơi có node cơ hội:<br>

-   Tạo ra một số chuỗi tung xúc xắc (ví dụ: 50) xuống đến một độ sâu phù hợp (ví dụ: 8).<br>

-   Với các lần tung xúc xắc đã biết, cây game trở nên xác định. Đối với mỗi chuỗi tung xúc xắc, giải cây game xác định kết quả bằng alpha–beta.<br>

-   Sử dụng kết quả để ước tính giá trị của mỗi nước đi và chọn nước đi tốt nhất.<br>

Quy trình này có hoạt động tốt không? Tại sao (hoặc tại sao không)?<br>


---

##### Bài tập 5.22

Trong các phần sau, một cây "max" chỉ bao gồm các max node, trong khi một cây "expectimax" bao gồm một max node ở gốc với các lớp xen kẽ của cơ hội và max node. Tại các node cơ hội, tất cả các xác suất kết quả đều khác không. Mục tiêu là *tìm giá trị của gốc* với tìm kiếm có độ sâu giới hạn. Đối với mỗi mục từ (a) đến (f), hãy đưa ra một ví dụ hoặc giải thích tại sao điều này không thể.<br>

1.  Giả sử các giá trị lá là hữu hạn nhưng không bị chặn, liệu việc cắt tỉa (như trong alpha–beta) có bao giờ có thể xảy ra trong một cây max không?<br>

2.  Liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây expectimax dưới cùng các điều kiện không?<br>

3.  Nếu tất cả các giá trị lá đều không âm, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây max không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

4.  Nếu tất cả các giá trị lá đều không âm, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây expectimax không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

5.  Nếu tất cả các giá trị lá đều nằm trong khoảng $[0,1]$, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây max không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

6.  Nếu tất cả các giá trị lá đều nằm trong khoảng $[0,1]$, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây expectimax không?1<br>

7.  Xem xét các kết quả của một node cơ hội trong cây expectimax. Thứ tự đánh giá nào sau đây có khả năng mang lại cơ hội cắt tỉa nhất?<br>

    i.  Xác suất thấp nhất trước<br>

    ii. Xác suất cao nhất trước<br>

    iii. Không tạo ra sự khác biệt<br>


---

##### Bài tập 5.23

Trong các phần sau, một cây "max" chỉ bao gồm các max node, trong khi một cây "expectimax" bao gồm một max node ở gốc với các lớp xen kẽ của cơ hội và max node. Tại các node cơ hội, tất cả các xác suất kết quả đều khác không. Mục tiêu là *tìm giá trị của gốc* với tìm kiếm có độ sâu giới hạn.<br>

1.  Giả sử các giá trị lá là hữu hạn nhưng không bị chặn, liệu việc cắt tỉa (như trong alpha–beta) có bao giờ có thể xảy ra trong một cây max không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

2.  Liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây expectimax dưới cùng các điều kiện không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

3.  Nếu các giá trị lá bị giới hạn trong khoảng $[0,1]$, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây max không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

4.  Nếu các giá trị lá bị giới hạn trong khoảng $[0,1]$, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây expectimax không? Đưa ra một ví dụ (khác biệt về mặt định tính so với ví dụ của bạn trong (e), nếu có), hoặc giải thích tại sao không.<br>

5.  Nếu các giá trị lá đều không âm, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây max không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

6.  Nếu các giá trị lá đều không âm, liệu việc cắt tỉa có bao giờ có thể xảy ra trong một cây expectimax không? Đưa ra một ví dụ, hoặc giải thích tại sao không.<br>

7.  Xem xét các kết quả của một node cơ hội trong cây expectimax. Thứ tự đánh giá nào sau đây có khả năng mang lại cơ hội cắt tỉa nhất: (i) Xác suất thấp nhất trước; (ii) Xác suất cao nhất trước; (iii) Không tạo ra sự khác biệt?<br>


---

##### Bài tập 5.24

Những phát biểu nào sau đây là đúng và những phát biểu nào là sai? Đưa ra giải thích ngắn gọn.<br>

1.  Trong một trò chơi tổng bằng không (zero-sum), có thể quan sát đầy đủ, theo lượt, giữa hai người chơi hoàn toàn hợp lý, việc biết chiến lược mà người chơi thứ hai đang sử dụng—tức là, người chơi thứ hai sẽ thực hiện nước đi nào, tùy thuộc vào nước đi của người chơi thứ nhất—sẽ không giúp ích gì cho người chơi thứ nhất.<br>

2.  Trong một trò chơi tổng bằng không (zero-sum), có thể quan sát một phần, theo lượt, giữa hai người chơi hoàn toàn hợp lý, việc biết người chơi thứ hai sẽ thực hiện nước đi nào, tùy thuộc vào nước đi của người chơi thứ nhất, sẽ không giúp ích gì cho người chơi thứ nhất.<br>

3.  Một agent backgammon hoàn toàn hợp lý không bao giờ thua.<br>


---

##### Bài tập 5.25

Xem xét cẩn thận sự tương tác của các sự kiện cơ hội và thông tin không đầy đủ trong mỗi trò chơi trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/game-playing-exercises/ex_4/">game-playing-chance-exercise</a>.<br>

1.  Đối với trò chơi nào mô hình expectiminimax tiêu chuẩn là phù hợp? Triển khai thuật toán và chạy nó trong agent chơi game của bạn, với các sửa đổi phù hợp cho môi trường chơi game.<br>

2.  Đối với trò chơi nào, sơ đồ được mô tả trong Bài tập <a href="#ex5.21">game-playing-monte-carlo-exercise</a> sẽ phù hợp?<br>

3.  Thảo luận về cách bạn có thể xử lý thực tế là trong một số trò chơi, người chơi không có cùng kiến thức về state hiện tại.<br>

<!-- tabs:end -->
