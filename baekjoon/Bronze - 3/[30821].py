import sys
input = sys.stdin.readline

def fact(n): 
    if n == 1 or n == 0: 
        return 1
    return n * fact(n - 1)

n = int(input())

print(fact(n) // (fact(n - 5) * fact(5)))
