def golbange_print(n):
    answer = ['' for _ in range(n * 5)]
    
    for idx in range(n * 5):
        if 2 * n - 1 < idx < 2 * n + n:
            answer[idx] = "@" * (n * 3)
        elif idx < 2 * n:
            answer[idx] = f"{'@' * n}{((3 - (idx // n)) * n) * ' '}{'@' * (n)}"
        else:
            answer[idx] = f"{'@' * n}{((idx // n) * n - n ) * ' '}{'@' * (n)}"
        
    return "\n".join(answer)


if __name__ == "__main__":
    n = int(input())
    
    print(golbange_print(n = n))
