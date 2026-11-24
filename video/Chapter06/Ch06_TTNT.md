# CHƯƠNG 5: TÌM KIẾM ĐỐI KHÁNG VÀ TRÒ CHƠI (GAMES & ADVERSARIAL SEARCH)
## TOÀN TẬP LÝ THUYẾT NỀN TẢNG, THUẬT TOÁN VÀ HƯỚNG DẪN GIẢI THÍCH CODE

**Học phần:** Trí tuệ Nhân tạo (Artificial Intelligence)  
**Tài liệu tham khảo chính:** Stuart J. Russell & Peter Norvig - *Artificial Intelligence: A Modern Approach*; Slide bài giảng & Giáo trình Khoa CNTT - Đại học Đông Á.  

---

## Mục 6.1: Trò chơi và Lý thuyết Trò chơi (Game Theory & Formal Formulation)

### 1. Lý thuyết cốt lõi: Phần 6.1. Trò chơi và Lý thuyết trò chơi (Game Theory)

Trong trí tuệ nhân tạo, **tìm kiếm đối kháng (adversarial search)** xuất hiện khi một tác tử phải hành động trong môi trường có các tác tử khác mang mục tiêu xung đột với mình. Thay vì đối mặt với các xung đột phức tạp ngoài đời thực, AI tập trung nghiên cứu các trò chơi trí tuệ (như cờ vua, cờ vây, cờ ca-rô/tic-tac-toe) vì chúng có trạng thái rõ ràng, hữu hạn nước đi và luật chơi hoàn toàn chuẩn xác.

---

#### 1.1. Ba góc nhìn đối với môi trường đa tác tử

Khi thiết kế AI hoạt động trong môi trường có nhiều tác tử, giáo trình đưa ra 3 góc nhìn:

1. **Góc nhìn nền kinh tế (Economy):** Phù hợp khi số lượng tác tử cực kỳ lớn. Ta chỉ cần dự đoán xu hướng chung của đám đông (như giá tăng khi cầu tăng) mà không cần đoán hành động của từng cá nhân.
1. **Xem đối thủ như một phần của môi trường ngẫu nhiên:** Coi đối thủ như thời tiết (mưa hay nắng ngẫu nhiên). Cách này có nhược điểm lớn là bỏ qua sự thật rằng **đối thủ đang chủ động tìm mọi cách để đánh bại ta**.
1. **Mô hình hóa đối kháng trực tiếp (Game-Tree Search):** Phân tích rõ hành động của từng người chơi thông qua **cây trò chơi (game tree)**. Đây chính là trọng tâm của Chương 6.

---

#### 1.2. Trò chơi đối kháng 2 người, tổng bằng không (Two-player zero-sum games)

Phần 6.1.1 tập trung vào lớp trò chơi cơ bản và kinh điển nhất trong AI, mang các đặc điểm:

- **Hai người chơi (Two-player):** Quy ước đặt tên là **MAX** và **MIN**. MAX đi trước, sau đó hai bên luân phiên thay phiên nhau đi. MAX luôn muốn điểm số của mình **lớn nhất** (tối đa hóa điểm), còn MIN luôn muốn điểm số của MAX **nhỏ nhất** (tức điểm của MIN lớn nhất).
- **Tổng bằng không (Zero-sum):** Những gì có lợi cho người này sẽ là bất lợi tương đương cho người kia, không tồn tại kịch bản đôi bên cùng có lợi ("win-win"). Ví dụ: nếu MAX thắng (+1) thì MIN thua (-1); tổng kết quả bằng 0.
- **Tất định & Thông tin hoàn hảo (Deterministic & Perfect information):** Không có yếu tố xúc xắc may rủi, và mọi thông tin trên bàn cờ đều hiển hiện rõ ràng trước mắt cả hai đấu thủ (quan sát toàn phần).

---

#### 1.3. Mô hình toán học hình thức của một trò chơi (Game Formulation)

Để máy tính hiểu và giải quyết một trò chơi, ta chuẩn hóa nó thành một bộ các yếu tố hình thức:

1. $S_0$ **(Initial State):** Trạng thái khởi đầu của bàn cờ (ví dụ: bàn cờ vua lúc chưa đánh, bàn cờ ca-rô trống trơn).
1. $\text{TO-MOVE}(s)$ **:** Cho biết hiện tại đang là lượt đi của ai (MAX hay MIN) tại trạng thái $s$.
1. $\text{ACTIONS}(s)$ **:** Tập hợp các nước đi hợp lệ mà người chơi hiện tại có thể thực hiện từ trạng thái $s$.
1. $\text{RESULT}(s, a)$ **:** Mô hình chuyển trạng thái, trả về bàn cờ mới sau khi thực hiện nước đi $a$ từ bàn cờ $s$.
1. $\text{IS-TERMINAL}(s)$ **:** Hàm kiểm tra xem trò chơi đã kết thúc hay chưa (ai đó thắng, thua hoặc hòa). Các trạng thái kết thúc gọi là **trạng thái đích (terminal states)**.
1. $\text{UTILITY}(s, p)$ **:** Hàm thỏa dụng (payoff function), chấm điểm kết quả cuối cùng cho người chơi $p$ tại trạng thái kết thúc $s$ (ví dụ: với Tic-tac-toe, MAX thắng được $+1$, thua $-1$, hòa $0$ ).

---

#### 1.4. Cây trò chơi (Game Tree)

Từ trạng thái khởi đầu, mỗi nước đi của MAX tạo ra các nhánh con; từ mỗi nhánh đó, các nước đi đáp trả của MIN lại tạo ra các nhánh tiếp theo. Cứ như vậy, toàn bộ diễn biến có thể xảy ra tạo thành một **cây trò chơi**.

- Điểm cuối của cây là các **nút lá (terminal states)**, tại đó ta tính được điểm số cụ thể qua hàm `UTILITY`.
- Ở trò Tic-tac-toe, cây có tối đa $9! = 362{,}880$ nút lá (với 5,478 trạng thái thực tế), đủ nhỏ để máy duyệt hết. Nhưng ở Cờ vua, cây trò chơi có hơn $10^{40}$ nút, buộc AI phải dùng thuật toán cắt tỉa hoặc hàm lượng giá xấp xỉ.

---

### 2. Giải thích chi tiết mã nguồn chương trình (`games.ipynb`)

Trong tài liệu thực hành `games.ipynb` (mã nguồn đi kèm chuẩn của cuốn sách AIMA), mô hình toán học trên được hiện thực hóa bằng ngôn ngữ Python cực kỳ thanh lịch thông qua hai thành phần cốt lõi: **GameState** và lớp **Game**.

#### 2.1. Biểu diễn trạng thái: Cấu trúc `GameState`

Thay vì chỉ lưu bàn cờ thuần túy, tác giả sử dụng `namedtuple` để gói gọn mọi thông tin cần thiết của một trạng thái trò chơi:

