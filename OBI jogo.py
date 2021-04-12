# https://olimpiada.ic.unicamp.br/pratique/pj/2016/f1/jogo/
P = int(input())
D_1 = int(input())
D_2 = int(input())
X = (D_1 + D_2) % 2
if P == 1 and X == 0:
    print("1")
elif P == 1 and X != 0:
    print("0")
elif P == 0 and X != 0:
    print("1")
elif P == 0 and X == 0:
    print("0")