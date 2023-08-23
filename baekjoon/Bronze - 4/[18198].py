sb = input()
A, B = 0, 0

for i in range(len(sb)):
    if sb[i] == 'A':
        A += int(sb[i + 1])
    elif sb[i] == 'B':
        B += int(sb[i + 1])
        
print('A' if A > B else 'B')
