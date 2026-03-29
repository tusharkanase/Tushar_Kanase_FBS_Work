
Principle_Amount = float(input('Enter principle amount : '))
Rate = float(input('Enter Rate : '))
Time = float(input('Enter Time : '))

compound_interest = Principle_Amount * (1 + Rate/100)**Time-Principle_Amount

print('Compound Interest is : ',compound_interest)
