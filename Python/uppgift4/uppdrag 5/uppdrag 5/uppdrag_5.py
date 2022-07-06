def vending(): #defined use single mode vending buy one att time!
    print('vending machine buy mode "one at time"...')
    # This limit user to insert money maximum 100 kr
    while True: # while is true
        money = int(input('Input machine amount money: '))
        if money > 100: # if money more 100 kr
            print('This machine only accept 100 kr as maximum input') # print statment
        elif money <= 100: #if money bigger and equal to 100 kr money accepts
            print('Machine accepts money...\n') # print statment
            break
    '''
    
    Use your imaganation as list display avaible items 
    This machine does not need error handling beacuse user only promted once!
    
    '''
    slot1 = ['marobo', 'cocola', 'nudlar']
    slot2 = ['kinderkex', 'cocola-light', 'loka']
    slot3 = ['grill-chips', 'viniger-chips', 'cocola-chips']
    slot4 = ['Rizz', 'fonzies', 'nutella-cokies']
    slot5 = ['twix', 'water','snacks']
    '''
    
    Use your imaganation as list display avaible items
    print(slot1) prints whole list of slot 1
    print('statment')

    output:
    slot 1 = marabo, cocola, nudlar
    print(    'item',  'item', 'item', )

    This is purpes to emulate graphical display on real vending machine as for it is importent not taking it serously!
    *with spaces to format list to ouput optimal resulation.
    
    '''
    print(slot1)
    print(' E1 15.5 kr,   E2 20 kr, E3 30 kr')
    print(slot2)
    print(' E4 12.12 kr,       E5 15 kr,     E6 25kr')
    print(slot3)
    print(' E7 14 kr,           E8 25 kr,       E9 15 kr')
    print(slot4)
    print(' E10 10 kr, E11 12 kr,  E12 45 kr')
    print(slot5)
    print(' E13 17 kr, E14 10 kr, E15 14 kr')
    
    '''
    select has number to emulate buttons on vending machine
    output:
    E1, E2, E3 and so on...
    '''

    select = input('\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n Input machine: ') # users input with no while loop
    if select == 'E1' and money > 15.5: # if E1 and money are less 15.5 it check amount money given draw 15.5 kr
        print('It cost you 15 kr') # notify user with print statment
        money -= 15.5 # money increments -15.5 ot total money varibel wich user input may reach 100 maximum allownce
        print(slot1[0]) #print slot1[index 0]
        slot1.remove('marobo') # remove slot1: marabo
        for x in slot1, slot2 ,slot3 ,slot4 , slot5: #for each loop to dislay avaible items after  slot1.remove
            print(x) # prints x varibel in list of slot1,slot2,slot3,slot4,slot5
            '''
            Rest of funktions form E1->E15 are same with repeated values in diffrent form and shape!
            '''
    elif select == 'E2' and money > 20: # same statement!
        print('It cost you 20 kr')
        money -= 20
        print(slot1[1])
        slot1.remove('cocola')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E3' and money > 30: # same statement!
        print('It cost you 30 kr')
        money -= 30
        print(slot1[2])
        slot1.remove('nudlar')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E4' and money > 12.12: # same statement!
        print('It cost you 12.12 kr')
        money -= 12.12
        print(slot2[0])
        slot2.remove('kinderkex')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E5' and money > 15: # same statement!
        print('It cost you 15 kr')
        money -= 15
        print(slot2[1])
        slot2.remove('cocola-light')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E6' and money > 25: # same statement!
        print('It cost you 25 kr')
        money -= 25
        print(slot2[2])
        slot2.remove('loka')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E7' and money > 14: # same statement!
        print('It cost you 14 kr')
        money -= 14
        print(slot3[0])
        slot3.remove('grill-chips')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E8' and money > 25: # same statement!
        print('It cost you 25 kr')
        money -= 25
        print(slot3[1])
        slot3.remove('viniger-chips')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E9' and money > 15: # same statement!
        print('It cost you 15 kr')
        money -= 15
        print(slot3[2])
        slot3.remove('cocola-chips')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E10' and money > 10: # same statement!
        print('It cost you 10 kr')
        money -= 10
        print(slot4[0])
        slot4.remove('Rizz')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E11' and money > 12: # same statement!
        print('It cost you 12 kr')
        money -= 12
        print(slot4[1])
        slot4.remove('fonzies')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E12' and money > 45: # same statement!
        print('It cost you 45 kr')
        money -= 45
        print(slot4[2])
        slot4.remove('nutella-cokies')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E13' and money > 10: # same statement!
        print('It cost you 10 kr')
        money -= 10
        print(slot5[0])
        slot5.remove('twix')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E14' and money > 17: # same statement!
        print('It cost you 17 kr')
        money -= 17
        print(slot5[1])
        slot5.remove('water')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E15' and money > 14: # same statement!
        print('It cost you 14 kr')
        money -= 14
        print(slot5[2])
        slot5.remove('snacks')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    else:
        print('Not enough founds or program not accept input') #This else principel is reached when money is not meet requiments of if or elif-sets. It ouput print statement

    '''
    This section is soposed to emulate tickets after purchase is made
    '''
     
    while True: # while loop
        menu = input('load file: Load, append, exit: ') # load or oppend file
        if menu == 'load':
            try: # try to open file if it fails
                file = open('kvitto1.txt', 'r+') #open file
                print(file.read()) # print content of file
                file.close() # closes file
            except: # it excepts a FileNotFoundError
                (FileNotFoundError) 
                print('File not found')
        elif menu == 'append': #Append to file
            file = open('kvitto1.txt', 'a') #oppen file as appending
            purchase = input('What did you buy?: ') # input user what did they bay
            cost = input('How much did it cost?: ') # cost input
            name = input('Your name: ') 
            file.write('**********' + '\n')
            file.write('Vending machine: signle mode, kvitto1' + '\n')
            file.write('**********' + '\n')
            file.write('*' + '\n')
            file.write('**********' + '\n')
            file.write('Your name:' + name + '\n')
            file.write('**********' + '\n')
            file.write('*' + '\n')
            file.write('**********' + '\n')
            file.write( 'Money left: ' + str(money) + ',' + 'kr:' + cost + ',' + purchase + '\n') #Write file with varibel that must be in string format
            file.write('**********' + '\n')
            file.write('*' + '\n')
            while True: # emulate cash back from machine
                if money < 100:
                    print('Here is rest of your money')
                    money -= money
                    print(money)
                    break # break loop
                elif money >= 100:
                    print('Money still there want get it back? yes:')
                    input('Input: ')
                    if menu == 'yes':
                        money -= money
                        break # break loop
            file.close() # file closes
            print('File written!')
        elif menu == 'exit':
            break
   
