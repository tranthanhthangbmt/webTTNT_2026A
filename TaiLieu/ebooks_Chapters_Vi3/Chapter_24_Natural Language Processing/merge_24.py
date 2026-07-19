import os

base_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_24_Natural Language Processing"
output_file = os.path.join(base_dir, "chapter_24_vi.html")

num_parts = 11

with open(output_file, "w", encoding="utf-8") as outfile:
    for i in range(1, num_parts + 1):
        part_file = os.path.join(base_dir, f"part{i}_24.html")
        if os.path.exists(part_file):
            with open(part_file, "r", encoding="utf-8") as infile:
                outfile.write(f"<!-- PART {i} -->\n")
                outfile.write(infile.read())
                outfile.write("\n\n")
            print(f"Merged {part_file}")
        else:
            print(f"Warning: {part_file} not found")

print("Merge complete!")
