n, m = map(int, input().split())

def cnt_num(n, k):
    cnt = 0
    while n != 0:
        n = n // k
        cnt += n
    return cnt

print(min(cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n - m, 5), cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n - m, 2)))
