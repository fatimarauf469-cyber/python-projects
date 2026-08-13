tasks=[]

while True:
    print("....Task Manager....")
    print("1. add task")
    print("2. view task")
    print("3.Exit")

    choice=int(input("enter your choice"))

    if choice == 1:
     task=input("enter new task")
     tasks.append(task)
     print("add task successfully")

    elif choice==2:
     print("your tasks")

     if len(tasks)==0:
        print("no tasks found")
     else:
        for task in tasks:
          print(task)

    elif choice==3:
     print("Exit")
     break

    else:
     print("invalid choice")


    



