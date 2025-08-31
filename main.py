# this allows us to use code from the open-source pygame library
# throughout this file
import pygame
from constants import * 

def game_loop(screen):
    screen.fill("black")
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return;

        game_loop(screen)

if __name__ == "__main__":
    main()
