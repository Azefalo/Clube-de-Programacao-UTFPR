# https://www.urionlinejudge.com.br/judge/en/problems/view/1070
n = int(input())
if n % 2 != 0:
    for i in range(n,(n+12),2):
        if i >= n:
            print(i)
else:
    for i in range(n+1,n+12,2):
        if i >= n:
            print(i)   