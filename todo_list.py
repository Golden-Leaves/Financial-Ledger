#3/7/2024
todo_list = ["dog"]
Index = 1
def Options():
   
    print("1.Add tasks")
    print("2.Remove tasks")
    print("3.Quit the program")
    print("4.Show list")
    Choice = int(input("Enter your choice (1,2,3 or 4): "))
    if Choice == 1:
        new_tasks = input("Enter the task(s): ")
        todo_list.append(new_tasks)
        print(f"{new_tasks} succesfully added")
    elif Choice == 2:
        print(todo_list)
        TaskRemoveIndex = int(input("Which task which you like to remove (Enter the index): "))
        RemovedTasks = todo_list.pop(TaskRemoveIndex)
        print(f"{RemovedTasks} removed")
    elif Choice == 3:
        print("Quitting...")
    elif Choice == 4:
        if len(todo_list) == 0:
          print("Your to do list is empty")
        while Index != len(todo_list):
         for task in todo_list:
            print(f"{Index}.{task}")
            Index += 1   
    else:
        print("Please enter the appropriate option")
Options()
 
   
    
