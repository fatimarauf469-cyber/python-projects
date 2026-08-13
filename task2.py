total=0

while True:
    expense=input("enter your expense")
    if expense == "done":
        break
    expense=float(expense) 
    total+=expense 
print("total expense is",total)