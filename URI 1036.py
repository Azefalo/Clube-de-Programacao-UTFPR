# https://www.beecrowd.com.br/judge/en/problems/view/1036
I = input().split(" ")
A = float(I[0])
B = float(I[1])
C = float(I[2])
delta = B**2-4*A*C
if delta < 0 or A == 0:
  print("Impossivel calcular")
else:
  R1 = (-B +(delta**0.5)) / (2*A)
  R2 = (-B -(delta**0.5)) / (2*A)
  print(f"R1 = {R1:.5f}")
  print(f"R2 = {R2:.5f}")