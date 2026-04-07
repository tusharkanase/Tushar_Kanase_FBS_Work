number = int(input("Enter the number : "))
num1 = str(number)
num2 = len(num1)

sum = 0
for digit in num1:
  sum += int(digit) ** num2

if (sum == number): 
  print(number, "is armstrong number.")
else:
  print(number,"is not an armstrong number.")  