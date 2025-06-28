n = int(input())

if n >= -32768 and n <= 32767:
    print("short")
elif n >= -2147483648 and n <= 2147483647:
    print("int")
else:
    print("long long")