```python
GameState = namedtuple('GameState', 'to_move, utility, board, moves')
```

- **to_move**: Lưu ký tự cho biết ai đang đến lượt đi (ví dụ `'X'` hoặc `'O'`). Việc lưu sẵn thông tin này giúp AI không phải đếm lại số quân cờ trên bàn sau mỗi nước.
- **utility**: Lưu sẵn điểm số thỏa dụng của trạng thái (ví dụ $+1$ nếu X thắng, $-1$ nếu O thắng, $0$ nếu hòa/chưa xong). Khi thuật toán đệ quy duyệt cây, việc lưu điểm này giúp tránh việc phải tính đi tính lại nhiều lần.
- **board**: Một dictionary lưu tọa độ và quân cờ đang chiếm giữ (ví dụ `{(1, 1): 'X', (1, 2): 'O'}`).
- **moves**: Danh sách tất cả các nước đi hợp lệ còn lại từ vị trí hiện tại.

---

#### 2.2. Lớp mẫu trừu tượng `Game` (Base Class)

Lớp `Game` đóng vai trò là một "bản thiết kế mẫu" (template interface). Nó ánh xạ chính xác 6 thành phần toán học của Mục 6.1 thành các phương thức (methods):

```python
class Game:
    """Khung sườn định nghĩa một trò chơi đối kháng 2 người."""

    def actions(self, state):
        """Tương ứng ACTIONS(s): Trả về danh sách các nước đi hợp lệ."""
        raise NotImplementedError

    def result(self, state, move):
        """Tương ứng RESULT(s, a): Trả về GameState mới sau khi thực hiện nước đi."""
        raise NotImplementedError

    def utility(self, state, player):
        """Tương ứng UTILITY(s, p): Trả về điểm số cho player tại trạng thái kết thúc."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Tương ứng IS-TERMINAL(s): Trả về True nếu trò chơi đã kết thúc, ngược lại False."""
        return not self.actions(state)

    def to_move(self, state):
        """Tương ứng TO-MOVE(s): Trả về người chơi đang tới lượt."""
        return state.to_move

    def display(self, state):
        """In bàn cờ trực quan ra màn hình terminal."""
        print(state)
```

**Tại sao lớp** **Game** **lại viết như vậy?**

- Đây là thiết kế **hướng đối tượng**: Bất kỳ trò chơi nào (Tic-tac-toe, Cờ vua, Connect-4) chỉ cần kế thừa lớp `Game` và viết đè lại các hàm này là các thuật toán thông minh như Minimax hay Cắt tỉa Alpha-Beta đều có thể chạy được ngay mà không cần sửa đổi thuật toán.

---

#### 2.3. Cài đặt trò chơi cụ thể: Lớp `TicTacToe` kế thừa từ `Game`

Để thấy rõ cách hoạt động, `games.ipynb` xây dựng lớp `TicTacToe(Game)`:

```python
class TicTacToe(Game):
    def __init__(self, h=3, v=3, k=3):
        # h: số hàng (3), v: số cột (3), k: số quân liên tiếp để thắng (3)
        self.h = h
        self.v = v
        self.k = k
        # Tập hợp tất cả các ô trống ban đầu: (1,1) đến (3,3)
        moves = [(x, y) for x in range(1, h + 1)
                        for y in range(1, v + 1)]
        # Khởi tạo trạng thái ban đầu S0: 'X' đi trước, điểm = 0, bàn cờ rỗng
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

    def actions(self, state):
        # Nước đi hợp lệ chính là các ô còn trống chưa bị đánh
        return state.moves

    def result(self, state, move):
        # Nếu nước đi không hợp lệ, giữ nguyên trạng thái
        if move not in state.moves:
            return state
        # Tạo bản sao bàn cờ mới và đánh dấu quân cờ của người hiện tại
        board = state.board.copy()
        board[move] = state.to_move
        # Cập nhật danh sách các ô trống còn lại
        moves = list(state.moves)
        moves.remove(move)
        # Chuyển lượt đi: nếu vừa là 'X' thì tiếp theo là 'O', và ngược lại
        next_to_move = 'O' if state.to_move == 'X' else 'X'
        # Tính toán xem nước đi này đã phân định thắng thua chưa
        utility = self.compute_utility(board, move, state.to_move)
        return GameState(to_move=next_to_move, utility=utility, board=board, moves=moves)

    def utility(self, state, player):
        # Trả về điểm theo góc nhìn của người chơi được truyền vào
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        # Kết thúc khi đã có người thắng (utility != 0) hoặc hết ô trống (không còn moves)
        return state.utility != 0 or len(state.moves) == 0
```

---

#### 2.4. Cách hệ thống vận hành khi chơi một trận đấu (`play_game`)

Khi ta cho 2 tác tử đối đầu (chẳng hạn người đấu với máy hoặc AI đấu với AI), vòng lặp `play_game` vận hành vô cùng ngắn gọn:

1. Bắt đầu từ trạng thái `state = game.initial`.
1. Lấy người chơi hiện tại bằng `game.to_move(state)`.
1. Người chơi đó chọn ra nước đi `move` (ví dụ: máy dùng hàm `alpha_beta_search` để tính nước tối ưu).
1. Bàn cờ chuyển sang trạng thái mới qua `state = game.result(state, move)`.
1. Kiểm tra `game.terminal_test(state)`. Nếu xong thì dừng và xuất kết quả `game.utility(state, player)`; nếu chưa xong thì quay lại bước 2.

---

## Mục 6.2: Quyết định Tối ưu và Thuật toán Minimax (Optimal Decisions in Games & Minimax Algorithm)

### 1. Lý thuyết cốt lõi: Phần 6.2. Quyết định tối ưu và Thuật toán Minimax

Ở Mục 6.1, ta đã biết trò chơi đối kháng 2 người tổng bằng 0 có hai bên: **MAX** (muốn tối đa hóa điểm số) và **MIN** (muốn giảm thiểu điểm số của MAX xuống mức thấp nhất). Mục 6.2 trả lời cho câu hỏi: **Làm thế nào để MAX đưa ra được quyết định (nước đi) tối ưu nhất khi đối thủ MIN cũng chơi một cách hoàn hảo?**

---

#### 1.1. Giá trị Minimax (Minimax Value) là gì?

Trong môi trường tìm kiếm thông thường (như tìm đường đi), tác tử chỉ việc tìm chuỗi hành động dẫn tới đích. Nhưng trong trò chơi, MAX vừa đi một nước thì MIN sẽ đáp trả. Vì vậy, một chiến lược tối ưu phải tính toán trước phản ứng của MIN.

**Giá trị Minimax của một trạng thái** $s$ (ký hiệu là $\text{MINIMAX}(s)$ ) là điểm thỏa dụng (utility) mà MAX sẽ đạt được khi đứng ở trạng thái $s$, **giả định rằng cả hai đấu thủ đều chơi tối ưu từ trạng thái đó cho đến hết ván cờ**.

