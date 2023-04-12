# Solution 1
# 재귀
# 좌표 r, c가 2배가 되면 해당 배열값은 4배가 되는 규칙
N, r, c = map(int, input().split())

def sol(N, r, c):

	if N == 0:
		return 0
        
	return 2 * (r % 2) + (c % 2) + 4 * sol(N - 1, int(r / 2), int(c / 2))

print(sol(N, r, c))


#############################################################################################

# Solution 2
# 분할 정복
# 2의 N승 X 2의 N승의 사각형에서 분할된 계산에 의한 사분면의 시작과 끝의 관계에 따른 규칙
N, r, c = map(int, input().split())
ans = 0

while N != 0:
	N -= 1

	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N ) 
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)
