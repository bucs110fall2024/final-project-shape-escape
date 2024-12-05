import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "square":
            square_frame = pygame.image.load("assets/square.png").convert_alpha()
            self.frame = self.square_frame
            y_pos = random.ranint(0,200)
        else:
            circle_frame = pygame.image.load("assets/circle.png").convert_alpha() #converts image to pygame friendly file while also removing alpha values (black and white behind pic)
            self.frame = self.circle_frame
            y_pos = random.randint(201,400)
        
        self.animation_index = 0
        self.rect = self.frame.get_rect(midbottom = (random.randint(900,1100), y_pos))
        
    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


      