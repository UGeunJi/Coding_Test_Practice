def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                answer += code[i]
            elif code[i] == '1':
                mode = 1
        elif mode == 1:
            if code[i] != '1' and i % 2 == 1:
                answer += code[i]
            elif code[i] == '1':
                mode = 0
    
    if len(answer) == 0:
        return f'EMPTY'
    else:
        return answer
