import random

'''

snake = 1
water = -1
gun = 0

'''

computer = random.choice([-1,0,1])
youstr = input("enter your choice: ")
youdict = {"snake":1,"water":-1,"gun":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}

you = youdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")


if(computer == you):
    print("its a draw!")

else:
    if(computer ==-1 and you ==1):
        print("you win!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")


    else:
        print("something went wrong!")
