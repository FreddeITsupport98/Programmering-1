print("hello and Welcome!")
pinAccess = 0
menu = 0
name = input("Whats your name?")
print("Welcome :" + name)
while pinAccess < 3:
    pin = 1234
    userPin = int(input("Please login with your pin: "))
    if pin != userPin:
       print("Wrong input")
       pinAccess += 1
       print("Numbers of tries: ", pinAccess)
       continue
    elif pin == userPin: 
       print("Welcome customer!")
       pinAccess = 3
while menu < 4:
    print( "Welcome to car-delearchip" )
    menu = int(input("Menu 1: buy, menu 3: sell menu 3:exit: "))
    if menu == 1:
        menu2 = 0
        print("What do you want to buy?")
        menu2 = int(input("Car1 (1), car2 (2), car3 (3), car4 (4): "))
        if menu2 == 1:
            print("car1")
        elif menu2 == 2:
            print("car2")
        elif menu2 == 3:
            print("car3")
        elif menu2 == 4:
            print("car4")

    elif menu == 2:
        print("What do you want to sell?")
        menu3 = 0
        menu3 = int(input("Car1 (1), car2 (2), car3 (3), car4 (4): "))
        if menu3 == 1:
            print("car1")
        elif menu3 == 2:
            print("car2")
        elif menu3 == 3:
            print("car3")
        elif menu3 == 4:
            print("car4")
    elif menu == 3:
        print("Exiting")
        break