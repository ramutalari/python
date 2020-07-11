try:
    n=int(input("Enter number :"));
    print("You have entered :",n);
    print("Open the files....");
    a=100/n;
    print("a=",a)
    arr=[111,22,33,44];
    print("arr[5]:",arr[5]);
except ZeroDivisionError as e:
      print("Number should be greater than zero :",e);
except IndexError as e:
      print("Wrong Array Index  :",e);
finally:
    print("Close the files....");