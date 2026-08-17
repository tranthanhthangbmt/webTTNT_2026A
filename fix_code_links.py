import os
import re

chapters_dir = 'chapters'

def replace_html_link(match):
    href = match.group(1)
    rest_of_tag = match.group(2)
    text = match.group(3)
    
    if href.endswith('.py'):
        href = href[:-3] + '.ipynb'
        
    if href.endswith('.ipynb'):
        new_href = f"https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/{href}"
        return f'<a href="{new_href}" {rest_of_tag}>{text}</a>'
    
    return match.group(0)

def replace_md_link(match):
    text = match.group(1)
    path = match.group(2)
    path = path.split(" '")[0].strip()
    
    if path.startswith('python_runner.html?file='):
        path = path.replace('python_runner.html?file=', '')
        
    if path.endswith('.py'):
        path = path[:-3] + '.ipynb'
        
    if path.endswith('.ipynb'):
        new_path = f"https://colab.research.google.com/github/tranthanhthangbmt/webTTNT_2026A/blob/main/{path}"
        return f'<a href="{new_path}" target="_blank" data-ignore>{text}</a>'
    else:
        return f'<a href="{path}" target="_blank" data-ignore>{text}</a>'

for filename in os.listdir(chapters_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update markdown links
        content = re.sub(r'\[(.*?)\]\((python_runner\.html\?file=codeAndExercises/[^\)]+|codeAndExercises/[^\)]+)\)', replace_md_link, content)
        
        # 2. Update existing HTML links
        content = re.sub(r'<a href="(?:python_runner\.html\?file=)?(codeAndExercises/[^"]+)"([^>]*)>(.*?)</a>', replace_html_link, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
print("Done converting .py links to .ipynb Colab links.")
