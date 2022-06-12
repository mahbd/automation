with open('../requirements.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip().split('==')[0] for line in lines]
with open('../requirements.txt', 'w') as f:
    f.write('\n'.join(lines))