def vending_batch(): #This vending machine may be used purchase multiple times
    print('Vending machine buy mode "batch mode"')

    while True:
        money = int(input('Input machine amount money: '))
        if money > 100:
           print('This machine only accept 100 kr as maximum input')
        elif money <= 100:
            print('Machine accepts money...\n')
            break

    '''
    
    Use your imaganation as list display avaible items
    *This machine needed error handling beacuse user only promted many times!
    
    '''
    slot1 = ['marobo', 'cocola', 'nudlar', '', ''] # get list of range error thats why i add more indexes
    slot2 = ['kinderkex', 'cocola-light', 'loka', '', '']
    slot3 = ['grill-chips', 'viniger-chips', 'cocola-chips','' ,'']
    slot4 = ['Rizz', 'fonzies', 'nutella-cokies', '', '']
    slot5 = ['twix', 'water','snacks','', '']
    slot6 = {':Items:'}
    slot7 = {':Amount paid:'}
    slot8 = {':Kcal:'}
    '''
    
    Use your imaganation as list display avaible items
    print(slot1) prints whole list of slot 1
    print('statment')

    output:
    slot 1 = marabo, cocola, nudlar
    print(    'item',  'item', 'item', )

    This is purpes to emulate graphical display on real vending machine as for it is importent not taking it serously!
    with spaces to format list to ouput optimal resulation.
    
    '''
    print(slot1)
    print(' E1 15.5 kr,   E2 20 kr, E3 30 kr')
    print(slot2)
    print(' E4 12.12 kr,       E5 15 kr,     E6 25kr')
    print(slot3)
    print(' E7 14 kr,           E8 25 kr,       E9 15 kr')
    print(slot4)
    print(' E10 10 kr, E11 12 kr,  E12 45 kr')
    print(slot5)
    print(' E13 17 kr, E14 10 kr, E15 14 kr')
    '''
    select has number to emulate buttons on vending machine
    output:
    E1, E2, E3 and so on...

    Diffrence with vending machine and batch vending that has big loop

    '''
    while True: # added while loop to enable batch purchases
        select = input('\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n, exit \n Input machine: ')
        if select == 'E1' and money > 15.5: # if statement wih and money are less 15.5
            print('It cost you 15.5 kr')# print satetenebt
            money -= 15.5 # increments money from user input - 15.5
            print(money) #print user money
            print(slot1[0]) # print slot index: 0
            try:# this will try to remove marabo from slot 1
                slot1.remove('marobo')
            except: # progran will throw error if user tries enter same button so program will not crash
                print('You already have it"') # print statment!
            try: #try to add to list
                slot6.add('marobo') #add marabo to shopping list
                slot7.add('15.5') # add 15.5kr to slot 7
                slot8.add(500) # add 500 kcal to slot 8
            except: #if not succeded 
                print('It did not succed to add to list"') # print statment
            for x in slot1, slot2 ,slot3 ,slot4 , slot5: # for each loop
                print(x) # print context of x wich i slot1,slot2,slot3,slor4,slot5
        elif select == 'E2' and money > 20: #Same statment!
            print('It cost you 20 kr')
            money -= 20
            print(money)
            print(slot1[1])
            try: 
                slot1.remove('cocola')
            except: 
                print('You already have it!')
            try: 
                slot6.add('cocola')
                slot7.add('20')
                slot8.add(1000)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E3' and money > 30: #Same statment!
            print('It cost you 30 kr') 
            money -= 30
            print(money)
            print(slot1[2])
            try:
                slot1.remove('nudlar')
            except: 
                print('You already have it!')
            try:
                slot6.add('nudlar')
                slot7.add('30')
                slot8.add(800)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E4' and money > 12.12:#Same statment!
            print('It cost you 12.12 kr')
            money -= 12.12
            print(money)
            print(slot2[0])
            try:
                slot2.remove('kinderkex')
            except:
                print('You already have it!')
            try:
                slot6.add('kinderkex')
                slot7.add('12.12')
                slot8.add(650)
            except:
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E5' and money > 15:#Same statment!
            print('It cost you 15 kr')
            money -= 15
            print(money)
            print(slot2[1])
            try:
                slot2.remove('cocola-light')
            except: 
                print('You already have it!')
            try:
                slot6.add('cocola-light')
                slot7.add('15')
                slot8.add(1)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E6' and money > 25:#Same statment!
            print('It cost you 25 kr')
            money -= 25
            print(money)
            print(slot2[2])
            try:
                slot2.remove('loka')
            except: 
                print('You already have it!')
            try:
                slot6.add('loka')
                slot7.add('25')
                slot8.add(1)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E7' and money > 14:#Same statment!
            print('It cost you 14 kr')
            money -= 14
            print(money)
            print(slot3[0])
            try:
                slot3.remove('grill-chips')
            except: 
                print('You already have it')
            try:
                slot6.add('grill-chips')
                slot7.add('14')
                slot8.add(560)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E8' and money > 25:#Same statment!
            print('It cost you 25 kr')
            money -= 25
            print(money)
            print(slot3[1])
            try:
                slot3.remove('viniger-chips')
            except: 
                print('You already have it!')
            try:
                slot6.add('viniger-chips')
                slot7.add('25')
                slot8.add(600)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E9' and money > 15:#Same statment!
            print('It cost you 15 kr')
            money -= 15
            print(money)
            print(slot3[2])
            try:
                slot3.remove('cocola-chips')
            except: 
                print('You already have it!')
            try:
                slot6.add('cocola-chips')
                slot7.add('15')
                slot8.add(800)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E10' and money > 10:#Same statment!
            print('It cost you 10 kr')
            money -= 10
            print(money)
            print(slot4[0])
            try:
                slot4.remove('Rizz')
            except: 
                print('You already have it!')
            try:
                slot6.add('Rizz')
                slot7.add('10')
                slot8.add(200)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E11' and money > 12:#Same statment!
            print('It cost you 12 kr')
            money -= 12
            print(money)
            print(slot4[1])
            try:
                slot4.remove('fonzies')
            except: 
                print('You already have it!')
            try:
                slot6.add('fonzies')
                slot7.add('12')
                slot8.add(400)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E12' and money > 45:#Same statment!
            print('It cost you 45 kr')
            money -= 45
            print(money)
            print(slot4[2])
            try:
                slot4.remove('nutella-cokies')
            except: 
                print('You already have it!')
            try:
                slot6.add('nutella-cokies')
                slot7.add('45')
                slot8.add(600)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E13' and money > 10:#Same statment!
            print('It cost you 10 kr')
            money -= 10
            print(money)
            print(slot5[0])
            try:
                slot5.remove('twix')
            except: 
                print('You already have it!')
            try:
                slot6.add('twix')
                slot7.add('10')
                slot8.add(200)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E14' and money > 17:#Same statment!
            print('It cost you 17 kr')
            money -= 17
            print(money)
            print(slot5[1])
            try:
                slot5.remove('water')
            except: 
                print('You already have it!')
            try:
                slot6.add('water')
                slot7.add('17')
                slot8.add(0)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E15' and money > 14:#Same statment!
            print('It cost you 14 kr')
            money -= 14
            print(money)
            print(slot5[2])
            try:
                slot5.remove('snacks')
            except: 
                print('You already have it!')
            try:
                slot6.add('snacks')
                slot7.add('14')
                slot8.add(450)
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'exit':
            print('good bye...')
            break
        else:
            print('Not enough founds or program not accept input')
            break

     
    while True:#Same statment as at "def vending"!
        menu = input('load file: Load, append, exit: ')
        if menu == 'load':
            try: 
                file = open('kvitto2.txt', 'r+') # open diffrent file as kvitto2
                print(file.read())
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
        elif menu == 'append':
            name = input('Your name: ')
            file = open('kvitto2.txt', 'a') #open kvitto2 as appending
            file.write('**********' + '\n')
            file.write('Vending machine: Batch, kvitto2' + '\n')
            file.write('**********' + '\n')
            file.write('*' + '\n')
            file.write('**********' + '\n')
            file.write('Your name:' + name + '\n')
            file.write('**********' + '\n')
            file.write('*' + '\n')
            file.write('**********' + '\n')
            file.write( 'Money left: ' + str(money) + ',' + '\n')
            file.write('**********' + '\n')
            file.write('*' + '\n')
            while True:
                if money < 100:
                    print('Here is rest of your money')
                    money -= money
                    print(money)
                    break
                elif money > 100:
                    print('Money still there want get it back? yes:')
                    input('Input: ')
                    if menu == 'yes':
                        money -= money
                        break
            file.write('*' + '\n')
            file.write('**********' + '\n')
            file.write(str(slot6) + '\n') # amount paid
            file.write(str(slot7) + '\n') # items
            file.write(str(slot8) + '\n') # kcal
            file.write('**********' + '\n')
            file.write('*' + '\n')
            print('File written!')
            file.close()
        elif menu == 'exit':
            break


