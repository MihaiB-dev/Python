
#Se dă fișierul “magazine.in” cu următoarea structură:

#Pe prima linie sunt două numere naturale m și n separate printr-un spațiu.
#Pe următoarele m linii sunt câte 2 valori separate prin spațiu reprezentând informații despre un magazin:
# codul (număr natural), numele unui magazin (format din unul sau mai multe cuvinte separate prin spațiu).
#Pe următoarele n linii sunt valori separate prin spațiu reprezentând 6 informații despre produse aflate
# în stocul magazinelor date anterior (un produs se găsește la un singur magazin):
# codul unui magazin (număr natural, dintre codurile date pe liniile 2, …, m+1),
# codul produsului (număr natural), numărul de bucăți aflate în stoc (număr natural),
# prețul produsului (număr real), greutatea produsului (număr natural), numele produsului (șir ce poate conține spații).

#a)      [1,25p] Să se memoreze datele din fișier într-o singură structură astfel încât să se răspundă cât mai eficient la cerințele b)
# (ștergerea unui produs având dat codul produsului și aflarea numelui unicului magazin unde se găsește acel produs)
# și c) (accesarea numelui unui magazin și a informațiilor despre toate produsele sale, având dat codul m

# { cod: { nume: " ", cod_produs: { bucati: .., pret: .., greutate: .., nume_prod:..}, ...} ... }
f = open("magazin.in")
dict_magazin = {}
linie = f.readline().split()
m = int(linie[0])
n = int(linie[1])
for x in range(m):
    linie = f.readline().split()
    dict_magazin[int(linie[0])]={'nume':" ".join([linie[x] for x in range(1,len(linie))])}
for x in range(n): 
    linie = f.readline().split() # linie[0] = cod, linie[1] = cod prod, linie[2]= bucati, linie[3] = pret, linie[4] = greutate, linie[5].. = nume_produs
    dict_magazin[int(linie[0])][int(linie[1])] = {'bucati': int(linie[2]), 'pret': float(linie[3]), 'greutate': int(linie[4]), 'nume_produs': " ".join([linie[x] for x in range(5, len(linie))])}

f.close()

print(dict_magazin)

#b)     [0,75p] Să se scrie o funcție sterge_produs cu 2 parametri:
# în primul parametru se transmite structura în care s-au memorat datele la cerința a),
# iar al doilea este codul unui produs, care șterge din structura de date primită toate informațiile
# legate de produsul cu codul dat ca parametru. Funcția returnează numele unicului magazin unde se găsește produsul,
# sau None dacă produsul nu se află în stocul niciunui magazin.

#Să se apeleze funcția pentru un cod de produs citit de la tastatură și să se afișeze pe ecran mesajul
#“Produsul se gasea la magazinul numit … .”, sau mesajul “Produsul nu exista.”
# dacă niciun magazin nu are în stoc produsul cu codul dat.
# Apoi să se afișeze pe ecran toată structura rămasă după ștergere, într-o formă convenabilă.
def sterge_produs(dict_magazin, cod_produs):
    keys = dict_magazin.keys()
    for key in keys:
        if cod_produs in dict_magazin[key]:
            dict_magazin[key].pop(cod_produs)
            return dict_magazin[key]['nume']
    return None

# cod = int(input("cod produs: "))
# magazin = sterge_produs(dict_magazin,cod)
# if magazin == None:
#     print("Produsul nu exista.")
# else:
#     print(f"Produsul se gasea la magazinul numit {magazin}.")

#c)      [1p] Să se scrie o funcție produse_magazin cu 2 parametri:
# în primul parametru se transmite structura în care s-au memorat datele la cerința a),
# iar al doilea este codul unui magazin. Funcția returnează numele magazinului și o listă
# cu informații despre produsele din stocul său (un element al listei fiind un tuplu ce conține:
# numele produsului, numărul de bucăți aflate în stocul acelui magazin, prețul, greutatea produsului),
# lista fiind sortată descrescător după numărul de bucăți, în caz de egalitate crescător după prețul unitar
# (raportul dintre preț și greutate), iar în caz de egalitate crescător după numele produsului.
# Funcția va returna o listă vidă dacă nu există un magazin cu codul primit ca parametru.

#Să se apeleze funcția pentru un cod de magazin citit de la tastatură și să se afișeze rezultatul returnat ca în exemplul de mai jos.
def produs_magazin(dict_magazin, cod_magazin):
    Lista_produse=[dict_magazin[cod_magazin]['nume'], [tuple(dict_magazin[cod_magazin][x].values()) for x in dict_magazin[cod_magazin] if type(x) == int]]
    Lista_produse[1].sort(key = lambda x: (-x[0], x[1]/x[2],x[3]))
    return Lista_produse

print(produs_magazin(dict_magazin, 1))
    

