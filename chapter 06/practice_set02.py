a = int(input("enter marks : "))
b = int(input("enter marks : "))
c = int(input("enter marks : "))

total_percentange = (100* (a + b + c))/300

if(total_percentange>=40 and a >= 33 and b >= 33 and c >= 33):
    print("you passed",total_percentange)
else:
    print("noob",total_percentange)


