n = int(input())

for i in range(n):
    num = 1
    score = 1
    limit = int(input())
    
    while True:
        score *= num
        num += 1
        if num > limit:
          break
          
    score = str(score)
  
    print(int(score[-1]))
