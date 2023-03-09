def solution(skill, skill_trees):
    answer = 0
    
    skill = list(skill)
    for i in range(len(skill_trees)):
        skill_trees[i] = list(skill_trees[i])

    for i in range(len(skill_trees)):
        match = 1
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                if match != skill.index(skill_trees[i][j]) + 1:
                    break
                match += 1

        else:
            answer += 1
        
    return answer
