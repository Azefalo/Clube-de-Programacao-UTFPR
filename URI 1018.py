# https://www.urionlinejudge.com.br/judge/en/problems/view/1018
n = int(input())
print(n)
if (n/100) >= 1:
    x = int(n/100)
    print(f'{x} nota(s) de R$ 100,00')
    n -= 100 * x
else:
    print('0 nota(s) de R$ 100,00')
if (n/50) >= 1:
    x = int(n/50)
    print(f'{x} nota(s) de R$ 50,00')
    n -= 50 * x
else:
    print('0 nota(s) de R$ 50,00')
if (n/20) >= 1:
    x = int(n/20)
    print(f'{x} nota(s) de R$ 20,00')
    n -= 20 * x
else:
    print('0 nota(s) de R$ 20,00')
if (n/10) >= 1:
    x = int(n/10)
    print(f'{x} nota(s) de R$ 10,00')
    n -= 10 * x
else:
    print('0 nota(s) de R$ 10,00')
if (n/5) >= 1:
    x = int(n/5)
    print(f'{x} nota(s) de R$ 5,00')
    n -= 5 * x
else:
    print('0 nota(s) de R$ 5,00')
if (n/2) >= 1:
    x = int(n/2)
    print(f'{x} nota(s) de R$ 2,00')
    n -= 2 * x
else:
    print('0 nota(s) de R$ 2,00')
if (n/1) >= 1:
    x = int(n/1)
    print(f'{x} nota(s) de R$ 1,00')
    n -= 1 * x
else:
    print('0 nota(s) de R$ 1,00')
