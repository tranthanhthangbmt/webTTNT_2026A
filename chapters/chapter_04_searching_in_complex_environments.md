# Chapter 04 Searching In Complex Environments

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_04/chapter_04_vi.html" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_04_Searching%20In%20Complex%20Environments.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter04_4th.pdf" width="100%" height="100%"></iframe>
</div>

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="TaiLieu/slide_4th/Chapter04_4th.pdf" width="100%" height="100%"></iframe>
</div>

#### **Video**

<div class="pdf-container" style="margin-bottom: 20px;">
  <iframe src="video/Chapter04/index.html" width="100%" height="100%"></iframe>
</div>

#### **Trắc nghiệm**
<div id="quiz-container" data-chapter="04"></div>

#### **Pseudocode**
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Hill-Climbing.md" target="_blank">HILL-CLIMBING</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Simulated-Annealing.md" target="_blank">SIMULATED-ANNEALING</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Genetic-Algorithm.md" target="_blank">GENETIC-ALGORITHM</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/And-Or-Graph-Search.md" target="_blank">AND-OR-GRAPH-SEARCH</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/Online-DFS-Agent.md" target="_blank">ONLINE-DFS-AGENT</a>
- <a href="#/codeAndExercises/aima-pseudocode-master/md/LRTAStar-Agent.md" target="_blank">LRTA*-AGENT</a>

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- **Search**: <a href="https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/codeAndExercises/aima-python-master/notebooks/search.ipynb" target="_blank">Mở trên Colab</a> | <a href="codeAndExercises/aima-python-master/notebooks/search.py" download>Tải .py</a> | <a href="codeAndExercises/aima-python-master/notebooks/search.ipynb" download>Tải .ipynb</a>



#### **Bài tập**


##### Bài tập 4.1

Hãy cho biết tên của thuật toán tương ứng với mỗi trường hợp đặc biệt sau đây:<br>

1.  Local beam search với $k = 1$.<br>

2.  Local beam search với một initial state và không giới hạn số lượng các state được giữ lại.<br>

3.  Simulated annealing với $T = 0$ tại mọi thời điểm (và bỏ qua termination test).<br>

4.  Simulated annealing với $T=\infty$ tại mọi thời điểm.<br>

5.  Genetic algorithm với kích thước population $N = 1$.<br>


---

##### Bài tập 4.2

Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_19/">brio-exercise</a> xem xét bài toán xây dựng đường ray xe lửa dưới giả định rằng các mảnh ghép khớp nhau hoàn toàn và không có độ rơ. Bây giờ hãy xem xét bài toán thực tế, trong đó các mảnh ghép không khớp hoàn toàn mà cho phép xoay tối đa 10 độ về mỗi bên so với góc căn chỉnh “chuẩn”. Hãy giải thích cách formulate bài toán này để có thể giải quyết bằng simulated annealing.


---

##### Bài tập 4.3

Trong bài tập này, chúng ta khám phá việc sử dụng các phương pháp local search để giải quyết các bài toán TSP thuộc loại được định nghĩa trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_38/">tsp-mst-exercise</a><br>

