import re
import os
import random

with open("content_calendar.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

in_july = False

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
    if "## Tháng 7/2026" in line:
        in_july = True
    elif "## Tháng 8/2026" in line:
        in_july = False

    if in_july and line.strip().startswith("|"):
        parts = line.split("|")
        # In our previous update, we added Link Bài Social at index 5.
        # Header: | No. | Title | Group / Keyword | File Link | Link Bài Social | Buyer Stage | Summary | Est. Views |
        # So len is 10 (empty, no, title, group, file_link, social_link, buyer, summary, est_views, empty)
        if len(parts) > 8 and "No." not in line and "---" not in line:
            title = parts[2].strip()
            title = title.replace("✅", "").strip()
            file_link_md = parts[4].strip()
            # Because we added social_link at index 5, buyer stage is 6, summary is 7
            # Let's double check if summary is at index 7. Wait, previously summary was 6 before insertion, now it should be 7.
            # But let's just find the file link and summary properly.
            # Parts after split: 
            # 0: 
            # 1: No.
            # 2: Title
            # 3: Group
            # 4: File Link
            # 5: Link Bài Social
            # 6: Buyer Stage
            # 7: Summary
            # 8: Est. Views
            # 9: 
            summary = parts[7].strip()

            match = re.search(r"\]\((.*?)\)", file_link_md)
            if match:
                original_path = match.group(1)
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
                    
                if os.path.exists(write_path):
                    with open(write_path, "w", encoding="utf-8") as f_out:
                        f_out.write(content)
                    count += 1

print(f"Done translating {count} social posts to English!")
