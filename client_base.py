# -*- coding: cp1251 -*-
#import pickle
s = []
try:
    f = open ("base.txt", "r")
    #s = pickle.load (f)
    for l in f:
        kl,add,tlf_s = (l.split (' '))
        strst = {'KL': kl, 'ADD': add, 'TLF': int (tlf_s)}
        s.append (strst)
    f.close ()
except:
    pass
print ("\n1 Добавление клиента")
print ("2 Поиск по базе")
print ("3 Вывод")
print ("4 Удаление")
print ("5 Выход")
while True:
    n = input ("\nВыберите пункт: ")
    if n == 1:
        kl = raw_input ("\nВведите ФИО клиента: ")
        add = raw_input ("Введите адрес клиента: ")
        tlf = input ("Введите номер для связи с клиентом: ")
        strst = {'KL': kl, 'ADD': add, 'TLF': tlf}
        s.append (strst)
    elif n == 2:
        kl = raw_input ("\nВведите ФИО клиента для поиска по базе: ")
        flag = 1
        for strst in s:
            if strst ['KL'] == kl:
                flag = 0
                print (strst ['ADD'] + " " + str(strst ['TLF']))
                break
        if flag == 1:
            print ("Нет результата")
    elif n == 3:
        for strst in s:
            print (strst ['KL'] + " " + strst ['ADD'] + " " + str (strst ['TLF']))
    elif n == 4:
        add = raw_input ("\nВведите адрес клиента: ")
        for strst in s:
            if strst ['ADD'] == add:
                s.remove (strst)
                print ("Строка удалена")
                break
    else:
        print ("\nДо свидания")
        break
f = open ("base.txt", "w")
#pickle.dump (s,f)
for strst in s:
    f.write (strst ['KL'] + " " + strst ['ADD'] + " " + str (strst ['TLF']) + "\n")
f.close ()