Công thức toán học của giá trị Minimax được định nghĩa đệ quy như sau:

\[\text{MINIMAX}(s) = \begin{cases} \text{UTILITY}(s, \text{MAX}) & \text{nếu } \text{IS-TERMINAL}(s) \ \max_{a \in \text{ACTIONS}(s)} \text{MINIMAX}(\text{RESULT}(s, a)) & \text{nếu } \text{TO-MOVE}(s) = \text{MAX} \ \min_{a \in \text{ACTIONS}(s)} \text{MINIMAX}(\text{RESULT}(s, a)) & \text{nếu } \text{TO-MOVE}(s) = \text{MIN} \end{cases}\]

- **Tại nút lá (kết thúc):** Giá trị Minimax chính là điểm số thực tế của ván đấu qua hàm `UTILITY`.
- **Tại lượt của MAX:** MAX có quyền chọn nước đi, nên MAX sẽ chọn nhánh con có giá trị **lớn nhất** (dùng hàm $\max$ ).
- **Tại lượt của MIN:** MIN là đối thủ, luôn tìm cách dìm điểm của MAX xuống, nên MIN sẽ chọn nhánh con có giá trị **nhỏ nhất** (dùng hàm $\min$ ).

---

#### 1.2. Ví dụ trực quan trên Cây trò chơi 2 tầng (Hình 6.2 trong sách)

Giả sử MAX đang ở gốc $A$ và có 3 nước đi: $a_1, a_2, a_3$ dẫn tới các trạng thái $B, C, D$. Tại $B, C, D$ là lượt của MIN:

1. **Duyệt nhánh con dưới** $B$ **:** MIN có 3 lựa chọn dẫn đến các kết quả cuối cùng có điểm là $3, 12, 8$. Vì MIN muốn điểm thấp nhất, MIN sẽ chọn $3$. Do đó, **giá trị của** $B = \min(3, 12, 8) = 3$.
1. **Duyệt nhánh con dưới** $C$ **:** Các nút lá có điểm là $2, 4, 6$. MIN sẽ chọn $2$. Do đó, **giá trị của** $C = \min(2, 4, 6) = 2$.
1. **Duyệt nhánh con dưới** $D$ **:** Các nút lá có điểm là $14, 5, 2$. MIN sẽ chọn $2$. Do đó, **giá trị của** $D = \min(14, 5, 2) = 2$.
1. **Trở lại nút gốc** $A$ **(lượt của MAX):** MAX so sánh các kết quả mà MIN sẽ để lại cho mình: đi $a_1$ thì được $3$, đi $a_2$ thì được $2$, đi $a_3$ thì được $2$. Vì MAX muốn điểm cao nhất: 

$$
\text{Giá trị của } A = \max(3, 2, 2) = 3
$$

 👉 **Quyết định Minimax (Minimax Decision):** MAX quyết định chọn hành động $a_1$.

---

#### 1.3. Độ phức tạp của thuật toán

- **Thuật toán duyệt:** Minimax thực hiện duyệt theo chiều sâu ( **Depth-First Search - DFS** ) toàn bộ cây trò chơi.
- **Độ phức tạp thời gian:** $O(b^m)$ với $b$ là hệ số phân nhánh (số nước đi hợp lệ ở mỗi lượt) và $m$ là độ sâu tối đa của cây.
- **Độ phức tạp không gian (bộ nhớ):** $O(bm)$ nếu ta sinh toàn bộ danh sách hành động một lần, hoặc $O(m)$ nếu chỉ sinh từng hành động một.
- **Hạn chế:** Với các trò chơi lớn như Cờ vua ( $b \approx 35, m \approx 80$ ), cây có tới hơn $35^{80} \approx 10^{123}$ trạng thái, Minimax duyệt hết cây là bất khả thi. Điều này dẫn tới nhu cầu cần kỹ thuật **Cắt tỉa Alpha-Beta** hoặc **Hàm lượng giá Heuristic**.

---

### 2. Giải thích chi tiết mã nguồn chương trình (`games.ipynb`)

Trong tài liệu thực hành `games.ipynb`, thuật toán Minimax được triển khai thông qua đệ quy tương hỗ (mutual recursion) giữa hai hàm `max_value` và `min_value`.

#### 2.1. Mã giả chuẩn (Pseudocode) và Bản chất đệ quy

Thuật toán chia thành 3 hàm phối hợp nhịp nhàng với nhau:

```python
def minimax_decision(state, game):
    """
    Hàm khởi đầu: Trả về hành động (action) tốt nhất cho người chơi hiện tại.
    """
    player = game.to_move(state)

    def max_value(state):
        # 1. Điểm dừng đệ quy: nếu ván cờ đã kết thúc, trả về điểm số thực tế
        if game.terminal_test(state):
            return game.utility(state, player)
        
        # 2. Khởi tạo điểm số tệ nhất cho MAX (-vô cực)
        v = -float('inf')
        
        # 3. Duyệt qua tất cả các nước đi hợp lệ
        for a in game.actions(state):
            # Sau khi MAX đi nước 'a', lượt chuyển sang MIN -> gọi min_value
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        # 1. Điểm dừng đệ quy: nếu ván cờ đã kết thúc
        if game.terminal_test(state):
            return game.utility(state, player)
        
        # 2. Khởi tạo điểm số tệ nhất cho MIN (+vô cực)
        v = float('inf')
        
        # 3. Duyệt qua tất cả các nước đi hợp lệ của MIN
        for a in game.actions(state):
            # Sau khi MIN đi nước 'a', lượt trả về cho MAX -> gọi max_value
            v = min(v, max_value(game.result(state, a)))
        return v

    # Tại trạng thái gốc, MAX sẽ chọn hành động 'a' nào đem lại min_value lớn nhất
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))
```

---

#### 2.2. Giải thích từng dòng code thật dễ hiểu

1. **game.terminal_test(state)** **(Điều kiện dừng đệ quy):**
  - Giống như việc nhìn xuống đáy bàn cờ. Nếu có người thắng/thua hoặc bàn cờ đã kín ô, không đệ quy sâu hơn nữa mà lập tức gọi `game.utility(state, player)` để lấy điểm số ( $+1, -1, 0$ ).
1. **Khởi tạo** **v = -inf** **ở MAX và** **v = +inf** **ở MIN:**
  - MAX muốn tìm giá trị cao nhất, nên khởi điểm lấy giá trị nhỏ nhất có thể ( $-\infty$ ) để bất kỳ nước đi nào tốt hơn cũng sẽ được cập nhật.
  - Ngược lại, MIN muốn tìm giá trị nhỏ nhất, nên khởi điểm lấy giá trị lớn nhất ( $+\infty$ ).
