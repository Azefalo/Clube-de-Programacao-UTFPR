# https://olimpiada.ic.unicamp.br/pratique/pj/2018/f2/copa/
K = int(input())
L = int(input())

if 1 <= K <= 8 and 9 <= L <= 16 or 1 <= L <= 8 and 9 <= K <= 16:
    print("final")
elif 1 <= K <= 4 and 5 <= L <= 8 or 9 <= K <= 12 and 13 <= L <= 16:
    print("semifinal")
elif 1 <= L <= 4 and 5 <= K <= 8 or 9 <= L <= 12 and 13 <= K <= 16:
    print("semifinal")
elif (K == 1 or K == 2) and (L == 3 or L == 4):
    print("quartas")
elif K == 5 or K == 6 and (L == 7 or L == 8):
    print("quartas")
elif (K == 9 or K == 10) and (L == 11 or L == 12):
    print("quartas")
elif (K == 13 or K == 14) and (L == 15 or L == 16):
    print("quartas")
elif (L == 1 or L == 2) and (K == 3 or K == 4):
    print("quartas")
elif (K == 5 or K == 6) and (K == 7 or K == 8):
    print("quartas")
elif (L == 9 or L == 10) and (K == 11 or K == 12):
    print("quartas")
elif (L == 13 or L == 14) and (K == 15 or K == 16):
    print("quartas")
elif K == L - 1 or L == K -1:
    print("oitavas")
