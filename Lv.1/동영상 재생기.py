def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = int(video_len.replace(":", ""))
    pos = int(pos.replace(":", ""))
    op_start = int(op_start.replace(":", ""))
    op_end = int(op_end.replace(":", ""))
    
    m = pos // 100
    s = pos % 100
    
    for i in range(len(commands)):
        if op_start <= pos <= op_end:
            pos = op_end
            m = pos // 100
            s = pos % 100

        if commands[i] == 'prev':
            s -= 10
            if s < 0 and m > 0:
                m -= 1
                s += 60
            elif s < 0 and m <= 0:
                m, s = 0, 0

        elif commands[i] == 'next':
            s += 10
            if s > 60:
                m += 1
                s -= 60

        pos = m * 100 + s
        
        if pos > video_len:
            pos = video_len
            m = pos // 100
            s = pos % 100
                
    if op_start <= pos <= op_end:
        pos = op_end
        m = pos // 100
        s = pos % 100

    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)

    if s < 10:
        s = "0" + str(s)
    else:
        s = str(s)
    
    if s == 0:
        answer = str(m) + ":00"
    elif m == 0:
        answer = "00:" + str(s)
    else:
        answer = str(m) + ":" + str(s)
            
    return answer
