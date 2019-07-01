def exportar_tabla(articulos,sucursales,artxsuc):
	archivo1=open('articulos.csv','w')
	for i in articulos:
		archivo1.write(str(i[0]))
		archivo1.write(',')
		archivo1.write(i[1])
		archivo1.write(',')
		archivo1.write(i[2])
		archivo1.write(',')
		archivo1.write(str(i[2]))
		archivo1.write('\n')
	archivo2=open('sucursales.csv','w')
	for i in sucursales:
		archivo2.write(str(i[0]))
		archivo2.write(',')
		archivo2.write(i[1])
		archivo2.write('\n')
	archivo3=open('artxsuc.csv','w')
	for i in artxsuc:
		archivo3.write(str(i[0]))
		archivo3.write(',')
		archivo3.write(str(i[1]))
		archivo3.write(',')
		archivo3.write(str(i[2]))
		archivo3.write(',')
		archivo3.write(str(i[2]))
		archivo3.write('\n')
	archivo1.close()
	archivo2.close()
	archivo3.close()



