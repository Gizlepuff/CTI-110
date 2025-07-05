#Jonas Hall
#7/5/25
#P4HW1
#Enter in score and get a list of them, average and the letter grade assiociated with the number
#Psudocode:
#Prompt to enter score
# Read the number given
#Collect all scores and find lowest and drop it from list
#Calculate average without lowest
num_scores = int(input("How many scores would you like to enter? "))

score_list = []

i = 0
while i < num_scores:
    score = float(input(f"Enter score #{i + 1}: "))
    if 0 <= score <= 100:
        score_list.append(score)
        i += 1  
    else:
        print("Invalid score. Please enter a value between 0 and 100.")

lowest_score = min(score_list)
print(f"\nLowest score entered: {lowest_score}")

modified_scores = score_list.copy()
modified_scores.remove(lowest_score)

print(f"Score list after dropping lowest score: {modified_scores}")

if modified_scores:
    average = sum(modified_scores) / len(modified_scores)
else:
    average = 0

print(f"Average of modified score list: {average:.2f}")

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Letter grade for average: {grade}")
