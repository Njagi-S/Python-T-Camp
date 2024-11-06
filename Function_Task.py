# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

# Taking user input
maths = int(input("Enter marks for Maths: "))
english = int(input("Enter marks for English: "))
kiswahili = int(input("Enter marks for Swahili: "))
science = int(input("Enter marks for Science: "))
social_studies = int(input("Enter marks for Social Studies: "))

def calculate_total(mathss, eng, swa, sci, sos):
    total_marks = mathss + eng + swa + sci + sos
    return total_marks
# Calculating total
total = calculate_total(maths, english, kiswahili, science, social_studies)


def calculate_average(totalmarks):
    avg = totalmarks / 5
    return avg

# Calculating average
average = calculate_average(total)

def determine_grade(average):
    if average > 79:
        return 'A'
    elif 60 <= average <= 79:
        return 'B'
    elif 49 <= average < 60:
        return 'C'
    elif 40 <= average < 49:
        return 'D'
    else:
        return 'E'

# Determining grade
grade = determine_grade(average)

# Outputting the results
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
