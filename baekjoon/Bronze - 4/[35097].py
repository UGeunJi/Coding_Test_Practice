while True:
    num = int(input())
    if num == 0:
        break
    number = 0
    
    for i in range(num):
        for j in range(num):
            number += (i + 1) * (j + 1)
    
    print(number)
