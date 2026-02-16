vowel = "aeiou"
s = input()
res = 0

for word in s:
    if word in vowel:
        res += 1

print(res, res + s.count('y'))
