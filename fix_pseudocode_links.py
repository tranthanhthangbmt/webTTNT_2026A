import os
import re

chapters_dir = 'chapters'

def replace_pseudocode_link(match):
    path = match.group(1)
    text = match.group(2)
    return f'<a href="#/{path}" target="_blank">{text}</a>'

for filename in os.listdir(chapters_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = re.sub(r'<a href="(codeAndExercises/aima-pseudocode-master/md/[^"]+)"\s*target="_blank"\s*data-ignore>(.*?)</a>', replace_pseudocode_link, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Pseudocode links updated to Docsify routes!")
