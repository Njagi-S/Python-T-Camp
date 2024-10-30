# 1. Write a program that displays a numbers 1 to 50 inside a list.
l1 = list(range(1,51))
nums = []
for i in l1:
    nums.append(i)
print("The Numbers from 1 to  50 are: ", nums)


# 2. From 1 above display the ones divisible by 7 or 5 inside a list.
nums1 = []
for ty in l1:
    if ty % 7 == 0 or ty % 5 == 0:
        nums1.append(ty)
print("The numbers divisible by 7 or 5 between 1 and 50 are: ",nums1)
        
# 3. Find sum and average of values in the range between 10 to 40.
values_to_forty = []
total_sum = 0
for i in range(10,41):
    values_to_forty.append(i)    
    total_sum += i
    average = total_sum / len(values_to_forty)
print("The sum of numbers  between 10 and 40 is: ",total_sum)
print("The average of the sum of numbers from  10 to 40 is: ",average)

# 4. Put in a list the first 10 odd numbers between 10 to 50.
# Step 4: Put in a list the first 10 odd numbers between 10 to 50
odd_numbers = []
for odds in range(10, 50):
    if odds %  2 != 0:
        odd_numbers.append(odds)
    if len(odd_numbers) == 10:
        break
print("The first 10 odd numbers between 10 and 50:", odd_numbers) 

# 5. write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# Taking input from the user
user_input = int(input("Enter a number: "))

print(f"Multiplication table for {user_input}:")

# Loop to print the multiplication table
for i in range(11):
    result = user_input * i
    print(f"{user_input} x {i} = {result}")

# 6. write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even_numbers=[]
for i in range(1,50):
    if i % 2 == 0:
        even_numbers.append(i)

print("The  number of even numbers between 1 and 50 is:", len(even_numbers))
print("The number of even numbers between 1 and 50 ares:",even_numbers)
        

# 7. Display the total quantity of the 3 below.
ls1 = [ ("Jay", 20), ("Mo", 30), ("Mya", 32) ]
# Initialize total quantity
total_quantity = 0
# Loop through each tuple in the list
for t in ls1:
    amount =t[1]
    total_quantity += amount
# Display the total quantity
print("Total quantity:", total_quantity)
