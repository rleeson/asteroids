# this allows us to use code from the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import Player

def game_loop(screen, dt, drawable, updatable):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0

    updatable.update(dt)
    
    screen.fill("black")

    for entity in drawable:
        entity.draw(screen)

    pygame.display.flip()

    return 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        game_state = game_loop(screen, dt, drawable, updatable)
        dt = clock.tick(60) / 1000

        if game_state == 0:
            return

if __name__ == "__main__":
    main()
