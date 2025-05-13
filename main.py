import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: { SCREEN_WIDTH }")
    print(f"Screen height: { SCREEN_HEIGHT }")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2) , (SCREEN_HEIGHT / 2))
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        screen.fill("black")
        for x in drawable:
            x.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
        main()

