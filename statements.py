if 20>40 :
    print("The given Number is Greater  than 40")

else:
    print('The given Number is less than 40')
    
# Declare a variable marks then check if the marks is above 50 print pass, otherwise print fail
gmarks =int(input("Enter your gmarks: "))
if gmarks >50 and gmarks<100:
    print("PASS")
else:
    print("FAIL")
    
# Declare a variable number then if the number is even (print even) otherwise print odd
number = int(input("Enter a number: "))
if number %2 == 0:
    print("This is an Even Number")
else:
    print("This is an Odd Number")
    
    
# if elif else

marks=int(input("Enter your marks: "))
if marks >=0 and marks <= 100:
    if marks >=90 and marks <= 100:
        print("You scored an A")
    elif marks >=80 and marks <90:
        print("You scored a B")
    elif marks >=70 and marks <80:
        print("You scored a C")
    elif marks >=60 and marks <70:
        print("You scored a D")
    elif marks >=50 and marks <60:
        print("You scored an E")
    else:
        print("You failed!")
else:
    print("Enter Valid marks")

# Write a program that takes age from users input
#if the age is 60 or above print  you are senior citizen
#if age is 18 and  above but less than 60 print you are an adult
#else print you are a minor

age = int(input("Please Enter your age: "))
if age  >= 60:
    print("You are a Senior Citizen")
elif age >= 18 and age < 60:
    print("Your are an Adult")
else:
    print("You are a Minor")
    
# Nested if Statements
# You give 100 discount on purchase 1000
# You give 200 discount on purchase 5000
# no discount

purchase=int(input("Enter Your Purchase price: "))
if purchase > 1000:
    print("You Have a discount of 100 Kshs")
    if purchase  > 5000:
        print("You Have a discount of 200 Kshs")
else:
    print("No Discount")

    
    
# Write a program that:
# =>Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above $50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score = int(input("Please enter your credit score:"))
if credit_score >700:
    annual_income= int(input("Please enter your annual income:"))
    if annual_income >50000:
        print("Loan Approved.")
    else:
        print("Income requirement has not been met.")
else:
    print("Your credit score is too low.")


