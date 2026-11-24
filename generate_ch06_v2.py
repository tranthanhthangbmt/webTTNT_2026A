# -*- coding: utf-8 -*-
"""
Script tạo file Ch06_TTNT_v2.docx:
Bổ sung đầy đủ toàn bộ 16 hình từ Giáo trình Russell & Norvig (AIMA 4th)
và 10 hình slide infographic 3D kết xuất chất lượng cao, kèm các hộp giải thích trực quan chuẩn Word
và hiệu chỉnh toàn bộ công thức toán học bị thiếu.
"""
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os

def create_callout_box(doc, title, items, border_color="1A5276", bg_color="F4F6F7"):
    """Tạo hộp ghi chú / giải thích trực quan chuẩn Word với viền trái màu đậm và nền nhạt."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    
    # Màu nền
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)
    
    # Viền trái đậm, các viền khác ẩn
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)
    
    # Tiêu đề hộp giải thích
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"💡 {title}")
    run_t.bold = True
    run_t.font.name = 'Calibri'
    run_t.font.size = Pt(10.5)
    run_t.font.color.rgb = RGBColor(26, 82, 118)
    
    # Các điểm giải thích
    for item in items:
        p_item = cell.add_paragraph()
        p_item.paragraph_format.space_before = Pt(2)
        p_item.paragraph_format.space_after = Pt(2)
        p_item.paragraph_format.left_indent = Inches(0.15)
        run_bullet = p_item.add_run("• ")
        run_bullet.bold = True
        run_bullet.font.color.rgb = RGBColor(40, 116, 166)
        
        if ":" in item:
            parts = item.split(":", 1)
            r_bold = p_item.add_run(parts[0] + ":")
            r_bold.bold = True
            r_bold.font.name = 'Calibri'
            r_bold.font.size = Pt(9.5)
            r_text = p_item.add_run(parts[1])
            r_text.font.name = 'Calibri'
            r_text.font.size = Pt(9.5)
        else:
            r_text = p_item.add_run(item)
            r_text.font.name = 'Calibri'
            r_text.font.size = Pt(9.5)
            
    p_last = cell.paragraphs[-1]
    p_last.paragraph_format.space_after = Pt(6)
    return tbl

def insert_figure_before_p(doc, target_p, img_path, caption_text, width_inches=5.6, expl_title=None, expl_items=None):
    """Chèn hình ảnh, chú thích và hộp giải thích vào trước một paragraph mục tiêu."""
    if not os.path.exists(img_path):
        print(f"ERROR: File not found: {img_path}")
        return
        
    # 1. Đoạn chứa ảnh
    img_p = target_p.insert_paragraph_before()
    img_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    img_p.paragraph_format.space_before = Pt(14)
    img_p.paragraph_format.space_after = Pt(4)
    run_img = img_p.add_run()
    run_img.add_picture(img_path, width=Inches(width_inches))
    
    # 2. Đoạn chú thích ảnh
    cap_p = target_p.insert_paragraph_before()
    cap_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_p.paragraph_format.space_before = Pt(2)
    cap_p.paragraph_format.space_after = Pt(8)
    run_cap = cap_p.add_run(caption_text)
    run_cap.font.name = 'Calibri'
    run_cap.font.size = Pt(10)
    run_cap.font.italic = True
    run_cap.font.color.rgb = RGBColor(70, 70, 70)
    
    # 3. Hộp giải thích chi tiết nếu có
    if expl_title and expl_items:
        tbl = create_callout_box(doc, expl_title, expl_items)
        target_p._p.addprevious(tbl._tbl)
        
    # 4. Đoạn khoảng cách sau khối hình
    spacer = target_p.insert_paragraph_before()
    spacer.paragraph_format.space_before = Pt(2)
    spacer.paragraph_format.space_after = Pt(6)

def find_first_p(doc, snippet):
    """Tìm paragraph đầu tiên chứa chuỗi snippet (không phân biệt hoa thường)."""
    snippet_lower = snippet.lower()
    for p in doc.paragraphs:
        if snippet_lower in p.text.lower():
            return p
    return None

def fix_text_and_formulas(doc):
    """Sửa lỗi tiêu đề chương và các ký hiệu toán học bị mất trong văn bản gốc."""
    for p in doc.paragraphs:
        t = p.text
        # 1. Sửa tiêu đề chương 5 thành chương 6
        if 'CHƯƠNG 5: TÌM KIẾM ĐỐI KHÁNG' in t:
            p.text = t.replace('CHƯƠNG 5: TÌM KIẾM ĐỐI KHÁNG', 'CHƯƠNG 6: TÌM KIẾM ĐỐI KHÁNG')
            
        # 2. Sửa các thành phần bài toán hình thức ở Mục 1.3
        if '(Initial State): Trạng thái khởi đầu' in t and not t.startswith('• S₀'):
            p.text = '• S₀ (Initial State): Trạng thái khởi đầu của bàn cờ (ví dụ: bàn cờ vua lúc chưa đánh, bàn cờ ca-rô trống trơn).'
        elif ': Cho biết hiện tại đang là lượt đi của ai' in t and not t.startswith('• Player'):
            p.text = '• Player(s): Cho biết hiện tại đang là lượt đi của ai (MAX hay MIN) tại trạng thái s.'
        elif ': Tập hợp các nước đi hợp lệ' in t and not t.startswith('• Actions'):
            p.text = '• Actions(s): Tập hợp các nước đi hợp lệ mà người chơi hiện tại có thể thực hiện từ trạng thái s.'
        elif ': Mô hình chuyển trạng thái' in t and not t.startswith('• Result'):
            p.text = '• Result(s, a): Mô hình chuyển trạng thái (Transition Model), trả về bàn cờ mới sau khi thực hiện nước đi a từ bàn cờ s.'
        elif ': Hàm kiểm tra xem trò chơi đã kết thúc' in t and not t.startswith('• TerminalTest'):
            p.text = '• TerminalTest(s): Hàm kiểm tra xem trò chơi đã kết thúc hay chưa (ai đó thắng, thua hoặc hòa). Các trạng thái kết thúc gọi là trạng thái đích (terminal states).'
        elif ': Hàm thỏa dụng (payoff function)' in t and not t.startswith('• Utility'):
            p.text = '• Utility(s, p): Hàm thỏa dụng (payoff function), chấm điểm kết quả cuối cùng cho người chơi p tại trạng thái kết thúc s (ví dụ: với Tic-tac-toe, MAX thắng được +1, thua -1, hòa 0).'
            
        # 3. Sửa tham số alpha và beta ở Mục 6.3
        if '1.1. Ý nghĩa trực quan của hai tham số  và' in t:
            p.text = '1.1. Ý nghĩa trực quan của hai tham số α (Alpha) và β (Beta)'
        elif '(Alpha): Điểm số tốt nhất' in t and not t.startswith('• α'):
            p.text = '• α (Alpha): Điểm số tốt nhất (lớn nhất) mà người chơi MAX chắc chắn đã đạt được tại bất kỳ điểm lựa chọn nào từ trước tới nay dọc theo đường đi. (Khởi tạo ban đầu α = -∞).'
        elif 'Tư duy: MAX tự nhủ: “Tôi đã có trong tay' in t and 'ít nhất là  điểm' in t:
            p.text = 'Tư duy: MAX tự nhủ: “Tôi đã có trong tay phương án chắc chắn đạt ít nhất là α điểm”.'
        elif '(Beta): Điểm số tốt nhất' in t and not t.startswith('• β'):
            p.text = '• β (Beta): Điểm số tốt nhất (nhỏ nhất) mà đối thủ MIN chắc chắn đã ghìm được MAX xuống tại bất kỳ điểm lựa chọn nào dọc theo đường đi. (Khởi tạo ban đầu β = +∞).'
        elif 'Tư duy: MIN tự nhủ: “Tôi đã có trong tay' in t and 'chỉ được  điểm' in t:
            p.text = 'Tư duy: MIN tự nhủ: “Tôi đã có trong tay phương án ghìm MAX xuống nhiều nhất chỉ được β điểm”.'
            
        # 4. Sửa công thức Expectiminimax ở Mục 6.5
        if '[(s) =' in t:
            p.text = 'Expectiminimax(s) = ∑ P(r) × Expectiminimax(Result(s, r))   [tại nút ngẫu nhiên CHANCE]'
        elif t.strip() == ']':
            p.text = 'Tại nút MAX: max_a Expectiminimax(Result(s, a))  |  Tại nút MIN: min_a Expectiminimax(Result(s, a))  |  Tại nút lá: Utility(s)'
        elif 'Độ phức tạp: Với hệ số phân nhánh' in t and 'khác nhau ở mỗi lần đổ xúc xắc' in t:
            p.text = 'Độ phức tạp: Với hệ số phân nhánh b, độ sâu m, và n kết quả ngẫu nhiên khác nhau ở mỗi lần đổ xúc xắc, độ phức tạp thời gian tăng vọt lên O(b^m × n^m).'

def main():
    docx_in = 'video/Chapter06/Ch06_TTNT.docx'
    docx_out = 'video/Chapter06/Ch06_TTNT_v2.docx'
    
    print(f"Loading {docx_in}...")
    doc = docx.Document(docx_in)
    
    print("Fixing textual and mathematical issues...")
    fix_text_and_formulas(doc)
    
    print("Injecting figures and explanations...")
    
    # ----------------------------------------------------
    # 1. Slide 1: Đấu trường Trí tuệ Nhân tạo 3D
    # ----------------------------------------------------
    p_target = find_first_p(doc, 'Mục 6.1: Trò chơi và Lý thuyết Trò chơi')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-1.png',
        'Hình 6.0A (Slide 1): Đấu trường Trí tuệ Nhân tạo - Cuộc đối đầu kinh điển giữa Vua Trắng và Vua Đen trên bàn cờ vua 3D.',
        width_inches=5.8,
        expl_title="Ý nghĩa chiến lược của Tìm kiếm đối kháng trong AI",
        expl_items=[
            "Đấu trường trí tuệ kinh điển: Khác biệt căn bản với môi trường đơn tác tử ở các chương trước (nơi ngoại cảnh thụ động và đứng yên), trong trò chơi đối kháng tác nhân phải đối mặt với đối thủ có trí thông minh và mục tiêu hoàn toàn trái ngược.",
            "Mô hình tương tác: Hai bên luân phiên đưa ra quyết định, biến ván cờ thành một cuộc đấu trí chiến lược nhiều tầng đầy kịch tính.",
            "Mục tiêu tối thượng: Tìm ra nước đi tối ưu (Optimal Decision) giúp tác nhân giành chiến thắng hoặc bảo toàn vị thế bất kể đối thủ đáp trả sắc bén đến đâu."
        ]
    )
    
    # ----------------------------------------------------
    # 2. Slide 2: Bản đồ 5 chuyên đề cốt lõi
    # ----------------------------------------------------
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-2.png',
        'Hình 6.0B (Slide 2): Bản đồ 5 chuyên đề cốt lõi của Chương 6 trong Giáo trình Chuẩn AIMA.',
        width_inches=5.8,
        expl_title="Bản đồ kiến thức 5 chuyên đề cốt lõi của Chương 6",
        expl_items=[
            "Mục 6.1 (Biểu tượng Quân Mã): Lý thuyết trò chơi và công thức hóa bài toán đối kháng 2 người tổng bằng không.",
            "Mục 6.2 (Biểu tượng Cúp vàng): Quyết định tối ưu và Thuật toán Minimax kinh điển của John von Neumann.",
            "Mục 6.3 (Biểu tượng Kéo tỉa): Tối ưu hóa không gian và thời gian với Giải thuật Cắt tỉa Alpha-Beta.",
            "Mục 6.4 (Biểu tượng Đồng hồ cát): Quyết định thời gian thực không hoàn hảo, Hàm Heuristic và Tìm kiếm Cây Monte Carlo (MCTS).",
            "Mục 6.5 & 6.6 (Biểu tượng Xúc xắc & Bộ bài): Mở rộng sang trò chơi ngẫu nhiên (Expectiminimax) và khuyết thiếu thông tin (Partially Observable)."
        ]
    )
    
    # ----------------------------------------------------
    # 3. Slide 3: Lý thuyết trò chơi & Shannon Number
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.2. Trò chơi đối kháng 2 người')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-3.png',
        'Hình 6.1A (Slide 3): Lý thuyết trò chơi, Phân loại môi trường đối kháng và Sự bùng nổ tổ hợp (Shannon Number).',
        width_inches=5.8,
        expl_title="Ba góc nhìn đa tác tử và Con số Shannon trong Cờ vua",
        expl_items=[
            "Môi trường đa tác tử: Tác nhân không thể lập kế hoạch tuyến tính cố định mà phải liên tục mô hình hóa hành động và phản ứng của đối phương.",
            "Trò chơi tổng bằng không (Zero-sum): Lợi ích của người này là tổn thất của người kia. Tổng giá trị Utility luôn triệt tiêu lẫn nhau.",
            "Độ phức tạp vượt ngưỡng vũ trụ: Cờ vua có khoảng 10^40 trạng thái và cây trò chơi có khoảng 10^123 nút (Số Shannon), lớn hơn nhiều so với 10^80 nguyên tử trong vũ trụ khả kiến! Việc tìm kiếm vét cạn bằng BFS/DFS truyền thống là vĩnh viễn bất khả thi."
        ]
    )
    
    # ----------------------------------------------------
    # 4. Slide 4: Chuẩn hóa mô hình hình thức 6 thành phần
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.4. Cây trò chơi (Game Tree)')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-4.png',
        'Hình 6.1B (Slide 4): Chuẩn hóa mô hình toán học hình thức 6 thành phần của trò chơi đối kháng 2 người.',
        width_inches=5.8,
        expl_title="Chi tiết 6 thành phần của bài toán trò chơi 2 người",
        expl_items=[
            "S₀ (Initial State): Trạng thái khởi đầu của bàn cờ.",
            "Player(s): Hàm xác định người chơi đến lượt đi tại trạng thái s (MAX hoặc MIN).",
            "Actions(s): Tập các nước đi hợp lệ có thể thực hiện từ trạng thái s.",
            "Result(s, a): Hàm chuyển đổi trạng thái (Transition Model), trả về bàn cờ mới sau khi thực hiện nước đi a.",
            "TerminalTest(s): Hàm kiểm tra điều kiện kết thúc ván cờ (thắng, thua, hòa).",
            "Utility(s, p): Hàm thỏa dụng chấm điểm kết quả cuối cùng cho người chơi p tại trạng thái lá (ví dụ: +1 nếu MAX thắng, -1 nếu MIN thắng, 0 nếu hòa)."
        ]
    )
    
    # ----------------------------------------------------
    # 5. Hình 6.1 AIMA: Cây trò chơi Tic-Tac-Toe
    # ----------------------------------------------------
    p_target = find_first_p(doc, '2. Giải thích chi tiết mã nguồn chương trình (games.ipynb)')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.1.jpg',
        'Hình 6.1 (AIMA): Cây trò chơi Tic-Tac-Toe (Cờ ca-rô 3x3) với các tầng luân phiên MAX / MIN và các nút lá kết thúc.',
        width_inches=5.5,
        expl_title="Phân tích cấu trúc Cây trò chơi Tic-Tac-Toe (Hình 6.1 AIMA)",
        expl_items=[
            "Cấu trúc phân tầng (Two-ply): Nút gốc là lượt của MAX (quân X có 9 lựa chọn). Tầng kế tiếp là lượt của MIN (quân O có 8 lựa chọn cho mỗi nhánh con của X).",
            "Các nút lá (Terminal States): Điểm cuối cùng của mỗi nhánh nơi trò chơi kết thúc. Hàm Utility chấm điểm: +1 nếu MAX thắng, -1 nếu MIN thắng, 0 nếu hòa.",
            "Quy mô cây tìm kiếm: Tổng số nút lá trên cây đầy đủ là 255.168 nhánh, nhưng chỉ tương ứng với 5.478 trạng thái bàn cờ phân biệt (nhờ các phép đối xứng xoay và phản xạ)."
        ]
    )
    
    # ----------------------------------------------------
    # 6. Hình 6.3 AIMA: Lan truyền giá trị Minimax trên cây 2 tầng
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.3. Độ phức tạp của thuật toán')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.3.jpg',
        'Hình 6.3 (AIMA): Cơ chế lan truyền giá trị đệ quy của thuật toán Minimax trên cây trò chơi 2 tầng (Two-ply game tree).',
        width_inches=4.8,
        expl_title="Cơ chế lan truyền giá trị đệ quy Minimax (Hình 6.3 AIMA)",
        expl_items=[
            "Tầng lá: Các trạng thái kết thúc mang giá trị thỏa dụng được xác định từ trước: Nhánh B có [3, 12, 8], nhánh C có [2, 4, 6], nhánh D có [14, 5, 2].",
            "Tầng của MIN (Nút B, C, D): MIN là người chơi tối ưu hóa điểm trừ của MAX, do đó MIN luôn chọn giá trị nhỏ nhất: min(3, 12, 8) = 3; min(2, 4, 6) = 2; min(14, 5, 2) = 2.",
            "Tầng gốc của MAX (Nút A): MAX chọn nước đi đem lại giá trị lớn nhất từ các kịch bản của MIN: max(3, 2, 2) = 3 (chọn nhánh a1).",
            "Triết lý Minimax: MAX không kỳ vọng vào kịch bản may mắn (như điểm số 14 ở nhánh D) mà luôn tính toán dựa trên kịch bản đối thủ đáp trả hiểm hóc nhất."
        ]
    )
    
    # ----------------------------------------------------
    # 7. Hình 6.4 AIMA: Cây trò chơi 3 người chơi
    # ----------------------------------------------------
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.4.jpg',
        'Hình 6.4 (AIMA): Cây trò chơi đối kháng 3 người chơi (Three-player game tree) với vector thỏa dụng [vA, vB, vC].',
        width_inches=5.5,
        expl_title="Mở rộng Minimax cho trò chơi 3 người chơi (Hình 6.4 AIMA)",
        expl_items=[
            "Vector thỏa dụng: Mỗi nút lưu một vector điểm số [vA, vB, vC] tương ứng với lợi ích của 3 người chơi A, B và C.",
            "Lựa chọn của từng người chơi: Đến lượt của A, A chọn nhánh có vA lớn nhất; đến lượt của B, B chọn nhánh có vB lớn nhất; đến lượt của C, C chọn nhánh có vC lớn nhất.",
            "Động lực liên minh: Trong trò chơi đa đối thủ, có thể xuất hiện sự bắt tay ngầm hoặc phản bội giữa các bên yếu để lật đổ người chơi đang dẫn đầu."
        ]
    )
    
    # ----------------------------------------------------
    # 8. Hình 6.2 AIMA: Mã giả thuật toán Minimax
    # ----------------------------------------------------
    p_target = find_first_p(doc, '2.2. Giải thích từng dòng code thật dễ hiểu')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.2.jpg',
        'Hình 6.2 (AIMA): Mã giả chuẩn tắc thuật toán Minimax (MINIMAX-SEARCH, MAX-VALUE, MIN-VALUE) trong giáo trình Russell & Norvig.',
        width_inches=5.2,
        expl_title="Giải thuật Minimax đệ quy tương hỗ (Hình 6.2 AIMA)",
        expl_items=[
            "MINIMAX-SEARCH: Hàm điều phối chính, gọi MAX-VALUE để duyệt qua mọi hành động hợp lệ từ trạng thái hiện tại và trả về hành động mang lại điểm số cao nhất.",
            "MAX-VALUE và MIN-VALUE: Hai hàm đệ quy tương hỗ (Mutual Recursion). MAX-VALUE tìm giá trị lớn nhất từ các phản hồi của MIN-VALUE; ngược lại MIN-VALUE tìm giá trị nhỏ nhất từ MAX-VALUE.",
            "Điều kiện neo (Base Case): Khi IS-TERMINAL(state) là True, đệ quy dừng và trả về UTILITY(state, player).",
            "Ánh xạ Python: Tương ứng trực tiếp 1:1 với hàm minimax_decision(state, game) trong file games.py."
        ]
    )
    
    # ----------------------------------------------------
    # 9. Slide 9: Biểu tượng Kéo vàng cắt tỉa Alpha-Beta
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.2. Nguyên lý cắt tỉa: Khi nào ta được quyền')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-9.png',
        'Hình 6.4A (Slide 9): Nguyên lý Cắt tỉa Alpha-Beta và điều kiện cắt nhánh then chốt α ≥ β.',
        width_inches=5.8,
        expl_title="Kỹ thuật Cắt tỉa Alpha-Beta và Điều kiện cốt lõi α ≥ β",
        expl_items=[
            "α (Alpha): Giới hạn sàn - Điểm số tốt nhất (cao nhất) mà MAX chắc chắn có thể đạt được ở các nhánh đã duyệt qua từ trước tới nay. (Ban đầu α = -∞).",
            "β (Beta): Giới hạn trần - Điểm số tốt nhất cho MIN (tức thấp nhất cho MAX) mà MIN có thể ép MAX nhận. (Ban đầu β = +∞).",
            "Điều kiện cắt tỉa α ≥ β: Khi giá trị nhánh con vượt quá β (tại lượt MAX) hoặc tụt dưới α (tại lượt MIN), nhánh này sẽ bị đối phương né tránh hoàn toàn, do đó việc tiếp tục tính toán là vô nghĩa và có thể cắt bỏ ngay."
        ]
    )
    
    # ----------------------------------------------------
    # 10. Hình 6.6 AIMA: Trường hợp tổng quát Alpha-Beta
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.3. Ví dụ minh họa từng bước trên Hình 6.5')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.6.jpg',
        'Hình 6.6 (AIMA): Mô hình toán học tổng quát chứng minh tính đúng đắn của Cắt tỉa Alpha-Beta.',
        width_inches=4.2,
        expl_title="Mô hình toán học tổng quát của Cắt tỉa Alpha-Beta (Hình 6.6 AIMA)",
        expl_items=[
            "Nút tổ tiên: Người chơi (Player) tại một nút tổ tiên đã có trong tay phương án chắc chắn đạt ít nhất là điểm m.",
            "Nút đang xét: Khi Người chơi xét nhánh con dẫn đến nút n, Đối thủ (Opponent) có một nước đi n' dẫn đến kết quả m' ≤ m.",
            "Hệ quả logic: Đối thủ chắc chắn sẽ chọn nước đi dẫn tới m' để ghìm điểm Người chơi xuống. Do đó Người chơi không bao giờ chọn đi vào nút n. Toàn bộ các nhánh con còn lại của n bị cắt bỏ lập tức mà không làm mất tính tối ưu!"
        ]
    )
    
    # ----------------------------------------------------
    # 11. Hình 6.5 AIMA: Diễn biến 4 giai đoạn Cắt tỉa Alpha-Beta
    # ----------------------------------------------------
    # Look for third occurrence of this heading (in Section 6.3)
    headings_found = [p for p in doc.paragraphs if '2. Giải thích chi tiết mã nguồn chương trình (games.ipynb)'.lower() in p.text.lower()]
    p_target_63 = headings_found[2] if len(headings_found) > 2 else headings_found[-1]
    
    insert_figure_before_p(
        doc, p_target_63,
        'TaiLieu/Figures/Images/figure_6.5.jpg',
        'Hình 6.5 (AIMA): Quá trình cắt tỉa Alpha-Beta diễn ra tuần tự qua 4 giai đoạn (a), (b), (c), (d) trên cây Fig52Game.',
        width_inches=5.8,
        expl_title="Diễn biến 4 giai đoạn cắt tỉa Alpha-Beta (Hình 6.5 AIMA)",
        expl_items=[
            "Bước (a): Duyệt xong nhánh B, xác định giá trị của B là 3. Cập nhật tại gốc α = 3.",
            "Bước (b): Sang nhánh C, xét lá đầu tiên có giá trị 2. Vì C là nút MIN nên C tối đa chỉ bằng 2 (β ≤ 2). Vì β = 2 ≤ α = 3, xảy ra Alpha-cutoff! Hai lá còn lại của C bị cắt bỏ hoàn toàn.",
            "Bước (c): Chuyển sang nhánh D, xét lá đầu tiên có giá trị 14. Vì 14 > α nên chưa thể cắt, tiếp tục xét lá thứ hai có giá trị 5.",
            "Bước (d): Xét lá thứ ba của D có giá trị 2, suy ra giá trị của D là 2. Kết luận: Gốc A chọn nhánh B với điểm số 3, bảo toàn kết quả tối ưu của Minimax mà không cần duyệt 2 lá ở nhánh C."
        ]
    )
    
    # ----------------------------------------------------
    # 12. Hình 6.7 AIMA: Mã giả thuật toán Alpha-Beta Search
    # ----------------------------------------------------
    p_target = find_first_p(doc, '2.2. Kiểm chứng trong thực tế với games.ipynb')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.7.jpg',
        'Hình 6.7 (AIMA): Mã giả thuật toán Tìm kiếm Alpha-Beta (ALPHA-BETA-SEARCH) hoàn chỉnh trong giáo trình AIMA.',
        width_inches=4.8,
        expl_title="Mã giả thuật toán Tìm kiếm Alpha-Beta (Hình 6.7 AIMA)",
        expl_items=[
            "Khởi tạo biên: Bắt đầu với α = -∞ và β = +∞.",
            "Cắt tỉa trong MAX-VALUE: Nếu giá trị con v ≥ β, hàm lập tức ngắt vòng lặp và return v (Beta-cutoff). Sau mỗi nhánh, cập nhật α = max(α, v).",
            "Cắt tỉa trong MIN-VALUE: Nếu giá trị con v ≤ α, hàm lập tức ngắt vòng lặp và return v (Alpha-cutoff). Sau mỗi nhánh, cập nhật β = min(β, v).",
            "Tương ứng mã nguồn: Ánh xạ chuẩn tắc vào hàm alphabeta_search(state, game) trong file games.py."
        ]
    )
    
    # ----------------------------------------------------
    # 13. Slide 13: Hiệu quả Alpha-Beta & Move Ordering
    # ----------------------------------------------------
    p_target = find_first_p(doc, 'Mục 6.4: Quyết định Thời gian thực Không hoàn hảo')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-13.png',
        'Hình 6.7A (Slide 13): Đánh giá hiệu quả của Cắt tỉa Alpha-Beta và Tầm quan trọng của Kỹ thuật Sắp xếp nước đi (Move Ordering).',
        width_inches=5.8,
        expl_title="Hiệu quả của Cắt tỉa Alpha-Beta và Kỹ thuật Sắp xếp nước đi (Slide 13)",
        expl_items=[
            "Bảo toàn 100% tính tối ưu: Quyết định trả về bởi Alpha-Beta hoàn toàn trùng khớp với kết quả duyệt toàn bộ của Minimax.",
            "Thứ tự duyệt ngẫu nhiên: Độ phức tạp trung bình giảm xuống còn O(b^(3m/4)).",
            "Thứ tự duyệt lý tưởng (Move Ordering): Nếu luôn xét nước đi tốt nhất trước, độ phức tạp thời gian giảm ngoạn mục xuống O(b^(m/2)) = O((√b)^m).",
            "Ý nghĩa thực chiến: Trong cờ vua (b ≈ 35), hệ số phân nhánh hữu hiệu giảm xuống chỉ còn ≈ 6. Điều này cho phép AI nhìn sâu gấp đôi số nước đi trong cùng một khoảng thời gian thi đấu!"
        ]
    )
    
    # ----------------------------------------------------
    # 14. Slide 14: Kỹ thuật nâng cao thời gian thực (Vua bọc não nơ-ron)
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1. Lý thuyết cốt lõi: Phần 6.4')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-14.png',
        'Hình 6.7B (Slide 14): Cột mốc chuyển tiếp sang các kỹ thuật nâng cao giải quyết áp lực thời gian thực trong Cây trò chơi.',
        width_inches=5.8,
        expl_title="Kỹ thuật nâng cao trong Cây trò chơi dưới áp lực thời gian thực (Slide 14)",
        expl_items=[
            "Hình ảnh nghệ thuật 3D Quân Vua cờ vua gỗ ôm trọn bộ não nơ-ron: Tượng trưng cho sự hội tụ giữa lý thuyết trò chơi toán học kinh điển và mạng nơ-ron học sâu hiện đại.",
            "Thách thức thực tế: Kỳ thủ AI không thể duyệt đến tận cuối ván cờ vì thời gian suy nghĩ bị giới hạn nghiêm ngặt.",
            "Giải pháp: Cắt ngắn cây tìm kiếm tại độ sâu hợp lý và dùng Hàm lượng giá Heuristic (Eval Function) để phán đoán ưu thế thế cờ."
        ]
    )
    
    # ----------------------------------------------------
    # 15. Slide 15: Heuristic Minimax & 3 Yêu cầu Eval
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.2. Hàm lượng giá Heuristic (EVAL) được xây dựng')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-15.png',
        'Hình 6.7C (Slide 15): Mô hình Heuristic Minimax và 3 yêu cầu chuẩn tắc của Hàm lượng giá thế cờ (Eval Function).',
        width_inches=5.8,
        expl_title="Heuristic Minimax và 3 Yêu cầu Chuẩn tắc của Hàm Lượng Giá (Slide 15)",
        expl_items=[
            "Công thức chuyển đổi: Thay TerminalTest bằng CutoffTest và thay Utility bằng Eval.",
            "Yêu cầu 1 (Bảo toàn thứ tự): Hàm Eval phải xếp hạng các trạng thái kết thúc hoàn toàn trùng khớp với hàm Utility (Thắng > Hòa > Thua).",
            "Yêu cầu 2 (Tốc độ tính toán): Hàm Eval phải cực kỳ nhanh, vì một giây máy tính cần đánh giá hàng triệu vị trí bàn cờ.",
            "Yêu cầu 3 (Tương quan chính xác): Đối với các thế cờ chưa kết thúc, giá trị Eval phải tỷ lệ thuận với xác suất thực tế giành chiến thắng."
        ]
    )
    
    # ----------------------------------------------------
    # 16. Hình 6.8 AIMA: Hàm lượng giá Heuristic Cờ vua
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.3. Hai cạm bẫy kinh điển và cách khắc phục')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.8.jpg',
        'Hình 6.8 (AIMA): Hàm lượng giá thế cờ trong Cờ vua - Đánh giá ưu thế dựa trên chênh lệch giá trị quân và vị trí chiến lược.',
        width_inches=5.8,
        expl_title="Hàm lượng giá Heuristic trong Cờ vua (Hình 6.8 AIMA)",
        expl_items=[
            "Thang điểm trọng số quân cờ: Tốt (Pawn) = 1, Mã (Knight) = 3, Tượng (Bishop) = 3, Xe (Rook) = 5, Hậu (Queen) = 9.",
            "Hàm tổ hợp tuyến tính: Eval(s) = w₁f₁(s) + w₂f₂(s) + ... + wₙfₙ(s), với f_i là các đặc trưng bàn cờ (chênh lệch lực lượng, vị trí kiểm soát trung tâm, an toàn của Vua).",
            "Phân tích thế trận trên hình: Cả hai thế cờ có cùng chênh lệch quân số (Trắng hơn 1 Xe), nhưng thế cờ bên trái Trắng có ưu thế áp đảo do Xe kiểm soát cột mở và Vua Trắng được che chắn kín kẽ hơn."
        ]
    )
    
    # ----------------------------------------------------
    # 17. Hình 6.9 AIMA: Cạm bẫy tìm kiếm cạn & Tìm kiếm tĩnh lặng
    # ----------------------------------------------------
    p_target = find_first_p(doc, 'Hiệu ứng chân trời (Horizon Effect):')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.9.jpg',
        'Hình 6.9 (AIMA): Cạm bẫy của việc dừng tìm kiếm tại trạng thái không tĩnh (Non-quiescent state) và Giải pháp Tìm kiếm tĩnh lặng.',
        width_inches=4.2,
        expl_title="Cạm bẫy Tìm kiếm cạn và Giải pháp Tìm kiếm tĩnh lặng (Hình 6.9 AIMA)",
        expl_items=[
            "Bẫy điểm mù (Non-quiescent state): Nếu dừng tìm kiếm ngay sau khi Xe trắng vừa ăn một quân của Đen, hàm Heuristic thấy Trắng hơn điểm (+5) và đánh giá rất cao nước đi này. Tuy nhiên ngay nước sau, Đen dùng Hậu bắt lại Xe Trắng, khiến Trắng thiệt hại nặng nề.",
            "Giải pháp - Tìm kiếm tĩnh lặng (Quiescence Search): Khi đạt độ sâu giới hạn, nếu bàn cờ chưa ổn định (còn các nước ăn quân hoặc chiếu tướng), AI tiếp tục mở rộng đệ quy thêm các nước giao tranh cho tới khi thế cờ thực sự yên ắng mới được phép gọi hàm Eval."
        ]
    )
    
    # ----------------------------------------------------
    # 18. Hình 6.10 AIMA: Hiệu ứng đường chân trời
    # ----------------------------------------------------
    p_target = find_first_p(doc, '2. Giải thích chi tiết mã nguồn chương trình (games.ipynb / games.py)')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.10.jpg',
        'Hình 6.10 (AIMA): Hiệu ứng đường chân trời (Horizon Effect) trong cờ vua - Nguy cơ quân Tốt đối phương phong cấp thành Hậu.',
        width_inches=5.8,
        expl_title="Hiệu ứng đường chân trời (Horizon Effect) trong Cờ vua (Hình 6.10 AIMA)",
        expl_items=[
            "Bản chất cạm bẫy: Khi một tổn thất lớn là không thể đảo ngược (quân Tốt Đen chắc chắn sẽ phong Hậu), AI bị giới hạn độ sâu sẽ cố tình chiếu Vua vô nghĩa hoặc thí quân để đẩy thời điểm đối phương phong Hậu vượt ra ngoài 'đường chân trời' tìm kiếm.",
            "Hậu quả thảm hại: AI tưởng rằng mình đã hóa giải được nguy hiểm, nhưng thực chất chỉ đang hoãn thời điểm chịu đòn và làm mất thêm nhiều quân cờ khác một cách vô ích."
        ]
    )
    
    # ----------------------------------------------------
    # 19. Bổ sung Chuyên đề MCTS: Slide 17, Hình 6.11, Hình 6.12
    # ----------------------------------------------------
    # Chèn một Heading 4 và nội dung giới thiệu MCTS trước Mục 2 của 6.4
    p_mcts_head = p_target.insert_paragraph_before()
    p_mcts_head.style = doc.styles['Heading 4']
    p_mcts_head.text = "1.4. Đột phá Thời đại mới: Tìm kiếm Cây Monte Carlo (MCTS - Monte Carlo Tree Search)"
    
    p_mcts_desc = p_target.insert_paragraph_before()
    p_mcts_desc.text = "Trong giáo trình AIMA 4th Edition, Tìm kiếm Cây Monte Carlo (MCTS) được dành một vị trí trung tâm nhằm lý giải sự thống trị của AlphaGo trước các đại kiện tướng cờ vây nhân loại. Khi hệ số phân nhánh b quá lớn và hàm đánh giá tĩnh không thể tính toán chính xác, MCTS giải quyết bài toán bằng cách kết hợp giữa việc mở rộng cây tìm kiếm có chọn lọc với mô phỏng ngẫu nhiên (rollout)."
    
    # Chèn Slide 17
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-17.png',
        'Hình 6.10A (Slide 17): Cuộc cách mạng Tìm kiếm Cây Monte Carlo (MCTS) và Cột mốc lịch sử AlphaGo.',
        width_inches=5.8,
        expl_title="Cuộc cách mạng MCTS và Cột mốc Lịch sử AlphaGo (Slide 17)",
        expl_items=[
            "Đấu trường Cờ Vây: 10^170 trạng thái hợp lệ với hệ số phân nhánh trung bình b ≈ 250, vượt xa năng lực duyệt của Minimax và Alpha-Beta truyền thống.",
            "Ý tưởng cốt lõi của MCTS: Thay vì lượng giá bàn cờ bằng một hàm heuristic tĩnh, tác nhân thực hiện hàng nghìn ván chơi mô phỏng nhanh đến khi kết thúc để thống kê tỷ lệ thắng thực tế.",
            "AlphaGo (2016): Đột phá lịch sử khi kết hợp MCTS với mạng nơ-ron sâu (Policy Network chọn nước đi và Value Network đánh giá thế cờ), chính thức đánh bại đương kim vô địch thế giới Lee Sedol."
        ]
    )
    
    # Chèn Hình 6.11 AIMA
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.11.jpg',
        'Hình 6.11 (AIMA): 4 giai đoạn cốt lõi của Thuật toán MCTS: Selection, Expansion, Simulation, Backpropagation.',
        width_inches=5.8,
        expl_title="4 Giai đoạn cốt lõi của Thuật toán MCTS (Hình 6.11 AIMA)",
        expl_items=[
            "1. Lựa chọn (Selection): Đi xuống cây từ gốc bằng công thức UCT (Upper Confidence Bound for Trees): UCT = Q/N + c√(ln(N_parent)/N), giúp cân bằng hoàn hảo giữa Khai thác (Exploitation - chọn nhánh có tỷ lệ thắng cao) và Khám phá (Exploration - thử các nhánh ít được thăm).",
            "2. Mở rộng (Expansion): Khi chạm tới một nút lá chưa được mở rộng hoàn toàn, chọn một hành động hợp lệ chưa thử và thêm nút con mới vào cây tìm kiếm.",
            "3. Mô phỏng (Simulation / Rollout): Từ nút con mới, tiến hành chơi ngẫu nhiên nhanh (hoặc dùng chính sách nhẹ) cho đến khi ván cờ phân định thắng bại.",
            "4. Lan truyền ngược (Backpropagation): Lấy kết quả thắng/thua truyền ngược lên gốc, cập nhật số trận thắng Q và số lượt ghé thăm N cho toàn bộ các nút tổ tiên."
        ]
    )
    
    # Chèn Hình 6.12 AIMA
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.12.jpg',
        'Hình 6.12 (AIMA): Mã giả thuật toán Tìm kiếm Cây Monte Carlo (MCTS) chuẩn tắc trong AIMA 4th Edition.',
        width_inches=5.0,
        expl_title="Mã giả thuật toán MCTS (Hình 6.12 AIMA)",
        expl_items=[
            "Vòng lặp trong quỹ thời gian: Hàm MCTS-SEARCH lặp lại 4 bước Selection -> Expansion -> Simulation -> Backpropagation liên tục cho đến khi hết thời gian suy nghĩ cho phép.",
            "Quyết định nước đi cuối cùng: Sau khi hết thời gian, thay vì chọn nút có điểm Q cao nhất, thuật toán trả về nút con có số lượt ghé thăm N nhiều nhất (nước đi vững chắc và được kiểm chứng nhiều nhất)."
        ]
    )
    
    # ----------------------------------------------------
    # 20. Slide 18: Trò chơi ngẫu nhiên & xúc xắc
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.1. Trò chơi ngẫu nhiên và thuật toán Expectiminimax')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-18.png',
        'Hình 6.12A (Slide 18): Trò chơi Ngẫu nhiên (Stochastic Games) và Thuật toán Expectiminimax.',
        width_inches=5.8,
        expl_title="Trò chơi Ngẫu nhiên và Thuật toán Expectiminimax (Slide 18)",
        expl_items=[
            "Môi trường có yếu tố may rủi: Xúc xắc, xáo bài hoặc biến cố ngẫu nhiên làm cho kết quả của một hành động không còn tất định.",
            "Nút cơ hội (Chance Nodes): Các nút hình tròn nằm xen kẽ giữa các tầng MAX và MIN trên cây trò chơi.",
            "Nguyên lý tính điểm: Tại nút cơ hội, điểm số được tính bằng giá trị kỳ vọng (Expected Value) - trung bình có trọng số theo xác suất của các kết quả ngẫu nhiên."
        ]
    )
    
    # ----------------------------------------------------
    # 21. Hình 6.13 AIMA: Bàn cờ Backgammon
    # ----------------------------------------------------
    p_target = find_first_p(doc, 'Giá trị kỳ vọng (Expected Value):')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.13.jpg',
        'Hình 6.13 (AIMA): Bàn cờ Thỏ cáo (Backgammon) - Trò chơi Đối kháng Ngẫu nhiên Kinh điển.',
        width_inches=5.2,
        expl_title="Bàn cờ Thỏ cáo (Backgammon) - Trò chơi Đối kháng Ngẫu nhiên (Hình 6.13 AIMA)",
        expl_items=[
            "Quy tắc xúc xắc: Mỗi lượt người chơi tung 2 con xúc xắc. Có 21 kết quả khả dĩ: 6 cặp đôi (như 6-6, 5-5) với xác suất 1/36, và 15 cặp khác nhau (như 6-5, 4-3) với xác suất 2/36 = 1/18.",
            "Hệ số phân nhánh: Sau khi có kết quả xúc xắc, người chơi có trung bình khoảng 20 nước đi hợp lệ. Khi tính cả biến cố xúc xắc, hệ số phân nhánh trung bình lên tới ≈ 20 × 21 ≈ 400!",
            "Thành tựu AI: Chương trình TD-Gammon của Gerald Tesauro (1992) sử dụng học tăng cường (Temporal Difference Learning) kết hợp mạng nơ-ron đã đạt trình độ đẳng cấp thế giới."
        ]
    )
    
    # ----------------------------------------------------
    # 22. Hình 6.14 AIMA: Cây trò chơi Expectiminimax
    # ----------------------------------------------------
    p_target = find_first_p(doc, 'Lưu ý quan trọng về hàm EVAL: Ở trò chơi ngẫu nhiên')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.14.jpg',
        'Hình 6.14 (AIMA): Cây trò chơi Expectiminimax với các nút cơ hội Chance xen kẽ giữa MAX và MIN.',
        width_inches=5.8,
        expl_title="Cây trò chơi Expectiminimax với các nút cơ hội Chance (Hình 6.14 AIMA)",
        expl_items=[
            "Nút tam giác MAX: Chọn nước đi tối đa hóa điểm số (max_a).",
            "Nút tròn CHANCE: Tính tổng giá trị kỳ vọng: ∑ P(r) × Expectiminimax(Result(s, r)).",
            "Nút tam giác MIN: Chọn nước đi ghìm điểm số xuống thấp nhất (min_a).",
            "Độ phức tạp tính toán: Độ phức tạp thời gian là O(b^m × n^m), trong đó n là số kết quả ngẫu nhiên khả dĩ ở mỗi lần tung xúc xắc."
        ]
    )
    
    # ----------------------------------------------------
    # 23. Hình 6.15 AIMA: Tính nhạy cảm Expectiminimax
    # ----------------------------------------------------
    p_target = find_first_p(doc, '1.2. Trò chơi khuyết thiếu thông tin (Mục 6.6)')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.15.jpg',
        'Hình 6.15 (AIMA): Tính nhạy cảm của Expectiminimax trước phép biến đổi thang điểm đánh giá.',
        width_inches=5.0,
        expl_title="Tính nhạy cảm của Expectiminimax trước phép biến đổi thang điểm (Hình 6.15 AIMA)",
        expl_items=[
            "Sự khác biệt với Minimax: Trong Minimax chuẩn, bất kỳ phép biến đổi đơn điệu bảo toàn thứ tự (Order-preserving monotonic transformation) nào cũng không làm đổi nước đi tối ưu.",
            "Phát hiện toán học sâu sắc: Trong Expectiminimax, nếu ta thay đổi thang đo điểm số không theo tỷ lệ tuyến tính dương, nước đi tối ưu của MAX có thể bị lật ngược hoàn toàn từ a1 sang a2!",
            "Yêu cầu sống còn: Hàm lượng giá thế cờ Heuristic trong trò chơi ngẫu nhiên bắt buộc phải là một phép biến đổi tuyến tính dương chuẩn xác, phản ánh đúng xác suất giành chiến thắng thực tế."
        ]
    )
    
    # ----------------------------------------------------
    # 24. Slide 20: Khuyết thiếu thông tin & Bluffing
    # ----------------------------------------------------
    p_target = find_first_p(doc, 'Tập trạng thái niềm tin (Information Sets')
    insert_figure_before_p(
        doc, p_target,
        'video/Chapter06/images/slide-20.png',
        'Hình 6.15A (Slide 20): Trò chơi Khuyết thiếu thông tin (Partially Observable Games) và Kỹ năng Tung hỏa mù (Bluffing).',
        width_inches=5.8,
        expl_title="Trò chơi Khuyết thiếu thông tin và Kỹ năng Tung hỏa mù (Bluffing) (Slide 20)",
        expl_items=[
            "Ẩn thông tin: Người chơi không thể nhìn thấy toàn bộ quân bài của đối phương (như trong bài Poker). Trạng thái thực tế bị che khuất tạo thành các Tập hợp thông tin (Information sets).",
            "Sự sụp đổ của Chiến lược Thuần (Pure Strategy): Nếu AI chỉ áp dụng quy tắc cố định (bài đẹp thì cược to, bài xấu thì úp), đối thủ sẽ lập tức bắt bài và khai thác triệt để.",
            "Chiến lược Hỗn hợp (Mixed Strategy) & Cân bằng Nash: AI bắt buộc phải ngẫu nhiên hóa hành động theo một phân phối xác suất tối ưu. Đó chính là cơ sở toán học của kỹ thuật 'Bluffing' (Tung hỏa mù) - đôi khi bài xấu vẫn cược lớn để bảo vệ thông tin lá bài thật!"
        ]
    )
    
    # ----------------------------------------------------
    # 25. Hình 6.16 AIMA: Tàn cuộc cờ vua mù Kriegspiel
    # ----------------------------------------------------
    p_target = find_first_p(doc, '2. Giải thích chi tiết mã nguồn chương trình (expectiminimax)')
    insert_figure_before_p(
        doc, p_target,
        'TaiLieu/Figures/Images/figure_6.16.jpg',
        'Hình 6.16 (AIMA): Tìm kiếm chiến lược trong điều kiện khuyết thiếu thông tin - Tàn cuộc cờ vua mù Kriegspiel.',
        width_inches=5.5,
        expl_title="Tìm kiếm chiến lược trong điều kiện khuyết thiếu thông tin - Cờ vua mù Kriegspiel (Hình 6.16 AIMA)",
        expl_items=[
            "Mô hình Kriegspiel: Bàn cờ 4x4, người chơi Trắng không nhìn thấy vị trí Vua Đen. Mọi tương tác đều thông qua một trọng tài bí mật.",
            "Phản hồi của trọng tài: Khi Trắng thử đi Kc3?, trọng tài thông báo 'OK' (nước đi hợp lệ) hoặc 'Illegal' (phạm quy, ví dụ đụng quân hoặc bị cản). Khi thử Rc3?, trọng tài thông báo 'OK' hoặc 'Check' (chiếu vua).",
            "Thu hẹp Tập hợp thông tin: Mỗi câu trả lời của trọng tài giúp loại bỏ các trạng thái không phù hợp, giúp AI thu hẹp không gian niềm tin (Belief state) và xây dựng kế hoạch chiến thắng chắc chắn ngay trong bóng tối thông tin."
        ]
    )
    
    # ----------------------------------------------------
    # 26. Slide 21: Bức tranh tổng kết vinh quang toàn chương
    # ----------------------------------------------------
    # Chèn ở cuối tài liệu
    p_last = doc.paragraphs[-1]
    insert_figure_before_p(
        doc, p_last,
        'video/Chapter06/images/slide-21.png',
        'Hình 6.17 (Slide 21): Bức tranh tổng kết vinh quang - 4 thành tựu cốt lõi của Trí tuệ Nhân tạo trong Trò chơi đối kháng.',
        width_inches=5.8,
        expl_title="Bức tranh Tổng kết Vinh quang - 4 Thành tựu Cốt lõi của AI trong Trò chơi Đối kháng (Slide 21)",
        expl_items=[
            "Trụ cột 1 (Bản chất đối kháng): Môi trường đa tác tử tổng bằng không, tính chất luân phiên theo lượt và sự bùng nổ tổ hợp của không gian trạng thái.",
            "Trụ cột 2 (Quyết định tối ưu Minimax): Nền tảng toán học bảo đảm kết quả an toàn và chắc chắn nhất trước đối thủ chơi hoàn hảo.",
            "Trụ cột 3 (Cắt tỉa Alpha-Beta): Đỉnh cao tối ưu hóa giúp giảm độ phức tạp xuống O(b^(m/2)), nhân đôi độ sâu tìm kiếm trong cùng giới hạn thời gian.",
            "Trụ cột 4 (Kỷ nguyên AI hiện đại): Sự kết hợp đột phá giữa MCTS, Heuristic học máy và Mạng nơ-ron sâu đã đưa AI chinh phục những đỉnh cao bất hủ của nhân loại: Deep Blue (1997 - Cờ vua), AlphaGo (2016 - Cờ vây), và Pluribus (2019 - Poker 6 người)."
        ]
    )
    
    print(f"Saving enriched document to {docx_out}...")
    doc.save(docx_out)
    print("SUCCESS! Document generated and saved successfully.")

if __name__ == '__main__':
    main()
