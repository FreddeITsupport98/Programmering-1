
# Python does not support swedish utf-code so i must write in english, but it sucks so keep it up!

print("helo welcome to car dealership, here you can buy cars!")

car_make = input("whats is your car brand?: ")
model = input("What year modell is your car?: ")
year_model = input("what year model does your car have? ")
drive_distance = input("How far do you drive in Km ?: ")

print(" Well you have a " + car_make + " of " + model + " and already from " + year_model + " but it has not gone more than " + (drive_distance) + " it sounds intresting! " )

# buy car code sett

money = 1500 # defined money amount to buy
sale = 0 #Sale means owned car 
menu = 0 # menu
car1 = 250 # car value
car_Name1 = "volvo v100, model 2005" #car name
car2 = 300
car_Name2 = "volvo v200, model 2010"
car3 = 400
car_Name3 = "volvo v300, model 2022"

owned_car1 = {""} #created empty list to concatenete



while money > car1 and money > car2 and money > car3 and menu < 4: # if money are less car value break loop, if menu = 4 breaks loop to.
    menu = int(input("Choose menu 1: to buy, 2 sale, 3 exit: ")) #converted int number it will trhow a error if value is string
    if menu == 1: #If statment
       menu2 = 0 #defult as menu equals to 0
       menu2 = int(input(" Do you want to buy? Volvo v100 (1), volvo v200, (3) volvo v300, (4) exit: " )) # menu devided into number to choose as menu
       if menu2 == 1 :
           money -= car1 # buy car lose money
           print("money: ",money) #print value from money variable
           print(car_Name1) #print varible name
           sale += 1 #add 1 to sale
           print("Owned cars ", sale) #let user known how much they own cars
           owned_car1.add("Volvo v100, model 2005") # add to array list owned_car1
           
       elif menu2 == 2: # same statment!
           money -= car2
           print("money: ",money)
           print(car_Name2)
           sale += 1
           print("Owned cars ", sale)
           owned_car1.add("Volvo v200, model 2010")

       elif menu2 == 3: # same statment!
            money -= car3
            print("money: ",money)
            print(car_Name3)
            sale += 1
            print("Owned cars ", sale)
            owned_car1.add("Volvo v300, model 2022")

       elif menu2 == 4: # same statment!
            print("money: ",money)
            print("Owned cars ", sale)
            menu == 0
         
       else :
            print("wrong keyboard input")
    elif menu == 2 :
       menu3 = 0
       menu3 = int(input(" Do you want to sell? Volvo v100 (1), volvo v200, (3) volvo v300, (4) exit: " ))
       print("Owned cars ",owned_car1)

       if menu3 == 1 and sale > 0: # If sale is zero you promted back with massage "no purchased car"
           money += car1 # adds money when you sell car
           print("money: ",money)
           print(car_Name1)
           sale -= 1 # sale varible reduct to -1
           print("Owned cars ", sale) #print varible
           owned_car1.remove("Volvo v100, model 2005") # remove from list as it added by .add list.
           
       elif menu3 == 2 and sale > 0: # same statment!
           money += car2
           print("money: ",money)
           print(car_Name2)
           sale -= 1
           print("Owned cars ", sale)
           owned_car1.remove("Volvo v200, model 2010")

       elif menu3 == 3 and sale > 0: # same statment!
            money += car3
            print("money: ",money)
            print(car_Name3)
            sale -= 1
            print("Owned cars ", sale)
            owned_car1.remove("Volvo v300, model 2022")

       elif menu3 == 4: # same statment!
            print("money: ",money)
            print("Owned cars ", sale)
            menu == 0
         
       else :
            print("wrong keyboard input or you don't own a car") #else statment if sale = 0
            print("Owned cars ", sale)
            print("money: ",money)

    elif menu == 3:
        menu = 4

    else :
        print("wrong keyboard input")
print("You have no more money or you exited dealership")
print("Owned cars after purchase ",owned_car1)




f = open('text.txt', 'r')
print(f.name)
f.close()