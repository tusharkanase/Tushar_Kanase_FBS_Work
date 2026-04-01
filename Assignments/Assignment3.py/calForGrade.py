Marathi = float(input('Enter marks : '))
Hindi = float(input('Enter marks : ' ))
English = float(input('Enter marks : '))
Maths = float(input('Enter marks : '))
History = float(input('Enter marks : '))

per = (Marathi + Hindi + English + Maths + History) / 5
print('percentage : ',per)

if per >= 60:
  print('First Class')
elif per >= 50:
  print('Second Class')
elif per >= 40:
  print('Third Class') 
else:
  print('Fail')     