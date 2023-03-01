import heapq
import sys

n = int(sys.stdin.readline())

heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)
