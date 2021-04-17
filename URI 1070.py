# https://www.urionlinejudge.com.br/judge/en/problems/view/1070
n = int(input())
if n % 2 != 0:
    for i in range(n,n+12,2):
        if i >= n:
            print(i)
else:
    for i in range(n+1,n+12,2):
        if i >= n:
            print(i)

### OU ###

n = int(input())
impares = [i for i in range(n,n+12) if  i % 2 != 0] # Criamos uma lista com os 6 números ímpares depois de n
for i in impares:
    print(i)