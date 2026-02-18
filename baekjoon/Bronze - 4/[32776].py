S = int(input())
Ma, F, Mb = map(int, input().split())
 
if S <= Ma + F + Mb or S <= 240:
    print("high speed rail")
else:
    print("flight")
