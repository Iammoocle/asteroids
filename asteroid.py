import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

        def draw(screen,radius):
            pygame.draw.circle(screen,'white',self.position,radius,LINE_WIDTH)
        
        def update(dt):
            self.position += (self.velocity * dt)