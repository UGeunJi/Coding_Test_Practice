from collections import deque 

n = int(input()) 

for i in range(n):
    s = input()
    num = int(input())
    arr = input()[1:-1].split(",")

    queue = deque(arr)
    
    base = 0
    
    if num == 0:
        queue = []

    for j in s:
        if j == 'R':
            base += 1
        elif j == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if base % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    else:
        if base % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
