start = int(input("Enter a start number : "))
end = int(input("Enter a end number : "))
divisor = int(input("Enter a divisor : "))

print(f"number between {start} and {end} divisible by {divisor}")
for i in range(start, end):
  if(i % divisor == 0): 
    print(i)