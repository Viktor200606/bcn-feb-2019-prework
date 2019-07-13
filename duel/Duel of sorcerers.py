print("Duelo de brujos\n\n"
      "Estás presenciando una batalla épica entre dos poderosos hechiceros: Gandalf y Saruman.\n"
      "Cada hechicero tiene 10 hechizos de poder variable en su mente y los van a lanzar uno tras otro. \n"
      "El ganador del duelo será el que gane más de esos enfrentamientos entre hechizos. \n"
      "Los hechizos se representan como una lista de 10 enteros cuyo valor es igual al poder del hechizo.\n"
      "gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]\n"
      "saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]\n"
      "Por ejemplo:\n"
      "Saruman gana el primer choque: 10 contra 23, gana 23\n"
      "El segundo choque gana Saruman: 11 contra 66, gana 66 etc.\n"
      "Creará dos variables, una para cada hechicero, donde se almacenará la suma de los choques ganados. \n"
      "Dependiendo de qué variable sea mayor al final del duelo, mostrarás uno de los siguientes tres \n"
      "resultados en la pantalla:\n"
      "Gandalf gana\n"
      "Saruman gana\n"
      "Empate\n")

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

gan=0
sar=0
i=0
for echizo in gandalf:
    if gandalf[i]<saruman[i]:
        sar += 1
    else:
        if gandalf[i]>saruman[i]:
            gan += 1
    i+=1

if gan<sar:
    print("Saruman gana\n\n")
else:
    if gan>sar:
        print("Gandalf gana\n\n")
    else :
        print("Empate\n\n")

print("Los hechizos ahora tienen un nombre y hay un diccionario que relaciona ese nombre con un poder.\n"
      "Un hechicero gana si logra ganar 3 choques de hechizos seguidos.\n"
      "Promedio de cada una de las listas de hechizos.\n"
      "Desviación estándar de cada una de las listas de hechizos.\n"
      "POTENCIA = {\n"
      "    'Bola de fuego': 50,\n"
      "    'Rayo': 40,\n"
      "    'Flecha mágica': 10\n"
      "    'Tentáculos Negros': 25,\n"
      "    'Contagio': 45\n"
      "}\n"
      "gandalf = ['Bola de fuego', 'Rayo', 'Rayo', 'Flecha mágica', 'Bola de fuego',\n"
      "           'Flecha mágica', 'Rayo', 'Bola de fuego', 'Bola de fuego', 'Bola de fuego']\n"
      "saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',\n"
      "           'Relámpago', 'Flecha mágica', 'Contagio', 'Flecha mágica', 'Flecha mágica']\n"
      "¡Buena suerte!\n")

POTENCIA = {
            'Bola de fuego': 50,
            'Rayo': 40,
            'Flecha mágica': 10,
            'Tentáculos Negros': 25,
            'Contagio': 45
           }
gandalf = ['Bola de fuego', 'Rayo', 'Rayo', 'Flecha mágica', 'Bola de fuego',
           'Flecha mágica', 'Rayo', 'Bola de fuego', 'Flecha mágica', 'Bola de fuego']
saruman = ['Contagio', 'Contagio', 'Tentáculos Negros', 'Bola de fuego', 'Tentáculos Negros',
           'Rayo', 'Flecha mágica', 'Contagio', 'Flecha mágica', 'Flecha mágica']

gan=0
sar=0
i=0
for echizo in gandalf:
    if POTENCIA[gandalf[i]]<POTENCIA[saruman[i]]:
        sar += 1
        gan = 0
        if sar==3:
            print("Saruman gana\n\n")
            break
    else:
        if POTENCIA[gandalf[i]]>POTENCIA[saruman[i]]:
            gan += 1
            sar = 0
            if gan==3:
                print("Gandalf gana\n\n")
                break
    i+=1

s=0
for echizo in gandalf:
    s=s+POTENCIA[echizo]
mg=s/len(gandalf)
print("\nPromedio de la lista de hechizos de gandalf = ", mg)

s=0
for echizo in saruman:
    s=s+POTENCIA[echizo]
ms=s/len(saruman)
print("Promedio de la lista de hechizos de saruman =", ms)

varianza=0
for echizo in gandalf:
    varianza=varianza+((POTENCIA[echizo]-mg)**2)
varianza=varianza/(len(gandalf)-1)
import math
print("Desviación estándar de la lista de hechizos de gandalf = ", math.sqrt(varianza))

varianza=0
for echizo in saruman:
    varianza=varianza+((POTENCIA[echizo]-ms)**2)
varianza=varianza/(len(saruman)-1)
print("Desviación estándar de la lista de hechizos de saruman = ", math.sqrt(varianza))



