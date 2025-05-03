owed = float(input("enter the amount you owe me in dollars:\n"))
apr = float(input("annual percentage rate:\n"))
payment = float(input("monthly payment:\n"))
month = int(input("number of months:\n"))
monthly_rate = apr/100/12

for i in range(month):
    interest_paid = owed * monthly_rate
    owed = owed + interest_paid
    if (owed - payment < 0):
        print(f"the last payment is {owed:.2f}$")
        print(f"you paid of the loan in {i+1} months")
        break

    owed = owed - payment


    print(f"paid {payment:.2f}$ of which {interest_paid:.2f}$ was interest",end=" ")
    print(f"now you owe {owed:.2f}$")



