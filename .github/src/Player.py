import pygame
import sys
import game_menu

pygame.init()

class Triangle(pygame.sprite.Sprite):
      def __init__(self, x, y, img="assets/triangle.png"):
        super().__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullets = []

      def right(self, distance=5):
            self.rect.x += distance
            
      def left(self, distance=5):
            self.rect.x -= distance

      def up(self, distance=5):
            self.rect.y += distance
            
      def down(self, distance=5):
            self.rect.y -= distance

      def update(self):
            if self.rect.x > game_menu.SCREEN_WIDTH:
                  self.rect.x = -50  
            elif self.rect.x < -50:
                  self.rect.x = game_menu.SCREEN_WIDTH

            if self.rect.y > game_menu.SCREEN_HEIGHT:
                  self.rect.y = -50  
            elif self.rect.y < -50:
                  self.rect.y = game_menu.SCREEN_HEIGHT