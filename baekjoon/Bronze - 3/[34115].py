n = int(input())
x = list(map(int, input().split()))
max_k = 0
 
for i in range(1, n + 1):
    firstNum = x.index(i)
    except_X = [0] * (firstNum + 1) + x[firstNum + 1 :]
    lastNum = except_X.index(i)
 
    max_k = max(max_k, abs(firstNum - lastNum) - 1)
 
print(max_k)
