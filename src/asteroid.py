import pygame
import random
from circleshape import CircleShape
from constants import *


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
            return
        else:
            random_angle = random.uniform(20, 50)
            rotation_1 = self.velocity.rotate(random_angle)
            rotation_2 = self.velocity.rotate(-random_angle)

            neuwe_radius = self.radius - ASTEROID_MIN_RADIUS

            new_astroid_1 = Asteroid(self.position.x, self.position.y, neuwe_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, neuwe_radius)

            new_astroid_1.velocity = rotation_1 * 1.2
            new_asteroid_2.velocity = rotation_2 * 1.2
