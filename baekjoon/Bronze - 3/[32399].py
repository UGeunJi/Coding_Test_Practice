import sys
input = sys.stdin.readline

s = input().rstrip()

if s == ")1(": 
    print(2)
elif s == "(1)": 
    print(0)
else: 
    print(1)
