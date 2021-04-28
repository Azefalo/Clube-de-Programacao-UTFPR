# https://www.urionlinejudge.com.br/judge/en/problems/view/1060
positive = 0
for i in range(6):
    n = float(input())
    if n > 0:
        positive += 1
print(f"{positive} valores positivos")