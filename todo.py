import time
tasks = []
def main():
    print("To-Do List ")
    time.sleep(1)
    print("\n \"Press 1\" to add a new Task\n \"Press 2\" to Search for all Tasks\n \"Press 3\" to mark a Task as complete\n \"Press 4\" to quit")
    while True:
        option(int(input("\nEnter option: ")))

def option(n):
    if n == 1:
        add = input("\nTask: ")
        tasks.append(add)
        print(f"\n{add} added successfully! ")
    elif n == 2:
        print(tasks)
    elif n == 3:
        print("\nWhich Task would you like to remove? ")
        remove = input("Remove: ")
        tasks.remove(remove)
        print(f"{remove} removed successfully! ")
    elif n == 4:
        print("\nGoodbye! ")
        quit()
    else:
        print("\nIncorrect option! ")
        

main()
    
        
     
    
