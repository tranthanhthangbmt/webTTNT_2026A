import bs4
import sys

soup = bs4.BeautifulSoup(open('chapter_03_vi.html', encoding='utf-8').read(), 'html.parser')
for i, img in enumerate(soup.find_all('img')):
    src = img.get("src", "").split("/")[-1]
    prev_text = [s.get_text(strip=True) for s in img.find_all_previous(string=True) if s.strip()][:2]
    next_text = [s.get_text(strip=True) for s in img.find_all_next(string=True) if s.strip()][:3]
    print(f"[{i}] {src}: Prev={prev_text}, Next={next_text}")
