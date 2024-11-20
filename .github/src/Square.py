import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")

clock = pygame.time.Clock()

class Square(pygame.sprite.Sprite):
      def __init__(self, x, y, img="assets/triangle.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y