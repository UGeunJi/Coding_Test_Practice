while 1:

	try:
    		N, S = map(int, input().split())
	except EOFError:
    		break
	else:
    		print(S // (N + 1))
