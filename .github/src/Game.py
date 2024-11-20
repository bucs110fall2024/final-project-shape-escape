import pygame
import random
import pygame_menu


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        self.direction = "left"
        self.size = size
        
        self.image = pygame.Surface((size, size), pygame.SRCALPHA, 32).convert_alpha()
        self.rect = pygame.draw.circle(
                self.image,
                "yellow",
                (size/2, size/2),
                self.size/2,
            )
        self.rect.x = x
        self.rect.y = y

        

    def update(self):
        if self.direction == "left":
            self.rect.x -= 3
        else:
            self.rect.x += 3

class Controller:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.width, self.height = pygame.display.get_window_size()

        ## Bouncing Ball Model
        self.ball = Ball(self.width / 2, self.height / 2, 100)
        self.sprites = pygame.sprite.Group((self.ball,))

        self.state = "START"
        

    def mainloop(self):
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state =="END":
                self.endloop()

    def startloop(self):

        self.menu = pygame_menu.Menu("Shape Escape", self.width-20, self.height/2)
        # a label allows you to add text on the page
        self.menu.add.label("How long can you escape for", max_char=-1, font_size=14)
        #a button creates a button you can link to a method
        self.menu.add.button(
            'Start', 
            self.start_game, 
            align=pygame_menu.locals.ALIGN_CENTER
        )
        
        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "GAME"


            # pass events to the menu object
            self.menu.update(pygame.event.get())
            # You can draw the menu onto any surface
            # so if you want the menu in a specific place, 
            # create a surface in the location to draw the menu on
            self.menu.draw(self.screen)
            pygame.display.flip()

    def endloop(self):
        font_obj = pygame.font.SysFont(None, 48)
        msg = font_obj.render("You win! You may quit any time by closing the program", True, "yellow")
        
        while self.state == "END":

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        
            self.screen.blit(msg, (10, 10))
            pygame.display.flip()
        
                    
    def gameloop(self):

        while self.state == "GAME":

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ball.rect.collidepoint(event.pos):
                        self.state = "END"

            self.sprites.update()
            # adjust the direction of the ball based on position
            if self.ball.rect.x < 0:
                self.ball.direction = "right"
            elif self.ball.rect.x > (self.width - self.ball.rect.width):
                self.ball.direction = "left"
            
            self.screen.fill("purple")

            self.sprites.draw(self.screen)
            
            pygame.display.flip()


    def start_game(self):
        self.state = "GAME"

def main():
    game = Controller()
    game.mainloop()


if __name__ == "__main__":
    main()