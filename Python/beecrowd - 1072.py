n = int(input())
inn = 0
out = 0
for c in range (1,n+1):
  x = input()
  x = int(x)
  if 10 <= x <= 20:
    inn += 1
  else:
    out += 1
print ("{} in".format(inn))
print ("{} out".format(out))