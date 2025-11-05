n, k, T = map(int, input().split())
d = [0] + list(map(int, input().split()))
T_lst = [T] + [0] * n
 
for i in range(n):
    if T_lst[i] > k:
        T_lst[i + 1] = T_lst[i] + d[i + 1] - abs(T_lst[i] - k)
    elif T_lst[i - 1] < k:
        T_lst[i + 1] = T_lst[i] + d[i + 1] + abs(T_lst[i] - k)
    else:
        T_lst[i + 1] = T_lst[i] + d[i + 1]
 
result = 0
for t in T_lst[1:]:
    result += abs(t - k)
 
print(result)
