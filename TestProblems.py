#Check if a number is Even,Odd or Zero using if,elif,else
#example Input:7

num=7
if num%2==0:
    print('Even')
elif num==0:
    print('Zero')
else:
    print('Negative')
#output:Negative

#check positive,negative,zero
#Example Input=-2

num=-2
if num>0:
    print('positive')
elif num==0:
    print('zero')
else:
    print('negative')
#output:negative

#find the greatest of two numbers
#Example Input=10,20

n1=10
n2=20
if n1>n2:
    print('n1 is greater than n2')
else:
    print('n2 is greater than n1')

#output:n2 is greater than n1

#check if a person is Eligible to vote
#Example Input=16

Age=16
if Age>=18:
    print('Eligible to Vote')
else:
    print('Not Eligible to Vote')

#output:Not Eligible to Vote

#check if a number is a multiple of 3 or 5
#Example Input=15

num=15
if num%3==0 or num%5==0:
    print('Multiple of 3 or 5')
else:
    print('Not Multiple')

#output:Multiple of 3 or 5


#print numbers from 10 to 1 in reverse order

for i in range(10,0,-1):
    print(i,end=' ')
#output:10 9 8 7 6 5 4 3 2 1


#print even numbers between 1 to 20

for i in range(1,21):
    if i%2==0:
        print(i,end='  ')

for i in range(2,21,2):
    print(i,end='  ')
#output:2  4  6  8  10  12  14  16  18  20

#sum of first N natural numbers 
#Example Input=5
num=5
total=0
for i in range(1,num+1):
    total=total+num
    num+=1
print(total)
#output:35

#multiplication table of a number
#Example Input=3

num=3
for i in range(1,11):
    print(num,'x',i,'=',num*i)
#output:
'''
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
'''
#factorial of a number
#Example Input=4
num=4
fact=1
for i in range(1,num+1):
    fact=fact*num
print(fact)

#output:256

#write a function to print odd numbers between 1 to 20

def odd_num():
    for i in range(1,21):
        if i%2!=0:
            print(i)
odd_num()
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
17
19
'''

#write a function to check if a string is a palindrome
#Example Input:madam

def string():
    str='madam'
    rev=str[::-1]
    if str==rev:
        print('palindrome')
    else:
        print('not palindrome')
string()

#output:palindrome


#write a function to return the sum of even numbers from 1 to 10

def sum_even():
    n=10
    total=0
    while n>0:
        total=total+n
        n-=1
    return total
print(sum_even())

#output:55

#write a function to print numbers divisible by both 3 and 5 in range 1-50

def div():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print(i)
div()

'''
output:
15
30
45
'''

#write a function to reverse a number
#Example Input:1234

def rev():
    num=1234
    rev=0
    while num!=0:
        last_digit=num%10
        rev=rev*10+last_digit
        num=num//10
    return rev
print(rev())

#output:4321