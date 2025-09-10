s = input()
t = input()
result = ""
 
for i in t:
    if i not in s:
        result += i
 
print(result)
