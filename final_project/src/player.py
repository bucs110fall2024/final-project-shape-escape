import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):       
        super().__init__()
        self.player_walk = pygame.image.load("assets/triangle.png").convert_alpha()       
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

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