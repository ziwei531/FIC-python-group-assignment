#Inventory System
import datetime
userAccount = "admin"
truePass = "admin"
#login page
def log_in():
    while True:
        global userID
        global password
        print("Welcome to ABC Company's inventory system terminal.")
        print("Clearance: Only those working for the IT department from ABC Company may access this terminal.")
        print("\n")
        print("Please enter the correct ID and Password provided by your supervisor in order to access this terminal.")
        userID = input("Enter your ID: ")
        password = input("Enter your password: ")
        if (password == truePass) and (userID == userAccount):
            print("\n")
            print("Welcome " + userID)
            break
        else:
            print("\n")
            print("Incorrect password or Admin ID.")
            print("\n")
            continue

log_in()

#FUNCTIONS
def main_menu():
        timeNow = datetime.datetime.now()
        print()
        print("*************************************")
        print("MAIN MENU : ")
        print("*************************************")
        print("Enter 0 to 5 for the following options:")
        print("0 -> Exit")
        print("1 -> Show all items")
        print("2 -> Add or remove items from inventory")
        print("3 -> Search items by category")
        print("4 -> Show total number of items")
        print("5 -> View User Account for this terminal")
        print("6 -> Export stock information to a text file")
        print("7 -> Log out of terminal")
        print("*************************************")
        print()
        print("Current time and date: ", timeNow.strftime("%d %B %Y %H:%M"))
        
        alert_system(beds)
        alert_system(chairs)
        alert_system(tables)
        alert_system(sofa)

def alert_system(cat):
    for key, value in cat.items():
        if value <= 2:
            print("[Warning!", key, "is currently very low in stock]")
            
def show_items():
    print()
    print("*************************************")
    print("ALL ITEMS : ")
    print("*************************************")
    for key, value in category.items():
        print("-------------")
        print(key, ":")
        print("-------------")
        for i, (item, number) in enumerate(value.items(), 1):
            print(str(i) + ")", item, " : ", number)
    print()
    print("*************************************")

def add_remov_menu():
  while True:
    print()
    print("*************************************")
    print("ADD OR REMOVE ITEM MENU : ")
    print("*************************************")
    print("1 -> Add or remove from an existing item")
    print("2 -> Add a new item")
    print("3 -> Exit to main menu")
    print()
    opt = int(input("Enter your option: "))
    if opt == 1:
        while True:
            print()
            print("*************************************")
            print("CATEGORY MENU : ")
            print("*************************************")
            print("1 -> Beds")
            print("2 -> Chairs")
            print("3 -> Tables")
            print("4 -> Sofa")
            print("5 -> Exit to ADD ITEM MENU")
            print()
            cat_opt = int(input("Select your category: "))
            if cat_opt == 1:
                item_menu(beds)
            elif cat_opt == 2:
                item_menu(chairs)
            elif cat_opt == 3:
                item_menu(tables)
            elif cat_opt == 4:
                item_menu(sofa)
            elif cat_opt == 5:
                print()
                print("Exiting to ADD ITEM MENU....")
                break
            else:
                print()
                print("Invalid option, please try again")
                continue
    elif opt == 2:
        print()
        print("*************************************")
        print("CATEGORY MENU : ")
        print("*************************************")
        print("1 -> Beds")
        print("2 -> Chairs")
        print("3 -> Tables")
        print("4 -> Sofa")
        print("5 -> Exit to ADD ITEM MENU")
        print()
        cat_opt = int(input("Select your category: "))
        if cat_opt == 1:
            add_item(beds)
        elif cat_opt == 2:
            add_item(chairs)
        elif cat_opt == 3:
            add_item(tables)
        elif cat_opt == 4:
            add_item(sofa)
        elif cat_opt == 5:
            print()
            print("Exiting to ADD ITEM MENU....")
            break
        else:
            print()
            print("Invalid option, please try again")
            continue   
    elif opt == 3:
        print()
        print("Exiting to main menu.....")
        break
    else:
        print()
        print("Invalid option, please try again")
        continue

