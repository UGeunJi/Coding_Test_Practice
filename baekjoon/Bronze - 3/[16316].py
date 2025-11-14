def sol(nums):
    for i in range(1,len(nums)+1):
        if nums[i-1].isdigit() and int(nums[i-1]) != i:
                return 'something is fishy'
    return 'makes sense'
 
if __name__ == '__main__':
    n = int(input())
    nums = list(input().split())
    print(sol(nums))
