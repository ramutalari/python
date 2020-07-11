from numpy import *

arr1 = array([
                [1,2,3],
                [4,5,6]

            ])

print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)
print(arr1.size)

#converting multi-dimention array to single-dimention
arr2 = arr1.flatten()
print(arr2)
#reconverting one dimentional to multi-dimentioanl array
arr3 = arr2.reshape(2,3)
print(arr3)

#without using array keywor creating multi dimentional array
m = matrix('1,2,3;4,5,6;7,8,9')
print('Multi dimentional array of m is - without using array keyword')
print(m)

#how to get diagonal element
print("diagonal matrix of m is:",diagonal(m))

#multiply array

m1 = matrix('1,2,3;4,5,6')
m2 = matrix('3,2,1;6,7,8')
m3 = m1 *  m2;
print(m3)




