def solution(my_string, queries):
    for i in range(len(queries)):
        s_start = my_string[:queries[i][0]]
        s_end = my_string[queries[i][1] + 1:]
        s = my_string[queries[i][0] : queries[i][1] + 1]
        s_1 = s[::-1]
        my_string = s_start + s_1 + s_end

    return my_string
