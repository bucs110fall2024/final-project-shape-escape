import pygame
import game_menu
import sys
import random

pygame.init()

class Bullet(pygame.sprite.Sprite):
      def __init__(self, x, y, num, img="assets/bullet.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.num = num
      def update(self, num):
        if(num == 1):
          self.rect.x += 10  
        if(num == 2):
          self.rect.y += 10  
        if(num == 3):
          self.rect.x -= 10  
        if(num == 4):
          self.rect.y -= 10 
        if self.rect.y < 0:
          self.kill()  # Remove from all sprite groups

