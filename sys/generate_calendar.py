import sys
from collections import defaultdict

def generate_calendar(index_file, output_file):
    with open(index_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    articles = []
    current_group = "Uncategorized"

    for line in lines:
        line = line.strip()
        if line.startswith('## '):
            current_group = line[3:].strip()
            continue
            
        if line.startswith('|') and '---' not in line and 'Title' not in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 8:
                title = parts[2]
                if not title:
                    continue
                # For "Other", keyword is col 3, link is col 4, buyer stage col 5, summary col 6, est views col 7
                if current_group == "Other" and len(parts) >= 9:
                    group = parts[3]
                    link = parts[4]
                    buyer_stage = parts[5]
                    summary = parts[6]
                    est_views = parts[7]
                else:
                    group = current_group
                    link = parts[3]
                    buyer_stage = parts[4] if len(parts) > 4 else ""
                    summary = parts[5] if len(parts) > 5 else ""
                    est_views = parts[6] if len(parts) > 6 else ""
                
                # Verify if it's a real row
                if parts[1].isdigit():
                    articles.append({
                        'title': title, 
                        'group': group, 
                        'link': link,
                        'buyer_stage': buyer_stage,
                        'summary': summary,
                        'est_views': est_views
                    })

    # Group by category to mix them
    grouped_articles = defaultdict(list)
    for a in articles:
        grouped_articles[a['group']].append(a)
        
    mixed_articles = []
    while grouped_articles:
        keys_to_remove = []
        for k in list(grouped_articles.keys()):
            mixed_articles.append(grouped_articles[k].pop(0))
            if not grouped_articles[k]:
                keys_to_remove.append(k)
        for k in keys_to_remove:
            del grouped_articles[k]

    months = ["Tháng 7/2026", "Tháng 8/2026", "Tháng 9/2026", "Tháng 10/2026", "Tháng 11/2026", "Tháng 12/2026", 
              "Tháng 1/2027", "Tháng 2/2027", "Tháng 3/2027", "Tháng 4/2027", 
              "Tháng 5/2027", "Tháng 6/2027", "Tháng 7/2027", "Tháng 8/2027", "Tháng 9/2027", "Tháng 10/2027", "Tháng 11/2027", "Tháng 12/2027"]
              
    out_lines = ["# Content Calendar\n\n"]
    
    month_idx = 0
    for i in range(0, len(mixed_articles), 60):
        chunk = mixed_articles[i:i+60]
        month_name = months[month_idx] if month_idx < len(months) else f"Tháng {month_idx+7} (?)"
        out_lines.append(f"## {month_name}\n")
        out_lines.append(f"**Số lượng bài viết:** {len(chunk)}\n\n")
        out_lines.append("| No. | Title | Group / Keyword | File Link | Buyer Stage | Summary | Est. Views |\n")
        out_lines.append("|---|---|---|---|---|---|---|\n")
        for j, article in enumerate(chunk, 1):
            out_lines.append(f"| {j} | {article['title']} | {article['group']} | {article['link']} | {article['buyer_stage']} | {article['summary']} | {article['est_views']} |\n")
        out_lines.append("\n")
        month_idx += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"Calendar generated with {len(mixed_articles)} articles over {month_idx} months.")

if __name__ == "__main__":
    generate_calendar('/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/LONG_ARTICLES_INDEX.md', 
                      '/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/content_calendar.md')
