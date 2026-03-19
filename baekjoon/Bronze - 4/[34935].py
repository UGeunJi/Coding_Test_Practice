import sys

def solve():
    n = int(sys.stdin.readline())
    
    a = list(map(int, sys.stdin.readline().split()))
    
    if n == 1:
        print(1)
        return

    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print(0)
            return
            
    print(1)

if __name__ == "__main__":
    solve()
