a = 'y'
while a == 'y':
    cost = float(input('Enter the item wholesale cost: '))
    retail_price = cost*2.5
    print('retail price',retail_price)
    a = input('Do you have another item? (Enter y for yes): ')