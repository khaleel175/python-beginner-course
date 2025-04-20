a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
d = int(input("enter a number: "))

if(a>b and a>c and a>d):
    print("a is the greatest: ", a)
elif(b>a and b>c and b>d):
    print("b is the greatest: ", b)
elif(c>b and c>d and c>a):
    print("c is the greatest: ", c)
elif(d>b and d>c and d>a):
    print("d is the greatest: ", d)