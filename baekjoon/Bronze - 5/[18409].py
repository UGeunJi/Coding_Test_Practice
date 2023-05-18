n = int(input())
s = input()
answer = 0

for i in s:
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
        answer += 1
        
print(answer)
