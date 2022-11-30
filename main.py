from functions import *

listabetoltes()

valasztas=''
while valasztas!='0':
    valasztas=menu()
    if valasztas=='1':
        listatorles()
    elif valasztas=='2':
        termeklista()
    elif valasztas=='3':
        termekhozzaadas()
    elif valasztas=='4':
        deleteTermek()
    elif valasztas=='5':
        Legvegso()
