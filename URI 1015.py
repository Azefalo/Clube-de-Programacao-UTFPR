# https://www.beecrowd.com.br/judge/en/problems/view/1015
P1 = input().split()
P2 = input().split()

X1 = float(P1[0])
Y1 = float(P1[1])
X2 = float(P2[0])
Y2 = float(P2[1])

distance = ((X2-X1)**2+(Y2-Y1)**2)**0.5

print(f"{distance:.4f}")