A = int(input())
B = int(input())
C = int(input())
D = int(input())
B_C = B == C
BC_D = B + C == D
BCD_A = B + C + D == A
if B_C and BC_D and BCD_A:
    print("S")
else:
    print("N")