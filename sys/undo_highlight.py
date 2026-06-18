import sys

def undo_highlight(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the <mark> tags back to just the word
    content = content.replace('<mark>Decision</mark>', 'Decision')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    undo_highlight('/Users/duyle/.gemini/antigravity-ide/scratch/marketingskills-coreyhaines31/LONG_ARTICLES_INDEX.md')
