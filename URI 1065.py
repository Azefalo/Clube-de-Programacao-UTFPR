# https://www.urionlinejudge.com.br/judge/en/problems/view/1065
pares = []
def par(x):
    if x % 2 == 0: # O resto da divisão por 2 é 0 (portanto el é par)
        pares.append(x)

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
par(n1)
par(n2)
par(n3)
par(n4)
par(n5)
print(f"{len(pares)} valores pares")