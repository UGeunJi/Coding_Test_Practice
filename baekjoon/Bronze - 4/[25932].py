for _ in range(int(input())) :
    line = input()
    res = "none"
    if '17' in line :
        res = "zack"
    if '18' in line :
        res = ["mack", "both"][res == "zack"]
    print(line)
    print(res+'\n')