def vending_search():
    print('Wending search mode')
    print('!Enter a number. Program wont accept other input!')

    '''
        This is dictonary work as switch case!

        varibel = integer(input())

        defined varibel_name()
                print-statment('Something')
        dictonary = {1: varibel_name}
        dictonary.get(varibel) ()
        -------------------------------------
        in retrospectrum
        x = int(input())
        def a()
            print('Something')
        dict = {1: a}
        dict.get(x) ()
    '''

    '''
    
    Use your imaganation as list display avaible items
    print(slot1) prints whole list of slot 1
    print('statment')

    output:
    slot 1 = marabo, cocola, nudlar
    print(    'item',  'item', 'item', )

    This is purpes to emulate graphical display on real vending machine as for it is importent not taking it serously!
    with spaces to format list to ouput optimal resulation.
    
    '''
    slot1 = ['marobo', 'cocola', 'nudlar', '', '']
    slot2 = ['kinderkex', 'cocola-light', 'loka', '', '']
    slot3 = ['grill-chips', 'viniger-chips', 'cocola-chips', '', '']
    slot4 = ['Rizz', 'fonzies', 'nutella-cokies', '']
    slot5 = ['twix', 'water','snacks', '', '']
    '''
    select has number to emulate buttons on vending machine
    output:
    E1, E2, E3 and so on...
    '''
    print('\n')
    print(slot1)
    print(' E1 15.5 kr,   E2 20 kr, E3 30 kr')
    print(slot2)
    print(' E4 12.12 kr,       E5 15 kr,     E6 25kr')
    print(slot3)
    print(' E7 14 kr,           E8 25 kr,       E9 15 kr')
    print(slot4)
    print(' E10 10 kr, E11 12 kr,  E12 45 kr')
    print(slot5)
    print(' E13 17 kr, E14 10 kr, E15 14 kr')
    print('\n')
    print('\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n')
    while True: # While loop
        try: # Try to get x input in int
            x = int(input('Enter Number: '))
        except: # if user enter other value not are int-range it trhow value error 
            (ValueError)
            print('Error invalid input!') # print statment!

        def first(): # print statment!
            print('E1')
            print('Marabo')
            print('15.5 kr')
            print('500 kcal')
            print('200 g')
            print('laktose')
        def second(): # print statment!
            print('E2')
            print('cocola')
            print('20 kr')
            print('1000 kcal')
            print('450 g')
            print('sugar and chemicals')
        def third(): # print statment!
            print('E3')
            print('Nudlar')
            print('30 kr')
            print('800 kcal')
            print('200 g')
            print('sugar and salt')
        def fourth(): # print statment!
            print('E4')
            print('Kinderkex')
            print('12.12 kr')
            print('650 kcal')
            print('50 g')
            print('sugar and chemicals and lactose')
        def fith(): # print statment!
            print('E5')
            print('cocola-light')
            print('15 kr')
            print('1 kcal')
            print('450 g')
            print('sugar and chemicals')
        def six(): # print statment!
            print('E6')
            print('Loka')
            print('25 kr')
            print('1 kcal')
            print('450 g')
            print('carbonise water')
        def seven(): # print statment!
            print('E7')
            print('Grill-chips')
            print('17 kr')
            print('560 kcal')
            print('400 g')
            print('high fatt and salt')
        def eight(): # print statment!
            print('E8')
            print('viniger-chips')
            print('25 kr')
            print('600 kcal')
            print('350 g')
            print('high fatt and salt')
        def nine():# print statment!
            print('E9')
            print('Cocola-chips')
            print('800 kcal')
            print('200 g')
            print('high fatt and salt')
        def ten(): # print statment!
            print('E10')
            print('Rizz')
            print('10 kr')
            print('200 kcal')
            print('50 g')
            print('Sugar and lactose')
        def eleven(): # print statment!
            print('E11')
            print('fronzies')
            print('12 kr')
            print('400 kcal')
            print('50 g')
            print('Sugar and lactose')
        def tvelve(): # print statment!
            print('E12')
            print('Nutella-cokies')
            print('45 kr')
            print('600 kcal')
            print('150 g')
            print('Sugar and lactose')
        def thirteen(): # print statment!
            print('E13')
            print('twix')
            print('17 kr')
            print('200 kcal')
            print('100 g')
            print('Sugar and lactose')
        def forteen(): # print statment!
            print('E14')
            print('water')
            print('10 kr')
            print('0 kcal')
            print('450 g')
        def fifteen(): # print statment!
            print('E15')
            print('snacks')
            print('14 kr')
            print('450 kcal')
            print('75 g')
            print('high fatt and salt')
        dict = {
            1:first, 
            2:second,
            3:third,
            4:fourth,
            5:fith,
            6:six,
            7:seven,
            8:eight,
            9:nine,
            10:ten,
            11:eleven,
            12:tvelve,
            13:thirteen,
            14:forteen,
            15:fifteen,
            }
        try: # try get dict by value x
            dict.get(x) () # this closing braket is needed
        except: # except if number are exceed more 15 concatenating number
            print('An error happened, meaby invalid number...') # print statment!
        menu = input('Write "exit" to exit vending machine search mode or press enter to continue.') # it appears after every input to exit program!
        if menu == 'exit': # exit if-statment!
            break
        

