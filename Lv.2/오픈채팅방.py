def solution(record):
    answer = []

    id = {i.split()[1]:i.split()[2] for i in record if i.split()[0]!="Leave"}
    
    for i in record:
        if i.split()[0]=="Enter":
            answer.append(f"{id[i.split()[1]]}님이 들어왔습니다.")
        elif i.split()[0]=="Leave":
            answer.append(f"{id[i.split()[1]]}님이 나갔습니다.")

    return answer
