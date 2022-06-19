def staff():
    print("Start to save file")

    staff = open('staff.txt', 'a')
    employee = input('Enter your name to check in: ')
    staffId = input('enter staff id: ')

    staff.write(employee + ',' + ' Welcome staff ID: ' + staffId + '\n')
    print(' Welcome ' + employee + ' Your staff ID: ' + staffId + ' data is stored in server ')
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
    print('This section is for car purchase')
    ticket = open('ticket.txt', 'a')
   
    car_price = input("Enter car prise: ")
    car_model = input('enter car model: ')
    manufacture_date = input('manufacture date: ')
    owner = input('Name of owner: ')

    ticket.write(' $ ' + car_price + ',' + ' Model: ' + car_model + ' Manufacture date: ' + manufacture_date + ' , ' + owner +'\n')
    ticket.close
    
    ticket = open('ticket.txt', 'r')
    print(ticket.read(), 'checkout')

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

while True:
    array = {'Register buyers', 'Handle cars','Perform service, repairs and warranty matters', 'Manage staff' }
    print(array)
    menu = input('Whats today service:' )
    if menu == 1:
    elif menu == 2:
    elif menu == 3:
    elif menu == 4:
    elif menu == 5:
        break