import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return;

        new_size = self.radius - ASTEROID_MIN_RADIUS
        new_velocities = (
            self.velocity.rotate(random.uniform(20, 50)),
            self.velocity.rotate(-random.uniform(20, 50))
        )

        for velocity in new_velocities:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_size)
            new_asteroid.velocity = 1.2 * velocity
