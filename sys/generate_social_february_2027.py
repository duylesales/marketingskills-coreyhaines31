import re
import os
import random

with open("content_calendar.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
in_target_month = False

templates = [
    """🚀 **{title}**

💡 {summary}

For Tech Leaders, Founders, and PMs, this article dives deep into the core issues you can't afford to ignore.

👉 Read the full breakdown here: {link}

#SoftwareDevelopment #TechLeadership #B2B #Engineering #OffshoreDevelopment
""",
    """🔥 The hard truth about tech: **{title}**

📌 {summary}

Discover the in-depth strategies and enterprise-grade solutions in our latest article.

👉 Check out the full article: {link}

#TechStrategy #SoftwareEngineering #B2B #TechInsights
""",
    """🌟 **{title}**

Have you ever faced this challenge?
👉 {summary}

Let's dive into how to solve this effectively in our comprehensive analysis.

👉 Read more at: {link}

#CustomSoftware #TechLeadership #Innovation #SoftwareArchitecture
"""
]

count = 0

for line in lines:
    if line.startswith("## Tháng 2/2027"):
        in_target_month = True
    elif line.startswith("## Tháng ") and "2/2027" not in line:
        in_target_month = False

    if in_target_month and line.strip().startswith("|") and "No." not in line and "---" not in line:
        parts = line.split("|")
        # We expect Link Bài Social to be at parts[5]
        if len(parts) > 8:
            title = parts[2].strip()
            title = title.replace("✅", "").strip()
            file_link_md = parts[4].strip()
            summary = parts[7].strip()

            if "](" in file_link_md:
                original_path = file_link_md.split("](", 1)[1].rstrip(")").strip()
                base, ext = os.path.splitext(original_path)
                new_path = f"{base}_blog{ext}"
                
                template = random.choice(templates)
                content = template.format(
                    title=title,
                    summary=summary,
                    link="https://manifera.com" + original_path.replace("./blog/", "/insights/")
                )
                
                write_path = new_path
                if write_path.startswith("./"):
                    write_path = write_path[2:]
                    
                with open(write_path, "w", encoding="utf-8") as f_out:
                    f_out.write(content)
                count += 1
                
                parts[5] = f" [{os.path.basename(new_path)}]({new_path}) "
            
            out_lines.append("|".join(parts))
        else:
            out_lines.append(line)
    else:
        out_lines.append(line)

with open("content_calendar.md", "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print(f"Done generating {count} social posts for February 2027 and updating content_calendar.md!")
