#default value
#Ex:1
def person(name,age=27):
    print(name)
    print(age)

person('pawan')

#Ex:2
def person2(name,age=27):
    print(name)
    print(age)

person2('abc',32)


#Keyword arguments - when we dont know the position of arguments we can use keyword
def person3(name,age):
    print(name)
    print(age)

person3(age=22,name='abc')


# Variable length arguments

def sum(a, *b):
    c = a
    for i in b:
        c = c + i

    print("Sum of a and tuple b values are: ",c)

sum(2, 4, 6, 8, 10, 12)