# Define a class named car

class Car:
    # Constructor Method
    def __init__(self,color,brand,shape):
        self.color = color
        self.brand = brand
        self.shape = shape
    
    def describe(self):
        return f"The color of this car is {self.color}, the brand is {self.brand} and the shape is {self.shape}."

mycar = Car("Black","Mercedes","Wagon")
car1 = Car("Green","Audi","Sedan")
car2 = Car("Orange","BMW","HatchBack")

# Printing Specific Attributes
print(mycar.color)
print(car1.brand)
print(car2.shape)

# Printing All the Attributes (the entire description of the car)
print(mycar.describe())
print(car1.describe())
print(car2.describe())

# Create a class called Student with attributes name and age.
# Add a method introduce that prints: "Hello, my name is [name] and I am [age] years old."
# Create an object of Student and call the introduce method.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

student=Student("John Doe",24)

print(student.introduce())


# Define a class Calculator with methods add, subtract, multiply, and divide that perform the respective operations on two numbers.
# Create an object of Calculator and use it to perform some calculations.
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1 / self.num2

# Perform calculations
num_x = float(input("Enter The First Number: "))
num_y = float(input("Enter The Second Number: "))

# Create a Calculator object
my_calculator = Calculator(num_x,num_y)

addition = my_calculator.add()
subtraction = my_calculator.subtract()
multiplication = my_calculator.multiply()
division = my_calculator.divide()

print(f"The result of {num_x} + {num_y} is: {addition}")
print(f"The result of {num_x} - {num_y} is: {subtraction}")
print(f"The result of {num_x} * {num_y }is: {multiplication}")