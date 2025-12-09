def calculate_weight(num):
    weight = len(str(num)) * sum(list(map(int, list(str(num)))))
    
    return weight

def heavy_numbers(num1, num2):
    answer = 0
    
    weight_1 = calculate_weight(num=num1)
    weight_2 = calculate_weight(num=num2)
    
    if weight_1 > weight_2:
        answer = 1
    elif weight_1 < weight_2:
        answer = 2
        
    return answer


if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    
    print(heavy_numbers(num1=num1, num2=num2))
