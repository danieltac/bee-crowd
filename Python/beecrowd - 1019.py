n1 = int(input())

hora = n1 // 3600
minutos = (n1%3600)//60
segundos = (n1%60)

print ("{}:{}:{}".format(hora,minutos,segundos))