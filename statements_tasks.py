# 1. Take three inputs from a user, separately. Print the largest of the numbers.
# Hint: Determine what type of data is taken in as input.

num1=int(input('Enter the first number: '))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1 >  num2 and num1 > num3:
    print("The  largest number is number one:",num1)
elif num2 >  num1 and num2 > num3:
    print("The largest number is number two:",num2)
else:
    print("The largest number is number three:",num3)

# 2. Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temperature=int(input("Please enter your temperature: "))
if temperature > 15 and temperature  <= 30:
    print("Normal temperature.")
elif temperature > 30:
    print("The temperature is too hot.")
else:
    print("Cold temperature.")

# 3. Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print
# "Conditions not met"
x = int(input("Enter the number x: "))
y = int(input("Enter the number y: "))
if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access granted", otherwise print "Access denied"
password = input("Please enter your password: ")
if  password == "secret123":
    print("Access granted")
else:
    print("Access denied!")

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score = float(input("Please enter the student's score: "))
attendance = int(input("Please enter the student's attendance: "))
if student_score in range(0,101) and attendance in range(0,101):
    if student_score > 90 and attendance > 80:
        print("Excellent Student.")
    else:
        print("Good score, but attendance needs improvement.")
else:
    print("Invalid score or attendance.")

#6. Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."

account_type = input("Enter your account type (Standard/Premium): ")
transaction_amount = float(input("Enter your transaction amount: "))

if account_type == "Standard":
    if transaction_amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "Premium":
    if transaction_amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("Invalid account type. Please enter 'Standard' or 'Premium'.")
