import pygame
from Player import Triangle
from Square import Square
import game_menu
from Bullet import Bullet
import random

class Controller:
    def __init__(self):
        pygame.init() #starts pygame and initiates all sub-parts, must be put before any other pygame command, opposite to pygame.quit()
        screen = pygame.display.set_mode((800,400)) #creates the screen with ((width, height))
        pygame.display.set_caption("My First Game") #names game screen tab
        clock = pygame.time.Clock() #creates a clock to establish time in the game
        test_font = pygame.font.Font("font/Pixeltype.ttf", 50)#creates font with (font_type, size)
        game_active = False
        start_time = 0
        score = 0

        #Groups 
        player_group = pygame.sprite.GroupSingle()
        p1 = Player()
        player_group.add(p1)

        obstacle_group = pygame.sprite.Group()

        sky_surf = pygame.image.load("graphics/Sky.png").convert() #converts to file pygame can work with more easily
        ground_surf = pygame.image.load("graphics/Ground.png").convert()

        #intro screen
        player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
        player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #transforms the surface (surface, rotate, scale)
        player_stand_rect = player_stand.get_rect(center = (400,200))

        game_name = test_font.render("Shape Escape", False, (111,196,169))
        game_name_rect = game_name.get_rect(center = (400,80))

        game_message = test_font.render("Press Space To Run", False, (111,196,169))
        game_message_rect = game_message.get_rect(center = (400,320))

        # Timer
        obstacle_timer = pygame.USEREVENT + 1 # makes a new game event
        pygame.time.set_timer(obstacle_timer, 1500) #(event you want to trigger, how often by milliseconds)

    def display_score():

        current_time = int((pygame.time.get_ticks()/100) - start_time)# gives time in milliseconds
        score_num_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
        score_num_rect = score_num_surf.get_rect(center = (400, 50))
        pygame.draw.rect(screen, "#c0e8ec", score_num_rect)
        screen.blit(score_num_surf, score_num_rect)
        return current_time

    def collision_sprite():
        if pygame.sprite.spritecollide(p1, obstacle_group, True):
            obstacle_group.empty() 
            return False
        else:
            return True

    def mainloop(self):    
        while(True): 
            for event in pygame.event.get(): #loops through all possible events
                if event.type == pygame.QUIT:
                    pygame.quit()#stops the game, opposite to pygame.init()
                    exit()#stops error caused by quitting python while while(True) is still running and trying to run pygame.display.update

                if game_active == False:
                    if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_SPACE):
                            game_active=True
                            start_time = int(pygame.time.get_ticks())/100

                if game_active:
                    if event.type == obstacle_timer:
                        obstacle_group.add(Obstacle(random.choice(["fly", "snail", "snail", "snail"])))

            if game_active: #only runs if the game is active and not over
                screen.blit(sky_surf, (0,0))#puts one surface onto another (surface, position) #(0,0) for pygame is at the top left, not the middle or bottom left
                screen.blit(ground_surf, (0, 300))#would go in front the sky image as it is made after
                score = display_score()

                player_group.draw(screen)
                player_group.update()

                obstacle_group.draw(screen)
                obstacle_group.update()

                # collision, stops game if snail touches player
                game_active = collision_sprite()
            else: #changes screen when you lose
                screen.fill((94, 129, 162)) 
                screen.blit(player_stand, player_stand_rect)

                score_message = test_font.render(f"your score: {score}", False, (111, 196, 169))
                score_message_rect = score_message.get_rect(center=(400,330))

                screen.blit(game_name, game_name_rect)

                if score == 0:
                    screen.blit(game_message, game_message_rect)
                else:
                    screen.blit(score_message, score_message_rect)

            pygame.display.update() #updates the display/makes the new updated frames
            clock.tick(60)#the while loop should not run more than 60 times per second, (60 fps)