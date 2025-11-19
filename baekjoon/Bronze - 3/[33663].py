Hlo, Hhi = map(int, input().split())
Slo, Shi = map(int, input().split())
Vlo, Vhi = map(int, input().split())
R, G, B = map(int, input().split())
 
V, m = max(R, G, B), min(R, G, B)
S = 255 * (V - m) / V
 
if V == R:
    H = 60 * (G - B) / (V - m)
elif V == G:
    H = 120 + 60 * (B - R) / (V - m)
elif V == B:
    H = 240 + 60 * (R - G) / (V - m)
 
if H < 0:
    H += 360
 
if Hlo <= H <= Hhi and Slo <= S <= Shi and Vlo <= V <= Vhi:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")
