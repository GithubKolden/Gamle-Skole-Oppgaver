def innlesning():
    # LESER FRA FIL INN TIL LISTE
    try:
        liste = []
        varer = open('Varer.txt','r')
        vnr = varer.readline()

        while vnr != '':
            vnr = vnr.rstrip('\n')
            betegnelse = varer.readline().rstrip('\n')
            pris = varer.readline().rstrip('\n')
            kategori = varer.readline().rstrip('\n')
            hylle = varer.readline().rstrip('\n')
            liste += [[vnr,betegnelse,pris,kategori,hylle]]
            vnr = varer.readline()

        varer.close() 
        return liste
    
    except IOError:
        # FEILMELDING HVIS FIL IKKE FINNES
        print('\nFilen "Varer.txt" eksisterer ikke.')



def f1(v_liste,l_lengde):
    # SKRIVER UT VAREBESKRIVELSE MED HYLLEPLASS
    for i in range(0,l_lengde,1):
        print(
                '______________________________\n',
                'Vare:',v_liste[i][1],
                '\nHylle:',v_liste[i][4]
            )



def f2(v_liste,l_lengde):
    # SKRIVER UT ALLE VARER SOM IKKE ER HYLLEPLASSERTE(NULL)
    teller = 0

    for i in range(0,l_lengde,1):
        if v_liste[i][4] == 'NULL':
            print(
                    '______________________________\n',
                    'VNr:',v_liste[i][0],
                    '\nVare:',v_liste[i][1],
                    '\nPris:',v_liste[i][2],
                    '\nKategori:',v_liste[i][3],
                    '\nHylle:',v_liste[i][4]
                )
            teller = 1

    if teller == 0:
        print('Det finnes ingen varer som ikke er hylleplasserte (NULL)')



def f3(v_liste,l_lengde):
    # SKRIVER UT ALLE VARER MED BRUKEROPPGITT FORBOKSTAV
    bokstav = input('Skriv inn en bokstav: ')

    for i in range(0,l_lengde,1):
        if v_liste[i][1][0:1].lower() == bokstav.lower():
            print(
                    '______________________________',
                    '\nVNr:',v_liste[i][0],
                    '\nVare:',v_liste[i][1],
                    '\nPris:',v_liste[i][2],
                    '\nKategori:',v_liste[i][3],
                    '\nHylle:',v_liste[i][4]
                )



def f4(v_liste,l_lengde):
    # SKRIVER UT ALLE VARER I EN BRUKEROPPGITT KATEGORI
    teller = 0
    i_kategori = input('Skriv inn en kategori: ')

    for i in range(0,l_lengde,1):
        if v_liste[i][3].lower() == i_kategori.lower():
            print(
                '______________________________',
                '\nVNr:',v_liste[i][0],
                '\nVare:',v_liste[i][1],
                '\nPris:',v_liste[i][2],
                '\nKategori:',v_liste[i][3],
                '\nHylle:',v_liste[i][4]
                )
            teller = teller + 1
            
    if teller == 0:
        print('Det finnes ingen varer innen kategorien:',i_kategori)
    else:
        print('Det eksisterer',teller,'antall varer innen denne kategorien')



def f5(v_liste,l_lengde):
    # SKRIVER UT ALLE VARER SOM HAR EN PRIS I INTERVALLET [100,200]kr
    teller = 0

    for i in range(0,l_lengde,1):
        if float(v_liste[i][2]) >=100 and float(v_liste[i][2]) <= 200:
            print(
                    '______________________________',
                    '\nVNr:',v_liste[i][0],
                    '\nVare:',v_liste[i][1],
                    '\nPris:',v_liste[i][2],
                    '\nKategori:',v_liste[i][3],
                    '\nHylle:',v_liste[i][4]
                    )
            teller = 1

    if teller == 1:
        print('Det finnes ingen varer innen pris intervallet [100,200]kr')



def f6(v_liste,l_lengde):
    # SORTERER LISTE MED BOBLESORTERING M/ STOPPMERKE
    j = 1
    bytte = True

    while bytte == True:
        bytte = False
        for i in range(0,l_lengde-j,1):
            if v_liste[i][1].lower() > v_liste[i+1][1].lower():
                bytte = True
                temp = v_liste[i]
                v_liste[i] = v_liste[i+1]
                v_liste[i+1] = temp
        j = j + 1

    # SKRIVER SORTERT LISTE TIL FIL
    sortert_vare = open('SortertVare.txt','w')

    for x in range(0,l_lengde,1):
        sortert_vare.write(
            (v_liste[x][0]) + '\n' + 
            (v_liste[x][1]) + '\n' + 
            (v_liste[x][2]) + '\n' + 
            (v_liste[x][3]) + '\n' + 
            (v_liste[x][4]) + '\n')
        
    sortert_vare.close()

    # LESER INN LISTE FOR Å FÅ ORGINAL STRUKTUR
    innlesning()
    liste = innlesning()
    return liste



def main():
    innlesning()
    liste = innlesning()
    lengde = len(liste)
    fortsette = True

    while fortsette == True:
        # SKRIVER UT HOVEDMENY
        print(
                '\nHovedmeny:\n',
                '\n1 - Vise alle varer og hylleplass',
                '\n2 - Vise alle varer som ikke',
                '\n3 - Vise alle varer med betegnelse/varenavn som begynner på brukeroppgitt forbokstav',
                '\n4 - Vise alle varer i en brukeroppgitt kategori, med opptelling av antall varer',
                '\n5 - Vise alle varer som har en pris i intervallet [100,200]kr',
                '\n6 - Vise sortere liste og skrive til fi SortertVare.txt',
                '\n7 - Avslutt Program'
            )
        
        valg = int(input('\nHvilke operasjon skal gjøres? [1,2,3,4,5,6,7]: '))

        if valg == 1:
            f1(liste,lengde)
        
        elif valg == 2:
                f2(liste,lengde)
        elif valg == 3:
            f3(liste,lengde)

        elif valg == 4:
            f4(liste,lengde)

        elif valg == 5:
            f5(liste,lengde)

        elif valg == 6:
            f6(liste,lengde)
            liste = f6(liste,lengde)

        elif valg == 7:
            fortsette = False
            print('Avslutter Program...')

        else:
            print('Feil valg, prøv på nytt!')
            
main()