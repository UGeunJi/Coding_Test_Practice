def generate_akaraka_string(K):
    result = "AKARAKA" + "RAKA" * (K - 1)
    return result

K = int(input())

print(generate_akaraka_string(K))
