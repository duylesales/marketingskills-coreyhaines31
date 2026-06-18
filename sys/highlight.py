import sys

def highlight_decision(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        if line.strip().startswith('|'):
            parts = line.split('|')
            # Check all parts to find the "Buyer Stage" column holding 'Decision'
            # We look for parts that exactly match ' Decision ' or similar padding
            for i in range(1, len(parts) - 1):
                if parts[i].strip() == 'Decision':
                    # Replace with <mark>Decision</mark> while keeping original spacing
                    parts[i] = parts[i].replace('Decision', '<mark>Decision</mark>')
            new_lines.append('|'.join(parts))
        else:
            new_lines.append(line)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    highlight_decision('/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/LONG_ARTICLES_INDEX.md')
