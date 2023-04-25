def solution(ineq, eq, n, m):
    if eq == '=' and ineq == '<':
        if n <= m:
            return 1
        else:
            return 0
    elif eq == '=' and ineq == '>':
        if n >= m:
            return 1
        else:
            return 0
    elif eq == '!' and ineq == '<':
        if n < m:
            return 1
        else:
            return 0
    elif eq == '!' and ineq == '>':
        if n >= m:
            return 1
        else:
            return 0
