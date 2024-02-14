from funciones import mostrarMenu,numeroTemporadas,numeroEpisodiosTotal,puntuacionEpisodio,mayorPuntuacion,calculoPuntuacion

bandera = True

while bandera == True:
    numero = mostrarMenu()
    print()
    if numero == 1:
        numeroTemporadas()
        print()
    elif numero == 2:
        numeroEpisodiosTotal()
        print()
    elif numero == 3:
        puntuacionEpisodio()
        print()
    elif numero == 4:
        mayorPuntuacion()
        print()
    elif numero == 5:
        calculoPuntuacion()
        print()
    elif numero == 6:
        bandera = False
