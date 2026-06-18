import os
import glob
import json

blog_dir = 'blog'
files = glob.glob(os.path.join(blog_dir, 'long_article_*.md'))
files.sort(key=lambda x: int(x.split('_')[2])) # Sort by article number

queue = []

for filepath in files:
    base = os.path.splitext(filepath)[0]
    pic_path = f"{base}_pic.jpg"
    
    # Check if pic exists
    if os.path.exists(pic_path):
        continue
        
    title = ""
    # Extract title from the first line
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('# '):
                title = line[2:].strip()
                break
    
    if title:
        queue.append({
            "filepath": filepath,
            "title": title,
            "pic_path": pic_path
        })

with open('image_queue.json', 'w') as f:
    json.dump(queue, f, indent=2)

print(f"Found {len(queue)} articles needing images.")
