user="Nani Yadav"
print(len(user))

print(user[0])
print(user[1])

print(user[-1])
print(user[-2])

username='panchabhatla saranga pani'

username="Panchabhatla saranga pani"
print(username)

word='venakta sai kumar yadav'
for i in range(0,len(word)):
    print(word[i])

#we have to count alphabetical not a space

name='venakta sai kumar yadav'
char_count=0
for i in range(len(__name__)):
    if name[i]!=" ":
        char_count+=1
print(char_count)

word="nandan"
last=len(word)-1
for i in range(last,-1,-1):
    print(word[i])

#count vowels

name='jagadeesh'
char_count=0
for i in range(len(name)):
    c=name[i]
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        char_count+=1
print(char_count)

#To print char and index
'''
name='NaniYadav'
for i in range(len(name)):
    print(name[i],'is in',i,'index')
'''

#print the position of the vowels

name='Nani yadav'
for i in range(len(name)):
    v=name[i]
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        print(name[i],'is in',i,'index')


#count the no.of consonents'
name='VinayKumarReddy'
consonent_count=0
for i in range(len(name)):
    c=name[i]
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        continue
    else:
        consonent_count+=1
print(consonent_count)


name='VinayKumarReddy'
consonent_count=0
for i in range(len(name)):
    c=name[i]
    if c!='a' and c!='e' and c!='i' and c!='o' and c!='u':
        consonent_count+=1
print(consonent_count)


#1.Create a string with your name and print it

name='Nani Yadav'
for i in range(len(name)):
    print(name[i])

#2.Get the first character from the string

name='Nani'
print(name[0])

#3.Get the last character from the string

name='Nani yadav'
print(name[-1])

#4.Concatenate two strings.

n1='Nani'
n2='Yadav'
print(n1+n2)   #concatenate the strings using '+' operator

#5.Repeat a string 3 times.

word='python ' 
print(word*3) #Repeat the string using '*' operator


#6.Slice the first 5 characters.

sentence='Python Programming Language'
print(sentence[0:5])

#7.Reverse a string using slicing.
str='python'
print(str[::-1])
rev=str[::-1]
print(rev)

#8.Check if a substring exists in a string

text1='learning python'
text2='ing'
if text2 in text1:
    print('sub_string')
else:
    print('Not Sub_string')

#9.Find the length of a string.

word='hello world'
print(len(word))

#10.Convert string to uppercase

name='naniyadav'
name1=name.upper()
print(name1)

#11.Convert string to lowercase

name='NANI'
name1=name.lower()
print(name1)

#12.Capitalize the first letter

word='learning python'
word1=word.capitalize()  
print(word1)             #returns first letter to upper case and remaining characters is same

#13.Convert a string to title case.

senetnce='i am learing full stack python '
print(senetnce.title())


#14.Remove leading spaces using lstrip()

word='    python    '
word1=word.lstrip()
print(word1.lstrip())
print(len(word))
print(len(word1))


#14.Remove leading spaces using rstrip()

word='  python programming   '
word1=word.rstrip()
print(word1)
print(len(word))
print(len(word1))

#using strip

sen='   i am learning python    '
sen1=sen.strip()
print(sen1)

print(len(sen))
print(len(sen1))

#find()

word='sentence'
print(word.find('s'))     
print(word.find('e'))    # to return first comes position

#replace(old,new)

word='python language'
w1=word.replace('language','programming')
print(w1)

#remove prefix
a='python language'
print(a.removeprefix('python'))

print(a.removesuffix('language'))

#split()---split the string into a list

str='python is highlevel programming lang'
print(str.split())

#isalnum()---returns all the letters and numbers
word='nani123'
print(word.isalnum())

#isdigit()--returns the numbers
a='123'
print(a.isdigit())

#isalpha()----returns the letters
name='nani'
print(name.isalpha())

#swapcase()---returns upper to lower and lower to upper

word='pYthOn'
print(word.swapcase())

#join(iterable)----join() method is used to concatenate elements of an iterable(list,tuple,set,dictionary)

s='naniyadav'
s1='#'.join(s)
print(s1)

#joning with list
fruits=['apple','banana','cherry']
result=','.join(fruits)
print(result)

#joining with letters
letters=['p','y','t','h','o','n']
result=''.join(letters)
print(result)

#joining with new line(\n)
lines=['line1','line2','line3']
result='\n'.join(lines)
print(result)

letter='koushik'
result='\n'.join(letter)
print(result)

#zfill()--zerofill

word='python'
word1=word.zfill(15)
print(word1)


#wrie a function to return no.of plaindromes in the string

def Number_of_palindromes(sentence):
    sentence=sentence.split(" ")
    count=0
    for i in range(len(sentence)):
        if sentence[i][::-1]==sentence[i]:
            count+=1
    return count
print(Number_of_palindromes('my family is consists of amma nanna akka anna'))

