# https://www.urionlinejudge.com.br/judge/en/problems/view/1071
x = int(input())
y = int(input())
soma = 0

for i in range((y+1),x):
    if i % 2 != 0:
        soma += i
print(soma)