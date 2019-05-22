def cargar_datos(cant_art):
	band=False
	with open('sucursales.csv') as f:
		reader = csv.reader(f, delimiter=";")
		for row in reader:
			if not band:
				band=True
			else: sucursales.append([int(row[0]),row[1],row[2]])				
	band=False;cant_art=0
	with open('articulos.csv', encoding="utf8") as f:
		reader = csv.reader(f, delimiter=";")
		for row in reader:
			if not band:
				band=True		
			else: 
					productos.append([int(row[0]),row[1],row[2],float(row[3])])
					cant_art=cant_art+1
	band=False
	with open('artxsuc.csv') as f:
		reader = csv.reader(f, delimiter=";")
		for row in reader:
			if not band:
				band=True		
			else: prodxsuc.append([int(row[0]),int(row[1]),int(row[2]),int(row[3])])
	return cant_art

import csv
from datetime import datetime
nom=1;suc=1;dire=2;desc=2;prod=2;prec=3;cant=3;cant_art=0
sucursales=[];productos=[];prodxsuc=[]
cant_art=cargar_datos(cant_art)

#los archivos csv solo los uso para cargar los datos, en el programa elegí usar listas

input('presione enter para comenzar')
instanteInicial = datetime.now()

cont=0
print('\n\nLista de productos que en alguna sucursal poseen stock 0 y en alguna otra posee stock mayor que 5:\n\n')
for i in productos:
	band=False;band2=False
	for j in sucursales:
		if (prodxsuc[((j[0]-1)*cant_art+i[0])-1][cant]==0):
			band2=True
		elif (prodxsuc[((j[0]-1)*cant_art+i[0])-1][cant]>5):
			band=True
		if (band and band2):
			print(i[desc],'\n')
			cont=cont+1
			break
print('se encontraron ',cont,' articulos')

#probé tambien recorriendo la lista de sucursales y de productos por sucursal pero eran mas lentos y repetian los articulos
#el programa solo lista los productos, para informar las sucursales que tiene stock 0 y 5 hay que hacer agregarle una lista nomas

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
print('\n'+'el programa tardó',tiempo.seconds+(tiempo.microseconds*0.000001),' segundos'+'\n')
input()


