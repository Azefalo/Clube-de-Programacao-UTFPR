#  https://www.urionlinejudge.com.br/judge/en/problems/view/1035
INPUT = input().split(" ")
A = int(INPUT[0])
B = int(INPUT[1])
C = int(INPUT[2])
D = int(INPUT[3])

if B > C and D > A and (C + D) > (A + B) and (A % 2) == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")