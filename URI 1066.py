# https://www.urionlinejudge.com.br/judge/en/problems/view/1066
pares = []
positivos = []
negativos = []

def par(x):
    if x % 2 == 0:
        pares.append(x)
def positivo(x):
    if x > 0:
        positivos.append(x)
def negativo(x):
    if x < 0:
        negativos.append(x)

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
positivo(n1)
positivo(n2)
positivo(n3)
positivo(n4)
positivo(n5)
negativo(n1)
negativo(n2)
negativo(n3)
negativo(n4)
negativo(n5)

print(f"{len(pares)} valor(es) par(es)")
print(f"{5 - len(pares)} valor(es) impar(es)")
print(f"{len(positivos)} valor(es) positivo(s)")
print(f"{len(negativos)} valor(es) negativo(s)")