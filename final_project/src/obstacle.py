import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "square":
            self.square_frame = pygame.transform.scale_by(pygame.image.load("final_project/assets/square.png").convert_alpha(), (0.15, 0.15))
            self.frame = self.square_frame
            y_pos = random.randint(0,200)
        else:
            self.circle_frame = pygame.transform.scale_by(pygame.image.load("final_project/assets/circle.png").convert_alpha(), (0.15, 0.15))
            self.frame = self.circle_frame
            y_pos = random.randint(201,400)
        self.rect = self.frame.get_rect(midbottom = (random.randint(900,1100), y_pos))
        
    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


      