num = input()
arr = list(map(int, input().split()))
print(['no', 'yes'][sum(arr)%3==0])
