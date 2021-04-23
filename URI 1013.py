# https://www.urionlinejudge.com.br/judge/en/problems/view/1013
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
def maior(x,y):
    if x > 0 and y < 0:
        y = -y
        if x > y:
            return x
        else:
            return y
    elif x < 0 and y > 0:
        x = -x
        if x > y:
            return x
        else:
            return y
    elif x < 0 and y < 0:
        x = -x
        y = -y
        if x > y:
            return x
        else:
            return y
    else:
        if x > y:
            return x
        else:
            return y
print(f"{maior(maior(a,b),c)} eh o maior")