# Create a tuple
marks=(100,300,160,250,450,600)
print (type(marks))

#Converting To a List
marks=list(marks)
print(type(marks))

#Coverting to a tuple
marks=tuple(marks)
print(type(marks))


days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
#1. Find Wednesday using the index
print(days[2])

#2. Using a function find the lenght of the tuple
print(len(days))

#3.Replace Thursday with Thur
days=list(days)
days[3]="Thur"
days=tuple(days)
print(days)

my_tuple=("age",14,"Location","Kiambu",[100,300,500])
my_tuple[4][1]=1000
print(my_tuple)