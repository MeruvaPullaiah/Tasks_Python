'''
char=input('enter the char:')
asc_code=ord(char)
if asc_code>=97 and asc_code<=122:
   print('lower case')
elif asc_code>=65 and asc_code<=90:
    print('upper case')
elif asc_code>=48 and asc_code<=57:
    print('number')
else:
   print('not a alphabet and number')

name='chitti'
secret=''
for i in range(len(name)):
    code=ord(name[i])
    new_char=chr(code+1)
    secret+=new_char
print(secret)

char='hello'
secret=''
for i in range(len(char)):
    code=ord(char[i])
    if char[i]=='a' or char[i]=='e' or char[i]=='i' or char[i]=='o' or char[i]=='u':
        secret+=chr(code+1)
    else:
        secret+=char[i]
print(secret)

'''


#(hello-hfllp) write a function to convert vowel char into next char

def vowel(char):
    secret=""
    for i in range(len(char)):
        code=ord(char[i])
        if char[i]=='a' or char[i]=='e' or char[i]=='i' or char[i]=='o' or char[i]=='u':
            secret+=chr(code+1)
        else:
            secret+=char[i]
    return secret
print(vowel('hello'))
print(vowel('nani'))

   
#check whether the char is upper,lower,number using function
def greet():
    char=input('enter the char:')
    asc_code=ord(char)
    if asc_code>=65 and asc_code<=90:
        return 'upper case'
    elif asc_code>=97 and asc_code<=122:
        return 'lower case'
    elif asc_code>=48 and asc_code<=57:
        return 'number'
    else:
        return 'other'
print(greet())
print(greet())


    

    


