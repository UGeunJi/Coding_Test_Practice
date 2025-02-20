for i in range(int(input())):
    li = input().split()
    res = "NO"
    
    if li[1] == '+' and int(li[0]) + int(li[2]) == int(li[4]):
        res = "YES"
    if li[1] == '-' and int(li[0]) - int(li[2]) == int(li[4]):
        res = "YES"
    
    print(f"Case {i + 1}: {res}")
