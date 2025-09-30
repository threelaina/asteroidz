import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, approaching):
        colliding = False
        r1 = self.radius
        r2 = approaching.radius
        distance = self.position.distance_to(approaching.position)
        if distance <= r1 + r2:
            print("distance between objects = " + str(distance))
            print("r1 + r2 = " + str(r1 + r2))
            colliding = True
        return colliding
