arr = []
num = []
ma = []

n = int(input())

for i in range(n):
    arr.append(input())

s_arr = list(set(arr))

for i in range(len(s_arr)):
    num.append(arr.count(s_arr[i]))

for i in range(len(num)):
    if num[i] == max(num):
        ma.append(s_arr[i])

if len(ma) != 1:
    ma.sort()
    print(ma[0])
else:
    print(ma[0])
