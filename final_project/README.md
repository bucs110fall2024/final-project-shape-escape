Team Members
    - Jimmy Zou
    - Jordanny Ramos Rodriguez

Project Description
    A game where a triangle jumps to aviod other shapes that are trying to get them. While also avioding the obstacles in their way like flappy bird.

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

Test Case 1: Player Movement

Test Description: Verify that the player’s jump is moving as expected
Test Steps:
Start the game.
Press Spacebar
Verify that the player is moving up
Verify that the player also falls if they didn’t input jump
Expected Outcome: The player should be able to jump up and fall down when they don’t press a button.

Test Case 2: Collision Detection

Test Description: Ensure that collisions between the player and the shapes
Test Steps:
Start the game.
Jump and come in contact with the enemy
Verify that the player loses
Expected Outcome: The Player should lose when it comes in contact with the enemy

Test Case 3: Game Over Condition

Test Description: Confirm that the game ends when the player comes in contact with the enemy
Test Steps:
Start the game.
Jump into one of the moving shapes
Verify that the game displays a "Game Over" message.
Verify that the game also shows the score you’ve received at the end
Expected Outcome: The game should display a "Game Over" message with the score you’ve achieved when the player loses in the game

Test Case 4: Boundaries

Test Description: Confirm that the player does not fall off or jump over the screen
Test Steps:
Start the game.
Jump in the max height on the screen
Verify that the player hits the top and no longer can go higher
Fall into the bottom of the screen
Verify once the player makes contact with the floor and does not fall through the screen
Expected Outcome: The player should not die or fall through the screen upon hitting the roof or the floor

Test Case 5: The Score

Test Description: Verify the score would change depending on how long you stay in the level
Test Steps:
Start the game.
Play the game for 10 seconds
Verify the score is going up during the duration of you playing
Verify that the program is accurately displaying the score you’ve received upon death
Expected Outcome: The program should display the score once you die