def search_menu():
  while True:
    print()
    print("*************************************")
    print("SEARCH ITEM MENU : ")
    print("*************************************")
    print("1 -> Search item by name")
    print("2 -> Search item by ID")
    print("3 -> Exit to main menu")
    print()
    try:
      opt = int(input("Enter your option: "))
    except ValueError:
      print('You have not entered a valid number. Please try again')
      continue
    if opt == 1:
        print()
        print("*************************************")
        print("SEARCH ITEM  BY NAME MENU : ")
        print("*************************************")
        print("1. Beds")
        print("2. Chairs")
        print("3. Tables")
        print("4. Sofa")
        print()
        opt_name = input("Search item name: ")
        if opt_name == "beds":
            print("Item name: ",beds)
        elif opt_name == "chairs":     
            print("Item name: ",chairs)
        elif opt_name == "tables":
            print("Item name: ",tables)
        elif opt_name == "sofa":
            print("Item name: ",sofa)
        else:
            print()
            print("Invalid option, please try again")
            continue
    elif opt == 2:
        print()
        print("*************************************")
        print("SEARCH ITEM BY ID MENU : ")
        print("*************************************")
        print("Beds -> A001")      
        print("Chairs -> B001")   
        print("Tables -> C001")    
        print("Sofa -> D001")      
        print("5 -> Exit to Main Menu")
        print()
        itemid = input("Search item id: ")
        if itemid == "A001":
            print("Item: ",beds)
        elif itemid == "B001":     
            print("Item: ",chairs)
        elif itemid == "C001":
            print("Item: ",tables)
        elif itemid == "D001":
            print("Item: ",sofa)
        elif itemid == "5":
            print()
            print("Exiting to SEARCH MENU....")
            break
        else:
            print()
            print("Invalid option, please try again")
            continue
    elif opt == 3:
        print()
        print("Exiting to main menu.....")
        break
    else:
        print()
        print("Invalid option, please try again")
        continue 
        
def add_item(dictionary):
    x = "n"
    while x != "y":
        print()
        print("*************************************")
        print("ADD ITEM MENU : ")
        print("*************************************")
        for i, (key, value) in enumerate(dictionary.items(), 1):
            print(str(i) + ")", key, " : ", value)
        print()
        new_item = input("Please type name of new item: ")
        new_item_num = int(input("Please enter number of new items to add: "))
        dictionary[new_item] = new_item_num
        print()
        for i, (key, value) in enumerate(dictionary.items(), 1):
            print(str(i) + ")", key, " : ", value)
        print()
        x = input("Do you wish to exit to CATEGORY MENU? (y/n) : ")

def item_menu(dictionary):
    x = "n"
    while x != "y":
        print()
        print("*************************************")
        print("SELECT ITEM MENU : ")
        print("*************************************")
        for i, (key, value) in enumerate(dictionary.items(), 1):
            print(str(i) + ")", key, " : ", value)
        print()
        while True:
            opt = input("Please type the name of the item to add or remove from: ")
            if opt in dictionary:
                break
            else:
                print()
                print("Item not found, please type the correct item.")
                print()
                continue
        add_num = int(input("Type the number of items you want to add(+) or remove(-) e.g., +2, -2: "))
        dictionary[opt] += add_num
        print()
        for i, (key, value) in enumerate(dictionary.items(), 1):
            print(str(i) + ")", key, " : ", value)
        print()
        x = input("Do you wish to exit to CATEGORY MENU? (y/n) : ")

def list_menu(dictionary):
    x = "n"
    while x != "y":
        print()
        print("*************************************")
        print("SEARCH MENU : ")
        print("*************************************")
        for i, (key, value) in enumerate(dictionary.items(), 1):
            print(str(i) + ")", key, " : ", value)
        x = input("Do you wish to exit to CATEGORY MENU? (y) : ")

def user_account():
    global userID
    global userAccount
    while True:
        print("\n")
        print("Current User Account registered in this terminal: ", userID)
        print("\n")
        print("*************************************")
        print("USER ACCOUNT MENU: ")
        print("*************************************")
        print("1 -> Change this terminal's username")
        print("2 -> Change this terminal's password")
        print("3 -> Exit back to Main Menu")
        
        try:
            userInput = int(input('Enter your option: '))
            print("\n")
        except ValueError:
            print("\n")
            print("You've entered an invalid number, please try again.")
            continue
        if userInput == 1:
            newName = input("Enter your new name: ")
            userID = newName
            userAccount = newName
            print("Name changed successfully!")
        elif userInput == 2:
            print("\n")
            print("Warning! Please ensure that you have consulted with the other admins before proceeding to change this terminal's password.")
            newPass = input("Enter your new password: ")
            while True:
                confirmPass = input("Please confirm your new password: ")
                if newPass != confirmPass:
                    print("You've entered the wrong password, please try again!")
                else:
                    global truePass
                    truePass = newPass
                    print("Password changed successfully!")
                    break
        elif userInput == 3:
            print("Exiting to Main Menu...")
            break
        else: 
            print("You've entered an invalid option, please try again.")

