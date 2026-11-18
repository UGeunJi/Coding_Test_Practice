def solution(bandage, health, attacks):
    heal = 0
    full = health
    for i in range(len(attacks)):
        health += (abs(attacks[i][0] - heal) - 1) * bandage[1]
        health += bandage[2] * ((abs(attacks[i][0] - heal) - 1) // bandage[0])
        if health > full:
            health = full
        health -= attacks[i][1]
        if health <= 0:
            return -1
        heal = attacks[i][0]

    return health