1. **Vòng lặp đệ quy đan xen (** **min_value** **gọi** **max_value** **,** **max_value** **gọi** **min_value** **):**
  - Khi MAX thử đi một nước $a$, trạng thái mới chuyển thành `game.result(state, a)`. MAX tự hỏi: *"Nếu mình đi nước này, đối thủ MIN sẽ đáp trả làm mình còn bao nhiêu điểm?"* $\rightarrow$ Lập tức gọi `min_value(...)`.
  - Khi MIN phân tích, MIN lại tự hỏi: *"Nếu mình đi nước này, MAX sẽ phản công thế nào?"* $\rightarrow$ Gọi ngược lại `max_value(...)`.
  - Hai hàm cứ thế "bóng bàn" qua lại cho đến khi chạm nút lá (kết thúc game), rồi các giá trị được thu gom ngược lên trên (gọi là **backed-up values** ).
1. **Dòng lệnh chọn hành động ở gốc:** **max(actions, key=lambda a:...)** **:**
  - Thay vì chỉ trả về con số điểm, ở tầng gốc, tác tử AI cần biết **cụ thể là nước đi nào**. Hàm `max(..., key=...)` sẽ so sánh tất cả các hành động $a$ khả dĩ và bốc ra đúng nước đi mang lại điểm số cao nhất.

---

#### 2.3. Minh họa chạy thử trong `games.ipynb` với trò chơi Fig52Game

Trong file notebook, tác giả kiểm tra thuật toán trên trò chơi minh họa `Fig52Game` (mô phỏng chính xác Hình 6.2 của sách):

```python
fig52 = Fig52Game()

# Hỏi MIN sẽ đi nước nào nếu đứng tại B, C, D:
print(minmax_decision('B', fig52)) # Trả về: 'b1' (vì b1 có điểm 3, nhỏ nhất trong 3, 12, 8)
print(minmax_decision('C', fig52)) # Trả về: 'c1' (vì c1 có điểm 2, nhỏ nhất trong 2, 4, 6)
print(minmax_decision('D', fig52)) # Trả về: 'd3' (vì d3 có điểm 2, nhỏ nhất trong 14, 5, 2)

# MAX đứng tại đỉnh A sẽ đi nước nào?
print(minmax_decision('A', fig52)) # Trả về: 'a1' (dẫn tới B có giá trị 3, lớn hơn C và D đều là 2)
```

Kết quả in ra `'a1'` chứng minh thuật toán Minimax đã tính toán chính xác nước đi đem lại kết quả tốt nhất cho MAX trong kịch bản đối thủ đáp trả hoàn hảo.

---

## Mục 6.3: Cắt tỉa Alpha–Beta (Alpha–Beta Pruning & Optimization)

### 1. Lý thuyết cốt lõi: Phần 6.3. Cắt tỉa Alpha–Beta (Alpha–Beta Pruning)

Ở phần 6.2, ta đã thấy thuật toán **Minimax** phải duyệt toàn bộ cây trò chơi theo chiều sâu. Với hệ số phân nhánh là $b$ và độ sâu là $m$, số lượng trạng thái cần duyệt lên đến $O(b^m)$. Đây là một con số khổng lồ (ví dụ cờ vua có hơn $10^{40}$ nút) khiến máy tính không thể duyệt hết.

**Cắt tỉa Alpha–Beta (Alpha–Beta Pruning)** ra đời nhằm giải quyết vấn đề này: nó loại bỏ các nhánh cây trò chơi chắc chắn không ảnh hưởng đến quyết định tối ưu cuối cùng. Kết quả tính ra hoàn toàn **chính xác 100% như Minimax**, nhưng bỏ qua được các tính toán dư thừa.

---

#### 1.1. Ý nghĩa trực quan của hai tham số $\alpha$ và $\beta$

Thuật toán duy trì hai cận giá trị xuyên suốt đường đi tìm kiếm:

- $\alpha$ **(Alpha):** Điểm số **tốt nhất (lớn nhất)** mà người chơi **MAX** chắc chắn đã đạt được tại bất kỳ điểm lựa chọn nào từ trước tới nay dọc theo đường đi.
  - *Tư duy:* MAX tự nhủ: *"Tôi đã có trong tay phương án chắc chắn đạt ít nhất là* $\alpha$ *điểm"*.
- $\beta$ **(Beta):** Điểm số **tốt nhất (nhỏ nhất)** mà đối thủ **MIN** chắc chắn đã ghìm được MAX xuống tại bất kỳ điểm lựa chọn nào dọc theo đường đi.
  - *Tư duy:* MIN tự nhủ: *"Tôi đã có trong tay phương án ghìm MAX xuống nhiều nhất chỉ được* $\beta$ *điểm"*.

Ban đầu ở gốc cây, ta chưa biết gì nên khởi tạo: 

$$
\alpha = -\infty, \quad \beta = +\infty
$$

---

#### 1.2. Nguyên lý cắt tỉa: Khi nào ta được quyền "bỏ qua"?

Thuật toán duyệt cây theo chiều sâu (DFS). Khi đánh giá một trạng thái có giá trị hiện tại là $v$:

1. **Tại nút của MIN (Cắt nhánh** $\alpha$ **- Alpha Cutoff):**
  - MIN chọn giá trị nhỏ nhất, nên cập nhật $\beta = \min(\beta, v)$.
  - Nếu phát hiện một nhánh con có giá trị $v \le \alpha$: **DỪNG LẠI NGAY LẬP TỨC!**
  - *Giải thích đời thực:* MAX ở phía trên đã có sẵn một lựa chọn đem lại $\alpha$ điểm. Ở nhánh hiện tại, MIN đã tìm ra cách ghìm MAX xuống còn $v$ (mà $v \le \alpha$ ). Vậy thì MAX sẽ **không bao giờ chọn đi vào nhánh này nữa**. Các nhánh con còn lại dưới chân MIN dù có bằng bao nhiêu đi chăng nữa cũng vô nghĩa $\rightarrow$ Cắt bỏ!
1. **Tại nút của MAX (Cắt nhánh** $\beta$ **- Beta Cutoff):**
  - MAX chọn giá trị lớn nhất, nên cập nhật $\alpha = \max(\alpha, v)$.
  - Nếu phát hiện một nhánh con có giá trị $v \ge \beta$: **DỪNG LẠI NGAY LẬP TỨC!**
  - *Giải thích đời thực:* MIN ở phía trên đã có một lựa chọn ghìm điểm MAX xuống mức $\beta$. Ở nhánh hiện tại, MAX lại tìm ra nước đi được tận $v \ge \beta$. MIN đang ở trên nhìn thấy điều đó sẽ **không bao giờ cho phép thế cờ rơi vào nhánh này**. Vì vậy, việc tìm tiếp dưới nhánh này là lãng phí $\rightarrow$ Cắt bỏ!

---

#### 1.3. Ví dụ minh họa từng bước trên Hình 6.5 (Fig52Game)

Xét cây trò chơi với gốc $A$ (MAX), 3 nhánh con là $B, C, D$ (MIN):

