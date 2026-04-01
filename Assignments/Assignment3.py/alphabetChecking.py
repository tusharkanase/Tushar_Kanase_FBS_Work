check = input('Enter an alphabet: ')

if check.isalpha() and len(check) == 1:
  if check.lower() in ['a', 'e', 'i', 'o', 'u']:
    print('It is vowel')
  else:
    print('It is consonant')
else:
  print('Please enter a single valid alphabet')