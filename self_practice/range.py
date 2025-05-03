total = 0
expenses = []
num_expenses = int(input("enter number of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("enter your expenses:")))

total = sum(expenses)
print(f"total expenses:${total}")