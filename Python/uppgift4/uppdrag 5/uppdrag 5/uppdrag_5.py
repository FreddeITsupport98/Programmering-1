
def vending():
    print('vending machine buy mode "one at time"...')

    while True:
        money = int(input('Input machine amount money: '))
        if money > 100:
            print('This machine only accept 100 kr as maximum input')
        elif money <= 100:
            print('Machine accepts money...\n')
            break

    slot1 = ['marobo', 'cocola', 'nudlar']
    slot2 = ['kinderkex', 'cocola-light', 'loka']
    slot3 = ['grill-chips', 'viniger-chips', 'cocola-chips']
    slot4 = ['Rizz', 'fonzies', 'nutella-cokies']
    slot5 = ['twix', 'water','snacks']
    
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
    
    select = input('\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n Input machine: ')
    if select == 'E1' and money > 15.5:
        print('It cost you 15 kr')
        money -= 15.5
        print(slot1[0])
        slot1.remove('marobo')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E2' and money > 20:
        print('It cost you 20 kr')
        money -= 20
        print(slot1[1])
        slot1.remove('cocola')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E3' and money > 30:
        print('It cost you 30 kr')
        money -= 30
        print(slot1[2])
        slot1.remove('nudlar')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E4' and money > 12.12:
        print('It cost you 12.12 kr')
        money -= 12.12
        print(slot2[0])
        slot2.remove('kinderkex')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E5' and money > 15:
        print('It cost you 15 kr')
        money -= 15
        print(slot2[1])
        slot2.remove('cocola-light')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E6' and money > 25:
        print('It cost you 25 kr')
        money -= 25
        print(slot2[2])
        slot2.remove('loka')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E7' and money > 14:
        print('It cost you 14 kr')
        money -= 14
        print(slot3[0])
        slot3.remove('grill-chips')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E8' and money > 25:
        print('It cost you 25 kr')
        money -= 25
        print(slot3[1])
        slot3.remove('viniger-chips')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E9' and money > 15:
        print('It cost you 15 kr')
        money -= 15
        print(slot3[2])
        slot3.remove('cocola-chips')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E10' and money > 10:
        print('It cost you 10 kr')
        money -= 10
        print(slot4[0])
        slot4.remove('Rizz')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E11' and money > 12:
        print('It cost you 12 kr')
        money -= 12
        print(slot4[1])
        slot4.remove('fonzies')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E12' and money > 45:
        print('It cost you 45 kr')
        money -= 45
        print(slot4[2])
        slot4.remove('nutella-cokies')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E13' and money > 10:
        print('It cost you 10 kr')
        money -= 10
        print(slot5[0])
        slot5.remove('twix')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E14' and money > 17:
        print('It cost you 17 kr')
        money -= 17
        print(slot5[1])
        slot5.remove('water')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    elif select == 'E15' and money > 14:
        print('It cost you 14 kr')
        money -= 14
        print(slot5[3])
        slot5.remove('snacks')
        for x in slot1, slot2 ,slot3 ,slot4 , slot5:
            print(x)
    else:
        print('Not enough founds or program not accept input')

    while True:
        if money < 100:
            print('Here is rest of your money')
            money -= money
            print(money)
            break
        elif money >= 100:
            print('Money still there want get it back? yes:')
            input('Input: ')
            if menu == 'yes':
                money -= money
                break
     
    while True:
        menu = input('load file: Load, append, exit: ')
        if menu == 'load':
            try: 
                file = open('kvitto.txt', 'r+')
                print(file.read())
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
        elif menu == 'append':
            file = open('kvitto.txt', 'a')
            purchase = input('What did you buy?: ')
            cost = input('How much did it cost?: ')
            file.write( 'Money left: ' + str(money) + ',' + 'kr:' + cost + ',' + purchase + '\n')
            file.close()
        elif menu == 'exit':
            break
   
def vending_batch():
    print('Vending machine buy mode "batch mode"')

    while True:
        money = int(input('Input machine amount money: '))
        if money > 100:
            print('This machine only accept 100 kr as maximum input')
        elif money <= 100:
            print('Machine accepts money...\n')
            break

    slot1 = ['marobo', 'cocola', 'nudlar', '']
    slot2 = ['kinderkex', 'cocola-light', 'loka', '']
    slot3 = ['grill-chips', 'viniger-chips', 'cocola-chips', '']
    slot4 = ['Rizz', 'fonzies', 'nutella-cokies', '']
    slot5 = ['twix', 'water','snacks', '']
    slot6 = {''}
    
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
    
    while True:
        select = input('\n E1, E2, E3,\n E4, E5, E6\n E7, E8, E9 \n E10, E11 E12 \n E13, E14, E15 \n, exit \n Input machine: ')
        if select == 'E1' and money > 15.5:
            print('It cost you 15.5 kr')
            money -= 15.5
            print(money)
            print(slot1[0])
            try:
                slot1.remove('marobo')
            except: 
                print('You already have it"')
            try:
                slot6.add('marobo')
            except: 
                print('It did not succed to add to list"')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E2' and money > 20:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E3' and money > 30:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E4' and money > 12.12:
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
            except:
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E5' and money > 15:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E6' and money > 25:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E7' and money > 14:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E8' and money > 25:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E9' and money > 15:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E10' and money > 10:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E11' and money > 12:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E12' and money > 45:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E13' and money > 10:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E14' and money > 17:
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
            except: 
                print('It did not succed to add to list!')
            for x in slot1, slot2 ,slot3 ,slot4 , slot5:
                print(x)
        elif select == 'E15' and money > 14:
            print('It cost you 14 kr')
            money -= 14
            print(money)
            print(slot5[3])
            try:
                slot5.remove('snacks')
            except: 
                print('You already have it!')
            try:
                slot6.add('snacks')
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

    while True:
        if money < 100:
            print('Here is rest of your money')
            money -= money
            print(money)
            break
        elif money >= 100:
            print('Money still there want get it back? yes:')
            input('Input: ')
            if menu == 'yes':
                money -= money
                break
     
    while True:
        menu = input('load file: Load, append, exit: ')
        if menu == 'load':
            try: 
                file = open('kvitto.txt', 'r+')
                print(file.read())
                file.close()
            except:
                (FileNotFoundError)
                print('File not found')
        elif menu == 'append':
            file = open('kvitto.txt', 'a')
            file.write( 'Money left: ' + str(money) + ',' + '\n')
            file.write(str(slot6))
            file.close()
        elif menu == 'exit':
            break

vending_batch()
   
money = 1000   

while True:
    menu = input('Buy vending machine: \n 1 Single mode,\n 2 batch mode, \n search mode 3, \n 4 exit, \n Input: ')