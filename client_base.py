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
print ("\n1 ���������� �������")
print ("2 ����� �� ����")
print ("3 �����")
print ("4 ��������")
print ("5 �����")
while True:
    n = input ("\n�������� �����: ")
    if n == 1:
        kl = raw_input ("\n������� ��� �������: ")
        add = raw_input ("������� ����� �������: ")
        tlf = input ("������� ����� ��� ����� � ��������: ")
        strst = {'KL': kl, 'ADD': add, 'TLF': tlf}
        s.append (strst)
    elif n == 2:
        kl = raw_input ("\n������� ��� ������� ��� ������ �� ����: ")
        flag = 1
        for strst in s:
            if strst ['KL'] == kl:
                flag = 0
                print (strst ['ADD'] + " " + str(strst ['TLF']))
                break
        if flag == 1:
            print ("��� ����������")
    elif n == 3:
        for strst in s:
            print (strst ['KL'] + " " + strst ['ADD'] + " " + str (strst ['TLF']))
    elif n == 4:
        add = raw_input ("\n������� ����� �������: ")
        for strst in s:
            if strst ['ADD'] == add:
                s.remove (strst)
                print ("������ �������")
                break
    else:
        print ("\n�� ��������")
        break
f = open ("base.txt", "w")
#pickle.dump (s,f)
for strst in s:
    f.write (strst ['KL'] + " " + strst ['ADD'] + " " + str (strst ['TLF']) + "\n")
f.close ()
