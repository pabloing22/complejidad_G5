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
		print('idp: ',articulos[i-1][0],' - nombre: ',articulos[i-1][nom])
		cont=cont+1
	print('\nDe los productos sin stock se encontraron ',cont,' articulos con stock mayor que cinco en alguna otra sucursal')

nom=1;suc=1;prod=2;cant=3
cant_productos=50000;cant_sucursales=5;stock_cero=500;mas_de_cinco=450
tablas=crear_tablas(cant_productos,cant_sucursales,stock_cero,mas_de_cinco)

#elijo la cantidad de productos con stock cero y demas para despues saber si el programa los detecta y los cuenta bien
#en tabla.py se puede ver como genera las tablas

articulos=tablas[0]
sucursales=tablas[1]
artxsuc=tablas[2]

input('presione enter para comenzar')
instanteInicial = datetime.now()

lista=buscar_stock_cero(artxsuc)
lista=buscar_stock_mayor_que_cinco(artxsuc,lista)
listar_productos(articulos,lista.sort())

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
print('\n'+'el programa tardó',tiempo.seconds+(tiempo.microseconds*0.000001),' segundos'+'\n')

exportar_tabla(articulos,sucursales,artxsuc)
#al final exporta las tablas arbitrarias que habia generado al principio por si quiero comprobar que listo son correctos