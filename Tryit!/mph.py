print('_'*14)
print('KPH','\t','MPH')
print('-'*14)
KPH = 60
while KPH <= 130:
    MPH = KPH*0.6214
    print(format(KPH,'.1f'),'\t',format(MPH,'.1f'))
    KPH+=10