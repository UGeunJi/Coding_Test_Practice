for i in range(1, int(input()) + 1) :
    t = [i ** 2 for i in [*map(int, input().split())]]
    if max(t) == sum(t) - max(t) : print(f"Case #{i}: YES")
    else : print(f"Case #{i}: NO")
