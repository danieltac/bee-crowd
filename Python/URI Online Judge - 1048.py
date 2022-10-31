a = float(input())

if (0 <= a <= 400):
  reajuste = a*0.15
  novo_sal = a + reajuste
  print("Novo salario: {:.2f}".format(novo_sal))
  print("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual: 15 %")
elif (400.01 <= a <= 800):
  reajuste = a*0.12
  novo_sal = a + reajuste
  print ("Novo salario: {:.2f}".format(novo_sal))
  print ("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual: 12%")
elif (800.01 <= a <= 1200):
  reajuste = a*0.1
  novo_sal = a + reajuste
  print ("Novo salario: {:.2f}".format(novo_sal))
  print ("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual: 10 %")
elif (1200.01 <= a <= 2000):
  reajuste = a*0.07
  novo_sal = a + reajuste
  print ("Novo salario: {:.2f}".format(novo_sal))
  print ("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual: 7 %")
elif (a > 2000):
  reajuste = a*0.04
  novo_sal = a + reajuste
  print ("Novo salario: {:.2f}".format(novo_sal))
  print ("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual: 4 %")