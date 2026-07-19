import fitz
import os
import math

pdf_path = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_26_Robotics.pdf"
output_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_26_Robotics"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

doc = fitz.open(pdf_path)
total_pages = len(doc)
chunks = 11 # 56 pages -> ~5 pages per chunk
pages_per_chunk = math.ceil(total_pages / chunks)

print(f"Total pages: {total_pages}. Dividing into {chunks} chunks, approx {pages_per_chunk} pages per chunk.")

for i in range(chunks):
    start_page = i * pages_per_chunk
    end_page = min((i + 1) * pages_per_chunk, total_pages)
    
    if start_page >= total_pages:
        break
        
    text = ""
    for page_num in range(start_page, end_page):
        page = doc[page_num]
        text += page.get_text() + "\n\n"
        
    out_file = os.path.join(output_dir, f"part{i+1}_26.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(text)
        
    print(f"Written {out_file} (Pages {start_page} to {end_page-1})")
