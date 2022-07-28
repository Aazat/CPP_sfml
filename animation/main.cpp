// SFML_sample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <SFML/Graphics.hpp>
#include <SFML/Window/Keyboard.hpp>

int main()
{
    sf::Clock clock;
	
	float window_width = 400, window_height = 200;
	float width = 5.f, height= 120.f;
	
	sf::RenderWindow window(sf::VideoMode(window_width, window_height), "SFML WORKS!");
	sf::RectangleShape shape(sf::Vector2f(width, height));
	//sf::RectangleShape shape_2(sf::Vector2f(width, height));
	
	float x_origin = 0.f, y_origin = 0.f, x_offset = 0.05, y_offset = 0;
	float num_frames = window_width / x_offset;
	float height_decrement = height / num_frames;
	y_offset = height_decrement;
	
	shape.setPosition(x_origin, y_origin);
	shape.setFillColor(sf::Color::Color(255,255,0));	// RGB values

	sf::Vector2f pos = shape.getPosition();
	
	
	while (window.isOpen()) {
		sf::Event event;
		while (window.pollEvent(event)) {
			if (event.type == sf::Event::Closed || sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
				window.close();
		}
		if (pos.x > window_width)
			window.close();
		window.clear();
		window.draw(shape);
		window.display();
		shape.move(x_offset, y_offset);
		pos = shape.getPosition();
		shape.setSize(sf::Vector2f(5.f, height));
		height = height - height_decrement;
	}

    sf::Time elapsed = clock.getElapsedTime();
    std::cout << "Time elapsed in seconds: " << elapsed.asSeconds() << "\n";
    clock.restart();
    return 0;
}
