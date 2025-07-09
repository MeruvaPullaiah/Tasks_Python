#len()
str='Hello'
print(len(str))      #5

#Upper()
name='naniyadav'
name1=name.upper()
print(name1)         #NANIYADAV

#lower()
name='NANI'
name1=name.lower()
print(name1)         #nani

#title()
str='hello world'
str=str.title()
print(str)         #Hello World

#capitalize
word='learning python'
word1=word.capitalize()  
print(word1)              #Learning python
  
#swapcase()
word='pYthOn'
print(word.swapcase())    #PyTHoN
 
#strip

sen='   i am learning python    '
sen1=sen.strip()
print(sen1)              #i am learning python
print(len(sen))          #27
print(len(sen1))         #20


#lstrip()
sen='   i am learning python'    
sen1=sen.strip()
print(sen1)               #i am learning python
print(len(sen))           #23 
print(len(sen1))          #20

#rstrip()
sen=' i am learning python    '
sen1=sen.strip()
print(sen1)               #i am learning python 
print(len(sen))           #25
print(len(sen1))          #20

#find()
word='sentence'
print(word.find('s'))    #0
print(word.find('e'))    #1 (to return first comes position)

#replace(old,new)
word='python language'
w1=word.replace('language','programming')
print(w1)                #python programming

#count()
word='sentence'
print(word.count('e'))   #3

#remove prefix
a='python language'
print(a.removeprefix('python'))    #  language

#remove suffix
print(a.removesuffix('language'))  #python 


#isalnum()
word='nani123'
print(word.isalnum())   #True
 
#isdigit()
a='123'
print(a.isdigit())      #True

#isalpha()
name='nani'
print(name.isalpha())   #True


#split()
str='python is highlevel programming lang'
print(str.split())       #['python', 'is', 'highlevel', 'programming', 'lang']



#join(iterable)----join() method is used to concatenate elements of an iterable(list,tuple,set,dictionary)
s='naniyadav'
s1='#'.join(s)
print(s1)         #n#a#n#i#y#a#d#a#v

#joning with list
fruits=['apple','banana','cherry']
result=','.join(fruits)
print(result)             #apple,banana,cherry

#joining with letters
letters=['p','y','t','h','o','n']
result=''.join(letters)
print(result)             #python


#joining with new line(\n)

letter='koushik'
result='\n'.join(letter)
print(result)

'''
output:
k
o
u
s
h
i
k
'''

#positive indexing
s = "Python"
print(s[0])        #p
print(s[3])        #h

#negative indexing
s = "Python"
print(s[-1])       #n
print(s[-2])       #o


#slicing
word='arundhathi'
print(word[0:4])    #arun

word='Naniyadav'
print(word[-1:-4:-1])   #vad

#write a fuunction to print palindrome or not using slicing 
def palindrome(word):
    rev=word[::-1]
    if word==rev:
        return 'palindrome'
    else:
        return 'not a palindrome'
print(palindrome('wow'))            #palindrome


