# fruits =["Apple","Banana","Cherry","Avocado"]
# for fruit in fruits:
#     print("These are the available fruits: ",fruit)


# # Range Function =>

# x = [1,2,3,4,5,6,7,8,9,10]
# y = list(range(1,11))
# num = list(range(1,1000,200))
# print(num)

# for bert in range(1,100,2):
#     if bert >= 80:
#         print(bert)

# # iterate though numbers 20 - 100 and only display even numbers

# numbers = list(range(20,101))
# even_numbers = []
# for i in numbers:
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)

# break => USed to stop the loop

ls1 = list(range(20,50))
res = []
for i in ls1:
	if i == 30:
		break
	if i%2==0:
			res.append(i)
	else:
	    pass

print(res)




