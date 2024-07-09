n = int(input())
st = input()

u = st.count('u')
o = st.count('o')
s = st.count('s')
p = st.count('p')
c = st.count('c')

li = [u, o, s, p ,c]

print(min(li))
