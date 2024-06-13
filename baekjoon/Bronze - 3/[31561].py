input_minute = int(input())
correct_minute = 0

if input_minute >= 30:
    correct_minute += 15
    input_minute -= 30
    correct_minute += input_minute * 1.5
else:
    correct_minute = input_minute / 2

print(correct_minute)
