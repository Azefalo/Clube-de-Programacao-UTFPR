# https://www.urionlinejudge.com.br/judge/en/problems/view/1020
n = int(input())
ano = int(n/365)
mes = int((n-(ano * 365))/30)
dia = int((n-(mes * 30 + ano * 365)))
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")