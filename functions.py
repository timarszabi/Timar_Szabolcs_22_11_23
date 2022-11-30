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
        print(f'\t{termekek[i]} - {mennyiseg[i]} darab')
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
    print(f'\tTermékek listája: ')
    for i in range(0,len(termekek)):
        print(f'{i+1}. {termekek[i]} - {mennyiseg[i]} darab')
    termek=int(input('A törlendő termék sorszáma: '))
    
    termekek.pop(termek-1)
    mennyiseg.pop(termek-1)
    egysegar.pop(termek-1)
    mentesFajlba()
    input('Termék törölve a listáról. Tovább...')
    


def termekhozzaadas():
    system('cls')
    print('-------Új termék-------')
    bekerttermek=input('Nevezze meg a terméket, amit a listáhot szeretne adni!: ')
    bekertmennyiseg=input('Adja meg a termék mennyiségét!: ')
    bekertegysegar=input('Adja meg a termék egységárát!:')
    termekek.append(bekerttermek)
    mennyiseg.append(int(bekertmennyiseg))
    egysegar.append(int(bekertegysegar))
    adatokmentese(bekerttermek,bekertmennyiseg,bekertegysegar)
    input('Sikeres felvétel.Tovább..')

def adatokmentese(termek,mennyiseg,egysegar):
    file=open(filename, 'a', encoding='utf-8')
    file.write(f'\n{termek};{mennyiseg};{egysegar}')
    file.close


def listatorles():
    f = open('bevasarlo.csv', 'r+')
    f.truncate(0)
    visszair()
    input('A lista tartalma törölve.')
    

def visszair():
    f = open("bevasarlo.csv", "a")
    f.write("termekek;mennyiseg;egysegar")
    f.close()

def vegosszeg():
    vegosszeg=0
    for i in range(len(egysegar)):
        vegosszeg+=egysegar[i]*mennyiseg[i]
    print(f'A listán szereplő termékek együttes összege {vegosszeg} ft.')
    input('')
    
