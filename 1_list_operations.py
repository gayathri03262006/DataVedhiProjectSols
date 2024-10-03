#Aim - Write a program to create, append and remove list in python/c/java

import sys

def create(lst):
    n = int(input("Enter number of elements of list: "))
    print("Enter elements: ")
    for _ in range(n):
        lst.append(input())

def append(lst):
    lst.append(input("Enter element: "))

def remove(lst):
    try:
        lst.remove(input("Enter element: "))
    except ValueError:
        print("Element not found in list")

def display(lst):
    print("Elements of List: ")
    for ele in lst:
        print(ele)    

def  main():
    lst = []

    while True:
        print("TASKS")
        print("1. Create a list")
        print("2. Append")
        print("3. Remove")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create(lst)
        elif choice == 2:
            append(lst)
        elif choice == 3:
            remove(lst)
        elif choice == 4:
            sys.exit("Exiting program")
        else:
            print("Invalid Choice")

        display(lst)
    
if __name__ == "__main__":
    main()
            
        
        
