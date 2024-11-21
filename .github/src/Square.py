import pygame
import sys

pygame.init()

width, height = 800, 600

class Square(pygame.sprite.Sprite):
      def __init__(self, x, y, img="assets/square.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
      
      def getx():
          return x
      
      def gety():
          return y


      