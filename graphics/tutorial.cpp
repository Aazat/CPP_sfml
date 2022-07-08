#include <SFML/Graphics.hpp>
#include <iostream>

int main(){
	sf::RenderWindow window(sf::VideoMode(800, 600), "Graphics Window");

	sf::CircleShape shape(60.f);
	shape.setFillColor(sf::Color(100, 250, 50));
	//shape.setOrigin(800.f/2, 600.f/2);
	shape.setPosition(900.f/2, 600.f/2);

	sf::RectangleShape rectangle(sf::Vector2f(200.f, 200.f));
	rectangle.setFillColor(sf::Color::Magenta);
	rectangle.setPosition(0, 300.f/2);


	while(window.isOpen()){
		sf::Event event;
		while(window.pollEvent(event)){

			if(event.type ==  sf::Event::Closed){
				window.close();
			}
		}

		window.clear(sf::Color::Black);
		
		window.draw(shape);
		window.draw(rectangle);
		
		window.display();

	}
	std::cout << rectangle.getPosition().x << " : " << rectangle.getPosition().y << "\n";
	std::cout << shape.getPosition().x << " : " << shape.getPosition().y << "\n";
	std::cout << "Origin of Rectangle: "  << rectangle.getOrigin().x << " : " << rectangle.getOrigin().y << "\n";
	return 0;
}