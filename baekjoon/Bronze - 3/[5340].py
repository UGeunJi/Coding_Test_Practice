res = []

for _ in range(6):
    line = input().rstrip()
    res.append(len(line))

print(f"Latitude {res[0]}:{res[1]}:{res[2]}")
print(f"Longitude {res[3]}:{res[4]}:{res[5]}")
