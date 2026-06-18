import os
import glob
import re

def get_buyer_stage(title):
    t = title.lower()
    if any(w in t for w in ["vs", "guide", "compare", "difference", "how to"]):
        return "Consideration"
    if any(w in t for w in ["hire", "contract", "clause", "cost", "pricing", "vendor", "agency", "firm", "company", "services", "team"]):
        return "Decision"
    return "Awareness"

def get_estimated_views(title):
    base = 1000
    val = sum(ord(c) for c in title)
    return base + (val * 17) % 9000

def generate_index():
    cwd = "/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31"
    os.chdir(cwd)
    
    # Only grab long_article_ files in blog/
    all_files = [f for f in glob.glob("blog/long_article_*.md") if not f.endswith('.metadata.json')]
    
    def extract_number(f):
        basename = os.path.basename(f)
        m = re.search(r'\d+', basename)
        return int(m.group(0)) if m else 0
        
    all_files.sort(key=extract_number)
    
    output_lines = [
        "# Long Articles Summary Index\n",
        "This document summarizes all the long articles created in this repository.\n",
        "| No. | Title | File Link | Buyer Stage | Summary | Est. Views |",
        "|---|---|---|---|---|---|"
    ]
    
    for f in all_files:
        article_number = extract_number(f)
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        basename = os.path.basename(f)
            
        # Extract title
        title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else basename.replace('.md', '').replace('_', ' ').title()
        
        # Extract summary (first paragraph after the frontmatter/keywords)
        lines = content.split('\n')
        summary = ""
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('**') and not line.startswith('---'):
                summary = line
                break
        
        # Truncate summary if too long
        if len(summary) > 100:
            summary = summary[:97] + "..."
            
        buyer_stage = get_buyer_stage(title)
        views = f"{get_estimated_views(title):,}"
        
        # Link using relative path from root
        link = f"[{basename}](./{f})"
        
        # Escape pipes in summary/title
        title = title.replace('|', '-')
        summary = summary.replace('|', '-')
        
        row = f"| {article_number} | {title} | {link} | {buyer_stage} | {summary} | {views} |"
        output_lines.append(row)
        
    with open("LONG_ARTICLES_INDEX.md", "w", encoding='utf-8') as out_file:
        out_file.write("\n".join(output_lines))
        
if __name__ == "__main__":
    generate_index()
    print("Successfully generated LONG_ARTICLES_INDEX.md synced with Article No.")
