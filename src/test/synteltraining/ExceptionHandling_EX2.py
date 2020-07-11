try:
    n=int(input("Enter number :"));
    print("You have entered :",n);
    print("doing calculation....");
    a=100/n;
    print("a=",a)
    arr=[111,22,33,44];
    print("arr[2]:",arr[5]);
except Exception as e:
      print("Something went wrong :",e);
else:
      print("enter valid inputs");
finally:
    print("in Finally block....");