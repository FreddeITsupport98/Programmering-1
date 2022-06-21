from getkey import getkey, keys
import replit

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
   
def service():
    print('This section is for car purchase or register car pruchase')
    service = open('service.txt', 'a')
   
    car_price = input("Enter car prise: ")
    car_model = input('enter car model: ')
    manufacture_date = input('manufacture date: ')
    owner = input('Name of owner: ')
    service_time = input('Service repair time in weeks: ')

    service.write(' $ ' + car_price + ',' + ' Model: ' + car_model + ' Manufacture date: ' + manufacture_date + ' , ' + owner + 'service time:'+  service_time +'\n')
    service.close

def service_read():
    service = open('ticket.txt', 'r')
    print(service.read(), 'checkout')
    service.close()

def agreement():
    print('Welcome to user agreement here you sign the contract for leasing or purchase is made')
    
    menu = input('Do you want sign contract?: Yes or No: ')
    if menu == 'yes':
        contract = open('agreement.txt', 'a')
        name_owner = input('Write your name: ')
        lease = input('Lease licanse in years: ')
        car_model = input('Car model: ')
        warranty = input('Warranty in years: ')
        cost = input('Cost for warranty per year: ')
        signed_by_seller = input('Seller sign contract: ')
        print('Saving contract to file... press enter')
    
        contract.write('\n')
        contract.write('***********\n')
        contract.write('Dealer ship signing contrak \n')
        contract.write('Her by i purchase this car by accepting warranty and lease time \n')
        contract.write('Here by i accept warranty-policy and leasing license \n')
        contract.write('Name and surname\n')
        contract.write(name_owner +'\n')
        contract.write('***********\n')
        contract.write('\n')
        contract.write('lease\n')
        contract.write(lease+'\n')
        contract.write('***********\n')
        contract.write('\n')
        contract.write('Carmodel\n')
        contract.write(car_model+'\n')
        contract.write('***********\n')
        contract.write('\n')
        contract.write('Warranty\n')
        contract.write(warranty+'\n')
        contract.write('***********\n')
        contract.write('Cost\n')
        contract.write(cost+'\n')
        contract.write('***********\n')
        contract.write('\n')
        contract.write('Signed by seller\n')
        contract.write(signed_by_seller +'\n')
        contract.write('***********\n')
        contract.close()

    elif menu == 'no':
        print('You must accept to buy or lease our cars if you are not registered!')
        print('loading contract file...')
        contract = open('agreement.txt', 'r')
        print(contract.read())
        contract.close()


def agreement_read():
    print('Read contract to console output')

    menu = input('Do want to load file?: Yes or No: ')
    if menu == 'yes':
        print('loading contract file...')
        contract = open('agreement.txt', 'r')
        print(contract.read())
        contract.close()

    elif menu == 'no':
        print('Exiting... press enter.')




menu = 0
car = 0
money = 1000
cars = {'volvo 2005', 'volvo 2010', 'volvo 2015' }

while True:
    array = {'Register buyers*', 'Handle cars*','Perform service, repairs and warranty matters', 'Manage staff' }
    print(array)
    menu = int(input('Whats today service: staff login 1, register as buyers 2, warranty check 3:' ))
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
         elif menu3 == 2:
            print('do you want to purchese a car?') 
            menu5 = input('Yes or No: ')
            if menu5 == 'yes':
                print('You need to purchase car ticket format will hand out and warranty license need to be filled')
                ticket()
                print('after you finnished sign ticket for purches next is sign warranty license')
                agreement()
            elif menu5 == 'no':
                print(cars)
                print('here is aviable cars to purchase')
    elif menu == 3:
        print('Welcome to warranty checkout, here you can check if you are listed in warranty')
        menu7 = input("Do you want us to check your warranty: Yes or no: ")
        if menu7 == 'yes':
            print('Let us take a look at warranty database in your name')
            agreement_read()
            menu8 = input('Your name show in database? Yes or no: ')
            if menu8 == 'yes':
                print('Do you seek maintenance')
                menu9 = input('Yes or No i want to read my service status: ')
                if menu9 == 'yes':
                    print('let us take a look at service and warranty')
                    service_read()
                    print('Next warranty')
                    agreement_read() 
                    menu11 = input('Do you want to register your warranty and service?: yes or no: ')
                    if menu11 == 'yes':
                        print('Alright service registering')
                        service()
                        print('Then warranty')
                        agreement()
                        print('We let you know when car is finished from service')
                    elif menu11 == 'no':
                        print('Bye')
                elif menu9 == 'no':
                    print('Alright let see service status')
                    service_read()
                    menu10 = input('Do you want to register at service?: yes or no: ')
                    if menu == 'yes':
                        print()
                        service()

                    elif menu10 == 'no':
                        print('Goodbye')
            elif menu8 == 'no':
                print('Do you want to register your warranty?')
                menu12 = input('Yes or no: ')
                if menu12 == 'yes':
                    print('Let us see')
                    agreement()
                elif menu12 == 'no':
                    print('Bye')
        elif menu7 == 'no':
            print('Get back any time!')
    elif menu == 4:
        print('4')
    elif menu == 5:
        break
