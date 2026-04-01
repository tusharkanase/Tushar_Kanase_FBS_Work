import random
uid = 'tushar.18'
pas = 'tushar@81'

u = input('Emter user ID : ')
p = input('Enter Password : ')

if u == uid and p == pas:
  num = random.randint(1000, 9999)
  print('Enter this number : ',num)

  user_num = input('Enter number : ')

  if user_num == str(num):
    print('Success Login')
  else:
    print('Wrong Captcha')
else:
  print('Wrong user ID or Password')      