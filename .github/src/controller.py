import pygame
from src.Player import Triangle
from src.Square import Square
from src.Game import Game
from src.Bullet import Bullet

class Controller:
    def __init__(self):
        
        pygame.init()
        pygame.event.pump()

        self.screen = pygame.display.set_mode()
        
        triangle = Triangle(0,0)

    def mainloop(self):
        """
        runs the game

        Args:
        which key is pressed making the triangle move in that direction

        Returns: 
        the new position of the triangle
        """
        while(True): 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.triangle.left()
                    if event.key == pygame.K_RIGHT:
                        self.triangle.right()
                    if event.key == pygame.K_DOWN:
                        self.triangle.down()
                    if event.key == pygame.K_UP:
                        self.triangle.up()
            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()