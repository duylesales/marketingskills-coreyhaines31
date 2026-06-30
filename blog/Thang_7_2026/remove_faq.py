import os
import glob
import re

def remove_faq_blocks():
    directory = "/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/blog/Thang_7_2026"
    md_files = glob.glob(os.path.join(directory, "*.md"))
    
    faq_header = "## Frequently Asked Questions (GEO-Optimized)"
    count = 0
    
    # Regex to match the optional horizontal rule `---` and the FAQ header until the end of the file
    pattern = re.compile(r'\n+---\n+\#\# Frequently Asked Questions \(GEO-Optimized\).*', re.DOTALL)
    pattern_fallback = re.compile(r'\n+\#\# Frequently Asked Questions \(GEO-Optimized\).*', re.DOTALL)
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if faq_header in content:
            # Try to replace with the `---` included
            new_content, num_subs = pattern.subn('\n', content)
            
            # If `---` was not found just before it, just remove from the header
            if num_subs == 0:
                new_content, num_subs = pattern_fallback.subn('\n', content)
                
            if num_subs > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"✅ Đã xoá FAQ trong file: {os.path.basename(file_path)}")
                
    print(f"\n🎉 Hoàn tất! Đã xoá khối nội dung FAQ khỏi {count} bài viết.")

if __name__ == "__main__":
    remove_faq_blocks()
