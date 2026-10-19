# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
if name.strip() == "":
    print("Error: Name must not be empty.")
    name = input("Please enter a valid name: ")
    
distance = float(input("Enter distance (km): "))
if distance <= 0:
   print("Error: Distance must be greater than 0.")
   distance = input("Please enter a distance greater than 0: ")

passengers = int(input("Enter number of passengers: "))
if passengers  <= 0:
    print("Error: passengers must be a postive whole number.")
    passengers = input("Please enter a number of passengers more than 0: ")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
