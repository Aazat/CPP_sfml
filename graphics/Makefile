LIBS =-lsfml-graphics -lsfml-window -lsfml-system
default: tutorial-app

	
tutorial-app: tutorial.o
	g++ tutorial.o -o tutorial-app $(LIBS) 

tutorial.o: tutorial.cpp
	g++ -c tutorial.cpp 

clean:

run: tutorial-app
	./tutorial-app
