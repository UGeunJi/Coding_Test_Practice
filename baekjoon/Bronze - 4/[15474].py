n, a, b, c, d = map(int, input().split())
a = (n // a + (1 if n % a else 0)) * b
c = (n // c + (1 if n % c else 0)) * d

print(min(a, c))
