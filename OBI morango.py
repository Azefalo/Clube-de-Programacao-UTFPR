# https://olimpiada.ic.unicamp.br/pratique/pj/2016/f1/morango/
Comprimento1 = int(input())
Largura1 = int(input())
Comprimento2 = int(input())
Largura2 = int(input())
Area1 = int(Comprimento1 * Largura1)
Area2 = int(Comprimento2 * Largura2)
if Area1 > Area2:
    print(Area1)
else:
    print(Area2)