a=str(input("enter the string :"))
b=a.replace(" ","")
c=b[::-1]
if c==b:
    print("YES it is a palidrome")
else:
    print("NO it is not a palidrome")