n = 5
x = 2
a = 2

sum_a = 0
fact = 1
for i in range(1, n+1):
  fact = fact * i
  sum_a = sum_a + fact
print("a:",sum_a)  

sum_b = 0
for i in range(1, n+1):
  sum_b = sum_b + n**i
print("b:",sum_b)  

sum_c = 0
term = 1
for i in range(1, n+1):
  sum_c = sum_c* 2
  term = term* 2
print("c:", sum_c)

sum_d = 0
for i in range(1, 11):
  sum_d = sum_d + (a**i / i)
print("d:", sum_d) 

sum_e = 0
den = 1
sign = 1
for i in range(1, n+1):
  sum_e = sum_e + (x**i / den) * sign
  den = den + 2
  sign = sign * -1
print("e:", sum_e)  