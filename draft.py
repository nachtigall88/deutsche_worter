def check_availability(data, arrange):
    flag = True
    with open(arrange, 'r') as file:
        res = file.readlines()
        for i in res:
            if data in i:
                flag = False
    for i in res:
        print(i)
    return flag



print(check_availability('ordnung', 'try.txt'))
'''
das, Buch, �����
das, Madchen, ����
der, Fehler, �������
None, brauchen, �����������
'''