cand = int(input())
votosac=0
Lista0=[]
if 2<= cand <=10**4:
    count=0
    while count != cand:
        votos = int(input())
        Lista0.append(votos)
        if votos>Lista0[0]:
            print('N')
            break
        elif votos <=Lista0[0]:
            count+=1
            votosac+=votos
            if votosac>100000:
                break
if count == cand:
    print('S')