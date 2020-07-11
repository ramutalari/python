#continue example - It continue the execution after skipping matched condition
print("By using continue statement:")
for i in range(1,6):
    if i==3:
        continue
    print(i)

#break example - It breaks the loop and it wont continue futher execution
print("By using break statement:")
for i in range(1,6):
    if i==3:
        break
    print(i)