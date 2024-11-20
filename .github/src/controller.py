import pygame
from Triangle import Triangle
from Square import Square
from Game import Game
from Bullet import Bullet

class Controller:
    def __init__(self):
        pygame.init()
        pygame.event.pump()

        self.screen = pygame.display.set_mode()
        
        triangle = Triangle(0,0)

    def mainloop(self):
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