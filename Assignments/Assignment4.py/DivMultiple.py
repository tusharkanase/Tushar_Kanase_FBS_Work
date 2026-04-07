start = int(input("Enter a star number : "))
end = int(input("Enter a end number : "))

print("number is divisible by 7 and multiplie by 5")
for i in range(start, end):
  if(i%7 == 0 and i%5 == 0): 
    print(i)
    