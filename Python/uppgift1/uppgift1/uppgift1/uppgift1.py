
# Python does not support swedish utf-code so i must write in english, but it sucks so keep it up!

print("helo welcome to car dealership, here you can buy caras!")

car_make = input("whats is your car brand?: ")
model = input("What year modell is your car?: ")
year_model = input("what year model does your car have? ")
drive_distance = input("How far do you drive in Km ?: ")

print(" Well you have a " + car_make + " of " + model + " and already from " + year_model + " but it has not gone more than " + (drive_distance) + " it sounds intresting! " )

# buy car code sett

money = 1000
sale = 0
menu = 0
car1 = 250
car_Name1 = "volvo v100"
car2 = 300
car_Name2 = "volvo v200"
car3 = 300
car_Name3 = "volvo v300"

owned_car1 = {"Volvo v100", "Volvo V200", "Volvo V 300"}
owned_car2 = {"Volvo V200", "Volvo V 300"}
owned_car3 = {"Volvo V 300"}


while money > car1 and money > car2 and money > car3 and menu != True :
    menu = int(input("Choose menu 1: to buy, 2 sale, 3 exit: "))
    if menu == 1:
       menu2 = 0
       menu2 = int(input(" Do you want to buy? Volvo v100 (1), volvo v200, (3) volvo v300, (4) exit: " ))
       if menu2 == 1 :
           money -= car1
           print(money)
           print(car_Name1)
           sale += 1
           
       elif menu2 == 2: 
           money -= car2
           print(money)
           print(car_Name2)
           sale += 1

       elif menu2 == 3:
            money -= car3
            print(money)
            print(car_Name3)

       elif menu2 == 4:
            print(money)
            print(Sale)
            menu == 0
         
       else :
            print("wrong keyboard input")
    elif menu == 2 and sale < 1:
       menu3 = 0
       menu2 = int(input(" Do you want to sell? Volvo v100 (1), volvo v200, (3) volvo v300, (4) exit: " ))
       if menu3 == 1 and sale < 1 :
           money += car1
           print(money)
           print(car_Name1)
           sale -= 1
           
       elif menu3 == 2 and sale < 1: 
           money += car2
           print(money)
           print(car_Name2)

       elif menu3 == 3 and sale < 1:
            money += car3
            print(money)
            print(car_Name3)
       elif menu3 == 4:
            print(money)
            print(sale)
            menu == 0
         
       else :
            print("wrong keyboard input or you dont own a car")

    elif menu == 3:
        menu = True

    else :
        print("wrong keyboard input")
print("You have no more money")

if sale == 1 :
    print("Owned cars ",owned_car3)
elif sale == 2:
    print("Owned cars ",owned_car2)
elif sale == 3:
    print("Owned cars ",owned_car1)



f = open('text.txt', 'r')
print(f.name)
f.close()