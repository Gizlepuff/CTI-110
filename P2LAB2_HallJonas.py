#Jonas Hall
#6/23/25
#P2LAB2
#This code is supposed to ask you for a vehicle shown then tell you the mpg of the vehicle. You can then tell how many miles you are driving and it gives you a response on how many gallons you will need.
mpg_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }
keys = mpg_dict.keys()
print("Available vehicles", keys)
vehicle = input("Enter the name of a vehicle as shown above: ")
mpg=mpg_dict[vehicle]
print("The", vehicle, "gets", mpg, "miles per gallon.")
miles = float(input("How many miles will you drive?"))
gallons = miles / mpg
print(f"You will need {gallons:.2f} gallons of gas.")
    
