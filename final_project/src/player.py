import pygame
import src

class Player(pygame.sprite.Sprite):
    def __init__(self):       
        super().__init__()
        self.player_walk = pygame.transform.scale_by(pygame.image.load("final_project/assets/triangle.png").convert_alpha(), (0.06, 0.06))     
        self.image = self.player_walk
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.y = self.rect.bottom

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -12

    def apply_gravity(self):
        self.gravity += 0.7
        self.rect.y += self.gravity

    def update(self):
        self.player_input()
        self.apply_gravity()

        if self.rect.bottom >=400:
            self.rect.bottom = 400
            
        if self.rect.top <= 0:
            self.rect.top = 0

