# write a function to print numbers from 1 to 10
def num():
    for i in range(1,11):
        print(i)
num()

def num1():
    i=1
    while i<11:
        print(i)
        i+=1
num1()

'''
output:
1
2
3
4
5
6
7
8
9
10
'''

#write a function to print numbers from 10 to 1 in reverse order

def rev():
    for i in range(10,0,-1):
        print(i)
rev()

def rev():
    num=10
    while num>0:
        print(num)
        num-=1
rev()   

'''
output:
10
9
8
7
6
5
4
3
2
1
'''


#write a function to print even numbers from 1 to 20

def even():
    for i in range(1,21):
        if i%2==0:
            print(i)
even()

def even():
    i=1
    while i<21:
        if i%2==0:
          print(i)
        i+=1
even()

'''
output:
2
4
6
8
10
12
14
16
18
20
'''

#write a function to print odd numbers from 1 to 15

def odd():
    for i in range(1,16):
        if i%2!=0:
            print(i)
odd()

def odd():
    num=1
    while num<16:
        if num%2!=0:
            print(num)
        num+=1
odd()

'''
output:
1
3
5
7
9
11
13
15
'''

#write the function to print a square of numbers from 1 to 10

def squ():
    for i in range(1,11):
        print(i*i)
squ()

def squ():
    sq=1
    while sq<11:
        print(sq*sq)
        sq+=1
squ()

'''
output:
1
4
9
16
25
36
49
64
81
100
'''

#write a function to print the cube of numbers from 1 to 5

def cube():
    for i in range(1,6):
        print(i*i*i)
cube()

def cube():
    i=1
    while i<6:
        print(i*i*i)
        i+=1
cube()

'''
output:
1
8
27
64
125
'''

#write a function to print multiplication table of 5

def table(num):
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
table(5)

def table(num):
    i=1
    while i<11:
        print(num,'x',i,'=',num*i)
        i+=1
table(5)

'''
output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

#write a function to calculate sum of numbers from 1 to 100

def sum():
    sum=0
    for i in range(1,101):
        sum=sum+i
    return sum
print(sum())

def sum():
    i=1
    sum=0
    while i<101:
        sum=sum+i
        i+=1
    return sum
print(sum())

#output:5050

#write a function to calculate the sum of only even numbers from 1 to 50

def sum_even():
    sum=0
    for i in range(1,51):
        if i%2==0:
           sum=sum+i
        i+=1
    return sum
print(sum_even())

def sum_even():
    i=1
    sum=0
    while i<51:
        if i%2==0:
            sum=sum+i
        i+=1
    return sum
print(sum_even())

#output:650

#write a function to print factorial of a number

def fac():
    fact=1
    for i in range(1,6):
        fact=fact*i
        i+=1
    return fact
print(fac())

def fac():
    i=1
    fact=1
    while i<6:
        fact=fact*i
        i+=1
    return fact
print(fac())

#output:120