def kalkylator():

    while True: # while loop
        enter = input('Want use wending search mode?: yes or no: ') # user input
        if enter == 'yes': # yes
            vending_search() # start vending_search
        elif enter == 'no':
            print('Good luck')

            '''
            Here is to measure amount kcal and i setup kcal rekommended and it writes out to file
            it is important to use vending search to get data amount kcal you get from those item to kalkulate amount
            it is a fun little program.
            '''
        menu = int(input('How many do you want to buy (Rekomended use vending search mode) ?: 1,2,3,4,5, 6: exit program: ')) #menu
        if menu == 1:
            print('Single mode') #single mode
            item1 = input('Enter a item name: ')
            kcal1 = int(input('Enter mount of kcal: '))
            kcal1_rec = 250 # rekommended kcal set
            if kcal1 > kcal1_rec:
                print(item1) # print item
                print('Recomended intake', kcal1_rec,'kcal', 'yours is: ', kcal1, '\n') # print statmend
                file = open('Kalkylator.txt', 'a') # open file
                file.write('items:' + item1 +','+ '\n' + 'Rekommended kcal intake: '  + str(kcal1_rec) + ','  + '\n'+ 'Your kcal intake: '+ str(kcal1)) # write file
                file.close() # close file
                print('file written...') # notify user
            elif kcal1 < kcal1_rec: # if in rekommended kcal intake
                print(item1)# same statment!
                print('You are in rekomended intake', kcal1_rec,'kcal','yours is:', kcal1, '\n') # same statment!
                file = open('Kalkylator.txt', 'a') # same statment!
                file.write( 'items:' + item1 +',' + '\n' + 'Rekommended kcal intake: ' + str(kcal1_rec) +','  + '\n' + 'Your kcal intake: ' + str(kcal1)) # same statment!
                file.close() # same statment!
                print('file written...') # same statment!
            
        elif menu == 2: # same statment but with more values and higher rekmmended intake!
            print('Dual mode')
            item2 = input('Enter item name 1: ')
            item3 = input('Enter item name 2: ')
            kcal2 = int(input('Enter item 1 kcal amount: '))
            kcal3 = int(input('Enter item 2 kcal amount: '))
            totalkcal1 = kcal2 + kcal3
            kcal1_rec2 = 600
            if totalkcal1 > kcal1_rec2:
                print(item2)
                print(item3)
                print('Recomended intake', kcal1_rec2,'kcal', 'yours is: ', totalkcal1)
                file = open('Kalkylator.txt', 'a')
                file.write('Items: ' + item2 + ',' + item3 +',' + '\n' + 'Rekommended kcal intake: ' + str(kcal1_rec2) + ',' + '\n'+ 'Your total kcal intake: ' + str(totalkcal1) + '\n')
                file.close()
                print('file written...')
            elif totalkcal1 < kcal1_rec2:
                print(item2)
                print(item3)
                print('You are in rekomended intake', kcal1_rec2,'kcal','yours is:', totalkcal1)
                file = open('Kalkylator.txt', 'a')
                file.write('Items: ' + item2 + ',' + item3 +','  + '\n'+  'Rekommended kcal intake: ' + str(kcal1_rec2) +',' + '\n'+ 'Your total kcal intake: ' + str(totalkcal1) + '\n')
                file.close()
                print('file written...')

        elif menu == 3: # same statment but with more values and higher rekmmended intake!
            print('Quadro mode')
            item4 = input('Enter item name 1: ')
            item5 = input('Enter item name 2: ')
            item6 = input('Enter item name 3: ')
            kcal4 = int(input('Enter item 1 kcal amount: '))
            kcal5 = int(input('Enter item 2 kcal amount: '))
            kcal6 = int(input('Enter item 3 kcal amount: '))
            totalkcal2 = kcal4 + kcal5 + kcal6
            kcal1_rec3 = 800
            if totalkcal2 > kcal1_rec3:
                print(item4)
                print(item5)
                print(item6)
                print('Recomended intake', kcal1_rec3,'kcal', 'yours is: ', totalkcal2)
                file = open('Kalkylator.txt', 'a')
                file.write('Items: ' +item4 + ',' + item5 +',' + item6 + ',' + '\n'+ 'Rekommended kcal intake: ' + str(kcal1_rec3) + ',' + '\n'+ 'Your total kcal intake: ' + str(totalkcal2) + '\n')
                file.close()
                print('file written...')
            elif totalkcal2 < kcal1_rec3:
                print(item4)
                print(item5)
                print(item6)
                print('You are in rekomended intake', kcal1_rec3,'kcal','yours is:', totalkcal2)
                file = open('Kalkylator.txt', 'a')
                file.write( 'Items: ' + item4 + ',' + item5 +',' + item6 + ',' + '\n'+ 'Rekommended kcal intake: ' + str(kcal1_rec3) + ','+ '\n' + 'Your total kcal intake: ' + str(totalkcal2) + '\n')
                file.close()
                print('file written...')
        elif menu == 4: # same statment but with more values and higher rekmmended intake!
            print('Octa mode')
            item7 = input('Enter item name 1: ')
            item8 = input('Enter item name 2: ')
            item9 = input('Enter item name 3: ')
            item10 = input('Enter item name 4: ')
            kcal7 = int(input('Enter item 1 kcal amount: '))
            kcal8 = int(input('Enter item 2 kcal amount: '))
            kcal9 = int(input('Enter item 3 kcal amount: '))
            kcal10 = int(input('Enter item 4 kcal amount: '))
            totalkcal3 = kcal7 + kcal8 + kcal9 + kcal10
            kcal1_rec4 = 1100
            if totalkcal3 > kcal1_rec4:
                print(item7)
                print(item8)
                print(item9)
                print(item10)
                print('Recomended intake', kcal1_rec4,'kcal', 'yours is: ', totalkcal3)
                file = open('Kalkylator.txt', 'a')
                file.write('Items: ' + item7 + ',' + item8 +',' + item9 + ',' + item10 + ',' + '\n'+ 'Rekommended kcal intake: ' + str(kcal1_rec4) + ',' + '\n'+ 'Your total kcal intake: '+ str(totalkcal3) + '\n')
                file.close()
                print('file written...')
            elif totalkcal3 < kcal1_rec4:
                print(item7)
                print(item8)
                print(item9)
                print(item10)
                print('You are in rekomended intake', kcal1_rec4,'kcal','yours is:', totalkcal3)
                file = open('Kalkylator.txt', 'a')
                file.write( 'Items:' + item7 + ',' + item8 +',' + item9 + ',' + item10 + ',' + '\n'+ 'Rekommended kcal intake: ' + str(kcal1_rec4) +',' + '\n'+ 'Your total kcal intake: ' + str(totalkcal3) + '\n')
                file.close()
                print('file written...')
        elif menu == 5: # same statment but with more values and higher rekmmended intake!
            print('Mode 5')
            item11 = input('Enter item name 1: ')
            item12 = input('Enter item name 2: ')
            item13 = input('Enter item name 3: ')
            item14 = input('Enter item name 4: ')
            item15 = input('Enter item name 5: ')
            kcal11 = int(input('Enter item 1 kcal amount: '))
            kcal12 = int(input('Enter item 2 kcal amount: '))
            kcal13 = int(input('Enter item 3 kcal amount: '))
            kcal14 = int(input('Enter item 4 kcal amount: '))
            kcal15 = int(input('Enter item 5 kcal amount: '))
            totalkcal4 = kcal11 + kcal12 + kcal13 + kcal14 + kcal15
            kcal1_rec5 = 1500
            if totalkcal4 > kcal1_rec5:
                print(item11)
                print(item12)
                print(item13)
                print(item14)
                print(item15)
                print('Recomended intake', kcal1_rec5,'kcal', 'yours is: ', totalkcal4)
                file = open('Kalkylator.txt', 'a')
                file.write( 'items: ' + item11 + ',' + item12 +',' + item13 + ',' + item14 + ',' + item15 + ',' + '\n' +'Rekommended kcal intake: ' + str(kcal1_rec5) + ',' + '\n'+ 'Your total kcal intake: ' + str(totalkcal4) + '\n')
                file.close()
                print('file written...')
            elif totalkcal4 < kcal1_rec5:
                print(item11)
                print(item12)
                print(item13)
                print(item14)
                print(item15)
                print('You are in rekomended intake', kcal1_rec5,'kcal','yours is:', totalkcal4)
                file = open('Kalkylator.txt', 'a')
                file.write( 'Items: ' + item11 + ',' + item12 +',' + item13 + ',' + item14 + ',' + item15 + ',' + '\n' + 'Rekommended kcal intake: ' + str(kcal1_rec5) + ',' + '\n'+ 'Your total kcal intake: ' + str(totalkcal4) + '\n')
                file.close()
                print('file written...')
        elif menu == 6:
            print('Exiting kalkylator...')
            break

