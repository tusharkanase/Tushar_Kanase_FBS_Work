num = int(input('Enter the Number : '))
if num > 1:
  for i in range(2,num):
      if(num%i==0):
         print(f'{num} is not prime number.')
         break
  else:
     print(f'{num} is prime number.') 
else:
   print('Num is not prime number.')     