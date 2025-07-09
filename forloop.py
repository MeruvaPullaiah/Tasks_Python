#print numbers from 1 to 10 using for loop
for i in range(1,11):
    print(i)

#print numbers from 10 to 1 in reverse order using for loop
for j in range(10,0,-1):
    print(j)

#print all even numbers from 1 to 20
for even in range(1,21):
    if even%2==0:
        print(even)

for even1 in range(1,21):
    print(even1)


#print the square of numbers from 1 to 10
for square in range(1,11):
       print(square**2)

#print the cube of numbers from 1 to 5
for cube in range(1,6):
    print(cube**3)


#print the sum of numbers from 1 to 100 using a for loop
sum=0 
for s in range(1,101):
    sum+=1
    print(sum)

#print the multiplication table of 5
num=5
for m in range(1,11):
    print(f"{num}x{m}={num*m}")

#calculate the sum fo numbers from 1 to 100 using for loop
for a in range(1,101):
    sum=sum+a
    a+=1
print(sum)

#calculate the sum of only even numbers from 1 to 50
for b in range(1,51):
    if b%2==0:
        sum=sum+b
    b+=1
print(sum)

#calculate the product of numbers from 1 to 5
mul=1
for c in range(1,6):
    mul=mul*c
    i+=1
print(mul)
