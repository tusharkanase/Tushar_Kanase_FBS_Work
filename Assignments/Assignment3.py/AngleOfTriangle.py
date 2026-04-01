x = float(input('Enter first angle: '))
y = float(input('Enter second angle: '))
z = float(input('Enter third angle: '))

if x > 0 and y > 0 and z > 0 and (x + y + z) == 180:
  print('The triangle is valid')
else:
  print('The triangle is not valid')
