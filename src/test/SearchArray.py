from array import *

arr = array('i',[])

arrlengh = int(input("Enter lenght of an array"))
for i in range(arrlengh):
    val = int(input("Enter array value: "))
    arr.append(val)


print(arr)


searchele = int(input("Enter search element"))

#type 1
k = 0
for e in arr:
        if e == searchele:
            print(k)
            break
        k+=1;
        
#type2
for e in arr:
        if e == searchele:
            print(arr.index(searchele))






