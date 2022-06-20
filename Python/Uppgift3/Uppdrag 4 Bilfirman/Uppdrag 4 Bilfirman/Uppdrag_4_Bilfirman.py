from getkey import getkey, keys

def staff():
    print("Start to write in staff")

    staff = open('staff.txt', 'a')
    employee = input('Enter your name to check in: ')
    staffId = input('enter staff id: ')
    time = input('Enter date: ')

    staff.write(employee + ',' + ' Welcome staff ID: ' + staffId + ',' + time + '\n')
    print(' Welcome ' + employee + ' Your staff ID: ' + staffId + ',' + time + ' data is stored in server ')
    staff.close()
    
def staff_read():
    print('start to read employee checkin')
    menu = 0
    menu = input("Read check list press 1: ")
    if menu == '1':
         staff2 = open('staff.txt', 'r')
         print(staff2.read())
         staff2.close()
    else :
        print('wrong input...')

def ticket():
    print('This section is for car purchase or register car pruchase')
    ticket = open('ticket.txt', 'a')
   
    car_price = input("Enter car prise: ")
    car_model = input('enter car model: ')
    manufacture_date = input('manufacture date: ')
    owner = input('Name of owner: ')

    ticket.write(' $ ' + car_price + ',' + ' Model: ' + car_model + ' Manufacture date: ' + manufacture_date + ' , ' + owner +'\n')
    ticket.close

def ticket_read():
    ticket_read = open('ticket.txt', 'r')
    print(ticket_read.read(), 'checkout')
    ticket.close()
    


def ensurance():
    print('This sention is for car ensurance')

    ensurance = open('ensurance.txt', 'a')

    car_price = input("Enter ensurance cost: ")
    car_model = input('enter car model: ')
    manufacture_date = input('manufacture date: ')
    owner = input('Name of owner: ')

    ensurance.write(' $ ' + car_price + ',' + ' Model: ' + car_model + ' Manufacture date: ' + manufacture_date + ' , ' + owner + '\n')
    ensurance.close
    
    ensurance = open('ensurance.txt', 'r')
    print(ensurance.read(), 'checkout')




menu = 0
car = 0
money = 1000
cars = {'volvo 2005', 'volvo 2010', 'volvo 2015' }

while True:
    array = {'Register buyers', 'Handle cars','Perform service, repairs and warranty matters', 'Manage staff' }
    print(array)
    menu = int(input('Whats today service: staff login 1, register as buyers 2:' ))
    if menu == 1:
        menu2 = 0
        menu2 = int(input('Do you want to check in: 1: for yes or 2: for manager read logg: '))
        if menu2 == 1:
            print('yes')
            staff()
        elif menu2 == 2:
            print('This is for manager to read log')
            staff_read()
    elif menu == 2:
         print('Register your purchase or purchese a car')
         menu3 = 0
         car = int(input('Do you own car?: Yes press 1, No press 0: '))
         menu3 = int(input('Do you want to purchase car or register your car at our service self-checkout?:\n 1 yes register my car, 2 make a purchase : '))
         if menu3 == 1 and car == 1:
            print('you own a car, let us se our register')
            menu4 = 0
            print(' it cost 100 kr as service fee to register your car')
            menu4 = input('register my car: yes or no: ')
            if menu4 == 'yes' and money > 0:
                money -= 100
                ticket()
            elif menu4 == 'no' and money < 100:
                print('Sorry here is your money back')
                money += 100
                print(money)
            else :
                print('sorry your input is wrong or system dont accept money for now')
         elif menu3 == 2 and car == 0:
            print('do you want to purchese a car?') 
            menu5 = input('Yes or No: ')
            if menu5 == 'yes':
                print()
            elif menu5 == 'no':
                print(cars)
                print('here is aviable cars to purchase')
    elif menu == 3:
        print('3')
    elif menu == 4:
        print('4')
    elif menu == 5:
        break