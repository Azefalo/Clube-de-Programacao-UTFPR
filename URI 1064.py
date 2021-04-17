# https://www.urionlinejudge.com.br/judge/en/problems/view/1064
positivos = []
soma_positivos = 0
def positivo(x): # Função que adiciona a lista de positivos, valores que são maiores que 0
    if x > 0:
        positivos.append(x)

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
positivo(n1)
positivo(n2)
positivo(n3)
positivo(n4)
positivo(n5)
positivo(n6)

print(f"{len(positivos)} valores positivos") # Imprime a quantidade de números na lista positivos
for i in range(len(positivos)):
    soma_positivos += positivos[i]
media_positivos = soma_positivos / len(positivos) # Pega a soma dos positivos e divide pela quantidade de números
print(f"{media_positivos:.1f}")