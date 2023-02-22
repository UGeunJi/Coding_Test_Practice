min, max = map(int, input().split())

answer = max - min + 1

square_arr = [False] * (max - min + 1)

for i in range(2, int(max ** 0.5 + 1)):
    square = i ** 2

    for j in range((((min - 1) // square) + 1) * square, max + 1, square):
        if not square_arr[j - min] :
            square_arr[j - min] = True
            answer -= 1

print(answer)