1. **Duyệt cây con dưới** $B$ **:** Các lá có điểm là $3, 12, 8$.
  - Nút $B$ chọn giá trị nhỏ nhất $\rightarrow$ Giá trị của $B = 3$.
  - Quay lại gốc $A$ (MAX): Cập nhật $\alpha = \max(-\infty, 3) = 3$.
1. **Duyệt cây con dưới** $C$ **:**
  - Lá đầu tiên dưới $C$ có giá trị là $2$.
  - Lúc này giá trị của $C$ sẽ nhiều nhất là $2$ (vì $C$ là nút MIN, $v \le 2$ ).
  - So sánh điều kiện: $v = 2 \le \alpha = 3$ $\rightarrow$ **Thỏa mãn điều kiện cắt nhánh** $\alpha$!
  - Ta lập tức cắt tỉa 2 nút lá còn lại dưới $C$ mà không cần tính toán.
1. **Hiệu quả:** Trong trường hợp lý tưởng nhất (nước đi tốt nhất được xét trước), số trạng thái cần duyệt giảm từ $O(b^m)$ xuống chỉ còn $O(b^{m/2})$. Điều này tương đương với việc **hệ số phân nhánh hiệu dụng giảm từ** $b$ **xuống còn** $\sqrt{b}$ (ví dụ ở cờ vua từ 35 giảm xuống khoảng 6), giúp AI tính toán sâu gấp đôi trong cùng một khoảng thời gian.

---

### 2. Giải thích chi tiết mã nguồn chương trình (`games.ipynb`)

Trong tài liệu thực hành `games.ipynb`, thuật toán được cài đặt trực tiếp qua hàm `alpha_beta_search`. Dưới đây là mã nguồn chuẩn hóa dễ hiểu nhất:

```python
def alpha_beta_search(state, game):
    """
    Tìm nước đi tối ưu cho người chơi hiện tại bằng thuật toán Alpha-Beta.
    """
    player = game.to_move(state)

    # -------------------------------------------------------------
    # Hàm tính giá trị cho lượt của MAX
    # -------------------------------------------------------------
    def max_value(state, alpha, beta):
        # 1. Điểm dừng: nếu ván đấu kết thúc, trả về điểm số thực tế
        if game.terminal_test(state):
            return game.utility(state, player)

        v = -float('inf')
        # 2. Duyệt qua từng nước đi hợp lệ của MAX
        for a in game.actions(state):
            # Đi thử nước 'a' -> chuyển lượt sang MIN tính tiếp
            v = max(v, min_value(game.result(state, a), alpha, beta))
            
            # CẮT TỈA BETA (Beta cutoff):
            # Nếu điểm v tìm được đã vượt quá hoặc bằng beta của MIN ở tầng trên,
            # MIN chắc chắn sẽ chặn nhánh này -> Ngừng xét các hành động còn lại!
            if v >= beta:
                return v
            
            # Cập nhật mốc an toàn mới cho MAX
            alpha = max(alpha, v)
        return v

    # -------------------------------------------------------------
    # Hàm tính giá trị cho lượt của MIN
    # -------------------------------------------------------------
    def min_value(state, alpha, beta):
        # 1. Điểm dừng: nếu ván đấu kết thúc
        if game.terminal_test(state):
            return game.utility(state, player)

        v = float('inf')
        # 2. Duyệt qua từng nước đi hợp lệ của đối thủ MIN
        for a in game.actions(state):
            # MIN đi thử nước 'a' -> chuyển lượt sang MAX tính tiếp
            v = min(v, max_value(game.result(state, a), alpha, beta))
            
            # CẮT TỈA ALPHA (Alpha cutoff):
            # Nếu điểm v bị MIN ghìm xuống <= alpha mà MAX đã nắm giữ trước đó,
            # MAX ở tầng trên sẽ không bao giờ chọn vào đây -> Ngừng xét tiếp!
            if v <= alpha:
                return v
            
            # Cập nhật mốc ghìm điểm mới cho MIN
            beta = min(beta, v)
        return v

    # -------------------------------------------------------------
    # Khởi động tại nút GỐC (Root - lượt của MAX)
    # -------------------------------------------------------------
    best_score = -float('inf')
    best_action = None
    alpha = -float('inf')
    beta = float('inf')

    for a in game.actions(state):
        # Với mỗi nước đi ban đầu, gọi MIN đáp trả
        v = min_value(game.result(state, a), alpha, beta)
        if v > best_score:
            best_score = v
            best_action = a
        alpha = max(alpha, best_score)

    return best_action
```

---

#### 2.1. Phân tích chi tiết từng khối code

1. **Khởi tạo dải chặn ban đầu (** **alpha = -inf** **,** **beta = +inf** **)** **:**
  - Thể hiện rằng ở đầu trận, MAX chưa có điểm số tối thiểu nào đảm bảo ( $-\infty$ ), và MIN cũng chưa có giới hạn trần nào ( $+\infty$ ).
1. **Khối lệnh cắt tỉa trong** **min_value** **:**

```python
if v <= alpha:
    return v
```

- Biến `v` là giá trị nhỏ nhất mà MIN vừa tìm được.
- Nếu giá trị này thấp hơn hoặc bằng `alpha` (mức tốt nhất mà MAX đã tìm ra ở nhánh khác), câu lệnh `return v` được kích hoạt ngay lập tức. Vòng lặp `for a in game.actions(state)` bị bẻ gãy, **toàn bộ các nhánh còn lại của nút đó không bao giờ được sinh ra hay duyệt đến**.
1. **Khối lệnh cắt tỉa trong** **max_value** **:**

```python
if v >= beta:
    return v
```

- Ngược lại, nếu MAX thấy một nước đi đạt `v >= beta`, MAX trả về ngay vì biết rằng đối thủ MIN ở tầng trên sẽ lập tức tránh nước đi dẫn vào nhánh này.
1. **Cập nhật động theo thời gian thực:**
  - Sau mỗi lần duyệt một nhánh con mà không bị cắt tỉa, `alpha` (trong `max_value`) hoặc `beta` (trong `min_value`) sẽ được thu hẹp lại dần dần. Càng vào sâu và tìm được các nước đi sắc bén sớm, khoảng cách giữa `[alpha, beta]` càng hẹp, giúp các nhánh sau bị cắt tỉa càng nhanh.

---

#### 2.2. Kiểm chứng trong thực tế với `games.ipynb`

Trong notebook, khi cho tác tử thông minh `alphabeta_player` thi đấu với nhau trong cờ ca-rô `TicTacToe`:

```python
ttt = TicTacToe()
ttt.play_game(alpha_beta_player, alpha_beta_player)
```

Kết quả của trận đấu giữa hai tác tử dùng thuật toán Alpha–Beta luôn luôn kết thúc với tỷ số **hòa (0)**. Điều này chứng minh thuật toán cắt tỉa Alpha–Beta không chỉ chạy nhanh hơn mà còn giữ trọn vẹn khả năng tìm ra chiến lược đối kháng hoàn hảo của Minimax.

