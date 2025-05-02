n = int(input())
s1 = input()
s2 = input()
answer = 0

for i in range(n):
    if s1[i] != s2[i]:
      answer += 1
      
print(answer)
