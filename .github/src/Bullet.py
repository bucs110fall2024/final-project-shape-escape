import pygame
from src.Game import Game
import sys
import random

pygame.init()

class Bullet(pygame.sprite.Sprite):
      def __init__(self, x, y, img="assets/bullet.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

