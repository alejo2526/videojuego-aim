import pygame
import math
from app.constants import *

# esta se encarga de dibujar los objetivos y checar si les dan o no
class Target:
    def __init__(self, x, y, radius, disappearing=False, lifetime=2000):
        self.x = x
        self.y = y
        self.radius = radius
        self.disappearing = disappearing
        self.lifetime = lifetime
        self.creation_time = pygame.time.get_ticks()
   
        self.image = pygame.image.load("assets\sounds\pajaro.png")  
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))

    def draw(self, screen):
        
        image_x = self.x - self.radius
        image_y = self.y - self.radius
        screen.blit(self.image, (image_x, image_y))

    def check_hit(self, mouse_pos):
        distance = math.hypot(mouse_pos[0] - self.x, mouse_pos[1] - self.y)
        return distance <= self.radius

    def should_disappear(self):
        if self.disappearing:
            return pygame.time.get_ticks() - self.creation_time > self.lifetime
        return False