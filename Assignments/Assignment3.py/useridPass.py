correct_userid = 'tushar.18'
correct_password = 'tushar@81'

userid = input('Enter user ID : ')
password = input('Enter Password : ')

if userid == correct_userid and password == correct_password:
  print('Login Successful.')
else:
  print('Invalid user Id or Password')  