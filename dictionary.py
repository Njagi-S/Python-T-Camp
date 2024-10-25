person={
    "name":"Sheldon",
    "age":24,
    "gender":"Male",
    "location":["Kiambu",518,"Thika"],
    "address": {
        'street':"Muthaiga",
        "city":"Nairobi",
        "country":"Kenya",
    }  
}
print(type(person))
print(person)

 #.Display Name
print(person['name'])

 #.Display Age
print(person['age'])

 #.Display Gender
print(person['gender'])

 #.Display 518 
print(person['location'][1])

 #.Display Thika
print(person["location"][2])

#.Display Kenya
print(person["address"]['country'])

#.Display City
print(person['address']['city'])

#.Display Street
print(person['address']['street'])

#UPDATING VALUES
#updating location
person['location']=['Meru',60200,'Makutano']

#updating a new property(key:value)
person['occupation']='Developer'
print(person)



#DICTIONARY METHODS

#1. key()=> returns all the keys in the dictionary
print(person.keys())

#2.  values()=> returns all the values in the dictionary
print(person.values())

#3.  items()=> returns all the key-value pairs in the dictionary
print(person.items())

#4.  pop()=> removes the values  of the key specified
#.Removing Occupation
person.pop('occupation')
print(person)

#5.  get()=>  returns the value of the key specified
#.Getting the value of location
print(person.get('location'))

employee = {
  "id": 1701,
  "name": "James T Kirk",
  "email": "jtkirk@starfleet.com",
  "position": "captain",
}

# Add your code below:
print(employee.get('email'))




