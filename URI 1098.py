# https://www.urionlinejudge.com.br/judge/en/problems/view/1098
'''
Como o python funciona em binário, números flutuantes ficam um pouco diferentes, veja:
Na ultima linha, ao invéz de I=2, na verdade, ele fica I = 1.9999999999999998
Portanto, vamos multiplicar tudo por 10, ou seja, trabalhar só com inteiro, mas
na hora de imprimir, dividimos por 10 para transforamar em flutuante como pedido
'''

I = 0
J = 10
x = J
for i in range(11):
    for i in range(3):
        x = J + 10*i
        if I == 0 or I == 10 or I == 20:
            print(f"I={int(I/10)}", end=" ")
            print(f"J={int(x/10)}")
        else:
            print(f"I={I/10}", end=" ")
            print(f"J={x/10}")
        
    I += 2
    J += 2