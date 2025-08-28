n = int(input())
li = list(map(int, input().split()))
cnt = li.count(1)

print(cnt if cnt <= n - cnt else n - cnt)
