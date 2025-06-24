from typing import override
import pygame
from pygame.draw import circle
from circleshape import CircleShape
from constants import SHOT_RADIUS


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
        pygame.draw.circle(screen, "White",(self.position.x, self.position.y), SHOT_RADIUS, 2)

    @override
    def update(self, dt):
        self.position += (self.velocity * dt)
