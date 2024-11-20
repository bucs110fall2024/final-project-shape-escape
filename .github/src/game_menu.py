import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 48
WHITE = (235, 212, 203)
PINK = (182, 70, 95)
BLACK = (44, 7, 3)
RED = (137, 6, 32)
BLUE = (0, 0, 255)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shape Escape")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Function to draw the menu
def draw_menu():
    screen.fill(BLACK)
    
    title_text = font.render("Shape Escape", True, WHITE)
    start_text = font.render("Start Game(S)", True, PINK)
    instructions_text = font.render("Instructions(I)", True, PINK)
    high_scores_text = font.render("High Scores(H)", True, PINK)
    exit_text = font.render("Exit(X)", True, RED)

    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 200))
    screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, 300))
    screen.blit(high_scores_text, (SCREEN_WIDTH // 2 - high_scores_text.get_width() // 2, 400))
    screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, 500))

    pygame.display.flip()

# Main menu loop
def menu_loop():
    while True:
        draw_menu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_s:
                    # You can implement the game start logic here
                    print("Starting the game...")
                    return
                elif event.key == pygame.K_i:
                    # Show instructions
                    print("Showing instructions...")
                elif event.key == pygame.K_h:
                    # Show high scores
                    print("Showing high scores...")
                elif event.key == pygame.K_x:
                    pygame.quit()
                    sys.exit()

# Run the menu loop
menu_loop()