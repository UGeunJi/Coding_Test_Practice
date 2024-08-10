import sys
input = sys.stdin.readline

str_list = ['G...', '.I.T', '..S.']
K = int(input())

for temp in str_list : 
    temp_str = ''
    for j in range(len(temp)) : 
        temp_str += (temp[j] * K)
    
    for k in range(K) : 
        print(temp_str)
