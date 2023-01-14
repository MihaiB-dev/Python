# a) [0,5p] Scrieți o funcție citire_matrice cu un parametru reprezentând numele unui fișier care conține elementele unei matrice
# de numere naturale cu următoarea structură: pe linia i a fișierului sunt elementele de pe linia i a matricei separate printr-un
# spațiu (vezi exemplul de fișier de intrare la punctul c)). Funcția citește elementele matricei din fișierul cu numele dat ca parametru
# și returnează matricea cu aceste elemente.
# Dacă în fișierul de intrare numărul de numere de pe fiecare linie nu este același pentru toate liniile funcția va returna None.
# --------------------------------------------------------
def citire_matrice(file):
    f = open(file)
    Lista = []
    lenth = 0
    for rand in f.readlines():
        local = [int (x) for x in rand.split()]
        if lenth == 0:
            lenth = len(local)
        elif len(local) != lenth:
                return None
        Lista.append(local)

    f.close()
    return Lista
    
# b) [1,25p] Scrieți o funcție multimi care primește ca parametri (în această ordine):
# o matrice  și un număr variabil de numere naturale reprezentând indici ai liniilor din matrice
# (indicele primei linii din matrice este 0; indicii dați sunt mai mici decât numărul de linii ale matricei).
# Asociem fiecărei linii din matrice două mulțimi: mulțimea elementelor negative și mulțimea elementelor
# pozitive care au prima cifră egală cu ultima.

# Funcția returnează următoarele două mulțimi:

# - intersecția mulțimilor elementelor negative asociate liniilor corespunzătoare indicilor dați

# - reuniunea mulțimilor elementelor pozitive care au prima cifră egală cu ultima asociate liniilor corespunzătoare indicilor dați
def poz_neg(Matrice, *indici):
    elemente_poz = set()
    elemente_neg = set()
    for indice in indici: 
        local_poz = [x for x in Matrice[indice] if x >= 0 and str(x)[0] == str(x)[-1]] #numerele pozitive
        local_neg = [x for x in Matrice[indice] if x < 0]

        if elemente_neg == set():
            elemente_neg = set(local_neg)
        else:
            elemente_neg &= set(local_neg)

        for numar in local_poz:
            elemente_poz.add(numar)

    return elemente_neg, elemente_poz


# (elementele din reuniune sunt distincte două câte două, la fel și cele din intersecție)
# -----------------------------------------------------------
#c) [1,25p] Se dă fișierul "matrice.in" cu structura descrisă la punctul a).
# Folosind apeluri utile ale funcțiilor de la a) și b) să se citească matricea din fișierul “matrice.in”
# și să se afișeze pe ecran numerele pozitive cu prima cifră egală cu ultima care se află în fișier pe ultimele 3 linii
# (se vor afișa pe aceeași linie, separate prin spațiu, ordonate crescător), precum și numărul de elemente negative
# care se află atât pe prima cât și pe ultima linie din fișier.

#avem matricea citita in Matrice
Matrice = citire_matrice("matrice.in")
ceva,numere_pozitive = poz_neg(Matrice,len(Matrice)-1,len(Matrice)-2,len(Matrice)-3)
numere_negative,ceva = poz_neg(Matrice,0,len(Matrice)-1)
print(*sorted(numere_pozitive))
print(*sorted(numere_negative))
