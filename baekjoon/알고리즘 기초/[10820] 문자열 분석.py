while True:
    try:
        s = input()
        answer = [0] * 4

        for i in s:
            if i == ' ':
                answer[3] += 1
            elif i.isdigit():
                answer[2] += 1
            elif i.isupper():
                answer[1] += 1
            elif i.islower():
                answer[0] += 1

        print(*answer)
        
    except:
        break
