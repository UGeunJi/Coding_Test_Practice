T = int(input())

for _ in range(T):
    N = int(input())
    total_credit = 0
    total_grade = 0
    
    for _ in range(N):
        credit, grade = map(float, input().split())
        total_credit += credit
        total_grade += credit * grade
        
    GPA = total_grade / total_credit
    print(int(total_credit), '%.1f' % GPA)
