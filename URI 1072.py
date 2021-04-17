# https://www.urionlinejudge.com.br/judge/en/problems/view/1072
X = int(input())
N = None # N é vazio
intervalo = []

for i in range(X):
    N = int(input())
    if 10 <= N <= 20:
        intervalo.append(N)

print(f"{len(intervalo)} in")
print(f"{X - len(intervalo)} out")