start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
print(f"The Odd number from {start} to {end} are : ")
for i in range(start,end+1):
     if(i%2 != 0):
      print(i)
      