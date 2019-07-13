print("Temperatura del procesador\n\n"
      "Tenemos un sensor de temperatura en el procesador del servidor de nuestra empresa. \n"
      "Queremos analizar los datos proporcionados para determinar \n"
      "si debemos cambiar el sistema de enfriamiento por uno mejor. \n"
      "Es costoso y como analista de datos no podemos tomar decisiones sin una base.\n"
      "Proporcionamos las temperaturas medidas a lo largo de las 24 horas del día \n"
      "en una estructura de datos de tipo lista compuesta por 24 enteros:\n"
      "temperaturas_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,71,63,53,50,49,53,48,45,39 ]\n")

import matplotlib.pyplot as plt

#Las gráficas apreceran automáticamente incrustadas en el notebook
#%matplotlib inline

# Definir los datos eje x, eje y
temperaturas_C = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
horas = list(range(len(temperaturas_C)))

# gráfico
# Configurar las caracteristicas del grafico
plt.plot(horas, temperaturas_C, label = "Temperatura", linewidth = 4, color = "green")
plt.axhline(y=70, linewidth=1, color='r')
#Definir nombres de ejes y titulo
plt.xlabel('horas')
plt.ylabel('Temperatura ºC')
plt.title('Temperaturas de nuestro servidor a lo largo del día')
#Mostrar leyenda, cuadricula y figura
plt.legend()
plt.minorticks_on()
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.grid(b=True, which='minor', color='black', linestyle='-', alpha=0.2)
plt.show()

print("Problema\n"
      "Si el sensor detecta más de 4 horas con temperaturas superiores o iguales a 70ºC \n"
      "o cualquier temperatura superior a 80ºC o el promedio supera los 65ºC \n"
      "durante todo el día, debemos ordenar el cambio del sistema de enfriamiento \n"
      "para evitar dañar el procesador.\n"
      "Lo guiaremos paso a paso para que pueda tomar la decisión \n"
      "calculando algunos pasos intermedios:\n")

print("La Temperatura mínima que se registro es =", min(temperaturas_C))
print("La Temperatura maxima que se registro es =", max(temperaturas_C))
print("Las Temperaturas iguales o superiores a 70ºC son:")
for t in temperaturas_C:
      if 70 <= t:
            print(t)

print("La temperatura media a lo largo del día =", sum(temperaturas_C)/len(temperaturas_C))
print("\nSi hubiera una falla en el sensor a las 03:00 y no capturáramos los datos, \n"
      "¿cómo estimaría el valor que nos falta? \n"
      "Corregir ese valor en la lista de temperaturas.")

il=(((temperaturas_C[4]-temperaturas_C[2])/(horas[4]-horas[2]))*(horas[3]-horas[2]))+temperaturas_C[2]
temperaturas_C[3]=il
print("Ocupando el metodo de interpolacion lineal; el valor del sensor a las 3:00 \n"
      "deberia ser = ", il, "°c")
print("Lista de temperaturas corregida\nHoras\tTemperaturas °c")
for h in horas:
      print(horas[h],": 00\t\t", temperaturas_C[h])

print("Bonificación: nuestro personal de mantenimiento es de los Estados Unidos \n"
      "y no comprende el sistema métrico internacional. \n"
      "Pasar las temperaturas a grados Fahrenheit.\n"
      "Fórmula: F = 1.8 * C + 32\n"
      "web: https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature\n")
def conversion (tem):
      tem = (tem*9/5)+32
      return tem
temperaturas_f=[]
for t in temperaturas_C:
      temperaturas_f.append(conversion(t))
print("Lista de temperaturas convertidas a grados Fahrenheit\n"
      "Horas\tTemperaturas °F")
for h in horas:
      print(horas[h],": 00\t\t", temperaturas_f[h])

print("\nToma la decision\n"
      "Recuerde que si el sensor detecta \n"
      "más de 4 horas con temperaturas superiores o iguales a 70ºC o \n"
      "cualquier temperatura superior a 80ºC o \n"
      "el promedio fue superior a 65ºC a lo largo del día, \n"
      "debemos dar la orden de cambiar el sistema de enfriamiento \n"
      "para evitar el peligro de dañar el equipo\n")
i=0
media_c=sum(temperaturas_C)/len(temperaturas_C)
for t in temperaturas_C:
      if (65 < media_c):
          print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡VERDADERO: CAMBIAR EL SISTEMA DE ENFRIAMIENTO!!!!!!!!!!!!!!!")
          break

      if (80<t):
          print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡VERDADERO: CAMBIAR EL SISTEMA DE ENFRIAMIENTO!!!!!!!!!!!!!!!")
          break

      if 70<=t:
          i += 1
      if 4 < i:
          print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡VERDADERO: CAMBIAR EL SISTEMA DE ENFRIAMIENTO!!!!!!!!!!!!!!!")
          break

print("\nMejoras futuras\n")

print("Queremos las horas (no las temperaturas) cuya temperatura supero los 70ºC\n"
      "con la condición de que esas horas son más de 4 y consecutivas, \n"
      "no simplemente la suma de todo el conjunto. \n"
      "¿Se cumple esta condición?")
print("Si se cumplio en el siguiente conjunto de horas:")
i=0
f=0
for h in horas:
    if 70 < temperaturas_C[h]:
        f=h
        i += 1
    else:
          if 4 < i:
              print(horas[f+1-i:f+1])
              i=0

print("\nPromedio de cada una de las listas (ºC y ºF). ¿Cómo se relacionan?")
media_c=sum(temperaturas_C)/len(temperaturas_C)
print("Promedio de lista de temperaturas en °c", media_c)
media_f=sum(temperaturas_f)/len(temperaturas_f)
print("Promedio de lista de temperaturas en °F", media_f)
print("Se relacionan ya que practicamente son el mismo resultado uno en °c "
      "y el otro en °F\n")

print("Desviación estándar de cada una de las listas. ¿Cómo se relacionan?")
import math
varianza=0
for t in temperaturas_C:
    varianza=varianza+((t-media_c)**2)
varianza=varianza/(len(temperaturas_C)-1)
print("Desviación estándar lista °c = ", math.sqrt(varianza))

varianza=0
for t in temperaturas_f:
    varianza=varianza+((t-media_f)**2)
varianza=varianza/(len(temperaturas_f)-1)
print("Desviación estándar lista °F = ", math.sqrt(varianza))
print("Se relacionan las desviasiones ya que son proporcionales:\n"
      "la desviacion estandar de °F =  1.8 * desviacion estandar de °c\n"
      "Esto devido a la Fórmula: F = 1.8 * C + 32; el 32 ya no aparece \n"
      "devido a que se elimina en cada una de las diferencias de cuadrados dentro \n"
      "del calculo de la varianza")
