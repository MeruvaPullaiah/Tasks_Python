#1.abs---returns positive

print(abs(-10))
print(abs(10))

#2.round()

print(round(0.34+0.34,1))
print(round(3.4))
print(round(3.5))
print(round(3.456,2))

#3.pow(x,y)--Exponential values

print(pow(2,3))
print(pow(3,3))

#4.divmod(a,b)--returns quotient and remainder values

print(divmod(20,10))
print(divmod(11,3))

#5.int()--converts a number or string into integer

print(int(2))
print(int('2'))
print(int(2.3))

#6.float()

print(float(2))
print(float('2'))
print(float(2.0))

#7.complex()

print(complex(2,4))
print(complex(1,0))
print(complex(0))

#8.bin()--binary(base 2)

print(bin(2))
print(bin(10))
print(bin(20))

#9.oct()--octal(base 8)--012345667


print(oct(2))
print(oct(4))
print(oct(9))
print(oct(10))

#10.hexadecimal(base 16)---(0-9)and(a-f)


print(hex(2))
print(hex(10))
print(hex(8))
print(hex(11))

#11.isinstance()

print(isinstance(1,int))
print(isinstance('hello',str))
print(isinstance(3.0,float))

#12.type()
a=10
print(type(a))

b=[1,2,3]
print(type(b))