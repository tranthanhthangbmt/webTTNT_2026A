import os
import re
import google.generativeai as genai
import time
from dotenv import load_dotenv

# Tự động load biến môi trường từ file .env (nếu có)
load_dotenv()

# Kiểm tra API Key
if not os.environ.get("GEMINI_API_KEY"):
    print("Lỗi: Không tìm thấy biến môi trường GEMINI_API_KEY.")
    print("Cách khắc phục (Tuyệt đối KHÔNG hardcode key vào file Python):")
    print("1. Tạo một file tên là `.env` ở cùng thư mục với script này.")
    print("2. Mở file `.env` và thêm dòng sau:")
    print("   GEMINI_API_KEY=điền_api_key_của_bạn_vào_đây")
    print("Lưu ý: File .env đã được thêm vào .gitignore nên sẽ an toàn, không bị đẩy lên GitHub.")
    exit(1)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3.5-flash-lite')

def translate_chunk(text):
    if not text.strip(): return ""
    prompt = """
You are an expert AI translator. Translate the following exercises from English to Vietnamese.
Rules:
1. Preserve all markdown formatting, including headers (like `##### Bài tập 1.1`), bolding, lists, and horizontal rules (`---`).
2. Preserve all HTML tags perfectly (e.g. `<a class="...">`, `<br>`, `<i>`).
3. Preserve all mathematical formulas (e.g. `$T$`, `$O(n)$`).
4. KEEP ALL ARTIFICIAL INTELLIGENCE TERMINOLOGY IN THEIR ORIGINAL ENGLISH FORM (e.g. agent, state, environment, rationality, reflex action, percept, search, node, etc.). Do not translate these.
5. Translate the rest naturally and fluently into Vietnamese.
6. Return ONLY the translated text, with no introductory or conversational text like 'Here is the translation'.

Text to translate:
"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                prompt + text,
                generation_config=genai.types.GenerationConfig(temperature=0.1)
            )
            result = response.text
            if result.startswith("```markdown"):
                result = result[len("```markdown"):]
            if result.endswith("```"):
                result = result[:-3]
            return result.strip() + "\n"
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                print(f"Rate limited. Retrying in 15 seconds... (Attempt {attempt+1}/{max_retries})")
                time.sleep(15)
            else:
                print(f"Error on chunk: {e}")
                return text # Fallback to original
    return text

def process_file(filepath):
    print(f"Translating {filepath} in chunks...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'(#### \*\*Bài tập\*\*\s*\n)(.*?)(<!-- tabs:end -->)', content, re.DOTALL)
    if not match: return
    prefix = match.group(1)
    exercises_text = match.group(2)
    suffix = match.group(3)

    # Split by `##### Bài tập`
    chunks = re.split(r'(##### Bài tập \d+\.\d+)', exercises_text)
    
    translated_text = ""
    # chunk[0] is the preamble (if any) before the first exercise
    if chunks[0].strip():
        print(f"Translating preamble...")
        translated_text += translate_chunk(chunks[0]) + "\n"
        time.sleep(4)
        
    for i in range(1, len(chunks), 2):
        header = chunks[i]
        body = chunks[i+1]
        print(f"Translating {header.strip()}...")
        translated_body = translate_chunk(body)
        translated_text += "\n" + header + "\n" + translated_body + "\n"
        time.sleep(4) # Respect rate limits (15 RPM)
        
    new_content = content[:match.start()] + prefix + "\n" + translated_text + suffix + content[match.end():]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Successfully translated and updated: {filepath}")

if __name__ == "__main__":
    process_file("chapters/chapter_09_inference_in_first_order_logic.md")
    process_file("chapters/chapter_20_knowledge_in_learning.md")
