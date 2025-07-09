rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)

rows=5
for i in range(rows,0,-1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(j)+" "
    print(pattern)

rows=6
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(j)+" "
    print(pattern)


rows=6
for i in range(rows,0,-1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(j)+" "
    print(pattern)

rows=6
for i in range(1,rows+1):
    pattern=""
    for j in range(i,0,-1):
        pattern+=str(j)+" "
    print(pattern)

rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(i)+" "
    print(pattern)

rows=4
num=2
for i in range(rows):
    pattern=""
    for j in range(i+1):
        pattern+=str(num)+" "
        num+=2
    print(pattern)

rows=4
num=1
for i in range(1,rows+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(num)+" "
        num+=2
    print(pattern)


rows=5
for row in range(rows):
    pattern=""
    for col in range(row+1):
        pattern+=str(rows)+" "
    rows-=1
    print(pattern)

rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1 or j==rows:
           pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)

rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or j==1 or i==rows:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)



rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or j==1 or i==rows or i==(rows//2)+1:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)



rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or j==(rows//2)+1 or i==rows:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)


rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==j or i+j==6:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)

    

rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==(rows//2)+1 or j==1 or j==rows:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)


rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or j==(rows//2)+1:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)


rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==j or j==1 or j==rows:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)


rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or i==5 or i+j==6: 
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)

#To print the pattern letter S using nested loops
# * * * * *
# *
# * * * * *
#         *
# * * * * *

rows=5
for i in range(1,rows+1):
    pattern=""
    mid=(rows//2)+1
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==1:
                pattern+="*"+" "
            else:
                pattern+=" "+" "
        else:
            if i==rows or j==rows:
                pattern+="*"+" "
            else:
                pattern+=" "+" "
    print(pattern)

#To print the pattern 2 using nested loops
        
# * * * * *
#         *
# * * * * *
# *
# * * * * *

rows=5
for i in range(1,rows+1):
    pattern=""
    mid=(rows//2)+1
    for j in range(1,rows+1):
        if i<=mid:
            if i==1 or i==mid or j==rows:
                pattern+="*"+" "
            else:
                pattern+=" "+" "
        else:
            if j==1 or i==rows:
                pattern+="*"+" "
            else:
                pattern+=" "+" "
    print(pattern)

#To print the pattern 3 using nested loops

# * * * * *
#         *
# * * * * *
#         *
# * * * * *

rows=5
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or i==(rows//2)+1 or i==rows or j==rows:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)
