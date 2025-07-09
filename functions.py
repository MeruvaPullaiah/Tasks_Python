#Add numbers without using parameters and arguments
def add():
    print(1+2)
add()           #output:3

#Every implicity returns non
def greet():
    pass
print(greet())   #output:None

#Add numbers using parameters and arguments
def add_numbers(num1,num2):
    print(num1+num2)
add_numbers(9,2)         #output:11
add_numbers(4,6)         #output:10

#return statement
def greet():
    return "hello"
print(greet())          #output:hello

def greet():
    print("hello")
    return "world"
print("hi")
print(greet())
'''output:
hi
hello
world
'''
#parameters and arguments

def add(a,b):
    result=a+b
    return result
print(add(10,20))      #output:30

#function with default values
def coffee_shop(type, sugar="no"):
    return type + sugar
print(coffee_shop('coffee' ))       #output:coffeeno

def add(a,b=100):
    return a+b
print(add(10))       #output:110

#function with Reassignment
def add(a=100,b=200):
    a=500
    b=400
    return a+b
print(add(10,20))     #output:900

#position and keyword arguments
def biryani(item1,item2):
    return item1+item2
print(biryani('chicken','rice'))      #position argument
print(biryani(item1='mutton',item2='chicken'))   #keyword argument

# *args-----collection of data stores in list
def marks(*args):
    print(*args)
marks(43,44,88,67,10,36,8)

# **kwargs----stores in dictionary

def person(**kwargs):
    print(**kwargs)
person(age=25,name='nani',weight='6',loc='hyd')

#lambda function ----it a anonymous function and single line code

add=lambda p1,p2:p1+p2
print(add(4,6))            #output:10
 
sub=lambda p1,p2:p1-p2
print(sub(9,3))            #output:6

#lambda function with default value
add=lambda p1,p2=200:p1+p2
print(add(10))            #output:210

