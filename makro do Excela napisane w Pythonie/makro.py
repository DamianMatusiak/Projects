# coding=utf-8
from datetime import datetime,date
from xlwings import Book
from matplotlib import pyplot as plt

def get_path(name):
    from os.path import realpath, dirname, join
    return join(dirname(realpath(__file__)), name)

def projekt():
    sheet_name = "Zakupy"
    wb = Book(r'Dane.xlsm')
    table = wb.sheets[sheet_name].range('A1').current_region
    [ids, dates, size, cost] = table.options(transpose=True).value
    ids = [int(x) for x in ids[1:]]             # ids będą liczbami całkowitymi (bez tej pętli byłyby typu float)
    dates_zakupy = [datetime.strptime(data, '%d.%m.%Y').date() for data in dates[1:]]
    size = size[1:]
    cost = cost[1:]
    
    sheet_name = "Klient"
    table = wb.sheets[sheet_name].range('A1').current_region
    [names, birth, ids_klient] = table.options(transpose=True).value
    names = names[1:]
    birth = [datetime.strptime(data, '%d-%m-%Y') for data in birth[1:]]
    ids_klient = [int(x) for x in ids_klient[1:]]
    
    firstnames,surnames,ages = [],[],[]
    names[0] = ' nancy\xa0  davolio\xa0'
    for i in range(0,len(birth)):
        ages.append(date.today().year - birth[i].year - ((date.today().month, date.today().day) < (birth[i].month, birth[i].day)))
    for data in names:
            # dzielimy napisy na spacjach, wyrzucamy puste, powiększamy 1. literę
            parts = [part.capitalize() for part in data.split(" ") if part]
            # zapamiętanie danych
            firstnames.append(" ".join(parts[:-1]))
            surnames.append(parts[-1])
    
    # 1. zadanie: -------------------------
    with open(get_path('zad1.htm'),'wb') as f:
        def pisz(tekst):
            tekst += "\r\n"
            f.write(tekst.encode("utf-8"))    
        pisz('<!DOCTYPE html>')
        pisz('<html lang="pl">')
        pisz('<head>')
        pisz('<meta charset="utf-8">')
        pisz('<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Gugi" rel="stylesheet">')
        pisz('<link rel="stylesheet" href="styl1.css">')
        pisz('<title>Posumowanie</title>')
        pisz('</head>')
        pisz('<body>')
        pisz('<nav>')
        pisz('<ul>')
        pisz('<li><a href="tabelka.htm">Tabelka</a></li>')
        pisz('<li><a href="wykres.htm">Wykres</a></li>')
        pisz('<li><a href="autor.htm">Autorzy</a></li>')
        pisz('</ul>')
        pisz('</nav>')
        pisz('<div class="card-container">')
        pisz('<div class="card">')
        pisz('<div class="front">')
        pisz('<h2>Touch me!</h2>')
        pisz('</div>')
        pisz('<div class="back">')
        pisz('<h1>Liczba klientów: '+str(len(set(ids)))+'</h1>')
        pisz('<h1>Całkowity obrót: '+str(round(sum(cost),2))+' zł</h1>')
        pisz('<h1>Ostatnia sprzedaż: '+str(max(dates_zakupy))+'</h1>')
        pisz('</div>')
        pisz('</div>')
        pisz('</div>')
        pisz('</body>')
        pisz('</html>')

    #--------------------------------------
    
    # 2. zadanie: -------------------------
    l = []
    for i in set(ids):
        l.extend([i,0,0,0])             # stworzenie listy na zadanie 2. przechowuje dane w sposób: [id_klienta , obecnosc_w_sklepie , ilosc_produktow , suma_pieniędy , id_klienta , obecnosc_w_sklepie , ilosc_produktow , suma_pieniędy itd.]
    
    for row in range(len(ids)):
        j = l.index(ids[row])
        l[j+1] += 1
        l[j+2] += size[row]
        l[j+3] += cost[row]             # uzupełnia listę o dane z excela
    #print(l)
    #for k in range(int(len(l)/4)):
        #print('ID: ',l[4*k],'Imię: ',firstnames[ids_klient.index(l[4*k])],'Nazwisko: ',surnames[ids_klient.index(l[4*k])],'Ile razy był w sklepie: ',l[4*k+1],'Ile produktów kupił: ',int(l[4*k+2]),'Ile pieniędzy zostawił: ',round(l[4*k+3],2),'zł')
    #--------------------------------------
    with open(get_path('Tabelka.htm'),'wb') as f:  
        pisz('<!DOCTYPE html>')
        pisz('<html lang="pl">')
        pisz('<head>')
        pisz('<meta charset="utf-8">')
        pisz('<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Gugi" rel="stylesheet">')
        pisz('<link rel="stylesheet" href="styl1.css">')
        pisz('<title>Tabelka</title>')
        pisz('</head>')
        pisz('<body>')
        pisz('<nav>')
        pisz('<ul>')
        pisz('<li><a href="zad1.htm">Podsumowanie</a></li>')
        pisz('<li><a href="wykres.htm">Wykres</a></li>')
        pisz('<li><a href="autor.htm">Autorzy</a></li>')
        pisz('</ul>')
        pisz('</nav>')
        pisz('<table>')
        
        # Nagłówki
        pisz('<tr>')
        pisz('<td>ID</td>')
        pisz('<td>Imię</td>')
        pisz('<td>Nazwisko</td>')
        pisz('<td>Wiek</td>')
        pisz('<td>Ile razy w sklepie</td>')
        pisz('<td>Suma produktów</td>')
        pisz('<td>Ilość pieniędzy</td>')
        pisz('</tr>')
        # Zawartość tabelki
        for k in range(int(len(l)/4)):
            pisz('<tr>')
            pisz('<th>'+str(l[4*k])+'</th>')
            pisz('<th>'+firstnames[ids_klient.index(l[4*k])]+'</th>')
            pisz('<th>'+surnames[ids_klient.index(l[4*k])]+'</th>')
            pisz('<th>'+str(ages[ids_klient.index(l[4*k])])+'</th>')
            pisz('<th>'+str(l[4*k+1])+'</th>')
            pisz('<th>'+str(int(l[4*k+2]))+'</th>')
            pisz('<th>'+str(round(l[4*k+3],2))+'zł</th>')
            pisz('</tr>')
        pisz('</table>')
        pisz('</body>')
        pisz('</html>')
        
    # Zadanie dodatkowe: ---------------------------------------
    d = {}
    for key in set(ages):
        d[key] = 0                                      # stworzenie słownika łączącego wiek i wydane pieniądze
    for i in range(int(len(l)/4)):
        age = ages[ids_klient.index(l[4*i])]            # wyszukanie wieku korzystając z id klienta z listy l
        d[age] += l[4*i+3]                              # dodanie pieniędzy do słownika
    for i in d:
        d[i] = d[i]/ages.count(i)
    x = list(d.keys())                          # zbiór X: wiek klienta
    y = list(d.values())                        # zbiór Y: suma wydanych pieniędzy dla danego wieku klienta
    plt.plot(x,y,'ro')
    plt.xlabel('wiek')
    plt.ylabel('Średnia kwota')
    plt.savefig(get_path('wykres.jpg'))
    print(get_path('wykres.jpg'))
    with open(get_path('wykres.htm'),'wb') as f:
        pisz('<!DOCTYPE html>')
        pisz('<html lang="pl">')
        pisz('<head>')
        pisz('<meta charset="utf-8">')
        pisz('<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Gugi" rel="stylesheet">')
        pisz('<link rel="stylesheet" href="styl1.css">')
        pisz('<title>Wykres</title>')
        pisz('</head>')
        pisz('<body>')
        pisz('<nav>')
        pisz('<ul>')
        pisz('<li><a href="zad1.htm">Podsumowanie</a></li>')
        pisz('<li><a href="Tabelka.htm">Tabelka</a></li>')
        pisz('<li><a href="autor.htm">Autorzy</a></li>')
        pisz('</ul>')
        pisz('</nav>')
     
        pisz('<img src="wykres.jpg" alt="Wykres" height="500" width="700">')
        pisz('</body>')
        pisz('</html>')
        
    with open(get_path('autor.htm'),'wb') as f:
        def pisz(tekst):
            tekst += "\r\n"
            f.write(tekst.encode("utf-8"))    
        pisz('<!DOCTYPE html>')
        pisz('<html lang="pl">')
        pisz('<head>')
        pisz('<meta charset="utf-8">')
        pisz('<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Gugi" rel="stylesheet">')
        pisz('<link rel="stylesheet" href="styl1.css">')
        pisz('<title>Autorzy</title>')
        pisz('</head>')
        pisz('<body>')
        pisz('<nav>')
        pisz('<ul>')
        pisz('<li><a href="tabelka.htm">Tabelka</a></li>')
        pisz('<li><a href="wykres.htm">Wykres</a></li>')
        pisz('<li><a href="zad1.htm">Podsumowanie</a></li>')
        pisz('</ul>')
        pisz('</nav>')
        pisz('<h3>Damian Matusiak</h3>')
        pisz('<h4>Numer indeksu: 243027</h4>')
        pisz('<a href="mailto:243027@student.pwr.edu.pl" target="_top">Napisz email</a>')
        pisz('<h3>Jakub Jasiński</h4>')
        pisz('<h4>Numer indeksu: 243019</h4>')
        pisz('<a href="mailto:243019@student.pwr.edu.pl" target="_top">Napisz email</a>')
        pisz('</body>')
        pisz('</html>')