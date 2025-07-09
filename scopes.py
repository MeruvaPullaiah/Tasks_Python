#1.Local Scope
def greet():
    message = "Hi!"
    print(message)  # works
greet()
print(message)  # NameError: not defined

#2.Enclosing Scope (Nested Functions)
def outer():
    x = 'outer'
    def inner():
        print(x)     # finds x in enclosing scope
    inner()
outer()

#3.Global Scope
x = 10
def print_x():
    print(x)      # prints 10
print_x()

#4.Built-in Scope

def analyze_list(numbers):
    print("Length is", len(numbers))     #Length is 5
    print("Sum is", sum(numbers))        #Sum is 14
    print("Max is", max(numbers))        #Max is 5
analyze_list([3, 1, 4, 1, 5])
