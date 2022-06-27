
def staff(): # staff sign
    print("Start to write to logg staff time")

    staff = open('staff.txt', 'a') # opens staff.txt as appending
    employee = input('Enter your name to check in: ') # input
    staffId = input('enter staff id: ')
    time = input('Enter date: ')

    staff.write(employee + ',' + ' Welcome staff ID: ' + staffId + ',' + time + '\n') # writes file following values
    print(' Welcome ' + employee + ' Your staff ID: ' + staffId + ',' + time + ' data is stored in server ') #printing
    staff.close() # closses file


    
def staff_read(): #Staff.txt read file
    print('start to read employee checkin')
    menu = 0
    menu = input("Read check list press 1: ")
    if menu == '1':
         staff2 = open('staff.txt', 'r')
         print(staff2.read())
         staff2.close()
    else :
        print('wrong input...')

def ticket(): # ticken are shown proof for purchase
    print('This section is for car purchase or register car pruchase')
    ticket = open('ticket.txt', 'a')
   
    car_price = input("Enter car prise: ")
    car_model = input('enter car model: ')
    manufacture_date = input('manufacture date: ')
    owner = input('Name of owner: ')

    ticket.write(' $ ' + car_price + ',' + ' Model: ' + car_model + ' Manufacture date: ' + manufacture_date + ' , ' + owner +'\n')
    ticket.close

def ticket_read(): # read file
    ticket_read = open('ticket.txt', 'r')
    print(ticket_read.read(), 'checkout')
    ticket.close()
   
def service(): # service is to serve car in repair shop
    print('This section is for car purchase or register car pruchase')
    service = open('service.txt', 'a')
   
    car_price = input("Enter car prise: ")
    car_model = input('enter car model: ')
    manufacture_date = input('manufacture date: ')
    owner = input('Name of owner: ')
    service_time = input('Service repair time in weeks: ') # amount time need to repair

    service.write(' $ ' + car_price + ',' + ' Model: ' + car_model + ' Manufacture date: ' + manufacture_date + ' , ' + owner + 'service time:'+  service_time +'\n')
    service.close()

def service_read(): #read service.txt file
    service = open('service.txt', 'r')
    print(service.read(), 'checkout')
    service.close()

def agreement(): # this is aggremment as warranty
    print('Welcome to user agreement here you sign the contract for leasing or purchase is made')
    
    menu = input('Do you want sign contract?: (Yes) register new warranty or (No) i already have one: ')
    if menu == 'yes':
        contract = open('agreement.txt', 'a')
        name_owner = input('Write your name: ')
        lease = input('Lease licanse in years: ')
        car_model = input('Car model: ')
        warranty = input('Warranty in years: ')
        cost = input('Cost for warranty per year: ')
        signed_by_seller = input('Seller sign contract: ')
        print('Saving contract to file... press enter')
    
        '''
        This is form followed by writing in file ant concatenating values into name.write()
        '''

        contract.write('\n')
        contract.write('***********\n')
        contract.write('Dealer ship signing contrak \n')
        contract.write('Her by i purchase this car by accepting warranty and lease time \n')
        contract.write('Here by i accept warranty-policy and leasing license \n')
        contract.write('\n')
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


def agreement_read(): # agremment read file
    print('Read contract to console output')

    menu = input('Do want to load file?: Yes or No: ')
    if menu == 'yes':
        print('loading contract file...')
        contract = open('agreement.txt', 'r')
        print(contract.read())
        contract.close()

    elif menu == 'no':
        print('Exiting... press enter.')

