#Pentru un cuvânt c=s1...sn și un număr natural pozitiv k<n permutarea circulară la stânga cu k poziții a lui
# c este sk+1…sns1…sk . De exemplu, pentru k=2 și cuvântul arc se obține cuvântul car.

#) [1p] Scrieți o funcție permuta_cuvinte cu 2 parametri: prop, k (în această ordine),
# unde prop este o propoziție în care cuvintele sunt separate prin câte un spațiu, iar k este un număr natural pozitiv.
# Funcția returnează două valori:

#- propoziția obținută modificând propoziția prop astfel:
# fiecare cuvânt de lungime cel puțin k+1 este înlocuit cu permutarea sa la stânga cu k poziții

#- numărul de cuvinte modificate

def permuta_cuvinte(prop,k):
    propozitie = prop.split()
    contor = 0
    for poz in range(len(propozitie)):
        if len(propozitie[poz]) == k:
            pass
        else:
            propozitie[poz] = propozitie[poz][k-len(propozitie[poz]):] + propozitie[poz][0:k]
            contor +=1
    return " ".join(propozitie),contor

print(permuta_cuvinte("arc are merisaore dulci",2))
#b) [1p] Scrieți o funcție sub_medie cu un parametru, care primește ca parametru o
# listă de numere naturale și returnează două valori: media aritmetică a numerelor din listă
# (suma lor împărțită la numărul lor) precum și numărul de elemente din listă mai mici strict decât media;
# dacă lista este vidă atunci funcția va returna None.

def sub_medie(list):
    if list == []:
        return None
    media_ar = sum(list)/len(list)
    contor = len([x for x in list if x < media_ar])
    return media_ar, contor

#c) [1p] Se dă fișierul "circular.in" cu următoarea structură:

#- pe fiecare linie a fișierului se află o propoziție cu cuvintele separate prin câte un spațiu

#Se citește de la tastatură un număr natural k.  Folosind apeluri utile ale funcțiilor de la a) și b) să se rezolve următoarele cerințe:

#- să se creeze un nou fișier "circular.out" cu propozițiile din fișierul "circular.in"
# modificate astfel:  fiecare cuvânt de lungime cel puțin k+1 este înlocuit cu permutarea sa la stânga cu k poziții

#- să se afișeze pe ecran numărul mediu de modificări de pe o linie cu două zecimale
# (=media aritmetică a șirului format cu numărul de modificări de pe fiecare linie)
# și pe câte linii numărul de modificări a fost mai mic decât numărul mediu de modificări.

f = open("circular.in")
out = open("circular.out","a")
k = int(input("k: "))

list_schimbari =[]
for linie in f.readlines():
    propozitie, nr_schimbari = permuta_cuvinte(linie, k)

    out.write(propozitie)
    out.write("\n")
    list_schimbari.append(nr_schimbari)

media, linii_mai_mic = sub_medie(list_schimbari)
print(round(media,2), linii_mai_mic)

