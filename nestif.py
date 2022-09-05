earn = int(input('Enter you earnings: '))
if earn >= 15000:
    print('Pass')
    if earn < 70000:
        print('Silver card')
    if earn < 100000:
        print('Gold card')
    if earn > 100000:
        print('Platinum card')
            
else:
        print('Not pass')

    