import re
import os
import random

with open("content_calendar.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
in_july = False

templates = [
    """🚀 **{title}**

💡 {summary}

Dành cho các nhà lãnh đạo công nghệ và quản lý dự án, bài viết này sẽ đi sâu vào những vấn đề cốt lõi mà bạn không thể bỏ qua.

👉 Đọc ngay bài viết chi tiết: {link}

#SoftwareDevelopment #TechLeadership #B2B #Engineering
""",
    """🔥 Vấn đề nan giải trong công nghệ: **{title}**

📌 {summary}

Khám phá ngay các chiến lược và giải pháp chuyên sâu dành cho Enterprise trong bài viết mới nhất của chúng tôi.

👉 Link bài viết: {link}

#TechStrategy #SoftwareEngineering #B2B #TechInsights
""",
    """🌟 **{title}**

Bạn đã bao giờ gặp phải thách thức này chưa?
👉 {summary}

Cùng tìm hiểu cách giải quyết bài toán này triệt để trong bài phân tích chuyên sâu dưới đây.

👉 Xem chi tiết tại: {link}

#CustomSoftware #TechLeadership #Innovation #SoftwareArchitecture
"""
]

for line in lines:
    if "## Tháng 7/2026" in line:
        in_july = True
    elif "## Tháng 8/2026" in line:
        in_july = False

    if line.strip().startswith("|") and "No." in line and "Title" in line:
        # Header
        parts = line.split("|")
        parts.insert(5, " Link Bài Social ")
        out_lines.append("|".join(parts))
    elif line.strip().startswith("|") and "---" in line:
        # Separator
        parts = line.split("|")
        parts.insert(5, " --- ")
        out_lines.append("|".join(parts))
    elif line.strip().startswith("|"):
        # Data row
        parts = line.split("|")
        if len(parts) > 7:
            if in_july:
                title = parts[2].strip()
                title = title.replace("✅", "").strip()
                file_link_md = parts[4].strip()
                summary = parts[6].strip()

                # Extract file path from markdown link [text](path)
                match = re.search(r"\]\((.*?)\)", file_link_md)
                if match:
                    original_path = match.group(1) # e.g. ./blog/long_article_3_enterprise_mobile_security.md
                    # new file path
                    base, ext = os.path.splitext(original_path)
                    new_path = f"{base}_blog{ext}"
                    
                    # Generate content
                    template = random.choice(templates)
                    content = template.format(
                        title=title,
                        summary=summary,
                        link="https://manifera.com" + original_path.replace("./blog/", "/insights/") # fake public link for social
                    )
                    
                    # Write to file
                    # We need to resolve the path relative to the current directory
                    write_path = new_path
                    if write_path.startswith("./"):
                        write_path = write_path[2:]
                        
                    with open(write_path, "w", encoding="utf-8") as f_out:
                        f_out.write(content)
                        
                    # Add to table
                    parts.insert(5, f" [{os.path.basename(new_path)}]({new_path}) ")
                else:
                    parts.insert(5, " ")
            else:
                parts.insert(5, " ")
            out_lines.append("|".join(parts))
        else:
            out_lines.append(line)
    else:
        out_lines.append(line)

with open("content_calendar.md", "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print("Done generating 60 social posts and updating content_calendar.md!")
