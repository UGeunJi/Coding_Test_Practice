def solution(my_string, indices):
    my_string = list(my_string)
    
    for i in range(len(indices)):
        my_string[indices[i]] = '-'
        
    for i in range(len(my_string)):
        if my_string[i] == '-':
            my_string[i] = ''
            
    return ''.join(my_string)
