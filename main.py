import pygame
from constants import *
from player import *


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add player to groups
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # display update
        dt = clock.tick(60) /1000 # Limit framerate to 60 FPS

if __name__ == "__main__":
    main()