print("El caracol y el pozo\n\n"
      "Un caracol cae en el fondo de un pozo de 125 cm. "
      "\nCada día el caracol se eleva 30 cm. "
      "\nPero por la noche, mientras duerme, "
      "\nse desliza 20 cm porque las paredes están mojadas. "
      "\n\n¿Cuántos días se tarda en escapar del pozo?"
      "\nCONSEJO: http://puzzles.nigelcoldwell.co.uk/sixtytwo.htm")

altura_pozo=125
avance_diario=30
retroceso_nocturno=20
distancia_acumulada=avance_diario
dias=0

while distancia_acumulada < altura_pozo:
    dias += 1
    distancia_acumulada=distancia_acumulada-retroceso_nocturno+avance_diario
dias += 1
print('Dias =', dias)

print("\n\nBonus!!!!!!!!!!!!!!!!1\n\n"
      "La distancia recorrida por el caracol ahora está definida por una lista.\n"
      "avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]")

avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

print("\n¿Cuánto tiempo se tarda en salir del pozo?")
dias=0
distancia_acumulada=avance_cm[0]
for avance_diario in avance_cm[1:]:
    if distancia_acumulada < altura_pozo:
        dias += 1
        distancia_acumulada=distancia_acumulada-retroceso_nocturno+avance_diario
dias += 1
print('Dias =', dias)

print("\n¿Cuál es su desplazamiento máximo en un día? ¿Y su mínimo?")
print("Desplazamiento máximo = ", max(avance_cm))
print("Desplazamiento mínimo = ", min(avance_cm))

print("\n¿Cuál es su velocidad media durante el día?")
print("Velocidad media = ", sum(avance_cm)/len(avance_cm),"cm/dia")

print("\n¿Cuál es la desviación estándar de su desplazamiento durante el día?")
media=sum(avance_cm)/len(avance_cm)
varianza=0
for i in avance_cm:
    varianza=varianza+((i-media)**2)
varianza=varianza/(len(avance_cm)-1)
import math
print("La desviacion estandar es = ", math.sqrt(varianza))