def managment(): #this is for admin to manage staff login rutins
    print('Welcome to managment console...')
    
    file = open('agreement.txt', 'a') # add security to write in password as to emulate login screen
    pinAccess = 0
    name = input('Enter your name: ')
    print(' Welcome ' + name)
    while pinAccess < 3:
        pin = 1234
        userPin = int(input('Please ogin with your pin: '))
        if pin != userPin:
            print("Wrong input")
            pinAccess += 1
            print("Numbers of tries: ", pinAccess)
            continue
        elif pin == userPin:
            print('Welcome to the Administration console: ' + name)
            pinAccess = 3
    


    while True: 
        '''
        This while loop wrapps around menu: 1 and 2 and 3 and 4
        '''
        menu = int(input('Welcome to the console:\n ' + name + '\nMenu: staff logg book (1) \n' + 'Apply violation to staff (2)\n' + 'Apply warning to staff (3) \n' + 'Exit console (4)\n: ' + 'Input: '))
        if menu == 1: # loads staff.txt
            print('Load staff logg book')
            menu1 = input('Load file: Yes or No: ')
            if menu1 == 'yes':
                print('Loading file...')
                staff = open('staff.txt','r')
                print(staff.read())
                staff.close()
                menu3 = input('Do you want to append staff list?: Yes or No: ') # if not shown allows user to append text file
                if menu3 == 'yes':
                    print('Appending file...')
                    staff = open('staff.txt', 'a')
                    employee = input('Enter your name to check in: ')
                    staffId = input('enter staff id: ')
                    time = input('Enter date: ')

                    staff.write(employee + ',' + ' Welcome staff ID: ' + staffId + ',' + time + '\n')
                    print(' Welcome ' + employee + ' Your staff ID: ' + staffId + ',' + time + ' data is stored in server ')
                    print('Done file is saved')
                    staff.close()
                elif menu3 == 'no':
                    print('Exiting...')
                    
            elif menu1 == 'no':
                print('exiting')
        elif menu == 2: # this is writing violation for staff if reason happens
            print('Welcome to staff managenent: Violation')
            menu4 = input('Do you want to load or append violation?: load or append: ')
            if menu4 == 'load':
                print('Loading previus violations')
                violation = open('violation.txt', 'r')
                print(violation.read())
                violation.close()
            elif menu4 == 'append':
                violation = open('violation.txt', 'a')
                name_violation = input('Enter person name and surname: ')
                datum = input('Enter a date when violation occur')
                reason = input('Reason for violation: ')
                length = input('Length of punishment: ')
                cost = input('Amount of damaged need to cost: ')
                boss = input('Boss signature: ')

                violation.write('\n')
                violation.write('***********\n')
                violation.write('This file is for staff violation \n')
                violation.write('here by i accept my punishement for violating rules of company \n')
                violation.write('There for i accept punishiement prosucuted by company policy rules \n')
                violation.write('\n')
                violation.write('Name and surname\n')
                violation.write(name_violation +'\n')
                violation.write('***********\n')
                violation.write('\n')
                violation.write('datum\n')
                violation.write(datum +'\n')
                violation.write('***********\n')
                violation.write('\n')
                violation.write('reason\n')
                violation.write(reason +'\n')
                violation.write('***********\n')
                violation.write('\n')
                violation.write('Lenght follow by punishment\n')
                violation.write(length+'\n')
                violation.write('***********\n')
                violation.write('Cost\n')
                violation.write(cost+'\n')
                violation.write('***********\n')
                violation.write('\n')
                violation.write('Signed by manager\n')
                violation.write(boss +'\n')
                violation.write('***********\n')
                violation.close()
        elif menu == 3: # This is to give warning to staff if it occurs.
            print('Welcome to staff managenent: Warning')
            menu4 = input('Do you want to load or append Warning?: load or append: ')
            if menu4 == 'load':
                print('Loading previus warning')
                warning = open('warning.txt', 'r')
                print(warning.read())
            elif menu4 == 'append':
                warning = open('warning.txt', 'a')
                name_warning = input('Enter person name and surname: ')
                datum = input('Enter a date when warning occur')
                reason = input('Reason for warning: ')
                length = input('Length of warning remains: ')
                cost = input('cost: ')
                boss = input('Boss signature: ')

                warning.write('\n')
                warning.write('***********\n')
                warning.write('This file is for staff warning \n')
                warning.write('here by i accept my warning for violating rules of company \n')
                warning.write('There for if i repeat i must accept punishment prosucuted by company policy rules \n')
                warning.write('\n')
                warning.write('Name and surname\n')
                warning.write(name_warning +'\n')
                warning.write('***********\n')
                warning.write('\n')
                warning.write('datum\n')
                warning.write(datum +'\n')
                warning.write('***********\n')
                warning.write('\n')
                warning.write('reason\n')
                warning.write(reason +'\n')
                warning.write('***********\n')
                warning.write('\n')
                warning.write('Lenght follow by warning\n')
                warning.write(length+'\n')
                warning.write('***********\n')
                warning.write('Cost\n')
                warning.write(cost+'\n')
                warning.write('***********\n')
                warning.write('\n')
                warning.write('Signed by manager\n')
                warning.write(boss +'\n')
                warning.write('***********\n')
                warning.close()
        elif menu == 4:
            print('exiting administation console...')
            break






