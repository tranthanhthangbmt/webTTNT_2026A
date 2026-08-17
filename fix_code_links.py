import os
import re

chapters_dir = 'chapters'

# Pattern matches HTML links we previously generated:
# <a href="codeAndExercises/aima-python-master/notebooks/agents.py" target="_blank" data-ignore>Agents (Python File)</a>

def replace_html_link(match):
    href = match.group(1)
    rest_of_tag = match.group(2)
    text = match.group(3)
    
    # Check if it's a python file
    if href.endswith('.py'):
        new_href = f"python_runner.html?file={href}"
        return f'<a href="{new_href}" {rest_of_tag}>{text}</a>'
    elif href.endswith('.ipynb'):
        new_href = f"https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/{href}"
        return f'<a href="{new_href}" {rest_of_tag}>{text}</a>'
    
    # For .md files, keep them as is (raw download/view in browser)
    return match.group(0)

# We also need to match the original markdown links just in case some were missed or added
def replace_md_link(match):
    text = match.group(1)
    path = match.group(2)
    path = path.split(" '")[0].strip()
    
    if path.endswith('.py'):
        new_path = f"python_runner.html?file={path}"
        return f'<a href="{new_path}" target="_blank" data-ignore>{text}</a>'
    elif path.endswith('.ipynb'):
        new_path = f"https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/{path}"
        return f'<a href="{new_path}" target="_blank" data-ignore>{text}</a>'
    else:
        return f'<a href="{path}" target="_blank" data-ignore>{text}</a>'


for filename in os.listdir(chapters_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update markdown links (if any)
        content = re.sub(r'\[(.*?)\]\((codeAndExercises/[^\)]+)\)', replace_md_link, content)
        
        # 2. Update existing HTML links to point to python_runner.html
        # <a href="(codeAndExercises/[^"]+)"([^>]*)>(.*?)</a>
        content = re.sub(r'<a href="(codeAndExercises/[^"]+)"([^>]*)>(.*?)</a>', replace_html_link, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
print("Done updating links to use python_runner.html for .py files.")
