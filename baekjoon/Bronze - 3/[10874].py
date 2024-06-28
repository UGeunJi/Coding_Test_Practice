import sys
for _ in range(int(sys.stdin.readline())):
    tmp=list(map(int,sys.stdin.readline().split()))
    cnt=0
  
    for i in range(10):
        if tmp[i]== (i + 1) % 5 : cnt += 1
    if cnt == 8 : print(_+1)