def rate(): # this is to rate services 
    print(' Welcome to rate us our service')
    while True: # while loop
        menu = input('load file: Load previus rate, append: rating, exit: ') # menu
        if menu == 'load':
            try: #error handling
                file = open('rate.txt', 'r+')
                print(file.read())
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
        elif menu == 'append':
            file = open('rate.txt', 'a') #open file
            rate = input('How manu stars do you want rate us *-> ***** as maximum stars you can give us. \n Rate: ') # user input
            name = input('Name and surname :')# user input
            service = input('Rate our service: ')# user input
            comment = input('Comments: ')# user input
            file.write('*' + '\n')# file write
            file.write('*' + '\n')
            file.write('**************' + '\n')# file write
            file.write('Rate in stars:' + rate + '\n' + 'Name and surname: ' + name + '\n' + 'Service: ' + service + '\n' + 'Comment: ' + comment + '\n' )# file write
            file.write('**************' + '\n')# file write
            file.write('*' + '\n')# file write
            file.write('*' + '\n')# file write
            file.close()
        elif menu == 'exit':
            break


def kalkylator_file():
     name = input('Your name: ') #user input
     while True: # loop
        print('Hello' + ': ' + name)
        menu = input('load previus kalkylator file?: load or exit \n input: ')
        if menu == 'load':
            try:  # file not found error
                file = open('Kalkylator.txt', 'r+') # file open
                print(file.read()) # print content
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
        elif menu == 'exit': #exit
            break

