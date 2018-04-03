mialbum.pdf : datos.txt graficar.py
	python graficar.py

datos.txt : monas
	./monas > datos.txt

monas:
	c++ album.cpp -o monas
