from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", [self.position.x, self.position.y], self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        old_radius = self.radius
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            import random
            random_angle = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 = self.velocity.rotate(-random_angle)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            new_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_1.velocity = new_velocity_1 * 1.2 
            new_2.velocity = new_velocity_2 * 1.2







