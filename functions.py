from data import *
from os import system

filename='bevasarlo.csv'



def menu():
    valasztas=''
    print
    system('cls')
    print('0 - Kilépés')
    print('1 - Lista újrakezdése')
    print('2 - Bevásárlólista') 
    print('3 - Termék hozzáadása')
    print('4 - Termék törlése')
    print('5 - Lista nyomtatása')
    return input('Kérem válasszon!:')
    

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
    for i in range(0,len(termekek)):
        print(f'{termekek[i]} - {mennyiseg[i]} darab')
    input("Tovább...")


def mentesFajlba():
    file=open(filename,'w',encoding='utf-8')
    file.write('termekek;mennyiseg;egysegar\n')
    for i in range(len(termekek)):
        file.write(f'{termekek[i]};{mennyiseg[i]};{egysegar[i]}')
        if i<len(termekek)-1:
            file.write('\n')
    file.close()

def deleteTermek():
    system('cls')
    print('Termék törlése\n')
    termek=input('A törlendő termék megnevezése: ')
    if termek in termekek:  
        termekek.remove(termek) 
        mentesFajlba()
        input('Termék. Tovább...')
    else:
        input('Nincs ilyen termék. Tovább...')


def termekhozzaadas():
    system('cls')
    print('-------Új termék-------')
    termek=input('Nevezze meg a terméket, amit a listáhot szeretne adni!: ')
    mennyiseg=input('Adja meg a termék mennyiségét!: ')
    egysegar=input('Adja meg a termék egységárát!:')
    adatokmentese(termek,mennyiseg,egysegar)
    input('Sikeres felvétel.Tovább..')

def adatokmentese(termek,mennyiseg,egysegar):
    file=open(filename, 'a', encoding='utf-8')
    file.write(f'\n{termek};{mennyiseg};{egysegar}')
    file.close


