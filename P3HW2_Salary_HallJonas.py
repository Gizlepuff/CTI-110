#Jonas Hall
#6/30/25
#P3HW1
#This code works to use and employee's name,  hours worked, and their pay rate to figure out total pay based on different variables
#Ask for name
#Ask for hours worked
#Ask for pay rate
# If the hours worked > 40
# Calculate overtime
#Overtime hours are 1.5X
#Set regualr hours to 0
#Else:
#Set the OT to 0
#OT pay = 0
#Calcualte regular pay as regular hours
# Gross pay as regular + OT
# all values displayed in a table 

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

print("Employee name:  ", employee_name)
print()
print(f"{'Hours Worked':<13}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
print("-------------------------------------------------------------------------------")
print(f"{hours_worked:<13.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f}"
      f"${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
