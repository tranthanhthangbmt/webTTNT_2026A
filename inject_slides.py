import os
import re
import glob

def inject_slides():
    chapters_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\chapters'
    slides_md_dir = r'd:\DongAUniversity\TÀI LIỆU DẠY HỌC_2024-2025\Trí tuệ nhân tạo_UDA_2025\webTTNT_2026\TaiLieu\slide_md'
    
    chapter_files = glob.glob(os.path.join(chapters_dir, 'chapter_*.md'))
    
    for chapter_file in chapter_files:
        basename = os.path.basename(chapter_file)
        # Extract chapter number, e.g., '01' from 'chapter_01_introduction.md'
        match = re.search(r'chapter_(\d+)_', basename)
        if not match:
            continue
        chapter_num = match.group(1)
        
        # Find matching slides. E.g., for chapter 04, match chapter04a.md, chapter04b.md, chapter04.md
        slide_pattern = os.path.join(slides_md_dir, f'chapter{chapter_num}*.md')
        slide_files = sorted(glob.glob(slide_pattern))
        
        if not slide_files:
            continue
            
        # Read all matched slide files
        slide_content = ''
        for sfile in slide_files:
            with open(sfile, 'r', encoding='utf-8') as sf:
                slide_content += sf.read() + '\n\n'
                
        # Read the chapter file
        with open(chapter_file, 'r', encoding='utf-8') as cf:
            content = cf.read()
            
        # Replace the content between #### **Slide** and the next #### **
        # Wait, the structure is usually:
        # #### **Slide**
        # *(Chưa có slide)*
        # #### **Trắc nghiệm**
        
        # Regex to match the section
        # We need to replace everything after #### **Slide** until the next #### ** or <!-- tabs:end -->
        pattern = re.compile(r'(#### \*\*Slide\*\*\n)(.*?)(?=\n#### \*\*|\n<!-- tabs:end -->)', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(r'\1' + '\n' + slide_content.replace('\\', '\\\\') + '\n', content)
            
            with open(chapter_file, 'w', encoding='utf-8') as cf:
                cf.write(new_content)
            print(f"Injected slides into {basename}")
        else:
            print(f"Could not find #### **Slide** section in {basename}")

if __name__ == '__main__':
    inject_slides()
