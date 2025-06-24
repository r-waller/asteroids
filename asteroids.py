from typing import override
import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White",(self.position.x, self.position.y), self.radius, 2) 

    def update(self, dt):
        self.position += (self.velocity * dt)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen):
        return super().draw(screen)

    @override
    def update(self, dt):
        return super().update(dt)
