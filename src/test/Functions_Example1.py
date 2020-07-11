#ex1:with single return statement
def add(x,y):
    c = x+y
    return c

result =add(4,6)
print(result)

#By using multiple return statements
def add_sub_mul(a,b):
    p = a+b
    q = a-b
    r = a*b
    return p,q,r

result1,result2,result3 = add_sub_mul(14,4)
print(result1,result2,result3)


