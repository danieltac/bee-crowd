n1 = int(input())

y = 365
m = 30
years = n1 // y
months = (n1 % 365) // m
days =  (n1 % 365) % m

print (years,"ano(s)")
print (months,"mes(es)")
print (days,"dia(s)")