for i in range(int(input())):
    a, b = map(int, input().split())
    print(f"Case {i + 1}:", end=' ')
    if a == 0:
        print('0')
        continue
    if a // b:
        print(a // b, end=' ') 
    if a % b:
        print(f"{a % b}/{b}", end='')
    print()
