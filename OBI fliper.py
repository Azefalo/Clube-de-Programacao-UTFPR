# https://olimpiada.ic.unicamp.br/pratique/pj/2014/f1/fliper/
entrada = input().split(" ")
P = int(entrada[0])
R = int(entrada[1])
if P == 0:
    print("C")
elif P == 1 and R == 1:
    print("A")
else:
    print("B")