---

## Mục 6.4: Quyết định Thời gian thực Không hoàn hảo (Heuristic Minimax & Evaluation Functions)

### 1. Lý thuyết cốt lõi: Phần 6.4 (hoặc 6.3 trong bản 4th). Quyết định thời gian thực không hoàn hảo (Imperfect Real-Time Decisions)

Trong các phần trước, thuật toán **Minimax** và **Cắt tỉa Alpha-Beta** chỉ tìm được nước cờ khi duyệt đến tận **nút lá (terminal states - trạng thái kết thúc ván cờ)**. Tuy nhiên, trong các trò chơi thực tế có giới hạn thời gian (như cờ vua với quy định mỗi nước đi chỉ có vài phút):

- Cây trò chơi cờ vua có khoảng $10^{40}$ đến $10^{120}$ trạng thái.
- Ngay cả khi có thuật toán Alpha-Beta tối ưu hóa, máy tính thông thường cũng chỉ tính trước được khoảng 10–14 nước (ply) trong thời gian cho phép.

Vì vậy, chương trình **bắt buộc phải đưa ra quyết định mà không thể đợi duyệt hết ván cờ**. Đây gọi là **quyết định thời gian thực không hoàn hảo (imperfect real-time decisions)**.

---

#### 1.1. Công thức chuyển đổi: Heuristic Minimax

Để giải quyết bài toán thời gian thực, Russell & Norvig thay thế hai thành phần chính của thuật toán gốc:

1. **Hàm kết thúc** **IS-TERMINAL(s)** $\rightarrow$ **Hàm cắt tỉa sớm** **IS-CUTOFF(s, d)** **:**
  - Thay vì chỉ dừng lại khi ván cờ kết thúc (thắng/thua/hòa), hàm này sẽ trả về `True` nếu đã đạt tới một độ sâu giới hạn $d$ hoặc khi hết thời gian cho phép.
1. **Hàm điểm số thật** **UTILITY(s)** $\rightarrow$ **Hàm lượng giá ước tính** **EVAL(s)** **:**
  - Vì ván cờ chưa kết thúc nên ta không có điểm thực tế (+1, -1). Ta phải dùng một hàm Heuristic **EVAL(s)** để "đoán" xem ở vị trí bàn cờ hiện tại, ai đang chiếm ưu thế hơn.

Công thức tổng quát $\text{H-MINIMAX}(s, d)$: \[\text{H-MINIMAX}(s, d) = \begin{cases} \text{EVAL}(s, \text{MAX}) & \text{nếu } \text{IS-CUTOFF}(s, d) \ \max_{a} \text{H-MINIMAX}(\text{RESULT}(s, a), d+1) & \text{nếu } \text{TO-MOVE}(s) = \text{MAX} \ \min_{a} \text{H-MINIMAX}(\text{RESULT}(s, a), d+1) & \text{nếu } \text{TO-MOVE}(s) = \text{MIN} \end{cases}\]

---

#### 1.2. Hàm lượng giá Heuristic (`EVAL`) được xây dựng như thế nào?

Một hàm đánh giá tốt cần tính toán rất nhanh và phản ánh chính xác cơ hội thắng. Thông thường, người ta sử dụng **tổng tuyến tính có trọng số (Weighted Linear Combination)** của các đặc trưng trên bàn cờ:

$$
\text{EVAL}(s) = w_1 f_1(s) + w_2 f_2(s) + \dots + w_n f_n(s) = \sum_{i=1}^n w_i f_i(s)
$$

- **Ví dụ trong cờ vua:**
  - Các đặc trưng $f_i$: Số quân Tốt, Mã, Tượng, Xe, Hậu của mỗi bên.
  - Trọng số tương ứng $w_i$: Tốt = 1 điểm, Mã = 3 điểm, Tượng = 3 điểm, Xe = 5 điểm, Hậu = 9 điểm.
  - Ngoài ra còn tính đến các yếu tố chiến thuật: an toàn của vua, quyền kiểm soát trung tâm bàn cờ, tính cơ động (số nước đi hợp lệ).

---

#### 1.3. Hai cạm bẫy kinh điển và cách khắc phục

Khi cắt ngắn độ sâu tìm kiếm, AI rất dễ mắc phải hai lỗi lớn:

1. **Vấn đề tĩnh lặng (Quiescence) & Tìm kiếm tĩnh lặng (Quiescence Search):**
  - *Nguy cơ:* Giả sử máy cắt độ sâu đúng lúc quân Trắng vừa ăn quân Mã của Đen. Nhìn bề ngoài thì Trắng đang hơn điểm. Nhưng ngay nước tiếp theo, Đen sẽ dùng Hậu bắt lại Xe của Trắng. Vị trí này gọi là **không tĩnh lặng (nonquiescent)** vì đang có giao tranh lớn.
  - *Giải pháp:* Tại điểm cắt độ sâu, nếu bàn cờ chưa "yên bình" (còn nước ăn quân, chiếu tướng), AI không được dừng lại mà phải tìm sâu thêm vài nước nữa chỉ tập trung vào các nước ăn quân ( **quiescence search** ) cho tới khi thế cờ thực sự ổn định.
1. **Hiệu ứng chân trời (Horizon Effect):**
  - *Nguy cơ:* Khi một đòn sát thương của đối thủ là **không thể tránh khỏi** (ví dụ sắp mất quân Xe), AI cố tình thực hiện các nước chiếu vô nghĩa bằng các quân Tốt để đẩy thời điểm mất Xe vượt qua "đường chân trời" (độ sâu tối đa mà máy nhìn thấy). Lúc này, máy tưởng rằng mình đã cứu được Xe, nhưng thực chất chỉ đang ném thêm các quân cờ khác vào chỗ chết.

---

### 2. Giải thích chi tiết mã nguồn chương trình (`games.ipynb` / `games.py`)

Trong thư viện mã nguồn đi kèm của giáo trình, thuật toán này được hiện thực hóa qua hàm **alpha_beta_cutoff_search**. Thuật toán kết hợp cả kỹ thuật cắt tỉa Alpha-Beta và cắt giới hạn độ sâu.

#### 2.1. Mã nguồn Python chi tiết có chú thích

