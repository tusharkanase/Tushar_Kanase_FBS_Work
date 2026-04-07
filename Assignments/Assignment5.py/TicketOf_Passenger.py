num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_fare = 0

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))
    
    if age < 12:
        total_fare += ticket_cost * 0.7  
    elif age > 59:
        total_fare += ticket_cost * 0.5  
    else:
        total_fare += ticket_cost        

print("Total amount to pay:", total_fare)