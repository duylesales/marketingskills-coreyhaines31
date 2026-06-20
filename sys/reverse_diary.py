import os

diary_path = '/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/marketingskills-coreyhaines31/diary.md'

with open(diary_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = []
months = []
current_month = None
current_day = None
current_phase = None
current_item = None

state = 'header'

for line in lines:
    if line.startswith('## '):
        state = 'month'
        current_month = {'title': line.strip(), 'days': []}
        months.append(current_month)
    elif line.startswith('### '):
        current_day = {'title': line.strip(), 'phases': []}
        current_month['days'].append(current_day)
    elif line.startswith('**Giai đoạn'):
        current_phase = {'title': line.strip(), 'items': []}
        current_day['phases'].append(current_phase)
    elif line.startswith('- ['):
        current_item = [line.rstrip('\n')]
        current_phase['items'].append(current_item)
    elif state == 'header':
        header.append(line.rstrip('\n'))
    elif line.strip() != '':
        if current_item is not None:
            current_item.append(line.rstrip('\n'))

with open(diary_path, 'w', encoding='utf-8') as f:
    for h in header:
        f.write(h + '\n')
    for m in reversed(months):
        f.write(m['title'] + '\n\n')
        for d in reversed(m['days']):
            f.write(d['title'] + '\n\n')
            for p in reversed(d['phases']):
                f.write(p['title'] + '\n')
                for item in reversed(p['items']):
                    for il in item:
                        f.write(il + '\n')
                f.write('\n')
