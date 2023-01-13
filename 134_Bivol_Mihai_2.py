def sterge_oare(dict, cinema,film,ore): #b)
    ore = [[int(x.split(":")[0]),int(x.split(":")[1])] for x in ore.split()]
    for ora in ore:
        dict[cinema.strip()][film.strip()].remove(ora)
    return dict[cinema.strip()][film.strip()]

def cinema_film(dict, *cinematografe, ora_minima, ora_maxima):#return (nume_film, nume_cinema, lista_de_ore)
    List = []
    print()
    ora_minima = [int(x) for x in ora_minima.split(":")]
    ora_maxima = [int(x) for x in ora_maxima.split(":")]
    for cinema in cinematografe:
        for movie in dict[cinema]:
            ore = []
            for time in dict[cinema][movie]:
                if time >= ora_minima and time <= ora_maxima:
                    hour_str = ":".join([str(x) for x in time])
                    if hour_str[-2:] == ':0':
                        hour_str += "0"
                    ore.append(hour_str)
                    
            if ore != []:
                List.append(tuple([movie, cinema, ore]))
    List = sorted(List, key = lambda x: (x[0], len(x[2])))
    return List



#dicitonarul: {nume_cinema: {nume_film: [ [ora,minut] ... [ora, minut] ], ....}}
dict_cinema = {} #a)
with open("cinema.in") as f:
    for rand in f.readlines():
        rand = [x.strip() for x in rand.split("%")]

        rand[-1] = rand[-1].strip("\n")

        #daca nu a mai aparut cinemaul pana acum
        if rand[0] not in dict_cinema:
            dict_cinema[rand[0]] = {rand[1]: [[int(x.split(":")[0]),int(x.split(":")[1])] for x in rand[2].split()]}

        else: #daca a mai aparut
            dict_cinema[rand[0]][rand[1]] = [[int(x.split(":")[0]),int(x.split(":")[1])] for x in rand[2].split()]

# f = input("film: ")
# c = input("cinematograf: ")
# o = input("ore: ")
# print(sterge_oare(dict_cinema, c,f,o)) #b)
print(dict_cinema)
#-----

#c)
print(cinema_film(dict_cinema, 'Cinema 1', 'Cinema 2', ora_minima='14:00',ora_maxima='20:00'))
