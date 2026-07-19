import os

def merge_html_files():
    chapter_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_27_Computer Vision"
    output_file = os.path.join(chapter_dir, "chapter_27.html")

    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chương 27: Thị giác máy tính (Computer Vision)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            text-align: justify;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        p {
            margin-bottom: 15px;
        }
        .math {
            font-family: "Times New Roman", Times, serif;
            font-style: italic;
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
    </style>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
"""

    for i in range(1, 10):
        part_file = os.path.join(chapter_dir, f"part{i}_27.html")
        if os.path.exists(part_file):
            with open(part_file, "r", encoding="utf-8") as f:
                html_content += f.read() + "\n"
        else:
            print(f"Warning: {part_file} not found.")

    html_content += """</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Merged successfully into {output_file}")

if __name__ == "__main__":
    merge_html_files()
