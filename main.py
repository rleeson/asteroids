# this allows us to use code from the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player

def game_loop(screen, dt, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0
    
    screen.fill("black")
    player.update(dt)
    player.draw(screen)

    pygame.display.flip()

    return 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        game_state = game_loop(screen, dt, player)
        dt = clock.tick(60) / 1000

        if game_state == 0:
            return

if __name__ == "__main__":
    main()
