import pygame

class Player(pygame.sprite.Sprite): 
    def __init__ (self, name):
        super().__init__()

        self.name
        self.size = 'small'
        self.image = pygame.image.load('assets/(name).png')
        self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        is_jumping_up = False # "up"
        is_jumping_down = False # "down"

    def jump(self):
        if self.is_jumping:
            self.rect.y = 1
        elif self.is_jumping_down:
            self.rect.y=-1