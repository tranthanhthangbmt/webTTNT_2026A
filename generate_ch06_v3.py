# -*- coding: utf-8 -*-
"""
Script tạo file Ch06_TTNT_v3.docx (Version 3):
- Chèn chính xác toàn bộ 16 hình chuẩn từ Giáo trình AIMA (Russell & Norvig 4th Edition):
  từ Figure 6.1 đến Figure 6.16 trong TaiLieu/Figures/Images THEO ĐÚNG THỨ TỰ TĂNG DẦN 1 ĐẾN 16.
- Loại bỏ toàn bộ các bức ảnh slide không liên quan, đưa tài liệu về chuẩn sách giáo trình học thuật cao cấp.
- Mỗi hình ảnh đều đi kèm chú thích chuẩn xác và hộp giải thích trực quan (Callout Box).
- Hiệu chỉnh toàn bộ các công thức toán học bị thiếu trong văn bản gốc.
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

def insert_figure_before_p(doc, target_p, img_path, caption_text, width_inches=5.5, expl_title=None, expl_items=None):
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
    docx_out = 'video/Chapter06/Ch06_TTNT_v3.docx'
    img_dir = 'TaiLieu/Figures/Images'
    
    print(f"Loading base document {docx_in}...")
    doc = docx.Document(docx_in)
    
    print("Fixing textual and mathematical issues...")
    fix_text_and_formulas(doc)
    
    print("Injecting all 16 canonical Figure 6.X images in strict numerical order 6.1 -> 6.16...")
    
    # ----------------------------------------------------
    # 1. Hình 6.1 (figure_6.1.jpg): Cây trò chơi Tic-Tac-Toe
    # Vị trí: Mục 6.1 - Phần 1.4 Cây trò chơi, trước mục 2 (mã nguồn)
    # ----------------------------------------------------
    p_target_61 = find_first_p(doc, '2. Giải thích chi tiết mã nguồn chương trình (games.ipynb)')
    insert_figure_before_p(
        doc, p_target_61,
        f'{img_dir}/figure_6.1.jpg',
        'Hình 6.1 (AIMA): Cây trò chơi (một phần) cho trò chơi Tic-Tac-Toe (Cờ ca-rô 3x3). Nút gốc là trạng thái ban đầu, MAX đi trước đặt quân X vào ô trống; MIN đi sau đặt quân O.',
        width_inches=5.5,
        expl_title="Hướng dẫn phân tích Cây trò chơi Tic-Tac-Toe (Hình 6.1 AIMA)",
        expl_items=[
            "Cấu trúc phân tầng xen kẽ (Ply): Nút gốc là lượt của MAX (quân X có 9 lựa chọn). Tầng kế tiếp là lượt của MIN (quân O có 8 lựa chọn cho mỗi nước của MAX), tạo thành cây phân nhánh liên tục.",
            "Nút lá (Terminal Nodes): Điểm cuối của mỗi nhánh nơi trò chơi kết thúc. Hàm Utility chấm điểm: +1 nếu MAX thắng (tạo thành hàng 3 quân X), -1 nếu MIN thắng (tạo thành hàng 3 quân O), và 0 nếu hòa.",
            "Quy mô cây tìm kiếm: Tổng số nút lá trên cây đầy đủ là 9! = 362.880 nhánh (thực tế là 255.168 lá do nhiều nhánh kết thúc sớm), quy về 5.478 trạng thái bàn cờ phân biệt nhờ các phép đối xứng xoay và lật gương."
        ]
    )
    
    # ----------------------------------------------------
    # 2. Hình 6.2 (figure_6.2.jpg): Cây trò chơi 2 tầng Minimax
    # Vị trí: Mục 6.2 - Phần 1.2 Ví dụ trực quan trên Cây trò chơi 2 tầng
    # ----------------------------------------------------
    p_target_62 = find_first_p(doc, '1.3. Độ phức tạp của thuật toán')
    insert_figure_before_p(
        doc, p_target_62,
        f'{img_dir}/figure_6.2.jpg',
        'Hình 6.2 (AIMA): Cây trò chơi hai tầng (Two-ply game tree). Các nút hình tam giác hướng lên △ là nút MAX, các nút hình tam giác hướng xuống ▽ là nút MIN. Nước đi tốt nhất của MAX tại gốc là a1.',
        width_inches=5.0,
        expl_title="Hướng dẫn phân tích Cây trò chơi hai tầng Minimax (Hình 6.2 AIMA)",
        expl_items=[
            "Ý nghĩa các ký hiệu: Nút tam giác hướng lên △ biểu thị lượt đi của MAX (tìm cách tối đa hóa điểm số), nút tam giác hướng xuống ▽ biểu thị lượt đi của MIN (tìm cách ghìm điểm số xuống thấp nhất).",
            "Tầng lá (Terminal level): Các giá trị thỏa dụng Utility được biết trước cho MAX: Nhánh B có [3, 12, 8], nhánh C có [2, 4, 6], nhánh D có [14, 5, 2].",
            "Tầng của MIN (Nút B, C, D): MIN là đối thủ tối ưu nên luôn chọn nhánh có giá trị nhỏ nhất: min(3, 12, 8) = 3; min(2, 4, 6) = 2; min(14, 5, 2) = 2.",
            "Tầng gốc của MAX (Nút A): MAX chọn nước đi mang lại điểm số cao nhất trong các kịch bản tồi tệ nhất do MIN ép: max(3, 2, 2) = 3 (chọn hành động a1).",
            "Triết lý Minimax cốt lõi: Nước đi tối ưu là a1 vì nó bảo đảm MAX đạt ít nhất 3 điểm, bất kể MIN chơi hiểm hóc đến đâu. MAX không kỳ vọng vào số 14 ở nhánh D vì đối thủ thông minh sẽ không bao giờ cho phép điều đó xảy ra."
        ]
    )
    
    # ----------------------------------------------------
    # 3. Hình 6.3 (figure_6.3.jpg): Mã giả thuật toán Minimax Search
    # Vị trí: Mục 6.2 - Phần 2.1 Mã giả chuẩn (Pseudocode) và Bản chất đệ quy
    # ----------------------------------------------------
    p_target_63 = find_first_p(doc, '2.2. Giải thích từng dòng code thật dễ hiểu')
    insert_figure_before_p(
        doc, p_target_63,
        f'{img_dir}/figure_6.3.jpg',
        'Hình 6.3 (AIMA): Thuật toán Minimax chuẩn tắc (MINIMAX-SEARCH, MAX-VALUE, MIN-VALUE) tính toán nước đi tối ưu trên cây trò chơi trong giáo trình Russell & Norvig.',
        width_inches=5.2,
        expl_title="Phân tích Thuật toán Minimax đệ quy tương hỗ (Hình 6.3 AIMA)",
        expl_items=[
            "Hàm điều phối MINIMAX-SEARCH(state): Duyệt qua mọi hành động hợp lệ a ∈ ACTIONS(state), gọi MIN-VALUE(RESULT(state, a)) và trả về hành động đạt giá trị cao nhất argmax.",
            "Đệ quy tương hỗ (Mutual Recursion): MAX-VALUE duyệt qua các nhánh con, gọi MIN-VALUE và cập nhật giá trị lớn nhất v = max(v, MIN-VALUE(s')); ngược lại MIN-VALUE gọi MAX-VALUE và cập nhật v = min(v, MAX-VALUE(s')).",
            "Điều kiện neo (Base Case): Khi IS-TERMINAL(state) là True, quá trình đệ quy dừng và trả về giá trị thực sự UTILITY(state, player).",
            "Liên hệ mã nguồn Python: Thuật toán ánh xạ trực tiếp 1:1 với hàm minimax_decision(state, game) trong file games.py."
        ]
    )
    
    # ----------------------------------------------------
    # 4. Hình 6.4 (figure_6.4.jpg): Cây trò chơi 3 người chơi
    # Vị trí: Mục 6.2 - Phần 2.4 Mở rộng trò chơi nhiều người (sau phần 2.3)
    # ----------------------------------------------------
    p_target_64 = find_first_p(doc, 'Mục 6.3: Cắt tỉa Alpha–Beta')
    p_multi_head = p_target_64.insert_paragraph_before()
    p_multi_head.style = doc.styles['Heading 4']
    p_multi_head.text = "2.4. Mở rộng cho Trò chơi nhiều người (Multiplayer Games - Hình 6.4 trong sách)"
    
    p_multi_desc = p_target_64.insert_paragraph_before()
    p_multi_desc.text = "Trong giáo trình AIMA, tác giả mở rộng thuật toán Minimax từ 2 người chơi sang trò chơi n-người. Thay vì một điểm số vô hướng duy nhất, mỗi trạng thái bàn cờ được liên kết với một vector giá trị thể hiện lợi ích độc lập của từng người chơi."
    
    insert_figure_before_p(
        doc, p_target_64,
        f'{img_dir}/figure_6.4.jpg',
        'Hình 6.4 (AIMA): Ba ply đầu tiên của cây trò chơi với 3 người chơi (A, B, C). Mỗi nút được gắn nhãn với vector giá trị [vA, vB, vC] theo góc nhìn của từng người.',
        width_inches=5.5,
        expl_title="Hướng dẫn phân tích Cây trò chơi 3 người chơi (Hình 6.4 AIMA)",
        expl_items=[
            "Vector thỏa dụng [vA, vB, vC]: Trong trò chơi nhiều người, giá trị tại mỗi nút không còn là một số vô hướng mà là một vector thể hiện lợi ích của 3 người chơi A, B và C.",
            "Lựa chọn tối đa hóa vị kỷ: Đến lượt của A, A chọn nhánh có vA lớn nhất; đến lượt của B, B chọn nhánh có vB lớn nhất; đến lượt của C, C chọn nhánh có vC lớn nhất.",
            "Hiện tượng liên minh chiến thuật: Trong trò chơi đa tác tử, hai người chơi yếu thế hoàn toàn có thể bắt tay ngầm hoặc phản bội lẫn nhau để triệt hạ người chơi đang dẫn đầu, làm phát sinh động lực lý thuyết trò chơi phức tạp."
        ]
    )
    
    # ----------------------------------------------------
    # 5. Hình 6.5 (figure_6.5.jpg): 4 giai đoạn Cắt tỉa Alpha-Beta trên Fig52Game
    # Vị trí: Mục 6.3 - Phần 1.3 Ví dụ minh họa từng bước trên Hình 6.5
    # ----------------------------------------------------
    p_target_65 = find_first_p(doc, 'Xét cây trò chơi với gốc')
    insert_figure_before_p(
        doc, p_target_65,
        f'{img_dir}/figure_6.5.jpg',
        'Hình 6.5 (AIMA): Các giai đoạn tính toán quyết định tối ưu cho cây trò chơi trong Hình 6.2 bằng thuật toán cắt tỉa Alpha-Beta qua 4 bước (a), (b), (c), (d).',
        width_inches=5.8,
        expl_title="Phân tích chi tiết 4 giai đoạn cắt tỉa Alpha-Beta (Hình 6.5 AIMA)",
        expl_items=[
            "Bước (a): Duyệt xong nhánh B, xác định giá trị của B là min(3, 12, 8) = 3. Cập nhật tại gốc A: α = 3 (MAX chắc chắn đạt ít nhất 3 điểm).",
            "Bước (b): Chuyển sang nhánh C, xét lá đầu tiên có giá trị 2. Vì C là nút MIN nên giá trị của C tối đa là 2 (β ≤ 2). Khi đó β = 2 ≤ α = 3, thỏa mãn điều kiện cắt tỉa α ≥ β ⇒ Xảy ra Alpha-cutoff! Hai lá còn lại của C bị cắt bỏ hoàn toàn.",
            "Bước (c): Chuyển sang nhánh D, xét lá đầu tiên có giá trị 14. Vì 14 > α = 3 nên chưa thể cắt tỉa, tiếp tục xét lá thứ hai có giá trị 5.",
            "Bước (d): Xét lá thứ ba của D có giá trị 2, suy ra giá trị của D là min(14, 5, 2) = 2. Tại gốc, MAX chọn max(3, 2) = 3. Nước đi tối ưu là a1, hoàn toàn trùng khớp với Minimax nhưng tiết kiệm duyệt 2 lá ở nhánh C."
        ]
    )
    
    # ----------------------------------------------------
    # 6. Hình 6.6 (figure_6.6.jpg): Trường hợp tổng quát Alpha-Beta
    # Vị trí: Mục 6.3 - Ngay sau phần 1.3, trước phần 2 (mã nguồn)
    # ----------------------------------------------------
    headings_found = [p for p in doc.paragraphs if '2. Giải thích chi tiết mã nguồn chương trình (games.ipynb)'.lower() in p.text.lower()]
    p_target_66 = headings_found[2] if len(headings_found) > 2 else find_first_p(doc, '2.1. Phân tích chi tiết từng khối code')
    
    p_gen_head = p_target_66.insert_paragraph_before()
    p_gen_head.style = doc.styles['Heading 4']
    p_gen_head.text = "1.4. Trường hợp tổng quát chứng minh tính đúng đắn của Cắt tỉa Alpha-Beta (Hình 6.6 trong sách)"
    
    p_gen_desc = p_target_66.insert_paragraph_before()
    p_gen_desc.text = "Để hiểu vì sao việc bỏ qua các nhánh con không bao giờ làm thay đổi quyết định tối ưu cuối cùng, giáo trình AIMA đưa ra mô hình toán học tổng quát chứng minh rằng đối thủ sẽ luôn ngăn chặn người chơi đạt được điểm số tốt hơn cận α đã biết."
    
    insert_figure_before_p(
        doc, p_target_66,
        f'{img_dir}/figure_6.6.jpg',
        'Hình 6.6 (AIMA): Trường hợp tổng quát cho việc cắt tỉa Alpha-Beta. Nếu m hoặc m\' tốt hơn n cho Người chơi (Player), chúng ta sẽ không bao giờ đi vào n trong thực tế.',
        width_inches=4.2,
        expl_title="Chứng minh hình học tính đúng đắn của Cắt tỉa Alpha-Beta (Hình 6.6 AIMA)",
        expl_items=[
            "Nút tổ tiên: Giả sử Player tại một nút tổ tiên dọc đường đi đã có trong tay phương án chắc chắn đạt điểm số ít nhất là m.",
            "Nút đang xét: Khi Player xét nhánh con dẫn đến nút n, Opponent có một nước đi dẫn tới n' với điểm số m' ≤ m.",
            "Hệ quả logic: Opponent chắc chắn sẽ chọn nước đi dẫn tới m' để ghìm điểm Player xuống. Nhận thấy điều đó, Player sẽ không bao giờ chọn đi vào nút n.",
            "Hành động cắt tỉa: Toàn bộ các nhánh con còn lại của n bị cắt bỏ lập tức mà không cần duyệt, bảo đảm 100% tính tối ưu của quyết định cuối cùng."
        ]
    )
    
    # ----------------------------------------------------
    # 7. Hình 6.7 (figure_6.7.jpg): Mã giả thuật toán Alpha-Beta Search
    # Vị trí: Mục 6.3 - Phần 2.1 Phân tích chi tiết từng khối code
    # ----------------------------------------------------
    p_target_67 = find_first_p(doc, '2.2. Kiểm chứng trong thực tế với games.ipynb')
    insert_figure_before_p(
        doc, p_target_67,
        f'{img_dir}/figure_6.7.jpg',
        'Hình 6.7 (AIMA): Thuật toán tìm kiếm Alpha-Beta (ALPHA-BETA-SEARCH) hoàn chỉnh với việc duy trì và truyền hai cận α và β qua các lời gọi đệ quy.',
        width_inches=4.8,
        expl_title="Phân tích Thuật toán Tìm kiếm Alpha-Beta (Hình 6.7 AIMA)",
        expl_items=[
            "Khởi tạo biên: Bắt đầu với α = -∞ (cận dưới cho MAX) và β = +∞ (cận trên cho MIN).",
            "Cắt tỉa trong MAX-VALUE: Nếu giá trị con v ≥ β, hàm ngắt vòng lặp lập tức và return v (Beta-cutoff). Sau mỗi nhánh, cập nhật α = max(α, v).",
            "Cắt tỉa trong MIN-VALUE: Nếu giá trị con v ≤ α, hàm ngắt vòng lặp lập tức và return v (Alpha-cutoff). Sau mỗi nhánh, cập nhật β = min(β, v).",
            "Hiệu quả độ phức tạp: Trong trường hợp sắp xếp nước đi lý tưởng (Best Move First), độ phức tạp giảm từ O(b^m) xuống O(b^(m/2)), cho phép AI nhìn sâu gấp đôi số nước đi trong cùng thời gian."
        ]
    )
    
    # ----------------------------------------------------
    # 8. Hình 6.8 (figure_6.8.jpg): Hàm lượng giá Heuristic Cờ vua
    # Vị trí: Mục 6.4 - Phần 1.2 Hàm lượng giá Heuristic (EVAL)
    # ----------------------------------------------------
    p_target_68 = find_first_p(doc, '1.3. Hai cạm bẫy kinh điển và cách khắc phục')
    insert_figure_before_p(
        doc, p_target_68,
        f'{img_dir}/figure_6.8.jpg',
        'Hình 6.8 (AIMA): Hai vị trí cờ vua chỉ khác nhau ở vị trí quân Xe ở góc dưới bên phải. Trong (a), Đen có lợi thế hơn một Mã và hai Tốt; trong (b), Trắng sẽ thắng sau chuỗi nước đi 1. Rh8+! Kg7 2. Rxg8+ Kxg8 3. g7!.',
        width_inches=5.6,
        expl_title="Phân tích Hàm lượng giá Heuristic trong Cờ vua (Hình 6.8 AIMA)",
        expl_items=[
            "Hàm tổ hợp tuyến tính: Eval(s) = w₁f₁(s) + w₂f₂(s) + ... + wₙfₙ(s), với trọng số quân cổ điển: Tốt = 1, Mã = 3, Tượng = 3, Xe = 5, Hậu = 9.",
            "Ý nghĩa chiến thuật: Cả hai thế cờ có cùng quân số, nhưng vị trí quân Xe quyết định tất cả. Ở thế cờ (b), quân Xe Trắng chiếm cột mở kiểm soát hành lang, hỗ trợ Tốt phong Hậu không thể ngăn cản.",
            "Bài học cốt lõi: Hàm đánh giá Heuristic không thể chỉ đếm quân đơn thuần mà bắt buộc phải tính đến vị trí chiến lược, quyền kiểm soát không gian và an toàn của Vua."
        ]
    )
    
    # ----------------------------------------------------
    # 9. Hình 6.9 (figure_6.9.jpg): Hiệu ứng đường chân trời trong Cờ vua
    # Vị trí: Mục 6.4 - Phần 1.3 Cạm bẫy 2: Hiệu ứng chân trời (Horizon Effect)
    # ----------------------------------------------------
    p_target_69 = find_first_p(doc, '2. Giải thích chi tiết mã nguồn chương trình (games.ipynb / games.py)')
    insert_figure_before_p(
        doc, p_target_69,
        f'{img_dir}/figure_6.9.jpg',
        'Hình 6.9 (AIMA): Hiệu ứng đường chân trời (Horizon Effect) trong Cờ vua. Với lượt đi của Đen, Tượng đen chắc chắn bị tiêu diệt, nhưng Đen trì hoãn bằng cách thí quân Tốt chiếu Vua liên tiếp.',
        width_inches=4.8,
        expl_title="Phân tích Hiệu ứng đường chân trời (Horizon Effect) (Hình 6.9 AIMA)",
        expl_items=[
            "Bản chất hiện tượng: Khi một tổn thất lớn là không thể đảo ngược (quân Tượng đen chắc chắn bị tiêu diệt), AI bị giới hạn độ sâu sẽ tìm cách thực hiện các nước chiếu Vua vô nghĩa bằng quân Tốt.",
            "Ảo tưởng của máy tính: Các nước chiếu này đẩy thời điểm quân Tượng bị bắt vượt ra ngoài độ sâu tối đa mà máy nhìn thấy (vượt qua 'đường chân trời'). Máy tưởng rằng mình đã cứu được Tượng.",
            "Hậu quả thực tế: Vua Trắng dễ dàng tránh các nước chiếu, và cuối cùng Tượng đen vẫn bị bắt, khiến Đen mất thêm nhiều quân Tốt một cách hoàn toàn vô ích."
        ]
    )
    
    # ----------------------------------------------------
    # 10 & 11. Bổ sung Mục MCTS: Hình 6.10 & Hình 6.11 (AIMA)
    # Vị trí: Mục 6.4, trước Mục 2 (Mã nguồn)
    # ----------------------------------------------------
    p_mcts_head = p_target_69.insert_paragraph_before()
    p_mcts_head.style = doc.styles['Heading 4']
    p_mcts_head.text = "1.4. Đột phá Thời đại mới: Tìm kiếm Cây Monte Carlo (MCTS - Monte Carlo Tree Search)"
    
    p_mcts_desc = p_target_69.insert_paragraph_before()
    p_mcts_desc.text = "Trong giáo trình AIMA 4th Edition, Tìm kiếm Cây Monte Carlo (MCTS) được dành một vị trí trung tâm nhằm lý giải sự thống trị của AlphaGo trước các đại kiện tướng cờ vây nhân loại. Khi hệ số phân nhánh b quá lớn (b ≈ 250 trong cờ vây) và hàm đánh giá tĩnh không thể tính toán chính xác, MCTS giải quyết bài toán bằng cách kết hợp giữa việc mở rộng cây tìm kiếm có chọn lọc với các ván chơi mô phỏng ngẫu nhiên (rollout)."
    
    # Chèn Hình 6.10 AIMA
    insert_figure_before_p(
        doc, p_target_69,
        f'{img_dir}/figure_6.10.jpg',
        'Hình 6.10 (AIMA): Một lần lặp của quy trình chọn nước đi bằng Tìm kiếm Cây Monte Carlo (MCTS) sử dụng chỉ số UCT qua 4 giai đoạn: 1. Selection, 2. Expansion, 3. Simulation, 4. Backpropagation.',
        width_inches=5.6,
        expl_title="4 Giai đoạn cốt lõi của Thuật toán MCTS (Hình 6.10 AIMA)",
        expl_items=[
            "Thông tin tại mỗi nút Q/N: Q là số trận thắng, N là số lượt ghé thăm qua nút đó (ví dụ 37/60).",
            "1. Lựa chọn (Selection): Đi xuống cây từ gốc bằng công thức UCT = Q/N + c√(ln(N_parent)/N), giúp cân bằng hoàn hảo giữa Khai thác (Exploitation - chọn nhánh có tỷ lệ thắng cao) và Khám phá (Exploration - thử các nhánh ít được ghé thăm).",
            "2. Mở rộng (Expansion): Khi chạm tới nút chưa được mở rộng đầy đủ, chọn một hành động hợp lệ chưa thử và thêm nút con mới vào cây tìm kiếm.",
            "3. Mô phỏng (Simulation / Rollout): Từ nút con mới, tiến hành chơi ngẫu nhiên nhanh đến khi ván cờ phân định thắng bại.",
            "4. Lan truyền ngược (Backpropagation): Cập nhật kết quả thắng/thua truyền ngược lên các nút tổ tiên, tăng số lượt ghé thăm N và số trận thắng Q."
        ]
    )
    
    # Chèn Hình 6.11 AIMA
    insert_figure_before_p(
        doc, p_target_69,
        f'{img_dir}/figure_6.11.jpg',
        'Hình 6.11 (AIMA): Mã giả thuật toán Tìm kiếm Cây Monte Carlo (MCTS-SEARCH) hoàn chỉnh trong AIMA 4th Edition.',
        width_inches=5.0,
        expl_title="Mã giả thuật toán MCTS (Hình 6.11 AIMA)",
        expl_items=[
            "Vòng lặp trong quỹ thời gian: Hàm MCTS-SEARCH lặp lại liên tục chu trình 4 bước Selection -> Expansion -> Simulation -> Backpropagation cho đến khi hết thời gian tính toán cho phép.",
            "Quyết định nước đi cuối cùng: Sau khi hết thời gian, thay vì chọn nút có tỷ lệ Q/N cao nhất, thuật toán trả về nút con có số lượt ghé thăm N nhiều nhất (nước đi đã được kiểm chứng kỹ lưỡng và an toàn nhất)."
        ]
    )
    
    # ----------------------------------------------------
    # 12. Hình 6.12 (figure_6.12.jpg): Bàn cờ Thỏ cáo (Backgammon)
    # Vị trí: Mục 6.5 - Phần 1.1 Trò chơi ngẫu nhiên và Expectiminimax
    # ----------------------------------------------------
    p_target_612 = find_first_p(doc, 'Giá trị kỳ vọng (Expected Value):')
    insert_figure_before_p(
        doc, p_target_612,
        f'{img_dir}/figure_6.12.jpg',
        'Hình 6.12 (AIMA): Vị trí bàn cờ Thỏ cáo (Backgammon) điển hình. Mục tiêu là đưa toàn bộ quân cờ ra khỏi bàn. Quân Đen di chuyển theo chiều kim đồng hồ tới ô 25; quân Trắng ngược chiều kim đồng hồ về ô 0.',
        width_inches=5.0,
        expl_title="Phân tích Bàn cờ Thỏ cáo (Backgammon) (Hình 6.12 AIMA)",
        expl_items=[
            "Quy tắc xúc xắc: Mỗi lượt người chơi tung 2 con xúc xắc. Có 21 kết quả khả dĩ: 6 cặp đôi (như 6-6, 5-5) với xác suất 1/36, và 15 cặp khác nhau (như 6-5, 4-3) với xác suất 2/36 = 1/18.",
            "Hệ số phân nhánh khổng lồ: Sau khi có kết quả xúc xắc, người chơi có trung bình khoảng 20 nước đi hợp lệ. Khi tính cả biến cố xúc xắc, hệ số phân nhánh trung bình lên tới ≈ 20 × 21 ≈ 400!",
            "Thành tựu AI: Chương trình TD-Gammon của Gerald Tesauro (1992) kết hợp học tăng cường với mạng nơ-ron đã đạt trình độ đẳng cấp thế giới."
        ]
    )
    
    # ----------------------------------------------------
    # 13. Hình 6.13 (figure_6.13.jpg): Cây trò chơi Expectiminimax với nút Chance
    # Vị trí: Mục 6.5 - Phần 1.1 Giá trị kỳ vọng
    # ----------------------------------------------------
    p_target_613 = find_first_p(doc, 'Độ phức tạp: Với hệ số phân nhánh')
    insert_figure_before_p(
        doc, p_target_613,
        f'{img_dir}/figure_6.13.jpg',
        'Hình 6.13 (AIMA): Cây trò chơi sơ đồ cho vị trí bàn cờ Backgammon. Các nút tam giác △ là nút MAX, ▽ là nút MIN, và các nút hình tròn ○ là các nút ngẫu nhiên (Chance nodes).',
        width_inches=5.2,
        expl_title="Hướng dẫn phân tích Cây trò chơi Expectiminimax (Hình 6.13 AIMA)",
        expl_items=[
            "Cấu trúc cây 3 loại nút: Nút MAX (tam giác △), nút MIN (tam giác ▽) và nút ngẫu nhiên CHANCE (hình tròn ○).",
            "Cơ chế tính điểm tại nút ngẫu nhiên: Điểm số bằng tổng kỳ vọng toán học: ExpectedValue(s) = ∑ P(r) × Expectiminimax(Result(s, r)), trong đó P(r) là xác suất của biến cố xúc xắc r.",
            "Độ phức tạp tính toán: Với b là hệ số phân nhánh nước đi, m là độ sâu, và n là số biến cố ngẫu nhiên khả dĩ, độ phức tạp thời gian tăng vọt lên O(b^m × n^m)."
        ]
    )
    
    # ----------------------------------------------------
    # 14. Hình 6.14 (figure_6.14.jpg): Tính nhạy cảm Expectiminimax
    # Vị trí: Mục 6.5 - Phần 1.1 Lưu ý quan trọng về hàm EVAL
    # ----------------------------------------------------
    p_target_614 = find_first_p(doc, '1.2. Trò chơi khuyết thiếu thông tin (Mục 6.6)')
    insert_figure_before_p(
        doc, p_target_614,
        f'{img_dir}/figure_6.14.jpg',
        'Hình 6.14 (AIMA): Phép biến đổi bảo toàn thứ tự trên các giá trị nút lá làm thay đổi nước đi tốt nhất trong thuật toán Expectiminimax.',
        width_inches=5.4,
        expl_title="Phân tích Tính nhạy cảm của Expectiminimax (Hình 6.14 AIMA)",
        expl_items=[
            "Cây (a): Với thang điểm lá [1, 2, 3, 4], nhánh a1 đạt giá trị kỳ vọng là 0.5×1 + 0.5×2 = 1.5; nhánh a2 đạt giá trị kỳ vọng thấp hơn ⇒ Nước đi tối ưu là a1.",
            "Cây (b): Áp dụng phép biến đổi đơn điệu bảo toàn thứ tự y = x² (các điểm trở thành [1, 4, 9, 16]), nước đi tối ưu của MAX bị lật ngược hoàn toàn sang nhánh a2!",
            "Yêu cầu sống còn đối với hàm EVAL: Khác với Minimax thuần túy (miễn nhiễm với mọi phép biến đổi đơn điệu), trong Expectiminimax, hàm Heuristic bắt buộc phải là một phép biến đổi tuyến tính dương chuẩn xác, phản ánh đúng xác suất giành chiến thắng thực tế."
        ]
    )
    
    # ----------------------------------------------------
    # 15. Hình 6.15 (figure_6.15.jpg): Tàn cuộc cờ vua mù Kriegspiel
    # Vị trí: Mục 6.5 - Phần 1.2 Trò chơi khuyết thiếu thông tin
    # ----------------------------------------------------
    p_target_615 = find_first_p(doc, '2. Giải thích chi tiết mã nguồn chương trình (expectiminimax)')
    insert_figure_before_p(
        doc, p_target_615,
        f'{img_dir}/figure_6.15.jpg',
        'Hình 6.15 (AIMA): Một phần của chiến lược chiếu hết được bảo đảm trong tàn cuộc KRK (Vua và Xe chống Vua) trong cờ vua mù Kriegspiel trên bàn cờ thu nhỏ 4x4.',
        width_inches=5.2,
        expl_title="Phân tích Tìm kiếm chiến lược trong Cờ vua mù Kriegspiel (Hình 6.15 AIMA)",
        expl_items=[
            "Bối cảnh ẩn thông tin: Trắng không biết chính xác vị trí Vua Đen, chỉ biết Vua Đen nằm ở một trong các ô trên hàng 4. Trạng thái thực tế bị che khuất tạo thành Tập hợp thông tin (Information set / Belief state).",
            "Tương tác qua trọng tài: Khi Trắng thử đi Kc3?, trọng tài thông báo 'OK' (nước đi hợp lệ) hoặc 'Illegal' (nước đi phạm quy). Khi thử Rc3?, trọng tài thông báo 'OK' hoặc 'Check' (chiếu vua).",
            "Thu hẹp không gian niềm tin: Mỗi phản hồi của trọng tài giúp AI loại bỏ các trạng thái không phù hợp, thu hẹp Information set và thiết lập chuỗi nước đi bảo đảm chiến thắng chắc chắn ngay cả khi không nhìn thấy quân địch.",
            "Bản chất của Bluffing (Tung hỏa mù) & Cân bằng Nash: Trong trò chơi khuyết thiếu thông tin (như Poker), chiến lược thuần dễ bị bắt bài; AI bắt buộc phải chơi chiến lược hỗn hợp (Mixed Strategy) ngẫu nhiên hóa hành động theo tỷ lệ xác suất tối ưu."
        ]
    )
    
    # ----------------------------------------------------
    # 16. Hình 6.16 (figure_6.16.jpg): Cây trò chơi lỗi Heuristic cạn
    # Vị trí: Cuối Mục 6.5, phần đúc kết chuyên sâu
    # ----------------------------------------------------
    p_last = doc.paragraphs[-1]
    
    p_app_head = p_last.insert_paragraph_before()
    p_app_head.style = doc.styles['Heading 4']
    p_app_head.text = "2.4. Phụ lục phân tích chuyên sâu: Cạm bẫy hàm lượng giá Heuristic không tĩnh lặng (Hình 6.16 trong sách AIMA)"
    
    p_app_desc = p_last.insert_paragraph_before()
    p_app_desc.text = "Để đúc kết lại các rủi ro cốt tử khi xây dựng AI chơi cờ vua, giáo trình AIMA đưa ra Hình 6.16 như một minh họa toán học kinh điển cho thấy việc dừng tìm kiếm đột ngột ở trạng thái chưa ổn định sẽ khiến hàm lượng giá đánh giá hoàn toàn sai lệch thế trận."
    
    insert_figure_before_p(
        doc, p_last,
        f'{img_dir}/figure_6.16.jpg',
        'Hình 6.16 (AIMA): Cây trò chơi hai tầng mà Heuristic Minimax có thể mắc sai lầm nghiêm trọng do đánh giá tĩnh tại điểm cắt độ sâu khi trạng thái bàn cờ chưa tĩnh lặng (non-quiescent).',
        width_inches=4.8,
        expl_title="Đúc kết về Cạm bẫy Tìm kiếm cạn và Tìm kiếm tĩnh lặng (Hình 6.16 AIMA)",
        expl_items=[
            "Cạm bẫy không tĩnh lặng (Non-quiescent): Nếu cắt độ sâu tìm kiếm đúng lúc Xe trắng vừa ăn một quân của Đen, hàm Heuristic thấy Trắng hơn điểm (+5) và tưởng rằng đây là nước đi tuyệt hảo.",
            "Hiểm họa nhãn tiền: Ngay nước sau đó, Đen dùng Hậu bắt lại Xe Trắng (-9 điểm), biến chiến thắng ảo thành thất bại nặng nề.",
            "Giải pháp - Tìm kiếm tĩnh lặng (Quiescence Search): Tại điểm cắt độ sâu, nếu bàn cờ chưa ổn định (còn các nước ăn quân hoặc chiếu tướng), AI không được dừng lại mà phải mở rộng thêm các nước giao tranh cho tới khi bàn cờ thực sự yên tĩnh mới gọi hàm Eval."
        ]
    )
    
    print(f"Saving Version 3 document to {docx_out}...")
    doc.save(docx_out)
    print("SUCCESS! Version 3 created successfully with all 16 canonical figures in strict 1->16 order!")

if __name__ == '__main__':
    main()
