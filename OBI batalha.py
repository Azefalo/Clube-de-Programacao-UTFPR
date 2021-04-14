# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f3/batalha/
A1 = int(input())
D1 = int(input())
A2 = int(input())
D2 = int(input())

if D1 == A2 and D2 == A1:
    print("-1")
elif A1 != D2 and D1 == A2:
    print("1")
elif A2 != D1 and D2 == A1:
    print("2")
else:
    print("-1")