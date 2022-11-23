from data import *
from os import system

filename='bevasarlo.cvs'



def menu():
    valasztas=''
    print
    system('cls')
    print('0 - Kilépés')
    print('1 - Meglévő lista betöltése')
    print('2 - Lista újrakezdése')
    print('2 - Bevásárlólista') 
    print('3 - Termék hozzáadása')
    print('4 - Termék törlése')
    print('5 - Lista nyomtatása')

def listabetoltes():
    file=open('bevasarlo.csv','r',encoding='utf-8')
    file.readline()
    for egysor in file:
        darabolt=egysor.strip().split(';')
        termekek.append(darabolt[0])
        mennyiseg.append(int(darabolt[1]))
        egysegar.append(int(darabolt[2]))
    file.close()



def termeklista():
    system('cls')
    print('Termékek listája: ')
    for termek in termekek:
        print(f'\t{termek}')
        