money = 100000
cars = {'volvo 2005', 'volvo 2010', 'volvo 2015' }

while True: #Big while menu
    print(money, 'Kr as founds')
    menu = int(input('Whats today service \n: staff login (1) \n, register as buyers (2)\n, warranty check (3)\n, staff managemnt(Admin) (4) \n, exit the program (5)\n' + 'Input: ' ))
    #This is to login as staff
    if menu == 1:
        menu2 = 0
        menu2 = int(input('Do you want to check in: 1: for yes or 2: read logg: '))
        if menu2 == 1:
            print('yes')
            staff() #start staff funktion
        elif menu2 == 2:
            print('Read log')
            staff_read() #start staff_read funktion

    elif menu == 2: 
        # this is to register purchase
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
                ticket() #start ticket funktion
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
                ticket() # funktion
                print('You need fill warranty license')
                money -= 70000
                print(money)
                print('after you finnished sign ticket for purches next is sign warranty license')
                agreement() # funktion
            elif menu5 == 'no':
                print(cars) # array of cars
                print('here is aviable cars to purchase')

    elif menu == 3: #this is warranty section able to register and register service for repair time
        print('Welcome to warranty checkout, here you can check if you are listed in warranty')
        menu7 = input("Do you want us to check your warranty: Yes or no: ")
        if menu7 == 'yes':
            print('Let us take a look at warranty database in your name')
            agreement_read() # funktion
            menu8 = input('Does your name show in database? Yes or no: ')
            if menu8 == 'yes':
                print('Do you seek maintenance')
                menu9 = input('Yes or No i want to read my service status: ')
                if menu9 == 'yes':
                    print('let us take a look at service and warranty')
                    service_read() # funktion
                    print('Next warranty')
                    agreement_read()  # funktion
                    print('Next is proof of purchase the car')
                    ticket_read()# funktion
                    menu11 = input('Do you want to register your warranty and service it cost 500 kr?: yes or no: ')
                    if menu11 == 'yes' and money > 500:
                        money -= 500
                        print('Alright service registering')
                        service() # funktion
                        print('Then warranty registering')
                        agreement() # funktion
                        print('We let you know when car is finished from service!')
                    elif menu11 == 'no':
                        print('Bye')
                    else: 
                        print('Not enough founds to apply service')
                elif menu9 == 'no':
                    print('Alright let see service status')
                    service_read() # funktion
                    menu10 = input('Do you want to register at service 500kr cost it?: yes or no: ')
                    if menu == 'yes' and money > 500:
                        print('Let us see how we can help you att service registering')
                        service() # funktion
                        money -= 500
                    elif menu10 == 'no':
                        print('Goodbye thank you for your patience')
                    else: 
                        print('Not enough founds to apply service')
            elif menu8 == 'no':
                print('Do you want to register your warranty?')
                menu12 = input('Yes or no: ')
                if menu12 == 'yes':
                    print('Let us see')
                    agreement() # funktion
                elif menu12 == 'no':
                    print('Bye')
        elif menu7 == 'no':
            print('Get back any time!')

    elif menu == 4: # This sis for addministatore sektion is for manager to login
        print('This section is for staff management')
        
        menu13 =input('Welcome do you want to login administration console? yes or no: ')
        if menu13 == 'yes':
            print('loading into console...')
            managment()
        elif menu13 == 'no':
            print('Call us if you need to use administator console')
    elif menu == 5:
        break
