from numpy import *

arr = array([2,5,8,6])
#increment each array value with 1
arr1 = arr + 1
print(arr1)

arr2 = array([3,6,9,12])
arr3 = array([4,8,12,15])
#add two array values
arr4 = arr2 + arr3
print("Adding two arrays:",arr4)

#mathematical functions
arr5 = sqrt(arr)
print("sqrt of array is:",arr5)
arr6 = sin(arr2)
print("sin of an array is:",arr6)
arr7 = log(arr3)
print("log of an array is:",arr7)

minvalue = min(arr)
print("minvalue",minvalue)
maxvalue = max(arr3)
print("max value is:",maxvalue)

print("concatenate of two arrays: ",concatenate([arr2,arr3]))

# Assigning one array to anohter i.e copying an array from one to other

#type 1 - directly assigning an array then it will copy
arr20 = array([10,20,30,40])

arr30 = arr20

print("arr20 array is:",arr20)
print("arr30 array is:",arr30)

print(id(arr20))
print(id(arr30))

#if you change one array value then it is reflecting to both arrays
arr20[0] = 70

print(arr20)
print(arr30)


#Type2: to avoid above issue use .copy

arr40 = arr20.copy()

arr20[1] = 80

print("arr20 array is:",arr20)
print("arr40 array is:",arr40)

print("arr20 address is:",id(arr20))
print("arr40 address is:",id(arr40))
