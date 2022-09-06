earn = int(input('Enter you earnings: '))
if earn >= 15000:
    print('Pass')
    if earn < 70000:
        print('Silver Card')
    elif earn < 100000 :
        print('Gold Card')
    elif earn > 100000:
        print('Platinum Card')
            
else:
        print('Not pass')

    