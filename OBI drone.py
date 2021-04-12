# https://olimpiada.ic.unicamp.br/pratique/pj/2017/f1/drone/
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
if n1 <= n4 and n2 <= n5 or n1 <= n5 and n2 <= n4:
    print("S")
elif n2 <= n4 and n3 <= n5 or n2 <= n5 and n3 <= n4:
    print("S")
elif n1 <= n4 and n3 <= n5 or n1 <= n5 and n3 <= n4:
    print("S")
else:
    print("N")
