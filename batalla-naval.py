import random
import os

def batalla_naval():
	mapa=[]
	fila=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

	for i in fila:
		mapa.append(fila.copy())

	def imprimir_mapa(mapa):
		t=len(mapa)
		for i in range(t):
			if t < len(mapa):
				print(t, "",mapa[i])
			else:
				print(t,mapa[i])
			t-=1
		print('',end='     ')
		for i in range(len(mapa)):
			print(i+1,end='    ')


	def cabe_en(fila):
		cabe=[]
		posicion=0
		largo=0
		for punto in fila:
			if punto == " ":
				largo += 1
				if posicion == len(fila)-1:
					cabe.append([posicion-largo+1, largo])
			else:
				if largo != 0:
					cabe.append([posicion-largo, largo])
				largo=0
			posicion += 1

		return cabe

	def transpuesta(mapa):
		mapa2=[]
		f=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
		for i in f:
			mapa2.append(fila.copy())
		k=0
		l=0

		for i in range(len(mapa2)):
			for j in range(len(f)):
				mapa2[i][j]=mapa[j][i]

		return mapa2

	barcos = [6,7,4]

	for b in barcos:
		f_c=random.choice(range(2))
		fila_elegida=random.choice(range(10))

		if f_c ==1:
			mapa=transpuesta(mapa)

		posicion_elegida=random.choice(cabe_en(mapa[fila_elegida]))

		while b >= posicion_elegida[1]:
			f_c=random.choice(range(2))
			fila_elegida=random.choice(range(10))
			if f_c ==1:
				mapa=transpuesta(mapa)
			posicion_elegida=random.choice(cabe_en(mapa[fila_elegida]))


		if b < posicion_elegida[1]:
			posicion_elegida[0] = random.choice(range(posicion_elegida[1]-b))+posicion_elegida[0]
			for i in range(b):
				mapa[fila_elegida][posicion_elegida[0]+i]='B'

	mapa_usuario=[]
	for i in fila:
		mapa_usuario.append(fila.copy())

	FILA=[9,8,7,6,5,4,3,2,1,0]

	torpedos=0
	vidas = 7
	tiro = 0
	error=0
	while torpedos<sum(barcos) and 0 < vidas:
		if error ==1:
			print("\n                       ERROR\n¡¡¡¡¡¡¡¡¡Ingresa valores enteros entre [1-10]!!!!!!!!!\n")
		if tiro == 1:
			if torpedo == 'B':
				print("\n¡¡¡¡¡¡¡¡¡Genial le diste a parte de un barco!!!!!!!!!!\n")
				torpedos += 1
				vidas += 1
				mapa_usuario[FILA[j]][i]='H'
			else:
				print("\n¡¡¡¡¡¡¡No le diste a ninguno sigue intentando!!!!!!!!\n")
				vidas -= 1

		print("              VAMOS  A JUGAR BATALLA NAVAL\n                    Tienes", vidas, "vidas\n                  Hunde mis 4 barcos")
		imprimir_mapa(mapa_usuario)
		#print("\n")
		#imprimir_mapa(mapa)

		try:
			i=int(input("\ningresa la coordenanda X donde deseas colocar un torpedo \n"))-1
			j=int(input("ingresa la coordenada Y donde deseas colocar un torpedo\n"))-1

			if i>9 or j>9:
				int("fallaste")

			torpedo=mapa[FILA[j]][i]
			mapa[FILA[j]][i]='X'
			mapa_usuario[FILA[j]][i]='X'
			tiro = 1
		except:
			error = 1

		if torpedos==sum(barcos)-1:
			for i in range(30):
				print("¡¡¡¡¡¡¡¡¡¡¡    FELICIDADS GANASTE   !!!!!!!!!!!!!!!!!!!")
			break
		if vidas == 1:
			for i in range(30):
				print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡    PERDEDOR    !!!!!!!!!!!!!!!!!!!!!!!")
			break

		os.system('clear')

denuevo = '1'
while denuevo == '1':
	batalla_naval()
	denuevo = input("\n\nIngresa 1 y presiona ENTER si deseas jugar de nuevo\nDe lo contrario presiona cualquier caracter y presiona ENTER\n\n")

