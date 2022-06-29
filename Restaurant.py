def MainMenu():                         #This is the main function
    print("1. Burgers")                 #printing burgers
    print("2. Steaks")                  #printing steaks
    print("3. Quit")                    #printing quit

    while True:                         #while loop for condition of ValueError
        try:
            select = int(input("Enter Choice: "))           #User inputs
            if select == 1:                                 #if/else condition
                Burgers()
                break
            elif select == 2:
                Steaks()
                break
            elif select == 3:
                print(total)
                break
            else:
                print("Invalid choice, Enter 1-3")
                MainMenu()
        except ValueError:                                  #dont show the error instead print "Invalid choice"
            print("Invalid choice. Enter 1-3")


total = 0.00                            #total cost


def Burgers():                          #Defining burgers function
    rate = {                            #using dictionary for storing price
        "Zinger_Burger": 230,
        "Zinger_Cheese_Burger": 260,
        "Thames_Special_Burger": 320,
        "Beef_Burger": 250,
        "Tower_Burger": 320,
        "Fish_Burger": 260,
        "Fish_Cheese_Burger": 290,
        "Fire_Stone_Burger": 170,
        "Crispy_Burger": 170,
        "Chicken_Burger": 180,
        "Tikka_Burger": 170,
        "Shami_Burger": 170

    }
    tax = 0.08                          #adding tax in total cost

    #printing all the values of Burger

    print("Zinger Burger : 230")
    print("Zinger Cheese Burger : 260")
    print("Thames Special Burger : 320")
    print("Beef Burger : 250")
    print("Tower Burger : 320")
    print("Fish Burger : 260")
    print("Fish Cheese Burger : 290")
    print("Fire Stone Burger : 170")
    print("Crispy Burger : 170")
    print("Chicken Burger : 180")
    print("Tikka Burger : 170")
    print("Shami Burger : 170")

    tax = 0.08                          #tax, that we will add in the total cost
    global total                        #this is the global total variable

    selection = int(input("Enter choice: "))        #asking user to give an input for what they want to order

    #if body starts from here
    if selection == 1:                              #if/else condition, if they want to eat that or something else.
        UserInput()
        cost = Quantity() * rate["Zinger_Burger"]   #multiplying the quantity from the total cost of the burger
        Bill = cost + (cost * tax)                  #adding cost to the variable Bill

        total += Bill                               #adding Bill to the variable total

        MainMenu()                                  #sending user to the mainmenu if they want to order anything else
    elif selection == 2:
        UserInput()
        cost = Quantity() * rate["Zinger_Cheese_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 3:
        UserInput()
        cost = Quantity() * rate["Thames_Special_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 4:
        UserInput()
        cost = Quantity() * rate["Beef_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 5:
        UserInput()
        cost = Quantity() * rate["Tower_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 6:
        UserInput()
        cost = Quantity() * rate["Fish_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 7:
        UserInput()
        cost = Quantity() * rate["Fish_Cheese_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 8:
        UserInput()
        cost = Quantity() * rate["Fire_Stone_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 9:
        UserInput()
        cost = Quantity() * rate["Crispy_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 10:
        UserInput()
        cost = Quantity() * rate["Chicken_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 11:
        UserInput()
        cost = Quantity() * rate["Tikka_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    elif selection == 12:
        UserInput()
        cost = Quantity() * rate["Shami_Burger"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()

    else:                                       #if the user inputs invalid number then it prints "invalid choice"
        print("Invalid choice. Enter 1-12")
    #if body ends here


def Steaks():                                   #Defining steaks function
    rate = {                                    #using dictionary for storing price
        "Arizona_Steak": 650,
        "Mushroom_Steak": 650,
        "Pepper_Steak": 650,
        "Polo_Tuscany": 650

    }
    #printing all the values of Steaks
    print("Arizona Steak : 650")
    print("Mushroom Steak : 650")
    print("Pepper Steak : 650")
    print("Polo Tuscany : 650")

    tax = 0.08                                  #tax added in the final bill
    global total                                #this is the global variable of total

    selection = int(input("Enter choice: "))    #asking user to give an input for what they want to order


    #if body starts from here
    if selection == 1:
        UserInput()
        cost = Quantity() * rate["Arizona_Steak"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()
    elif selection == 2:
        UserInput()
        cost = Quantity() * rate["Mushroom_Steak"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()
    elif selection == 3:
        UserInput()
        cost = Quantity() * rate["Pepper_Steak"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()
    elif selection == 4:
        UserInput()
        cost = Quantity() * rate["Polo_Tuscany"]
        Bill = cost + (cost * tax)

        total += Bill

        MainMenu()
    else:
        print("Invalid choice. Enter 1-4")
    #if body ends here


def UserInput():                            #this function prints "Select Quantity"
    print("Select Quantity:")


def Quantity():                             #this function asks for Quantity
    give = int(input())
    return give


import os                                   #importing operating system

file = "Bill"                               #folder of the file, where we saved it
filename = "bill.txt"                       #this is the file that we created for printing bill

final = os.path.join(file, filename)        #we given a variable
with open(final, "w") as f:                 #opening file as txt
    f.write("Your total bill is: ")
    f.write(str(total))                     #this prints the total price

MainMenu()
