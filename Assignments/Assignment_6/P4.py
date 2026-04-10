n = 5
for i in range(n+1):
  for j in range(5,5-i,-1):
    print(chr(64+i), end = " ")
  print()