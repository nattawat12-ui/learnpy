#number = int(input('Enter number: '))
#disply = sum(1+2+3+4+5+6+7+8+9+10)
#x = sum(range(1,number+1))
#print(x)
number = int(input('Enter number: '))
s=0
for i in range(1,number+1,1):
    s+=i
print('Sum:',s)
