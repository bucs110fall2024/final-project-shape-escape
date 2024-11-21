Team Members
    - Jimmy Zou
    - Jordanny Ramos Rodriguez

Project Description
    We plan to create a game similar to pacman but with shapes instead called shape escape. We will likely try to include different stages and weapons or power ups. The user plays as a triangle and tries to dodge bullets from squares and other shapes.

GUI Design - Initial Design

The Picture is in the assets foler.

Program Design - Features
    1. Start Menu
    2. Power Ups
    3. Obstacles
    4. Moving Character
    5. Different Characters

Bullet Class: Creates bullet objects which shoot out of squares from the top, right, left, and bottom at a set speed to try and hit the player.

Controller Class: Creates a player, runs the start screen, and creates a list for the bullets and the square that the bullets will shoot out of. Also sets a tick speed for how often more bullets will be shot out of the square. Also, establishes commands to help move the player depending on which arrow key is pressed and implements an update function to move the bullets and the player.

game_menu.py has a class to introduce the player to the game while having different actions to do from. Accessing the Instructions, Seeing the High Score, Exiting the Game, Starting the Game

Player.py has a class of Triangle and this acts like the player where you are able to control him and dodge the bullets

Square.py has a class of Square, squares are used as the enemies in Shape Escape and this has all their properties and their ability to shoot bullets
