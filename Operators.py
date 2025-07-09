#1.Arithmetic operators
a=10
b=20
#Addiction
print(a+b)  #output:30

#Subtraction
print(a-b)  #output:-10

#Multiplication
print(a*b)   #output:200

#Division
print(a/b)  #output:0.5

#Floor Division 
print(a//b)  #output:0

#Modulo  
print(a%b)   #output:10

#Exponentiation
print(a**b)  #output:100000000000000000000


#2.Assignment operators
#Simple Assignment
c=10   

#Add and Assign
d=10
d+=2    
print(d)   #output:12

#Sub and Assign
e=10
e-=3    
print(e)   #output:7

#Mul and Assign
f=10
f*=2     
print(f)   #output:20

#Divide and Assign
g=10
g/=2    
print(g)  #output:5.0

#Floor Divide and assign
h=10
h//=2   
print(h)  #output:5

#Modulo and Assign
i=10
i%=2    
print(i)  #output:0

#Exponentiate and Assign
j=10
j**=2 
print(j)  #output:100

#3.compariosn operators
a=2
b=4
#Equal to(==)
print(a==b)    #output:False

#Not Equal to(!=)
print(a!=b)    #output:True

#Greater(>)
print(a>b)     #output:False

#Lessthan(<)
print(a<b)     #output:True

#Greater than or Equal to(>=)
print(a>=b)    #output:False

#Less than or equal to(<=)
print(a<=b)    #output:True

#4.Logical operators
a=10
b=20
c=5

#and
print((a>b) and (a>c))   #output:False
#or
print((a>b) or (a>c))    #output:True
#not
print(not (a==4))        #output:True


#5.Identity operators

a=[1,2,3,4]
b=[1,2,3,4]
#is
print(a is b)  #output:False

#is not
print(a is not b)  #output:True

#6.Membership operator

a=[1,2,3,4,5]
#in
print(3 in a)       #output:True

#not in 
print(6 not in a)   #output:True




#7.Bitwise operators
#Bitwise AND(&)
a = 10  # 1010₂  
b = 8   # 1000₂  
print(a & b)     #output: 8 (1000₂)  
#Bitwise OR(|)
a = 15  # 1111₂  
b = 10  # 1010₂  
print(a | b)     #output: 15 (1111₂)
#Bitwise XOR(^)
a = 15  # 1111₂  
b = 10  # 1010₂  
print(a ^ b)     #output:5 (0101₂)
#Bitwise NOT(~)
a = 10
print(~a)       #output: -11
#Bitwise LeftShift(<<)
a = 9      # 1001₂  
print(a << 1)      #output: 18 (10010₂)  
print(a << 2)      #output: 36
#Bitwise RightShift(>>)
a = 22     # 10110₂  
print(a >> 1)      #output: 11 (1011₂)  
print(a >> 2)      #output: 5
