n = int(input())
s = list(map(str, input().split()))
s1 = list(map(str, input().split()))
s2 = []

for i in range(len(s)):
    if s[i] not in s1:
        s2.append(s[i])
    
print(s2[0])
