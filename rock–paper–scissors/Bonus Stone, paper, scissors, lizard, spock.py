print("Bonus: Piedra, papel, tijeras, lagarto, spock\n"
      "Ahora comienza la mejora.\n"
      "http://www.samkass.com/theories/RPSSL.html\n"
      "https://www.youtube.com/watch?v=C7gneuyNLwE\n"
      "https://www.youtube.com/watch?v=2H6JkhtEz58\n"
      "Se le pedirá que implemente algunas mejoras \n"
      "con respecto al juego anterior simple. \n"
      "Además, el número de juegos (que debe ser ODD) \n"
      "se solicitará por consola hasta que se ingrese un número válido.\n")

import random
import math

opciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]
combates = [[0,2,1,1,2],
            [1,0,2,2,1],
            [2,1,0,1,2],
            [2,1,2,0,1],
            [1,2,1,2,0]]

partidas = 2
while partidas%2 == 0:
    partidas = int(input("Ingresa el numero Maximo de partidas que deseas contender.\n"
                         "Recuerde que debe ser un numero impar: \n"))
ganar = math.ceil(partidas/2)
print("Para ganar necesitas vencerme en ", ganar, "partidas de ", partidas)

def ordenador ():
    valor = random.choice(opciones)
    return valor

def usuario ():
    u = input("\nEscribe tu eleccion (piedra, papel, tijeras, lagarto, spock) y presiona enter: \n").lower()
    while u not in opciones:
        u = input("Eleccion incorrecta!!!!! Solo puedes elegir piedra, papel, tijeras, lagarto, spock\n"
                    "Escribe tu eleccion y presiona enter: \n").lower()
    return u

def combate(maquina,humano):
    resultado = combates[opciones.index(maquina)][opciones.index(humano)]
    return resultado

jugadas_o = [0]
jugadas_u = [0]
combat = [0]
burla = ["Empatamos", "Perdiste", "Ganaste"]
ganados=[0,0]
def puntuacion():
    o = ordenador()
    u = usuario()
    c = combate(o,u)
    jugadas_o.append(o)
    jugadas_u.append(u)
    combat.append(c)
    if c == 1:
        jugadas_o[0] += 1
    else:
        if c == 2:
            jugadas_u[0] += 1
        else:
            combat[0] += 1
    print("{:<12}".format("Ordenador"), "{:<12}".format("Usuario"), "{:<12}".format("Resultado"))
    j=1
    for i in jugadas_o[1:]:
        print("{:<12}".format(i),  "{:<12}".format(jugadas_u[j]), combat[j], burla[combat[j]])
        j += 1
    if jugadas_o[0] < jugadas_u[0]:
        print("Estas ganando llevas", jugadas_u[0], "y yo solo", jugadas_o[0] )
    else:
        if jugadas_o[0] > jugadas_u[0]:
            print("Estas PERDIENDO!!!!! llevas", jugadas_u[0], "y yo solo", jugadas_o[0] )
        else:
            print("Estamos empatados llevas", jugadas_u[0], "y yo solo", jugadas_o[0] )

    if jugadas_o[0] == ganar:
        print("¡¡¡¡¡¡¡¡Perdiste!!!!!!!!!!")
        ganados[1] +=1;
        print("\nEn total llevas ", ganados[0], "juego(s) ganado(s) y " ,ganados[1], "juego(s) perdido(s)")

    if jugadas_u[0] == ganar:
        print("¡¡¡¡¡¡¡¡Ganaste!!!!!!!!!!")
        ganados[0] +=1;
        print("\nEn total llevas ", ganados[0], "juego(s) ganado(s) y " ,ganados[1], "juego(s) perdido(s)")

ganadas=[0,0]
while jugadas_o[0] < ganar and jugadas_u[0] < ganar:
    puntuacion()
    if jugadas_o[0] >= ganar or jugadas_u[0] >= ganar:
        seguir = input("\n\nSi deseas jugar nuevamente presiona 1 y despues enter\n"
                       "de lo contrario solo presiona enter\n")
        if seguir == "1":
            partidas = 2
            while partidas%2 == 0:
                partidas = int(input("Ingresa el numero Maximo de partidas que deseas contender.\n"
                                     "Recuerde que debe ser un numero impar: \n"))
            ganar = math.ceil(partidas/2)
            print("Para ganar necesitas vencerme en ", ganar, "partidas de ", partidas)
            jugadas_o = [0]
            jugadas_u = [0]
            combat = [0]

