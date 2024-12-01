import sys

input = sys.stdin.readline
x_lst = []
y_lst = []

for _ in range(int(input())) :
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
    
print((max(x_lst) - min(x_lst)) * (max(y_lst) - min(y_lst)))
