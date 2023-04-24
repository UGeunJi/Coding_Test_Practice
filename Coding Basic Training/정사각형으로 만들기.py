def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
    elif len(arr) < len(arr[0]):
        while len(arr) != len(arr[0]):
            arr.append([0] * len(arr[0]))
    elif len(arr) > len(arr[0]):
        while len(arr) != len(arr[0]):
            for i in range(len(arr)):
                arr[i].append(0)
    return arr
