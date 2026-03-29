num = int(input('Enter Basic Amount : '))

DA = 0.10*num
TA = 0.12*num
HRA = 0.15*num
# sum = num * (1 + da + ta + hra)
sum = num * (1 + 0.10 + 0.12 + 0.15)
sum = num * 1.37

print('Dear Allowance : ',DA)
print('Travel Allowance : ',TA)
print('House Rent Allowance : ',HRA)
print('Total Salary : ',sum)