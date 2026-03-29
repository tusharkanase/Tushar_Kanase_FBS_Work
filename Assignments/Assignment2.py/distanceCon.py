num1 = float(input('number of Feet : '))
num2 = float(input('number of Inches : '))

sum1 = (num1*12) + num2
sum2 = sum1*2.54
sum3 = sum2/100

print(f'{sum1} Meters, {sum2} Centimeters')