```python
def alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """
    Tìm nước đi bằng Alpha-Beta kết hợp cắt tỉa độ sâu 'd' và hàm đánh giá 'eval_fn'.
    """
    player = game.to_move(state)

    # 1. Định nghĩa điều kiện cắt tỉa (cutoff_test):
    # Nếu không truyền vào, mặc định dừng khi:
    # - Ván đấu kết thúc tự nhiên (terminal_test), HOẶC
    # - Độ sâu tìm kiếm đạt mốc giới hạn 'd'
    cutoff_test = cutoff_test or (lambda state, depth: depth > d or game.terminal_test(state))
    
    # 2. Định nghĩa hàm lượng giá Heuristic (eval_fn):
    # Nếu không truyền vào, mặc định dùng hàm utility của game
    eval_fn = eval_fn or (lambda state: game.utility(state, player))

    # ---------------------------------------------------------
    # Hàm MAX-VALUE có thêm tham số depth (độ sâu hiện tại)
    # ---------------------------------------------------------
    def max_value(state, alpha, beta, depth):
        # Kiểm tra xem đã đến lúc DỪNG chưa (chạm đáy độ sâu hoặc game over)
        if cutoff_test(state, depth):
            return eval_fn(state)  # Dùng hàm lượng giá Heuristic để chấm điểm

        v = -float('inf')
        for a in game.actions(state):
            # Đi thử nước 'a', tăng độ sâu lên 1 (depth + 1)
            v = max(v, min_value(game.result(state, a), alpha, beta, depth + 1))
            
            # Cắt tỉa nhánh Beta
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    # ---------------------------------------------------------
    # Hàm MIN-VALUE có thêm tham số depth
    # ---------------------------------------------------------
    def min_value(state, alpha, beta, depth):
        # Kiểm tra xem đã đến lúc DỪNG chưa
        if cutoff_test(state, depth):
            return eval_fn(state)

        v = float('inf')
        for a in game.actions(state):
            # Chuyển tiếp lượt sang MAX, tăng độ sâu lên 1
            v = min(v, max_value(game.result(state, a), alpha, beta, depth + 1))
            
            # Cắt tỉa nhánh Alpha
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # ---------------------------------------------------------
    # Tại nút gốc (depth = 0): Chọn ra nước đi mang lại điểm số cao nhất
    # ---------------------------------------------------------
    best_score = -float('inf')
    best_action = None
    alpha = -float('inf')
    beta = float('inf')

    for a in game.actions(state):
        # Thử từng nước đi với depth bắt đầu từ 1
        v = min_value(game.result(state, a), alpha, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
        alpha = max(alpha, best_score)

    return best_action
```

---

#### 2.2. Giải thích các điểm quan trọng trong code

1. **Tham số** **depth** **và cơ chế đếm tầng:**
  - Tại trạng thái gốc bàn cờ, `depth = 0`. Mỗi khi gọi đệ quy sang lượt của đối phương, ta truyền `depth + 1`.
1. **cutoff_test(state, depth)** **linh hoạt:**
  - Thay vì chỉ kiểm tra cứng nhắc `game.terminal_test(state)`, hàm kiểm tra xem `depth > d` hay chưa. Nhờ tham số này, lập trình viên có thể tùy biến điều kiện dừng tinh vi hơn (chẳng hạn: kiểm tra thời gian đồng hồ thực tế đã hết 3 giây chưa).
1. **eval_fn(state)** **thay thế** **utility** **:**
  - Khi `cutoff_test` trả về `True` ở một nút nằm lơ lửng giữa ván cờ, thay vì trả về lỗi, `eval_fn(state)` sẽ chạy thuật toán tính điểm nhanh (đếm quân, đo lợi thế) để gán cho trạng thái đó một con số ước lượng.
1. **Kết hợp Tìm kiếm sâu dần (Iterative Deepening Search):**
  - Trong thực tế thi đấu, người ta thường cho hàm `alpha_beta_cutoff_search` chạy trong một vòng lặp tăng dần độ sâu: đầu tiên tìm với `d = 1`, rồi `d = 2`, `d = 3`.... Nếu đồng hồ báo hết giờ giữa chừng, máy chỉ việc lấy ngay kết quả tốt nhất của độ sâu hoàn thành gần nhất để đánh.

---

## Mục 6.5: Trò chơi Ngẫu nhiên (Expectiminimax) và Khuyết thiếu Thông tin (Partially Observable Games)

### 1. Lý thuyết cốt lõi: Trò chơi ngẫu nhiên & Khuyết thiếu thông tin

Trong các phần trước, cờ vua và cờ ca-rô là các trò chơi **tất định (deterministic)** và **thông tin hoàn hảo (perfect information)**: không có may rủi và hai bên nhìn thấy toàn bộ bàn cờ. Tuy nhiên, thực tế phong phú hơn rất nhiều:

1. **Trò chơi ngẫu nhiên (Stochastic Games - Mục 6.5):** Có yếu tố may rủi (như tung xúc xắc trong Cờ cá ngựa, Backgammon).
1. **Trò chơi khuyết thiếu thông tin (Partially Observable / Imperfect Information Games - Mục 6.6):** Một phần trạng thái bị che giấu (như bài Poker, Tam cúc, cờ Kriegspiel).

---

#### 1.1. Trò chơi ngẫu nhiên và thuật toán Expectiminimax (Mục 6.5)

Khi trò chơi có yếu tố ngẫu nhiên (ví dụ tung xúc xắc), ta không thể chắc chắn một nước đi sẽ dẫn đến trạng thái cụ thể nào.

- **Nút cơ hội (Chance Nodes):** Bên cạnh nút **MAX** (hình tam giác hướng lên) và nút **MIN** (hình tam giác hướng xuống), cây trò chơi có thêm **nút cơ hội (vẽ bằng hình tròn)** đại diện cho xúc xắc hoặc xáo bài.
- **Giá trị kỳ vọng (Expected Value):** Tại nút cơ hội, không dùng hàm $\max$ hay $\min$ mà ta tính **trung bình có trọng số** (giá trị kỳ vọng) dựa trên xác suất $P(r)$ của từng kết quả ngẫu nhiên:

\[\text{EXPECTIMINIMAX}(s) = \begin{cases} \text{UTILITY}(s, \text{MAX}) & \text{nếu } \text{IS-TERMINAL}(s) \ \max_{a} \text{EXPECTIMINIMAX}(\text{RESULT}(s, a)) & \text{nếu } \text{TO-MOVE}(s) = \text{MAX} \ \min_{a} \text{EXPECTIMINIMAX}(\text{RESULT}(s, a)) & \text{nếu } \text{TO-MOVE}(s) = \text{MIN} \ \sum_{r} P(r) \cdot \text{EXPECTIMINIMAX}(\text{RESULT}(s, r)) & \text{nếu } \text{TO-MOVE}(s) = \text{CHANCE} \end{cases}\]

- **Độ phức tạp:** Với hệ số phân nhánh $b$, độ sâu $m$, và $n$ kết quả ngẫu nhiên khác nhau ở mỗi lần đổ xúc xắc, độ phức tạp thời gian tăng vọt lên $O(b^m \cdot n^m)$.
- **Lưu ý quan trọng về hàm EVAL:** Ở trò chơi ngẫu nhiên, **hàm đánh giá thế cờ (EVAL) bắt buộc phải là một phép biến đổi tuyến tính dương của xác suất chiến thắng**. Nếu chỉ giữ nguyên thứ tự ưu tiên (order-preserving) mà bóp méo tỷ lệ điểm số, thuật toán sẽ chọn sai nước đi hoàn toàn (xem Hình 6.14 trong sách).

