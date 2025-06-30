money = float(input("Enter the amount of money as a float: $"))

cents = int(money * 100)

if cents == 0:
    print("No change")
else:
    
    dollars = cents // 100
    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")
    cents = cents - (dollars * 100)

    quarters = cents // 25
    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")
    cents = cents - (quarters * 25)

    dimes = cents // 10
    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")
    cents = cents - (dimes * 10)
    
    nickels = cents // 5
    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")
    cents = cents - (nickels * 5)
    
    pennies = cents
    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(f"{pennies} Pennies")
