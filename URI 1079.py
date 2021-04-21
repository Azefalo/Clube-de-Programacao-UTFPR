# https://www.urionlinejudge.com.br/judge/en/problems/view/1079
qtde_num = int(input())
for i in range(qtde_num):
    n = input().split()
    n1 = float(n[0])
    n2 = float(n[1])
    n3 = float(n[2])
    print(f"{(2*n1 + 3*n2 + 5*n3)/10:.1f}")