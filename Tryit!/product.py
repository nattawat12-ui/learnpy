id_product = str(input('ID Product: '))
price_product = int(input('Price Product: '))
quantity = int(input('Quantity: '))
if id_product[1] == '1':
    sum=price_product*quantity*97/100
elif id_product[1] == '2':
    if quantity <= 3 :
        sum=price_product*quantity*97/100
    if quantity >= 3 :  
        sum=price_product*quantity*95/100
else:
    sum=price_product*quantity
print(sum)