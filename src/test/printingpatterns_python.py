
#To print # 4 times for in each row
for i in range(4):
    for j in range(4):
        print("# ",end="")

    print()
#To print # based on row number count
print()

for i in range(4):
    for j in range(i+1):
        print("# ",end="")

    print()
#To print #
print()

for i in range(4):
    for j in range(4-i):
        print("# ",end="")

    print()
