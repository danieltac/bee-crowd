lista = []
n = int(input())
for c in range(n):
    x = int(input())
    lista.append(x)
for t in lista:
    soma = 0
    y = t-1
    for s in range(1,y):
        if t%s==0:
            soma+=s
    if soma == t:
        print("{} eh perfeito".format(t))
    else:
        print("{} nao eh perfeito".format(t))