again = range(1,10)
while  again == 'y':
    cost = int(input('Enter the items wholesales cost: '))
    retail_price= cost *2.5
    print('Retail price:',retail_price)
    again=str(input('Do you have another item? (enter y for y) '))

