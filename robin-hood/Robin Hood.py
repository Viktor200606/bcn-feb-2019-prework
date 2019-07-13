print("Robin Hood:\n"
      "Estamos en un concurso para ganar el concurso de tiro con arco en Sherwood. \n"
      "Con nuestro arco y flechas disparamos a un objetivo e intentamos golpear lo más cerca posible del centro.\n"
      "El centro del objetivo está representado por los valores (0, 0) en los ejes de coordenadas.\n"
      "Descripción:\n"
      "En el espacio bidimensional, un punto puede definirse por un par de valores que corresponden \n"
      "a la coordenada horizontal (x) y la coordenada vertical (y). El espacio se puede dividir en 4 zonas \n"
      "(cuadrantes): Q1, Q2, Q3, Q4. Cuyo único punto de unión es el punto (0, 0).\n"
      "Si un punto está en Q1, tanto su coordenada x como la y son positivas. Os dejo un enlace \n"
      "a wikipedia para familiarizaros con estos cuadrantes.\n"
      "https://en.wikipedia.org/wiki/Cartesian_coordinate_system\n"
      "https://en.wikipedia.org/wiki/Euclidean_distance\n"
      "Disparos\n"
      "puntos = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),\n"
      "          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),\n"
      "          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),\n"
      "          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]\n"
      "Tareas\n"
      "Robin Hood es famoso por golpear una flecha con otra flecha. ¿Lo obtuviste?\n"
      "Calcula cuántas flechas han caído en cada cuadrante.\n"
      "Encuentra el punto más cercano al centro. Calcula su distancia al centro.\n"
      "Si el objetivo tiene un radio de 9, calcule el número de flechas que deben recogerse en el bosque.\n")

puntos = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

print("1. Robin Hood es famoso por golpear una flecha con otra flecha. ¿Lo obtuviste?")
print("Robin Hood golpeo una flecha con otra flecha en los siguientes puntos: ")
i=0
for punto in puntos:
    p=puntos[:i]+puntos[i+1:]
    if puntos[i] in p:
        print(puntos[i])
    i += 1

print("\n2. Calcula cuántas flechas han caído en cada cuadrante.")
Q1=0
Q2=0
Q3=0
Q4=0
Q5=0
for punto in puntos:
    if punto[0]>0 and punto[1]>0:
        Q1+=1
    else:
        if punto[0]<0 and punto[1]>0:
            Q2+=1
        else:
            if punto[0]<0 and punto[1]<0:
                Q3+=1
            else:
                if punto[0]>0 and punto[1]<0:
                    Q4+=1
                else:
                    Q5+=1

print("Numero de flechas en Q1 = ", Q1)
print("Numero de flechas en Q2 = ", Q2)
print("Numero de flechas en Q3 = ", Q3)
print("Numero de flechas en Q4 = ", Q4)
print("Numero de flechas sobre algun eje = ", Q5)

print("\n3. Encuentra el punto más cercano al centro. Calcula su distancia al centro. \n"
      "Definir una función que calcula la distancia al centro puede ayudar.")
import math
def distancia (pun):
    return math.sqrt((pun[0]**2)+(pun[1]**2))

distancias=[]
for punto in puntos:
    distancias.append(distancia(punto))
m=min(distancias)
print("Los siguientes puntos tuvieron la misma distancia de", m, "unidades al centro del objetivo\n"
      " y fueron los que mas se acercaron: ")
for punto in puntos:
    if distancia(punto)==m:
        print(punto)

print("\n4. Si el objetivo tiene un radio de 9, \n"
      "calcule el número de flechas que deben ser recogidas en el bosque.")
a=0
for d in distancias:
    if 9<d:
        a+=1
print("El numero de flechas que deben ser recoginas en el bosque son: ",a)

