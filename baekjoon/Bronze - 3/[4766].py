temp = float(input())

while True:
    n = float(input())
    
    if n == 999:
        break
        
    print("{:.2f}".format(n - temp))
    temp = n