def kvitto():
     '''
     This is to get kvitto make sure to buy something otherwise it will error out
     '''
     name = input('Your name: ') #user input
     while True: # loop
        print('Hello' + ': ' + name) #user input
        menu = input('load previus kvitto?: load or exit \n input: ') # menu
        if menu == 'load':
            try: #file not found error
                file = open('kvitto1.txt', 'r+') # vvending machine 1 kvitto1
                print(file.read())
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
            try: #file not found error
                file = open('kvitto2.txt', 'r+') #vending machine bach kvitto 2
                print(file.read())
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
        elif menu == 'exit':
            break


while True:
    '''
    This senction is self-explanatory it does not need comment to explain but here in big menu tree and is...
    funktion to appear when selection is made. that binds whole code as one. Please use it in causon 
    '''
    print(' Welcome to vending alley there you can buy at vending machine for diffrent prices.')
    print(' Here can you test out our kalkylator to measure the intake of kcal \n program is built to guide users whieght loss \n ')
    print('*********************************')
    print(' * You can buy one at the time!')
    print(' * You can buy at batch if needed!')
    print(' * Measure amount kcal we fix it!')
    print(' *       *  *  *  *  *           *')
    print(' *      FIVE STAR RATING         *')
    print('*********************************')
    print(' \n')
    menu = input('Buy at vending machine: \n 1 Single mode,\n 2 batch mode, \n 3 search mode, \n 4 rate us, \n 5 exit, \n Input: ')
    print('\n')
    if menu == '1':
        print('\n')
        print('Welcome to vending single mode...')
        print('\n')
        buy = input(' I want to use kalkylator: 1 \n I want make purchase: 2 \n check kvitto: 3 \n check kalkylator file: 4 \n \input: ')
        print('\n')
        if buy == '1':
            print('\n')
            print('Starting kalkylator... \n')
            print('\n')
            kalkylator() #funktion
            print('\n')
        elif buy == '2':
            print('\n')
            print('Start vending machine in single mode...\n')
            print('\n')
            vending() #funktion
            print('\n')
            print('Please rate us\n')
            print('\n')
        elif buy == '3':
            print('\n')
            print('Please rate us!\n')
            print('\n')
            print('Loading kvitto... \n')
            print('\n')
            kvitto() #funktion
            print('\n')
        elif buy == '4':
            print('\n')
            print('Please rate us!\n')
            print('\n')
            print('Loading kalkylator file... \n')
            print('\n')
            kalkylator_file() #funktion
            print('\n')
    elif menu == '2':
        print('\n')
        print('Welcome to vending machine batch mode...\n it is rekommended user kalkylator to se how much kcal you buy')
        print('\n')
        buy2 = input(' I want to use kalkylator: 1 \n I want make purchase: 2 \n check kvitto: 3 \n check kalkylator file: 4 \n \input: ')
        print('\n')
        if buy2 == '1':
            print('\n')
            print('Starting kalkylator... \n')
            print('\n')
            kalkylator() #funktion
            print('\n')
        elif buy2 == '2':
            print('\n')
            print('Start vending machine in single mode...\n')
            print('\n')
            vending_batch() #funktion
            print('\n')
            print('Please rate us\n')
            print('\n')
        elif buy2 == '3':
            print('Please rate us!\n')
            print('\n')
            print('Loading kvitto... \n')
            print('\n')
            kvitto() #funktion
            print('\n')
        elif buy2 == '4':
            print('\n')
            print('Please rate us!\n')
            print('\n')
            print('Loading kalkylator file... \n')
            print('\n')
            kalkylator_file() #funktion
            print('\n')
    elif menu == '3':
        print('Welcome to search mode with our new kalkylator! \n')
        b = input('Do you want to use search mode? yes or no: \n')
        print('\n')
        if b == 'yes':
            print('Before we use search let us check your kvitto \n')
            print('\n')
            c = input('Understood: Yes for check kvitto, no for use search mode or kalkylator  \n Input: ')
            print('\n')
            if c == 'yes':
                print('Starting kvitto...\n')
                print('\n')
                kvitto() #funktion
                d = input('Did you find items\n * It is recommended to use our new tool to measure kcal in kalkylator with your purchase? : \n yes or no: ')
                print('\n')
                if d == 'yes':
                    print('\n')
                    f = input(' Still want use search mode? "yes" or "no" i want to use new kalkylator \n input:')
                    print('\n')
                    if f == 'yes':
                        print('\n')
                        print('Entering search mode \n')
                        print('\n')
                        vending_search() #funktion
                    elif f == 'no':
                        print('\n')
                        print('Enter kalkylator...\n')
                        print('\n')
                        kalkylator() #funktion
                elif d == 'no':
                    print('\n')
                    print('Please purchase by using single mode or batch mode vending machine')
                    print('\n')
            elif c == 'no':
                print('\n')
                i = input('Use search mode or kalkylator: Yes for search mode or No for kalkylator \n Input: ')
                print('\n')
                if i == 'yes':
                    print('\n')
                    print('Entering search mode...\n')
                    print('\n')
                    vending_search() #funktion
                    print('\n')
                elif i == 'no':
                    print('\n')
                    print('Starting kalkylator...\n')
                    print('\n')
                    kalkylator() #funktion
                    print('\n')
        elif b == 'no':
            print('\n')
            g = input('Do you want use our new kalkylator?: \n yes or no: ')
            print('\n')
            if g == 'yes':
                print('\n')
                print('Entering kalkylator mode...\n')
                print('\n')
                print('\n')
                kalkylator() #funktion
            elif g == 'no':
                print('\n')
                print('Bye')
                print('\n')
    elif menu == '4':
        print('\n')
        print('What do you want to rate our service?')
        print('\n')
        a = input('Are you satified: yes or no: ') 
        print('\n')
        if a == 'yes':
            print('\n')
            print('please rate us')
            print('\n')
            rate() #funktion
            print('\n')
        elif a == 'no':
            print('\n')
            print('Please put your thoughts to rate us!')
            print('\n')
            h = input('"Yes" i do it or "No" i dont want to do it. \n Input: ')
            print('\n')
            if h == 'yes':
                print('\n')
                rate() #funktion
                print('\n')
            elif h == 'no':
                print('\n')
                print('Okey welcome back!')
                print('\n')   
    elif menu == '5':
        print('Exiting vending valley.. thank you and come back for some more!')
        break


    
    