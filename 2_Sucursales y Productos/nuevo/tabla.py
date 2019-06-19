def crear_tablas(cant_prod,cant_suc,stock_cero,mas_de_cinco):

	import numpy
	from random import randrange
	from random import choice
	from random import sample
	import string

	cant=3;prec=3;desc=2;nom=1;prod=0;suc=0
	sucursales=[];articulos=[];artxsuc=[]

	for i in range(cant_prod):
		articulos.append([None,None,None,None])
	for i in range(cant_suc):
		sucursales.append([None,None])
	for i in range(cant_prod*(cant_suc)):
		artxsuc.append([None,None,None,None])
	#cargo las tres listas con vacios
	
	lista=list((sample([x for x in range(1,cant_prod)],stock_cero)))
	#listo al azar los n articulos que tendran stock cero

	#accedo a los elementos de la lista artxsuc por el id que obtengo multiplicando la sucursal por la cantidad de productos por el producto actual
	#el "randrange(cant_suc)" busca una sucursal (del 0 al 4) al azar donde el producto tendra cantidad cero
	#para el primer producto de la primera sucursal seria 0 * (cantidad de productos) + 1 = 1, y asi con todos los demas 

	cont=0
	for i in lista:
		sucu=randrange(cant_suc)
		artxsuc[(sucu*cant_prod+i)-1][cant]=0#le pongo cantidad cero a esos n productos en una sucursal elegida aleatorialente
		if cont<mas_de_cinco:
			while True:
				sucu=randrange(cant_suc)
				if (artxsuc[(sucu*cant_prod+i)-1][cant]==None):#elijo otra sucursal le pongo cantidad 10 al mismo producto
					artxsuc[(sucu*cant_prod+i)-1][cant]=10
					break
		cont=cont+1
	for i in range(cant_prod):
		articulos[i][prod]=i+1
		articulos[i][nom]=choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)#genero nombres random
		articulos[i][desc]=choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)+choice(string.ascii_uppercase)
		articulos[i][prec]=randrange(1,101)+((randrange(0,100)*0.01))

	for i in range(cant_suc):
		for j in range(cant_prod):
				ID=(i*cant_prod+j)
				if artxsuc[ID][cant]==None:
					artxsuc[ID][cant]=randrange(1,6)
				artxsuc[ID][0]=ID+1
				artxsuc[ID][1]=i+1
				artxsuc[ID][2]=j+1

	for i in range(cant_suc):
		sucursales[i][suc]=1
		sucursales[i][nom]=('sucursal numero '+str(i))

	return (articulos,sucursales,artxsuc)