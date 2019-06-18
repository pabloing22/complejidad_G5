from tabla import crear_tablas
from datetime import datetime
from exportar_tabla import exportar_tabla

def buscar_stock_cero(artxsuc):
	conj=set()
	cont=0
	for i in artxsuc:
		if i[cant]==0:
			conj.add(i[prod])
			cont=cont+1
	print('Hay ', cont,' productos sin stock en alguna sucursal\n')
	return conj

def buscar_stock_mayor_que_cinco(artxsuc,lista):
	resultado=[]
	for i in artxsuc:
		if (i[prod] in lista) and (i[cant]>5):
			resultado.append(i[prod])
			lista.remove(i[prod])
	return resultado

def listar_productos(articulos,lista):
	cont=0
	for i in lista:
		print(articulos[i-1][nom])
		cont=cont+1
	print('\nDe los productos sin stock se encontraron ',cont,' articulos con stock mayor que cinco en alguna otra sucursal')

nom=1;suc=1;desc=2;prod=2;prec=3;cant=3;cant_art=0
tablas=crear_tablas(50000,5,500,450)
#creo una tabla aleatoria pasando como parametro:
#la cantidad de productos en total 
#la cantidad de sucursales
#la cantidad de productos que quiero que tengan stock cero
#la cantidad de productos con stock cero que quiero que tengan mas de cinco en stock en otra sucursal)

#elijo la cantidad de productos con stock cero y demas para despues saber si el programa los detecta y los cuenta bien
#en tabla.py se puede ver como genera las tablas

articulos=tablas[0]
sucursales=tablas[1]
artxsuc=tablas[2]

input('presione enter para comenzar')
instanteInicial = datetime.now()

lista=buscar_stock_cero(artxsuc)
lista=buscar_stock_mayor_que_cinco(artxsuc,lista)
listar_productos(articulos,lista)

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
print('\n'+'el programa tardó',tiempo.seconds+(tiempo.microseconds*0.000001),' segundos'+'\n')

exportar_tabla(articulos,sucursales,artxsuc)
#al final exporta las tablas arbitrarias que habia generado al principio por si quiero comprobar que listo son correctos