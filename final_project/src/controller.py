import pygame
from src.player import Player
from src.obstacle import Obstacle
import random

class Controller:
    def __init__(self):
        pygame.init() #starts pygame and initiates all sub-parts, must be put before any other pygame command, opposite to pygame.quit()
        self.screen = pygame.display.set_mode((800,400)) #creates the screen with ((width, height))
        pygame.display.set_caption("Shape Escape") #names game screen tab
        self.clock = pygame.time.Clock() #creates a clock to establish time in the game
        self.none = pygame.font.Font(None, 50)#creates font with (font_type, size)
        self.game_active = False
        self.start_time = 0
        self.score = 0

        #Groups 
        self.player_group = pygame.sprite.GroupSingle()
        self.p1 = Player()
        self.player_group.add(self.p1)

        self.obstacle_group = pygame.sprite.Group()

        self.sky_surf = pygame.transform.scale_by(pygame.image.load("final_project/assets/Sky.jpeg").convert_alpha(), (0.4, 0.4))

        #intro screen
        self.player_stand = pygame.transform.scale_by(pygame.image.load("final_project/assets/triangle.png").convert_alpha(), (0.15, 0.15))
        self.player_stand_rect = self.player_stand.get_rect(center = (400,200))

        self.game_name = self.none.render("Shape Escape", False, (111,196,169))
        self.game_name_rect = self.game_name.get_rect(center = (400,80))

        self.game_message = self.none.render("Press Space To Run", False, (111,196,169))
        self.game_message_rect = self.game_message.get_rect(center = (400,320))

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1 # makes a new game event
        pygame.time.set_timer(self.obstacle_timer, 1500) #(event you want to trigger, how often by milliseconds)
        
    def display_score(self):
        
        current_time = int((pygame.time.get_ticks()/100) - int(self.start_time))# gives time in milliseconds
        score_num_surf = self.none.render(f"Score: {current_time}", False, (64, 64, 64))
        score_num_rect = score_num_surf.get_rect(center = (400, 50))
        pygame.draw.rect(self.screen, "#c0e8ec", score_num_rect)
        self.screen.blit(score_num_surf, score_num_rect)
        return current_time

    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.p1, self.obstacle_group, True):
            self.obstacle_group.empty() 
            return False
        else:
            return True

    def mainloop(self):

        """
        runs the game

        Args:
        which key is pressed making the triangle move in that direction

        Returns: 
        the new position of the player
        """
        while(True): 
#always true so the game will continue to run until it breaks the loop from the inside
#draw all our elementsx
#update everything
            for event in pygame.event.get(): #loops through all possible events
                if event.type == pygame.QUIT:
                    pygame.quit()#stops the game, opposite to pygame.init()
                    exit()#stops error caused by quitting python while while(True) is still running and trying to run pygame.display.update
                
                if self.game_active == False:
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_SPACE):
                            self.game_active=True
                            self.start_time = int((pygame.time.get_ticks())/100)

                if self.game_active:
                    if event.type == self.obstacle_timer:
                        self.obstacle_group.add(Obstacle(random.choice(["square", "circle", "circle", "circle"])))


            if self.game_active: #only runs if the game is active and not over
                self.screen.blit(self.sky_surf, (0,0))#puts one surface onto another (surface, position) #(0,0) for pygame is at the top left, not the middle or bottom left
                self.score = self.display_score()

                self.player_group.draw(self.screen)
                self.player_group.update()

                self.obstacle_group.draw(self.screen)
                self.obstacle_group.update()

                # collision, stops game if snail touches player
                self.game_active = self.collision_sprite()
            else: #changes screen when you lose
                self.screen.fill((94, 129, 162)) 
                self.screen.blit(self.player_stand, self.player_stand_rect)

                score_message = self.none.render(f"your score: {self.score}", False, (111, 196, 169))
                score_message_rect = score_message.get_rect(center=(400,330))

                self.screen.blit(self.game_name, self.game_name_rect)

                if self.score == 0:
                    self.screen.blit(self.game_message, self.game_message_rect)
                else:
                    self.screen.blit(score_message, score_message_rect)

            pygame.display.update() #updates the display/makes the new updated frames
            self.clock.tick(60)#the while loop should not run more than 60 times per second, (60 fps)