LIBS = -lsfml-graphics -lsfml-window -lsfml-system
default: animation-app

animation-app: main.o
	g++ main.o first.o -o animation-app $(LIBS)

main.o: first.o
	g++ -c main.cpp

first.o: first.cpp
	g++ -c first.cpp

clean:

run: animation-app
	./animation-app