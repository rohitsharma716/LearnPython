# List in python
 
fruits = ["Apple", "Banana", "Cherry"]
print(fruits) 
print(fruits[-1])  # this is new for me 👍


fruits.append("mango")
print(fruits)

fruits.insert(1,"Orange")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("Apple")
print(fruits)

# Tuples in python
# A tuple is like a list, but immutable (cannot be changed after creation).

color = ("pink" , "orange" , "purpal")
# color[0] ="blue"  -> ❌ this opration is in not possilbe 



# Dictionaries (dict) in Python
person ={ 
      "name": "rohit sharma",
      "age" : 24,
      "job" : "software engineer"
 }

print(person)
print(person["name"])
person["city"] ="new delhi"

person.pop("job")

for  key , value in person.items():
     print(key,":",value)

#set in python
number ={1,2,3,4,5,5}
print(number)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}




