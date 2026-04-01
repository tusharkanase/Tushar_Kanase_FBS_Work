x = float(input('Enter first side: '))
y = float(input('Enter second side: '))
z = float(input('Enter third side: '))

if x > 0 and y > 0 and z > 0 and (x + y > z) and (x + z > y) and ( y + z > x):

   if z == y == z:
      print('The triangle is equilateral.')
   elif x == y or y == z or x == z:
      print('The triangle is isosceles.')
   else: 
      print('The triangle is scalene.')

else:
   print('Invalid triangle.')       