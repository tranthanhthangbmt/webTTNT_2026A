import os
import re
import google.generativeai as genai

# Kiểm tra API Key
if not os.environ.get("GEMINI_API_KEY"):
    print("Lỗi: Không tìm thấy biến môi trường GEMINI_API_KEY.")
    print("Vui lòng thiết lập biến môi trường này trước khi chạy script.")
    print("Trên Windows PowerShelL:")
    print('$env:GEMINI_API_KEY="your_api_key_here"')
    print("Hoặc sửa trực tiếp trong file này (nhưng cẩn thận không commit lên git).")
    exit(1)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3.5-flash-lite')

import time
def translate_content(text):
    prompt = """
You are an expert AI translator. Translate the following exercises from English to Vietnamese.
Rules:
1. Preserve all markdown formatting, including headers (like `##### Bài tập 1.1`), bolding, lists, and horizontal rules (`---`).
2. Preserve all HTML tags perfectly (e.g. `<a class="...">`, `<br>`, `<i>`).
3. Preserve all mathematical formulas (e.g. `$T$`, `$O(n)$`).
4. KEEP ALL ARTIFICIAL INTELLIGENCE TERMINOLOGY IN THEIR ORIGINAL ENGLISH FORM (e.g. agent, state, environment, rationality, reflex action, percept, search, node, etc.). Do not translate these.
5. Translate the rest naturally and fluently into Vietnamese.

Text to translate:
"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                prompt + text,
                generation_config=genai.types.GenerationConfig(temperature=0.1)
            )
            break
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                print(f"Rate limited. Retrying in 15 seconds... (Attempt {attempt+1}/{max_retries})")
                time.sleep(15)
            else:
                raise e

    # Loại bỏ block code markdown nếu model vô tình thêm vào
    result = response.text
    if result.startswith("```markdown"):
        result = result[len("```markdown"):]
    if result.endswith("```"):
        result = result[:-3]
    
    return result.strip() + "\n\n"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tìm đoạn nội dung từ `#### **Bài tập**` cho đến `<!-- tabs:end -->`
    match = re.search(r'(#### \*\*Bài tập\*\*\s*\n)(.*?)(<!-- tabs:end -->)', content, re.DOTALL)
    
    if match:
        prefix = match.group(1)
        exercises_text = match.group(2)
        suffix = match.group(3)

        # Bỏ qua nếu phần bài tập rỗng hoặc không có nội dung tiếng Anh (chỉ có comment)
        if len(exercises_text.strip()) < 10:
            print(f"Skipping {filepath}: Không có nội dung bài tập.")
            return

        print(f"Translating {filepath}...")
        
        try:
            translated_text = translate_content(exercises_text)
            new_content = content[:match.start()] + prefix + "\n" + translated_text + suffix + content[match.end():]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Successfully translated and updated: {filepath}")
            time.sleep(15) # Tránh rate limit của Free Tier
        except Exception as e:
            print(f"❌ Error translating {filepath}: {e}")
    else:
        print(f"Skipping {filepath}: Không tìm thấy section 'Bài tập'.")

if __name__ == "__main__":
    chapters_dir = "chapters"
    
    if not os.path.exists(chapters_dir):
        print(f"Thư mục {chapters_dir} không tồn tại!")
        exit(1)

    print("Bắt đầu dịch...")
    for filename in sorted(os.listdir(chapters_dir)):
        if filename.endswith(".md"):
            if filename in ["chapter_09_inference_in_first_order_logic.md", "chapter_20_knowledge_in_learning.md"]:
                filepath = os.path.join(chapters_dir, filename)
                process_file(filepath)
    print("Hoàn tất!")
