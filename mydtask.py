my_ds = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency' : 'KES'}], 987,(76,'John')]
#  Print KES
print(my_ds[3][2].get('currency'))

#  Print 560
print(my_ds[2])

#  Print Maths
print(my_ds[3][1])

#  In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]['amount']=90
print(my_ds)

#  Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#  Hint: Strings can be reversed using [::]

# Step 1: Locate the number 987 in the list
# Step 2: Convert it to a string
number_str = str(my_ds[4])  # my_ds[4] is 987

# Step 3: Reverse the string using slicing
reversed_str = number_str[::-1]  # This will give '789'

# Step 4: Convert the reversed string back to an integer
reversed_number = int(reversed_str)  # This will give 789

# Step 5: Replace the original number with the reversed number in the list
my_ds[4] = reversed_number

# Output the modified list
print(my_ds)

#  Change the name “John” to “Jane”.
# # Method  1: Using index

# my_ds = [23, "Jane", 560, ["Lesson", "Maths", {"currency": "KES"}], 789, (76, "John")]

# # Step 1: Access the tuple and replace "John" with "Jane"
# my_ds[5] = (76, "Jane")  # Create a new tuple with "Jane" instead of "John"

# # Output the modified list
# print(my_ds)

# Method  2: Using list comprehension
# Convert the tuple to a list, update the name, and convert it back to a tuple
my_ds[5] = list(my_ds[5])
my_ds[5][1] = "Jane"
my_ds[5] = tuple(my_ds[5])

# Output the modified list
print(my_ds)


