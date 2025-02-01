for i in range(int(input())):
    a, b = map(int, input().split())
    res = (b- a + 1) * (a + b) // 2
  
    print(f"Scenario #{i + 1}:")
    print(f"{res}\n")
