#Jonas Hall
#6/23/25
#P2HW2
#Asks user to enter grades for certain modules then gives them the lowest, highest, sum of all, and the average
#Pseudocode Starts Here:
#Ask user to enter grade for modules 1-6
#Store it in a list
# Use some simple functions to do the calculations
#Get average by dividing sum by number of grades
#Psudocode Ends Here
grade1 = float(input("Enter grade for Module 1:"))
grade2 = float(input("Enter grade for Module 2:"))
grade3 = float(input("Enter grade for Module 3:"))
grade4 = float(input("Enter grade for Module 4:"))
grade5 = float(input("Enter grade for Module 5:"))
grade6 = float(input("Enter grade for Module 6:"))
grades = [grade1, grade2, grade3, grade4, grade5, grade6]
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)
print("------------Results------------")
print(f"Lowest Grade:     {lowest}")
print(f"Highest Grade:    {highest}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {average:.2f}")

