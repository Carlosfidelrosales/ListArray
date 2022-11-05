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
# 1 -> Add an element
# 2 -> Insert an element
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
What do you want to do? (1-6)\n
THE LIST OF NUMBERS ARE THE FOLLOWING: 2, 5, 87, 8, 5, 1, 99, 10, 24, 56
1. Add an Element
2. Insert an Element
3. Modify an Element
4. Delete an Element
5. Arrange in Ascending Order
6. Arrange in Descending Order

>>> ''')


    myInventory = [2, 5, 87, 8, 5, 1, 99, 10, 24, 56]

    if list_menu == "1":
        print("\nADD AN ELEMENT MENU")
        print("\nWhat number do you want to add?: ")
        num = float(input())
        myInventory.append(num)
        print("This is the new Array:" , myInventory)

    elif list_menu == "2":
        print("\nINSERT AN ELEMENT MENU\n")
        num_idx = int(input("\nPlease enter the index you want for your element to be injected: "))
        num_flt = float(input("\nPlease enter the number you want to be inserted: "))
        myInventory.insert(num_idx, num_flt)
        print("This is the new Array:" , myInventory)

    elif list_menu == "3":
        print("\nMODIFY AN ELEMENT MENU")
        print("\n Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n")
        print("\n Numbers List = [2, 5, 87, 8, 5, 1, 99, 10, 24, 56]\n")
        num_idx1 = int(input("\nPlease enter the index position you want for your number to be replaced?: "))
        num_flt1 = int(input("Please enter the number you want: "))
        myInventory.pop(num_idx1)
        myInventory.insert(num_idx1, num_flt1)
        print("This is the new Array:" , myInventory)

    elif list_menu == "4":
        print("\nDELETE AN ELEMENT MENU")
        num_rmv = int(input("\nPlease enter the number you want to remove?: "))
        myInventory.remove(num_rmv)
        print("This is the new Array:" , myInventory)

    elif list_menu == "5":
        print("\nSORT AN ELEMENT TO ASCENDING MENU")
        

    
    







        





    
    

list1()

