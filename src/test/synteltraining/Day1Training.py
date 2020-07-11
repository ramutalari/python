s1="This is Python";
s2="I like it";
s3="SYNTEL";
print("s1 :",s1);
print("s2 :",s2);
print("s3 :",s3);
print("Length of s1 :",len(s1));
print(s1+" "+s2);
print("s1 in lowercase :"+s1.lower());
print("s1 in uppercase :"+s1.upper());
print("P index :",s1.find("P"));
print("i  index :",s1.find("i"));
print("i  index :",s1.find("i",3));
print("I  index :",s1.find("I"));
print(" 'is'   index :",s1.find("is"));
print(" 'like'   index :",s2.find("like"));
print(" 'LIKE'   index :",s2.find("LIKE"));
print("s1[0]  :",s1[0]);
print("Last Char of s1 :  ",s1[len(s1)-1]);
p=s2[0:7];  # I Like
q=s3[0:];   # SYNTEL
r=s3[:3];   # SYNTEL
print("r",r);
print(p,q);
print("s1==s2 :",(s1==s2));
print("s1==s1 :",(s1==s1));
a=100;
b="100";
c=100;
print("a==b  :",(a==b)); #False
print("a==c :",(a==c));  #True