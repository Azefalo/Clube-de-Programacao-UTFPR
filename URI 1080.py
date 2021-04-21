# https://www.urionlinejudge.com.br/judge/en/problems/view/1080
n = []
for i in range(10):
    n.append(int(input()))
print(f"{max(n)}")
print(f"{n.index(max(n))+1}")