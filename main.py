import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black')

        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event('player_hit')
                print('Game Over!')
                sys.exit()

        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
