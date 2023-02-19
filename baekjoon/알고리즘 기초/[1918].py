s = list(input())
stack = []
ss = ''

for i in s:
    if i.isalpha():
        ss += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ss += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ss += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ss += stack.pop()
            stack.pop()
        print('ss:', ss, 'stack:', stack)
        
while stack:
    ss += stack.pop()
    
print(ss)
