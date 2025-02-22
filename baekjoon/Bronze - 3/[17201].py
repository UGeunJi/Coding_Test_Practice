n = input()
n2 = input()
connected = "Yes"

for index in range(0, len(n2) - 2, 2):
    if n2[index] != n2[index + 2]:
        connected = "No"
        break

print(connected)
