import json
with open("estructura.json") as fichero:
    datos=json.load(fichero)

#Mostar el menu:
def mostrarMenu():
    menu = '''Bien venido al menu
    1. Listar el numero de temporadas que tiene la serie
    2. Contar el numero de episodios que tiene la serie
    3. Mostar la puntuacion de un episodio
    4. Mostrar los episodios mayores a una puntuacion ingresada
    5. Mostrar la puntuacion media de la serie
    6.Salir del menu
    '''
    print(menu)

    while True:
        try:
            numero = int(input("Ingresame una opcion: "))
            while numero > 7 or numero <= 0:
                print("Debes ingresar un valor que este disponible")
                numero = int(input("Ingresame una opcion: "))
            break
        except ValueError:
            print ("Debes introducir un número")

    return numero

#Listar las temporadas que hay:

def numeroTemporadas():
    temporadas= []
    print("La temporadas que hay son: ")
    for var in datos["_embedded"]["episodes"]:
        if var["season"] not in temporadas:
            temporadas.append(var["season"])

    for var in temporadas:
        print("Temporada",var)

#Cuéntame el número de episodios que tiene la serie en total 

def numeroEpisodiosTotal():
    cont= 0
    print("El numero de episdios que tiene la serie")

    for var in datos["_embedded"]["episodes"]:
        cont += 1
    
    print("Tiene",cont,"episodios")

#Mostrar por pantalla la puntuación de un episodio para ello pedir por pantalla el nombre del episodio 

def puntuacionEpisodio():

    episodio = input("Ingresame el nombre del episodio: ")
    bandera = False

    for var in datos["_embedded"]["episodes"]:
        if episodio == var["name"]:
            print("La puntuacion del episodio",var["name"],"es de",var["rating"]["average"])
            bandera= True
    
    if bandera == False:
        print("El episodio introducido no existe")

#Muestrame los episodios con una puntuación mayor o igual a una pedida por el usuario y que me lo muestre por temporadas

def mayorPuntuacion():

    while True:
        try:
            puntuacion= float(input("Ingresame la puntuacion: "))
            break
        except ValueError:
            print ("Debes introducir un número")


    temporadas = {"1": [], "2": [], "3": [], "4": []}

    print("Los episodios que superan la puntuacion ingresada son: ")
    print()

    for var in datos["_embedded"]["episodes"]:
        if var["rating"]["average"] >= puntuacion:
            temporada = var["season"]
            temporadas[str(temporada)].append(var["name"])
    
    max_episodios = max(len(episodios) for episodios in temporadas.values())
    
    print(("{:<30}{:<30}{:<30}{:<30}".format("Temporada 1","Temporada 2","Temporada 3","Temporada 4")))

    for var in range(max_episodios):
        for temporada, episodios in temporadas.items():
            if var < len(episodios):
                print("{:<30}".format(episodios[var]), end="")
            else:
                print("{:<30}".format(""), end="")
        print()

#Calculame todas las notas que tiene los episodios y hazme la media de toda la serie

def calculoPuntuacion():
    puntacion = []
    cont = 0
    for var in datos["_embedded"]["episodes"]:
        puntacion.append(var["rating"]["average"])
        cont +=1
    
    print("La media de puntuacion que tiene la serie es de:", round(sum(puntacion)/cont,2))