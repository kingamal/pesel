print('Podaj numer pesel')
pesel = input()
# len() - ile znakow ma zmienna pesel
# pesel.isdigit() - sprawdza czy str sklada sie tylko z cyfr
while pesel:
    if len(pesel) == 11 and pesel.isdigit():
        dzien = pesel[4:6]
        miesiac = int(pesel[2:4])
        # po 2000 roku do miesiąca jest dodane 20
        if miesiac > 12:
            miesiac = miesiac - 20
            rok = '20' + pesel[0:2]
        else:
            rok = '19' + pesel[0:2]
        print(dzien, miesiac, rok)
        print('Podaj numer pesel')
        pesel = input()
    else:
        print('Pesel niepoprawny!')
        exit()