---

#### 1.2. Trò chơi khuyết thiếu thông tin (Mục 6.6)

Trong các trò chơi bài (Poker, Bridge) hay cờ có sương mù chiến tranh (Kriegspiel), người chơi không nhìn thấy bài của đối phương.

- **Tập trạng thái niềm tin (Information Sets / Belief States):** Người chơi không biết chính xác mình đang ở nút nào trên cây trò chơi thực tế, mà chỉ biết mình đang nằm trong một tập hợp các trạng thái khả dĩ (gọi là *information set* ).
- **Phương pháp "Bình quân qua thấu thị" (Averaging over Clairvoyance):**
  - Đây là cách tiếp cận xấp xỉ trực quan: Coi việc chia bài ngẫu nhiên ban đầu như một nút CHANCE ở gốc cây. Giả định sau khi chia bài xong, cả hai bên đều nhìn thấy bài của nhau ("thấu thị"), rồi dùng `Expectiminimax` để tính.
  - *Nhược điểm:* Cách này bỏ qua các yếu tố tâm lý cốt lõi của bài Poker như **hành động thăm dò thông tin** hay **đòn nghi binh (bluffing)**. Để giải quyết triệt để, ta cần tìm **Điểm cân bằng Nash** với chiến lược hỗn hợp ngẫu nhiên hóa (được trình bày sâu ở Chương 17).

---

### 2. Giải thích chi tiết mã nguồn chương trình (`expectiminimax`)

Trong mã nguồn AIMA (`games.py` / `games.ipynb`), thuật toán `expectiminimax` được mở rộng trực tiếp từ khung sườn `minimax` chuẩn bằng cách bổ sung xử lý cho nút ngẫu nhiên:

#### 2.1. Cài đặt thuật toán Expectiminimax bằng Python

```python
def expectiminimax(state, game):
    """
    Trả về hành động tốt nhất cho người chơi tại trạng thái 'state' 
    trong trò chơi có yếu tố ngẫu nhiên (chứa nút Chance).
    """
    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -float('inf')
        for a in game.actions(state):
            v = max(v, chance_value(game.result(state, a)))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = float('inf')
        for a in game.actions(state):
            v = min(v, chance_value(game.result(state, a)))
        return v

    def chance_value(state):
        """
        Xử lý tại NÚT CƠ HỘI (Chance Node):
        Tính trung bình có trọng số (kỳ vọng) của tất cả các kết quả ngẫu nhiên.
        """
        if game.terminal_test(state):
            return game.utility(state, player)
        
        # Nếu trạng thái này chưa phải kết quả của xúc xắc, chuyển lượt tiếp
        # Nếu đang là nút Chance:
        # Lấy danh sách các kết quả khả dĩ 'r' và xác suất P(r) tương ứng
        outcomes = game.chances(state)  # Ví dụ: [((1, 2), 1/18), ((6, 6), 1/36), ...]
        
        expected_value = 0.0
        for outcome, prob in outcomes:
            next_state = game.result(state, outcome)
            
            # Sau khi có kết quả ngẫu nhiên, xem lượt tiếp theo là của MAX hay MIN
            if game.to_move(next_state) == player:
                val = max_value(next_state)
            else:
                val = min_value(next_state)
                
            expected_value += prob * val
            
        return expected_value

    # Tại nút gốc (lượt của MAX): Chọn hành động đem lại giá trị kỳ vọng lớn nhất
    return max(game.actions(state), key=lambda a: chance_value(game.result(state, a)))
```

---

#### 2.2. Giải thích từng dòng code thật dễ hiểu

1. **Sự xuất hiện của hàm** **chance_value(state)** **:**
  - Trong `minimax` truyền thống, `max_value` gọi trực tiếp `min_value`.
  - Trong `expectiminimax`, sau khi MAX chọn một nước đi $a$, trò chơi chưa sang ngay lượt của MIN mà phải qua một sự kiện ngẫu nhiên (đổ xúc xắc). Vì vậy `max_value` sẽ gọi `chance_value`.
1. **Vòng lặp tính tổng kỳ vọng (** **expected_value += prob * val** **):**
  - Hàm `game.chances(state)` trả về các biến cố cùng xác suất tương ứng (ví dụ: đổ ra đôi 6 với xác suất $\frac{1}{36}$, ra 6-5 với xác suất $\frac{1}{18}$ ).
  - Với mỗi biến cố, thuật toán tính điểm số nhánh con `val`, nhân với xác suất `prob`, rồi cộng dồn lại theo đúng công thức kỳ vọng toán học: $\sum P(r) \cdot V(r)$.
1. **Tại sao cắt tỉa Alpha-Beta ở đây lại khó hơn?**
  - Để tính giá trị trung bình của nhiều số, thông thường ta phải biết tất cả các số đó. Tuy nhiên, nếu ta biết trước giá trị tiện ích nằm trong một khoảng cố định (ví dụ $U \in [-2, +2]$ ), ta vẫn có thể chặn trên cận giá trị của nút Chance để cắt bớt một số nhánh xúc xắc xác suất thấp.

---

#### 2.3. Mã nguồn mô phỏng Khuyết thiếu thông tin (Averaging over Clairvoyance)

Để lập trình một tác tử AI chơi bài đơn giản (như Poker 2 người), kỹ thuật **lấy mẫu ngẫu nhiên qua các kịch bản bài ẩn (sampling)** thường được áp dụng:

```python
def information_state_player(state, game, num_samples=50):
    """
    Tác tử giải quyết khuyết thiếu thông tin bằng phương pháp lấy mẫu (Sampling):
    Đoán ngẫu nhiên bài đối phương rồi tính trung bình nước đi tối ưu.
    """
    actions = game.actions(state)
    action_scores = {a: 0.0 for a in actions}

    for _ in range(num_samples):
        # 1. Sinh ngẫu nhiên một 'bàn cờ hoàn chỉnh' hợp lệ (đoán bài tẩy đối phương)
        concrete_state = game.sample_hidden_state(state)
        
        # 2. Chạy thuật toán Alpha-Beta hoặc Expectiminimax trên bàn cờ đã rõ ràng này
        for a in actions:
            # Tích lũy điểm số cho từng hành động
            score = evaluate_state(game.result(concrete_state, a), game)
            action_scores[a] += score

    # Chọn nước đi có điểm trung bình cao nhất qua tất cả các mẫu giả lập
    return max(actions, key=lambda a: action_scores[a])
```

- **Ý nghĩa thực tế:** Dù tác tử không biết chắc đối thủ cầm lá bài nào, việc thử nghiệm 50–100 kịch bản khả dĩ nhất và chọn nước đi an toàn nhất trên đa số kịch bản đó sẽ đem lại phong độ thi đấu rất ổn định.

---

