from collections import Counter

def odd_even_strings(string):
    even_check, odd_check = 0, 0
    
    answer = "0/1"
    
    cnt_items = Counter(string).items()
    
    for item in cnt_items:
        if item[1] % 2 == 0:
            even_check += 1
        elif item[1] % 2 == 1:
            odd_check += 1
    
    if even_check > 0 and odd_check == 0:
        answer = "0"
    elif even_check == 0 and odd_check > 0:
        answer = "1"
        
    return answer
        
if __name__ == "__main__":
    string = input()
    print(odd_even_strings(string=string))
