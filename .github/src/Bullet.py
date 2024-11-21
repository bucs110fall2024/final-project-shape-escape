import pygame
from src.Game import Game
import sys
import random

pygame.init()

class Bullet(pygame.sprite.Sprite):
      def __init__(self, img="assets/bullet.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange
        self.rect.y = random.randrange