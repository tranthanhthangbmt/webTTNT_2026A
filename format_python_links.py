import os
import re

chapters_dir = 'chapters'

def process_python_section(match):
    header = match.group(1) # "#### **Python**"
    body = match.group(2)   # The content
    
    link_pattern = re.compile(r'- <a href="([^"]+)"[^>]*>(.*?)</a>')
    links = link_pattern.findall(body)
    
    if not links:
        return match.group(0)
        
    topics = {}
    for href, text in links:
        if "colab.research.google.com" not in href:
            continue
            
        try:
            rel_path = href.split('/blob/main/')[1]
            base_path = rel_path.rsplit('.', 1)[0]
            title = text.replace(' (Python File)', '').strip()
            
            if title not in topics:
                topics[title] = base_path
        except IndexError:
            continue
            
    if not topics:
        return match.group(0)
        
    new_body = "\n"
    for title, base_path in topics.items():
        colab_link = f"https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/{base_path}.ipynb"
        py_download = f"{base_path}.py"
        ipynb_download = f"{base_path}.ipynb"
        
        line = f"- **{title}**: <a href=\"{colab_link}\" target=\"_blank\">Mở trên Colab</a> | <a href=\"{py_download}\" download>Tải .py</a> | <a href=\"{ipynb_download}\" download>Tải .ipynb</a>\n"
        new_body += line
        
    # preserve any extra trailing newlines in the original body
    trailing_newlines = len(body) - len(body.rstrip('\n'))
    new_body += '\n' * trailing_newlines
    
    return header + new_body

for filename in os.listdir(chapters_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(r'(#### \*\*Python\*\*)(.*?)(?=#### \*\*|\Z)', process_python_section, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Formatting complete!")
