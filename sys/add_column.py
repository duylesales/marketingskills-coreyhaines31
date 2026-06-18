import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('\n## Other\n')
    if len(parts) < 2:
        return
    
    before_other = parts[0]
    other_section = parts[1]
    
    lines = other_section.split('\n')
    new_lines = []
    
    in_table = False
    for line in lines:
        if line.strip().startswith('| No. |'):
            # It's the header row
            # Replace | No. | Title | ... with | No. | Title | Keyword | ...
            parts_line = line.split('|')
            if len(parts_line) > 3 and parts_line[2].strip() == 'Title':
                parts_line.insert(3, ' Keyword ')
                new_line = '|'.join(parts_line)
                new_lines.append(new_line)
                in_table = True
            else:
                new_lines.append(line)
        elif line.strip().startswith('| --- |'):
            if in_table:
                parts_line = line.split('|')
                parts_line.insert(3, ' --- ')
                new_line = '|'.join(parts_line)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        elif line.strip().startswith('|') and in_table:
            parts_line = line.split('|')
            if len(parts_line) > 3:
                title = parts_line[2].strip()
                
                # Determine keyword
                keyword = 'Unknown'
                if 'Dedicated Development Team' in title:
                    keyword = 'Dedicated Development Team'
                elif 'Software Product Engineering' in title:
                    keyword = 'Software Product Engineering'
                elif 'App Development' in title:
                    keyword = 'App Development'
                elif 'SaaS' in title:
                    keyword = 'SaaS Development'
                elif 'Software Engineers' in title or 'Software Developers' in title or 'Engineering' in title:
                    keyword = 'Software Engineering / Team'
                elif 'Software Development Company' in title:
                    keyword = 'Software Development Company'
                elif 'Node.js' in title or 'React' in title or 'CSS' in title or 'API' in title or 'Redis' in title or 'Docker' in title or 'DOM' in title or 'Regex' in title or 'Cache' in title or 'Memory' in title or 'Thread' in title or 'N+1' in title or 'Webhook' in title:
                    keyword = 'Technical Concept / Bug'
                else:
                    match = re.search(r'([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)', title)
                    if match:
                        keyword = match.group(1)
                
                parts_line.insert(3, f' {keyword} ')
                new_line = '|'.join(parts_line)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    # Write back
    new_other_section = '\n'.join(new_lines)
    new_content = before_other + '\n## Other\n' + new_other_section
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    process_file('/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/LONG_ARTICLES_INDEX.md')
