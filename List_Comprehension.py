# Offers a concise way to create a new list from another list.
# Create a list of even_numbers from numbers between 20 and 100
# Normal Loop
even = []
for i in range(20,101):
    if i % 2 == 0:
        even.append(i)

print(even)

# Using list comprehension to create a new list from another list
even_numbers = [i for i in range(20, 101) if i % 2 ==0]
print(even_numbers)

# Store in a list a square of numbers between 1 and 20
# Normal Way
square = []
for i in range (1,21):
    square.append(i**2)

print(square)

# Using list comprehension to create a new list from another list
square_numbers = [i**2 for i in range(1,21)]
print(square_numbers)