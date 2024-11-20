import pygame
import Triangle
import Square
import Game
import Bullet

def mainloop(self):
   while(True): 
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()

      #2. detect collisions and update models

      #3. Redraw next frame

      #4. Display next frame
      pygame.display.flip()