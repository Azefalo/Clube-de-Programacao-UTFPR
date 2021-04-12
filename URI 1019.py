# https://www.urionlinejudge.com.br/judge/en/problems/view/1019
n = int(input())
min = int(n/60)
hora = int(min/60) 
min = int((n-(hora * 60 * 60))/60)
sec = int((n-(hora * 60 * 60 + min * 60)))
print(f"{hora}:{min}:{sec}")