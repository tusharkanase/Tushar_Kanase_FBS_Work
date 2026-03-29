num = int(input('Enter the value of Days :'))

num1 = num // 365
num = num % 365

num2 = num // 7
num = num % 7

num3 = num % 7

print(f'years:{num1}, weaks:{num2}, days:{num3} ')
