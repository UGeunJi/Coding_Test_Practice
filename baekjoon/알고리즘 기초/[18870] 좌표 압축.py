import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
s_arr = list(sorted(set(arr)))

dic = {s_arr[i] : i for i in range(len(s_arr))}

for i in arr:
    print(dic[i], end = ' ')
