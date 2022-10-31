x = int(input())
y = int(input())
soma = 0

if x > y:
  if y%2 != 0:
    for c in range(y + 1,x):
      if c%2 != 0:
        soma += c
  elif y%2 == 0:
    for c in range (y,x):
      if c%2 !=0:
        soma += c
elif y > x:
  if x%2 != 0:
    for c in range(x + 1,y):
      if c%2 != 0:
        soma += c
  elif x%2 == 0:
    for c in range (x,y):
      if c%2!=0:
        soma += 1
print(soma)