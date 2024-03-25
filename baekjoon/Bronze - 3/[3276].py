a = 1
b = 1
n = int(input())

while a * b < n:
    if a > b: 
        b += 1
    else: 
        a += 1

print(a, b)
