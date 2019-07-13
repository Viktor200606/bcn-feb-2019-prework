print("Autobús\n\n"
      "Este autobús tiene un sistema de control de entrada \n"
      "y salida de pasajeros para monitorear el número de ocupantes que transporta y, \n"
      "por lo tanto, detectar cuándo hay una capacidad demasiado alta.\n"
      "En cada parada, la entrada y salida de los pasajeros está representada por una tupla \n"
      "que consta de dos números enteros.\n"
      "bus_stop = (in, out)\n"
      "La sucesión de paradas está representada por una lista de estas tuplas.\n"
      "stops  = [(in1, out1), (in2, out2), (in3, out3), (in4, out4)]\n")


stops = []
n_pasajeros=[]
pasajeros=0
bus_stop = [0,0]
n_stop=int(input("Ingresa el numero de paradas "))

i=0
while i<n_stop:
    print("En la parada ", i+1, "¿Cúantos pasajeron entraron?")
    bus_stop[0]=int(input())
    bus_stop[1]=int(input("¿Cúantos pasajeron salieron?\n"))
    a=tuple(bus_stop)
    stops.append(a)
    pasajeros=pasajeros+bus_stop[0]-bus_stop[1]
    n_pasajeros.append(pasajeros)
    i+=1

print("\nstops = ", stops)
print("numero de pasajeros en cada parada = ", n_pasajeros)

print("Ocupación máxima del autobús ", max(n_pasajeros))

media=sum(n_pasajeros)/len(n_pasajeros)
print("Ocupación media del autobus ", media)

varianza=0
for i in n_pasajeros:
    varianza=varianza+((i-media)**2)
varianza=varianza/(len(n_pasajeros)-1)
import math
print("Desviación estándar del autobus ", math.sqrt(varianza))
