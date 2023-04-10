arr1 = []
arr2 = []

for _ in range(4):
    arr1.append(int(input()))

arr1.sort()
arr1.pop(0)

for _ in range(2):
    arr2.append(int(input()))

a = sum(arr1)
b = max(arr2)

print(a + b)
