#Jonas Hall
#6/23/25
#P2HW1
#This code is used to ask for certain expenses and where you are going. It will list said expenses and compare it with your budget.
print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget:"))
destination =(input("Enter Your Travel Destination:"))
gas_cost = float(input("How Much Do You Think You Will Spend on Gas?:"))
hotel = float(input("Approximately, how much will you need for a hotel?:"))
food = float(input("Last, how much do you need for food?:"))
total_spent = gas_cost + hotel + food
remaining_balance = budget - total_spent
print("------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas_cost:.2f}")
print(f"{'hotel:':20}${hotel:.2f}")
print(f"{'Food:':20}${food:.2f}")
print("---------------------------------------")
print(f"Remaining Balance: ${remaining_balance:.2f}")
