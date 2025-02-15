import sys
input = sys.stdin.readline

money = 5000
button = map(int, input().split())

for i in button:
  if i == 1:
    money -= 500
  elif i == 2:
    money -= 800
  else:
    money -= 1000
    
print(money)
