p1 = ("make a lot of money")
p2 = ("buy now")
p3 = ("subscirbe")
p4 = ("click this")

message = input("enter a comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or(p4 in message)):
    print("banned")
else:
    print("good to go")