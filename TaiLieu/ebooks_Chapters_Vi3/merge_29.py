import os

def merge_html_files():
    base_dir = r"D:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\ebooks_Chapters_Vi3\Chapter_29_The future of AI"
    
    parts = [
        "part1_29.html",
        "part2_29.html",
        "part3_29.html"
    ]
    
    merged_content = ""
    for part in parts:
        file_path = os.path.join(base_dir, part)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                merged_content += f.read() + "\n"
        else:
            print(f"File not found: {file_path}")

    # Wrap the merged content in a proper HTML skeleton
    html_skeleton = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 29: The future of AI</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }}
        h1, h2, h3 {{
            color: #2c3e50;
        }}
        p {{
            text-align: justify;
            margin-bottom: 15px;
        }}
        img {{
            display: block;
            margin: 20px auto;
            max-width: 100%;
            height: auto;
        }}
    </style>
    <!-- MathJax for rendering math equations -->
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            }}
        }};
    </script>
</head>
<body>
{merged_content}
</body>
</html>
"""

    output_file = os.path.join(base_dir, "chapter_29_vi.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_skeleton)
        
    print(f"Merged parts into {output_file}")

if __name__ == "__main__":
    merge_html_files()