1.  Cài đặt và thử nghiệm một phương pháp hill-climbing để giải các bài toán TSP. So sánh kết quả với các optimal solution thu được từ thuật toán A* với MST heuristic (Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_38/">tsp-mst-exercise</a>)<br>

2.  Lặp lại phần (a) bằng cách sử dụng genetic algorithm thay vì hill climbing. Bạn có thể tham khảo @Larranaga+al:1999 để có một số gợi ý về representation.


---

##### Bài tập 4.4

Hãy tạo ra một số lượng lớn các instance của 8-puzzle và 8-queens rồi giải chúng (khi có thể) bằng hill climbing (các biến thể steepest-ascent và first-choice), hill climbing with random restart, và simulated annealing. Đo search cost cùng tỷ lệ phần trăm bài toán giải được, sau đó vẽ biểu đồ biểu diễn các đại lượng này theo optimal solution cost. Hãy đưa ra nhận xét về kết quả của bạn.


---

##### Bài tập 4.5

Thuật toán <b>And-Or-Graph-Search</b> trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/and-or-graph-search-algorithm.png">and-or-graph-search-algorithm</a> chỉ kiểm tra các repeated state trên path từ root đến current state. Giả sử rằng, ngoài ra, thuật toán còn lưu trữ <i>mọi</i> visited state và kiểm tra đối chiếu với danh sách đó. (Xem ví dụ trong Hình <a class="insideBookFigRef" href="#">breadth-first-search-algorithm</a>.) Hãy xác định thông tin cần được lưu trữ và cách thuật toán nên sử dụng thông tin đó khi tìm thấy một repeated state. (*Gợi ý*: Bạn sẽ cần phân biệt ít nhất giữa các state mà trước đó đã xây dựng thành công một subplan và các state không thể tìm thấy subplan nào.) Giải thích cách sử dụng label, như đã định nghĩa trong Mục <a class="sectionRef" title="" href="#">cyclic-plan-section</a>, để tránh việc tạo ra nhiều bản sao của các subplan.


---

##### Bài tập 4.6

Hãy giải thích chính xác cách sửa đổi thuật toán <b>And-Or-Graph-Search</b> để tạo ra một cyclic plan nếu không tồn tại acyclic plan nào. Bạn sẽ cần giải quyết ba vấn đề: gán nhãn cho các bước trong plan để một cyclic plan có thể trỏ ngược lại một phần trước đó của plan, sửa đổi <b>Or-Search</b> để nó tiếp tục tìm kiếm acyclic plan sau khi đã tìm thấy một cyclic plan, và mở rộng plan representation để chỉ ra liệu một plan có phải là cyclic hay không. Hãy chỉ ra cách thuật toán của bạn hoạt động trên (a) slippery vacuum world, và (b) slippery, erratic vacuum world. Bạn có thể muốn sử dụng một chương trình máy tính để kiểm tra kết quả của mình.


---

##### Bài tập 4.7

Trong Mục <a class="sectionRef" title="" href="#">conformant-section</a>, chúng ta đã giới thiệu belief state để giải quyết các bài toán sensorless search. Một chuỗi action sẽ giải quyết được một sensorless problem nếu nó ánh xạ mọi physical state trong initial belief state $b$ sang một goal state. Giả sử agent biết $h^\*(s)$, tức là chi phí tối ưu thực sự để giải quyết physical state $s$ trong fully observable problem, cho mọi state $s$ trong $b$. Hãy tìm một admissible heuristic $h(b)$ cho sensorless problem theo các chi phí này và chứng minh tính admissible của nó. Hãy nhận xét về độ chính xác của heuristic này trên sensorless vacuum problem trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/vacuum2-sets-figure.png">vacuum2-sets-figure</a>. Thuật toán A* hoạt động tốt đến mức nào?


---

##### Bài tập 4.8

Bài tập này khám phá các mối quan hệ tập con–tập cha (subset–superset) giữa các belief state trong sensorless environment hoặc partially observable environment.<br>

1.  Hãy chứng minh rằng nếu một chuỗi action là một solution cho một belief state $b$, thì nó cũng là một solution cho bất kỳ tập con nào của $b$. Có thể rút ra kết luận gì về các tập cha của $b$ hay không?<br>

2.  Hãy giải thích chi tiết cách sửa đổi graph search cho các sensorless problem để tận dụng các câu trả lời của bạn trong phần (a).<br>

3.  Hãy giải thích chi tiết cách sửa đổi and–or search cho các partially observable problem, bên cạnh các sửa đổi mà bạn đã mô tả trong (b).<br>


---

##### Bài tập 4.9

Ở trang <a class="pageRef" title="" href="#">multivalued-sensorless-page</a>, người ta đã giả định rằng một action nhất định sẽ có cùng chi phí khi được thực thi ở bất kỳ physical state nào trong một belief state cho trước. (Điều này dẫn đến một bài toán belief-state search với các step cost được xác định rõ ràng.) Bây giờ hãy xem xét điều gì sẽ xảy ra khi giả định này không còn đúng nữa. Khái niệm về optimality có còn ý nghĩa trong ngữ cảnh này không, hay nó cần phải được sửa đổi? Cũng hãy xem xét các định nghĩa khả dĩ khác nhau về “chi phí” của việc thực thi một action trong một belief state; ví dụ, chúng ta có thể sử dụng giá trị <i>nhỏ nhất (minimum)</i> của các physical cost; hoặc giá trị <i>lớn nhất (maximum)</i>; hoặc một <i>khoảng (interval)</i> chi phí với cận dưới là chi phí nhỏ nhất và cận trên là chi phí lớn nhất; hoặc chỉ cần lưu giữ tập hợp của tất cả các chi phí khả dĩ cho action đó. Đối với mỗi trường hợp này, hãy tìm hiểu xem liệu A* (với các sửa đổi nếu cần) có thể trả về các optimal solution hay không.


---

##### Bài tập 4.10

Xem xét phiên bản sensorless của erratic vacuum world. Hãy vẽ belief-state space có thể đi tới được từ initial belief state $\{1,2,3,4,5,6,7,8\}$, và giải thích tại sao bài toán này không thể giải được (unsolvable).


---

##### Bài tập 4.11

Xem xét phiên bản sensorless của erratic vacuum world. Hãy vẽ belief-state space có thể đi tới được từ initial belief state $\{ 1,3,5,7 \}$, và giải thích tại sao bài toán này không thể giải được (unsolvable).


---

##### Bài tập 4.12

Chúng ta có thể chuyển đổi bài toán điều hướng trong Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/search-exercises/ex_9/">path-planning-exercise</a> thành một environment như sau:<br>

-   Percept sẽ là một danh sách các vị trí của các đỉnh nhìn thấy được, <i>tương đối so với agent</i>. Percept <i>không</i> bao gồm vị trí của robot! Robot phải tự nhận biết vị trí của mình từ bản đồ; hiện tại, bạn có thể giả định rằng mỗi vị trí có một “góc nhìn” khác nhau.<br>

-   Mỗi action sẽ là một vector mô tả một đường thẳng cần đi theo. Nếu đường đi không bị cản trở, action sẽ thành công; nếu không, robot sẽ dừng lại tại điểm mà đường đi của nó cắt vật cản lần đầu tiên. Nếu agent trả về một vector chuyển động bằng 0 và đang ở goal (vốn cố định và đã biết), thì environment sẽ teleport agent đến một <i>vị trí ngẫu nhiên</i> (không nằm bên trong vật cản).<br>

-   Performance measure sẽ tính phí agent 1 điểm cho mỗi đơn vị khoảng cách đi qua và thưởng 1000 điểm mỗi khi đến được goal.<br>

1.  Hãy cài đặt environment này và một problem-solving agent cho nó. Sau mỗi lần teleportation, agent sẽ cần formulate một bài toán mới, bao gồm việc khám phá ra vị trí hiện tại của nó.<br>

2.  Hãy ghi lại performance của agent (bằng cách cho agent tạo ra các lời tường thuật thích hợp khi nó di chuyển xung quanh) và báo cáo performance của nó qua 100 episode.<br>

3.  Sửa đổi environment sao cho có 30% thời gian agent kết thúc tại một điểm đến không mong muốn (được chọn ngẫu nhiên từ các đỉnh nhìn thấy khác nếu có; nếu không, sẽ không di chuyển chút nào). Đây là một mô hình đơn giản về các lỗi chuyển động của một robot thực tế. Sửa đổi agent sao cho khi phát hiện lỗi như vậy, nó sẽ tìm xem mình đang ở đâu và sau đó xây dựng một plan để quay trở lại vị trí cũ và tiếp tục plan ban đầu. Hãy nhớ rằng đôi khi việc quay trở lại vị trí cũ cũng có thể thất bại! Hãy đưa ra một ví dụ về việc agent khắc phục thành công hai lỗi chuyển động liên tiếp mà vẫn đến được goal.<br>

4.  Bây giờ hãy thử hai chiến lược phục hồi (recovery scheme) khác nhau sau lỗi: (1) đi đến đỉnh gần nhất trên lộ trình ban đầu; và (2) replan một lộ trình đến goal từ vị trí mới. So sánh performance của ba chiến lược phục hồi. Liệu việc tính thêm search cost có ảnh hưởng đến sự so sánh này không?<br>

5.  Bây giờ giả sử rằng có những vị trí mà góc nhìn từ đó là giống hệt nhau. (Ví dụ, giả sử thế giới là một lưới với các vật cản hình vuông.) Lúc này agent phải đối mặt với loại bài toán nào? Các solution sẽ trông như thế nào?


---

##### Bài tập 4.13

Giả sử một agent đang ở trong một maze environment kích thước $3 \times 3$ như trong Hình <a class="insideBookFigRef"  target="_blank" href="https://aimacode.github.io/aima-exercises/figures/maze-3x3-figure.png">maze-3x3-figure</a>. Agent biết rằng vị trí ban đầu của nó là (1,1), goal ở (3,3), và các action <i>Up</i>, <i>Down</i>, <i>Left</i>, <i>Right</i> có các tác dụng thông thường trừ khi bị chặn bởi một bức tường. Agent <i>không</i> biết các bức tường bên trong nằm ở đâu. Tại bất kỳ state nào cho trước, agent đều perceive được tập hợp các action hợp lệ; nó cũng có thể nhận biết liệu state đó có phải là state mà nó đã visited trước đây hay không.<br>

1.  Hãy giải thích cách bài toán online search này có thể được xem như một offline search trong belief-state space, trong đó initial belief state bao gồm tất cả các cấu hình environment khả dĩ. Initial belief state lớn đến mức nào? Không gian các belief state lớn đến mức nào?<br>

2.  Có bao nhiêu percept phân biệt khả dĩ trong initial state?<br>

3.  Hãy mô tả một vài nhánh đầu tiên của một contingency plan cho bài toán này. Plan hoàn chỉnh (ước chừng) lớn đến mức nào?<br>

Lưu ý rằng contingency plan này là một solution cho <i>mọi environment khả dĩ</i> phù hợp với mô tả đã cho. Do đó, việc xen kẽ giữa search và execution không hoàn toàn bắt buộc ngay cả trong unknown environment.


---

##### Bài tập 4.14

Giả sử một agent đang ở trong một maze environment kích thước $3 \times 3$ như trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/maze-3x3-figure.png">maze-3x3-figure</a>. Agent biết rằng vị trí ban đầu của nó là (3,3), goal ở (1,1), và bốn action *Up*, *Down*, *Left*, *Right* có các tác dụng thông thường trừ khi bị chặn bởi một bức tường. Agent *không* biết các bức tường bên trong nằm ở đâu. Tại bất kỳ state nào cho trước, agent đều perceive được tập hợp các action hợp lệ; nó cũng có thể nhận biết liệu state đó có phải là state mà nó đã visited trước đây hay là một state mới.<br>

1.  Hãy giải thích cách bài toán online search này có thể được xem như một offline search trong belief-state space, trong đó initial belief state bao gồm tất cả các cấu hình environment khả dĩ. Initial belief state lớn đến mức nào? Không gian các belief state lớn đến mức nào?<br>

2.  Có bao nhiêu percept phân biệt khả dĩ trong initial state?<br>

3.  Hãy mô tả một vài nhánh đầu tiên của một contingency plan cho bài toán này. Plan hoàn chỉnh (ước chừng) lớn đến mức nào?<br>

Lưu ý rằng contingency plan này là một solution cho *mọi environment khả dĩ* phù hợp với mô tả đã cho. Do đó, việc xen kẽ giữa search và execution không hoàn toàn bắt buộc ngay cả trong unknown environment.


---

##### Bài tập 4.15

Trong bài tập này, chúng ta xem xét hill climbing trong ngữ cảnh robot navigation, sử dụng environment trong Hình <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/geometric-scene-figure.png">geometric-scene-figure</a> làm ví dụ.<br>

1.  Lặp lại Bài tập <a class="exerciseRef" href="{{ site.baseurl }}/advanced-search-exercises/ex_11/">path-planning-agent-exercise</a> bằng cách sử dụng hill climbing. Agent của bạn có bao giờ bị mắc kẹt trong một local minimum không? Liệu nó có *thể* bị mắc kẹt với các vật cản lồi (convex obstacle) hay không?<br>

2.  Hãy xây dựng một nonconvex polygonal environment mà trong đó agent bị mắc kẹt.<br>

3.  Sửa đổi thuật toán hill-climbing sao cho thay vì thực hiện một search độ sâu 1 (depth-1 search) để quyết định đi đâu tiếp theo, nó thực hiện một depth-$k$ search. Nó nên tìm path $k$-bước tốt nhất và thực hiện một bước dọc theo path đó, sau đó lặp lại quy trình.<br>

4.  Có tồn tại giá trị $k$ nào mà thuật toán mới đảm bảo sẽ thoát khỏi các local minima hay không?<br>

5.  Hãy giải thích cách LRTA* cho phép agent thoát khỏi các local minima trong trường hợp này.<br>


---

##### Bài tập 4.16

Giống như DFS, online DFS là incomplete đối với các reversible state space có các path vô hạn. Ví dụ, giả sử rằng các state là các điểm trên lưới hai chiều vô hạn và các action là các vector đơn vị $(1,0)$, $(0,1)$, $(-1,0)$, $(0,-1)$, được thử theo thứ tự đó. Hãy chứng minh rằng online DFS bắt đầu tại $(0,0)$ sẽ không bao giờ đến được $(1,-1)$. Giả sử agent có thể quan sát, ngoài current state của nó, tất cả các successor state và các action dẫn đến chúng. Hãy viết một thuật toán complete ngay cả đối với các bidirected state space có các path vô hạn. Thuật toán đó visit những state nào khi đi đến $(1,-1)$?


---

##### Bài tập 4.17

Hãy liên hệ time complexity của LRTA* với space complexity của nó.


---

<!-- tabs:end -->
