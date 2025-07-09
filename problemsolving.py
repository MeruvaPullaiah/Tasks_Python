#lcm(least common multiple)

n1=29
n2=31
big=0
small=0
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1
if big%small==0:
    print(big)
else:
    lcm_not_found=True
    temp_val=big+big
    while lcm_not_found==True:
        if temp_val%n1==0 and temp_val%n2==0:
            print(temp_val,'is the lcm')
            break
        else:
            temp_val+=big

n1=5
n2=50
big=0
small=0
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1
if big%small==0:
    print(big,'is the lcm')


n1=15 #15 30 45 60 75 90 105 120 135 150
n2=50 # 50 100 150
big=0
small=0
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1
if big%small==0:
    print(big,'is the lcm')
else:
    lcm_not_found=True
    temp_lcm=big+big
    while lcm_not_found==True:
        if temp_lcm%n1==0 and temp_lcm%n2==0:
            print(temp_lcm,'is the lcm')
            break
        else:
            temp_lcm+=big



n1=31 #31 62 93 
n2=59
big=0
small=0
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1
if big%small==0:
    print(big,'is the lcm')
else:
    lcm_not_found=True
    temp_lcm=big+big
    while lcm_not_found==True:
        if temp_lcm%n1==0 and temp_lcm%n2==0:
            print(temp_lcm,'is the lcm')
            break
        else:
            temp_lcm+=big


n1=67
n2=59
big=0
small=0
if n1>n2:
    big=n1
    small=n2
else:
    big=n2
    small=n1
if big%small==0:
    print(big,'is the lcm')
else:
    lcm_not_found=True
    temp_lcm=big+big
    while lcm_not_found==True:
        if temp_lcm%n1==0 and temp_lcm%n2==0:
            print(temp_lcm,'is the lcm')
            break
        else:
            temp_lcm+=big


def function(a,b):
    big=0
    small=0
    if a>b:
        big=a
        small=b
    else:
        big=b
        small=a
    if big%small==0:
        return (big,'is the lcm')
print(function(15,5))


def function(a,b):
    big=0
    small=0
    if a>b:
        big=a
        small=b
    else:
        big=b
        small=a
    if big%small==0:
        return (big,'is the lcm')
    else:
        lcm_not_found=True
        temp_lcm=big+big
        while lcm_not_found==True:
            if temp_lcm%a==0 and temp_lcm%b==0:
                return (temp_lcm,'is the lcm')
            else:
                temp_lcm+=big
print(function(15,50))
print(function(67,59))

def lcm(a,b):
    greater=max(a,b)
    while True:
        if greater%a==0 and greater%b==0:
            return (greater,'is the lcm')
        else:
            greater+=1
print(lcm(15,50))
print(lcm(67,59))



#gcd(greatest common divisior)

n1=20
n2=10
small=0
if n1<n2:
    small=n1
else:
    small=n2    
#small=10
for i in range(1,small+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)

n1=23
n2=11
small=0
if n1<n2:
    small=n1
else:
    small=n2    
#small=10
for i in range(1,small+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)


n1=20
n2=10
small=0
if n1<n2:
    small=n2
else:
    small=n1
gcd=0
for i in range(1,small+1):
    if n1%i==0 and n2%i==0:
        gcd=i
print(gcd)

def gcd(a,b):
    small=0
    if a<b:
        small=b
    else:
        small=a
    gcd=0
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
print(gcd(20,10))
print(gcd(23,11))



#perfect numbers

num=28
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
if s==num:
    print('perfect value')
else:
    print('not a perfect value')


num=28
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
if num==s:
    print('perfect')
else:
    print('not perfect')

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if n==s:
        return 'perfect'
    else:
        return 'not perfect'
print(perfect(6))
print(perfect(28))
print(perfect(20))

#fibonacci series(sum of two previous numbers)
#0 1 1 2 3 5 8 13 21 34 ........

a=0
b=1
for i in range(10):
    print(a)
    c=a+b
    a=b
    b=c


#To find the 31st fibonacci series

a=0
b=1
for i in range(31-1):
    c=a+b
    a=b
    b=c
print(a) 

def fibonacci(n):
    a=0
    b=1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return a
print(fibonacci(31))


#Amstrong number
#153--1**3+5**3+3**3=153

num=153
num1=num
num2=num
count=0
while num!=0:    #153 15  1  0!=0(false condition)
    num=num//10  #15  1   0
    count+=1     #1   2   3

sum=0     #initialize variable to store sum values
while num1!=0:
    last_digit=num1%10       #3   5   1
    sum=sum+(last_digit**3)  #27  27+125=152  27+125+1=153
    num1=num1//10            #15  1   0
if num2==sum:
    print('amstrong')
else:
    print('not amstrong')



def amstrong(num):
    num1=num
    num2=num
    count=0
    while num!=0:
        num=num/10
        count+=1
    sum=0
    while num1!=0:
        last=num1%10 
        sum=sum+(last**3)
        num1=num1//10
    if num2==sum:
        return 'amstrong'
    else:
        return 'not amstrong'
print(amstrong(153))
print(amstrong(167))
print(amstrong(370))
print(amstrong(371))


#TO check sentence there are palindromes are not

sentence="my mummy makes the lunch"
sentence=sentence.split()
for i in range(len(sentence)):
    if sentence[i][::-1]==sentence[i]:
        print('there are palindromes')
    else:
        print('there are no palindromes')
        break


sentence="my mom makes the lunch"
sentence=sentence.split()
for i in range(len(sentence)):
    if sentence[i][::-1]==sentence[i]:
        print('there are palindromes')

#To print a sequence of two strings in alphabetic order
str1='acegik'
str2='bdfhjl'
result=''
for i in range(len(str1)):
    result+=str1[i]+str2[i]
print(result)

def sequence(str1,str2):
    result=''
    for i in range(len(str1)):
        result+=str1[i]+str2[i]
    return result
print(sequence('acegik','bdfhjl'))

s1='13579'
s2='2468'
itr=0
result=''
if len(s1)>len(s2):
    itr=len(s1)
else:
    itr=len(s2)
for i in range(itr):
    if i<len(s1) and i<len(s2):
        result+=s1[i]+s2[i]
    else:
        result+=s1[i]
print(result)



#find the largest word in the sentence

sentence='python is a high level programming language'
sentence=sentence.split(" ")
largest_word=""
for i in range(len(sentence)):
    if len(largest_word) < len(sentence[i]):
        largest_word=sentence[i]
print(largest_word)


def long(sentence):
    sentence=sentence.split(" ")
    longest_word=''
    for i in range(len(sentence)):
        if len(longest_word)<len(sentence[i]):
            longest_word=sentence[i]
    return longest_word
print(long('level programming language'))