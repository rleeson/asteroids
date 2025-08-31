# this allows us to use code from the open-source pygame library
# throughout this file
import pygame
from constants import * 

def game_loop(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0
    
    screen.fill("black")
    pygame.display.flip()

    return 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        game_state = game_loop(screen)

        if game_state == 0:
            return

if __name__ == "__main__":
    main()
