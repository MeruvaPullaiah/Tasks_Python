
'''num=int(input('enter the number:'))
if num>=00:
    print('positive')
if num<0:
    print('negative')
if num==0:
    print('zero')
else:
    print('none')'''

'''day=int(input('enter the day:'))
match day:
    case 1:
        print('sunday')
    case 2:
        print('mon')
    case 3:
        print('tues')
    case 4:
        print('wed')
    case 5:
        print('thurs')
    case 6:
        print('fri')
    case 7:
        print('sat')'''

'''mob=9848022338
total=0
while mob!=0:
    last=mob%10
    if last%2==0:
        total+=last
    mob=mob//10
print(total)'''

#write a function to print odd numbers frm 1 to 20

'''def odd_num():
    for i in range(1,21):
        if i%2!=0:
            print(i) 
odd_num()'''
# find factorial using while loop
'''=5
fact=1
while n>1:
    fact=fact*n
    n-=1
print(fact)'''

#using fun
'''def fac():
    n=5
    fact=1
    while n>1:
        fact=fact*n
        n-=1
    return fact
print(fac())
print(fac())'''

#sum of numbers 

'''i=1
total=0
for i in range(1,6):
    total=total+i
print(total)'''

'''n=5
total=0
while n>0:
    total=total+n
    n-=1
print(total)'''

'''def sum_num():
    n=5
    total=0
    while n>0:
        total=total+n
        n-=1
    print(total)
sum_num()

def sum_num():
    total=0
    for i in range(1,6):
        total=total+i
    print(total)
sum_num()

def sum_num(n):
    total=0
    while n>0:
        total=total+n
        n-=1
    return total
print(sum_num(5))'''

'''def odd_num():
    for i in range(1,21):
        if i%2!=0:
           print(i)
odd_num()'''

'''def odd_num():
    i=1
    while i<21:
        if i%2!=0:
            print(i)
        i+=1
odd_num()

def string():
    str="madam"
    rev=str[::-1]
    if str==rev:
        print('palindrome')
    else:
        print('not a palindrome')
string()

def sum_num():
    num=10
    total=0
    while num>0:
        total=total+num
        num-=1
    print(total)
sum_num()

def sum_num():
    total=0
    for i in range(1,11):
        total=total+i
    print(total)
sum_num()

def div():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print(i)
div()


def rev():
    num=1234
    rev=0
    while num!=0:
        last_digit=num%10
        rev=rev*10+last_digit
        num=num//10
    print(rev)
rev()'''
'''for i in range(10):
    if i==3:
        break
    print(i)

for i in range(10):
    if i==5:
        continue
    print(i)

print(oct(8))'''

                #output:11


'''
#Arithmetic operators using functions

def add(num1,num2):
    print(num1+num2)
add(6,7)                  #output:13

def sub(num1,num2):
    print(num1-num2)
sub(9,7)                  #output:2

def mul(num1,num2):
    print(num1*num2)
mul(4,5)                  #output:20

def power(num1,num2):
    print(num1**num2)
power(2,3)                #output:8

def div(num1,num2):
    print(num1/num2)
div(6,3)                  #output:2.0

def floordiv(num1,num2):
    print(num1//num2)
floordiv(9,3)             #output:20


print(len("hello"))      # Built-in print() & len()
print(max(3, 7, 5))      # Built-in max()
print(abs(-10))          # Built-in abs()


def analyze_list(numbers):
    print("Length is", len(numbers))
    print("Sum is", sum(numbers))
    print("Max is", max(numbers))

analyze_list([3, 1, 4, 1, 5])
'''
#string ia collection of characters with singel queotes and double quotes


