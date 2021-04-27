# https://www.urionlinejudge.com.br/judge/en/problems/view/1094
Input = int(input())
quantity = list()
rabbit = list()
rat = list()
frog = list()
total = 0
total_rabbit = 0
total_rat = 0
total_frog = 0

for i in range(Input):
    n = input().split()
    if n[1] == 'C':
        rabbit.append(n[0])
    elif n[1] == 'R':
        rat.append(n[0])
    elif n[1] == 'S':
        frog.append(n[0])
    quantity.append(n[0])
# Total (animals)
for i in range(len(quantity)):
    total += int(quantity[i])
print(f"Total: {total} cobaias")
# Total (rabbits, rats, frogs)
for i in range(len(rabbit)):
    total_rabbit += int(rabbit[i])
print(f"Total de coelhos: {total_rabbit}")
for i in range(len(rat)):
    total_rat += int(rat[i])
print(f"Total de ratos: {total_rat}")
for i in range(len(frog)):
    total_frog += int(frog[i])
print(f"Total de sapos: {total_frog}")

# Porcentagem
print(f"Percentual de coelhos: {(total_rabbit / total)*100:.2f} %")
print(f"Percentual de ratos: {(total_rat / total)*100:.2f} %")
print(f"Percentual de sapos: {(total_frog / total)*100:.2f} %")
