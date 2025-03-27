def greet():
     print("Hello form this side  ")

greet()


# function with perameter 
def greet(name):
     print("Hello from ", name)

greet("rohit")


# function with return value

def add(a,b):
     return a+b
result = add(4,3)
print(result)

# multiple return value ******
def math_opration(a,b):
     return a+b,a-b,a*b
sum, diff, multi =  math_opration(2,3)
print("sum : ", sum ,"diff:",diff,"multi:",multi)

# lambda function -> one line function
square = lambda x:x*x
print(square(4))

# check number is even of not 
def  isEven(num):
     return num%2==0
print(isEven(4))