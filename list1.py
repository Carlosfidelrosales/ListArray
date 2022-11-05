#Write a python program that do the following:

#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array


#Note: 
#- The program has an array variable containing 10 random numbers
#- You may add other options and features
#- Your program should be uploaded to github before 1:30pm
#- Record a demo presenting your program
#- Send the demo directly to my messenger

#Example Output:

#Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
#Menu:
#1 -> Add an element
#2 -> Insert an element
 #3 -> Modify an element
 #4 -> Delete an element
 #5 -> Arrange in ascending order
 #6 -> Arrange in descending order
#What do you want to do? (1-6): 4
#Enter the index you want to delete: 3
#The element has been deleted
#This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]


def list1():
    list_menu = input('''
\033[33;1mWhat do you want to do? (1-6) \033[0m\n
\033[1;31;43m THE LIST OF NUMBERS ARE THE FOLLOWING: 2, 5, 87, 8, 6, 1, 99, 10, 24, 56 \033[0m
\033[36;3m
1. Add an Element
2. Insert an Element
3. Modify an Element
4. Delete an Element
5. Arrange in Ascending Order
6. Arrange in Descending Order \033[0m

\033[1m>>>\033[0m ''')


    myInventory = [2, 5, 87, 8, 6, 1, 99, 10, 24, 56]

    if list_menu == "1": #1 -> Add an element
        print("\n\033[41;1m ADD AN ELEMENT MENU \n\033[0m")
        num_float = float(input("\nWhat number do you want to add?: "))
        myInventory.append(num_float)
        print("\033[1mThis is the new Array:\033[0m" , myInventory)

    elif list_menu == "2": #2 -> Insert an element
        print("\n\033[41;1m INSERT AN ELEMENT MENU \n\033[0m")
        print("\n Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n")
        print("\n Numbers List = [2, 5, 87, 8, 6, 1, 99, 10, 24, 56]\n")
        num_idx = int(input("\n\033[3mPlease enter the index you want for your element to be injected:\033[0m "))
        num_flt = float(input("\n\033[3mPlease enter the number you want to be inserted:\033[0m "))
        myInventory.insert(num_idx, num_flt)
        print("\033[1mThis is the new Array:\033[0m" , myInventory)

    elif list_menu == "3": #3 -> Modify an element
        print("\n\033[41;1m MODIFY AN ELEMENT MENU \n\033[0m")
        print("\n Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n")
        print("\n Numbers List = [2, 5, 87, 8, 6, 1, 99, 10, 24, 56]\n")
        num_idx1 = int(input("\n\033[3mPlease enter the index position you want for your number to be replaced?:\033[0m "))
        num_flt1 = int(input("\033[3mPlease enter the number you want:\033[0m "))
        myInventory.pop(num_idx1)
        myInventory.insert(num_idx1, num_flt1)
        print("\n033[1mThis is the new Array:\033[0m" , myInventory)

    elif list_menu == "4": #4 -> Delete an element
        print("\n\033[41;1m DELETE AN ELEMENT MENU \n\033[0m")
        print("\n Numbers List = [2, 5, 87, 8, 6, 1, 99, 10, 24, 56]\n")
        num_rmv = int(input("\n\033[3mPlease enter the number you want to remove?:\033[0m "))
        myInventory.remove(num_rmv)
        print("\n\033[1mThis is the new Array:\033[0m" , myInventory)

    elif list_menu == "5": #5 -> Arrange in ascending order
        print("\n\033[41;1m SORT AN ELEMENT TO ASCENDING MENU \n\033[0m")
        myInventory.sort() 
        print("\n\033[1mThis is the new Array:\033[0m" , myInventory)

    elif list_menu == "6": #6 -> Arrange in descending order
        print("\n\033[41;1m SORT AN ELEMENT TO ASCENDING MENU \n\033[0m")
        myInventory.sort(reverse=True) 
        print("\n\033[1mThis is the new Array:\033[0m" , myInventory)

    else:
        print("\033[1mYou entered an invalid operator. Please Try Again.\033[0m")

    tryagain()

def tryagain():
    retry_again = input("\n\n\033[33mDo you want to try again? (Please type 'Y' if Yes and 'N' if No): \033[0m")
    if retry_again.upper() == "Y":
        list1()
    elif retry_again.upper() == "N":
        print("\n\033[1mHope to see you again. Thank you for using the program!\n\033[0m")
        print("\033[1m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PROGRAM CLOSED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\033[0m")
    else:
        tryagain

list1()

