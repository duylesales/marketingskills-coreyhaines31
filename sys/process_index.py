import re
import sys

def process_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header_lines = []
    table_header = []
    rows = []
    
    in_table = False
    for line in lines:
        if line.strip().startswith('| No. |') or line.strip().startswith('| --- |'):
            table_header.append(line)
            in_table = True
        elif in_table and line.strip().startswith('|'):
            rows.append(line)
        elif not in_table:
            header_lines.append(line)
            
    # Keywords to categorize
    keywords = {
        'Mobile App': ['mobile app', 'ios', 'android', 'cross-platform', 'native'],
        'Web Development': ['web app', 'web develop', 'pwa', 'ecommerce', 'frontend', 'seo'],
        'Software Outsourcing': ['outsource', 'outsourcing', 'vendor', 'offshore', 'nearshore', 'staff augmentation'],
        'Custom Software': ['custom software', 'bespoke', 'build vs', 'buy vs'],
        'Team & Engineering Culture': ['agile', 'developer myth', 'hiring', 'interview', '10x developer', 't-shaped', 'conway', 'bus factor', 'communication'],
        'Architecture & Cloud': ['architecture', 'cloud', 'aws', 'microservices', 'monolithic', 'multitenancy', 'ddd', 'domain-driven', 'caching', 'state management'],
        'Security & Compliance': ['security', 'compliance', 'gdpr', 'hipaa', 'iam', 'soc 2', 'escrow', 'ip escrow'],
        'Product & Strategy': ['procurement', 'discovery', 'mvp', 'roi', 'pricing', 'technical debt', 'legacy', 'feature flags', 'shift-left', 'chaos engineering']
    }

    groups = {k: [] for k in keywords}
    groups['Other'] = []

    for row in rows:
        # Extract title
        # | 1   | ✅ The CTO's Master Guide to Procurement: How to Audit a Software Development Company Before You Sign | ...
        parts = row.split('|')
        if len(parts) > 2:
            title = parts[2].strip().lower()
            assigned = False
            for group, kw_list in keywords.items():
                if any(kw in title for kw in kw_list):
                    groups[group].append(row)
                    assigned = True
                    break
            if not assigned:
                groups['Other'].append(row)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(header_lines)
        
        for group, group_rows in groups.items():
            if not group_rows:
                continue
            f.write(f'\n## {group}\n\n')
            f.writelines(table_header)
            f.writelines(group_rows)

if __name__ == "__main__":
    process_markdown(sys.argv[1])