def show_all_items():
    sumBeds = sum(beds.values())
    sumChairs = sum(chairs.values())
    sumTables = sum(tables.values())
    sumSofa = sum(sofa.values())
    total = sumBeds + sumChairs + sumTables + sumSofa

    while True:
        print("*************************************")
        print("DISPLAY TOTAL STOCK MENU: ")
        print("*************************************")
        print("1 -> Display the total of Beds")
        print("2 -> Display the total of Chairs")
        print("3 -> Display the total of Tables")
        print("4 -> Display the total of Sofas")
        print("5 -> Display the total of all furnitures")
        print("6 -> Exit back to Main Menu")

        try:
            usInput = int(input('Enter your option: '))
            print("\n")
        except ValueError:
            print("\n")
            print("You've entered an invalid number, please try again.")
            continue
        if usInput == 1:
            print("Here is the total of beds so far in the Inventory System:", sumBeds)
        elif usInput == 2:
            print("Here is the total of chairs so far in the Inventory System:", sumChairs)
        elif usInput == 3:
            print("Here is the total of tables so far in the Inventory System:", sumTables)
        elif usInput == 4:
            print("Here is the total of sofas so far in the Inventory System:", sumSofa)
        elif usInput == 5:
            print("Here are the list of total furnitures so far inside our inventory system: ", total)
        elif usInput == 6:
            print("Exiting...")
            break
        else:
            print("You have entered an invalid option, please try again.")

def print_stock_info():
    saveFile = open('stock_info.txt', 'w')
    saveFile.write('Beds in stock right: ')
    saveFile.write(str(beds))
    saveFile.write(str('\n'))
    saveFile.write('Chairs in stock right now: ')
    saveFile.write(str(chairs))
    saveFile.write(str('\n'))
    saveFile.write('Tables in stock right now: ')
    saveFile.write(str(tables))
    saveFile.write(str('\n'))
    saveFile.write('Sofas in stock right now: ')
    saveFile.write(str(sofa))
    saveFile.write("\n\n")
    saveFile.write("Total of furnitures left inside our inventory system: ")

    sumBeds = sum(beds.values())
    sumChairs = sum(chairs.values())
    sumTables = sum(tables.values())
    sumSofa = sum(sofa.values())

    total = sumBeds + sumChairs + sumTables + sumSofa
    saveFile.write(str(total))

    saveFile.close()
#END OF FUNCTIONS

#INVENTORY
beds = {"Queen sized bed" : 4, "King sized bed" : 2, "Single sized bed" : 8, "Full sized bed" : 5}
chairs = {"Metal chair" : 4, "Wooden chair" : 6, "Leather chair" : 8, "Plastic chair" : 10}
tables = {"Metal table" : 4, "Wooden table" : 6, "Plastic table" : 10, "Glass table" : 3}
sofa = {"Leather sofa" : 4, "Linen sofa" : 7, "Wooden sofa" : 6, "Velvet sofa" : 8}
category = {"Beds" : beds , "Chairs": chairs , "Tables": tables , "Sofa" : sofa }

#MAIN CODE
while True:
    main_menu()
    try:
        opt = int(input("Enter your option: "))
        if opt == 0:
            print()
            print("Exiting...")
            break
        elif opt == 1:
            show_items()
        elif opt == 2:
            add_remov_menu()
        elif opt == 3:
            search_menu()
        elif opt == 4:
            show_all_items()
        elif opt == 5:
            user_account()
        elif opt == 6:
            print_stock_info()
        elif opt == 7:
            log_in()
        else:
            print('\n')
            print("Invalid option, please try again")
            continue
    except ValueError:
        print('\n')
        print("You've entered an invalid number, please try again")