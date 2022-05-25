import cv2

image = cv2.imread('figurasColores2.png')
#  Convertimos la imagen en escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#  Necesitamos identificar el contorno de cada una de las figuras geometricas, por lo tanto necesitamos una imagen binarizada para eso, usaremos (canny) que es un identificador de bordes 
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

#  Utilizamos la funcion cv2 findContours para poder encontrar los contornos externos
#_,cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4
#  En este paso dibujamos todos los contornos encontrados con la funcion anterior
#cv2.drawContours(image, cnts, -1, (0,255,0), 2)

#  Para poder trabajar con cada con torno encontrado utilizaremos un for donde (C) es un contorno 
for c in cnts:
	#  Esta funcion aproxima curvas con una precision especifica
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)
	#print(len(approx))
	x,y,w,h = cv2.boundingRect(approx)

	if len(approx)==3:
		cv2.putText(image,'Triangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio == 1:
			cv2.putText(image,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
		else:
			cv2.putText(image,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(image,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==6:
		cv2.putText(image,'Hexagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>10:
		cv2.putText(image,'Circulo', (x,y-5),1,1,(0,255,0),1)

	cv2.drawContours(image, [approx], 0, (0,255,0),2)
	cv2.imshow('image',image)
	cv2.waitKey(0)