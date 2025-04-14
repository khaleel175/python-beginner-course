def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("enter your number: "))
b = int(input("enter your number: "))   
c = int(input("enter your number: "))
print(f"greatest number is {greatest(a,b,c)}")