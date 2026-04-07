num = int(input("Enter a number : "))
temp = num
sum = 0
while temp > 0:
    d1 = temp%10
    fact = 1
    for i in range(1,d1+1):
      fact = fact * i  
    sum += fact
    temp//=10
if sum == num:
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")
