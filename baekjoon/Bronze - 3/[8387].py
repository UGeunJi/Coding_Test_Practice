n = int(input())
s1 = input()
s2 = input()
ans = 0

for i in range(n) :
    if s1[i] == s2[i] : ans += 1

print(ans)
