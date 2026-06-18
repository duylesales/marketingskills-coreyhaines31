import sys

def bold_decision(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for line in lines:
        if line.strip().startswith('|'):
            parts = line.split('|')
            # Check all parts to find the "Buyer Stage" column holding 'Decision'
            for i in range(1, len(parts) - 1):
                if parts[i].strip() == 'Decision':
                    # Replace with **Decision** while keeping original spacing
                    parts[i] = parts[i].replace('Decision', '**Decision**')
            new_lines.append('|'.join(parts))
        else:
            new_lines.append(line)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    bold_decision('/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/LONG_ARTICLES_INDEX.md')
