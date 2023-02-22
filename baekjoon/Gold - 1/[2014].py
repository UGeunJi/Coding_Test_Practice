import heapq

k, n = map(int, input().split())
nums = list(map(int, input().split()))

heap = []

for i in nums:
    heapq.heappush(heap, i)

for _ in range(n):
    num = heapq.heappop(heap)
    for i in range(k):
        temp = num * nums[i]
        heapq.heappush(heap, temp)
        
        if num % nums[i] == 0:
            break
        
print(num)
