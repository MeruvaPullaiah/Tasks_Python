#print 1 to 10

a=1
while a<11:
    print(a)
    a+=1

#print 10 to 1 in reverse
b=10
while b>0:
    print(b)
    b-=1

#even numbers from 1 to 20
even=1
while even<21:
    if even%2==0:
        print(even)
    even+=1

#odd numbers from 1 to 30

odd=1
while odd<31:
    if odd%2!=0:
        print(odd)
    odd+=1

#squares from 1 to 10
sq=1
while sq<11:
    print(sq*2)
    sq+=1

#multiplication table fo 5

mul=1
while mul<11:
    print('5','X',mul,'=',5*mul)
    mul+=1

#cube of numbers from 1 to 5
cube=1
while cube<6:
    print(cube*cube*cube)
    cube+=1

#sum of numbers from 1 to 100
s=1
sum=0
while s<101:
    sum=s+sum
    s+=1
print(sum)

#sum of only even numbers from 1 to 10
e=1
sum=0
while e<11:
    sum=e+sum
    e+=1
print(sum)

#product of numbers from 1 to 5(without function)

product=1
mul=1
while product<6:
    mul=product*mul
    product+=1
print(mul)


#reverse a number

n=123
rev=0
while n!=0:
    last_digit=n%10
    rev=rev*10+last_digit
    n=n//10
print(rev)

print(123%10)
print(123//10)

#sum of mobile number 9848022338

mob=9848022338
total=0
while mob!=0:
    last_digit=mob%10
    total+=last_digit
    mob=mob//10
print(total)

#sum of mobile number 9848022338 to find even

mob=9848022338
total=0
while mob!=0:
    last=mob%10
    if last%2==0:
        total+=last
    mob=mob//10
print(total)