# https://olimpiada.ic.unicamp.br/pratique/pj/2019/f1/idade/
M = int(input()) # Idade da Mônica
A = int(input()) # Idade de um dos filhos
B = int(input()) # Idade de um dos filhos
C = M - (A + B)
if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
else:
    print(C)

##### Outra resolução utilizando funções #####

M = int(input()) # Idade da Mônica
A = int(input()) # Idade de um dos filhos
B = int(input()) # Idade de um dos filhos
C = M - (A + B)
def maior(x, y): # Função para gerar o maior valor entre x e y
    if x >= y:
        return x
    else:
        return y
mais_velho = maior(maior(A, B), C) # Define em mais_velho o maior valor entre A, B e C
print(mais_velho)