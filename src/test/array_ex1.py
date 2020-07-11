# import array as arr
# arr.array

from array import *

values = array('i',[10,15,20,25,30])

print(values.buffer_info())
print("Array values are:")
for i in values:
    print(i)

values.reverse();
print("Array values in reverse order:",values)


