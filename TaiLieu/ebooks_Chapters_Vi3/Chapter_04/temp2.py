import bs4
import re

soup = bs4.BeautifulSoup(open('chapter_04_vi.html', encoding='utf-8').read(), 'html.parser')
for i, img in enumerate(soup.find_all('img')):
    src = img.get("src", "").split("/")[-1]
    # Find the next text that looks like "Hình 3.X" or "Figure 3.X"
    caption_text = ""
    for s in img.find_all_next(string=True):
        s = s.strip()
        if not s: continue
        if re.search(r'(Hình|Figure)\s*3\.\d+', s, re.IGNORECASE):
            caption_text = s
            break
        
    # If not found immediately, just get the next 2 strings
    if not caption_text:
        caption_text = " ".join([s.strip() for s in img.find_all_next(string=True) if s.strip()][:3])
    else:
        # Get the next few strings after the "Hình 3.X"
        node = img.find_next(string=re.compile(r'(Hình|Figure)\s*3\.\d+', re.IGNORECASE))
        if node:
            parts = [node.strip()]
            for _ in range(3):
                node = node.find_next(string=True)
                if node and node.strip():
                    parts.append(node.strip())
            caption_text = " ".join(parts)

    print(f"* {src}: {caption_text}")
