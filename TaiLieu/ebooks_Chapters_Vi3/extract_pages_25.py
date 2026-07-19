import fitz
import os
import math

pdf_path = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_25_Deep learning for natural language processing.pdf"
output_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_25_Deep learning for natural language processing"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

doc = fitz.open(pdf_path)
total_pages = len(doc)
chunks = 10 # Adjust as needed based on total pages. Let's start with 10.
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
        
    out_file = os.path.join(output_dir, f"part{i+1}_25.txt")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(text)
        
    print(f"Written {out_file} (Pages {start_page} to {end_page-1})")
