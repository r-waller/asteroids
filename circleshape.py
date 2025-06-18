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
        pygame.draw.polygon(screen, "White", self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_detected(self, other_circle):
        # Two circles, need to calculate the distance between the center of both
        distance = self.position.distance_to(other_circle.position)
        # Need to know if distance is less than or equal to sum of radii. If true = collision. If false = not collision 
        return distance <= (self.radius + other_circle.radius)
