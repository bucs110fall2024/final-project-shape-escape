from src.player import Player
from src.enemy import Enemy
from src.cloud import Cloud
import pygame

class Controller:

    def __init__(self):
        pygame.init()
        pygame.event.pump()

        self.screen = pygame.display.set_mode()

        self.p1 = Player()
        self.p2 = Player()
        self.clouds = pygame.sprite.Group()
        for i in range(3):
             c = Cloud()
             self.clouds.add(c)

        self.enemies = pygame.sprite.Group()
        for i in range(3):
             e = Enemy()
             self.enemies.add(c)

    def mainloop(self):

            #1: event loop
            for event in pygame.events.get():
                if event.type == pygame.QUIT:
                    pygane.quit()
                    exit()
                ## handle any important events ##
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     self.player.is_jumping_up = True
            enemies = pygame.sprite.spritecollide(player, self.enemies, False)
            for enemy in enemies:
            #2: Updates
            self.player.jump()
            
            #3: Redraw
            self.clouds.draw()
            # completely overlay the screen
            self.background = pygame.image.load("assets/background.png")
            self.screen.blit(self.background, (0, 0))
            #4: Display
