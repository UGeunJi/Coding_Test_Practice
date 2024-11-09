import sys
input=sys.stdin.readline

if __name__ == "__main__":
    ans = 0
    for n in range(1, int(input()) + 1):
        s = 0
        tmp = n
        while tmp:
            s += tmp % 10
            tmp //= 10
            
        if n % s == 0: 
            ans += 1
    
    print(ans)
