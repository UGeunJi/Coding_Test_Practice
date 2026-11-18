def solution(wallet, bill):
    answer = 0

    while True:
        wallet = sorted(wallet)
        bill = sorted(bill)
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            break
        for i in range(2):
            if bill[i] > wallet[i]:
                bill[1] //= 2
                answer += 1
                break
                
        print("wallet:", wallet)
        print("bill:", bill)
                
    return answer
