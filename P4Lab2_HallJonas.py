#Jonas Hall
#7/5/25
#P4LAB2
#Runs a muiltiplacation table and asks if you want to add more numbers when prompted yes, no = stops working
run_program = "yes"
while run_program == "yes":
    user_input = int(input("Enter an integer: "))

    if user_input >= 0:
        print(f"Multiplication table for {user_input}:")
        for i in range(1, 13):
            print(f"{user_input} x {i} = {user_input * i}")
    else:
        print("This Program Does Not Handle Negative Number.")

    run_program = input("Do you want to run the program again? (yes/no): ")
print("Goodbye!")
