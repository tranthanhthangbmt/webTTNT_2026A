import fitz
import re

pdf_path = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_26_Robotics.pdf"
doc = fitz.open(pdf_path)

text = ""
for i in range(len(doc)):
    text += doc[i].get_text()

lines = text.split('\n')
for line in lines:
    if re.match(r'^26\.\d+', line.strip()):
        print(line.strip())
