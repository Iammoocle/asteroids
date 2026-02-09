import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_state,log_event
import random


class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,LINE_WIDTH)
        
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event('asteroid_split')
            angle = random.uniform(20,50)
            vector1 = pygame.math.Vector2.rotate(self.velocity,angle)
            vector2 = pygame.math.Vector2.rotate(self.velocity,-angle)
            self.radius -= ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0],self.position[1],self.radius)
            new_asteroid2 = Asteroid(self.position[0],self.position[1],self.radius)
            new_asteroid1.velocity = vector1 * 1.2
            new_asteroid2.velocity = vector2 * 1.2