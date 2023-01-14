#Subiect 1:
def citire_numere(file): #a)
    lista = []
    with open(file) as f:
        for line in f.readlines():
                line = [int(nr) for nr in line.split()]
                lista.append(line)
        return lista

def prelucrare_lista(lista): #b)
    for poz in range(len(lista)):
        minim = min(lista[poz])
        counter_min = lista[poz].count(minim)
        for x in range(counter_min):
            lista[poz].remove(minim)
            
    m = min([len(lista[poz]) for poz in range(len(lista))])
    for poz in range(len(lista)):
        lung_rand = len(lista)
        for x in range(m+1, len(lista[poz])+1):
            lista[poz].pop(len(lista[poz])-1)


#c)
matrice = citire_numere("numere.in")
prelucrare_lista(matrice)
for linie in matrice:
    print(*linie)
#------

#d)
k = int(input("k: "))
lista_k = []
for linie in matrice:
    for x in linie:
        if len(str(x)) == k:
            lista_k.append(x)


if lista_k == []:
    print("Imposibil!")
else:
    print_place = open("cifre.out","a")
    print(lista_k)
    string = " ".join(sorted(set([str(x) for x in lista_k]),reverse = True))
    print_place.write(string)
#------
