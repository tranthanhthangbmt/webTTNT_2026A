import os

def merge_html_parts(input_dir, output_file, num_parts):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i in range(1, num_parts + 1):
            part_file = os.path.join(input_dir, f'part{i}_28.html')
            if os.path.exists(part_file):
                with open(part_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(f"<!-- Part {i} -->\n")
                    outfile.write(content)
                    outfile.write("\n\n")
            else:
                print(f"Warning: {part_file} not found.")
    print(f"Merged {num_parts} parts into {output_file}")

if __name__ == "__main__":
    input_directory = "Chapter_28_Philosophy, ethics, and safety of AI"
    output_filename = "chapter_28_vi.html"
    output_path = os.path.join(input_directory, output_filename)
    merge_html_parts(input_directory, output_path, 8)
