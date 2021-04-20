# https://www.urionlinejudge.com.br/judge/en/problems/view/1074
n = int(input())
x = None
numeros = []

for i in range(n):
    numeros.append(int(input()))
for z in range(n):
    x = numeros[z]
    if x == 0:
        print("NULL")
    elif (x % 2) == 0:
        if x > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif (x % 2) != 0:
        if x > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")