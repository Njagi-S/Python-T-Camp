# # A function to calculate an area of a triangle
# def area_of_a_triangle():
#     base = 40
#     height = 70
#     area = (base*height)/2
#     return area

# area_of_a_triangle()

# # Create a function to calculate the area of a rectangle
# def area_of_a_rectangle():
#     length = 30
#     width = 20
#     area1 = length*width
#     return area1

# area_of_a_rectangle()


# def rec_area(len,wid):
#     area2 = len * wid
#     return area2

# rec_area(24,25)
# rec_area(67,90)
# rec_area(33,75)

# # Area of the Triangle using Parameters and arguments
# def tri_area(base,height):
#     area3 = (base * height)/2
#     return area3

# tri_area(23,24)
# tri_area(10,45)
# tri_area(44,80)

# # Write a function that is going to check if a number from input is even or odd
# def even_or_odd(number):
    
#     if number % 2 == 0:
#         result = "Even"
#     else:
#         result = "Odd"
#     return result

# num = int(input("Enter Your Number: "))
# x=even_or_odd(num)
# print(f"The Number is : {x}")

# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
def largest_input(num1,num2,num3,num4):
    if num1 > num2 and num1 > num3 and num1 > num4:
        largest = f"Number One Is The Largest Number: {num1}"
    elif num2 > num1 and num2 > num3 and num2 > num4:
        largest = f"Number Two Is The Largest Number: {num2}"
    elif num3 > num1 and num3 > num2 and num3 > num4:
        largest = f"Number Three Is The Largest Number: {num3}"
    else:
        largest = f"Number Four Is The Largest Number: {num4}"
    return largest

largest_Number1 = int(input("Enter The First Number: "))
largest_Number2 = int(input("Enter The Second Number: "))
largest_Number3 = int(input("Enter The Third Number: "))
largest_Number4 = int(input("Enter The Fourth Number: "))
final_number = largest_input(largest_Number1,largest_Number2,largest_Number3,largest_Number4)
print(final_number)


        
    



