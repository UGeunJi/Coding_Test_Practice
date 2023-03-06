import sys

arr = []
for _ in range(5):
    arr.append(sys.stdin.readline())

nums = []
for i in range(5):
    if "FBI" in arr[i]:
        nums.append(i + 1)

if len(nums) == 0:
    print("HE GOT AWAY!")
else:
    print(*nums, sep=' ')
