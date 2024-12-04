import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2] 
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha() #converts image to pygame friendly file while also removing alpha values (black and white behind pic)
            snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        
        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.5
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


      