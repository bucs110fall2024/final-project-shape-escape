import pygame
from Player import Triangle
from Square import Square
import game_menu
from Bullet import Bullet
import random

class Controller:
    def __init__(self):
        
        pygame.init()
        pygame.event.pump()

        self.screen = pygame.display.set_mode()
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.triangle = Triangle(0,0)
        self.square = (random.randrange(-(game_menu.SCREEN_WIDTH), game_menu.SCREEN_WIDTH),random.randrange(-(game_menu.SCREEN_HEIGHT), game_menu.SCREEN_HEIGHT))
        self.all_sprites.add(square)

        self.bullet_time = pygame.time.get_ticks()  
        self.bullet_interval = 500

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
            current_time = pygame.time.get_ticks()  
            if current_time - self.bullet_time > self.bullet_interval:
                for i in range(4):
                    bullet = Bullet(square.getx(), square.gety(), i+1)
                    self.all_sprites.add(bullet)
                    self.bullets.add(bullet)
                bullet_timer = current_time
                
            self.all_sprites.update()

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()