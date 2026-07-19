import glob
import re

files = glob.glob(r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_27_Computer Vision\part*.txt")

pattern = re.compile(r'^(27\.\d+(?:\.\d+)?\s+.*|Summary|Bibliographical and Historical Notes)$')

for f in sorted(files):
    print(f"\n--- {f} ---")
    with open(f, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                print(line)
